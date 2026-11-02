---
id: P3-11
title: So what (1) - how much money the spike moved, and to whom
phase: P3
status: doing
owner: Economist
working: Renzo
due: 2026-11-03
depends: P2-03, P3-01
---

## Goal
Turn "+94 bps for a month" into money: the extra paid by buyers of USDT/BRL over the pre-notice level during the
spike, on the volume actually traded. Frame it as the tariff equivalent of a quota: the notice restricted how
stablecoins could be brought in, and the rent went to whoever could still bring them in, not to the Treasury.
Plan: `docs/06-so-what.md`, answer 1. Rough sizing on 2 Nov (not a finding): about R$ 145 mn on three venues,
R$ 106 mn on Binance alone, on about R$ 16 bn traded.

## Specification (written 2 Nov 2026 before the script exists; rough sizing above was seen, nothing else)

- **Windows** (PTAX days around t0 = 23 Jun 2026, as in P2-03): before [−20, −1], spike [+1, +20], after [+21, +60].
  A window covers every calendar day from its first PTAX day up to the day before the next window starts (spike:
  24 Jun – 21 Jul; after: 22 Jul – the day before PTAX day +61). Each calendar day takes the premium and PTAX of the
  latest PTAX day on or before it (weekends use Friday's).
- **Excess premium** e_t = premium_t (P1-02, bps) − mean premium over the before window.
- **Transfer** = Σ_t e_t / 10,000 × volume_t (USDT, UTC day, frozen venue files) × PTAX_t, in R$. Per venue (Binance,
  Foxbit, Mercado Bitcoin) and total. **Headline = Binance alone** (Foxbit's volume has open questions, F-008); the
  three-venue total is the measured upper figure.
- **Tariff equivalent** = transfer / Σ volume_t × PTAX_t, in bps: the volume-weighted excess the buyers paid.
- **Range:** before window of 10 and 40 PTAX days; the synthetic-control acute gap (+109.31 bps, F-017 headline) in place
  of e_t; the after window (description only: F-022 found it not distinguishable from noise).
- **Placebo:** the same Binance tariff equivalent and transfer at each P2-03 placebo date (200, `P2-03_placebo_draws.csv`)
  with full data. p = (k+1)/(n+1), k = placebos with |tariff equivalent| ≥ the observed one. The R$ ranking is shown too,
  but volume grew over time, so the bps ranking is the test.
- **Interpretation fixed in advance:** the transfer goes from buyers to whoever sold USDT at the higher price; it is not a
  welfare loss and it misses OTC desks and other venues. The tax gap of the closed route (zero IOF vs 3.5%, E-05.10)
  is context, not a test.

## Subtasks
- [x] S1 — Write the specification in this file before running: transfer = Σ over the spike window [+1, +20] PTAX
  days of (premium − pre-window mean [−20, −1]) × traded volume in BRL; weekend volume assigned to the previous
  PTAX day; per venue and total; Binance alone as the conservative figure. — done: Renzo, 2 Nov (above)
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
- **State:** specification written and committed before the script. Rough sizing (not in the repo) gave R$ 145 mn / R$ 106 mn on Binance.
- **Next step:** S2–S3, `scripts/p3_11_money.py`
- **Open questions:** Foxbit volume quality (F-008): include it or report Binance alone as the headline? For the
  interpretation: the closed channel paid zero IOF-Câmbio against 3.5% for ordinary buyers (E-05.10, `docs/sources.md`), and
  F-024 measures the quantity that stopped (stablecoin purchases abroad −US$ 2.0 bn in July 2026).
- **How to resume:** volumes are in the frozen raw files (`scripts/p1_03_second_venue.py` shows how to read them).

## Log
- 2026-11-02, agent for Renzo: Renzo takes P3-11 (owner Economist; asked by Renzo); specification written (S1).
- 2026-11-02, agent for Renzo: created (plan `docs/06-so-what.md`).

## Result
