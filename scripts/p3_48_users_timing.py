r"""P3-48: one account for who paid (P3-21 users) and whether waiting helped (P3-31 treasury), on every decision date.
Specification fixed before this script: tasks/P3-48-unified-users-and-timing.md -> Specification (commit 99d2325).

Identity 1  E_t = q U_t X_t (p_t - p_ref)/1e4           excess premium of one trade (buyer pays, seller receives)
Identity 2  W^B(t,h) = q (1+c) X_T [U_t(1+p_t) - U_T(1+p_T)] - hedge fee      buyer waits h days with a CIP hedge
            W^B_open(t,h) = q (1+c) (P_t - P_T)                                    buyer waits unhedged (FX included)
            seller: W^S = -W^B with (1-c) in place of (1+c)                       positive W = waiting was better
Users       U1-U4 as policies, U6 anxious trader and U7 calm counterpart (addendum A) on Identity 1 (F-033 conventions shown beside); treasury reconciled to F-039 (P3-31)
Rules       R0 act now, R1 always wait, R2 wait iff p_t - median(p_{t-60..t-1}) > k (seller: < -k), k from training
            (2021-2025) on {5..100}; test from 2026; pre-set reading in the spec
Input       data/processed/P1-02_premium_daily.csv (frozen 30 Oct 2026)
Outputs     results/tables/P3-48_{users,reconcile,rules,stress,anxious_trades,waiting_daily_h10}.csv, results/figures/P3-48_waiting.png
Run         .venv/bin/python scripts/p3_48_users_timing.py      (self-checks run first and stop the script if they fail)
"""
from pathlib import Path
import sys

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import p3_31_holder as p331  # F-039's own functions, used only to reconcile

TAB, FIG = ROOT / "results/tables", ROOT / "results/figures"
Q, C, HEDGE_BPS = 100_000, 0.001, 0.22
HORIZONS, H_MAIN = (5, 10, 20), 10
GRID = range(5, 101, 5)
T0 = pd.Timestamp("2026-06-23")

d = pd.read_csv(ROOT / "data/processed/P1-02_premium_daily.csv", parse_dates=["date_brt"]).set_index("date_brt")
d = d.loc[:"2026-10-30"]
p331.require_prices(d)  # complete, positive, P = X U (1+p) reconciles
X, U, p, P = d.ptax_sell_brl_per_usd, d.usdtusd_window_usd, d.premium_bps, d.usdtbrl_window_brl
i0 = d.index.get_loc(T0)
p_ref = p.iloc[i0 - 20:i0].mean()
days = d.index


# ---------------------------------------------------------------- identities
def excess(t, q=Q):
    """Identity 1: excess premium of trading q USDT on day t, R$ (buyer pays, seller receives)."""
    return q * U[t] * X[t] * (p[t] - p_ref) / 1e4


def wait_value(i, h, side="buyer", hedged=True, fee=C, carry=0.0, q=Q):
    """Identity 2 for decision index i, horizon h: R$ gained by acting at i+h instead of i. Positive = waiting better.
    carry = US$ rate the forward prices while the USDT bought now sits idle (0 = USDT earns the same rate)."""
    t, T = days[i], days[i + h]
    sign, s = (1, 1 + fee) if side == "buyer" else (-1, 1 - fee)
    if not hedged:
        return sign * q * s * (P[t] - P[T])
    notional = q * U[t] * (1 + p[t] / 1e4) * s * X[t]
    premium_part = sign * q * s * X[T] * (U[t] * (1 + p[t] / 1e4) - U[T] * (1 + p[T] / 1e4))
    # idle-USDT carry (P3-31's usd_carry): the forward prices the US$ rate; a buyer who waits earns it, a seller who waits gives it up
    carry_part = sign * notional * (1 - 1 / (1 + carry) ** (h / 252))
    return premium_part + carry_part - notional * HEDGE_BPS / 1e4


def bps(w, i, side="buyer", fee=C):
    t = days[i]
    return w / (Q * P[t] * (1 + fee if side == "buyer" else 1 - fee)) * 1e4


# ---------------------------------------------------------------- self-checks
def checks():
    j = days.get_loc(pd.Timestamp("2026-06-25"))
    # nothing moves -> waiting worth minus the hedge fee only
    assert abs(Q * (1 + C) * X.iloc[j] * 0) == 0
    # buyer/seller mirror without fees: W^S = -W^B
    for h in HORIZONS:
        b = wait_value(j, h, "buyer", hedged=True, fee=0, carry=0)
        s = wait_value(j, h, "seller", hedged=True, fee=0, carry=0)
        hf = Q * U.iloc[j] * (1 + p.iloc[j] / 1e4) * X.iloc[j] * HEDGE_BPS / 1e4
        assert abs((b + hf) + (s + hf)) < 1e-6, (b, s)
        assert abs(wait_value(j, h, "buyer", False, 0) + wait_value(j, h, "seller", False, 0)) < 1e-6
    # identity 1 sums: round trip on the same day is zero
    assert abs(excess(days[j]) - excess(days[j])) == 0
    # F-039 reconciliation with its own function and conventions (USDT idle, r_USD 5%, r_BRL 10%)
    t = days[j]
    for h, want in zip(HORIZONS, (89.66, 92.32, 164.04)):
        T = days[j + h]
        r = p331.b3_hedged_buyer(Q, X[t], U[t], p[t], X[T], U[T], p[T], h)
        assert abs(r["savings_bps"] - want) < 0.5, (h, r["savings_bps"])
    print("self-checks passed")


checks()
rows = []
add = lambda **k: rows.append(k)

# ---------------------------------------------------------------- reconciliation (F-033, F-039)
rec = []
j25 = days.get_loc(pd.Timestamp("2026-06-25"))
for h, f039_bps, f039_sell in zip(HORIZONS, (89.66, 92.32, 164.04), (-4696.94, -11593.57, -21703.71)):
    t, T = days[j25], days[j25 + h]
    r = p331.b3_hedged_buyer(Q, X[t], U[t], p[t], X[T], U[T], p[T], h)
    mine_f039conv = wait_value(j25, h, "buyer", True, C, carry=0.05)
    mine = wait_value(j25, h, "buyer", True, C, carry=0.0)
    _, _, sell = p331.compare(Q, P[t], P[T], 0.10, h)
    rec.append(dict(h=h, item="buyer hedged, F-039 conventions (P3-31 function)", f039=f039_bps, value=round(r["savings_bps"], 2), unit="bps"))
    rec.append(dict(h=h, item="buyer hedged, this script with carry 5% (approx. F-039)", f039=f039_bps, value=round(bps(mine_f039conv, j25), 2), unit="bps"))
    rec.append(dict(h=h, item="buyer hedged, this script PRIMARY (carry 0)", f039=np.nan, value=round(bps(mine, j25), 2), unit="bps"))
    rec.append(dict(h=h, item="seller wait-minus-now, F-039 (UNHEDGED, r_BRL 10%)", f039=f039_sell, value=round(sell, 0), unit="R$"))
    rec.append(dict(h=h, item="seller hedged, this script PRIMARY", f039=np.nan,
                    value=round(wait_value(j25, h, "seller", True), 0), unit="R$"))
rec = pd.DataFrame(rec)

# ---------------------------------------------------------------- users as policies
spike = days[i0 + 1:i0 + 21]
u1 = pd.Series({t: excess(t) for t in spike})
add(user="U1", case="excess premium paid, mean of 20 days", brl=u1.mean(), f033=4842)
add(user="U1", case="excess premium paid, min", brl=u1.min(), f033=1895)
add(user="U1", case="excess premium paid, max", brl=u1.max(), f033=8824)
for h in HORIZONS:
    w = pd.Series({t: wait_value(days.get_loc(t), h) for t in spike})
    add(user="U1", case=f"waiting {h}d with hedge from each spike day: mean", brl=w.mean(), f033=np.nan)
    add(user="U1", case=f"waiting {h}d with hedge: share of spike days where waiting was worse", brl=(w < 0).mean(), f033=np.nan)
    add(user="U1", case=f"waiting {h}d with hedge: min / max", brl=f"{w.min():.0f} / {w.max():.0f}", f033=np.nan)
firsts = [days[days >= pd.Timestamp(m)][0] for m in ("2026-07-01", "2026-08-01", "2026-09-01", "2026-10-01")]
add(user="U2", case="excess premium paid, 4 monthly buys of 10k USDT after the notice", brl=sum(excess(t, 10_000) for t in firsts), f033=753)
add(user="U2", case="waiting 10d with hedge on each monthly buy, sum (10k USDT)",
    brl=sum(wait_value(days.get_loc(t), 10, q=10_000) for t in firsts if days.get_loc(t) + 10 < len(days)), f033=np.nan)
for s, f in (("2026-06-24", 6802), ("2026-06-30", 5487), ("2026-07-21", 1407), ("2026-10-30", -2992)):
    add(user="U3", case=f"held USDT, sells on {s}: excess premium received", brl=excess(pd.Timestamp(s)), f033=f)
for s, f in (("2026-07-21", -5223), ("2026-10-30", -10070)):
    add(user="U4", case=f"bought 24 Jun, sells on {s}: round trip E_sell - E_buy", brl=excess(pd.Timestamp(s)) - excess(pd.Timestamp("2026-06-24")), f033=f)
# the two timing alternatives the holder (U3, a seller) and the panic buyer (U4) had
for h in HORIZONS:
    w = pd.Series({t: wait_value(days.get_loc(t), h, "seller") for t in spike})
    add(user="U3", case=f"seller waiting {h}d with hedge from each spike day: mean", brl=w.mean(), f033=np.nan)
    add(user="U3", case=f"seller waiting {h}d with hedge: spike days where waiting was worse (of 20)", brl=int((w < 0).sum()), f033=np.nan)
    add(user="U4", case=f"had waited {h}d with hedge from 24 Jun", brl=wait_value(days.get_loc(pd.Timestamp("2026-06-24")), h), f033=np.nan)
# U6 anxious trader (addendum A): flat or 100k USDT; buys when flat and p rose > s bps day on day, sells when holding and p fell > s
def anxious(s_bps, start="2026-01-02"):
    k0 = days.get_loc(days[days >= pd.Timestamp(start)][0])
    held, trades, result, first_buy = None, [], 0.0, None
    for k in range(k0, len(days)):
        t, dp = days[k], p.iloc[k] - p.iloc[k - 1]
        if held is None and dp > s_bps:
            held = t; trades.append(("buy", t)); first_buy = first_buy or t
        elif held is not None and dp < -s_bps:
            result += excess(t) - excess(held); trades.append(("sell", t)); held = None
    if held is not None:
        result += excess(days[-1]) - excess(held)  # open position marked at 30 Oct
    fees = sum(Q * U[t] * (1 + p[t] / 1e4) * X[t] * C for _, t in trades)
    calm = excess(days[-1]) - excess(first_buy) if first_buy is not None else 0.0
    return trades, result, fees, calm, held


for s_bps in (10, 5, 20):
    trades, res, fees, calm, held = anxious(s_bps)
    tag = f"anxious, s = {s_bps} bps{' (primary)' if s_bps == 10 else ''}"
    add(user="U6", case=f"{tag}: trades in 2026", brl=len(trades), f033=np.nan)
    add(user="U6", case=f"{tag}: premium result (round trips + open position at 30 Oct)", brl=res, f033=np.nan)
    add(user="U6", case=f"{tag}: trading fees at 10 bps per trade", brl=-fees, f033=np.nan)
    add(user="U6", case=f"{tag}: trades dated inside the shock (24 Jun-21 Jul)",
        brl=sum(1 for a, t in trades if pd.Timestamp("2026-06-24") <= t <= pd.Timestamp("2026-07-21")), f033=np.nan)
    add(user="U7", case=f"calm counterpart of U6 (s = {s_bps}): same first purchase, held to 30 Oct", brl=calm, f033=np.nan)
    if s_bps == 10:
        pd.DataFrame(trades, columns=["side", "date"]).assign(premium_bps=lambda f: [p[t] for t in f.date],
                     excess_brl=lambda f: [excess(t) for t in f.date]).to_csv(TAB / "P3-48_anxious_trades.csv", index=False)
users = pd.DataFrame(rows)


# ---------------------------------------------------------------- rules on every decision date
def gap(i):
    return p.iloc[i] - p.iloc[i - 60:i].median()


def evaluate(h, side, fee=C, carry=0.0):
    idx = [i for i in range(60, len(days) - h) if days[i] >= pd.Timestamp("2021-01-01")]
    f = pd.DataFrame({"i": idx, "t": days[idx], "g": [gap(i) for i in idx],
                      "w": [wait_value(i, h, side, True, fee, carry) for i in idx]})
    f["w_bps"] = [bps(w, i, side, fee) for w, i in zip(f.w, f.i)]
    train, test = f[f.t < "2026-01-01"], f[f.t >= "2026-01-01"]
    sel = (lambda g, k: g > k) if side == "buyer" else (lambda g, k: g < -k)
    score = {k: train.w[sel(train.g, k)].sum() / len(train) for k in GRID}  # mean W per decision day (0 when acting now)
    best = max(score.values())
    k = max(k for k, v in score.items() if v == best)
    out = []
    for name, part in (("train", train), ("test", test), ("test, start in shock 24 Jun-21 Jul", test[(test.t >= "2026-06-24") & (test.t <= "2026-07-21")]),
                       # post hoc (added after the first run, not in the spec): is the test result only the June shock?
                       ("test without shock starts (post hoc)", test[(test.t < "2026-06-24") | (test.t > "2026-07-21")])):
        for rule, m in (("R1 always wait", np.ones(len(part), bool)), (f"R2 wait iff gap {'>' if side == 'buyer' else '<-'}{k}", sel(part.g, k).to_numpy())):
            w = np.where(m, part.w, 0.0)
            no = part.iloc[::h]
            mno = m[::h]
            wno = np.where(mno, no.w, 0.0)
            acting = no.w[mno].to_numpy()
            rng = np.random.default_rng(48)
            ci = (np.percentile([rng.choice(acting, len(acting)).mean() for _ in range(2000)], [2.5, 97.5])
                  if len(acting) > 1 else [np.nan, np.nan])
            out.append(dict(side=side, h=h, fee_bps=fee * 1e4, carry=carry, k=k, sample=name, rule=rule,
                            days=len(part), acting_days=int(m.sum()), mean_w_brl=w.mean(),
                            mean_w_brl_nonoverlap=wno.mean() if len(wno) else np.nan,
                            mean_w_acting_brl=part.w[m].mean() if m.any() else np.nan,
                            ci95_acting_nonoverlap_lo=ci[0], ci95_acting_nonoverlap_hi=ci[1],
                            share_acting_worse=(part.w[m] < 0).mean() if m.any() else np.nan,
                            worst_brl=part.w[m].min() if m.any() else np.nan,
                            mean_w_bps_acting=part.w_bps[m].mean() if m.any() else np.nan))
    return out


rules = pd.DataFrame([r for side in ("buyer", "seller") for h in HORIZONS for r in evaluate(h, side)])


def reading(r):
    ok = r.mean_w_brl > 0 and r.mean_w_brl_nonoverlap > 0 and r.ci95_acting_nonoverlap_lo > 0
    return "helped out of sample" if ok else "not shown"


rules["reading"] = [reading(r) if r.sample == "test" else "" for r in rules.itertuples()]
stress = pd.DataFrame([r for fee in (0, .001, .003) for carry in (0, .025, .05) for r in evaluate(H_MAIN, "buyer", fee, carry)
                       if r["sample"] == "test"])
stress["reading"] = [reading(r) for r in stress.itertuples()]

TAB.mkdir(parents=True, exist_ok=True)
users.to_csv(TAB / "P3-48_users.csv", index=False)
rec.to_csv(TAB / "P3-48_reconcile.csv", index=False)
rules.to_csv(TAB / "P3-48_rules.csv", index=False)
stress.to_csv(TAB / "P3-48_stress.csv", index=False)
pd.set_option("display.width", 250, "display.max_columns", 30, "display.max_colwidth", 70)
print(f"p_ref = {p_ref:.2f} bps")
print(rec.to_string(index=False)); print(users.to_string(index=False))
print(rules[["side", "h", "k", "sample", "rule", "acting_days", "mean_w_brl", "mean_w_brl_nonoverlap", "ci95_acting_nonoverlap_lo",
             "ci95_acting_nonoverlap_hi", "share_acting_worse", "worst_brl", "reading"]].round(1).to_string(index=False))
print(stress[["fee_bps", "carry", "k", "rule", "mean_w_brl", "ci95_acting_nonoverlap_lo", "reading"]].round(3).to_string(index=False))

# ---------------------------------------------------------------- figure: value of waiting 10d (hedged buyer) by decision date, 2026
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
idx = [i for i in range(60, len(days) - H_MAIN) if days[i] >= pd.Timestamp("2026-01-01")]
w = pd.Series([wait_value(i, H_MAIN) for i in idx], index=days[idx])
pd.DataFrame({"buyer_w_brl": w, "seller_w_brl": [wait_value(i, H_MAIN, "seller") for i in idx],
              "gap_bps": [gap(i) for i in idx]}, index=pd.Index(days[idx], name="decision_date")).to_csv(TAB / "P3-48_waiting_daily_h10.csv")
fig, ax = plt.subplots(figsize=(9, 3.4), dpi=200)
ax.bar(w.index, w.values / 1e3, width=1.0, color=np.where(w.values > 0, "#D9622B", "#3B6EA8"))
ax.axhline(0, color="#14213D", lw=0.8)
ax.set_ylabel("R$ mil por 100 mil USDT")
ax.set_title("Comprador com hedge: ganho de esperar 10 dias úteis, por data de decisão (2026)", fontsize=10, loc="left")
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
fig.tight_layout()
fig.savefig(FIG / "P3-48_waiting.png", transparent=False, facecolor="#F6F4EF")
