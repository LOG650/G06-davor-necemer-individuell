import csv
import re
from collections import defaultdict
from datetime import date, timedelta
from decimal import Decimal, InvalidOperation
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
RAW_DIR = BASE_DIR / "raw"
PROCESSED_DIR = BASE_DIR / "processed"

VOLUME_INPUT = RAW_DIR / "weekly_volume_2024_2025_2026.csv"
SUPPLEMENTAL_VOLUME_INPUT = RAW_DIR / "weekly_volume_2026_w06_w14.csv"
WEEKLY_OUTPUT = BASE_DIR / "weekly_volume.csv"
ARTICLE_WEEK_OUTPUT = PROCESSED_DIR / "article_week_volume_clean.csv"
CAMPAIGN_OUTPUT = PROCESSED_DIR / "campaign_events_clean.csv"
LIFECYCLE_OUTPUT = PROCESSED_DIR / "lifecycle_events_clean.csv"
QUALITY_OUTPUT = PROCESSED_DIR / "data_quality_summary.md"

STREAM_MAP = {
    "Egenproduserte": "F",
    "Forhandlingsvare": "S",
}


def parse_decimal(value):
    text = (value or "").strip().replace("\u00a0", "").replace(" ", "")
    if not text or text == "-":
        return Decimal("0")
    text = text.replace(".", "").replace(",", ".")
    try:
        return Decimal(text)
    except InvalidOperation:
        return Decimal("0")


def format_decimal(value):
    return f"{value.quantize(Decimal('0.01'))}"


def clean_key(value):
    text = (value or "").strip()
    if not text or text == "-":
        return ""
    text = re.sub(r"\.0$", "", text)
    return text


def parse_year_from_name(path):
    match = re.search(r"(20\d{2})", path.name)
    return int(match.group(1)) if match else None


def parse_week(value):
    text = (value or "").strip()
    match = re.search(r"\d{1,2}", text)
    if not match:
        return None
    week = int(match.group(0))
    if 1 <= week <= 53:
        return week
    return None


def parse_event_date(value, fallback_year):
    text = (value or "").strip()
    if not text or text.lower() in {"sanert", "rullerende", "rullerende overgang"}:
        return None

    for fmt in ("%d.%m.%Y", "%d.%m.%y"):
        try:
            day, month, year = text.split(".")[:3]
            return date(int(year), int(month), int(day))
        except (ValueError, IndexError):
            pass

    month_map = {
        "jan": 1,
        "feb": 2,
        "mar": 3,
        "apr": 4,
        "mai": 5,
        "jun": 6,
        "jul": 7,
        "aug": 8,
        "sep": 9,
        "okt": 10,
        "nov": 11,
        "des": 12,
    }
    match = re.match(r"(\d{1,2})\.?\s*([A-Za-zÆØÅæøå]{3})", text)
    if match and fallback_year:
        day = int(match.group(1))
        month = month_map.get(match.group(2).lower())
        if month:
            return date(fallback_year, month, day)
    return None


def iso_week_start(year, week):
    return date.fromisocalendar(int(year), int(week), 1)


def year_week_label(year, week):
    return f"{int(year)}-{int(week):02d}"


def is_larvik_relevant(text):
    value = (text or "").strip().lower()
    if not value:
        return True
    return "larvik" in value or "alle" in value or value in {"x", "p", "s", "ps"}


def norwegian_easter_sunday(year):
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    month = (h + l - 7 * m + 114) // 31
    day = ((h + l - 7 * m + 114) % 31) + 1
    return date(year, month, day)


def holiday_weeks(years):
    weeks = set()
    for year in years:
        easter = norwegian_easter_sunday(year)
        dates = {
            date(year, 1, 1),
            date(year, 5, 1),
            date(year, 5, 17),
            date(year, 12, 24),
            date(year, 12, 25),
            date(year, 12, 26),
            date(year, 12, 31),
            easter - timedelta(days=3),
            easter - timedelta(days=2),
            easter,
            easter + timedelta(days=1),
        }
        for day in dates:
            iso = day.isocalendar()
            weeks.add((str(iso.year), f"{iso.week:02d}"))
    return weeks


def read_campaign_events():
    events = []
    files = sorted(RAW_DIR.glob("Kjedekampanje*.csv"))
    for path in files:
        year = parse_year_from_name(path)
        lines = path.read_text(encoding="utf-8-sig").splitlines()
        header_idx = None
        for idx, line in enumerate(lines):
            columns = [column.strip() for column in line.split(";")]
            if "Uke" in columns and "Varenr" in columns:
                header_idx = idx
                break
        if header_idx is None:
            continue

        current_week = None
        reader = csv.DictReader(lines[header_idx:], delimiter=";")
        for row in reader:
            week = parse_week(row.get("Uke"))
            if week is not None:
                current_week = week
            elif current_week is None:
                continue

            article_no = clean_key(row.get("Varenr"))
            epd = clean_key(row.get("EPD"))
            if not article_no and not epd:
                continue

            events.append(
                {
                    "source_file": path.name,
                    "year": str(year or ""),
                    "week": f"{current_week:02d}",
                    "year_week": year_week_label(year, current_week) if year else "",
                    "customer": (row.get("Kunde") or "").strip(),
                    "distribution": (row.get("Distribusjon") or "").strip(),
                    "bakeries": (row.get("Bakerier") or "").strip(),
                    "larvik_relevant": "1" if is_larvik_relevant(row.get("Bakerier")) else "0",
                    "epd": epd,
                    "article_no": article_no,
                    "article_name": (row.get("Varenavn") or "").strip(),
                    "product_group": (row.get("Produktgruppe") or "").strip(),
                    "discount_pct": (row.get("% Rabatt") or "").strip(),
                    "updated_date": (row.get("Oppdatert dato") or "").strip(),
                    "remarks": (row.get("Anmerkninger") or "").strip(),
                    "price": (row.get("Utpris") or "").strip(),
                    "event_type": "kjedekampanje",
                }
            )
    return events


def read_lifecycle_events():
    events = []
    files = sorted(
        path
        for path in RAW_DIR.glob("*.csv")
        if "Lansering" in path.name or "sanering" in path.name or "Sanering" in path.name
    )
    for path in files:
        fallback_year = parse_year_from_name(path)
        lines = path.read_text(encoding="utf-8-sig").splitlines()
        header_idx = None
        for idx, line in enumerate(lines):
            columns = [column.strip() for column in line.split(";")]
            normalized = [column.replace("EPD ", "EPD") for column in columns]
            if ("Varenr" in normalized or "Varenummer" in normalized) and (
                "Varenavn" in normalized or "Artikkelnavn" in normalized
            ):
                header_idx = idx
                break
        if header_idx is None:
            continue

        reader = csv.DictReader(lines[header_idx:], delimiter=";")
        for row in reader:
            normalized = {((key or "").strip()): (value or "").strip() for key, value in row.items()}
            article_no = clean_key(normalized.get("Varenr") or normalized.get("Varenummer"))
            epd = clean_key(normalized.get("EPD") or normalized.get("EPD "))
            if not article_no and not epd:
                continue

            raw_date = (
                normalized.get("Lanseringsdato")
                or normalized.get("Saneringsdato")
                or normalized.get("Lanseringsuker")
            )
            parsed_date = parse_event_date(raw_date, fallback_year)
            if "Saneringsdato" in normalized:
                event_type = "sanering"
            elif "Julen" in path.name:
                event_type = "jul_lansering"
            else:
                event_type = "lansering"

            larvik_status = normalized.get("Larvik", "")
            comment = (
                normalized.get("Kommentar om produkt")
                or normalized.get("Kommentar nyhet/endring (om produkt)")
                or normalized.get("Kommentar til Bakeri")
                or normalized.get("Produksjonssted/kommentar")
                or ""
            )
            if parsed_date:
                iso = parsed_date.isocalendar()
                event_year = str(iso.year)
                event_week = f"{iso.week:02d}"
                event_year_week = year_week_label(iso.year, iso.week)
            else:
                event_year = str(fallback_year or "")
                event_week = ""
                event_year_week = ""

            events.append(
                {
                    "source_file": path.name,
                    "event_type": event_type,
                    "event_date": parsed_date.isoformat() if parsed_date else "",
                    "event_year": event_year,
                    "event_week": event_week,
                    "event_year_week": event_year_week,
                    "article_no": article_no,
                    "epd": epd,
                    "article_name": normalized.get("Varenavn") or normalized.get("Artikkelnavn") or "",
                    "larvik_status": larvik_status,
                    "larvik_relevant": "1" if is_larvik_relevant(larvik_status) else "0",
                    "comment": comment,
                }
            )
    return events


def event_maps(events, year_field="year", week_field="week"):
    by_article = defaultdict(list)
    by_epd = defaultdict(list)
    for event in events:
        if event.get("larvik_relevant") == "0":
            continue
        year = event.get(year_field, "")
        week = event.get(week_field, "")
        if not year or not week:
            continue
        if event.get("article_no"):
            by_article[(year, week, event["article_no"])].append(event)
        if event.get("epd"):
            by_epd[(year, week, event["epd"])].append(event)
    return by_article, by_epd


def unique_events(events):
    seen = set()
    result = []
    for event in events:
        key = (
            event.get("source_file"),
            event.get("event_type"),
            event.get("year") or event.get("event_year"),
            event.get("week") or event.get("event_week"),
            event.get("article_no"),
            event.get("epd"),
            event.get("customer", ""),
        )
        if key in seen:
            continue
        seen.add(key)
        result.append(event)
    return result


def iter_volume_rows():
    supplemental_weeks = {("2026", f"{week:02d}") for week in range(6, 15)}
    inputs = [
        (VOLUME_INPUT, None),
        (SUPPLEMENTAL_VOLUME_INPUT, supplemental_weeks),
    ]

    for path, allowed_weeks in inputs:
        if not path.exists():
            continue
        with path.open("r", encoding="utf-8-sig", newline="") as file:
            reader = csv.DictReader(file, delimiter=";")
            for row in reader:
                year = (row.get("År") or "").strip()
                week = (row.get("Uke") or "").strip().zfill(2)
                if path == VOLUME_INPUT and (year, week) in supplemental_weeks:
                    continue
                if allowed_weeks is not None and (year, week) not in allowed_weeks:
                    continue
                yield {
                    "source_file": path.name,
                    "customer": (row.get("Kunde") or "").strip(),
                    "article_no": clean_key(row.get("Artikkelnr")),
                    "article_name": (row.get("Artikkelnavn") or "").strip(),
                    "product_group_no": (row.get("Produktgruppe nr") or "").strip(),
                    "product_group_name": (row.get("Produktgruppe navn") or "").strip(),
                    "unit": (row.get("Grunnenhet") or "").strip(),
                    "order_type": (row.get("Ordretype/Navn") or "").strip(),
                    "epd": clean_key(row.get("EPD nr")),
                    "week": week,
                    "year": year,
                    "quantity": parse_decimal(row.get("Antall fakturert")),
                    "stream_name": (row.get("Egen forhandling") or "").strip(),
                }


def read_article_week_volume(campaign_events, lifecycle_events):
    campaign_by_article, campaign_by_epd = event_maps(campaign_events)
    lifecycle_by_article, lifecycle_by_epd = event_maps(
        lifecycle_events, year_field="event_year", week_field="event_week"
    )

    article_week = {}
    quality = {
        "raw_rows": 0,
        "raw_volume": Decimal("0"),
        "excluded_dash_rows": 0,
        "excluded_dash_volume": Decimal("0"),
        "excluded_nonpositive_rows": 0,
        "excluded_nonpositive_volume": Decimal("0"),
        "excluded_operational_rows": 0,
        "excluded_operational_volume": Decimal("0"),
        "included_rows": 0,
        "included_volume": Decimal("0"),
    }

    for row in iter_volume_rows():
            article_no = row["article_no"]
            article_name = row["article_name"]
            product_group_no = row["product_group_no"]
            product_group_name = row["product_group_name"]
            unit = row["unit"]
            order_type = row["order_type"]
            epd = row["epd"]
            week = row["week"]
            year = row["year"]
            quantity = row["quantity"]
            stream_name = row["stream_name"]
            stream_id = STREAM_MAP.get(stream_name, stream_name)

            quality["raw_rows"] += 1
            quality["raw_volume"] += quantity

            if order_type == "-":
                quality["excluded_dash_rows"] += 1
                quality["excluded_dash_volume"] += quantity
                continue
            if quantity <= 0:
                quality["excluded_nonpositive_rows"] += 1
                quality["excluded_nonpositive_volume"] += quantity
                continue
            if product_group_no == "850" or product_group_name.lower().startswith("øvrige driftsin"):
                quality["excluded_operational_rows"] += 1
                quality["excluded_operational_volume"] += quantity
                continue

            key = (
                year,
                week,
                article_no,
                epd,
                stream_id,
                stream_name,
                product_group_no,
                product_group_name,
                unit,
            )
            if key not in article_week:
                article_week[key] = {
                    "year": year,
                    "week": week,
                    "year_week": year_week_label(year, week),
                    "week_start_date": iso_week_start(year, week).isoformat(),
                    "article_no": article_no,
                    "article_name": article_name,
                    "epd": epd,
                    "stream_id": stream_id,
                    "stream_name": stream_name,
                    "product_group_no": product_group_no,
                    "product_group_name": product_group_name,
                    "unit": unit,
                    "volume_fpk_eq": Decimal("0"),
                    "campaign_events": [],
                    "lifecycle_events": [],
                }
            article_week[key]["volume_fpk_eq"] += quantity
            quality["included_rows"] += 1
            quality["included_volume"] += quantity

    for item in article_week.values():
        campaign_matches = []
        campaign_matches.extend(campaign_by_article.get((item["year"], item["week"], item["article_no"]), []))
        campaign_matches.extend(campaign_by_epd.get((item["year"], item["week"], item["epd"]), []))
        lifecycle_matches = []
        lifecycle_matches.extend(lifecycle_by_article.get((item["year"], item["week"], item["article_no"]), []))
        lifecycle_matches.extend(lifecycle_by_epd.get((item["year"], item["week"], item["epd"]), []))
        item["campaign_events"] = unique_events(campaign_matches)
        item["lifecycle_events"] = unique_events(lifecycle_matches)

    return list(article_week.values()), quality


def write_csv(path, rows, fieldnames):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=",", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_event_files(campaign_events, lifecycle_events):
    write_csv(
        CAMPAIGN_OUTPUT,
        campaign_events,
        [
            "source_file",
            "year",
            "week",
            "year_week",
            "customer",
            "distribution",
            "bakeries",
            "larvik_relevant",
            "epd",
            "article_no",
            "article_name",
            "product_group",
            "discount_pct",
            "updated_date",
            "remarks",
            "price",
            "event_type",
        ],
    )
    write_csv(
        LIFECYCLE_OUTPUT,
        lifecycle_events,
        [
            "source_file",
            "event_type",
            "event_date",
            "event_year",
            "event_week",
            "event_year_week",
            "article_no",
            "epd",
            "article_name",
            "larvik_status",
            "larvik_relevant",
            "comment",
        ],
    )


def write_article_week(article_week_rows):
    rows = []
    for item in sorted(
        article_week_rows,
        key=lambda row: (row["year"], row["week"], row["stream_id"], row["article_no"], row["epd"]),
    ):
        campaign_types = sorted({event["event_type"] for event in item["campaign_events"]})
        lifecycle_types = sorted({event["event_type"] for event in item["lifecycle_events"]})
        event_types = campaign_types + [event_type for event_type in lifecycle_types if event_type not in campaign_types]
        rows.append(
            {
                "year_week": item["year_week"],
                "week_start_date": item["week_start_date"],
                "year": item["year"],
                "week": item["week"],
                "stream_id": item["stream_id"],
                "stream_name": item["stream_name"],
                "article_no": item["article_no"],
                "article_name": item["article_name"],
                "epd": item["epd"],
                "product_group_no": item["product_group_no"],
                "product_group_name": item["product_group_name"],
                "unit": item["unit"],
                "volume_fpk_eq": format_decimal(item["volume_fpk_eq"]),
                "campaign_flag": "1" if campaign_types else "0",
                "event_types": ";".join(event_types),
                "campaign_event_count": str(len(item["campaign_events"])),
                "lifecycle_event_count": str(len(item["lifecycle_events"])),
            }
        )
    write_csv(
        ARTICLE_WEEK_OUTPUT,
        rows,
        [
            "year_week",
            "week_start_date",
            "year",
            "week",
            "stream_id",
            "stream_name",
            "article_no",
            "article_name",
            "epd",
            "product_group_no",
            "product_group_name",
            "unit",
            "volume_fpk_eq",
            "campaign_flag",
            "event_types",
            "campaign_event_count",
            "lifecycle_event_count",
        ],
    )


def write_weekly_volume(article_week_rows):
    years = {int(row["year"]) for row in article_week_rows if row["year"].isdigit()}
    holidays = holiday_weeks(years)
    weekly = {}
    for item in article_week_rows:
        key = (item["year"], item["week"], item["stream_id"])
        if key not in weekly:
            weekly[key] = {
                "year": item["year"],
                "week": item["week"],
                "year_week": item["year_week"],
                "week_start_date": item["week_start_date"],
                "stream_id": item["stream_id"],
                "volume_fpk_eq": Decimal("0"),
                "campaign_article_count": set(),
                "lifecycle_article_count": set(),
                "campaign_types": set(),
            }
        weekly[key]["volume_fpk_eq"] += item["volume_fpk_eq"]
        if item["campaign_events"]:
            weekly[key]["campaign_article_count"].add(item["article_no"] or item["epd"])
            weekly[key]["campaign_types"].add("kjedekampanje")
        if item["lifecycle_events"]:
            weekly[key]["lifecycle_article_count"].add(item["article_no"] or item["epd"])
            for event in item["lifecycle_events"]:
                weekly[key]["campaign_types"].add(event["event_type"])

    rows = []
    for key, item in sorted(weekly.items()):
        campaign_types = sorted(item["campaign_types"])
        notes = []
        if item["campaign_article_count"]:
            notes.append(f"campaign_articles={len(item['campaign_article_count'])}")
        if item["lifecycle_article_count"]:
            notes.append(f"lifecycle_articles={len(item['lifecycle_article_count'])}")
        rows.append(
            {
                "year_week": item["year_week"],
                "week_start_date": item["week_start_date"],
                "stream_id": item["stream_id"],
                "volume_fpk_eq": format_decimal(item["volume_fpk_eq"]),
                "campaign_flag": "1" if "kjedekampanje" in item["campaign_types"] else "0",
                "campaign_type": ";".join(campaign_types),
                "holiday_flag": "1" if (item["year"], item["week"]) in holidays else "0",
                "anomaly_flag": "0",
                "constrained_week_flag": "0",
                "notes": "; ".join(notes),
            }
        )
    write_csv(
        WEEKLY_OUTPUT,
        rows,
        [
            "year_week",
            "week_start_date",
            "stream_id",
            "volume_fpk_eq",
            "campaign_flag",
            "campaign_type",
            "holiday_flag",
            "anomaly_flag",
            "constrained_week_flag",
            "notes",
        ],
    )
    return rows


def write_quality_summary(campaign_events, lifecycle_events, article_week_rows, weekly_rows, quality):
    campaign_matched = sum(1 for row in article_week_rows if row["campaign_events"])
    lifecycle_matched = sum(1 for row in article_week_rows if row["lifecycle_events"])
    by_year_stream = defaultdict(Decimal)
    for row in weekly_rows:
        year = row["year_week"].split("-")[0]
        by_year_stream[(year, row["stream_id"])] += Decimal(row["volume_fpk_eq"])

    lines = [
        "# Data quality summary",
        "",
        "## Inputs",
        f"- Main volume file: `{VOLUME_INPUT.name}`",
        f"- Supplemental validation-period volume file: `{SUPPLEMENTAL_VOLUME_INPUT.name}`",
        "- Supplemental file replaces the main file for `2026-06` and extends the series through `2026-14`.",
        f"- Campaign files: `{len(list(RAW_DIR.glob('Kjedekampanje*.csv')))}`",
        f"- Lifecycle files: `{len([p for p in RAW_DIR.glob('*.csv') if 'Lansering' in p.name or 'sanering' in p.name or 'Sanering' in p.name])}`",
        "",
        "## Volume filtering",
        f"- Raw rows: `{quality['raw_rows']}`",
        f"- Raw volume: `{format_decimal(quality['raw_volume'])}`",
        f"- Excluded `Ordretype/Navn = -` rows: `{quality['excluded_dash_rows']}` / volume `{format_decimal(quality['excluded_dash_volume'])}`",
        f"- Excluded non-positive rows: `{quality['excluded_nonpositive_rows']}` / volume `{format_decimal(quality['excluded_nonpositive_volume'])}`",
        f"- Excluded operational/non-product rows: `{quality['excluded_operational_rows']}` / volume `{format_decimal(quality['excluded_operational_volume'])}`",
        f"- Included rows: `{quality['included_rows']}` / volume `{format_decimal(quality['included_volume'])}`",
        "",
        "Important: `Ordretype/Navn = -` closely mirrors the real order-type rows in the Qlik export and would almost double the weekly series. A customer-level check in `weekly_volume_2026_w06_w14.csv` confirmed that `-` appears on nearly the same customer/article/week keys as the named order types. It is therefore excluded from the cleaned dataset.",
        "",
        "## Cleaned outputs",
        f"- `{WEEKLY_OUTPUT.relative_to(BASE_DIR.parent)}` rows: `{len(weekly_rows)}`",
        f"- `{ARTICLE_WEEK_OUTPUT.relative_to(BASE_DIR.parent)}` rows: `{len(article_week_rows)}`",
        f"- `{CAMPAIGN_OUTPUT.relative_to(BASE_DIR.parent)}` rows: `{len(campaign_events)}`",
        f"- `{LIFECYCLE_OUTPUT.relative_to(BASE_DIR.parent)}` rows: `{len(lifecycle_events)}`",
        "",
        "## Event matching",
        f"- Article-week rows with campaign match: `{campaign_matched}`",
        f"- Article-week rows with lifecycle match: `{lifecycle_matched}`",
        "",
        "## Final volume by year and stream",
    ]
    for (year, stream_id), volume in sorted(by_year_stream.items()):
        lines.append(f"- `{year}` `{stream_id}`: `{format_decimal(volume)}`")

    weeks = sorted({row["year_week"] for row in weekly_rows})
    lines.extend(
        [
            "",
            "## Week coverage",
            f"- First week: `{weeks[0] if weeks else ''}`",
            f"- Last week: `{weeks[-1] if weeks else ''}`",
            f"- Unique year-week values: `{len(weeks)}`",
        ]
    )
    QUALITY_OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    campaign_events = read_campaign_events()
    lifecycle_events = read_lifecycle_events()
    write_event_files(campaign_events, lifecycle_events)
    article_week_rows, quality = read_article_week_volume(campaign_events, lifecycle_events)
    write_article_week(article_week_rows)
    weekly_rows = write_weekly_volume(article_week_rows)
    write_quality_summary(campaign_events, lifecycle_events, article_week_rows, weekly_rows, quality)
    print(f"Wrote {WEEKLY_OUTPUT}")
    print(f"Wrote {ARTICLE_WEEK_OUTPUT}")
    print(f"Wrote {CAMPAIGN_OUTPUT}")
    print(f"Wrote {LIFECYCLE_OUTPUT}")
    print(f"Wrote {QUALITY_OUTPUT}")


if __name__ == "__main__":
    main()
