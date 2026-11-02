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
- 2026-10-31, agent for Renzo (note from P3-03, nobody working here yet): the real-time monitor's upward sum starts building on 25 May 2026 and is at 92% of its threshold on 23 Jun; weekly premium 10–22 bps from mid-May vs 5.8 in Jan–Apr. Check a pre-trend before 23 Jun when fixing the windows (F-014).
- 2026-10-31, agent for Renzo (note from P2-02): the high regime after 23 Jun 2026 lasts about 20 PTAX days (24 Jun – 21 Jul; F-011), so the planned [+1, +20] window measures the spike almost exactly. The lasting effect is smaller (regime mean 9.3 → 26.8 bps after 22 Jul). Suggest reporting a later window too (e.g. [+21, +60]) as a pre-declared extra, decided before running.
- 2026-11-01, Felipe (Economist gate call): For the 23 Jun 2026 shock, report both the acute 20-day spike window ([+1, +20] trading days, 24 Jun – 21 Jul, ~109 bps) and the post-adaptation plateau ([+21, +60] trading days, 22 Jul – Oct, ~27 bps) separately. Within-Brazil placebo distribution (200 random dates) serves as primary statistical p-value. Event 23 Jun 2026 is framed as empirically confirmed break across 3 venues coinciding with reported BCB supervisory ofício (ConJur secondary source, not public DOU norm).

## Result
