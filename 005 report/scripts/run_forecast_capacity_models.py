"""Run publishable forecast and capacity models for the LOG650 report.

The script intentionally uses only anonymized/public model inputs. It writes
validation forecasts and an index-scale LP smoke test to 004 data/processed/.

Run from the repository root:
uv run --python 3.12 --with pandas --with scipy --with statsmodels python "005 report/scripts/run_forecast_capacity_models.py"
"""

from __future__ import annotations

import itertools
import json
import math
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
import scipy
import statsmodels
from scipy.optimize import linprog
from statsmodels.stats.diagnostic import acorr_ljungbox
from statsmodels.tsa.statespace.sarimax import SARIMAX


REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = REPO_ROOT / "004 data"
OUTPUT_DIR = DATA_DIR / "processed"

VOLUME_FILE = DATA_DIR / "weekly_volume_anonymized.csv"
PROCESS_TIME_FILE = DATA_DIR / "process_time_matrix.csv"
CAPACITY_FILE = DATA_DIR / "capacity_assumptions.csv"
ACTION_FILE = DATA_DIR / "action_parameters.csv"
ZONE_FILE = DATA_DIR / "zone_cutoff_profile.csv"

TRAIN_END_WEEK = "2025-52"
VALID_START_WEEK = "2026-01"
VALID_END_WEEK = "2026-13"
SEASONAL_PERIOD = 52
SLACK_PENALTY = 1000.0


ORDERS = [
    (0, 0, 0),
    (1, 0, 0),
    (0, 0, 1),
    (1, 0, 1),
    (2, 0, 0),
    (0, 0, 2),
    (0, 1, 0),
    (1, 1, 0),
    (0, 1, 1),
    (1, 1, 1),
]

SEASONAL_ORDERS = [
    (0, 0, 0, SEASONAL_PERIOD),
    (1, 0, 0, SEASONAL_PERIOD),
    (0, 1, 0, SEASONAL_PERIOD),
    (1, 1, 0, SEASONAL_PERIOD),
]

EXOGENEOUS_CANDIDATES = ["campaign_flag", "holiday_flag"]


def ensure_output_dir() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def read_inputs() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    volume = pd.read_csv(VOLUME_FILE, dtype={"year_week": str})
    process_time = pd.read_csv(PROCESS_TIME_FILE)
    capacity = pd.read_csv(CAPACITY_FILE)
    action = pd.read_csv(ACTION_FILE)
    zone = pd.read_csv(ZONE_FILE)

    volume["week_start_date"] = pd.to_datetime(volume["week_start_date"])
    for col in ["volume_index", "campaign_flag", "holiday_flag", "anomaly_flag", "constrained_week_flag"]:
        volume[col] = pd.to_numeric(volume[col], errors="coerce")
    volume = volume.sort_values(["stream_id", "week_start_date"]).reset_index(drop=True)

    process_time["minutes_per_fpk"] = pd.to_numeric(process_time["minutes_per_fpk"], errors="coerce")
    capacity["base_hours_per_week"] = pd.to_numeric(capacity["base_hours_per_week"], errors="coerce")
    action["max_hours_per_week"] = pd.to_numeric(action["max_hours_per_week"], errors="coerce")
    action["relative_cost_weight"] = pd.to_numeric(action["relative_cost_weight"], errors="coerce")
    zone["share_of_weekly_volume"] = pd.to_numeric(zone["share_of_weekly_volume"], errors="coerce")

    return volume, process_time, capacity, action, zone


def metric_dict(actual: pd.Series, forecast: pd.Series) -> dict[str, float]:
    actual_arr = actual.to_numpy(dtype=float)
    forecast_arr = forecast.to_numpy(dtype=float)
    error = actual_arr - forecast_arr
    mae = np.mean(np.abs(error))
    rmse = math.sqrt(np.mean(error**2))
    with np.errstate(divide="ignore", invalid="ignore"):
        ape = np.abs(error / actual_arr)
    mape = np.nanmean(ape[np.isfinite(ape)]) * 100
    return {"mae": float(mae), "rmse": float(rmse), "mape": float(mape)}


def aicc(result, nobs: int) -> float:
    k_params = len(result.params)
    denominator = nobs - k_params - 1
    if denominator <= 0:
        return float("nan")
    return float(result.aic + (2 * k_params * (k_params + 1)) / denominator)


def previous_year_week(year_week: str) -> str:
    year, week = year_week.split("-")
    return f"{int(year) - 1}-{week}"


def snaive_for_validation(stream_df: pd.DataFrame, valid_df: pd.DataFrame) -> pd.Series:
    values_by_week = stream_df.set_index("year_week")["volume_index"]
    forecasts = []
    for week in valid_df["year_week"]:
        forecasts.append(values_by_week.loc[previous_year_week(week)])
    return pd.Series(forecasts, index=valid_df.index, dtype=float)


def usable_exog_columns(train_df: pd.DataFrame) -> list[str]:
    columns: list[str] = []
    for col in EXOGENEOUS_CANDIDATES:
        values = train_df[col].dropna().astype(int)
        counts = values.value_counts()
        if len(counts) < 2:
            continue
        if counts.min() < 3:
            continue
        columns.append(col)
    return columns


def exog_sets(columns: list[str]) -> list[tuple[str, ...]]:
    sets: list[tuple[str, ...]] = [tuple()]
    for col in columns:
        sets.append((col,))
    if len(columns) > 1:
        sets.append(tuple(columns))
    return sets


def fit_sarimax_grid(
    stream: str,
    train_df: pd.DataFrame,
    valid_df: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.Series | None, dict[str, object] | None]:
    train_index = pd.date_range(
        start=train_df["week_start_date"].iloc[0],
        periods=len(train_df),
        freq="W-MON",
    )
    valid_index = pd.date_range(
        start=valid_df["week_start_date"].iloc[0],
        periods=len(valid_df),
        freq="W-MON",
    )
    y_train = pd.Series(train_df["volume_index"].to_numpy(dtype=float), index=train_index)
    y_valid = valid_df["volume_index"].astype(float)
    records: list[dict[str, object]] = []
    fitted_forecasts: dict[int, pd.Series] = {}

    candidate_index = 0
    for exog_cols in exog_sets(usable_exog_columns(train_df)):
        if exog_cols:
            x_train = pd.DataFrame(
                train_df[list(exog_cols)].to_numpy(dtype=float),
                index=train_index,
                columns=list(exog_cols),
            )
            x_valid = pd.DataFrame(
                valid_df[list(exog_cols)].to_numpy(dtype=float),
                index=valid_index,
                columns=list(exog_cols),
            )
        else:
            x_train = None
            x_valid = None

        for order, seasonal_order in itertools.product(ORDERS, SEASONAL_ORDERS):
            candidate_index += 1
            trend = "c" if order[1] == 0 and seasonal_order[1] == 0 else "n"
            record: dict[str, object] = {
                "stream_id": stream,
                "candidate_id": candidate_index,
                "order": str(order),
                "seasonal_order": str(seasonal_order),
                "exog": "+".join(exog_cols) if exog_cols else "none",
                "trend": trend,
            }

            try:
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore")
                    model = SARIMAX(
                        y_train,
                        order=order,
                        seasonal_order=seasonal_order,
                        exog=x_train,
                        trend=trend,
                        enforce_stationarity=False,
                        enforce_invertibility=False,
                    )
                    result = model.fit(disp=False, maxiter=150)
                    raw_forecast = result.get_forecast(steps=len(valid_df), exog=x_valid).predicted_mean
                    forecast = pd.Series(
                        np.maximum(raw_forecast.to_numpy(dtype=float), 0.0),
                        index=valid_df.index,
                    )
                    metrics = metric_dict(y_valid, forecast)
                    residuals = pd.Series(result.resid).replace([np.inf, -np.inf], np.nan).dropna()
                    if len(residuals) > 12:
                        lb = acorr_ljungbox(residuals, lags=[10], return_df=True)
                        ljung_box_p10 = float(lb["lb_pvalue"].iloc[0])
                    else:
                        ljung_box_p10 = float("nan")

                    record.update(
                        {
                            "status": "ok",
                            "converged": bool(result.mle_retvals.get("converged", False)),
                            "aic": float(result.aic),
                            "bic": float(result.bic),
                            "aicc": aicc(result, int(result.nobs)),
                            "llf": float(result.llf),
                            "n_params": int(len(result.params)),
                            "ljung_box_p10": ljung_box_p10,
                            **metrics,
                        }
                    )
                fitted_forecasts[candidate_index] = forecast
            except Exception as exc:  # noqa: BLE001 - all model failures are candidate outcomes
                record.update({"status": f"failed: {type(exc).__name__}", "error": str(exc)[:250]})

            records.append(record)

    candidates = pd.DataFrame(records)
    ok = candidates[candidates["status"].eq("ok") & candidates["converged"].eq(True)].copy()
    if ok.empty:
        ok = candidates[candidates["status"].eq("ok")].copy()
    if ok.empty:
        return candidates, None, None

    ok = ok.sort_values(["rmse", "aicc", "n_params"], ascending=[True, True, True])
    best = ok.iloc[0].to_dict()
    best_forecast = fitted_forecasts[int(best["candidate_id"])]
    return candidates, best_forecast, best


def minutes_per_index_unit(process_time: pd.DataFrame, process_id: str, stream_id: str) -> float:
    exact = process_time[
        (process_time["process_id"].eq(process_id)) & (process_time["stream_id"].eq(stream_id))
    ]
    if not exact.empty:
        return float(exact["minutes_per_fpk"].iloc[0])
    generic = process_time[
        (process_time["process_id"].eq(process_id)) & (process_time["stream_id"].eq("ALL"))
    ]
    if not generic.empty:
        return float(generic["minutes_per_fpk"].iloc[0])
    raise KeyError(f"No process time for {process_id}/{stream_id}")


def standard_xmax_hours(action: pd.DataFrame, process_id: str) -> float:
    rows = action[
        (action["process_id"].eq(process_id))
        & (action["action_type"].eq("early_start_standard_holiday"))
    ]
    if rows.empty or pd.isna(rows["max_hours_per_week"].iloc[0]):
        return 0.0
    return float(rows["max_hours_per_week"].iloc[0])


def standard_cost_weight(action: pd.DataFrame, process_id: str) -> float:
    rows = action[
        (action["process_id"].eq(process_id))
        & (action["action_type"].eq("early_start_standard_holiday"))
    ]
    if rows.empty or pd.isna(rows["relative_cost_weight"].iloc[0]):
        return 1.0
    return float(rows["relative_cost_weight"].iloc[0])


def solve_week_lp(
    workload_minutes: dict[str, float],
    base_hours: dict[str, float],
    xmax_hours: dict[str, float],
    cost_weight: dict[str, float],
) -> dict[str, dict[str, float]]:
    processes = list(workload_minutes)
    c = []
    bounds = []
    a_ub = []
    b_ub = []

    # Variable order: X_processes, SLACK_processes.
    for process in processes:
        c.append(cost_weight[process])
        bounds.append((0.0, xmax_hours[process]))
    for _process in processes:
        c.append(SLACK_PENALTY)
        bounds.append((0.0, None))

    for i, process in enumerate(processes):
        row = [0.0] * (2 * len(processes))
        row[i] = -60.0
        row[len(processes) + i] = -1.0
        a_ub.append(row)
        b_ub.append((60.0 * base_hours[process]) - workload_minutes[process])

    result = linprog(c=c, A_ub=a_ub, b_ub=b_ub, bounds=bounds, method="highs")
    if not result.success:
        raise RuntimeError(result.message)

    rows: dict[str, dict[str, float]] = {}
    for i, process in enumerate(processes):
        extra_hours = float(result.x[i])
        slack_minutes = float(result.x[len(processes) + i])
        capacity_minutes = 60.0 * base_hours[process]
        rows[process] = {
            "workload_index_minutes": float(workload_minutes[process]),
            "workload_index_hours": float(workload_minutes[process] / 60.0),
            "base_reference_hours": float(base_hours[process]),
            "xmax_reference_hours": float(xmax_hours[process]),
            "extra_index_hours": extra_hours,
            "slack_index_minutes": slack_minutes,
            "utilization_vs_reference_capacity": float(workload_minutes[process] / capacity_minutes)
            if capacity_minutes
            else float("nan"),
        }
    return rows


def run_forecasts(volume: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, dict[str, object]]:
    model_df = volume[volume["year_week"].le(VALID_END_WEEK)].copy()
    train_df = model_df[model_df["year_week"].le(TRAIN_END_WEEK)].copy()
    valid_df = model_df[
        model_df["year_week"].between(VALID_START_WEEK, VALID_END_WEEK, inclusive="both")
    ].copy()

    candidate_frames: list[pd.DataFrame] = []
    forecast_rows: list[dict[str, object]] = []
    summary: dict[str, object] = {
        "train_weeks": int(train_df["year_week"].nunique()),
        "validation_weeks": int(valid_df["year_week"].nunique()),
        "excluded_weeks": sorted(set(volume["year_week"]) - set(model_df["year_week"])),
        "streams": {},
    }

    for stream in sorted(model_df["stream_id"].unique()):
        stream_all = model_df[model_df["stream_id"].eq(stream)].copy()
        stream_train = train_df[train_df["stream_id"].eq(stream)].copy()
        stream_valid = valid_df[valid_df["stream_id"].eq(stream)].copy()

        snaive = snaive_for_validation(stream_all, stream_valid)
        snaive_metrics = metric_dict(stream_valid["volume_index"], snaive)
        candidates, sarimax_forecast, best = fit_sarimax_grid(stream, stream_train, stream_valid)
        candidate_frames.append(candidates)

        if best is not None and sarimax_forecast is not None:
            sarimax_metrics = {
                "mae": float(best["mae"]),
                "rmse": float(best["rmse"]),
                "mape": float(best["mape"]),
            }
            use_sarimax = sarimax_metrics["rmse"] < snaive_metrics["rmse"]
            operational_model = "SARIMAX" if use_sarimax else "SNaive"
            operational_forecast = sarimax_forecast if use_sarimax else snaive
            selected_model = best
        else:
            sarimax_metrics = None
            operational_model = "SNaive"
            operational_forecast = snaive
            selected_model = None

        for idx, row in stream_valid.iterrows():
            sarimax_value = float(sarimax_forecast.loc[idx]) if sarimax_forecast is not None else float("nan")
            forecast_rows.append(
                {
                    "year_week": row["year_week"],
                    "week_start_date": row["week_start_date"].date().isoformat(),
                    "stream_id": stream,
                    "actual_index": float(row["volume_index"]),
                    "snaive_forecast_index": float(snaive.loc[idx]),
                    "sarimax_forecast_index": sarimax_value,
                    "operational_model": operational_model,
                    "operational_forecast_index": float(operational_forecast.loc[idx]),
                    "snaive_error": float(row["volume_index"] - snaive.loc[idx]),
                    "sarimax_error": float(row["volume_index"] - sarimax_value)
                    if sarimax_forecast is not None
                    else float("nan"),
                    "operational_error": float(row["volume_index"] - operational_forecast.loc[idx]),
                }
            )

        summary["streams"][stream] = {
            "snaive": snaive_metrics,
            "sarimax_selected": selected_model,
            "sarimax": sarimax_metrics,
            "operational_model": operational_model,
            "exog_columns_allowed": usable_exog_columns(stream_train),
        }

    candidate_df = pd.concat(candidate_frames, ignore_index=True)
    forecast_df = pd.DataFrame(forecast_rows).sort_values(["year_week", "stream_id"])
    return candidate_df, forecast_df, summary


def run_index_lp(
    forecast_df: pd.DataFrame,
    process_time: pd.DataFrame,
    capacity: pd.DataFrame,
    action: pd.DataFrame,
    zone: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame, dict[str, object]]:
    base_hours = {
        row["process_id"]: float(row["base_hours_per_week"])
        for _, row in capacity.iterrows()
        if row["process_id"] in {"P1", "P2"}
    }
    xmax_hours = {process: standard_xmax_hours(action, process) for process in base_hours}
    cost_weight = {process: standard_cost_weight(action, process) for process in base_hours}

    lp_rows: list[dict[str, object]] = []
    zone_rows: list[dict[str, object]] = []
    scenarios = {"base": 1.0, "volume_minus_10": 0.9, "volume_plus_10": 1.1}

    for scenario_name, scenario_multiplier in scenarios.items():
        for week, week_df in forecast_df.groupby("year_week"):
            workload = {}
            for process in base_hours:
                total = 0.0
                for _, row in week_df.iterrows():
                    minutes = minutes_per_index_unit(process_time, process, row["stream_id"])
                    total += float(row["operational_forecast_index"]) * scenario_multiplier * minutes
                workload[process] = total

            solution = solve_week_lp(workload, base_hours, xmax_hours, cost_weight)
            for process, values in solution.items():
                lp_rows.append(
                    {
                        "scenario": scenario_name,
                        "year_week": week,
                        "process_id": process,
                        **values,
                    }
                )

            p2_workload = workload.get("P2", 0.0)
            cumulative = 0.0
            for _, zone_row in zone.sort_values("zone_bucket").iterrows():
                share = float(zone_row["share_of_weekly_volume"])
                cumulative += share
                zone_rows.append(
                    {
                        "scenario": scenario_name,
                        "year_week": week,
                        "zone_bucket": zone_row["zone_bucket"],
                        "cutoff_label": zone_row["cutoff_label"],
                        "share_of_weekly_volume": share,
                        "cumulative_share": cumulative,
                        "p2_zone_workload_index_minutes": p2_workload * share,
                        "p2_cumulative_workload_index_minutes": p2_workload * cumulative,
                    }
                )

    lp_df = pd.DataFrame(lp_rows).sort_values(["scenario", "year_week", "process_id"])
    zone_df = pd.DataFrame(zone_rows).sort_values(["scenario", "year_week", "zone_bucket"])

    base_lp = lp_df[lp_df["scenario"].eq("base")]
    lp_summary = {
        "scale_note": (
            "LP uses anonymized volume_index multiplied by minutes_per_fpk. "
            "Outputs are index-minutes/index-hours and are not real worker-hours."
        ),
        "total_extra_index_hours_base": float(base_lp["extra_index_hours"].sum()),
        "total_slack_index_minutes_base": float(base_lp["slack_index_minutes"].sum()),
        "max_utilization_vs_reference_capacity_base": {
            process: float(rows["utilization_vs_reference_capacity"].max())
            for process, rows in base_lp.groupby("process_id")
        },
        "max_workload_index_hours_base": {
            process: float(rows["workload_index_hours"].max())
            for process, rows in base_lp.groupby("process_id")
        },
    }

    return lp_df, zone_df, lp_summary


def main() -> None:
    ensure_output_dir()
    volume, process_time, capacity, action, zone = read_inputs()

    candidate_df, forecast_df, summary = run_forecasts(volume)
    lp_df, zone_df, lp_summary = run_index_lp(forecast_df, process_time, capacity, action, zone)

    candidate_file = OUTPUT_DIR / "sarimax_candidate_results.csv"
    forecast_file = OUTPUT_DIR / "forecast_validation_results.csv"
    lp_file = OUTPUT_DIR / "lp_capacity_validation_index.csv"
    zone_file = OUTPUT_DIR / "lp_zone_deadline_load_index.csv"
    summary_file = OUTPUT_DIR / "model_run_summary.json"

    candidate_df.to_csv(candidate_file, index=False)
    forecast_df.to_csv(forecast_file, index=False)
    lp_df.to_csv(lp_file, index=False)
    zone_df.to_csv(zone_file, index=False)

    summary["lp_index"] = lp_summary
    summary["software"] = {
        "python": "3.12 via uv",
        "pandas": pd.__version__,
        "scipy": scipy.__version__,
        "statsmodels": statsmodels.__version__,
    }
    summary_file.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"Wrote {candidate_file}")
    print(f"Wrote {forecast_file}")
    print(f"Wrote {lp_file}")
    print(f"Wrote {zone_file}")
    print(f"Wrote {summary_file}")
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
