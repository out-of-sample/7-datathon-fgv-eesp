---
id: F-003
title: Weekend moves in USDT/BRL only weakly anticipate Monday's official dollar
status: exploratory
task: P0-01
date: 2026-10-30
checked_by: -
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
- 2026-10-30 — agent for Renzo: created from the probe
