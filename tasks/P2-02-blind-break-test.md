---
id: P2-02
title: Blind structural-break test on the premium
phase: P2
status: doing
owner: CS 2
working: Renzo
due: 2026-11-01
depends: P1-02, P1-04
---

## Goal
Let an algorithm find the dates where the premium changed regime **without telling it the policy dates**,
then check which breaks match known events. If it finds 24 Jun 2026 on its own, that is our headline chart.

## Subtasks
- [x] S1 — **Before running**, write the specification here: method (Bai-Perron via R `strucchange`, or Python
   `ruptures`), minimum segment = 20 trading days, maximum breaks = 8, number of breaks chosen by BIC. — done: Renzo, 31 Oct (Specification below)
- [ ] S2 — Run on the daily premium (P1-02). Report break dates with confidence intervals.
- [ ] S3 — Match breaks to the P1-04 events (within +/-5 trading days). List unmatched breaks as "unexplained".
- [ ] S4 — Robustness: the alternative time-matching variant of the premium.

## Success criteria
- [x] Specification committed before the first run
- [ ] `results/tables/P2-02_breaks.csv` (date, CI, matched event or "unexplained")
- [ ] `results/figures/P2-02_premium_breaks.png` (premium, noise band, breaks, event markers)
- [ ] Finding written

## Outputs
- `scripts/p2_02_breaks.py` (or `.R`), table, figure, finding

## Specification (S1)
Written 31 Oct 2026 by the agent for Renzo and **committed before the first run** of any break test on the premium.
Main choices (method, 20-day minimum, BIC) come from `docs/02-dolar-cripto.md` §7.2 (30 Oct, before the v2 series
existed). Honesty note: the team has already seen the premium chart and knows about the 24 Jun 2026 jump; "blind"
means the algorithm is given no event dates, and every choice below is fixed before it runs.

- **Data.** `premium_bps` from `data/processed/P1-02_premium_daily.csv`: every PTAX day, 13 Oct 2020 – 30 Oct 2026
  (1,520 days, no gaps; the 14 `ptax_window_uncertain` days are kept, as in P1-02). One observation = one PTAX day.
- **Model.** Pure mean-shift model (Bai–Perron with a constant only): the premium is a constant plus noise within each
  regime. Break dates estimated by least squares with dynamic programming (`ruptures.Dynp`, cost `l2`, exact global
  optimum for each number of breaks), minimum segment 20 PTAX days, 0 to 8 breaks.
- **Number of breaks.** Primary: BIC as in Bai–Perron, `ln(SSR_m / T) + p ln(T) / T` with `p = 2m + 1` (m break dates
  plus m+1 means). Also reported: LWZ (Liu, Wu & Zidek 1997), `ln(SSR_m / (T − p)) + (p · 0.299 / T) (ln T)^2.1`.
  **Pre-committed rule:** BIC is known to over-select breaks when errors are serially correlated (here AR(1) ≈ 0.65).
  If BIC picks the maximum (8), we treat that as over-selection and the headline count is LWZ's; otherwise BIC's.
- **Confidence intervals.** Bai (1997) for a mean shift: 95% CI = break ± 11.03 · ω² / δ² PTAX days, where δ is the
  change in mean at the break and ω² the long-run variance of the residuals of the chosen model (Newey–West, Bartlett
  kernel, lag floor(4 (T/100)^(2/9)) = 7). Constants `[verify]` against Bai (1997) (L-03). Intervals reported in PTAX days
  and mapped to dates.
- **What counts as "found 24 Jun 2026".** A headline break whose 95% CI contains 23 or 24 Jun 2026, or whose date is
  within ±5 PTAX days of 23 Jun 2026 (the S3 matching window).
- **Matching (S3, after P1-04).** A break matches an event if the event date is within ±5 PTAX days of the break date;
  we also report whether the event lies inside the 95% CI. Breaks with no event are reported as "unexplained". Known
  non-rule candidates to list beside the rules: Binance tick cut (~27 Jun 2025, F-007), Binance Pix suspension
  (Jun–Jul 2022, E-07), FTX collapse (Nov 2022), SVB weekend (Mar 2023).
- **Robustness (S4), same specification:** (a) `premium_dayclose_bps` (other timing); (b) `premium_cb_bps` (Coinbase
  USDT/USD, from May 2021); (c) both BIC and LWZ counts shown for every series.
- **Figure.** Premium, P2-01 noise band, regime means, break dates with 95% CIs; event markers added in S3.
- **Not done:** no tuning of the minimum segment, the maximum or the penalty after seeing the output; any later variant
  is reported as an extra, next to this one.

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** not started
- **Next step:** S1
- **Open questions:** none
- **How to resume:** -

## Log
- 2026-10-31, agent for Renzo: S1 specification written and committed before any break-test run
- 2026-10-31, agent for Renzo: Renzo takes P2-02 (CS 2 task; Renzo covers CS 2 work and tells Nattan). S1–S2 and S4 now; S3 waits for P1-04
- 2026-10-31, agent for Renzo (note from P2-01, nobody working here yet): Binance cut the USDT/BRL price tick
  tenfold on ~27 Jun 2025 (0.001 → 0.0001 BRL; F-007). The premium steps down around Jul 2025 (P1-02 figures).
  If the break test finds a break there, the tick change is a candidate explanation besides any rule.

## Result
