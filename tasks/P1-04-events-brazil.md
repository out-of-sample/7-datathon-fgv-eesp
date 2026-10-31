---
id: P1-04
title: Verified list of Brazilian rule changes and events
phase: P1
status: todo
owner: Economist
working: -
due: 2026-10-31
depends: -
---

## Goal
A table of every dated rule or event that could change the cost of getting dollars via USDT, each with a
primary source. It feeds the event studies, the break matching, and is the human benchmark for extension B.

## Subtasks
- [ ] S1 — Start from `docs/02-dolar-cripto.md` §6 (event list) and `docs/sources.md` (E-01 to E-06).
- [ ] S2 — For each event, find the primary source (Diário Oficial, BCB normative search, BCB/Fazenda press release).
   Record **announcement date** and **effective date** separately.
- [ ] S3 — Confirm the 23 Jun 2026 notice in a primary or second independent source; otherwise mark it unconfirmed.
- [ ] S4 — Add events you find that are missing (e.g., exchange BRL deposit/withdrawal outages, the 24h-hold rule).
- [ ] S5 — Columns: `event_id, date_announced, date_effective, description, type (tax/restriction/reporting/outage/other),
   channel_affected, source_url, source_type (primary/secondary), verified_by, verified_on`.

## Success criteria
- [ ] `data/processed/P1-04_events_brazil.csv` exists; every row has a source URL
- [ ] 23 Jun 2026 status: confirmed or unconfirmed, with the evidence
- [ ] `docs/sources.md` statuses updated

## Outputs
- `data/processed/P1-04_events_brazil.csv`, updated `docs/sources.md`

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** not started
- **Next step:** S1
- **Open questions:** none
- **How to resume:** -

## Log

## Result
