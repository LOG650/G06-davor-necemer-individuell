"""Build report figures for LOG650 final report (section 8.0 Resultater).

Uses only anonymized/index-scale data so the figures are publishable.
All outputs land in ``005 report/figures/`` as 300 dpi PNG.

Run from the repository root:
    uv run --python 3.12 --with pandas --with numpy --with matplotlib \
        python "005 report/scripts/build_report_figures.py"
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import pandas as pd

REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = REPO_ROOT / "004 data"
PROC_DIR = DATA_DIR / "processed"
FIG_DIR = REPO_ROOT / "005 report" / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

# Academic style — light background, sober palette.
plt.rcParams.update(
    {
        "figure.dpi": 110,
        "savefig.dpi": 300,
        "savefig.bbox": "tight",
        "font.family": "DejaVu Sans",
        "font.size": 10,
        "axes.titlesize": 12,
        "axes.titleweight": "bold",
        "axes.labelsize": 10,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.alpha": 0.25,
        "grid.linestyle": "--",
        "legend.frameon": False,
    }
)

# Stream colours — F = ferskvare, S = sekundærvare.
COLOR_F = "#1f4e79"   # deep blue
COLOR_S = "#c0504d"   # warm red
COLOR_BASE = "#7f7f7f"
COLOR_LOW = "#2ca02c"
COLOR_HIGH = "#d62728"
NOTE_INDEX = "Indeks: 2024-snitt per varestrøm = 100"


def _load_volume() -> pd.DataFrame:
    df = pd.read_csv(DATA_DIR / "weekly_volume_anonymized.csv")
    df["week_start_date"] = pd.to_datetime(df["week_start_date"])
    df["iso_week"] = df["year_week"].str.slice(5).astype(int)
    df["iso_year"] = df["year_week"].str.slice(0, 4).astype(int)
    return df


def _save(fig: plt.Figure, name: str) -> Path:
    out = FIG_DIR / name
    fig.savefig(out)
    plt.close(fig)
    print(f"  wrote {out.relative_to(REPO_ROOT)}")
    return out


# ---------------------------------------------------------------------------
# Figure 1 — Volumtrend 2024-2026 (F og S)
# ---------------------------------------------------------------------------
def fig_volume_trend(volume: pd.DataFrame) -> None:
    fig, axes = plt.subplots(2, 1, figsize=(10.5, 6.5), sharex=True)
    for ax, stream, color, label in (
        (axes[0], "F", COLOR_F, "F – ferskvare"),
        (axes[1], "S", COLOR_S, "S – sekundærvare"),
    ):
        sub = volume[volume["stream_id"] == stream].sort_values("week_start_date")
        ax.plot(
            sub["week_start_date"], sub["volume_index"],
            color=color, linewidth=1.4, label=label,
        )
        # Highlight campaign weeks.
        camp = sub[sub["campaign_flag"] == 1]
        ax.scatter(
            camp["week_start_date"], camp["volume_index"],
            color=color, s=14, alpha=0.55,
            label="Kampanjeuke" if stream == "S" else None,
            zorder=3,
        )
        # Highlight holiday weeks.
        hol = sub[sub["holiday_flag"] == 1]
        ax.scatter(
            hol["week_start_date"], hol["volume_index"],
            facecolor="none", edgecolor="black", s=42, linewidth=0.8,
            label="Helligdagsuke" if stream == "S" else None,
            zorder=4,
        )
        ax.axhline(100, color="black", linewidth=0.6, alpha=0.4)
        ax.set_ylabel("Volumindeks")
        ax.set_title(label, loc="left")
    axes[1].set_xlabel("Uke (start)")
    axes[1].xaxis.set_major_locator(mdates.MonthLocator(bymonth=[1, 7]))
    axes[1].xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
    axes[1].legend(loc="upper left", ncol=2, fontsize=8)
    fig.suptitle(
        "Ukentlig volumtrend per varestrøm, 2024-W01 – 2026-W19",
        fontsize=13, fontweight="bold", y=0.995,
    )
    fig.text(
        0.01, 0.005,
        f"{NOTE_INDEX}. Sirkler = helligdagsuker.",
        fontsize=8, alpha=0.7,
    )
    _save(fig, "01_volumtrend.png")


# ---------------------------------------------------------------------------
# Figure 2 — Sesongmønster (heatmap: ISO-uke × år)
# ---------------------------------------------------------------------------
def fig_seasonality(volume: pd.DataFrame) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.6))
    for ax, stream, cmap, title in (
        (axes[0], "F", "Blues", "F – ferskvare"),
        (axes[1], "S", "Reds", "S – sekundærvare"),
    ):
        sub = volume[volume["stream_id"] == stream].copy()
        pivot = sub.pivot_table(
            index="iso_year", columns="iso_week",
            values="volume_index", aggfunc="mean",
        )
        im = ax.imshow(
            pivot.values, aspect="auto", cmap=cmap,
            vmin=np.nanpercentile(pivot.values, 5),
            vmax=np.nanpercentile(pivot.values, 95),
        )
        ax.set_yticks(range(len(pivot.index)))
        ax.set_yticklabels(pivot.index)
        ax.set_xticks(range(0, pivot.shape[1], 4))
        ax.set_xticklabels(pivot.columns[::4])
        ax.set_xlabel("ISO-uke")
        ax.set_ylabel("År")
        ax.set_title(title, loc="left")
        ax.grid(False)
        # Mark Easter / Christmas / Summer-low approximate windows.
        for week, label in ((13, "Påske"), (28, "Sommer"), (51, "Jul")):
            if week - 1 < pivot.shape[1]:
                ax.axvline(week - 1, color="black", linewidth=0.6, linestyle=":", alpha=0.6)
                ax.text(
                    week - 1, -0.6, label,
                    rotation=90, fontsize=7, ha="center", va="bottom", alpha=0.7,
                )
        cbar = fig.colorbar(im, ax=ax, shrink=0.85)
        cbar.set_label("Volumindeks", fontsize=8)
    fig.suptitle(
        "Sesongmønster per ISO-uke (varmkart, indekssnitt)",
        fontsize=13, fontweight="bold", y=1.02,
    )
    fig.text(
        0.01, -0.04,
        f"{NOTE_INDEX}. Stiplede linjer markerer typiske høytider/sommer-bunn.",
        fontsize=8, alpha=0.7,
    )
    _save(fig, "02_sesongmonster.png")


# ---------------------------------------------------------------------------
# Figure 3 — Prognose-validering (linje: actual vs SARIMAX vs SNaive)
# ---------------------------------------------------------------------------
def fig_forecast_validation() -> None:
    val = pd.read_csv(PROC_DIR / "forecast_validation_results.csv")
    val["week_start_date"] = pd.to_datetime(val["week_start_date"])

    # Pull MAE/RMSE/MAPE from model_run_summary for inset text.
    import json
    summary = json.loads((PROC_DIR / "model_run_summary.json").read_text())
    metrics_f = summary["streams"]["F"]
    metrics_s = summary["streams"]["S"]

    fig, axes = plt.subplots(1, 2, figsize=(12, 4.8), sharey=False)
    panels = (
        (axes[0], "F", COLOR_F, metrics_f),
        (axes[1], "S", COLOR_S, metrics_s),
    )
    for ax, stream, color, m in panels:
        sub = val[val["stream_id"] == stream].sort_values("week_start_date")
        ax.plot(sub["week_start_date"], sub["actual_index"],
                color="black", linewidth=1.6, marker="o", markersize=4, label="Faktisk")
        ax.plot(sub["week_start_date"], sub["sarimax_forecast_index"],
                color=color, linewidth=1.4, linestyle="--", marker="s", markersize=3.5,
                label="SARIMAX")
        ax.plot(sub["week_start_date"], sub["snaive_forecast_index"],
                color=COLOR_BASE, linewidth=1.1, linestyle=":", marker="^", markersize=3.5,
                label="SNaive")
        ax.set_title(f"Varestrøm {stream}", loc="left")
        ax.set_xlabel("Valideringsuke")
        ax.set_ylabel("Volumindeks")
        ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=2))
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-W%V"))
        for tick in ax.get_xticklabels():
            tick.set_rotation(35)
            tick.set_ha("right")
        # Metrics box.
        textstr = (
            f"SARIMAX  MAE={m['sarimax']['mae']:.1f}  RMSE={m['sarimax']['rmse']:.1f}  MAPE={m['sarimax']['mape']:.1f}%\n"
            f"SNaive   MAE={m['snaive']['mae']:.1f}  RMSE={m['snaive']['rmse']:.1f}  MAPE={m['snaive']['mape']:.1f}%"
        )
        ax.text(
            0.02, 0.97, textstr, transform=ax.transAxes,
            fontsize=8, va="top", ha="left", family="monospace",
            bbox=dict(boxstyle="round,pad=0.35", facecolor="white", edgecolor="lightgray"),
        )
        ax.legend(loc="lower left", fontsize=8)
    fig.suptitle(
        "Out-of-sample prognose-validering, 2026-W01 til 2026-W13",
        fontsize=13, fontweight="bold", y=1.0,
    )
    fig.tight_layout(rect=(0, 0.06, 1, 0.97))
    fig.text(
        0.01, 0.005,
        f"{NOTE_INDEX}. Uke 2026-W14 ekskludert (kun to virkedager).",
        fontsize=8, alpha=0.7,
    )
    _save(fig, "03_prognose_validering.png")


# ---------------------------------------------------------------------------
# Figure 4 — Kapasitets-scenarioer (LP indeks-skala)
# ---------------------------------------------------------------------------
def fig_capacity_scenarios() -> None:
    lp = pd.read_csv(PROC_DIR / "lp_capacity_validation_index.csv")
    # Aggregate per scenario × process: maximum utilisation across the 13 weeks.
    util = (
        lp.groupby(["scenario", "process_id"])["utilization_vs_reference_capacity"]
        .agg(["max", "mean"])
        .reset_index()
    )
    util["max_pct"] = util["max"] * 100.0
    util["mean_pct"] = util["mean"] * 100.0

    scenario_order = ["volume_minus_10", "base", "volume_plus_10"]
    scenario_label = {
        "volume_minus_10": "−10 % volum",
        "base": "Basis",
        "volume_plus_10": "+10 % volum",
    }
    scenario_color = {
        "volume_minus_10": COLOR_LOW,
        "base": COLOR_BASE,
        "volume_plus_10": COLOR_HIGH,
    }

    fig, axes = plt.subplots(1, 2, figsize=(11, 4.6), sharey=False)
    for ax, proc, title in (
        (axes[0], "P1", "P1 – PD/grovfordeling (referansekapasitet 24 t/uke)"),
        (axes[1], "P2", "P2 – ED/ekspedering (referansekapasitet 144 t/uke)"),
    ):
        sub = util[util["process_id"] == proc].set_index("scenario").reindex(scenario_order)
        x = np.arange(len(scenario_order))
        ax.bar(
            x - 0.18, sub["mean_pct"], width=0.36,
            color=[scenario_color[s] for s in scenario_order], alpha=0.55, label="Snitt",
        )
        ax.bar(
            x + 0.18, sub["max_pct"], width=0.36,
            color=[scenario_color[s] for s in scenario_order], alpha=0.95, label="Maks",
        )
        for i, s in enumerate(scenario_order):
            ax.text(
                i + 0.18, sub.loc[s, "max_pct"],
                f"{sub.loc[s, 'max_pct']:.3f} %",
                ha="center", va="bottom", fontsize=8,
            )
        ax.set_xticks(x)
        ax.set_xticklabels([scenario_label[s] for s in scenario_order])
        ax.set_ylabel("Utnyttelse mot referansekapasitet (%)")
        ax.set_title(title, loc="left", fontsize=10)
        ax.legend(loc="upper left", fontsize=8)
    fig.suptitle(
        "LP indeks-skala smoke-test: kapasitetsutnyttelse per scenario",
        fontsize=13, fontweight="bold", y=1.0,
    )
    fig.text(
        0.01, -0.05,
        "Tallene er indeks-prosent (volume_index × min/FPK), ikke faktiske mann-timer. "
        "Ingen scenario bryter referansekapasiteten.",
        fontsize=8, alpha=0.7,
    )
    _save(fig, "04_kapasitet_scenarioer.png")


# ---------------------------------------------------------------------------
# Figure 5 — Sone-fordeling med kumulativ frist-belastning
# ---------------------------------------------------------------------------
def fig_zone_distribution() -> None:
    zones = pd.read_csv(DATA_DIR / "zone_cutoff_profile.csv")
    zones = zones.sort_values("zone_bucket")
    shares = zones["share_of_weekly_volume"].to_numpy() * 100
    cum = np.cumsum(shares)
    labels = [f"{r.zone_bucket}\nfrist {r.cutoff_label}" for r in zones.itertuples()]

    fig, ax1 = plt.subplots(figsize=(8.5, 4.6))
    bar_colors = ["#5b9bd5", "#ed7d31", "#a5a5a5"]
    bars = ax1.bar(labels, shares, color=bar_colors, edgecolor="black", linewidth=0.5)
    for bar, val in zip(bars, shares):
        ax1.text(
            bar.get_x() + bar.get_width() / 2, val + 0.5,
            f"{val:.1f} %", ha="center", va="bottom", fontsize=10, fontweight="bold",
        )
    ax1.set_ylabel("Andel av ukevolum (%)")
    ax1.set_ylim(0, 110)

    ax2 = ax1.twinx()
    ax2.plot(labels, cum, color="black", marker="o", linewidth=1.4, label="Kumulativ andel")
    for x, y in zip(labels, cum):
        ax2.text(x, y + 2, f"{y:.1f} %", ha="center", va="bottom", fontsize=8)
    ax2.set_ylabel("Kumulativ andel ved frist (%)")
    ax2.set_ylim(0, 110)
    ax2.grid(False)

    ax1.set_title(
        "Sonevise andeler av ukevolum og kumulativ frist-belastning",
        loc="left", fontsize=12, fontweight="bold",
    )
    fig.text(
        0.01, -0.04,
        "Basert på ED-dispatcher historikk 2023-07-21 til 2026-04-28 (643 valgte datoer).",
        fontsize=8, alpha=0.7,
    )
    _save(fig, "05_sonefordeling.png")


# ---------------------------------------------------------------------------
# Figure 6 — Volatilitet: kampanje vs ikke-kampanje
# ---------------------------------------------------------------------------
def fig_volatility(volume: pd.DataFrame) -> None:
    df = volume.copy()
    df["segment"] = df["campaign_flag"].map({1: "Kampanje", 0: "Uten kampanje"})
    streams = ["F", "S"]

    fig, axes = plt.subplots(1, 2, figsize=(11, 4.6))

    # Left: boxplot per stream × segment.
    ax = axes[0]
    positions = []
    data = []
    labels = []
    palette = []
    for i, stream in enumerate(streams):
        for j, seg in enumerate(["Uten kampanje", "Kampanje"]):
            sub = df[(df["stream_id"] == stream) & (df["segment"] == seg)]["volume_index"]
            if len(sub) == 0:
                continue
            positions.append(i * 2.5 + j)
            data.append(sub.values)
            labels.append(f"{stream}\n{seg}\n(n={len(sub)})")
            palette.append(COLOR_F if stream == "F" else COLOR_S)
    bp = ax.boxplot(
        data, positions=positions, widths=0.7, patch_artist=True,
        medianprops=dict(color="black", linewidth=1.4),
    )
    for patch, color in zip(bp["boxes"], palette):
        patch.set_facecolor(color)
        patch.set_alpha(0.55)
    ax.set_xticks(positions)
    ax.set_xticklabels(labels, fontsize=8)
    ax.set_ylabel("Volumindeks per uke")
    ax.set_title("Boks-plott: ukesfordeling per varestrøm × kampanje", loc="left", fontsize=10)

    # Right: CV table-style bar.
    ax2 = axes[1]
    cv_rows = []
    for stream in streams:
        for seg in ["Uten kampanje", "Kampanje"]:
            sub = df[(df["stream_id"] == stream) & (df["segment"] == seg)]["volume_index"]
            if len(sub) == 0 or sub.mean() == 0:
                continue
            cv_rows.append(
                {
                    "label": f"{stream} – {seg}",
                    "cv": sub.std(ddof=0) / sub.mean(),
                    "n": len(sub),
                    "stream": stream,
                }
            )
    cv = pd.DataFrame(cv_rows)
    bar_colors = [COLOR_F if s == "F" else COLOR_S for s in cv["stream"]]
    bars = ax2.barh(cv["label"], cv["cv"] * 100, color=bar_colors, alpha=0.8)
    for bar, val, n in zip(bars, cv["cv"] * 100, cv["n"]):
        ax2.text(val + 0.5, bar.get_y() + bar.get_height() / 2,
                 f"{val:.1f} % (n={n})", va="center", fontsize=8)
    ax2.set_xlabel("Variasjonskoeffisient (CV %)")
    ax2.set_title("CV per segment (lavere = mer stabil)", loc="left", fontsize=10)
    ax2.set_xlim(0, max(cv["cv"] * 100) * 1.25)

    fig.suptitle(
        "Volatilitet i ukesvolumer: kampanje vs. ikke-kampanje",
        fontsize=13, fontweight="bold", y=1.0,
    )
    fig.text(
        0.01, -0.04,
        f"{NOTE_INDEX}. F er kampanje-aktiv i ~99 % av ukene; for S dominerer ikke-kampanje-uker.",
        fontsize=8, alpha=0.7,
    )
    _save(fig, "06_volatilitet.png")


def main() -> None:
    print("Bygger rapportfigurer ...")
    volume = _load_volume()
    fig_volume_trend(volume)
    fig_seasonality(volume)
    fig_forecast_validation()
    fig_capacity_scenarios()
    fig_zone_distribution()
    fig_volatility(volume)
    print(f"Ferdig. Filer i {FIG_DIR.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
