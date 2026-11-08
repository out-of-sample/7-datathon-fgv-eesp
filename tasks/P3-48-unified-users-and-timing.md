---
id: P3-48
title: One account for who paid and whether waiting helped - the four users (P3-21) and the treasury timing decision (P3-31) in a single framework, tested on every decision date
phase: P3
status: doing
owner: CS 1
working: Renzo (agent)
due: 2026-11-08
depends: P3-21, P3-31, P3-39, P1-02
---

## Goal
Slide 8 (four users, F-033) and slide 9 (wait to buy or sell with a hedge, F-039/F-048) describe the same thing, the
premium path seen by someone who must buy or sell USDT, with different reference points, start dates, hedge rules and
counterfactuals. This task puts both in one accounting identity, re-derives the four users and the treasury numbers from
it, and replaces the single start date (25 Jun) with **every PTAX day** as a decision date, so that "could waiting have
helped?" is tested with a naive baseline and an ex-ante rule out of sample. Requested by Renzo on 8 Nov for the merged
slide 8; slide 9 is then rebuilt.

## Specification (fixed before the script; written 8 Nov 2026 ~05:10 Brasília, before any result of this task)

**Data.** `data/processed/P1-02_premium_daily.csv` (frozen 30 Oct): PTAX X_t (sell), USDT/USD U_t and USDT/BRL P_t in
the PTAX window, premium p_t (bps), with P_t = X_t U_t (1 + p_t/1e4). PTAX days only, 13 Oct 2020 – 30 Oct 2026. No filling.

**Notional.** q = 100,000 USDT. Trading fee c = 10 bps on every trade (P3-31 default), hedge fee 0.22 bps (R-07).

**Reference premium.** p_ref = mean premium of the 20 PTAX days before t0 = 23 Jun 2026 (15.24 bps, F-033 main).

**Identity 1 - premium cost of one trade (who paid).** A trade of q USDT on day t carries the excess premium
E_t = q · U_t · X_t · (p_t − p_ref)/1e4 (R$). A buyer pays E_t; a seller receives it. A round trip (buy on t1, sell on t2)
nets E_t2 − E_t1. Fees are reported apart, not in E.

**Identity 2 - value of waiting h days (timing).** Decision date t, horizon h ∈ {5, 10, 20} PTAX days, T = t + h.
- Buyer, hedged (primary): keep reais and buy US$ forward at t (covered interest parity, B3), buy USDT at T.
  W^B_hedged(t,h) = q (1+c) X_T [U_t (1 + p_t/1e4) − U_T (1 + p_T/1e4)] − hedge fee. FX leaves the decision.
  **Carry convention (primary): zero**, i.e. USDT bought at t can earn the same US$ rate the forward prices. Sensitivity:
  USDT idle with the forward priced at r_USD ∈ {2.5%, 5%} (adds the US$ carry, as F-039 did with 5%). This is the
  one deliberate difference from F-039, reconciled in the output.
- Buyer, unhedged: W^B_open(t,h) = q (1+c) (P_t − P_T) (no interest on either side; FX included).
- Seller of q USDT (hedged by selling US$ forward; or unhedged): W^S = −W^B with (1−c) in place of (1+c).
Positive W = waiting was better. Units R$ per 100k USDT and bps of the decision-day notional.

**Users as policies (re-derived with Identity 1, F-033 conventions kept beside them):**
- U1 needed dollars in the spike: buys on one PTAX day in [24 Jun, 21 Jul]: E_t, mean/min/max over the 20 days; and,
  from the same days, W^B_hedged for h = 5, 10, 20 (what waiting would have changed).
- U2 monthly saver: buys US$ 10k-equivalent (10,000 USDT) on the first PTAX day of each month Jul–Oct 2026: sum of E_t;
  and W^B_hedged(h=10) on each of those days.
- U3 already held USDT, sells on 24 Jun, 30 Jun, 21 Jul or 30 Oct: +E_t (seller). F-033 used p(23 Jun) as base; shown beside.
- U4 bought in the panic on 24 Jun, sells on 21 Jul or 30 Oct: E_sell − E_24Jun (F-033 compared with holding official
  dollars; shown beside).
- U5 sellers as a group: not recomputed (F-025).

**Treasury reconciliation.** W^B_hedged at t = 25 Jun with F-039's conventions (USDT idle, r_USD 5%, r_BRL 10%) must
reproduce F-039's +89.7 / +92.3 / +164.0 bps within 0.5 bps; seller at 25 Jun reproduces R$ 4,697 / 11,594 / 21,704 within R$ 50.

**Timing test on every decision date (the robustness core).** Decision dates: every PTAX day t with T = t + h ≤ 30 Oct 2026.
Training: t in 2021-01-01 … 2025-12-31. Test: t from 2026-01-01. Primary h = 10 (P3-41's primary horizon); h = 5, 20 reported.
Rules for the buyer (hedged):
- R0 act now (naive baseline): W = 0 by definition.
- R1 always wait h.
- R2 wait iff g_t = p_t − median(p_{t−60}, …, p_{t−1}) > k (premium unusually high, so expect it to compress);
  k chosen on training only, from {5, 10, 15, …, 100} bps, maximising mean W; ties → larger k.
For the seller the mirror rule (wait iff g_t < −k, k chosen the same way on the seller's training W).
Reported on test: mean W (all days and non-overlapping, every h-th day starting at the first test day), share of acting
days with W < 0, worst W, number of days the rule acts, and the same for start dates inside the shock (24 Jun – 21 Jul).
Pre-set reading: R2 "helped out of sample" only if its test mean W > 0 in both the all-days and the non-overlapping
samples **and** the non-overlapping 95% bootstrap interval (2,000 resamples, seed 48) of its mean W on acting days
excludes 0. Otherwise "not shown". R1 is read the same way.

**Stress.** Primary W^B_hedged and the R2 test repeated over trading fee {0, 10, 30 bps} × carry {0, 2.5%, 5%}
(9 cases); report the range.

**Not claimed.** Access, liquidity, execution and margin are not modelled; one country and one shock dominate the test
period; no welfare statement. Every result is retrospective except the R2 out-of-sample test, whose rule and grid are fixed here.

## Subtasks
- [ ] S1 — spec (this section) committed before the script — doing: Renzo (agent)
- [ ] S2 — `scripts/p3_48_users_timing.py` with self-checks (identities, F-033 and F-039 reconciliation) — doing: Renzo (agent)
- [ ] S3 — finding F-055 with tables and the pre-set readings
- [ ] S4 — merged slide 8 (users + timing); slide 9 rebuilt
- [ ] S5 — teammate re-run (not Renzo) before the result is called confirmed

## Success criteria
- [ ] Script reproduces F-033 U1 mean (R$ 4,842 at each day's PTAX, within R$ 60 given q in USDT) and F-039 within the tolerances above
- [ ] All rules reported against R0 on train and test, with the pre-set reading applied verbatim
- [ ] Finding written with the exact command; slide numbers trace to it

## Outputs
- `scripts/p3_48_users_timing.py`
- `results/tables/P3-48_users.csv`, `results/tables/P3-48_rules.csv`, `results/tables/P3-48_stress.csv`, `results/tables/P3-48_reconcile.csv`
- `results/figures/P3-48_waiting.png`

## Handoff
- **State:** spec written; script next.
- **Next step:** S2.
- **Open questions:** none yet.
- **How to resume:** `.venv/bin/python scripts/p3_48_users_timing.py`

## Log
- 2026-11-08 05:10, agent for Renzo: task created at Renzo's request (merge slide 8 users with slide 9 timing); spec fixed before the script

## Result
