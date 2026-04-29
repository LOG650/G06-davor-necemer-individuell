import argparse
import csv
from collections import defaultdict
from datetime import datetime
from decimal import Decimal
from pathlib import Path

from build_capacity_control import (
    BASE_DIR,
    MAIN_PROCESS_MAP,
    PROCESS_TIME_OUTPUT,
    PROCESSED_DIR,
    RAW_OUTLOOK_DIR,
    final_production_lists_by_date,
    format_decimal,
    read_dispatcher_files,
    read_production_lists,
    summarize_dispatcher_records,
    write_process_time_matrix,
)


DEFAULT_SAMPLES_OUTPUT = PROCESSED_DIR / "process_time_samples.csv"


def parse_args():
    parser = argparse.ArgumentParser(
        description="Builds a weighted process_time_matrix.csv from several representative dates."
    )
    parser.add_argument(
        "--input-dir",
        type=Path,
        default=RAW_OUTLOOK_DIR,
        help="Directory with Outlook attachment exports.",
    )
    parser.add_argument(
        "--delivery-dates",
        required=True,
        help="Comma-separated delivery/shipping dates, ISO format YYYY-MM-DD.",
    )
    parser.add_argument(
        "--samples-output",
        type=Path,
        default=DEFAULT_SAMPLES_OUTPUT,
        help="Output path for per-date process-time samples.",
    )
    parser.add_argument(
        "--process-time-output",
        type=Path,
        default=PROCESS_TIME_OUTPUT,
        help="Output path for weighted process_time_matrix.csv.",
    )
    return parser.parse_args()


def parse_delivery_dates(value):
    dates = []
    for item in value.split(","):
        text = item.strip()
        if text:
            dates.append(datetime.strptime(text, "%Y-%m-%d").date())
    return dates


def write_csv(path, rows, fieldnames):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def dispatcher_batches_by_date(input_dir):
    batches = defaultdict(list)
    for shipping_date, records, article_rows in read_dispatcher_files(input_dir):
        batches[shipping_date].append((records, article_rows))
    return batches


def choose_dispatcher_batch(batches):
    return max(
        batches,
        key=lambda batch: batch[0][0].source_file if batch[0] else "",
    )


def main():
    args = parse_args()
    delivery_dates = parse_delivery_dates(args.delivery_dates)
    if not delivery_dates:
        raise SystemExit("No delivery dates provided.")

    production_lists = read_production_lists(args.input_dir)
    selected_production = final_production_lists_by_date(production_lists)
    dispatcher_by_date = dispatcher_batches_by_date(args.input_dir)

    sample_rows = []
    aggregate = defaultdict(lambda: {"duration_minutes": Decimal("0"), "quant_shipped": 0, "dates": []})
    missing = []

    for delivery_date in delivery_dates:
        production_list = selected_production.get(delivery_date)
        dispatcher_batches = dispatcher_by_date.get(delivery_date, [])
        if production_list is None or not dispatcher_batches:
            missing.append(
                {
                    "delivery_date": delivery_date.isoformat(),
                    "production": "yes" if production_list else "no",
                    "dispatcher": "yes" if dispatcher_batches else "no",
                }
            )
            continue

        dispatcher_records, _ = choose_dispatcher_batch(dispatcher_batches)
        dispatcher_source_file = dispatcher_records[0].source_file if dispatcher_records else ""
        summary = summarize_dispatcher_records(dispatcher_records)

        for action, (process_id, process_name) in MAIN_PROCESS_MAP.items():
            values = summary.get(action)
            if not values or not values["quant_shipped"]:
                continue

            minutes_per_fpk = values["duration_minutes"] / Decimal(values["quant_shipped"])
            sample_rows.append(
                {
                    "delivery_date": delivery_date.isoformat(),
                    "process_id": process_id,
                    "action": action,
                    "duration_minutes": format_decimal(values["duration_minutes"], "0.01"),
                    "quant_shipped": values["quant_shipped"],
                    "minutes_per_fpk": format_decimal(minutes_per_fpk),
                    "dispatcher_source_file": dispatcher_source_file,
                    "production_source_file": production_list.source_file,
                }
            )
            aggregate[process_id]["duration_minutes"] += values["duration_minutes"]
            aggregate[process_id]["quant_shipped"] += values["quant_shipped"]
            aggregate[process_id]["dates"].append(delivery_date.isoformat())

    if missing:
        for row in missing:
            print(
                "Missing complete pair for {delivery_date}: production={production}, dispatcher={dispatcher}".format(
                    **row
                )
            )

    if not sample_rows:
        raise SystemExit("No complete production/dispatcher pairs could be processed.")

    process_rows = []
    process_names = {process_id: process_name for _, (process_id, process_name) in MAIN_PROCESS_MAP.items()}
    for process_id, values in sorted(aggregate.items()):
        quant_shipped = values["quant_shipped"]
        if not quant_shipped:
            continue
        minutes_per_fpk = values["duration_minutes"] / Decimal(quant_shipped)
        dates = values["dates"]
        process_rows.append(
            {
                "stream_id": "ALL",
                "process_id": process_id,
                "minutes_per_fpk": format_decimal(minutes_per_fpk),
                "source_basis": f"weighted average from {len(dates)} production/dispatcher pairs: {', '.join(dates)}",
                "valid_from": min(dates),
                "valid_to": max(dates),
                "comment": process_names[process_id],
            }
        )

    write_csv(
        args.samples_output,
        sample_rows,
        [
            "delivery_date",
            "process_id",
            "action",
            "duration_minutes",
            "quant_shipped",
            "minutes_per_fpk",
            "dispatcher_source_file",
            "production_source_file",
        ],
    )
    write_process_time_matrix(args.process_time_output, process_rows)

    print(f"Processed {len({row['delivery_date'] for row in sample_rows})} complete date(s).")
    print(f"Wrote samples to {args.samples_output}")
    print(f"Wrote weighted process time matrix to {args.process_time_output}")


if __name__ == "__main__":
    main()
