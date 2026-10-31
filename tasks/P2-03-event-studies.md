---
id: P2-03
title: Before/after test for every dated rule, with placebo dates
phase: P2
status: todo
owner: CS 2
working: -
due: 2026-11-02
depends: P1-02, P1-04
---

## Goal
For each rule in the event list, measure how the premium changed, including the rules that did nothing.
The 23 Jun 2026 row is also the number the AI analysts (extension A) are compared with.

## Subtasks
- [ ] S1 — Mean premium in [-20, -1] vs [+1, +20] trading days around each effective date; Newey-West standard errors.
   Repeat with announcement dates where they differ.
- [ ] S2 — 200 random placebo dates (same weekday distribution); report where each real event falls.
- [ ] S3 — Baseline: pre-period mean (no-change forecast).

## Success criteria
- [ ] `results/tables/P2-03_event_table.csv` with every P1-04 event, including nulls
- [ ] Placebo distribution figure
- [ ] Finding written

## Outputs
- `scripts/p2_03_events.py`, table, figure, finding

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** not started
- **Next step:** S1
- **Open questions:** none
- **How to resume:** -

## Log

## Result
