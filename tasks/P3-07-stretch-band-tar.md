---
id: P3-07
title: Stretch: threshold model of the no-arbitrage band
phase: P3
status: done
owner: CS 2
working: -
due: 2026-11-03
depends: P2-02
---

## Goal
Only if P2 is complete by Tue 3 Nov at noon: estimate a band-TAR model per regime to get the implied arbitrage cost and how fast deviations close. Plan: `docs/02-dolar-cripto.md` §7.8.

## Subtasks
- [x] S1 — Implement symmetric Band-TAR(1) grid search (10th–85th percentiles of $|z_{t-1}|$, $\ge 15\%$ trimming) around regime mean and 0 parity across all 6 P2-02 structural regimes, pooled pre/post-notice windows, and full sample (`scripts/p3_07_tar.py`). — done: Felipe, 2 Nov
- [x] S2 — Compute moving block-bootstrap 95% confidence intervals (500 replications, `seed=20261102`) for threshold $c$, outside reversion $\beta_{\text{out}}$, and implied half-life $t_{1/2}$; evaluate in-sample and out-of-sample (80/20 split) RMSE against Naive RW persistence and Linear AR(1) baselines (`prompt.md` §5 Rule 2). — done: Felipe, 2 Nov
- [x] S3 — Save `results/tables/P3-07_band_tar.csv`, generate 4-panel publication figure `results/figures/P3-07_band_tar.png`, and record findings in `findings/F-021-band-tar.md`. — done: Felipe, 2 Nov

## Success criteria
- [x] Started only if the P2 criteria are all ticked — done: Felipe, 2 Nov (all P2 tasks P2-01 through P2-06 completed and reviewed ahead of Tue 3 Nov noon gate).
- [x] Band width and reversion speed per regime with confidence intervals — done: Felipe, 2 Nov.
- [x] Finding written, or task marked dropped — done: Felipe, 2 Nov (`findings/F-021-band-tar.md`).

## Outputs
- `scripts/p3_07_tar.py`
- `results/tables/P3-07_band_tar.csv`
- `results/figures/P3-07_band_tar.png`
- `findings/F-021-band-tar.md`

## Handoff
- **State:** complete, awaiting teammate review.
- **Next step:** none; P3-07 is ready for review.
- **Open questions:** none; results are fully consistent with P2-01 noise floor (2–10 bps), P2-02 breaks, and F-008 volume adaptation.
- **How to resume:** run `python scripts/p3_07_tar.py` (takes ~15–20s for 500 bootstrap replications across all regimes).

## Log
- 2026-11-03, Jonathan: independent re-run verified; status -> done.
- 2026-11-02, Felipe: verified all P2 tasks complete ahead of the gate; implemented `scripts/p3_07_tar.py` estimating symmetric Band-TAR(1) models (Obstfeld & Taylor 1997) across 6 P2-02 regimes, pooled pre-notice, pooled post-notice, and full sample; completed 500 block-bootstrap replications for 95% CIs; conducted honest in-sample and out-of-sample RMSE evaluations vs Naive RW and Linear AR(1); generated `results/tables/P3-07_band_tar.csv` and 4-panel figure `results/figures/P3-07_band_tar.png`; authored `findings/F-021-band-tar.md`; set status to review.

## Result
Estimated symmetric Band-TAR(1) threshold models across all regimes defined by P2-02 structural breaks:
1. **Arbitrage Corridor Evolution:** The no-arbitrage band threshold steadily compressed from 55.0 bps (R1, Oct 2020 – Jul 2021) to 13.6 bps (R2, Jul 2021 – Aug 2024), 4.8 bps (R3, Aug 2024 – Jul 2025), and reached 1.61 bps [1.22, 5.13] in Regime 4 (Pre-notice, Jul 2025 – Jun 2026), sitting directly within the microstructure noise floor (2–10 bps, F-007).
2. **Post-Notice Shock & Reversion Slowdown:** Following the 23 Jun 2026 supervisory notice, the band expanded 26-fold to 41.95 bps [9.96, 52.63] in the acute spike (R5), before compressing to 9.40 bps [3.13, 14.41] during domestic order-book adaptation (R6, still ~6x wider than pre-notice). Across the pooled post-notice period (Jun – Oct 2026), outside-band mean reversion slowed to $\beta_{\text{out}} = -0.352$ with half-life $t_{1/2} = 1.60$ trading days (vs $\le 1.00$ day pre-notice).
3. **Model Benchmark Comparison:** Band-TAR outperforms naive persistence ($\Delta y_t = 0$) across all regimes (7.8%–26.5% lower RMSE in-sample). Band-TAR beats linear AR(1) in-sample across all regimes (most notably in high-friction regimes: +10.8% gain in R5 acute spike, +7.2% gain in R6 plateau), and outperforms linear AR(1) out-of-sample in regimes with active threshold dynamics (R2, R5, R6, pooled post-notice).
All code, tables, figures, and findings are generated and validated.
