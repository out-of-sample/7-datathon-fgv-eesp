---
id: F-034
title: Exploratory Polygon BRLA price check using the PTAX window
status: exploratory
task: P5-01
checked_by: -
---

Flash's saved daily-close series reproduces the baseline, spike and fade means of 54.5, 139.9 and 54.4 bps. Using the main project's four PTAX-window hourly opens instead gives 36.4, 145.9 and 46.6 bps (21, 20 and 29 days), or +109.6 bps from baseline to acute. The 24 June daily-close reading was 164.9 bps. The acute-window maximum of the daily-close series was 241.8 bps.

This is a single-pool descriptive cross-rate comparison, assuming USDC/USD = 1. It shares PTAX and the event with the main study. See the [dossier](../docs/flash-findings-mentor-leads.md) for the remaining checks and the [bundle](../data/README.md#flash-mentor-leads-bundle) for provenance.

Reproduce from the repository root with `python scripts/p5_01_flash_checks.py`.

## History
- 2026-11-05, agent for Renzo: extended by F-037 (P3-24): PTAX-window S20 on the core study's windows +111.0 bps (this
  finding's +109.6 used a baseline that includes 23 Jun); robustness, second pool, contracts and the supply series there
- 2026-11-05, agent for Renzo: bundle moved from `results/flash-mentor-leads/` to `data/raw/flash-mentor-leads/` (raw data stays out of git, `prompt.md` §6–§7); link and `scripts/p5_01_flash_checks.py` path updated; numbers unchanged (re-run)
