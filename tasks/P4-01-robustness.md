---
id: P4-01
title: Robustness battery for every headline number
phase: P4
status: review
owner: CS 2
working: -
due: 2026-11-04
depends: P2-02, P2-03, P2-04
---

## Goal
Show that each headline survives reasonable changes: windows, premium definitions, second venue, with/without USDT adjustment, donor pool changes.

## Subtasks
- [x] S1 — Implement event-study window variations (10d, 15d, 20d, 30d, plateaus, clean pre-period), premium definitions (unadjusted, Coinbase, dayclose, uncertain filter), and domestic exchange venues (Binance, Foxbit, Mercado Bitcoin, composite) in `scripts/p4_01_robustness.py`. — done: Felipe, 2 Nov
- [x] S2 — Implement Bai (1997) Theorem 1 vs Theorem 2 regime-specific heteroskedastic confidence intervals across series, and Synthetic Control donor pool variations (strict 4-donor, 6-donor w/ IDR, ECB fix, DiD, Colombian Ley Emiliani festivos filter). — done: Felipe, 2 Nov
- [x] S3 — Implement cross-asset checks (BTC/USD premium, BTC-implied USDT cross) and microstructure noise floor bounds (Corwin-Schultz, Abdi-Ranaldo, Roll 1984, high-low range); export `results/tables/P4-01_robustness.csv`. — done: Felipe, 2 Nov
- [x] S4 — Generate forest plot / specification curve `results/figures/P4-01_robustness_forest.png` and write finding `findings/F-022-robustness-battery.md`. — done: Felipe, 2 Nov

## Success criteria
- [x] Table results/tables/P4-01_robustness.csv covering every headline number — done: Felipe, 2 Nov
- [x] At least two alternatives per dimension — done: Felipe, 2 Nov
- [x] Any headline that does not survive is flagged in its finding — done: Felipe, 2 Nov

## Outputs
- `scripts/p4_01_robustness.py`
- `results/tables/P4-01_robustness.csv`
- `results/figures/P4-01_robustness_forest.png`
- `findings/F-022-robustness-battery.md`

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** review (all 4 subtasks and criteria 1–3 satisfied; 51-run robustness matrix exported and verified).
- **Next step:** Teammate review (Jonathan or Renzo for P4-02 independent re-check); integrate forest plot and robustness matrix into deck slides.
- **Open questions:** None. All headline claims survive across all 6 dimensions.
- **How to resume / reproduce:** Run `py scripts/p4_01_robustness.py`. Outputs inspectable at `results/tables/P4-01_robustness.csv` and `results/figures/P4-01_robustness_forest.png`.

## Log
- 2026-11-02, Felipe: completed P4-01 robustness battery. Implemented 51 specification tests across 6 dimensions covering event-study windows, premium definitions, 3 domestic exchange order books, Bai (1997) Theorem 1 vs Theorem 2 regime-specific heteroskedastic break CIs, Synthetic Control donor pools & Colombian Ley Emiliani holiday filter, and cross-asset BTC lockstep jump. Exported `results/tables/P4-01_robustness.csv`, generated publication figure `results/figures/P4-01_robustness_forest.png`, and wrote finding `findings/F-022-robustness-battery.md`. Status -> review.

## Result
The headline empirical findings survive robustly across all 6 dimensions tested (51 total specification runs in `results/tables/P4-01_robustness.csv`):
1. **Window length:** Acute jump ranges between **+73.7 bps** (30d) and **+128.3 bps** (10d), with the headline 20-day window yielding **+93.9 bps** ($t=5.80, p < 10^{-8}$). Dropping pre-trend days yields **+103.4 bps**. Post-adaptation plateau settles at **+19.3 bps** (40d) and **+11.5 bps** (71d).
2. **Premium definition:** Unadjusted USDT/BRL (+93.1 bps) and Coinbase USDT/USD adjusted (+93.7 bps) match the headline series (+93.9 bps) within 0.8 bps. Day-close yields +76.1 bps. Excluding 14 uncertain days is identical (+93.9 bps).
3. **Domestic venues:** Replicated identically across Binance (+93.9 bps), Foxbit (+93.3 bps), and Mercado Bitcoin (+94.9 bps), with an equal-weighted 3-venue composite jump of **+94.0 bps** (and +95.8 to +96.6 bps on June pre-window).
4. **Structural break CIs:** Bai (1997) Theorem 1 pooled homoskedastic 95% CI is **18 Jun – 30 Jun 2026** ($\pm 3.1$ PTAX days). Bai (1997) Theorem 2 regime-specific heteroskedastic NW CI constrains the pre-break quiet regime to an asymmetric 95% interval of **23 Jun – 30 Jun 2026** ($-0.1$ / $+3.9$ PTAX days).
5. **Synthetic Control:** Acute treatment gap ranges between **+101.6 and +116.7 bps** (headline: **+109.3 bps**, plateau: **+28.2 bps**), with Brazil ranking #1 in post/pre RMSPE ratio across all donor specifications ($p \le 0.200$). Filtering Colombian Monday bank holidays (*Ley Emiliani*) yields identical +109.5 bps acute and +28.3 bps plateau gaps.
6. **Cross-asset & noise bounds:** Bitcoin premium jumped in lockstep by **+93.8 bps** (BTC/USD) and **+93.0 bps** (BTC-implied USDT cross), confirming frictionless triangular arbitrage. Baseline trading friction is only 2.7 to 4.3 bps (signal-to-noise ratio: **22× to 35×**).
