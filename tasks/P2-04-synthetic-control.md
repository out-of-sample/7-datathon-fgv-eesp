---
id: P2-04
title: Synthetic control for the 23 Jun 2026 shock
phase: P2
status: todo
owner: CS 2
working: -
due: 2026-11-02
depends: P1-05, P1-06, P2-03
---

## Goal
Compare Brazil's premium after 23 Jun 2026 with a "synthetic Brazil" built from currencies without that
shock. This is the main causal evidence of the project.

## Subtasks
- [ ] S1 — Donor pool: P1-05 currencies minus exclusions (P1-05 rule, P1-06 events). Write the final pool here
   before fitting.
- [ ] S2 — Pre-period 1 Nov 2025 - 22 Jun 2026; post 24 Jun - 30 Sep 2026. Choose the implementation (R `Synth` or a
   Python package) and justify it.
- [ ] S3 — In-space placebos (each donor treated in turn); post/pre RMSPE ratio; permutation p-value.
- [ ] S4 — Baseline: difference-in-differences against the donor average.
- [ ] S5 — If the pre-period fit is poor (the gate decides), report the DiD only and say why.

## Success criteria
- [ ] Donor pool written before fitting
- [ ] `results/figures/P2-04_synthetic_control.png` (Brazil vs synthetic, placebos in grey)
- [ ] `results/tables/P2-04_synth_results.csv` (weights, gap, RMSPE ratio, p-value, DiD baseline)
- [ ] Finding written

## Outputs
- `scripts/p2_04_synth.py` (or `.R`), figure, table, finding

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** not started
- **Next step:** S1
- **Open questions:** none
- **How to resume:** -

## Log
- 2026-10-31, agent for Renzo (note from P2-02): Brazil's premium after 23 Jun is a ~4-week spike (≈ +100 bps) that fades from 22 Jul to ≈ +17 bps above the pre-period (F-011). A post-period of 24 Jun – 30 Sep averages the two; consider reporting the gap path, not only its mean. Gate decision.
- 2026-10-31, agent for Renzo (note from P1-05): donor premiums ready (`data/processed/P1-05_donor_premiums_daily.csv`). Exclusion rule in P1-05 → Result, to be confirmed at the gate before fitting. After rules 1 and 3: EUR, TRY, ZAR, MXN, COP (rule 2 waits for P1-06). IDR misses only because its Binance pair starts 29 Nov 2025. Each donor is measured at its own fix time; `BRL_ecb` is Brazil measured the same way as the ECB donors. ZAR, MXN, COP are thin on Binance (noisier).

## Result
