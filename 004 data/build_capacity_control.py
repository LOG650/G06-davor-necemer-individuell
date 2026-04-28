import argparse
import csv
import re
import zipfile
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import date, datetime
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
from xml.etree import ElementTree

from pypdf import PdfReader


BASE_DIR = Path(__file__).resolve().parent
RAW_OUTLOOK_DIR = BASE_DIR / "raw" / "outlook_exports"
PROCESSED_DIR = BASE_DIR / "processed" / "capacity_control"
PROCESS_TIME_OUTPUT = BASE_DIR / "process_time_matrix.csv"

KNOWN_ACTIONS = {"PD", "ED", "DD", "Undo"}
MAIN_PROCESS_MAP = {
    "PD": ("P1", "PD / for-klargjoering"),
    "ED": ("P2", "ED / endelig dispatch/ekspedering"),
}
SPREADSHEET_NS = {"main": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}

PRODUCTION_LINE_RE = re.compile(
    r"^(?P<quantity>[0-9][0-9.]*)\s*"
    r"(?P<unit>[A-Z]{2,4})\s+"
    r"(?P<plates>[0-9.]+,[0-9]{2})"
    r"(?P<description>.*)$"
)
SECTION_RE = re.compile(r"^(?P<section_no>\d{2})\s+(?P<section_name>.+)$")


@dataclass
class ProductionItem:
    source_file: str
    delivery_date: date
    written_at: datetime
    section_no: str
    section_name: str
    article_no: str
    unit: str
    quantity: int
    plates: Decimal


@dataclass
class ProductionList:
    path: Path
    delivery_date: date | None
    written_at: datetime | None
    pages: int
    items: list[ProductionItem] = field(default_factory=list)
    parse_warning: str = ""

    @property
    def source_file(self):
        return self.path.name

    @property
    def total_by_unit(self):
        totals = Counter()
        for item in self.items:
            totals[item.unit] += item.quantity
        return totals

    @property
    def total_handling_units(self):
        return sum(item.quantity for item in self.items)


@dataclass
class DispatcherRecord:
    source_file: str
    shipping_date: date
    row_no: int
    worker_slot: str
    start_time: str
    duration_seconds: int
    action: str
    station_screen: str
    from_location: str
    to_location: str
    units_transnos: int = 0
    quant_reserved: int = 0
    quant_shipped: int = 0
    quant_arrived: int = 0
    transnos: set[str] = field(default_factory=set)
    article_nos: set[str] = field(default_factory=set)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Builds capacity-control extracts from Outlook production lists and dispatcher actions."
    )
    parser.add_argument(
        "--input-dir",
        type=Path,
        default=RAW_OUTLOOK_DIR,
        help="Directory with Outlook attachment exports.",
    )
    parser.add_argument(
        "--delivery-date",
        default="2026-04-27",
        help="Delivery/shipping date to report, ISO format YYYY-MM-DD.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=PROCESSED_DIR,
        help="Directory for anonymized control outputs.",
    )
    parser.add_argument(
        "--process-time-output",
        type=Path,
        default=PROCESS_TIME_OUTPUT,
        help="Output path for the derived process_time_matrix.csv.",
    )
    return parser.parse_args()


def parse_norwegian_int(value):
    text = (value or "").strip().replace("\u00a0", "").replace(" ", "")
    if not text:
        return 0
    return int(text.replace(".", ""))


def parse_decimal(value):
    text = (value or "").strip().replace("\u00a0", "").replace(" ", "")
    if not text:
        return Decimal("0")
    return Decimal(text.replace(".", "").replace(",", "."))


def format_decimal(value, places="0.000000"):
    quantized = value.quantize(Decimal(places), rounding=ROUND_HALF_UP)
    return f"{quantized:f}"


def parse_dispatcher_int(value):
    text = (value or "").strip().replace("\u00a0", "").replace(" ", "")
    if not text:
        return 0
    return int(Decimal(text.replace(",", ".")))


def parse_duration_seconds(value):
    text = (value or "").strip()
    if not text:
        return 0
    parts = [int(part) for part in text.split(":") if part != ""]
    if len(parts) == 2:
        return parts[0] * 60 + parts[1]
    if len(parts) == 3:
        return parts[0] * 3600 + parts[1] * 60 + parts[2]
    return 0


def parse_date_ddmmyy(value):
    return datetime.strptime(value, "%d.%m.%y").date()


def parse_datetime_ddmmyy(value, time_value):
    return datetime.strptime(f"{value} {time_value}", "%d.%m.%y %H:%M")


def parse_date_yyyymmdd(value):
    return datetime.strptime(value, "%Y%m%d").date()


def cell(row, index):
    if index >= len(row):
        return ""
    return row[index].strip()


def extract_pdf_text(path):
    reader = PdfReader(str(path))
    text = "\n".join((page.extract_text() or "") for page in reader.pages)
    return text, len(reader.pages)


def parse_production_pdf(path):
    text, pages = extract_pdf_text(path)
    delivery_dates = sorted(set(re.findall(r"Lev\.dato:\s*(\d{2}\.\d{2}\.\d{2})", text)))
    written_values = sorted(
        set(re.findall(r"Skrevet:\s*(\d{2}\.\d{2}\.\d{2})\s*-\s*(\d{2}:\d{2})", text))
    )

    delivery_date = parse_date_ddmmyy(delivery_dates[0]) if len(delivery_dates) == 1 else None
    written_at = parse_datetime_ddmmyy(*written_values[-1]) if written_values else None
    warning_parts = []
    if len(delivery_dates) != 1:
        warning_parts.append(f"expected one Lev.dato, found {len(delivery_dates)}")
    if not written_values:
        warning_parts.append("missing Skrevet timestamp")

    production_list = ProductionList(
        path=path,
        delivery_date=delivery_date,
        written_at=written_at,
        pages=pages,
        parse_warning="; ".join(warning_parts),
    )
    if not delivery_date or not written_at:
        return production_list

    section_no = ""
    section_name = ""
    for raw_line in text.splitlines():
        line = raw_line.strip()
        section_match = SECTION_RE.match(line)
        if section_match and "PRODUKSJONSLISTE" not in line:
            section_no = section_match.group("section_no")
            section_name = section_match.group("section_name").strip()
            continue

        match = PRODUCTION_LINE_RE.match(line)
        if not match:
            continue

        description = match.group("description").strip()
        article_match = re.search(r"(\d{4,6})$", description)
        article_no = article_match.group(1) if article_match else ""

        production_list.items.append(
            ProductionItem(
                source_file=path.name,
                delivery_date=delivery_date,
                written_at=written_at,
                section_no=section_no,
                section_name=section_name,
                article_no=article_no,
                unit=match.group("unit"),
                quantity=parse_norwegian_int(match.group("quantity")),
                plates=parse_decimal(match.group("plates")),
            )
        )

    return production_list


def read_production_lists(input_dir):
    lists = []
    for path in sorted(input_dir.glob("*.pdf")):
        lists.append(parse_production_pdf(path))
    return lists


def final_production_lists_by_date(production_lists):
    candidates = defaultdict(list)
    for production_list in production_lists:
        if production_list.delivery_date and production_list.written_at:
            candidates[production_list.delivery_date].append(production_list)

    selected = {}
    for delivery_date, date_candidates in candidates.items():
        selected[delivery_date] = max(
            date_candidates,
            key=lambda item: (item.written_at, item.path.name),
        )
    return selected


def worker_slots(rows):
    names = sorted(
        {
            cell(row, 0)
            for row in rows
            if cell(row, 6) in KNOWN_ACTIONS and cell(row, 0) and cell(row, 0) != "END DISPATCH TERMINALS"
        }
    )
    slots = {name: f"W{idx:02d}" for idx, name in enumerate(names, start=1)}
    slots["END DISPATCH TERMINALS"] = "SYSTEM_01"
    return slots


def new_dispatcher_record(path, shipping_date, row_no, row, slots):
    worker_name = cell(row, 0)
    return DispatcherRecord(
        source_file=path.name,
        shipping_date=shipping_date,
        row_no=row_no,
        worker_slot=slots.get(worker_name, "W00"),
        start_time=cell(row, 2),
        duration_seconds=parse_duration_seconds(cell(row, 4)),
        action=cell(row, 6),
        station_screen=cell(row, 8),
        from_location=cell(row, 11),
        to_location=cell(row, 14),
    )


def add_quantities(record, row):
    units_transnos = parse_dispatcher_int(cell(row, 21))
    quant_reserved = parse_dispatcher_int(cell(row, 29))
    quant_shipped = parse_dispatcher_int(cell(row, 31))
    quant_arrived = parse_dispatcher_int(cell(row, 33))

    record.units_transnos += units_transnos
    record.quant_reserved += quant_reserved
    record.quant_shipped += quant_shipped
    record.quant_arrived += quant_arrived

    transno = cell(row, 17)
    article_no = cell(row, 19)
    if transno:
        record.transnos.add(transno)
    if article_no:
        record.article_nos.add(article_no)

    return {
        "article_no": article_no,
        "units_transnos": units_transnos,
        "quant_reserved": quant_reserved,
        "quant_shipped": quant_shipped,
        "quant_arrived": quant_arrived,
    }


def parse_dispatcher_csv(path):
    with path.open("r", encoding="utf-8-sig", newline="") as file:
        rows = list(csv.reader(file, delimiter=";"))
    return parse_dispatcher_rows(path, rows)


def xlsx_column_index(cell_reference):
    match = re.match(r"([A-Z]+)", cell_reference)
    if not match:
        return 0
    index = 0
    for character in match.group(1):
        index = index * 26 + ord(character) - ord("A") + 1
    return index - 1


def read_xlsx_rows(path):
    with zipfile.ZipFile(path) as archive:
        names = set(archive.namelist())
        shared_strings = []
        if "xl/sharedStrings.xml" in names:
            root = ElementTree.fromstring(archive.read("xl/sharedStrings.xml"))
            for shared_item in root.findall("main:si", SPREADSHEET_NS):
                shared_strings.append(
                    "".join(text.text or "" for text in shared_item.findall(".//main:t", SPREADSHEET_NS))
                )

        sheet_name = next(
            (name for name in names if name.lower() == "xl/worksheets/sheet1.xml"),
            None,
        )
        if sheet_name is None:
            raise ValueError(f"Could not find Sheet1.xml in {path}")

        root = ElementTree.fromstring(archive.read(sheet_name))
        rows = []
        for sheet_row in root.findall(".//main:sheetData/main:row", SPREADSHEET_NS):
            values_by_index = {}
            for cell_node in sheet_row.findall("main:c", SPREADSHEET_NS):
                value_node = cell_node.find("main:v", SPREADSHEET_NS)
                inline_node = cell_node.find("main:is", SPREADSHEET_NS)
                if value_node is None and inline_node is None:
                    continue

                value = ""
                if inline_node is not None:
                    value = "".join(text.text or "" for text in inline_node.findall(".//main:t", SPREADSHEET_NS))
                elif value_node is not None:
                    value = value_node.text or ""
                    if cell_node.attrib.get("t") == "s":
                        value = shared_strings[int(value)]

                column_index = xlsx_column_index(cell_node.attrib.get("r", "A1"))
                values_by_index[column_index] = value.replace("_x000a_", "\n").strip()

            if values_by_index:
                max_index = max(values_by_index)
                rows.append([values_by_index.get(index, "") for index in range(max_index + 1)])
            else:
                rows.append([])
        return rows


def parse_dispatcher_xlsx(path):
    return parse_dispatcher_rows(path, read_xlsx_rows(path))


def parse_dispatcher_rows(path, rows):

    shipping_dates = []
    for row in rows:
        for idx, value in enumerate(row):
            if value.strip() == "Shipping date:" and idx + 2 < len(row):
                shipping_dates.append(parse_date_yyyymmdd(row[idx + 2].strip()))
    if len(set(shipping_dates)) != 1:
        raise ValueError(f"Expected one shipping date in {path}, found {sorted(set(shipping_dates))}")
    shipping_date = shipping_dates[0]

    slots = worker_slots(rows)
    records = []
    article_rows = []
    current = None

    for row_no, row in enumerate(rows, start=1):
        action = cell(row, 6)
        if action in KNOWN_ACTIONS:
            current = new_dispatcher_record(path, shipping_date, row_no, row, slots)
            records.append(current)

        if current is None:
            continue

        detail = add_quantities(current, row)
        if detail["article_no"]:
            article_rows.append(
                {
                    "source_file": path.name,
                    "shipping_date": shipping_date.isoformat(),
                    "row_no": str(row_no),
                    "action": current.action,
                    "worker_slot": current.worker_slot,
                    **detail,
                }
            )

    return shipping_date, records, article_rows


def read_dispatcher_files(input_dir):
    parsed = []
    csv_stems = {path.stem for path in input_dir.glob("*Dispatcher actions*.csv")}
    for path in sorted(input_dir.glob("*Dispatcher actions*.csv")):
        parsed.append(parse_dispatcher_csv(path))
    for path in sorted(input_dir.glob("*Dispatcher actions*.xlsx")):
        if path.stem not in csv_stems:
            parsed.append(parse_dispatcher_xlsx(path))
    return parsed


def summarize_dispatcher_records(records):
    summary = {}
    for action in sorted({record.action for record in records}):
        action_records = [record for record in records if record.action == action]
        duration_seconds = sum(record.duration_seconds for record in action_records)
        summary[action] = {
            "action": action,
            "records": len(action_records),
            "worker_slots": len({record.worker_slot for record in action_records}),
            "duration_seconds": duration_seconds,
            "duration_minutes": Decimal(duration_seconds) / Decimal(60),
            "units_transnos": sum(record.units_transnos for record in action_records),
            "quant_reserved": sum(record.quant_reserved for record in action_records),
            "quant_shipped": sum(record.quant_shipped for record in action_records),
            "quant_arrived": sum(record.quant_arrived for record in action_records),
            "unique_articles": len({article for record in action_records for article in record.article_nos}),
            "unique_transnos": len({transno for record in action_records for transno in record.transnos}),
        }
    return summary


def aggregate_production_by_article(production_list):
    article_totals = defaultdict(Counter)
    article_units = defaultdict(Counter)
    for item in production_list.items:
        article_totals[item.article_no][item.unit] += item.quantity
        article_units[item.article_no]["total"] += item.quantity
    return article_totals, article_units


def aggregate_dispatcher_article_rows(article_rows):
    totals = defaultdict(lambda: defaultdict(int))
    for row in article_rows:
        article_no = row["article_no"]
        action = row["action"]
        totals[article_no][f"{action}_quant_shipped"] += row["quant_shipped"]
        totals[article_no][f"{action}_units_transnos"] += row["units_transnos"]
    return totals


def build_article_control(production_list, dispatcher_article_rows):
    production_totals, _ = aggregate_production_by_article(production_list)
    dispatcher_totals = aggregate_dispatcher_article_rows(dispatcher_article_rows)
    article_nos = sorted(set(production_totals) | set(dispatcher_totals), key=lambda value: (len(value), value))
    rows = []
    for article_no in article_nos:
        fpk = production_totals[article_no].get("FPK", 0)
        dpk = production_totals[article_no].get("DPK", 0)
        production_total = fpk + dpk
        pd_shipped = dispatcher_totals[article_no].get("PD_quant_shipped", 0)
        ed_shipped = dispatcher_totals[article_no].get("ED_quant_shipped", 0)
        dd_shipped = dispatcher_totals[article_no].get("DD_quant_shipped", 0)
        rows.append(
            {
                "article_no": article_no,
                "production_fpk": fpk,
                "production_dpk": dpk,
                "production_handling_units": production_total,
                "dispatcher_pd_shipped": pd_shipped,
                "dispatcher_ed_shipped": ed_shipped,
                "dispatcher_dd_shipped": dd_shipped,
                "dispatcher_ed_dd_shipped": ed_shipped + dd_shipped,
                "production_vs_ed_diff": production_total - ed_shipped,
                "production_vs_ed_dd_diff": production_total - ed_shipped - dd_shipped,
            }
        )
    return rows


def write_csv(path, rows, fieldnames):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def production_index_rows(production_lists, selected_by_date):
    selected_files = {value.path.name for value in selected_by_date.values()}
    rows = []
    for production_list in production_lists:
        totals = production_list.total_by_unit
        rows.append(
            {
                "source_file": production_list.source_file,
                "delivery_date": production_list.delivery_date.isoformat() if production_list.delivery_date else "",
                "written_at": production_list.written_at.isoformat(sep=" ") if production_list.written_at else "",
                "pages": production_list.pages,
                "item_rows": len(production_list.items),
                "fpk_units": totals.get("FPK", 0),
                "dpk_units": totals.get("DPK", 0),
                "handling_units": production_list.total_handling_units,
                "selected_final_for_delivery_date": "1" if production_list.source_file in selected_files else "0",
                "parse_warning": production_list.parse_warning,
            }
        )
    return rows


def dispatcher_record_rows(records):
    rows = []
    for record in records:
        rows.append(
            {
                "source_file": record.source_file,
                "shipping_date": record.shipping_date.isoformat(),
                "row_no": record.row_no,
                "worker_slot": record.worker_slot,
                "start_time": record.start_time,
                "duration_seconds": record.duration_seconds,
                "action": record.action,
                "station_screen": record.station_screen,
                "from_location": record.from_location,
                "to_location": record.to_location,
                "units_transnos": record.units_transnos,
                "quant_reserved": record.quant_reserved,
                "quant_shipped": record.quant_shipped,
                "quant_arrived": record.quant_arrived,
                "unique_transnos": len(record.transnos),
                "unique_articles": len(record.article_nos),
            }
        )
    return rows


def dispatcher_summary_rows(summary):
    rows = []
    for action, values in sorted(summary.items()):
        shipped = values["quant_shipped"]
        duration_minutes = values["duration_minutes"]
        minutes_per_shipped = Decimal("0")
        if shipped:
            minutes_per_shipped = duration_minutes / Decimal(shipped)
        rows.append(
            {
                "action": action,
                "records": values["records"],
                "worker_slots": values["worker_slots"],
                "duration_minutes": format_decimal(duration_minutes, "0.01"),
                "units_transnos": values["units_transnos"],
                "quant_reserved": values["quant_reserved"],
                "quant_shipped": shipped,
                "quant_arrived": values["quant_arrived"],
                "unique_articles": values["unique_articles"],
                "unique_transnos": values["unique_transnos"],
                "minutes_per_shipped_unit": format_decimal(minutes_per_shipped),
            }
        )
    return rows


def process_time_rows(summary, delivery_date, production_list, dispatcher_source_file):
    rows = []
    for action, (process_id, process_name) in MAIN_PROCESS_MAP.items():
        values = summary.get(action)
        if not values or not values["quant_shipped"]:
            continue
        minutes_per_fpk = values["duration_minutes"] / Decimal(values["quant_shipped"])
        rows.append(
            {
                "stream_id": "ALL",
                "process_id": process_id,
                "minutes_per_fpk": format_decimal(minutes_per_fpk),
                "source_basis": (
                    f"{action} dispatcher {dispatcher_source_file}; "
                    f"final production list {production_list.source_file}"
                ),
                "valid_from": delivery_date.isoformat(),
                "valid_to": "",
                "comment": process_name,
            }
        )
    return rows


def write_process_time_matrix(path, rows):
    write_csv(
        path,
        rows,
        ["stream_id", "process_id", "minutes_per_fpk", "source_basis", "valid_from", "valid_to", "comment"],
    )


def write_control_report(path, delivery_date, production_list, dispatcher_source_file, summary, article_control_rows):
    totals = production_list.total_by_unit
    production_units = production_list.total_handling_units
    pd = summary.get("PD", {})
    ed = summary.get("ED", {})
    dd = summary.get("DD", {})
    undo = summary.get("Undo", {})

    pd_minutes = pd.get("duration_minutes", Decimal("0"))
    ed_minutes = ed.get("duration_minutes", Decimal("0"))
    pd_shipped = pd.get("quant_shipped", 0)
    ed_shipped = ed.get("quant_shipped", 0)
    dd_shipped = dd.get("quant_shipped", 0)
    combined_minutes = pd_minutes + ed_minutes
    combined_per_ed = Decimal("0") if not ed_shipped else combined_minutes / Decimal(ed_shipped)

    article_matches_ed = sum(1 for row in article_control_rows if row["production_vs_ed_diff"] == 0)
    article_matches_ed_dd = sum(1 for row in article_control_rows if row["production_vs_ed_dd_diff"] == 0)
    largest_diffs = sorted(
        article_control_rows,
        key=lambda row: abs(row["production_vs_ed_dd_diff"]),
        reverse=True,
    )[:10]

    lines = [
        f"# Capacity control {delivery_date.isoformat()}",
        "",
        "## Selected production list",
        "",
        f"- Source file: `{production_list.source_file}`",
        f"- Lev.dato: `{production_list.delivery_date.isoformat()}`",
        f"- Skrevet: `{production_list.written_at:%Y-%m-%d %H:%M}`",
        f"- Parsed item rows: `{len(production_list.items)}`",
        f"- FPK: `{totals.get('FPK', 0)}`",
        f"- DPK: `{totals.get('DPK', 0)}`",
        f"- Handling units: `{production_units}`",
        "",
        "## Dispatcher summary",
        "",
        f"- Source file: `{dispatcher_source_file}`",
        "| Action | Records | Worker slots | Minutes | Shipped | Arrived | Min/shipped |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for row in dispatcher_summary_rows(summary):
        lines.append(
            "| {action} | {records} | {worker_slots} | {duration_minutes} | {quant_shipped} | "
            "{quant_arrived} | {minutes_per_shipped_unit} |".format(**row)
        )

    lines.extend(
        [
            "",
            "## Reconciliation",
            "",
            f"- Production handling units minus ED shipped: `{production_units - ed_shipped}`",
            f"- Production handling units minus ED+DD shipped: `{production_units - ed_shipped - dd_shipped}`",
            f"- Article rows with exact production=ED match: `{article_matches_ed}` of `{len(article_control_rows)}`",
            f"- Article rows with exact production=ED+DD match: `{article_matches_ed_dd}` of `{len(article_control_rows)}`",
            f"- Undo shipped quantity is kept separate from main process totals: `{undo.get('quant_shipped', 0)}`",
            "",
            "## Process time candidates",
            "",
            f"- P1 / PD: `{format_decimal(pd_minutes / Decimal(pd_shipped) if pd_shipped else Decimal('0'))}` minutes per shipped unit",
            f"- P2 / ED: `{format_decimal(ed_minutes / Decimal(ed_shipped) if ed_shipped else Decimal('0'))}` minutes per shipped unit",
            f"- P1+P2 per ED shipped unit: `{format_decimal(combined_per_ed)}` minutes",
            "- DD is reported as a direct/special dispatch flow and is not used as a main process step here.",
            "",
            "## Largest article-level differences after ED+DD",
            "",
            "| Article | Production units | ED shipped | DD shipped | Difference |",
            "|---|---:|---:|---:|---:|",
        ]
    )
    for row in largest_diffs:
        lines.append(
            "| {article_no} | {production_handling_units} | {dispatcher_ed_shipped} | "
            "{dispatcher_dd_shipped} | {production_vs_ed_dd_diff} |".format(**row)
        )

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    args = parse_args()
    delivery_date = datetime.strptime(args.delivery_date, "%Y-%m-%d").date()
    input_dir = args.input_dir
    output_dir = args.output_dir

    production_lists = read_production_lists(input_dir)
    selected_by_date = final_production_lists_by_date(production_lists)
    if delivery_date not in selected_by_date:
        raise SystemExit(f"No final production list found for {delivery_date.isoformat()} in {input_dir}")
    production_list = selected_by_date[delivery_date]

    dispatcher_batches = [
        (shipping_date, records, article_rows)
        for shipping_date, records, article_rows in read_dispatcher_files(input_dir)
        if shipping_date == delivery_date
    ]
    if not dispatcher_batches:
        raise SystemExit(f"No dispatcher action CSV found for {delivery_date.isoformat()} in {input_dir}")
    if len(dispatcher_batches) > 1:
        raise SystemExit(f"Expected one dispatcher action CSV for {delivery_date.isoformat()}, found {len(dispatcher_batches)}")

    _, dispatcher_records, dispatcher_article_rows = dispatcher_batches[0]
    dispatcher_source_file = dispatcher_records[0].source_file if dispatcher_records else ""
    summary = summarize_dispatcher_records(dispatcher_records)
    article_control_rows = build_article_control(production_list, dispatcher_article_rows)
    process_rows = process_time_rows(summary, delivery_date, production_list, dispatcher_source_file)

    date_label = delivery_date.isoformat()
    write_csv(
        output_dir / "production_lists_index.csv",
        production_index_rows(production_lists, selected_by_date),
        [
            "source_file",
            "delivery_date",
            "written_at",
            "pages",
            "item_rows",
            "fpk_units",
            "dpk_units",
            "handling_units",
            "selected_final_for_delivery_date",
            "parse_warning",
        ],
    )
    write_csv(
        output_dir / f"dispatcher_actions_{date_label}_anonymized.csv",
        dispatcher_record_rows(dispatcher_records),
        [
            "source_file",
            "shipping_date",
            "row_no",
            "worker_slot",
            "start_time",
            "duration_seconds",
            "action",
            "station_screen",
            "from_location",
            "to_location",
            "units_transnos",
            "quant_reserved",
            "quant_shipped",
            "quant_arrived",
            "unique_transnos",
            "unique_articles",
        ],
    )
    write_csv(
        output_dir / f"dispatcher_summary_{date_label}.csv",
        dispatcher_summary_rows(summary),
        [
            "action",
            "records",
            "worker_slots",
            "duration_minutes",
            "units_transnos",
            "quant_reserved",
            "quant_shipped",
            "quant_arrived",
            "unique_articles",
            "unique_transnos",
            "minutes_per_shipped_unit",
        ],
    )
    write_csv(
        output_dir / f"article_control_{date_label}.csv",
        article_control_rows,
        [
            "article_no",
            "production_fpk",
            "production_dpk",
            "production_handling_units",
            "dispatcher_pd_shipped",
            "dispatcher_ed_shipped",
            "dispatcher_dd_shipped",
            "dispatcher_ed_dd_shipped",
            "production_vs_ed_diff",
            "production_vs_ed_dd_diff",
        ],
    )
    write_process_time_matrix(args.process_time_output, process_rows)
    write_control_report(
        output_dir / f"control_report_{date_label}.md",
        delivery_date,
        production_list,
        dispatcher_source_file,
        summary,
        article_control_rows,
    )

    print(f"Selected final production list: {production_list.source_file}")
    print(f"Production handling units: {production_list.total_handling_units}")
    print(f"Dispatcher source: {dispatcher_source_file}")
    for action, values in sorted(summary.items()):
        print(
            f"{action}: shipped={values['quant_shipped']} "
            f"minutes={format_decimal(values['duration_minutes'], '0.01')}"
        )
    print(f"Wrote control outputs to {output_dir}")
    print(f"Wrote process time matrix to {args.process_time_output}")


if __name__ == "__main__":
    main()
