r"""P3-24: BRLA as a fourth venue - did the route Pix -> BRLA -> USDC pay the June premium too?
Specification: tasks/P3-24-brla-fourth-venue.md -> Specification (committed in b57af33 before this script ran).

Quantity  route premium = BRLA per USDC on the pool / (PTAX sell x USDC/USD) - 1, in bps. Assumes 1 BRLA = R$ 1 (Avenia
          mints and redeems at par via Pix; not measured). A route cost, like the USDT premium; not a BRLA "depeg".
Primary   Polygon USDC/BRLA pool (Uniswap v3, 0x0e77...c956), hourly OPEN at 13-16 UTC (P1-02 timing), USDC/USD = 1
r1        USDC/USD measured in the same window: Binance USDCUSDT x Coinbase USDT/USD (P1-02 hourly columns)
r2        Polygon daily close (00h UTC = 21h Brasilia) over the same day's PTAX (F-034's timing)
r3        Gnosis (USDC.e/BRLA) and Base (BRLA/USDC) pools, daily close; liquidity flag if median daily volume in the
          pre-window is below US$ 100k
S20       mean over the 20 PTAX days after t0 = 23 Jun 2026 minus the 20 before (t0 excluded; >= 15 of 20 days each side);
          Binance's USDT premium on the same days next to it
Reference S20 at every clean date (P2-03 rule) in the Polygon daily-close series: description only, not a p-value
Inputs    data/raw/flash-mentor-leads/brla/* (Felipe's Flash snapshots, 4 Nov 2026; checksums in data/raw/SHA256SUMS;
          restore command in data/README.md), data/processed/P1-02_premium_daily.csv, P1-02_premium_hourly.csv,
          data/processed/P1-04_events_brazil.csv
Outputs   data/processed/P3-24_brla_daily.csv, results/tables/P3-24_brla_s20.csv, results/figures/P3-24_brla_vs_usdt.png
Run       python scripts/p3_24_brla.py
"""
import json
import sys
import time
import urllib.request
from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
B, PROC, TAB, FIG = ROOT / "data/raw/flash-mentor-leads/brla", ROOT / "data/processed", ROOT / "results/tables", ROOT / "results/figures"
T0 = pd.Timestamp("2026-06-23")
WINDOW_UTC = [13, 14, 15, 16]
POOL = {"Polygon": "polygon_pos_0x0e7754127dedd4097be750825dbb4669bc32c956",
        "Gnosis": "xdai_0x576bf065cbc15cb2d61affb156118fcff01a8238",
        "Base": "base_0x1c33aa5cc206ed3d9e29fb136796a8815e48af58"}
bps = lambda r: (r - 1) * 1e4
LIVE = ROOT / "data/raw/p3_24"  # spec 2 pulls (GeckoTerminal), raw JSON as returned
CELO = ("celo", "0x14e577e42d45fd2200a9b0e31d87fe826467111a")              # BRLA / USD₮, Uniswap v3
CURVE = ("polygon_pos", "0xc89f31f74573cc19fffc06108601c1ac71ba9735")      # TESOURO / BRZ / stBRZ / BRLA
BRLA, BRZ = "0xe6a537a407488807f0bbeb0038b79004f19dddfb", "0x4ed141110f6eeeaba9a1df36d8c26f684d2475dc"

if sys.argv[1:] == ["download"]:  # python scripts/p3_24_brla.py download  (then append checksums, data/README.md)
    api = "https://api.geckoterminal.com/api/v2/networks/{}/pools/{}/ohlcv/day?limit=200&currency=usd"
    pulls = {"celo_brla_usdt_day_usd": api.format(*CELO), "curve_brla_day_usd": api.format(*CURVE) + f"&token={BRLA}",
             "curve_brz_day_usd": api.format(*CURVE) + f"&token={BRZ}"}
    LIVE.mkdir(parents=True, exist_ok=True)
    stamp = pd.Timestamp.now("UTC").strftime("%Y%m%dT%H")
    for name, url in pulls.items():
        req = urllib.request.Request(url, headers={"User-Agent": "out-of-sample-datathon"})
        (LIVE / f"{name}_{stamp}.json").write_bytes(urllib.request.urlopen(req, timeout=30).read())
        print("saved", f"data/raw/p3_24/{name}_{stamp}.json")
        time.sleep(6)  # public API rate limit
    sys.exit()


def gecko(name):
    """Latest pull of a spec-2 file -> daily DataFrame (UTC dates) with close and volume (US$)."""
    f = sorted(LIVE.glob(f"{name}_*.json"))[-1]
    k = pd.DataFrame(json.loads(f.read_bytes())["data"]["attributes"]["ohlcv_list"], columns=["t", "o", "h", "l", "close", "volume"])
    k = k.set_index(pd.to_datetime(k.t, unit="s")).sort_index()[["close", "volume"]]
    return k[~k.index.duplicated(keep="last")]  # GeckoTerminal repeats the oldest day (5 May) in the Curve pulls


d = pd.read_csv(PROC / "P1-02_premium_daily.csv", parse_dates=["date_brt"], index_col="date_brt")
h1 = pd.read_csv(PROC / "P1-02_premium_hourly.csv", parse_dates=["time_utc"], index_col="time_utc",
                 usecols=["time_utc", "usdtbrl_open_brl", "usdtusd_open_usd", "usdtusd_cb_open_usd", "usdtbrl_volume_usdt"])
ptax = d.ptax_sell_brl_per_usd

# Primary: Polygon hourly opens in the PTAX window (BRLA per USDC: base USDC, quote BRLA)
ph = pd.read_csv(B / f"ohlcv_{POOL['Polygon']}_hour_token.csv", parse_dates=["datetime_utc"], index_col="datetime_utc")
w = ph[ph.index.hour.isin(WINDOW_UTC)].open
g = w.groupby(w.index.normalize())
out = pd.DataFrame({"brla_window_brl_per_usdc": g.mean(), "brla_window_hours": g.count()}).reindex(d.index)
out["brla_bps"] = bps(out.brla_window_brl_per_usdc / ptax)
# r1: USDC/USD in the window = (USDT per USDC, Binance) x (USD per USDT, Coinbase)
usdcusd = (h1.usdtusd_cb_open_usd / h1.usdtusd_open_usd).reindex(w.index)
out["usdcusd_window"] = usdcusd.groupby(usdcusd.index.normalize()).mean().reindex(d.index)
out["brla_r1_bps"] = bps(out.brla_window_brl_per_usdc / (ptax * out.usdcusd_window))
# Check: window opens far from Binance's implied BRL per USDC (USDT/BRL x USDT per USDC) are listed, not removed
bin_brl_per_usdc = (h1.usdtbrl_open_brl / h1.usdtusd_open_usd).reindex(w.index)
gap = bps(w / bin_brl_per_usdc).dropna()

# r2, r3: daily closes (00h UTC next day) over the same day's PTAX
vol_usd = {}
for name, pool in POOL.items():
    k = pd.read_csv(B / f"ohlcv_{pool}_day_token.csv", parse_dates=["date"], index_col="date")
    px = 1 / k.close if name == "Base" else k.close          # Base quotes USDC per BRLA; the others BRLA per USDC(.e)
    out[f"{name.lower()}_close_bps"] = bps(px.reindex(d.index) / ptax)
    vol_usd[name] = (pd.read_csv(B / f"ohlcv_{pool}_day_usd.csv", parse_dates=["date"], index_col="date").volume
                     if name == "Polygon" else k.volume / px if name == "Gnosis" else k.volume)  # US$ (approx. off Polygon)
out["binance_bps"] = d.premium_bps
first = d.index[d.index >= pd.Timestamp("2025-11-07")][0]
out = out.loc[first:]
out.round(3).to_csv(PROC / "P3-24_brla_daily.csv")

# S20 at t0, each series next to Binance on the same days
i = out.index.get_loc(T0)
pre_days, post_days = out.index[i - 20:i], out.index[i + 1:i + 21]


def s20(s, j=i):
    pre, post = s.iloc[j - 20:j], s.iloc[j + 1:j + 21]
    return post.mean() - pre.mean() if pre.count() >= 15 and post.count() >= 15 else np.nan


rows = []
series = {"Polygon, PTAX window (primary)": "brla_bps", "Polygon, window, USDC/USD measured (r1)": "brla_r1_bps",
          "Polygon, daily close (r2)": "polygon_close_bps", "Gnosis, daily close (r3)": "gnosis_close_bps",
          "Base, daily close (r3)": "base_close_bps"}
for label, col in series.items():
    s = out[col]
    same = out.binance_bps.where(s.notna())
    pool = label.split(",")[0]
    v = vol_usd[pool].reindex(pre_days)
    rows.append(dict(series=label, pre_mean_bps=round(s.iloc[i - 20:i].mean(), 1), post_mean_bps=round(s.iloc[i + 1:i + 21].mean(), 1),
                     s20_bps=round(s20(s), 1), days_pre=int(s.iloc[i - 20:i].count()), days_post=int(s.iloc[i + 1:i + 21].count()),
                     binance_s20_same_days_bps=round(s20(same), 1), pool_median_daily_volume_usd_pre=round(v.median()),
                     liquidity_flag="ok" if v.median() >= 100_000 else "fails liquidity (< US$ 100k/day)"))
res = pd.DataFrame(rows)
res.loc[len(res)] = dict(series="Binance USDT premium, all days (F-016)", s20_bps=round(s20(out.binance_bps), 1),
                         pre_mean_bps=round(out.binance_bps.iloc[i - 20:i].mean(), 1),
                         post_mean_bps=round(out.binance_bps.iloc[i + 1:i + 21].mean(), 1), days_pre=20, days_post=20)
res.to_csv(TAB / "P3-24_brla_s20.csv", index=False)
print(f"t0 {T0.date()}: pre {pre_days[0].date()}..{pre_days[-1].date()}, post {post_days[0].date()}..{post_days[-1].date()}")
print(res.to_string(index=False))

# Reference (description only): S20 at clean dates in the Polygon daily-close series (P2-03 clean rule, copied)
ev = pd.read_csv(PROC / "P1-04_events_brazil.csv")
full = d.index
mapped = set()
for _, r in ev.iterrows():
    for c in ["date_announced", "date_effective"]:
        x = str(r[c]).strip()
        if x not in ("N/A", "nan") and (full >= pd.Timestamp(x)).any():
            mapped.add(full[full >= pd.Timestamp(x)][0])
black = {q for e in mapped for q in out.index[max(0, out.index.searchsorted(e) - 20):out.index.searchsorted(e) + 21]}
ref = pd.Series({out.index[j]: s20(out.polygon_close_bps, j) for j in range(20, len(out) - 20)
                 if out.index[j] not in black}).dropna()
print(f"\nReference, Polygon daily close: S20 at {len(ref)} clean dates ({ref.index.min().date()}..{ref.index.max().date()}): "
      f"min {ref.min():+.1f}, max {ref.max():+.1f}, 2.5-97.5% {ref.quantile(.025):+.1f} .. {ref.quantile(.975):+.1f} bps "
      f"(description, overlapping windows, not a p-value)")
print(f"Window opens more than 300 bps from Binance's BRL per USDC: {int((gap.abs() > 300).sum())} of {len(gap)} "
      f"(median gap {gap.median():+.1f} bps); listed: {gap[gap.abs() > 300].round(0).to_dict()}")
print(f"Window hours per PTAX day, pre/post: {out.brla_window_hours.iloc[i - 20:i].mean():.2f} / "
      f"{out.brla_window_hours.iloc[i + 1:i + 21].mean():.2f} (of 4); USDC/USD in window, pre/post mean: "
      f"{out.usdcusd_window.iloc[i - 20:i].mean():.5f} / {out.usdcusd_window.iloc[i + 1:i + 21].mean():.5f}")

# S4: BRLA supply by chain around the notice (DefiLlama snapshots)
sup = pd.read_csv(B / "brla_supply_by_chain_daily.csv", parse_dates=["date"], index_col="date")
print("\nBRLA circulating supply by chain (DefiLlama, million BRLA), 19-30 Jun 2026:")
print((sup.loc["2026-06-19":"2026-06-30"] / 1e6).round(1).assign(total=lambda x: x.sum(axis=1)).to_string())

# Figure: BRLA route vs Binance USDT premium, same axes (pt-BR, for the deck/annex)
v = out.loc["2026-05-01":"2026-09-30"]
fig, ax = plt.subplots(figsize=(11, 4.6))
ax.plot(v.index, v.binance_bps, color="#2a78d6", lw=1.8, label="USDT/BRL na Binance (prêmio sobre a PTAX)")
ax.plot(v.index, v.brla_bps, color="#eb6834", lw=1.8, label="Rota Pix → BRLA → USDC (pool Polygon, janela da PTAX)")
ax.axvline(T0, color="#52514e", ls=":", lw=1)
ax.text(T0, 0.97, " 23/jun: ofício", transform=ax.get_xaxis_transform(), va="top", fontsize=9, color="#52514e")
ax.axhline(0, color="#52514e", lw=0.8)
ax.set_ylabel("pontos-base sobre a PTAX")
ax.set_title("O prêmio apareceu também fora das corretoras: a rota BRLA → USDC na Polygon", loc="left", fontweight="bold")
ax.legend(loc="upper right", frameon=False, fontsize=9)
ax.grid(axis="y", alpha=0.3)
ax.xaxis.set_major_formatter(mdates.DateFormatter("%m/%Y"))
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
fig.text(0.01, -0.02, "Fontes: GeckoTerminal (pool Uniswap v3 USDC/BRLA, Polygon), Binance, BCB (PTAX). Supõe 1 BRLA = R\\$ 1 "
         "e 1 USDC = US\\$ 1. Cálculo da equipe (P3-24).", fontsize=8, color="#52514e")
fig.savefig(FIG / "P3-24_brla_vs_usdt.png", dpi=180, bbox_inches="tight")

# Spec 2a: scale. Summed US$ volume per pool (UTC days) and Polygon against Binance USDT/BRL on the same days
vols = {k: v.sort_index() for k, v in vol_usd.items()}
celo = gecko("celo_brla_usdt_day_usd")
vols["Celo"] = celo.volume
binance_vol = h1.usdtbrl_volume_usdt.resample("D").sum()
rows = []
for label, (a, b) in {"before 25 May-22 Jun": ("2026-05-25", "2026-06-22"), "after 24 Jun-21 Jul": ("2026-06-24", "2026-07-21")}.items():
    s = {k: v.loc[a:b].sum() for k, v in vols.items()}
    rows.append({"window": label, **{f"{k.lower()}_usd": round(x) for k, x in s.items()},
                 "celo_days_with_trades": int((celo.volume.loc[a:b] > 0).sum()),
                 "polygon_share_of_pools_pct": round(100 * s["Polygon"] / sum(s.values()), 1),
                 "binance_usdtbrl_usdt": round(binance_vol.loc[a:b].sum()),
                 "polygon_vs_binance_pct": round(100 * s["Polygon"] / binance_vol.loc[a:b].sum(), 2)})
scale = pd.DataFrame(rows)
scale.to_csv(TAB / "P3-24_scale.csv", index=False)
print("\nSpec 2a, scale (US$ volume summed over calendar days):\n" + scale.to_string(index=False))

# Spec 2b: reais side. BRLA price in BRZ on the Curve pool = US$ price of BRLA / US$ price of BRZ (daily close), bps
brla_c, brz_c = gecko("curve_brla_day_usd"), gecko("curve_brz_day_usd")
gap = bps(brla_c.close / brz_c.close).reindex(out.index)
n_pre, n_post = int(gap.iloc[i - 20:i].count()), int(gap.iloc[i + 1:i + 21].count())
testable = n_pre >= 15 and n_post >= 15
s = s20(gap) if testable else np.nan
reading = ("not testable" if not testable else "BRLA kept its value against BRZ (|S20| <= 22 bps)" if abs(s) <= 22
           else "one of the two reais tokens moved in reais (|S20| > 22 bps)")
brl_side = pd.DataFrame([{"series": "BRLA in BRZ, Curve pool (bps)", "days_pre": n_pre, "days_post": n_post,
                          "pre_mean_bps": round(gap.iloc[i - 20:i].mean(), 1), "post_mean_bps": round(gap.iloc[i + 1:i + 21].mean(), 1),
                          "s20_bps": round(s, 1) if testable else np.nan,
                          "pre_range_bps": f"{gap.iloc[i - 20:i].min():.1f}..{gap.iloc[i - 20:i].max():.1f}",
                          "post_range_bps": f"{gap.iloc[i + 1:i + 21].min():.1f}..{gap.iloc[i + 1:i + 21].max():.1f}",
                          "dollar_route_s20_bps": res.loc[0, "s20_bps"], "reading": reading}])
brl_side.to_csv(TAB / "P3-24_brl_side.csv", index=False)
print("\nSpec 2b, reais side:\n" + brl_side.T.to_string(header=False))
print(f"Curve pool daily candles: {brla_c.index.min().date()}..{brla_c.index.max().date()} (n={len(brla_c)}); "
      f"median daily pool volume (all pairs) before/after US$ {brla_c.volume.loc['2026-05-25':'2026-06-22'].median():,.0f} / "
      f"{brla_c.volume.loc['2026-06-24':'2026-07-21'].median():,.0f}")

