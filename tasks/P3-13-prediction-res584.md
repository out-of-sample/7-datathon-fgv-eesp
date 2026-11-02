---
id: P3-13
title: So what (4) - a dated prediction for the 24-hour hold (Res. 584, 1 Jan 2027) read by the monitor
phase: P3
status: todo
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
- [ ] S1 — Prediction file `results/tables/P3-13_prediction.md`: the bound (one-day FX risk, P3-01 S2b), the
  direction, the date window, what would falsify it, and how the monitor reads it. Labelled as a scenario.
- [ ] S2 — Commit it and record the hash here (the commit date is the proof).
- [ ] S3 — One slide text (pt-BR): the monitor screenshot plus the prediction.

## Success criteria
- [ ] Prediction committed with a hash before submission (8 Nov)
- [ ] It states what result would prove it wrong

## Outputs
- `results/tables/P3-13_prediction.md`

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** not started.
- **Next step:** S1
- **Open questions:** does the hold bind arbitrageurs at all (transfers between Brazilian exchanges are not
  covered)? Read Res. 584 before writing the bound.
- **How to resume:** P3-01 risk number in `results/tables/P3-01_route_costs.csv`; monitor in `scripts/p3_03_monitor.py`.

## Log
- 2026-11-02, agent for Renzo: created (plan `docs/06-so-what.md`).

## Result
