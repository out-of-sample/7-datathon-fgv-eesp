---
id: P2-05
title: Rule out other causes of the 24 Jun 2026 jump
phase: P2
status: doing
owner: CS 1
working: Renzo
due: 2026-11-02
depends: P1-02, P1-03
---

## Goal
Check that the jump is not caused by something else: a BRL shock (PTAX rose ~0.7% on 24 Jun), a USDT/USD
move, a Binance-only problem, or a data error.

## Subtasks
- [ ] S1 — Second venue (P1-03): does it show the jump on the same day? — doing: Renzo
- [ ] S2 — BRL volatility and PTAX moves 15-30 Jun 2026; USDT/USD that week.
- [ ] S3 — Binance announcements about BRL deposits/withdrawals in June-July 2026.
- [ ] S4 — Hourly view of 23-25 Jun: when exactly did the premium move?

## Success criteria
- [ ] Each candidate cause checked, with evidence, in a finding file
- [ ] Clear conclusion: "jump confirmed on N venues; not explained by X, Y, Z" or the opposite

## Outputs
- `scripts/p2_05_checks.py`, figure of the hourly premium 22-26 Jun, finding

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** not started
- **Next step:** S1
- **Open questions:** none
- **How to resume:** -

## Log
- 2026-10-31, agent for Renzo: Renzo takes P2-05
- 2026-10-31, agent for Renzo (note from P1-03): S1 inputs ready: Foxbit (`data/raw/foxbit/`) and Mercado Bitcoin
  (`data/raw/mercadobitcoin/`) hourly USDT/BRL, both covering Jun 2026. Foxbit sits ~12.5 bps below Binance on
  average, so compare each venue's change around 23 Jun, not levels. Foxbit's volume rose ~6x from July 2026 (P1-03
  Result): worth a look in S3 (venue-specific events).

## Result
