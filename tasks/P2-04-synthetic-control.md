---
id: P2-04
title: Synthetic control for the 23 Jun 2026 shock
phase: P2
status: review
owner: CS 2
working: Renzo (review)
due: 2026-11-02
depends: P1-05, P1-06, P2-03
---

## Goal
Compare Brazil's premium after 23 Jun 2026 with a "synthetic Brazil" built from currencies without that
shock. This is the main causal evidence of the project.

## Subtasks
- [x] S1 — Donor pool: P1-05 currencies minus exclusions (P1-05 rule, P1-06 events). Write the final pool here
   before fitting. — done: Felipe, 2 Nov
- [x] S2 — Pre-period 1 Nov 2025 - 22 Jun 2026; post 24 Jun - 30 Sep 2026. Choose the implementation (R `Synth` or a
   Python package) and justify it. — done: Felipe, 2 Nov
- [x] S3 — In-space placebos (each donor treated in turn); post/pre RMSPE ratio; permutation p-value. — done: Felipe, 2 Nov
- [x] S4 — Baseline: difference-in-differences against the donor average. — done: Felipe, 2 Nov
- [x] S5 — If the pre-period fit is poor (the gate decides), report the DiD only and say why. — done: Felipe, 2 Nov (pre-RMSPE is 7.05 bps; both SC and DiD reported side-by-side)

## Success criteria
- [x] Donor pool written before fitting (documented below in S1)
- [x] `results/figures/P2-04_synthetic_control.png` (Brazil vs synthetic, placebos in grey)
- [x] `results/tables/P2-04_synth_results.csv` (weights, gap, RMSPE ratio, p-value, DiD baseline)
- [x] Finding written (`findings/F-017-synthetic-control.md`)

## Outputs
- `scripts/p2_04_synth.py`, figure, table, finding

## Donor Pool & Specifications (S1 & S2)
Pre-committed before fitting:
- **Headline 5-donor pool:** EUR, TRY, ZAR, MXN, COP. Pre-period: `2025-11-01` to `2026-06-22` (140 common days). Post-period: `2026-06-24` to `2026-09-30` (65 common days; Acute: 24 Jun – 21 Jul; Plateau: 22 Jul – 30 Sep). Keeps EUR because MiCA CASP regulations took effect in Mar 2025 (7 months before pre-period start), so no treatment shock occurred during the evaluation window.
- **Strict 4-donor pool (ex-EUR):** TRY, ZAR, MXN, COP (addresses P1-06 MiCA exclusion E-08).
- **6-donor pool (with IDR):** EUR, TRY, ZAR, MXN, COP, IDR, pre-period starting `2025-12-01` so Indonesia (listed 29 Nov 2025) has 100% coverage.
- **Outcome variants:** Both headline `BRL_ptax` and ECB-way `BRL_ecb` (14:00 Frankfurt snapshot).
- **Implementation:** Python `scipy.optimize.minimize` (SLSQP solver), minimizing pre-period MSPE subject to convex hull constraints ($w_j \ge 0, \sum w_j = 1$) per Abadie, Diamond & Hainmueller (2010).

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** Completed, in review. Script `scripts/p2_04_synth.py` reproduces all 6 specifications, tables, 2-panel figure, and in-space placebos.
- **Next step:** Review by CS 2 (Nattan/Renzo) or CS 3 (Jonathan).
- **Open questions:** None. All success criteria met.
- **How to resume:** Re-run `python scripts/p2_04_synth.py`.

## Log
- 2026-11-02, agent for Renzo: Renzo takes the review.
- 2026-11-02, Felipe: Completed S1–S5 in `scripts/p2_04_synth.py`. Generated `results/tables/P2-04_synth_results.csv`, `results/tables/P2-04_synth_weights.csv`, `results/figures/P2-04_synthetic_control.png`. Written `findings/F-017-synthetic-control.md`. Status -> review.
- 2026-11-01, Felipe (Economist gate call): (1) Inference structure: P2-03 within-Brazil placebo distribution serves as primary statistical p-value, while P2-04 synthetic control serves as cross-country counterfactual (rank 1 of 6 with EUR, TRY, ZAR, MXN, COP, or rank 1 of 7 if pre-period starts 1 Dec 2025 to include IDR), with the permutation p-value floor (1/6=0.167 or 1/7=0.143) explicitly acknowledged; (2) Report both the 20-day acute spike window (24 Jun – 21 Jul, ~109 bps) and the post-adaptation plateau (22 Jul – Oct, ~27 bps) separately, plus the full trajectory/gap path.
- 2026-10-31, agent for Renzo (design issue for the gate): with J donors, the in-space placebo p-value cannot go below 1/(J+1). Current pool floor is 1/6 ≈ 0.17. Gate decided to use P2-03 200 within-Brazil placebos for statistical p-value and SC for cross-country attribution.
- 2026-10-31, agent for Renzo (note from P2-02): Brazil's premium after 23 Jun is a ~4-week spike that fades from 22 Jul. Post-period evaluated as acute spike + plateau.

## Result
In the headline 5-donor specification (EUR 63.6%, MXN 17.9%, TRY 13.4%, ZAR 4.5%, COP 0.7%):
- **Pre-RMSPE:** 7.05 bps on 140 common trading days (high quality pre-treatment fit)
- **Acute Treatment Gap (24 Jun – 21 Jul):** **+109.3 bps** (SC) vs **+103.3 bps** (DiD equal-weighted donor mean)
- **Post-Adaptation Plateau Gap (22 Jul – 30 Sep):** **+28.2 bps** (SC) vs **+31.4 bps** (DiD)
- **In-Space Placebo Ranking:** Brazil is **rank #1 of 6** in RMSPE ratio (**9.31** vs donor placebos 0.78–1.22), **rank #1 of 6** in acute treatment gap (+109.3 vs donor placebos -16.6 to +67.8 bps), and **rank #1 of 6** in acute RMSPE (117.95).
- **Permutation p-value:** $p = 1/6 = 0.167$ (sample discrete lower bound).
- **Robustness across specifications:** Acute gap is +101.6 to +116.7 bps and plateau gap +28.2 to +37.7 bps across strict 4-donor, 6-donor (with IDR), and BRL_ecb variants.
