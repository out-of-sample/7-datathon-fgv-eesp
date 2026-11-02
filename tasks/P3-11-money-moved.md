---
id: P3-11
title: So what (1) - how much money the spike moved, and to whom
phase: P3
status: todo
owner: Economist
working: -
due: 2026-11-03
depends: P2-03, P3-01
---

## Goal
Turn "+94 bps for a month" into money: the extra paid by buyers of USDT/BRL over the pre-notice level during the
spike, on the volume actually traded. Frame it as the tariff equivalent of a quota: the notice restricted how
stablecoins could be brought in, and the rent went to whoever could still bring them in, not to the Treasury.
Plan: `docs/06-so-what.md`, answer 1. Rough sizing on 2 Nov (not a finding): about R$ 145 mn on three venues,
R$ 106 mn on Binance alone, on about R$ 16 bn traded.

## Subtasks
- [ ] S1 — Write the specification in this file before running: transfer = Σ over the spike window [+1, +20] PTAX
  days of (premium − pre-window mean [−20, −1]) × traded volume in BRL; weekend volume assigned to the previous
  PTAX day; per venue and total; Binance alone as the conservative figure.
- [ ] S2 — Range: alternative pre-windows (10, 40 days), the synthetic-control gap instead of the pre-mean
  (F-017), and the same transfer computed at every clean placebo date (P2-03) so the jury sees what an ordinary
  month moves.
- [ ] S3 — `scripts/p3_11_money.py`, table `results/tables/P3-11_transfer.csv`, finding.
- [ ] S4 — Two sentences of interpretation for the deck: transfer, not a welfare loss; who is on each side.

## Success criteria
- [ ] Specification committed before the run
- [ ] Transfer reported per venue, with the placebo comparison and the range
- [ ] Finding says what the number is not (welfare loss; whole market)

## Outputs
- `scripts/p3_11_money.py`, `results/tables/P3-11_transfer.csv`, finding

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** not started. Rough sizing script (not in the repo) gave R$ 145 mn / R$ 106 mn on Binance.
- **Next step:** S1
- **Open questions:** Foxbit volume quality (F-008): include it or report Binance alone as the headline? For the
  interpretation: the closed channel paid zero IOF-Câmbio against 3.5% for ordinary buyers (E-05.10, `docs/sources.md`), and
  F-024 measures the quantity that stopped (stablecoin purchases abroad −US$ 2.0 bn in July 2026).
- **How to resume:** volumes are in the frozen raw files (`scripts/p1_03_second_venue.py` shows how to read them).

## Log
- 2026-11-02, agent for Renzo: created (plan `docs/06-so-what.md`).

## Result
