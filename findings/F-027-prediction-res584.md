---
id: F-027
title: Prediction committed on 2 Nov 2026 - the 24-hour hold of Res. BCB 584 (from 1 Jan 2027) will not move the premium detectably; its cost to a USDT holder is about 9 bps
status: exploratory
task: P3-13
date: 2026-11-02
checked_by: -
---

## Claim
Res. BCB 584 delays by 24 hours transfers above US$ 10,000 that leave a Brazilian provider for a foreign entity or a
self-custody wallet. It does not touch the incoming channel that sets the premium, and for a trader who already holds USDT
a one-day delay costs about 9 bps (5.5 bps of financing at the 13.75% Selic target + 3.7 bps of 95% one-day USDT/USD
risk). We predict that the before/after change at 4 Jan 2027 stays inside the ordinary-date range (−35.0 to +37.6 bps).
This is a scenario, committed before the rule takes effect (commit `393a14a`, 2 Nov 2026), to be checked in Feb 2027.

## Evidence
- Rule text: art. 2-B of Res. 142 as amended by Res. 584 (E-06b, opened 2 Nov 2026).
- Numbers: `python scripts/p3_13_prediction.py` (Selic SGS 432, D-17; USDT/USD and PTAX from P1-02, 460 PTAX days 2025–26;
  band from P2-03 placebo draws; monitor false-alarm rate 2.4/yr from P3-03 → 21% chance of an alarm in any 25-day window).
- Announcement (7 Aug 2026) already showed no detectable change: −22.0 bps, placebo p = 0.19 (F-026).
- Full prediction, falsification rule and limits: `results/tables/P3-13_prediction.md`.

## Caveats
- A prediction, not a result. Res. BCB 580's prudential rules also start on 1 Jan 2027 (E-10), so a move on that date
  could not be attributed to Res. 584 alone.
- P3-01 S2b prices the hold as one day of BRL risk (130.5 bps); that applies only if the hold left a trader exposed in
  reais, which an outgoing USDT transfer does not.

## Used in deck
Not yet (candidate: the monitor slide, `docs/06-so-what.md` answer 4).

## History
- 2026-11-02, agent for Renzo: created (P3-13).
