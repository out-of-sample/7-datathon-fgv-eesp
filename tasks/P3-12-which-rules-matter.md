---
id: P3-12
title: So what (2) - which rules moved the premium (published rules vs the confidential notice)
phase: P3
status: doing
owner: Economist
working: Renzo
due: 2026-11-03
depends: P2-03
---

## Goal
One chart and one slide from the P2-03 event table, no new estimation: every dated rule, how it was issued
(decree, published resolution with notice period, confidential notice), the channel it touched, and its
before/after change against the placebo band. The point for regulators: the premium shows which channel
arbitrageurs actually use; only the notice that closed the funds' import route moved it. Plan: `docs/06-so-what.md`,
answer 2.

## Subtasks
- [ ] S1 — Add to the event table (or a small side table) how each rule was issued and how much notice the market
  had, each with its source from `docs/sources.md`.
- [ ] S2 — Figure `results/figures/P3-12_rules.png`: one row per rule, the change in bps, the 95% placebo band,
  the detection limit (~25–37 bps) marked.
- [ ] S3 — Slide text (pt-BR) with the two caveats: content and form differ together, so the chart cannot say
  which mattered; "no effect" means "no effect above the detection limit".

## Success criteria
- [ ] Every row's issuance type has a source
- [ ] Figure uses only numbers from `results/tables/P2-03_event_table.csv`
- [ ] Both caveats on the slide

## Outputs
- `scripts/p3_12_rules.py`, `results/figures/P3-12_rules.png`

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** not started.
- **Next step:** S1
- **Open questions:** none
- **How to resume:** `results/tables/P2-03_event_table.csv`, column `p_placebo_all_clean_2s`.

## Log
- 2026-11-02, agent for Renzo: Renzo takes P3-12 (owner Economist; asked by Renzo). Scope: the 8 rules (E-01 to E-06b); market events (E-07, M-01 to M-04) are not rules and stay out. Band = 2.5–97.5% of the 200 P2-03 placebo draws.
- 2026-11-02, agent for Renzo: created (plan `docs/06-so-what.md`).

## Result
