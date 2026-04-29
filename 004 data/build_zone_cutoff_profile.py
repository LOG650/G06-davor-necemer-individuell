import argparse
import csv
import re
from collections import Counter
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

from build_capacity_control import (
    BASE_DIR,
    PROCESSED_DIR,
    RAW_OUTLOOK_DIR,
    cell,
    is_legacy_dispatcher_rows,
    parse_dispatcher_int,
    parse_shipping_date,
    read_xlsx_rows,
)


ZONE_OUTPUT = BASE_DIR / "zone_cutoff_profile.csv"
DAILY_OUTPUT = PROCESSED_DIR / "zone_cutoff_profile_daily.csv"
SUMMARY_OUTPUT = PROCESSED_DIR / "zone_cutoff_profile_summary.csv"
QUALITY_OUTPUT = PROCESSED_DIR / "zone_cutoff_profile_quality.md"

STREET_RE = re.compile(r"\bStreet\s+(?P<number>\d+)\b", re.IGNORECASE)

ZONE_MAP = {
    "Z1": {"cutoff_label": "00:00", "street_min": 1, "street_max": 1},
    "Z2": {"cutoff_label": "01:00", "street_min": 2, "street_max": 2},
    "Z3": {"cutoff_label": "02:00", "street_min": 3, "street_max": None},
}


@dataclass
class DispatcherStreetBatch:
    path: Path
    shipping_date: object
    legacy: bool
    street_totals: Counter
    ed_rows: int
    skipped_ed_rows: int

    @property
    def total_quantity(self):
        return sum(self.street_totals.values())


def parse_args():
    parser = argparse.ArgumentParser(
        description="Builds zone/cut-off shares from raw dispatcher action exports."
    )
    parser.add_argument(
        "--input-dir",
        type=Path,
        default=RAW_OUTLOOK_DIR,
        help="Directory with Outlook dispatcher action exports.",
    )
    parser.add_argument(
        "--zone-output",
        type=Path,
        default=ZONE_OUTPUT,
        help="Published zone_cutoff_profile.csv output path.",
    )
    parser.add_argument(
        "--daily-output",
        type=Path,
        default=DAILY_OUTPUT,
        help="Local per-date control extract output path.",
    )
    parser.add_argument(
        "--summary-output",
        type=Path,
        default=SUMMARY_OUTPUT,
        help="Local aggregate source summary output path.",
    )
    parser.add_argument(
        "--quality-output",
        type=Path,
        default=QUALITY_OUTPUT,
        help="Local quality report output path.",
    )
    parser.add_argument(
        "--start-date",
        default="",
        help="Optional first shipping date to include, ISO format YYYY-MM-DD.",
    )
    parser.add_argument(
        "--end-date",
        default="",
        help="Optional last shipping date to include, ISO format YYYY-MM-DD.",
    )
    return parser.parse_args()


def parse_iso_date(value):
    if not value:
        return None
    return datetime.strptime(value, "%Y-%m-%d").date()


def read_dispatcher_rows(path):
    if path.suffix.lower() == ".csv":
        with path.open("r", encoding="utf-8-sig", newline="") as file:
            return list(csv.reader(file, delimiter=";"))
    return read_xlsx_rows(path)


def dispatcher_paths(input_dir):
    paths = [
        path
        for path in input_dir.iterdir()
        if path.is_file() and "dispatcher actions" in path.name.lower()
    ]
    csv_paths = sorted(path for path in paths if path.suffix.lower() == ".csv")
    xlsx_paths = sorted(path for path in paths if path.suffix.lower() == ".xlsx")
    csv_stems = {path.stem.lower() for path in csv_paths}
    return csv_paths + [path for path in xlsx_paths if path.stem.lower() not in csv_stems]


def parse_street_number(value):
    match = STREET_RE.search(value or "")
    if not match:
        return None
    return int(match.group("number"))


def parse_unique_shipping_date(rows, path):
    shipping_dates = []
    for row in rows:
        for idx, value in enumerate(row):
            if value.strip() == "Shipping date:":
                for date_index in (idx + 1, idx + 2):
                    parsed_date = parse_shipping_date(cell(row, date_index))
                    if parsed_date:
                        shipping_dates.append(parsed_date)
                        break
    if len(set(shipping_dates)) != 1:
        raise ValueError(f"Expected one shipping date in {path}, found {sorted(set(shipping_dates))}")
    return shipping_dates[0]


def parse_ed_street_batch(path):
    rows = read_dispatcher_rows(path)
    legacy = is_legacy_dispatcher_rows(rows)
    shipping_date = parse_unique_shipping_date(rows, path)
    totals = Counter()
    ed_rows = 0
    skipped_ed_rows = 0

    for row in rows:
        action = cell(row, 3) if legacy else cell(row, 6)
        if action != "ED":
            continue

        ed_rows += 1
        if legacy:
            street_no = parse_street_number(cell(row, 5))
            quantity = parse_dispatcher_int(cell(row, 13))
        else:
            street_no = parse_street_number(cell(row, 11)) or parse_street_number(cell(row, 14))
            quantity = parse_dispatcher_int(cell(row, 31))

        if street_no and quantity > 0:
            totals[street_no] += quantity
        else:
            skipped_ed_rows += 1

    return DispatcherStreetBatch(
        path=path,
        shipping_date=shipping_date,
        legacy=legacy,
        street_totals=totals,
        ed_rows=ed_rows,
        skipped_ed_rows=skipped_ed_rows,
    )


def selected_batches_by_date(paths, start_date=None, end_date=None):
    selected = {}
    parse_errors = []
    empty_batches = []

    for path in paths:
        try:
            batch = parse_ed_street_batch(path)
        except Exception as exc:
            parse_errors.append({"source_file": path.name, "error": str(exc)})
            continue

        if start_date and batch.shipping_date < start_date:
            continue
        if end_date and batch.shipping_date > end_date:
            continue
        if batch.total_quantity <= 0:
            empty_batches.append(batch)
            continue

        current = selected.get(batch.shipping_date)
        if current is None or (batch.total_quantity, batch.path.name) > (
            current.total_quantity,
            current.path.name,
        ):
            selected[batch.shipping_date] = batch

    return selected, parse_errors, empty_batches


def zone_for_street(street_no):
    if street_no == 1:
        return "Z1"
    if street_no == 2:
        return "Z2"
    if street_no >= 3:
        return "Z3"
    return ""


def zone_totals_from_streets(street_totals):
    zone_totals = Counter()
    for street_no, quantity in street_totals.items():
        zone_bucket = zone_for_street(street_no)
        if zone_bucket:
            zone_totals[zone_bucket] += quantity
    return zone_totals


def quantized_share(quantity, total):
    if not total:
        return Decimal("0.000000")
    return (Decimal(quantity) / Decimal(total)).quantize(Decimal("0.000001"), rounding=ROUND_HALF_UP)


def format_share(value):
    return f"{value:.6f}"


def shares_for_zones(zone_totals):
    total = sum(zone_totals.values())
    z1 = quantized_share(zone_totals["Z1"], total)
    z2 = quantized_share(zone_totals["Z2"], total)
    z3 = Decimal("1.000000") - z1 - z2 if total else Decimal("0.000000")
    return {"Z1": z1, "Z2": z2, "Z3": z3}


def write_csv(path, rows, fieldnames):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def build_zone_profile_rows(selected):
    street_totals = Counter()
    for batch in selected.values():
        street_totals.update(batch.street_totals)

    zone_totals = zone_totals_from_streets(street_totals)
    zone_shares = shares_for_zones(zone_totals)
    dates = sorted(selected)
    basis_period = (
        f"ED dispatcher street history {dates[0].isoformat()}..{dates[-1].isoformat()} "
        f"({len(dates)} selected dates)"
    )

    comments = {
        "Z1": "Observed ED quantity to Street 1",
        "Z2": "Observed ED quantity to Street 2",
        "Z3": "Observed ED quantity to Street 3 and later streets",
    }
    return [
        {
            "stream_id": "ALL",
            "zone_bucket": zone_bucket,
            "cutoff_label": ZONE_MAP[zone_bucket]["cutoff_label"],
            "share_of_weekly_volume": format_share(zone_shares[zone_bucket]),
            "basis_period": basis_period,
            "season_segment": "normal",
            "comment": comments[zone_bucket],
        }
        for zone_bucket in ("Z1", "Z2", "Z3")
    ]


def build_daily_rows(selected):
    rows = []
    for shipping_date, batch in sorted(selected.items()):
        zone_totals = zone_totals_from_streets(batch.street_totals)
        zone_shares = shares_for_zones(zone_totals)
        rows.append(
            {
                "shipping_date": shipping_date.isoformat(),
                "source_file": batch.path.name,
                "format": "legacy" if batch.legacy else "modern",
                "total_ed_quantity": batch.total_quantity,
                "z1_quantity": zone_totals["Z1"],
                "z2_quantity": zone_totals["Z2"],
                "z3_quantity": zone_totals["Z3"],
                "z1_share": format_share(zone_shares["Z1"]),
                "z2_share": format_share(zone_shares["Z2"]),
                "z3_share": format_share(zone_shares["Z3"]),
                "ed_rows": batch.ed_rows,
                "skipped_ed_rows": batch.skipped_ed_rows,
            }
        )
    return rows


def build_summary_rows(selected):
    street_totals = Counter()
    ed_rows = 0
    skipped_ed_rows = 0
    legacy_dates = 0
    modern_dates = 0
    for batch in selected.values():
        street_totals.update(batch.street_totals)
        ed_rows += batch.ed_rows
        skipped_ed_rows += batch.skipped_ed_rows
        if batch.legacy:
            legacy_dates += 1
        else:
            modern_dates += 1

    zone_totals = zone_totals_from_streets(street_totals)
    total = sum(zone_totals.values())
    rows = []
    for street_no, quantity in sorted(street_totals.items()):
        zone_bucket = zone_for_street(street_no)
        rows.append(
            {
                "level": "street",
                "bucket": f"Street {street_no}",
                "zone_bucket": zone_bucket,
                "quantity": quantity,
                "share_of_total": format_share(quantized_share(quantity, total)),
                "selected_dates": len(selected),
                "legacy_dates": legacy_dates,
                "modern_dates": modern_dates,
                "ed_rows": ed_rows,
                "skipped_ed_rows": skipped_ed_rows,
            }
        )

    zone_shares = shares_for_zones(zone_totals)
    for zone_bucket in ("Z1", "Z2", "Z3"):
        rows.append(
            {
                "level": "zone",
                "bucket": zone_bucket,
                "zone_bucket": zone_bucket,
                "quantity": zone_totals[zone_bucket],
                "share_of_total": format_share(zone_shares[zone_bucket]),
                "selected_dates": len(selected),
                "legacy_dates": legacy_dates,
                "modern_dates": modern_dates,
                "ed_rows": ed_rows,
                "skipped_ed_rows": skipped_ed_rows,
            }
        )
    return rows


def write_quality_report(path, selected, paths, parse_errors, empty_batches):
    dates = sorted(selected)
    street_totals = Counter()
    ed_rows = 0
    skipped_ed_rows = 0
    legacy_dates = 0
    modern_dates = 0
    for batch in selected.values():
        street_totals.update(batch.street_totals)
        ed_rows += batch.ed_rows
        skipped_ed_rows += batch.skipped_ed_rows
        if batch.legacy:
            legacy_dates += 1
        else:
            modern_dates += 1

    zone_totals = zone_totals_from_streets(street_totals)
    zone_shares = shares_for_zones(zone_totals)
    duplicate_exports = max(0, len(paths) - len(selected) - len(parse_errors) - len(empty_batches))

    lines = [
        "# Zone cut-off profile quality report",
        "",
        "## Method",
        "",
        "- Source: raw dispatcher action exports from Outlook.",
        "- One dispatcher export is selected per shipping date.",
        "- Selection rule for duplicate dates: highest ED street quantity, then source filename.",
        "- Basis action: ED / final dispatch.",
        "- Zone mapping: Z1 = Street 1, Z2 = Street 2, Z3 = Street 3 and later streets.",
        "- Legacy `.xls` files are not read directly; converted `.xlsx` files are used.",
        "",
        "## Coverage",
        "",
        f"- Dispatcher files considered: `{len(paths)}`",
        f"- Selected shipping dates: `{len(selected)}`",
        f"- Date range: `{dates[0].isoformat()}` to `{dates[-1].isoformat()}`",
        f"- Legacy-format selected dates: `{legacy_dates}`",
        f"- Modern-format selected dates: `{modern_dates}`",
        f"- Duplicate or superseded exports collapsed: `{duplicate_exports}`",
        f"- Empty ED batches skipped: `{len(empty_batches)}`",
        f"- Parse errors: `{len(parse_errors)}`",
        "",
        "## Aggregated ED volume",
        "",
        f"- Total ED quantity with street mapping: `{sum(zone_totals.values())}`",
        f"- ED rows scanned: `{ed_rows}`",
        f"- ED rows skipped because street or quantity was missing: `{skipped_ed_rows}`",
        "",
        "| Zone | Quantity | Share |",
        "|---|---:|---:|",
    ]
    for zone_bucket in ("Z1", "Z2", "Z3"):
        lines.append(
            f"| {zone_bucket} | {zone_totals[zone_bucket]} | {format_share(zone_shares[zone_bucket])} |"
        )

    if parse_errors:
        lines.extend(["", "## Parse Errors", "", "| Source file | Error |", "|---|---|"])
        for row in parse_errors[:25]:
            safe_error = row["error"].replace("|", "\\|")
            lines.append(f"| {row['source_file']} | {safe_error} |")
        if len(parse_errors) > 25:
            lines.append(f"| ... | {len(parse_errors) - 25} additional errors omitted |")

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    args = parse_args()
    start_date = parse_iso_date(args.start_date)
    end_date = parse_iso_date(args.end_date)

    paths = dispatcher_paths(args.input_dir)
    selected, parse_errors, empty_batches = selected_batches_by_date(paths, start_date, end_date)
    if not selected:
        raise SystemExit("No dispatcher ED street quantities could be parsed.")

    zone_rows = build_zone_profile_rows(selected)
    daily_rows = build_daily_rows(selected)
    summary_rows = build_summary_rows(selected)

    write_csv(
        args.zone_output,
        zone_rows,
        [
            "stream_id",
            "zone_bucket",
            "cutoff_label",
            "share_of_weekly_volume",
            "basis_period",
            "season_segment",
            "comment",
        ],
    )
    write_csv(
        args.daily_output,
        daily_rows,
        [
            "shipping_date",
            "source_file",
            "format",
            "total_ed_quantity",
            "z1_quantity",
            "z2_quantity",
            "z3_quantity",
            "z1_share",
            "z2_share",
            "z3_share",
            "ed_rows",
            "skipped_ed_rows",
        ],
    )
    write_csv(
        args.summary_output,
        summary_rows,
        [
            "level",
            "bucket",
            "zone_bucket",
            "quantity",
            "share_of_total",
            "selected_dates",
            "legacy_dates",
            "modern_dates",
            "ed_rows",
            "skipped_ed_rows",
        ],
    )
    write_quality_report(args.quality_output, selected, paths, parse_errors, empty_batches)

    zone_totals = zone_totals_from_streets(
        Counter(
            {
                street_no: sum(batch.street_totals[street_no] for batch in selected.values())
                for street_no in {
                    street_no
                    for batch in selected.values()
                    for street_no in batch.street_totals
                }
            }
        )
    )
    zone_shares = shares_for_zones(zone_totals)
    dates = sorted(selected)
    print(f"Processed {len(selected)} selected dispatcher date(s).")
    print(f"Date range: {dates[0].isoformat()} to {dates[-1].isoformat()}")
    print(
        "Zone shares: "
        + ", ".join(f"{zone}={format_share(zone_shares[zone])}" for zone in ("Z1", "Z2", "Z3"))
    )
    print(f"Wrote zone profile to {args.zone_output}")
    print(f"Wrote local control outputs to {args.daily_output.parent}")


if __name__ == "__main__":
    main()
