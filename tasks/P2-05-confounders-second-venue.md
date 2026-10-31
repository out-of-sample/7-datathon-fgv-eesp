---
id: P2-05
title: Rule out other causes of the 24 Jun 2026 jump
phase: P2
status: done
owner: CS 1
working: -
due: 2026-11-02
depends: P1-02, P1-03
---

## Goal
Check that the jump is not caused by something else: a BRL shock (PTAX rose ~0.7% on 24 Jun), a USDT/USD
move, a Binance-only problem, or a data error.

## Subtasks
- [x] S1 — Second venue (P1-03): does it show the jump on the same day? — done: Renzo, 31 Oct
- [x] S2 — BRL volatility and PTAX moves 15-30 Jun 2026; USDT/USD that week. — done: Renzo, 31 Oct
- [x] S3 — Binance announcements about BRL deposits/withdrawals in June-July 2026. — done: Renzo, 31 Oct
- [x] S4 — Hourly view of 23-25 Jun: when exactly did the premium move? — done: Renzo, 31 Oct

## Success criteria
- [x] Each candidate cause checked, with evidence, in a finding file
- [x] Clear conclusion: "jump confirmed on N venues; not explained by X, Y, Z" or the opposite

## Outputs
- `scripts/p2_05_checks.py`, figure of the hourly premium 22-26 Jun, finding

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** done (reviewed and verified by Jonathan). Jump replicated across Binance, Foxbit, and Mercado Bitcoin; figure and finding F-009 confirmed.
- **Next step (reviewer):** `python scripts/p1_02_premium.py && python scripts/p2_05_checks.py`; the printed tables must
  match F-009; look at `results/figures/P2-05_hourly_22_26_jun.png`. Then set `status: done`.
- **Open questions:** (1) Exact time of the BCB notice on 23 Jun (P1-04): the premium starts rising that afternoon.
  (2) Optional cross-check of PTAX against FRED DEXBZUS: FRED blocks scripts, so it needs a manual browser download.
  (3) Two non-regulatory candidate events passed to P1-04 (Binance Pix suspension 2022, tick cut 2025).
- **How to resume:** S3 was a news search (queries in the Log); everything else is in the script.

## Log
- 2026-10-31, Jonathan: review complete; scripts/p2_05_checks.py executed cleanly; jump replicated across all 3 venues; figure verified; status -> done
- 2026-10-31, agent for Renzo: S1–S4 done; F-009; status → review. S3 searches: "Binance Brasil depósito saque reais Pix
  suspenso junho 2026", "Binance BRL deposits withdrawals June 2026 announcement Brazil", "Foxbit julho 2026 volume
  USDT institucional OTC formador de mercado": no 2026 event; Binance's 2022 Pix suspension found (E-07).
- 2026-10-31, agent for Renzo: Renzo takes P2-05
- 2026-10-31, agent for Renzo (note from P1-03): S1 inputs ready: Foxbit (`data/raw/foxbit/`) and Mercado Bitcoin
  (`data/raw/mercadobitcoin/`) hourly USDT/BRL, both covering Jun 2026. Foxbit sits ~12.5 bps below Binance on
  average, so compare each venue's change around 23 Jun, not levels. Foxbit's volume rose ~6x from July 2026 (P1-03
  Result): worth a look in S3 (venue-specific events).

## Result
**Jump confirmed on 3 venues; not explained by a move in the real, by USDT/USD, by a Binance event or by a data
error** (F-009). The 20-day mean premium rose by 93.9 bps on Binance, 93.3 on Foxbit and 94.9 on Mercado Bitcoin.
The 24 Jun PTAX move (+0.68%) was ordinary, and after such moves the premium usually falls a little; USDT/USD moved
by less than 1 bps. Hour by hour, the premium was still at its earlier level in the 23 Jun PTAX window and began rising
that afternoon (Brasília), with a second step at the 24 Jun open. What caused it is for P1-04 / P2-03 / P2-04.
