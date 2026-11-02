---
id: P3-09
title: Open sources for the depeg case causes (restore them in the case table)
phase: P3
status: doing
owner: Economist
working: Felipe
due: 2026-11-04
depends: P3-04
---

## Goal
The P3-04 review marked every cause in the 11-case depeg table as unsourced. Find an opened, quoted source for each
cause (and for the USDP end-of-data on Binance), so the deck can say why each stablecoin left $1 without guessing.

## Subtasks
- [ ] S1 — Open and quote a source for each case cause, starting with FDUSD Apr 2025, TUSD Jan 2024, UST May 2022, and the USDP delisting — doing: Felipe
- [ ] S2 — Restore the sourced causes in esults/tables/P3-04_depeg_case_table.csv (via scripts/p3_04_depeg_chapter.py) and add the sources to docs/sources.md; leave "Causa não verificada" where nothing was found

## Success criteria
- [ ] Every cause in the case table is either sourced (opened, one line quoted) or marked "não verificada"
- [ ] F-019 History notes what changed

## Outputs
- esults/tables/P3-04_depeg_case_table.csv, docs/sources.md

## Handoff
- **State:** created; S1 running
- **Next step:** S1
- **Open questions:** -
- **How to resume:** python scripts/p3_04_depeg_chapter.py; see the P3-04 Handoff

## Log
- 2026-11-02, agent for Felipe: created from the P3-04 review's open item; Felipe takes it.

## Result