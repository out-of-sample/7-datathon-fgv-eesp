---
id: P3-13
title: So what (4) - a dated prediction for the 24-hour hold (Res. 584, 1 Jan 2027) read by the monitor
phase: P3
status: done
owner: CS 1
working: -
due: 2026-11-03
depends: P3-01, P3-03
---

## Goal
Give the jury a claim they can check after the competition. Res. BCB 584 imposes an up-to-24-hour hold on
virtual-asset transfers ≥ US$ 10,000 abroad or to self-hosted wallets from 1 Jan 2027 (E-06b). An arbitrageur
who must wait a day carries one day of FX risk; P3-01 already computes that risk. Write, and commit before the
final, what the premium should do if the hold binds, and how the monitor (F-014) will show it.
Plan: `docs/06-so-what.md`, answer 4.

## Subtasks
- [x] S1 — Prediction file `results/tables/P3-13_prediction.md`: the bound (one-day FX risk, P3-01 S2b), the
  direction, the date window, what would falsify it, and how the monitor reads it. Labelled as a scenario. — done: Renzo, 2 Nov (the bound is not P3-01's BRL risk: see Handoff)
- [x] S2 — Commit it and record the hash here (the commit date is the proof). — done: Renzo, 2 Nov (`393a14a`)
- [x] S3 — One slide text (pt-BR): the monitor screenshot plus the prediction. — done: Renzo, 2 Nov (Result)

## Success criteria
- [x] Prediction committed with a hash before submission (8 Nov)
- [x] It states what result would prove it wrong

## Outputs
- `results/tables/P3-13_prediction.md` (commit `393a14a`), `scripts/p3_13_prediction.py`, `data/raw/bcb/sgs_432.json`, F-027

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** done, in review (F-027). Prediction committed in `393a14a` (2 Nov 2026): no detectable move at 4 Jan 2027
  (inside −35.0 to +37.6 bps); the hold costs a USDT holder about 9 bps; it only delays outgoing transfers.
- **Next step:** Felipe checks F-027. In Feb 2027 (after 20 PTAX days of 2027 data): download 2027 data, add the E-06b
  entry-into-force row, run `python scripts/p2_03_events.py`, compare with the prediction and report either way.
- **Open questions:** P3-01 S2b uses one day of BRL risk (130 bps) for the hold; for an outgoing USDT transfer the
  relevant risk is USDT/USD (3.7 bps) plus financing (5.5 bps). Felipe (P3-01) to decide whether S2b's note changes.
- **How to resume:** `python scripts/p3_13_prediction.py`; the prediction text is `results/tables/P3-13_prediction.md`.

## Log
- 2026-11-02, Felipe (review): Independently verified `data/raw/bcb/sgs_432.json` SHA-256 (`be93f6...`) and re-ran `py scripts/p3_13_prediction.py` (Selic 13.75% -> 5.5 bps + 3.7 bps 95% 1d USDT/USD risk = 9.1 bps for an outgoing USDT holder; 130.5 bps if exposed in BRL). Updated `P3-01` S2b note to cross-reference `P3-13`/`F-027` and integrated the dated prediction (`393a14a`) into Slide 12 of `deck/deck_v1_ptbr.md`. Status -> `done`.
- 2026-11-02, agent for Renzo: Res. 584 text read (hold applies to outgoing transfers only); S1–S3 done; prediction committed
  (`393a14a`); F-027; status review.
- 2026-11-02, agent for Renzo: Renzo takes P3-13 (asked by Renzo).
- 2026-11-02, agent for Renzo: created (plan `docs/06-so-what.md`).

## Result
Prediction committed 2 Nov 2026 (`393a14a`): the 24-hour hold will not move the premium detectably at 4 Jan 2027 (F-027).
Slide text (pt-BR), next to the monitor screenshot:
"Uma previsão que pode ser conferida: em 1º/01/2027 entra em vigor a retenção de 24 h da Res. BCB 584. Ela atrasa só as
saídas de cripto acima de US$ 10 mil, não as entradas que formam o prêmio, e custa a quem já tem USDT cerca de 9 pb (um dia
de Selic mais o risco do USDT). Previsão registrada em 02/11/2026: o prêmio não muda de forma detectável (fica entre −35 e
+38 pb). O monitor mostrará o resultado em dias. Ressalva: a Res. BCB 580 também começa a valer na mesma data."
