r"""P3-21: who paid and who gained - the 23 Jun 2026 notice seen from four users with rules fixed in advance (illustration).
Specification fixed before this script: tasks/P3-21-who-paid.md -> Specification (commit 79e15d1).

Counterfactual  main: mean premium of the 20 PTAX days before t0 = 23 Jun 2026; variant: mean of PTAX days 22 Jul - 30 Oct.
Buyer cost      (premium_d - counterfactual) / 10,000 x US$ x PTAX_d, in R$.
Holder gain     (premium_d - premium_t0) / 10,000 x US$ x PTAX_d, in R$ (no counterfactual needed).
U1  buys US$ 100k on one PTAX day in [t0+1, t0+20]: mean, min and max over the 20 days; checks F-015 (R$ 5,052) within 2%.
U2  buys US$ 10k a month, Jan-Oct 2026: first PTAX day (main), last PTAX day, and equal amounts every PTAX day.
U3  holds US$ 100k of USDT at t0; sells on t0+1, t0+5, t0+20 or 30 Oct.
U4  buys US$ 100k on t0+1 and holds; value vs the official dollar at t0+20 and 30 Oct (negative = loss).
U5  not recomputed (F-025).
Input   data/processed/P1-02_premium_daily.csv
Output  results/tables/P3-21_who_paid.csv
Run     python scripts/p3_21_who_paid.py
"""
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
d = pd.read_csv(ROOT / "data/processed/P1-02_premium_daily.csv", parse_dates=["date_brt"]).set_index("date_brt")
d = d.loc[:"2026-10-30"]
prem, ptax = d.premium_bps, d.ptax_sell_brl_per_usd
i0 = d.index.get_loc(pd.Timestamp("2026-06-23"))
cf = {"pre-notice (20 days)": prem.iloc[i0 - 20:i0].mean(), "post-spike (22 Jul-30 Oct)": prem.loc["2026-07-22":].mean()}
print({k: round(v, 2) for k, v in cf.items()})


def cost(day, usd, c):
    return (prem[day] - c) / 1e4 * usd * ptax[day]


rows = []
add = lambda user, case, c_name, brl: rows.append({"user": user, "case": case, "counterfactual": c_name, "brl": brl})

for c_name, c in cf.items():
    # U1: needed dollars during the spike
    u1 = pd.Series([cost(day, 100_000, c) for day in d.index[i0 + 1:i0 + 21]])
    for stat in ("mean", "min", "max"):
        add("U1 needed dollars in the spike (US$ 100k, one day)", stat, c_name, getattr(u1, stat)())
    # U2: monthly saver, Jan-Oct 2026
    y = d.loc["2026-01":"2026-10"]
    m = y.index.to_period("M")
    usd_day = y.groupby(m).ptax_sell_brl_per_usd.transform("size").rdiv(10_000)  # US$ 10k per month over its PTAX days
    for case, days, usd in [("first PTAX day", y.groupby(m).head(1).index, 10_000),
                            ("last PTAX day", y.groupby(m).tail(1).index, 10_000),
                            ("every PTAX day", y.index, usd_day)]:
        per = pd.Series([cost(day, usd if case != "every PTAX day" else usd[day], c) for day in days], index=days)
        for mon, v in per.groupby(per.index.to_period("M")).sum().items():
            add("U2 monthly saver (US$ 10k/month)", f"{case} {mon}", c_name, v)
        # review fix (F-033): only purchases after t0 can carry a cost of the notice; earlier ones are a benchmark
        add("U2 monthly saver (US$ 10k/month)", f"{case} purchases up to t0", c_name, per[:d.index[i0]].sum())
        add("U2 monthly saver (US$ 10k/month)", f"{case} purchases after t0", c_name, per[d.index[i0 + 1]:].sum())
        add("U2 monthly saver (US$ 10k/month)", f"{case} total", c_name, per.sum())
    if c_name == "post-spike (22 Jul-30 Oct)":
        continue  # U3 and U4 do not use a counterfactual
    # U3: already held USDT at t0
    for lab, day in [("t0+1", d.index[i0 + 1]), ("t0+5", d.index[i0 + 5]), ("t0+20", d.index[i0 + 20]), ("30 Oct", d.index[-1])]:
        add("U3 held USDT at t0 (US$ 100k)", f"sells {lab} ({day:%d %b})", "none (vs premium at t0)", cost(day, 100_000, prem.iloc[i0]))
    # U4: bought on t0+1 and held
    b = d.index[i0 + 1]
    for lab, day in [("t0+20", d.index[i0 + 20]), ("30 Oct", d.index[-1])]:
        add("U4 bought on t0+1 and held (US$ 100k)", f"value at {lab} ({day:%d %b})", "none (vs premium at t0+1)",
            cost(day, 100_000, prem[b]))

res = pd.DataFrame(rows)
out = ROOT / "results/tables/P3-21_who_paid.csv"
res.to_csv(out, index=False, float_format="%.0f")
print(res[~res.case.str.match(r"(first|last|every) PTAX day \d")].round(0).to_string(index=False))

# Check against F-015 in bps: F-015 converts at a fixed reference PTAX of R$ 5.38, this script at each day's PTAX
# (mean R$ 5.14 in the spike window), so in R$ the two differ by the PTAX ratio, not by the premium (deviation logged in P3-21).
w = d.iloc[i0 + 1:i0 + 21]
excess = w.premium_bps.mean() - cf["pre-notice (20 days)"]
u1 = res.query("user.str.startswith('U1') and case == 'mean' and counterfactual.str.startswith('pre')", engine="python").brl.iloc[0]
print(f"\nU1 excess {excess:.2f} bps vs F-015 93.9 bps; U1 mean R$ {u1:,.0f} at daily PTAX (mean {w.ptax_sell_brl_per_usd.mean():.4f})"
      f" vs F-015 R$ 5,052 at PTAX 5.38: {u1 / 5052.36 - 1:+.1%}")
assert abs(excess / 93.9 - 1) < 0.02, "U1 does not reproduce F-015 within 2%"
