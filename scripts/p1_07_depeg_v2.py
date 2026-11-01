r"""P1-07 v2: Nattan's depeg detector (scripts/p1_07_depeg.py, "v1") with the review fixes
(tasks/P1-07-depeg-detector.md -> Review). v1 and its outputs stay untouched so both results can be compared.

Same relative-price screen, same frozen definition and same event IDs as v1. Changes, by review point:
  1 direction  each event is labelled below / above / both (vs $1); the chapter count uses below and both
  2 listing    an episode that starts at a pair's first candle is a listing artefact (USTC lists at $0.02)
  3 shared     at the event's peak hour, if another stablecoin/USDT pair is also outside +/-0.5% and within 0.1% of
               this pair, the move is USDT on Binance, not the coin: rejected
  4 recovery   the USD-level recovery is searched until the end of the data, not only until v1's end + 12 h
  5 delisting  events that start within 14 days of a pair's last candle (before the study end) are flagged, not
               dropped (UST's collapse ended in its delisting)
  6 data       Coinbase USDT/USD from the frozen data/raw/coinbase/USDT-USD-1h.csv instead of live API calls;
               Bitstamp read from data/raw/bitstamp/ (frozen by v1), not fetched again
Check: v1's rule (window to end + 12 h, no fixes) on the frozen Coinbase file must give v1's 29 USD-confirmed events.
Inputs   data/raw/binance/<stablecoin>USDT/ and data/raw/bitstamp/ (python scripts/p1_07_depeg.py),
         data/raw/coinbase/USDT-USD-1h.csv (python scripts/p1_01_download.py)
Outputs  data/processed/P1-07_depeg_events_v2.csv   v1's columns + direction, peak_utc, shared_with, near_delisting
         results/tables/P1-07_v1_vs_v2.csv          every v1 screen candidate, v1 vs v2 classification and end
         results/figures/P1-07_svb_weekend_v2.png
Run      python scripts/p1_07_depeg_v2.py
"""
import sys
from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import p1_07_depeg as v1  # reader, detector and bad-tick log exactly as in v1

RAW, PROC, TAB, FIG = ROOT / "data/raw", ROOT / "data/processed", ROOT / "results/tables", ROOT / "results/figures"
STUDY_END = pd.Timestamp("2026-09-30T23:00Z")
H, DAY = pd.Timedelta(hours=1), pd.Timedelta(days=1)

cb = pd.read_csv(RAW / "coinbase/USDT-USD-1h.csv")
cb = pd.Series(cb.close.to_numpy(), index=pd.to_datetime(cb.time_unix_utc, unit="s", utc=True), name="usdt_usd")
rel = {p: v1.read_pair(p).set_index("timestamp_utc").close.astype(float) for p in v1.PAIRS}
usd = {p: (r * cb.reindex(r.index)).dropna() for p, r in rel.items()}  # USD price of the coin, where Coinbase covers
usd_events = {p: v1.detect(u) for p, u in usd.items()}                 # fix 4: whole series, recovery seen if it exists


def window_end(pair, ev):
    """End of the relative episode, or v1's 14-day diagnostic window for an unrecovered one."""
    return ev["end_utc"] if ev["end_utc"] is not None else min(ev["start_utc"] + 14 * DAY, rel[pair].index[-1])


def v1_rule(pair, ev):
    """v1's confirmation (window start - 24 h to end + 12 h), on the frozen Coinbase file: reproduction check."""
    start, end = ev["start_utc"], window_end(pair, ev)
    if pair == "USDCUSDT" and pd.Timestamp("2023-03-11T14:00Z") <= start < pd.Timestamp("2023-03-13T00:00Z"):
        return "rejected"
    u = usd[pair][start - DAY:end + 12 * H]
    if start not in u.index:
        return "relative-price candidate"
    hits = [x for x in v1.detect(u) if x["start_utc"] <= end and (x["end_utc"] is None or x["end_utc"] >= start)]
    return "USD-confirmed" if hits else "rejected"


def shared_with(pair, t):
    """Fix 3: other pairs outside +/-0.5% at hour t and within 0.1% of this pair -> USDT moved on Binance."""
    x = rel[pair].get(t)
    return [q for q, r in rel.items() if q != pair and t in r.index
            and abs(r[t] - 1) > 0.005 and abs(x / r[t] - 1) < 0.001]


rows, check = [], 0
for pair in v1.PAIRS:
    r = rel[pair]
    for n, ev in enumerate(v1.detect(r), start=1):
        start, end = ev["start_utc"], window_end(pair, ev)
        check += v1_rule(pair, ev) == "USD-confirmed"
        row = {"event_id": f"P1-07-{pair}-{n:02d}", "pair": pair, "relative_start_utc": start,
               "relative_end_utc": ev["end_utc"], **ev, "direction": "", "peak_utc": pd.NaT, "shared_with": "",
               "near_delisting": r.index[-1] < STUDY_END - DAY and start >= r.index[-1] - 14 * DAY}
        if pair == "USDCUSDT" and pd.Timestamp("2023-03-11T14:00Z") <= start < pd.Timestamp("2023-03-13T00:00Z"):
            row |= {"classification": "rejected", "reason": "Binance relisted USDC/USDT mid-SVB episode (as v1)"}
        elif start <= r.index[0]:  # fix 2
            row |= {"classification": "rejected", "reason": "starts at the pair's first candle: listing artefact"}
        elif start not in usd[pair].index:
            row |= {"classification": "relative-price candidate", "reason": "no direct USDT/USD candle at the start"}
        else:
            hits = [x for x in usd_events[pair] if x["start_utc"] <= end and (x["end_utc"] is None or x["end_utc"] >= start)]
            if not hits:
                row |= {"classification": "rejected", "reason": "relative movement disappears after USDT/USD adjustment"}
            else:
                h = hits[0]
                seg = usd[pair][h["start_utc"]:h["end_utc"] or usd[pair].index[-1]]
                peak = (seg - 1).abs().idxmax()
                below, above = h["min_price"] < 0.995, h["max_price"] > 1.005
                row |= {k: h[k] for k in ("start_utc", "end_utc", "censored", "max_deviation_bps", "min_price",
                                          "max_price", "merged_episodes")}
                row |= {"peak_utc": peak, "shared_with": " ".join(shared_with(pair, peak)),  # fix 1, fix 3
                        "direction": "both" if below and above else "below" if below else "above"}
                row |= ({"classification": "rejected", "reason": "shared move with another stablecoin/USDT pair at "
                         "the peak hour: USDT on Binance, not the coin"} if row["shared_with"] else
                        {"classification": "USD-confirmed", "reason": "direct USDT/USD adjustment (frozen Coinbase)"})
        rows.append(row)
print(f"Check: v1 rule on the frozen Coinbase file gives {check} USD-confirmed events (v1 with live API calls: 29)")
assert check == 29, "frozen Coinbase data does not reproduce v1"

screen = pd.DataFrame(rows)
bad = pd.concat([pd.DataFrame(v1.quality_rejections(p, v1.read_pair(p))).assign(pair=p) for p in v1.PAIRS])
bad = bad.assign(classification="rejected", event_id=[f"P1-07-{p}-REJECT-{i:02d}" for p, i in
                                                      zip(bad.pair, bad.groupby("pair").cumcount() + 1)])
out = pd.concat([screen, bad]).sort_values(["pair", "start_utc"]).reset_index(drop=True)
out.to_csv(PROC / "P1-07_depeg_events_v2.csv", index=False, date_format="%Y-%m-%dT%H:%M:%SZ")

# v1 vs v2, every screen candidate (the bad-tick rows are identical by construction)
a = pd.read_csv(PROC / "P1-07_depeg_events.csv")
a = a[~a.event_id.str.contains("REJECT")]
cmp = a[["event_id", "classification", "start_utc", "end_utc", "censored", "max_deviation_bps"]].merge(
    screen[["event_id", "classification", "reason", "start_utc", "end_utc", "censored", "max_deviation_bps",
            "direction", "shared_with", "near_delisting"]], on="event_id", how="outer", suffixes=("_v1", "_v2"))
cmp.to_csv(TAB / "P1-07_v1_vs_v2.csv", index=False, date_format="%Y-%m-%dT%H:%M:%SZ")
print(f"\nRows: v1 {len(a) + (pd.read_csv(PROC / 'P1-07_depeg_events.csv').event_id.str.contains('REJECT')).sum()}, "
      f"v2 {len(out)}")
print(pd.crosstab(cmp.classification_v1, cmp.classification_v2, margins=True).to_string())
moved = cmp[(cmp.classification_v1 != cmp.classification_v2) | (cmp.end_utc_v1.fillna("") != cmp.end_utc_v2.fillna(""))]
print("\nCandidates whose classification or end changed:\n", moved[["event_id", "classification_v1",
      "classification_v2", "end_utc_v1", "end_utc_v2", "direction", "shared_with", "reason"]].to_string(index=False))

ok = screen[screen.classification == "USD-confirmed"]
dn = ok[ok.direction != "above"]
print(f"\nv2 USD-confirmed: {len(ok)} = below {(ok.direction == 'below').sum()}, both {(ok.direction == 'both').sum()}, "
      f"above {(ok.direction == 'above').sum()}; censored {ok.censored.sum()}")
print(f"Chapter count (below or both): {len(dn)}; of which near a delisting {dn.near_delisting.sum()}:")
print(dn[["event_id", "start_utc", "end_utc", "censored", "max_deviation_bps", "min_price", "near_delisting"]]
      .to_string(index=False))
s = dn.sort_values("start_utc")
shock = (s.start_utc.diff() > 2 * DAY).cumsum()
print(f"Distinct shocks among them (starts more than 48 h apart): {shock.nunique()}")

# SVB figure v2: lowest close and intra-hour low, Sunday announcement, footnote below the axis (fixes from Review)
BLUE, ORANGE, INK2, GRID = "#2a78d6", "#eb6834", "#52514e", "#e4e3df"
x = pd.read_csv(RAW / "bitstamp/USDC-USD-1h_2023-03-10_to_2023-03-14.csv", parse_dates=["timestamp_utc"])
fig, ax = plt.subplots(figsize=(11, 5.4))
ax.fill_between(x.timestamp_utc, x.low, x.high, color=BLUE, alpha=.15, linewidth=0, label="mínimo–máximo na hora")
ax.plot(x.timestamp_utc, x.close, color=BLUE, lw=2, label="USDC/USD, fechamento horário")
ax.axvspan(pd.Timestamp("2023-03-10T21:00Z"), pd.Timestamp("2023-03-13T13:30Z"), color=ORANGE, alpha=.15, linewidth=0,
           label="bancos dos EUA fechados (sex 16h – seg 9h30, Nova York)")
ax.axhline(1, color=INK2, lw=.8, ls="--")
ann = pd.Timestamp("2023-03-12T22:15Z")
ax.axvline(ann, color=INK2, lw=1, ls=":")
ax.annotate("dom 18h15 (NY): Tesouro, Fed e FDIC\ngarantem os depósitos do SVB", (ann, 0.93), xytext=(8, 0),
            textcoords="offset points", ha="left", fontsize=9, color=INK2)
c, lo = x.loc[x.close.idxmin()], x.loc[x.low.idxmin()]
ax.annotate(f"menor fechamento: US$ {c.close:.3f}".replace(".", ","), (c.timestamp_utc, c.close), xytext=(12, -4),
            textcoords="offset points", fontsize=9, color=INK2)
ax.annotate(f"mínimo intra-hora: US$ {lo.low:.3f}".replace(".", ","), (lo.timestamp_utc, lo.low), xytext=(12, -4),
            textcoords="offset points", fontsize=9, color=INK2)
ax.set(title="USDC perdeu a paridade com os bancos fechados e voltou quase toda antes de reabrirem",
       ylabel="US$ por USDC", ylim=(0.78, 1.02))
ax.xaxis.set_major_locator(mdates.DayLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter("%d mar"))
ax.set_xlabel("hora (UTC)", color=INK2)
ax.grid(axis="y", color=GRID, lw=.6)
ax.spines[["top", "right"]].set_visible(False)
ax.legend(loc="lower right", frameon=False, fontsize=8)
fig.text(0.01, -0.03, "Fonte: Bitstamp OHLC 1h (USDC/USD), obtido em 31 out. 2026; Federal Reserve, comunicado de "
         "12 mar. 2023. A faixa marca o horário bancário, não a disponibilidade de resgate da Circle.", fontsize=8,
         color=INK2)
fig.savefig(FIG / "P1-07_svb_weekend_v2.png", dpi=200, bbox_inches="tight")
