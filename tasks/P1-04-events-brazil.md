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
- 2026-10-31, agent for Renzo (note from P3-03): the premium rises modestly from late May 2026 (weekly 10–22 bps vs 5.8 in Jan–Apr) before the 24 Jun jump. Anything in May–Jun 2026? (F-014)
- 2026-10-31, agent for Renzo (note from P2-02): the blind break test (F-011) finds breaks on 26 Jul 2021, 20 Aug 2024, 8 Jul 2025, 24 Jun 2026 and 22 Jul 2026 (95% CIs in P2-02 Result). Please look especially for anything around **15–29 Jul 2026**, when the June spike faded (BCB clarification, bank or fund response, market adaptation?), and around Jul–Aug 2021 and Apr–Dec 2024. P2-02 S3 waits for `data/processed/P1-04_events_brazil.csv`.
- 2026-10-31, agent for Renzo (note from P2-05, not working here): candidate non-regulatory events found while
  ruling out causes: Binance BRL Pix suspension 17 Jun – Jul 2022 (E-07, `[verify]` dates) and Binance's USDT/BRL tick
  cut on ~27 Jun 2025 (F-007). Your call whether they go in the event list.

## Result
