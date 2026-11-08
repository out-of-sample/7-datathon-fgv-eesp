"""P3-47: bounded checks on whether Foxbit order flow helps explain the July premium recovery.

Inputs: frozen data/raw/foxbit/USDTBRL-1h.csv and its SHA256SUMS entry;
        results/tables/P3-19_daily.csv (morning premium, venue gap, afternoon flow).
Outputs: results/tables/P3-47_recovery_checks.csv and P3-47_coverage.csv.
Run:    python scripts/p3_47_recovery_check.py
The fixed specification is tasks/P3-47-recovery-mechanism-check.md.
"""

from __future__ import annotations

import hashlib
from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data/raw/foxbit/USDTBRL-1h.csv"
MANIFEST = ROOT / "data/raw/SHA256SUMS"
TABLES = ROOT / "results/tables"
DAILY = TABLES / "P3-19_daily.csv"
START, END = "2026-06-24", "2026-09-30"
N_BOOT, SEED = 2000, 47


def verify_hash() -> str:
    key = "data/raw/foxbit/USDTBRL-1h.csv"
    matches = [line.split()[0] for line in MANIFEST.read_text().splitlines() if line.endswith(key)]
    if len(matches) != 1:
        raise ValueError(f"Expected one manifest entry for {key}, found {len(matches)}")
    with RAW.open("rb") as source:
        digest = hashlib.file_digest(source, "sha256").hexdigest()
    if digest != matches[0]:
        raise ValueError(f"Foxbit raw hash mismatch: {digest} != {matches[0]}")
    return digest


def fit(y: np.ndarray, predictors: np.ndarray, weeks: np.ndarray | None = None) -> tuple[np.ndarray, float]:
    if weeks is None:
        design = np.column_stack((np.ones(len(y)), predictors))
    else:
        frame = pd.DataFrame(np.column_stack((y, predictors)))
        centered = frame - frame.groupby(weeks).transform("mean")
        y = centered.iloc[:, 0].to_numpy()
        design = centered.iloc[:, 1:].to_numpy()
    coefficients = np.linalg.lstsq(design, y, rcond=None)[0]
    predicted = design @ coefficients
    denominator = np.square(y - y.mean()).sum()
    r2 = 1 - np.square(y - predicted).sum() / denominator if denominator else np.nan
    return (coefficients[1:] if weeks is None else coefficients), float(r2)


def week_bootstrap(
    y: np.ndarray, predictors: np.ndarray, weeks: np.ndarray, fixed_effects: bool, seed: int
) -> np.ndarray:
    rng = np.random.default_rng(seed)
    unique = pd.unique(weeks)
    groups = [np.flatnonzero(weeks == week) for week in unique]
    draws = []
    for _ in range(N_BOOT):
        chosen = rng.integers(0, len(groups), size=len(groups))
        indices = np.concatenate([groups[i] for i in chosen])
        # A duplicate week is an independent resampled block. Give each block a new ID.
        sampled_weeks = np.concatenate([np.full(len(groups[i]), j) for j, i in enumerate(chosen)])
        coef, _ = fit(y[indices], predictors[indices], sampled_weeks if fixed_effects else None)
        draws.append(coef)
    return np.asarray(draws)


def add_model(rows: list[dict], name: str, frame: pd.DataFrame, outcome: str,
              predictors: list[str], fixed_effects: bool, seed: int, units: list[str]) -> float:
    y = frame[outcome].to_numpy(float)
    x = frame[predictors].to_numpy(float)
    weeks = frame.week.to_numpy()
    coef, r2 = fit(y, x, weeks if fixed_effects else None)
    draws = week_bootstrap(y, x, weeks, fixed_effects, seed)
    for j, predictor in enumerate(predictors):
        lo, hi = np.percentile(draws[:, j], [2.5, 97.5])
        rows.append(dict(test=name, term=predictor, estimate=coef[j], ci_low=lo, ci_high=hi,
                         unit=units[j], n_days=len(frame), n_weeks=frame.week.nunique(), r2=r2))
    return r2


def main() -> None:
    digest = verify_hash()
    fox = pd.read_csv(RAW)
    required = {"open_time_ms", "volume_usdt", "taker_buy_volume_usdt"}
    if not required.issubset(fox.columns):
        raise ValueError(f"Missing Foxbit columns: {sorted(required - set(fox.columns))}")
    if fox.open_time_ms.isna().any() or fox.open_time_ms.duplicated().any():
        raise ValueError("Missing or duplicate Foxbit open timestamps")
    if (fox.volume_usdt < 0).any() or (fox.taker_buy_volume_usdt < -1e-9).any():
        raise ValueError("Negative volume in Foxbit candles")
    if (fox.taker_buy_volume_usdt > fox.volume_usdt + 1e-6).any():
        raise ValueError("Foxbit taker-buy volume exceeds total volume")

    dates = pd.to_datetime(fox.open_time_ms, unit="ms") - pd.Timedelta(hours=3)
    fox["date_brt"] = dates.dt.normalize()
    fox["hour_brt"] = dates.dt.hour
    afternoon = fox[(fox.hour_brt >= 13) & (fox.hour_brt < 18) &
                    fox.date_brt.between(pd.Timestamp(START), pd.Timestamp(END))].copy()
    afternoon["net_mn"] = (afternoon.volume_usdt - 2 * afternoon.taker_buy_volume_usdt) / 1e6
    daily_raw = afternoon.groupby("date_brt").agg(
        net_mn=("net_mn", "sum"), total_mn=("volume_usdt", lambda v: v.sum() / 1e6),
        hours=("open_time_ms", "size"), zero_hours=("volume_usdt", lambda v: int((v == 0).sum())),
    )
    daily = pd.read_csv(DAILY, parse_dates=["date_brt"]).set_index("date_brt").loc[START:END]
    daily = daily.join(daily_raw, how="left")
    if daily[["x1", "x2", "y", "net_mn", "total_mn", "hours"]].isna().any().any():
        raise ValueError("Missing afternoon data or morning predictor on a PTAX day")
    if (daily.hours != 5).any():
        raise ValueError("A PTAX day lacks one of the five Foxbit afternoon candles")
    discrepancy = float((daily.y - daily.net_mn).abs().max())
    if discrepancy > 5.1e-5:
        raise ValueError(f"Rebuilt Foxbit net flow differs from rounded P3-19 daily table: {discrepancy}")
    zero_days = int((daily.total_mn == 0).sum())
    daily = daily[daily.total_mn > 0].copy()
    daily["imbalance_share"] = daily.net_mn / daily.total_mn
    daily["week"] = daily.index.to_period("W-SUN").astype(str)
    daily["next_change"] = daily.x1.shift(-1) - daily.x1

    coverage = pd.DataFrame([dict(
        raw_sha256=digest, period_start=START, period_end=END, ptax_days=len(daily) + zero_days,
        usable_days=len(daily), zero_volume_days=zero_days, observed_hours=int(daily.hours.sum()),
        zero_volume_hours=int(daily.zero_hours.sum()), weeks=daily.week.nunique(),
        median_afternoon_volume_mn=daily.total_mn.median(),
        min_afternoon_volume_mn=daily.total_mn.min(),
        max_afternoon_volume_mn=daily.total_mn.max(),
        max_p319_y_difference_mn=discrepancy,
    )])
    rows: list[dict] = []
    add_model(rows, "daily original, week bootstrap", daily, "net_mn", ["x1", "x2"],
              False, SEED, ["mn USDT per bp", "mn USDT per bp"])
    add_model(rows, "within week net flow", daily, "net_mn", ["x1", "x2"],
              True, SEED + 1, ["mn USDT per bp", "mn USDT per bp"])
    add_model(rows, "within week imbalance share", daily, "imbalance_share", ["x1", "x2"],
              True, SEED + 2, ["share per bp", "share per bp"])

    forward = daily.dropna(subset=["next_change"])
    baseline_r2 = add_model(rows, "next PTAX change baseline", forward, "next_change", ["x1", "x2"],
                            False, SEED + 3, ["bps per bp", "bps per bp"])
    flow_r2 = add_model(rows, "next PTAX change with flow", forward, "next_change", ["net_mn", "x1", "x2"],
                        False, SEED + 4, ["bps per mn USDT", "bps per bp", "bps per bp"])
    week_baseline_r2 = add_model(rows, "next PTAX change week baseline", forward, "next_change", ["x1", "x2"],
                                 True, SEED + 5, ["bps per bp", "bps per bp"])
    week_flow_r2 = add_model(rows, "next PTAX change within week", forward, "next_change", ["net_mn", "x1", "x2"],
                             True, SEED + 6, ["bps per mn USDT", "bps per bp", "bps per bp"])
    for name, value in [("forward delta R2 raw", flow_r2 - baseline_r2),
                        ("forward delta R2 within week", week_flow_r2 - week_baseline_r2)]:
        rows.append(dict(test="baseline comparison", term=name, estimate=value, ci_low=np.nan, ci_high=np.nan,
                         unit="R2 points, in sample", n_days=len(forward), n_weeks=forward.week.nunique(), r2=np.nan))

    y, x = daily.net_mn.to_numpy(), daily.x1.to_numpy()
    best = None
    for kink in range(10, 155, 5):
        basis = np.maximum(0, x - kink)
        if basis.std() == 0:
            continue
        design = np.column_stack((np.ones(len(x)), basis))
        intercept, slope = np.linalg.lstsq(design, y, rcond=None)[0]
        ssr = np.square(y - design @ np.array([intercept, slope])).sum()
        if best is None or ssr < best[0]:
            best = (ssr, kink, intercept, slope)
    assert best is not None
    _, kink, intercept, slope = best
    crossing = kink - intercept / slope if slope > 0 and intercept <= 0 else np.nan
    for term, value, unit in [("kink", kink, "bps"), ("intercept below kink", intercept, "mn USDT"),
                              ("slope above kink", slope, "mn USDT per bp"),
                              ("fitted zero crossing", crossing, "bps")]:
        rows.append(dict(test="hinge audit", term=term, estimate=value, ci_low=np.nan, ci_high=np.nan,
                         unit=unit, n_days=len(daily), n_weeks=daily.week.nunique(), r2=np.nan))

    coverage.to_csv(TABLES / "P3-47_coverage.csv", index=False)
    result = pd.DataFrame(rows)
    result.to_csv(TABLES / "P3-47_recovery_checks.csv", index=False, float_format="%.6f")
    print(coverage.to_string(index=False))
    print(result.to_string(index=False, float_format=lambda value: f"{value:+.5f}"))


if __name__ == "__main__":
    main()
