r"""P3-10: did stablecoin imports fall when the premium jumped (23 Jun 2026), and recover when it faded?
Specification fixed before the download: tasks/P3-10-stablecoin-imports.md -> Specification.

Imports  BCB external-sector statistics, Tabela 11 (Outros investimentos - ativos - moeda e depositos - demais
         setores), line "dos quais: criptoativos com passivo correspondente" = SGS 29644, US$ million per month.
         SGS stores it with a minus sign; we flip it so a positive number = net acquisition by residents.
T1       log change Jun -> Jul 2026, ranked against every other month-over-month log change (months with a
         value <= 0 have no log and are skipped). p = (k+1)/(n+1), k = other months with a fall at least as large.
         Robustness: log(month / mean of months t-6..t-2), same ranking (for Jul 2026: Jul vs mean Jan-May).
T2       R = mean(Aug, Sep 2026) / mean(Jan-May 2026). >= 0.5 recovered; < 0.25 not recovered; else partial.
T3       description: monthly imports next to the monthly mean premium (P1-02), Jan 2024 - Sep 2026.
S3       on-exchange trading in PTAX-day windows around 23 Jun 2026: before [-20,-1], spike [+1,+20],
         after [+21,+60]; per calendar day from the window's first to last PTAX date (UTC days). Binance volume
         change (log of spike/before) ranked two-sided against the 200 P2-03 placebo dates.
Inputs   data/raw/bcb/sgs_29644.json (frozen 2 Nov 2026), data/processed/P1-02_premium_daily.csv,
         data/raw/binance/USDTBRL/*.zip, data/raw/foxbit/USDTBRL-1h.csv, data/raw/mercadobitcoin/USDT-BRL-1h.csv,
         results/tables/P2-03_placebo_draws.csv
Outputs  data/processed/P3-10_imports_monthly.csv, results/tables/P3-10_imports.csv,
         results/tables/P3-10_order_flow.csv, results/figures/P3-10_imports.png
Run      python scripts/p3_10_imports.py
"""
import json
from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
RAW, PROC, TAB, FIG = ROOT / "data/raw", ROOT / "data/processed", ROOT / "results/tables", ROOT / "results/figures"
NOTICE = pd.Timestamp("2026-06-23")

# 1. Monthly series: stablecoin net acquisition abroad (US$ mn) and mean premium (bps)
sgs = json.loads((RAW / "bcb/sgs_29644.json").read_text())
imp = pd.Series({pd.to_datetime(r["data"], dayfirst=True): -float(r["valor"]) for r in sgs}).sort_index()
assert round(imp["2026-06-01"]) == 2542 and round(imp["2026-07-01"]) == 572, "press figures not reproduced"
daily = pd.read_csv(PROC / "P1-02_premium_daily.csv", parse_dates=["date_brt"]).set_index("date_brt")
monthly = pd.DataFrame({"imports_usd_mn": imp, "premium_mean_bps": daily.premium_bps.resample("MS").mean()})
monthly.index.name = "month"
PROC.mkdir(parents=True, exist_ok=True)
monthly.to_csv(PROC / "P3-10_imports_monthly.csv", float_format="%.3f")
print(f"imports: {imp.index[0]:%b %Y} - {imp.index[-1]:%b %Y}, {len(imp)} months; months <= 0: {(imp <= 0).sum()}")


def rank(stat, month, side="down"):
    """Empirical p of one month's statistic among all other months: (k+1)/(n+1)."""
    obs, rest = stat[month], stat.drop(month).dropna()
    k = (rest <= obs).sum() if side == "down" else (rest.abs() >= abs(obs)).sum()
    return obs, len(rest), k, (k + 1) / (len(rest) + 1)


rows = []
logs = np.log(imp.where(imp > 0))
for name, stat in [("T1 log change vs previous month", logs.diff()),
                   ("T1b log of month vs mean of t-6..t-2", logs - np.log(imp.shift(2).rolling(5).mean().where(lambda s: s > 0)))]:
    obs, n, k, p = rank(stat, pd.Timestamp("2026-07-01"))
    rows.append({"test": name, "month": "2026-07", "value": obs, "pct_change": np.expm1(obs) * 100, "n_other_months": n,
                 "k_as_large": k, "p_empirical": p, "verdict": "drop beyond normal range" if p <= 0.10 else "within normal range"})

pre, post = imp["2026-01-01":"2026-05-01"].mean(), imp["2026-08-01":"2026-09-01"]
r = post.mean() / pre
rows.append({"test": "T2 fade: mean(Aug,Sep 2026) / mean(Jan-May 2026)", "month": "2026-08..09", "value": r,
             "pct_change": (r - 1) * 100, "n_other_months": len(post), "k_as_large": np.nan, "p_empirical": np.nan,
             "verdict": "recovered" if r >= 0.5 else "not recovered" if r < 0.25 else "partial (inconclusive)"})
both = monthly["2024-01-01":"2026-09-01"].dropna()
rows.append({"test": "T3 correlation, monthly imports vs mean premium, Jan 2024 - Sep 2026", "month": "2024-01..2026-09",
             "value": both.imports_usd_mn.corr(both.premium_mean_bps), "pct_change": np.nan, "n_other_months": len(both),
             "k_as_large": np.nan, "p_empirical": np.nan, "verdict": "description only"})
res = pd.DataFrame(rows)
TAB.mkdir(parents=True, exist_ok=True)
res.to_csv(TAB / "P3-10_imports.csv", index=False, float_format="%.4f")
print(f"\nJan-May 2026 mean {pre:.0f}; Jun {imp['2026-06-01']:.0f}; Jul {imp['2026-07-01']:.0f}; "
      f"Aug {imp['2026-08-01']:.0f}; Sep {imp['2026-09-01']:.0f} (US$ mn)")
print(res.round(4).to_string(index=False))

# 2. On-exchange trading around the notice (S3)
b = pd.concat(pd.read_csv(z, header=None, usecols=[0, 5, 8, 9]) for z in sorted((RAW / "binance/USDTBRL").glob("*.zip")))
t = b[0].astype("int64")
b.index = pd.to_datetime(np.where(t > 1e14, t // 1000, t), unit="ms")  # Binance files from 2025 use microseconds
b = b.rename(columns={5: "volume", 8: "trades", 9: "buyer_volume"})[["volume", "trades", "buyer_volume"]]
f = pd.read_csv(RAW / "foxbit/USDTBRL-1h.csv")
f = pd.DataFrame({"volume": f.volume_usdt.values, "trades": f.trades.values, "buyer_volume": f.taker_buy_volume_usdt.values},
                 index=pd.to_datetime(f.open_time_ms, unit="ms"))
m = pd.read_csv(RAW / "mercadobitcoin/USDT-BRL-1h.csv")
m = pd.DataFrame({"volume": m.v.values}, index=pd.to_datetime(m.t, unit="s"))  # no trade count or side in this API
venues = {v: d.resample("D").sum() for v, d in [("Binance", b), ("Foxbit", f), ("Mercado Bitcoin", m)]}

ptax = daily.index
def window(t0, a, z):
    """Calendar days from the first to the last PTAX date of PTAX-day offsets [a, z] around t0."""
    i = ptax.get_loc(t0)
    return ptax[i + a], ptax[i + z]

flow = []
for wname, (a, z) in {"before [-20,-1]": (-20, -1), "spike [+1,+20]": (1, 20), "after [+21,+60]": (21, 60)}.items():
    lo, hi = window(NOTICE, a, z)
    for v, d in venues.items():
        w = d.loc[lo:hi]
        row = {"window": wname, "from": lo.date(), "to": hi.date(), "venue": v, "volume_usdt_per_day": w.volume.mean()}
        if "trades" in w:
            row |= {"trades_per_day": w.trades.mean(), "avg_trade_usdt": w.volume.sum() / w.trades.sum(),
                    "buyer_initiated_share": w.buyer_volume.sum() / w.volume.sum()}
        flow.append(row)
flow = pd.DataFrame(flow)


def vol_change(d, t0):
    (a0, a1), (b0, b1) = window(t0, -20, -1), window(t0, 1, 20)
    return np.log(d.volume.loc[b0:b1].mean() / d.volume.loc[a0:a1].mean())


bin_ = venues["Binance"]
plc = pd.read_csv(TAB / "P2-03_placebo_draws.csv", parse_dates=["date"]).date
plc = [p for p in plc if p in ptax and window(p, -20, -1)[0] >= bin_.index[0] and window(p, 1, 20)[1] <= bin_.index[-1]]
pl = pd.Series([vol_change(bin_, p) for p in plc], index=plc)
obs = vol_change(bin_, NOTICE)
k = (pl.abs() >= abs(obs)).sum()
flow.attrs["note"] = f"Binance volume log change spike/before = {obs:.3f}; placebo k={k} of n={len(pl)}, p={(k + 1) / (len(pl) + 1):.3f}"
flow.to_csv(TAB / "P3-10_order_flow.csv", index=False, float_format="%.4f")
print("\n" + flow.round(3).to_string(index=False))
print(f"\nBinance volume change, spike vs before: {np.expm1(obs) * 100:+.0f}% (log {obs:.3f}); "
      f"placebo dates with a change at least as large (two-sided): {k} of {len(pl)}, p = {(k + 1) / (len(pl) + 1):.3f}")

# 3. Figure (pt-BR): monthly imports and monthly premium, two panels on one time axis
BLUE, ORANGE, INK, INK2, GRID, SURFACE = "#2a78d6", "#eb6834", "#1f1e1c", "#52514e", "#e4e3df", "#fcfcfb"
plt.rcParams.update({"figure.facecolor": SURFACE, "axes.facecolor": SURFACE, "axes.edgecolor": GRID, "axes.labelcolor": INK2,
                     "xtick.color": INK2, "ytick.color": INK2, "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.6,
                     "axes.axisbelow": True, "axes.spines.top": False, "axes.spines.right": False, "font.size": 10,
                     "axes.titlesize": 12, "axes.titleweight": "bold", "axes.titlelocation": "left",
                     "legend.frameon": False, "savefig.dpi": 200, "savefig.bbox": "tight"})
w = monthly["2024-01-01":"2026-09-01"]
mid = w.index + pd.Timedelta(days=14)  # a month's value sits mid-month, so June (which includes 24-30 Jun) straddles the line
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 6.5), sharex=True, gridspec_kw={"hspace": 0.25})
ax1.bar(mid, w.imports_usd_mn / 1e3, width=24, color=BLUE)
ax1.set_ylabel("US$ bilhões por mês")
ax1.set_title("Compra líquida de stablecoins no exterior por residentes (BCB)")
ax2.plot(mid, w.premium_mean_bps, color=ORANGE, lw=2, marker="o", ms=4)
ax2.set_ylabel("pontos-base")
ax2.set_title("Prêmio do USDT sobre a PTAX, média do mês")
for ax in (ax1, ax2):
    ax.axvline(NOTICE, color=INK, lw=1, ls="--")
ax1.annotate("23/06/2026:\nofício do BCB", (NOTICE, 2.0), xytext=(6, 0), textcoords="offset points",
             ha="left", va="center", fontsize=9, color=INK)
ax2.xaxis.set_major_formatter(mdates.DateFormatter("%m/%Y"))
fig.text(0.01, -0.02, "Fonte: BCB, Estatísticas do setor externo, Tabela 11, \"criptoativos com passivo correspondente\" "
         "(SGS 29644); Binance e BCB (PTAX) para o prêmio; cálculo da equipe.", fontsize=8, color=INK2)
FIG.mkdir(parents=True, exist_ok=True)
fig.savefig(FIG / "P3-10_imports.png")
