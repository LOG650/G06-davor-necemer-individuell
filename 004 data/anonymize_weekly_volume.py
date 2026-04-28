import argparse
import csv
from collections import defaultdict
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DEFAULT_INPUT = BASE_DIR / "weekly_volume.csv"
DEFAULT_OUTPUT = BASE_DIR / "weekly_volume_anonymized.csv"


def parse_args():
    parser = argparse.ArgumentParser(
        description="Create a publishable indexed version of weekly_volume.csv."
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=DEFAULT_INPUT,
        help="Sensitive weekly volume input. Default: 004 data/weekly_volume.csv.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="Anonymized indexed output. Default: 004 data/weekly_volume_anonymized.csv.",
    )
    parser.add_argument(
        "--baseline-mode",
        choices=("year-average", "baseline-week"),
        default="year-average",
        help="Use a yearly average or one named week as index base.",
    )
    parser.add_argument(
        "--baseline-year",
        default="2024",
        help="Baseline year when --baseline-mode year-average is used.",
    )
    parser.add_argument(
        "--baseline-week",
        default="2024-01",
        help="Baseline week when --baseline-mode baseline-week is used.",
    )
    parser.add_argument(
        "--index-decimals",
        type=int,
        default=2,
        help="Decimal places for volume_index.",
    )
    parser.add_argument(
        "--keep-notes",
        action="store_true",
        help="Keep original notes. Default removes notes to avoid publishing event counts.",
    )
    return parser.parse_args()


def read_rows(path):
    with path.open("r", encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file))


def parse_decimal(value):
    return Decimal((value or "0").strip().replace(",", "."))


def decimal_places(decimals):
    if decimals < 0:
        raise ValueError("--index-decimals must be zero or positive")
    return Decimal("1").scaleb(-decimals)


def format_decimal(value, decimals):
    quantized = value.quantize(decimal_places(decimals), rounding=ROUND_HALF_UP)
    return f"{quantized:f}"


def baseline_label(args):
    if args.baseline_mode == "year-average":
        return f"{args.baseline_year}_average_per_stream=100"
    return f"{args.baseline_week}_per_stream=100"


def baselines_by_stream(rows, args):
    values = defaultdict(list)
    for row in rows:
        stream_id = row["stream_id"]
        year_week = row["year_week"]
        volume = parse_decimal(row["volume_fpk_eq"])
        if args.baseline_mode == "year-average":
            if year_week.startswith(f"{args.baseline_year}-"):
                values[stream_id].append(volume)
        elif year_week == args.baseline_week:
            values[stream_id].append(volume)

    baselines = {}
    for stream_id, stream_values in values.items():
        if not stream_values:
            continue
        baseline = sum(stream_values, Decimal("0")) / Decimal(len(stream_values))
        if baseline <= 0:
            raise ValueError(f"Non-positive baseline for stream {stream_id}")
        baselines[stream_id] = baseline

    streams = {row["stream_id"] for row in rows}
    missing = sorted(streams - set(baselines))
    if missing:
        raise ValueError(f"Missing baseline for stream(s): {', '.join(missing)}")
    return baselines


def anonymized_rows(rows, baselines, args):
    label = baseline_label(args)
    output_rows = []
    for row in rows:
        volume = parse_decimal(row["volume_fpk_eq"])
        index = volume / baselines[row["stream_id"]] * Decimal("100")
        output_rows.append(
            {
                "year_week": row["year_week"],
                "week_start_date": row["week_start_date"],
                "stream_id": row["stream_id"],
                "volume_index": format_decimal(index, args.index_decimals),
                "index_base": label,
                "campaign_flag": row["campaign_flag"],
                "campaign_type": row["campaign_type"],
                "holiday_flag": row["holiday_flag"],
                "anomaly_flag": row["anomaly_flag"],
                "constrained_week_flag": row["constrained_week_flag"],
                "notes": row["notes"] if args.keep_notes else "",
            }
        )
    return output_rows


def write_rows(path, rows):
    fieldnames = [
        "year_week",
        "week_start_date",
        "stream_id",
        "volume_index",
        "index_base",
        "campaign_flag",
        "campaign_type",
        "holiday_flag",
        "anomaly_flag",
        "constrained_week_flag",
        "notes",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main():
    args = parse_args()
    rows = read_rows(args.input)
    baselines = baselines_by_stream(rows, args)
    output_rows = anonymized_rows(rows, baselines, args)
    write_rows(args.output, output_rows)

    print(f"Wrote {len(output_rows)} anonymized rows to {args.output}")
    print(f"Index base: {baseline_label(args)}")
    print(f"Streams: {', '.join(sorted(baselines))}")


if __name__ == "__main__":
    main()
