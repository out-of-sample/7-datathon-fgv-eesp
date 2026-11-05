"""P3-25: Did observed trading composition recover when the premium did?

Inputs: frozen Binance USDTBRL hourly ZIPs, Foxbit and Mercado Bitcoin hourly
        CSVs in data/raw/, and data/processed/P1-02_premium_daily.csv.
Outputs: results/tables/P3-25_composition.csv,
         results/tables/P3-25_reference.csv,
         results/figures/P3-25_price_vs_share.png.
Run:     .venv/bin/python scripts/p3_25_composition.py

The retrospective windows and comparison rule were committed in P3-25 before
this script produced new results. Volumes are USDT base-asset units. All raw
candle timestamps are UTC; period dates and business hours are Brasilia (UTC-3).
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data/raw"
TABLES = ROOT / "results/tables"
FIGURES = ROOT / "results/figures"
TABLES.mkdir(parents=True, exist_ok=True)
FIGURES.mkdir(parents=True, exist_ok=True)

PERIODS = {
    "pre": ("2026-05-01", "2026-06-22"),
    "wave": ("2026-06-24", "2026-07-21"),
    "after": ("2026-07-22", "2026-10-30"),
}
EVENT_DATE = pd.Timestamp("2026-06-24")
LAST_BRT_DATE = pd.Timestamp("2026-10-30")


def checked_series(values: pd.Series, name: str) -> pd.Series:
    """Reject duplicate candle hours, bad volumes and non-hour timestamps."""
    values = values.sort_index()
    if values.index.has_duplicates:
        raise ValueError(f"{name}: duplicate UTC candle hour")
    if (values.index != values.index.floor("h")).any():
        raise ValueError(f"{name}: candle timestamp is not an exact UTC hour")
    if values.isna().any() or (values < 0).any():
        raise ValueError(f"{name}: missing or negative volume")
    return values.astype(float)


def load_hourly() -> pd.DataFrame:
    paths = sorted((RAW / "binance/USDTBRL").glob("*.zip"))
    if not paths:
        raise FileNotFoundError("No frozen Binance USDTBRL hourly ZIPs")
    parts = [pd.read_csv(path, header=None, usecols=[0, 5]) for path in paths]
    binance = pd.concat(parts, ignore_index=True)
    stamp = binance[0].astype("int64")
    # Binance changed its archive timestamps from milliseconds to microseconds.
    stamp = np.where(stamp > 10**14, stamp // 1000, stamp)
    binance = checked_series(pd.Series(binance[5].to_numpy(), index=pd.to_datetime(stamp, unit="ms")), "Binance")

    fox_raw = pd.read_csv(RAW / "foxbit/USDTBRL-1h.csv", usecols=["open_time_ms", "volume_usdt", "trades"])
    fox_idx = pd.to_datetime(fox_raw.open_time_ms, unit="ms")
    foxbit = checked_series(pd.Series(fox_raw.volume_usdt.to_numpy(), index=fox_idx), "Foxbit")
    trades = checked_series(pd.Series(fox_raw.trades.to_numpy(), index=fox_idx), "Foxbit trades")

    mb_raw = pd.read_csv(RAW / "mercadobitcoin/USDT-BRL-1h.csv", usecols=["t", "v"])
    mb = checked_series(pd.Series(mb_raw.v.to_numpy(), index=pd.to_datetime(mb_raw.t, unit="s")), "Mercado Bitcoin")

    first_hour = mb.index.min()
    # BRT 31 Oct 00:00 is UTC 31 Oct 03:00, exclusive.
    last_hour = LAST_BRT_DATE + pd.Timedelta(days=1, hours=3) - pd.Timedelta(hours=1)
    hours = pd.date_range(first_hour, last_hour, freq="h")
    frame = pd.DataFrame(index=hours)
    frame["binance"] = binance.reindex(hours)
    frame["foxbit"] = foxbit.reindex(hours)
    frame["fox_trades"] = trades.reindex(hours)
    frame["mb_observed"] = mb.reindex(hours).notna()
    frame["mb"] = mb.reindex(hours).fillna(0.0)
    frame["eligible"] = frame.binance.notna() & frame.foxbit.notna() & frame.fox_trades.notna()
    frame["date_brt"] = (frame.index - pd.Timedelta(hours=3)).normalize()
    frame["hour_brt"] = (frame.index - pd.Timedelta(hours=3)).hour
    return frame


def daily_table(hourly: pd.DataFrame) -> pd.DataFrame:
    retained = hourly[hourly.eligible].copy()
    retained["fox_business"] = retained.foxbit.where(retained.hour_brt.between(9, 17), 0)
    grouped = retained.groupby("date_brt")
    sums = grouped[["binance", "foxbit", "mb", "fox_trades", "fox_business"]].sum()
    counts = hourly.groupby("date_brt").agg(
        expected_hours=("eligible", "size"),
        eligible_hours=("eligible", "sum"),
        binance_missing_hours=("binance", lambda x: x.isna().sum()),
        foxbit_missing_hours=("foxbit", lambda x: x.isna().sum()),
        mb_no_candle_hours=("mb_observed", lambda x: (~x).sum()),
    )
    daily = counts.join(sums, how="left").fillna({col: 0 for col in sums.columns})
    daily["fox_share"] = daily.foxbit / daily[["binance", "foxbit", "mb"]].sum(axis=1).replace(0, np.nan)
    daily["fox_avg_trade"] = daily.foxbit / daily.fox_trades.replace(0, np.nan)
    return daily


def window_row(daily: pd.DataFrame, label: str, start: str | pd.Timestamp, end: str | pd.Timestamp) -> dict:
    period = daily.loc[pd.Timestamp(start):pd.Timestamp(end)]
    volumes = period[["binance", "foxbit", "mb"]].sum()
    total = volumes.sum()
    if len(period) != (pd.Timestamp(end) - pd.Timestamp(start)).days + 1 or total <= 0:
        raise ValueError(f"{label}: incomplete BRT dates or zero total volume")
    return {
        "period": label,
        "start_brt": pd.Timestamp(start).date().isoformat(),
        "end_brt": pd.Timestamp(end).date().isoformat(),
        "calendar_days": len(period),
        "expected_hours": int(period.expected_hours.sum()),
        "eligible_hours": int(period.eligible_hours.sum()),
        "binance_missing_hours": int(period.binance_missing_hours.sum()),
        "foxbit_missing_hours": int(period.foxbit_missing_hours.sum()),
        "mb_no_candle_hours": int(period.mb_no_candle_hours.sum()),
        "binance_volume_usdt": volumes.binance,
        "foxbit_volume_usdt": volumes.foxbit,
        "mb_volume_usdt": volumes.mb,
        "foxbit_share_pct": 100 * volumes.foxbit / total,
        "foxbit_median_daily_trade_usdt": period.fox_avg_trade.median(),
        "foxbit_business_hour_volume_pct": 100 * period.fox_business.sum() / volumes.foxbit,
    }


def historical_reference(daily: pd.DataFrame) -> pd.DataFrame:
    pre_length = (pd.Timestamp(PERIODS["pre"][1]) - pd.Timestamp(PERIODS["pre"][0])).days + 1
    after_length = (pd.Timestamp(PERIODS["after"][1]) - pd.Timestamp(PERIODS["after"][0])).days + 1
    rows = []
    for start in pd.date_range(daily.index.min(), daily.index.max() - pd.Timedelta(days=pre_length + after_length - 1)):
        pre_end = start + pd.Timedelta(days=pre_length - 1)
        after_start = pre_end + pd.Timedelta(days=1)
        after_end = after_start + pd.Timedelta(days=after_length - 1)
        if start <= EVENT_DATE <= after_end:
            continue
        first = window_row(daily, "reference_pre", start, pre_end)
        second = window_row(daily, "reference_after", after_start, after_end)
        rows.append({
            "start_brt": start.date().isoformat(),
            "pre_end_brt": pre_end.date().isoformat(),
            "after_start_brt": after_start.date().isoformat(),
            "end_brt": after_end.date().isoformat(),
            "pre_foxbit_share_pct": first["foxbit_share_pct"],
            "after_foxbit_share_pct": second["foxbit_share_pct"],
            "delta_percentage_points": second["foxbit_share_pct"] - first["foxbit_share_pct"],
            "pre_eligible_hours": first["eligible_hours"],
            "after_eligible_hours": second["eligible_hours"],
        })
    return pd.DataFrame(rows)


def plot(daily: pd.DataFrame) -> None:
    premium = pd.read_csv(ROOT / "data/processed/P1-02_premium_daily.csv", parse_dates=["date_brt"])
    premium = premium.set_index("date_brt").premium_bps
    view = daily.loc["2026-04-01":"2026-10-30"].copy()
    fig, left = plt.subplots(figsize=(11.5, 5.2))
    right = left.twinx()
    left.plot(premium.loc[view.index.min():view.index.max()].index,
              premium.loc[view.index.min():view.index.max()].values,
              color="#334155", lw=1.4, label="Prêmio USDT/BRL sobre PTAX (p.b.)")
    right.plot(view.index, 100 * view.fox_share.rolling(7, min_periods=1).mean(),
               color="#d97706", lw=2.2, label="Participação da Foxbit (média móvel, 7 dias)")
    left.axvspan(pd.Timestamp("2026-06-24"), pd.Timestamp("2026-07-22"), color="#fef3c7", alpha=0.65)
    left.axvline(pd.Timestamp("2026-06-23"), color="#b91c1c", ls="--", lw=1)
    left.text(pd.Timestamp("2026-06-25"), left.get_ylim()[1] * 0.93, "23 jun: ofício", color="#991b1b", fontsize=9)
    left.set_ylabel("Prêmio (pontos-base)", color="#334155")
    right.set_ylabel("Foxbit / três corretoras (% do volume USDT)", color="#b45309")
    left.set_title("O prêmio recuou; a participação da Foxbit permaneceu elevada")
    left.grid(axis="y", alpha=0.2)
    fig.text(0.01, 0.01, "Volume: USDT negociado em horas comuns; Mercado Bitcoin sem negócio = zero. "
             "Participação: média móvel de 7 dias; comparação principal usa volumes somados por período.", fontsize=8)
    fig.tight_layout(rect=(0, 0.04, 1, 1))
    fig.savefig(FIGURES / "P3-25_price_vs_share.png", dpi=180)
    plt.close(fig)


def main() -> None:
    hourly = load_hourly()
    daily = daily_table(hourly)
    episode = pd.DataFrame([window_row(daily, label, *period) for label, period in PERIODS.items()])
    episode.to_csv(TABLES / "P3-25_composition.csv", index=False, float_format="%.6f")
    reference = historical_reference(daily)
    reference.to_csv(TABLES / "P3-25_reference.csv", index=False, float_format="%.6f")
    plot(daily)
    pre = episode.set_index("period").loc["pre", "foxbit_share_pct"]
    after = episode.set_index("period").loc["after", "foxbit_share_pct"]
    delta = after - pre
    exceed = (reference.delta_percentage_points.abs() >= abs(delta)).sum()
    print(episode.to_string(index=False, float_format=lambda x: f"{x:,.2f}"))
    print(f"After − pre Foxbit share: {delta:+.2f} percentage points; historical adjacent-window pairs: "
          f"{len(reference)}, |change| >= observed: {exceed} ({exceed / len(reference):.3f}).")
    changes = reference.delta_percentage_points
    print(f"Historical signed change: min {changes.min():+.2f}, max {changes.max():+.2f}; "
          f"2.5th–97.5th percentile {changes.quantile(.025):+.2f} to {changes.quantile(.975):+.2f} percentage points.")


if __name__ == "__main__":
    main()
