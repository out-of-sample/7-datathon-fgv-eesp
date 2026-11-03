r"""P4-04: honest inference and window contents for the +93.9 bps headline (23 Jun 2026 notice).
Specification fixed before this script: tasks/P4-04-headline-inference-window.md -> S1 spec.

Clean    PTAX days outside +-20 PTAX days of every announced/effective date in P1-04 (same rule as p2_03_events.py).
A        mean[+1,+20] - mean[-20,-1] (t0 excluded). Placebos on non-overlapping clean windows: for each offset, keep a
         clean date if it is >= offset and >= 41 positions after the last kept one. p = (k+1)/(n+1), k two-sided.
B        mean[+1,+2] - mean[-20,-1] (before the 26 Jun meeting at +3). Placebos: all clean dates, and non-overlapping
         sets with stride 23.
C        one-day change 23 -> 24 Jun against clean one-day changes, all years and per year (description).
D        dated communications and market events within [-20,+20] PTAX days of t0 (sources in docs/sources.md).
Inputs   data/processed/P1-02_premium_daily.csv, data/processed/P1-04_events_brazil.csv
Outputs  results/tables/P4-04_nonoverlap.csv   one row per statistic x offset
         results/tables/P4-04_window_events.csv dated items in the window with the premium on each date
Run      python scripts/p4_04_inference.py
"""
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
PROC, TAB = ROOT / "data/processed", ROOT / "results/tables"
T0 = pd.Timestamp("2026-06-23")

d = pd.read_csv(PROC / "P1-02_premium_daily.csv", parse_dates=["date_brt"], index_col="date_brt").sort_index()
p = d["premium_bps"]
ev = pd.read_csv(PROC / "P1-04_events_brazil.csv")

# Clean dates: identical to scripts/p2_03_events.py
mapped = set()
for _, r in ev.iterrows():
    for col in ["date_announced", "date_effective"]:
        v = str(r[col]).strip()
        if v not in ("N/A", "nan"):
            sub = p.index[p.index >= pd.Timestamp(v)]
            if len(sub):
                mapped.add(p.index.get_loc(sub[0]))
black = {q for e in mapped for q in range(max(0, e - 20), min(len(p), e + 21))}
clean = [i for i in range(20, len(p) - 20) if i not in black]
t0 = p.index.get_loc(T0)


def stat(i, post):
    return p.iloc[i + 1:i + 1 + post].mean() - p.iloc[i - 20:i].mean()


def nonoverlap(post, stride):
    e, rows = stat(t0, post), []
    for off in range(stride):
        kept, last = [], -10**9
        for i in clean:
            if i >= off and i - last >= stride:
                kept.append(i)
                last = i
        s = np.array([stat(i, post) for i in kept])
        k2, k1 = int((np.abs(s) >= abs(e)).sum()), int((s >= e).sum())
        rows.append(dict(statistic=f"[+1,+{post}] vs [-20,-1]", observed_bps=round(e, 2), offset=off, n=len(s),
                         k_two_sided=k2, p_two_sided=round((k2 + 1) / (len(s) + 1), 4), k_one_sided=k1,
                         p_one_sided=round((k1 + 1) / (len(s) + 1), 4), max_abs_placebo_bps=round(np.abs(s).max(), 1)))
    return pd.DataFrame(rows)


# A and B
A, B = nonoverlap(20, 41), nonoverlap(2, 23)
pd.concat([A, B]).to_csv(TAB / "P4-04_nonoverlap.csv", index=False)
all_clean = {post: np.array([stat(i, post) for i in clean]) for post in (20, 2)}
for name, df, post in [("A", A, 20), ("B", B, 2)]:
    e, s = stat(t0, post), all_clean[post]
    k = int((np.abs(s) >= abs(e)).sum())
    print(f"{name} {df.statistic[0]}: observed {e:+.1f} bps | all {len(s)} clean dates: k={k}, p={(k + 1) / (len(s) + 1):.4f}, "
          f"largest |placebo| {np.abs(s).max():.1f} | non-overlapping: n {df.n.min()}-{df.n.max()}, "
          f"k {df.k_two_sided.min()}-{df.k_two_sided.max()}, p {df.p_two_sided.min():.3f}-{df.p_two_sided.max():.3f}")

# C: first-day change
d1 = p.diff()
first = d1.iloc[t0 + 1]
c1 = d1.iloc[[i for i in range(1, len(p)) if i not in black]]
print(f"C one-day change 23 -> 24 Jun: {first:+.1f} bps; clean one-day changes n={len(c1)}, as large: {(c1 >= first).sum()}")
others = d1.drop(p.index[t0 + 1]).dropna()
for y, s in others.groupby(others.index.year):
    big = s[s >= first]
    flags = d.loc[big.index, "ptax_window_uncertain"].tolist()
    print(f"  {y}: sd {s.std():5.1f}  max {s.max():+6.1f} on {s.idxmax().date()}  days >= first day: {len(big)} "
          f"{[str(x.date()) for x in big.index]} uncertain-window flags {flags}")

# D: dated items in the window (docs/sources.md)
items = [
    ("2026-06-18", "E-11", "Res. BCB 574 dated in the BCB register (reporting of virtual-asset FX operations from 3 Nov)"),
    ("2026-06-22", "E-11", "Res. BCB 574 published in the DOU"),
    ("2026-06-23", "E-05", "BCB notice to banks, FX brokers, crypto firms and funds (t0)"),
    ("2026-06-26", "E-05.5, E-12", "BCB meeting: suspension kept, in-book arbitrage released, 24-hour-hold draft presented"),
    ("2026-07-01", "E-10", "Res. BCB 580 published (SPSAVs as Tipo 3; rules from 1 Jan 2027)"),
    ("2026-07-07", "M-04", "Foxbit-NovaDAX partnership announced"),
    ("2026-07-18", "M-05", "Foxbit relaunches its B2B arm as Foxbit Infra (Saturday)"),
]
rows = []
for date, src, what in items:
    day = p.index[p.index >= pd.Timestamp(date)][0]
    rows.append(dict(date=date, source=src, item=what, ptax_day=day.date(), position=p.index.get_loc(day) - t0,
                     premium_bps=round(p[day], 1)))
W = pd.DataFrame(rows)
W.to_csv(TAB / "P4-04_window_events.csv", index=False)
print("D items within [-20,+20] PTAX days of t0:")
print(W.to_string(index=False))
print("Premium path, bps:", p.iloc[t0 - 1:t0 + 11].round(1).to_dict())
