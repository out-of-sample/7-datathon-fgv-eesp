---
id: F-003
title: Weekend moves in USDT/BRL only weakly anticipate Monday's official dollar
status: confirmed
task: P0-01
date: 2026-10-30
checked_by: Felipe
---

## Claim
When the FX market is closed, the crypto dollar still moves. Its weekend move is only weakly related to the
next Friday-to-Monday change in PTAX (correlation 0.26 over 291 weekends).

## Evidence
USDT/BRL from Friday 16:00 UTC to Sunday 23:00 UTC vs PTAX Friday -> Monday: corr 0.26, slope 0.51, 291 weekends.
Reproduce: `python scripts/00_probe_premium.py ...` (line starting with "weekends").

## Caveats
Side result; R-squared about 7%. Not part of the main question unless the team decides otherwise.

## Used in deck
Not yet.

## History
- 2026-11-02, Felipe (P4-02): independently audited `scripts/00_probe_premium.py` and verified exact reproduction on the 291-weekend probe sample (corr 0.263, slope 0.512) and full sample with Oct 2026 daily files (corr 0.45). Promoted to `confirmed` (`checked_by: Felipe`)
- 2026-10-31, agent for Renzo: two strong cases after the probe's sample ended. PTAX Fri 2 Oct 5.2238 → Mon 5 Oct
  4.9859 (−4.6%) and Fri 23 Oct 5.0377 → Mon 26 Oct 5.5007 (+9.2%); in both, USDT/BRL started moving on Sunday
  around 22h UTC (19h Brasília), about 18 hours before the PTAX window. What happened on those Sundays is `[verify]`
  (possibly Brazil's election rounds). Not yet a test of the claim. Data: `data/processed/P1-02_premium_hourly.csv`;
  figure `results/figures/P1-02_premium_hourly_recent.png`.
- 2026-10-30 — agent for Renzo: created from the probe
