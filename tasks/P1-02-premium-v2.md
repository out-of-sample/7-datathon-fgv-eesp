---
id: P1-02
title: Build the premium series v2 (time-matched, USDT/USD-adjusted)
phase: P1
status: todo
owner: CS 1
working: -
due: 2026-10-31
depends: P1-01
---

## Goal
Produce the official premium series the whole project uses: how much more USDT costs in reais than the
official dollar, in basis points, hourly and daily.

## Subtasks
- [ ] S1 — Definition: `premium = USDTBRL / (PTAX x USDTUSD) - 1`, in bps.
- [ ] S2 — Time matching: PTAX is the average of four windows between 10h and 13h Brasília (13-16 UTC). Match the
   USDT/BRL price to that window (mean of the hourly prices). Document the choice; also produce the
   closing-time version as an alternative.
- [ ] S3 — USDT/USD: use `1 / USDCUSDT` (assumes USDC = US$ 1). If Kraken USDT/USD is available, compare both.
- [ ] S4 — Daily series on PTAX days; hourly series for the weekend and noise work.
- [ ] S5 — Reproduce the probe's yearly means (F-001) within +/-5 bps, or explain the difference.

## Success criteria
- [ ] `data/processed/P1-02_premium_daily.csv` and `..._hourly.csv` with a column dictionary in the task Result
- [ ] Probe yearly means reproduced within +/-5 bps (table in Result)
- [ ] Both time-matching variants available
- [ ] Units stated in column names (`_bps`, `_utc`)

## Outputs
- `scripts/p1_02_premium.py`, `data/processed/P1-02_premium_daily.csv`, `data/processed/P1-02_premium_hourly.csv`

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** not started
- **Next step:** S1
- **Open questions:** none
- **How to resume:** -

## Log
- 2026-10-31, agent for Renzo (note from P1-01): inputs ready. Read the zips in `data/raw/binance/<PAIR>/`
  directly; USDCUSDT is missing 2022-09-26 to 2023-03-11 (S3 needs a fallback there); PTAX has one duplicate
  date and non-standard publication times on 24/31 Dec and Ash Wednesdays (S2). Details: P1-01 → Result.

## Result
