r"""P3-19: did seller-initiated trading on Foxbit respond to the premium over the official dollar (import arbitrage) or to the
Foxbit-Binance gap (cross-venue arbitrage)? Specification fixed before this script: tasks/P3-19-supply-response.md.

y        Foxbit seller-initiated minus buyer-initiated volume = volume - 2 x taker-buy volume (mn USDT).
Daily    y_t = y summed over 13:00-18:00 Brasilia (candles opening 16-20h UTC). x1_t = premium_bps (P1-02, PTAX windows).
         x2_t = Foxbit / Binance - 1 (bps) at the opens of the PTAX window hours 13-16h UTC, as in p2_05_venues.py
         (P2-05_venues_daily.csv ends on 31 Jul, so x2 is rebuilt here; checked against it on the overlap).
         OLS y ~ x1 + x2, moving-block bootstrap over days (block 5, 2,000 draws, seed 17). Sample 24 Jun - 30 Sep 2026;
         placebo 2 Jan - 22 Jun 2026.
Hourly   y in hour h+1 on x1_h (premium against the same day's PTAX at the close of hour h, start hours 13-17 Brasilia) and
         x2_h (Foxbit close / Binance close - 1, bps), both demeaned within day; bootstrap over whole days.
Hinge    y_t = a + b max(0, x1_t - k), k = 10..150 bps step 5, least squares; same block bootstrap.
Inputs   data/raw/foxbit/USDTBRL-1h.csv, data/raw/binance/USDTBRL/*.zip, data/processed/P1-02_premium_daily.csv,
         data/processed/P1-02_premium_hourly.csv, results/tables/P2-05_venues_daily.csv
Outputs  results/tables/P3-19_daily.csv  one row per PTAX day with y, x1, x2
         results/tables/P3-19_results.csv one row per test and coefficient with the estimate and 95% CI
Run      python scripts/p3_19_supply_response.py
"""
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
RAW, PROC, TAB = ROOT / "data/raw", ROOT / "data/processed", ROOT / "results/tables"
rng = np.random.default_rng(17)
B = 2000

# Hourly candles, indexed by candle open (UTC); loading as in p3_10_imports.py
bz = pd.concat(pd.read_csv(z, header=None, usecols=[0, 1, 4]) for z in sorted((RAW / "binance/USDTBRL").glob("*.zip")))
t = bz[0].astype("int64")
bz.index = pd.to_datetime(np.where(t > 1e14, t // 1000, t), unit="ms")  # Binance files from 2025 use microseconds
bz = bz.rename(columns={1: "open", 4: "close"})[["open", "close"]].sort_index()
fz = pd.read_csv(RAW / "foxbit/USDTBRL-1h.csv")
fz.index = pd.to_datetime(fz.open_time_ms, unit="ms")
fz = fz[fz.volume_usdt > 0].sort_index()
fz["y"] = (fz.volume_usdt - 2 * fz.taker_buy_volume_usdt) / 1e6
brt = fz.index - pd.Timedelta(hours=3)

# Daily variables
d = pd.read_csv(PROC / "P1-02_premium_daily.csv", parse_dates=["date_brt"], index_col="date_brt")
day = pd.DataFrame({"x1": d.premium_bps})
day["y"] = fz.y[(brt.hour >= 13) & (brt.hour < 18)].groupby(brt[(brt.hour >= 13) & (brt.hour < 18)].normalize()).sum()
win = bz.index.hour.isin([13, 14, 15, 16])
gap = np.log(fz.open / bz.open.reindex(fz.index)) * 1e4  # log ratio, as P2-05 differences of log premiums
day["x2"] = gap[fz.index.hour.isin([13, 14, 15, 16])].groupby(fz.index[fz.index.hour.isin([13, 14, 15, 16])].normalize()).mean()
day = day.dropna(subset=["x1"]).fillna({"y": 0.0})  # a PTAX day with no Foxbit trade in the afternoon has y = 0
day.to_csv(TAB / "P3-19_daily.csv", float_format="%.4f")

v = pd.read_csv(TAB / "P2-05_venues_daily.csv", parse_dates=["date_brt"], index_col="date_brt")
chk = (v.Foxbit - v.Binance).to_frame("p2_05").join(day.x2).dropna()
print(f"x2 check vs P2-05 ({len(chk)} days): mean abs diff {np.abs(chk.p2_05 - chk.x2).mean():.2f} bps, "
      f"corr {chk.p2_05.corr(chk.x2):.3f}")


def ols(y, X):
    X = np.column_stack([np.ones(len(y)), X])
    return np.linalg.lstsq(X, y, rcond=None)[0][1:]


def block_idx(n, L=5):
    starts = rng.integers(0, n - L + 1, size=int(np.ceil(n / L)))
    return np.concatenate([np.arange(s, s + L) for s in starts])[:n]


def hinge(y, x):
    best = None
    for k in range(10, 155, 5):
        z = np.maximum(0, x - k)
        if z.std() == 0:
            continue
        X = np.column_stack([np.ones(len(y)), z])
        coef, ssr = np.linalg.lstsq(X, y, rcond=None)[:2]
        ssr = ssr[0] if len(ssr) else ((y - X @ coef) ** 2).sum()
        if best is None or ssr < best[0]:
            best = (ssr, k, coef[1])
    return best[1], best[2]


rows = []
for lab, a, z in [("daily", "2026-06-24", "2026-09-30"), ("daily placebo", "2026-01-02", "2026-06-22")]:
    s = day[a:z].dropna()
    y, X = s.y.values, s[["x1", "x2"]].values
    est = ols(y, X)
    bs = np.array([ols(y[i], X[i]) for i in (block_idx(len(s)) for _ in range(B))])
    for j, name in enumerate(["x1 premium (mn USDT per bp)", "x2 Foxbit-Binance gap (mn USDT per bp)"]):
        lo, hi = np.percentile(bs[:, j], [2.5, 97.5])
        rows.append(dict(test=lab, term=name, estimate=est[j], ci_low=lo, ci_high=hi, n=len(s)))
    print(f"{lab:13} {a}..{z} n={len(s)}: x1 {est[0]:+.4f} [{np.percentile(bs[:, 0], 2.5):+.4f}, "
          f"{np.percentile(bs[:, 0], 97.5):+.4f}] | x2 {est[1]:+.4f} [{np.percentile(bs[:, 1], 2.5):+.4f}, "
          f"{np.percentile(bs[:, 1], 97.5):+.4f}] | x1 range {s.x1.min():.0f}..{s.x1.max():.0f} bps, sd x2 {s.x2.std():.1f}")
    if lab == "daily":
        k, b = hinge(y, s.x1.values)
        kb = np.array([hinge(y[i], s.x1.values[i])[0] for i in (block_idx(len(s)) for _ in range(B))])
        lo, hi = np.percentile(kb, [2.5, 97.5])
        rows.append(dict(test="hinge", term="k threshold (bps)", estimate=k, ci_low=lo, ci_high=hi, n=len(s)))
        rows.append(dict(test="hinge", term="b slope above k (mn USDT per bp)", estimate=b, ci_low=np.nan, ci_high=np.nan, n=len(s)))
        print(f"hinge: k = {k} bps [{lo:.0f}, {hi:.0f}], slope above k {b:+.4f} mn USDT per bp | "
              f"mean premium Aug {day.loc['2026-08'].x1.mean():.1f}, Sep {day.loc['2026-09'].x1.mean():.1f} bps")

# Within-day (hourly), 24 Jun - 30 Sep 2026
hp = pd.read_csv(PROC / "P1-02_premium_hourly.csv", usecols=["time_utc", "premium_vs_last_ptax_bps", "ptax_last_date_brt"],
                 parse_dates=["time_utc", "ptax_last_date_brt"], index_col="time_utc")
H = pd.DataFrame({"x1": hp.premium_vs_last_ptax_bps, "ptax_day": hp.ptax_last_date_brt})
H["x2"] = np.log(fz.close / bz.close.reindex(fz.index)).reindex(H.index) * 1e4
H["y_next"] = fz.y.reindex(H.index + pd.Timedelta(hours=1)).fillna(0.0).values
hb = H.index - pd.Timedelta(hours=3)
H["day"] = hb.normalize()
H = H[(hb.hour >= 13) & (hb.hour <= 17) & (H.ptax_day == H.day)]["2026-06-24 15:00":"2026-09-30 23:00"].dropna()
W = H[["x1", "x2", "y_next"]] - H.groupby("day")[["x1", "x2", "y_next"]].transform("mean")
est = ols(W.y_next.values, W[["x1", "x2"]].values)
days = H.day.unique()
g = {dd: np.where(H.day.values == dd)[0] for dd in days}
bs = []
for _ in range(B):
    i = np.concatenate([g[dd] for dd in rng.choice(days, size=len(days))])
    bs.append(ols(W.y_next.values[i], W[["x1", "x2"]].values[i]))
bs = np.array(bs)
for j, name in enumerate(["x1 premium (mn USDT per bp)", "x2 Foxbit-Binance gap (mn USDT per bp)"]):
    lo, hi = np.percentile(bs[:, j], [2.5, 97.5])
    rows.append(dict(test="within-day", term=name, estimate=est[j], ci_low=lo, ci_high=hi, n=len(H)))
print(f"within-day   {len(H)} hours on {len(days)} days: x1 {est[0]:+.4f} [{np.percentile(bs[:, 0], 2.5):+.4f}, "
      f"{np.percentile(bs[:, 0], 97.5):+.4f}] | x2 {est[1]:+.4f} [{np.percentile(bs[:, 1], 2.5):+.4f}, {np.percentile(bs[:, 1], 97.5):+.4f}]")
pd.DataFrame(rows).to_csv(TAB / "P3-19_results.csv", index=False, float_format="%.5f")
