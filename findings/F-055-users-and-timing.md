---
id: F-055
title: In one account, the four users and the treasury agree - a buyer during the spike paid about R$ 4,840 more per 100k, a holder who sold at once received about R$ 7,300; waiting 10 days with a hedge swung from −R$ 8,800 to +R$ 6,700 by decision date in 2026, and a simple "wait when the premium is above its 60-day median" rule helped out of sample only because of the June shock
status: exploratory
task: P3-48
date: 2026-11-08
checked_by: -
---

## Claim
**One identity for both slides.** Every trade of 100k USDT on day t carries the excess premium
E_t = q U_t X_t (p_t − p_ref), with p_ref = 15.24 bps (the 20 PTAX days before the notice). Buyers pay E_t, sellers receive it.
Waiting h days with a currency hedge changes the outcome by W = q X_T [U_t(1+p_t) − U_T(1+p_T)] (minus fees; zero carry in the
primary convention). The four users of F-033 and the treasury of F-039 are policies on these two lines.

**Users (re-derived).** Needed dollars in the spike (U1): +R$ 4,838 on average (R$ 1,894 to 8,817 by day; F-033: 4,842, the
small gap is 100k USDT instead of US$ 100k). Monthly saver (U2): +R$ 752 on the four purchases after the notice (F-033: 753).
Already held USDT (U3), sold on 24 Jun: +R$ 7,294 (F-033 measured from the 23 Jun premium: 6,802); on 30 Oct: −R$ 2,467.
Panic buyer (U4), bought 24 Jun and sold 30 Oct: −R$ 9,761 (F-033, against holding official dollars: −10,070); had they waited 10 days with a hedge, +R$ 1,974.

**Treasury (reconciled).** With F-039's conventions (USDT idle while the forward prices a 5% US$ rate) the script reproduces
F-039 exactly (+89.66 / +92.32 / +164.04 bps at 5 / 10 / 20 days from 25 Jun). Without that carry (primary here: the USDT bought
now earns the same US$ rate) waiting saved +80 / +73 / +126 bps. **F-039's seller figures (−R$ 4,697 / −11,594 / −21,704) are
unhedged**, while its buyer figures are hedged; hedged, the seller who waited lost −R$ 4,249 / −3,886 / −6,686. Slide 9 of
deck v4 put the two side by side.

**Every decision date (new).** For a hedged buyer waiting 10 days, the outcome in 2026 ranged from −R$ 8,800 (deciding in
early June: waiting meant buying into the spike) to +R$ 6,700 (deciding in early July). Over the 198 test days (2026), always
waiting averaged −R$ 3 per day (R0, acting at once, is 0 by definition). The rule fixed in the spec, wait only when the premium
is more than k bps above its 60-day median (k = 5, chosen on 2021–2025, the lowest value on the grid), met the pre-set reading
"helped out of sample" at 10 days (mean +R$ 197 per decision day; acting days +R$ 649, non-overlapping 95% interval +153 to
+2,109) but not at 5 or 20 days. **Post hoc**, without decision dates inside the shock (24 Jun – 21 Jul) the same rule averaged
−R$ 55 (always waiting −R$ 277): the rule's gain is the June shock. For a seller, waiting from any shock day lost money at
10 days (−R$ 2,457 on average, worse on 19 of 20 days); the mirror rule never asked to wait then.

## Evidence
Reproduce: `.venv/bin/python scripts/p3_48_users_timing.py` (self-checks first; reruns are byte-identical) →
`results/tables/P3-48_users.csv`, `P3-48_reconcile.csv`, `P3-48_rules.csv`, `P3-48_stress.csv`, `P3-48_waiting_daily_h10.csv`, `results/figures/P3-48_waiting.png`; slide chart `results/figures/P5-10_waiting.png` (`scripts/p5_10_deck_figures.py`, section 6).
Specification committed before the script: `99d2325`.

| Rule (hedged buyer, h = 10) | Train 2021–25, mean W per day | Test 2026, mean W per day | Test, non-overlapping | Acting days, 95% CI (non-overl.) | Pre-set reading |
|---|---:|---:|---:|---:|---|
| R0 act now | 0 | 0 | 0 | – | baseline |
| R1 always wait | +R$ 35 | −R$ 3 | −R$ 21 | −856 to +688 | not shown |
| R2 wait iff p − median₆₀ > 5 | +R$ 480 | +R$ 197 | +R$ 342 | +153 to +2,109 | helped out of sample |
| R2, test without shock starts (post hoc) | – | −R$ 55 | +R$ 97 | −414 to +1,287 | – |

h = 5: R2 test +R$ 114 (non-overlapping +33, CI −1,372 to +1,474), not shown. h = 20: +R$ 161 (−120), not shown.
Seller mirror rule (wait iff p − median₆₀ < −k): not shown at any horizon.
Stress (h = 10, trading fee 0/10/30 bps × idle-USDT carry 0/2.5/5%): R2 keeps the reading in all 9 cases; fees cancel
(both actions pay them); carry > 0 favours waiting by construction (always waiting passes at 5%).

## Caveats
- Retrospective on a known episode; only the R2 rule and its grid were fixed before computing, and its test period contains
  the shock it is meant to exploit. The post hoc split shows the gain is that one shock.
- k = 5 is the edge of the grid: in practice "wait whenever the premium is above its recent median".
- Hedge ideal (covered interest parity, no margin, no basis); access, liquidity and execution not modelled.
- Users' numbers move by up to R$ 500 from F-033 because one reference (p_ref) replaces F-033's per-user bases.

## Used in deck
Deck v4 slide 8 (users and waiting, one account) and slide 9 (rule test), 8 Nov. Still exploratory: teammate re-run pending.

## History
- 2026-11-08, agent for Renzo: created (P3-48 S2–S3)
