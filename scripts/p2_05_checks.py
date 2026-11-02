r"""P2-05: could something other than a rule have caused the 24 Jun 2026 premium jump? Checks: other venues (S1),
a BRL or USDT/USD shock (S2), and the hour-by-hour timing (S4). S3 (exchange announcements) is a web search, recorded
in the task file. Finding F-009.

Premium per venue: same definition as P1-02, venue_USDTBRL / (PTAX x USDTUSD) - 1, in bps, with the venue's price
  at the start of each PTAX window hour (13, 14, 15, 16h UTC) and Binance's USDT/USD for all venues.
  Binance and Mercado Bitcoin "open" = first trade of the hour; Foxbit "open" = previous hour's close (its docs).
  Hours without trades are skipped (Foxbit writes them as zeros; Mercado Bitcoin omits them).
Event: 23 Jun 2026 (reported BCB notice; date [verify] in P1-04). Before = 20 PTAX days ending 22 Jun; after =
  20 PTAX days starting 24 Jun; 23 Jun itself is left out. Compared as changes, because venue levels differ.
Inputs   data/processed/P1-02_premium_daily.csv, P1-02_premium_hourly.csv (run p1_02_premium.py first),
         data/raw/foxbit/USDTBRL-1h.csv, data/raw/mercadobitcoin/USDT-BRL-1h.csv
Outputs  results/tables/P2-05_venues_daily.csv           daily premium per venue, Jun-Jul 2026
         results/figures/P2-05_hourly_22_26_jun.png      hourly premium vs last published PTAX, 3 venues
Run      python scripts/p2_05_checks.py
"""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
RAW, PROC = ROOT / "data/raw", ROOT / "data/processed"
EVENT = pd.Timestamp("2026-06-23")
WINDOW_UTC = [13, 14, 15, 16]

d = pd.read_csv(PROC / "P1-02_premium_daily.csv", parse_dates=["date_brt", "ptax_published_brt"], index_col="date_brt")
h = pd.read_csv(PROC / "P1-02_premium_hourly.csv", parse_dates=["time_utc"], index_col="time_utc")
f = pd.read_csv(RAW / "foxbit/USDTBRL-1h.csv")
f = f[f.volume_usdt > 0].set_index(pd.to_datetime(f[f.volume_usdt > 0].open_time_ms, unit="ms"))
m = pd.read_csv(RAW / "mercadobitcoin/USDT-BRL-1h.csv")
m = m.set_index(pd.to_datetime(m.t, unit="s"))
opens = {"Binance": h.usdtbrl_open_brl, "Foxbit": f.open, "Mercado Bitcoin": m.o}
closes = {"Binance": h.usdtbrl_close_brl, "Foxbit": f.close, "Mercado Bitcoin": m.c}
bps = lambda ratio: (ratio - 1) * 1e4

# S1: daily window premium per venue
prem = {}
for name, s in opens.items():
    w = (s / h.usdtusd_open_usd.reindex(s.index)).dropna()
    w = w[w.index.hour.isin(WINDOW_UTC)]
    prem[name] = bps(w.groupby(w.index.normalize()).mean() / d.ptax_sell_brl_per_usd).reindex(d.index)
v = pd.DataFrame(prem)
pos = d.index.get_loc(EVENT)
before, after = v.iloc[pos - 20:pos], v.iloc[pos + 1:pos + 21]
s1 = pd.DataFrame({"before_bps": before.mean(), "after_bps": after.mean(), "change_bps": after.mean() - before.mean(),
                   "days_before": before.count(), "days_after": after.count()})
print(f"S1 - mean window premium, 20 PTAX days before ({before.index[0].date()}..{before.index[-1].date()}) "
      f"and after ({after.index[0].date()}..{after.index[-1].date()}) 23 Jun 2026:")
print(s1.round(1).to_string())
print("\nDaily window premium by venue (bps), 15 Jun - 10 Jul 2026:")
print(v["2026-06-15":"2026-07-10"].round(0).to_string())
(ROOT / "results/tables").mkdir(parents=True, exist_ok=True)
v["2026-05-25":"2026-07-31"].round(2).to_csv(ROOT / "results/tables/P2-05_venues_daily.csv")

# S2: was 24 Jun a big BRL day, and what does the premium usually do after one?
r = np.log(d.ptax_sell_brl_per_usd).diff() * 100  # PTAX daily change, %
dp = d.premium_bps.diff()
print(f"\nS2 - PTAX change on 24 Jun 2026: {r['2026-06-24']:+.2f}% (larger in absolute value than "
      f"{(r.abs() < abs(r['2026-06-24'])).mean():.0%} of all PTAX days since Oct 2020)")
print("PTAX daily change, %, 15-30 Jun 2026:", r["2026-06-15":"2026-06-30"].round(2).to_dict())
big = r[(r.abs() >= abs(r["2026-06-24"])) & (r.index < "2026-06-01")]
fwd = lambda k: d.premium_bps.shift(-k) - d.premium_bps.shift(1)  # premium k days later minus the day before
print(f"Other days with |PTAX change| >= {abs(r['2026-06-24']):.2f}% before Jun 2026: {len(big)}. Premium change from the day "
      f"before to: same day {fwd(0)[big.index].mean():+.1f} bps, +5 days {fwd(5)[big.index].mean():+.1f}, "
      f"+20 days {fwd(20)[big.index].mean():+.1f} (mean); 24 Jun 2026: {fwd(0)['2026-06-24']:+.1f}, "
      f"{fwd(5)['2026-06-24']:+.1f}, {fwd(20)['2026-06-24']:+.1f}")
up = big[big > 0]
print(f"  same, only PTAX up-days ({len(up)}): same day {fwd(0)[up.index].mean():+.1f}, +5 days {fwd(5)[up.index].mean():+.1f}, "
      f"+20 days {fwd(20)[up.index].mean():+.1f}")
vol = r.rolling(20).std()
print(f"20-day PTAX volatility (% per day): 22 Jun {vol['2026-06-22']:.2f}, 22 Jul {vol['2026-07-22']:.2f}, "
      f"median since 2020 {vol.median():.2f}")
uu = pd.DataFrame({"binance": bps(d.usdtusd_window_usd), "coinbase": bps(d.usdtusd_cb_window_usd)})
print("USDT/USD in the PTAX window, bps from US$ 1, 15-30 Jun 2026:")
print(uu["2026-06-15":"2026-06-30"].round(1).T.to_string())
print(f"mean before/after: Binance {uu.binance.iloc[pos - 20:pos].mean():.1f} / {uu.binance.iloc[pos + 1:pos + 21].mean():.1f}, "
      f"Coinbase {uu.coinbase.iloc[pos - 20:pos].mean():.1f} / {uu.coinbase.iloc[pos + 1:pos + 21].mean():.1f}")

# S4: hour by hour, each venue's close against the last PTAX published before that hour closed
hv = pd.DataFrame({n: bps(s / (h.ptax_last_sell_brl_per_usd.reindex(s.index) * h.usdtusd_close_usd.reindex(s.index)))
                   for n, s in closes.items()})["2026-06-22":"2026-06-26 23:00"]
print("\nS4 - hourly premium vs last published PTAX (bps), 23 Jun 12h UTC - 24 Jun 18h UTC:")
print(hv["2026-06-23 12:00":"2026-06-24 18:00"].round(0).to_string())

BLUE, ORANGE, AQUA = "#2a78d6", "#eb6834", "#1baf7a"
INK2, GRID, SURFACE = "#52514e", "#e4e3df", "#fcfcfb"
plt.rcParams.update({"figure.facecolor": SURFACE, "axes.facecolor": SURFACE, "axes.edgecolor": GRID, "axes.labelcolor": INK2,
                     "xtick.color": INK2, "ytick.color": INK2, "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.6,
                     "axes.axisbelow": True, "axes.spines.top": False, "axes.spines.right": False, "font.size": 10,
                     "axes.titlesize": 12, "axes.titleweight": "bold", "axes.titlelocation": "left",
                     "legend.frameon": False, "savefig.dpi": 150, "savefig.bbox": "tight"})
fig, ax = plt.subplots(figsize=(11, 4.2))
for (name, s), color in zip(hv.items(), [BLUE, ORANGE, AQUA]):
    ax.plot(s.index, s, color=color, linewidth=1.6, label=name)
for t in d.loc["2026-06-22":"2026-06-26", "ptax_published_brt"] + pd.Timedelta(hours=3):
    ax.axvline(t, color=INK2, linewidth=0.7, linestyle=":")
ax.text(d.loc["2026-06-22", "ptax_published_brt"] + pd.Timedelta(hours=3), 0.98, " PTAX published", va="top",
        transform=ax.get_xaxis_transform(), fontsize=8, color=INK2)
low = hv["Mercado Bitcoin"].idxmin()
ax.annotate("Mercado Bitcoin: one trade after\ntwo hours with no trades", (low, hv["Mercado Bitcoin"].min()), xytext=(10, 0),
            textcoords="offset points", va="center", fontsize=8, color=INK2)
ax.axhline(0, color=INK2, linewidth=0.8)
ax.set_ylabel("premium vs last PTAX (bps)")
ax.set_xlabel("UTC")
ax.set_title("Hourly USDT/BRL premium on three exchanges, 22–26 Jun 2026")
ax.legend(loc="upper left")
fig.savefig(ROOT / "results/figures/P2-05_hourly_22_26_jun.png")
