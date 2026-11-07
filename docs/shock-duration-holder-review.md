# Independent review: shock duration and holder decisions

**Reviewer:** Codex independent agent for Felipe. **Date:** 6 November 2026, Brasília.
**Status:** Completed and approved. All implementation outputs verified.

## Review scope

The approved question concerns an institution already holding USDT and funding a known BRL obligation. Review covers new tasks P3-30 and P3-31; frozen core findings are context, not re-estimated here. No live trading, legal determination of institutional access, or investment recommendation is being verified.

## Pre-implementation checks

The holder specification correctly distinguishes the net terminal BRL comparison from the historical acquisition cost. With quantity Q, price P, proportional charge c and fixed charge f, net proceeds are QP(1-c)-f. A fixed charge paid now must be deducted before investment accumulation. A fixed charge paid on exit belongs in the numerator of the required future gross price. Recovery of a positive premium reduces the holder's BRL sale price if FX and USDT/USD are unchanged.

The institutional calendar is a material assumption. Observed PTAX publication days are a defensible historical proxy, not proof of exchange cash settlement availability. Positive settlement lag must either move sale earlier or invalidate payment-date sale. Indicative window prices do not establish execution at institutional size.

Duration must remain distinct from the holder decision. Even a perfectly calibrated normalization probability does not predict FX appreciation, the premium's terminal magnitude, investment access, or feasible execution. Recovery at the fifth in-band observation is the confirmable event date; backdating recovery to the first observation would use information unavailable then.

Episodes crossing chronological cutoffs must be censored or purged using the cutoff's information, not their eventually observed recovery. Missing observations cannot certify consecutive recovery. Future paths must not be supplied to a model at a prediction landmark. Correlated currencies and repeated landmarks must not be counted as independent events.

## Method reference checked

Opened 6 November 2026 by Codex reviewer: [scikit-survival Brier-score documentation](https://scikit-survival.readthedocs.io/en/stable/api/generated/sksurv.metrics.brier_score.html).

Verbatim excerpt: “The censoring distribution is estimated using the Kaplan-Meier estimator”. The documented IPCW estimator uses training survival observations and assumes censoring independent of features. Evaluation outside the training follow-up support is unsupported. A custom implementation must retain these conditions or explicitly justify its alternative.

## Evidence distinctions to preserve

- F-033 is an illustrative premium-only revaluation, not execution profit or a trading backtest. It cannot validate the new full-return comparison by itself.
- F-014's signal supplies a historical timing convention. Initial illustrative execution must follow the signal's observation window.
- F-037's BRLA route finding is exploratory and a linked, small market; it is neither an independent replication nor an executable institutional quote.
- A failed forecasting gate is an informative limitation. It does not validate a profitable holder rule, and a successful scenario identity is not empirical predictive evidence.

## Implementation checks

Independent execution and audit completed on 6 November 2026.

### Commands and test suites verified
1. `scripts/p3_30_duration.py --test`: All 8 unit tests pass (ordinary recovery, cutoff censoring, missing-data censoring, zero-MAD handling, future-data invariance, simple censored KM arithmetic, unsupported-horizon suppression, and downward overshoot exclusion).
2. `scripts/p3_30_duration.py`: Clean execution; produces `P3-30_input_audit.csv`, `P3-30_episodes.csv`, `P3-30_feasibility.csv`, `P3-30_descriptive_km.csv`, `P3-30_census.csv`, and `P3-30_run_summary.json`.
3. `scripts/p3_31_holder.py`: All 6 `unittest` boundary tests pass (zero/unchanged prices, compression vs FX appreciation, unequal cost threshold identity, missing prices, settlement lag rejection, fixed-cost accumulation ordering). Generates `P3-31_thresholds.csv`, `P3-31_historical_comparison.csv`, `P3-31_historical_inputs.csv`, `P3-31_sensitivity.csv`, `P3-31_audit.json`, and figures `results/figures/P3-31_thresholds.png`, `results/figures/P3-31_historical.png`.

### Reconciled calculations and numbers

#### P3-30 / F-038 (Duration feasibility)
- **Input audit:** 1,520 PTAX dates (2020-10-13 to 2026-10-30). BRL has 1,520 valid rows (0 missing). Comparison series valid counts on the PTAX grid: EUR 1,510, TRY 1,510, ZAR 964, MXN 642, COP 560.
- **Feasibility gate (3-sigma primary):**
  - Training (to 2024-12-31): 11 episodes, 10 recoveries, 1 censored. (Floor: 10 episodes / 5 recoveries; passed).
  - Validation (2025): 3 episodes, 3 recoveries, 0 censored. (Floor: 5 episodes / 2 recoveries; failed: 3 < 5).
  - Test (2026): 1 episode, 0 recoveries, 1 censored. (Floor: 5 episodes / 2 recoveries; failed: 1 < 5, 0 < 2).
- **2026 onset:** Sole 2026 episode started on 25 May 2026 (reference median 5.31 bps, sigma 4.40 bps, band [0.91, 9.72] bps). Lasted 111 PTAX days through 30 October 2026 without confirmed recovery (`sample_end`).
- **Sensitivity:** 2-sigma yields 13/12 train, 2/1 val, 1/1 test (with the 2025-06-09 episode spanning 289 days into 2026); 4-sigma yields 6/5 train, 2/2 val, 1/0 test.
- **Gate decision:** Feasibility floor fails; no predictive hazard model fitted (`model_fitted: false`); status correctly recorded as `predictive_validation_unavailable`.

#### P3-31 / F-039 (Holder decision)
- **Base parameters:** 100,000 USDT; initial indicative gross price R$ 5.278475 (25 June 2026); initial net proceeds R$ 527,319.6525 (at 10 bps fee).
- **Required appreciation (10% annual net effective return, symmetric 10 bps):**
  - 5 PTAX days: +18.93 bps (gross price R$ 5.288466)
  - 10 PTAX days: +37.89 bps (gross price R$ 5.298477)
  - 20 PTAX days: +75.93 bps (gross price R$ 5.318554)
- **Retrospective June comparison (10% rate, actual indicative path):**
  - 5 PTAX days (deadline 02 July): waiting minus initial conversion = -R$ 4,696.94
  - 10 PTAX days (deadline 09 July): waiting minus initial conversion = -R$ 11,593.57
  - 20 PTAX days (deadline 23 July): waiting minus initial conversion = -R$ 21,703.71
- **Fixed FX and USDT/USD counterfactual (isolating premium compression):**
  - 5 PTAX days: -R$ 5,407.53
  - 10 PTAX days: -R$ 6,167.17
  - 20 PTAX days: -R$ 11,171.53
- **Price identity:** `PTAX * USDTUSD * (1 + premium/10000) == USDTBRL` verifies across all 21 rows of `P3-31_historical_inputs.csv`.

### Review findings and sign-off
- No bugs, arithmetic errors, or undocumented parameter overrides were found.
- The scripts adhere strictly to non-leakage, edge-case handling, and defensive assertion standards.
- Findings F-038 and F-039 accurately report verified numbers without predictive overclaiming.
- Review approved and closed.

