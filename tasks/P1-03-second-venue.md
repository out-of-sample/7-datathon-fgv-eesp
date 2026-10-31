---
id: P1-03
title: Find and download a second BRL venue for USDT
phase: P1
status: todo
owner: CS 2
working: -
due: 2026-10-31
depends: -
---

## Goal
Check that the premium (and the 24 Jun 2026 jump) is not a Binance-only artefact by getting USDT/BRL prices
from a second exchange.

## Subtasks
- [ ] S1 — Look for public historical USDT/BRL data (Mercado Bitcoin, Foxbit, or another Brazilian venue); hourly if
   possible, daily at minimum, covering at least 1 Jan - 30 Sep 2026.
- [ ] S2 — Record the endpoint, limits and terms in `docs/sources.md` (row D-04).
- [ ] S3 — Download to `data/raw/<venue>/` and add checksums and a manifest row.

## Success criteria
- [ ] A second venue with coverage of Jan-Sep 2026, or a written explanation of why none is available
- [ ] Source row D-04 updated to checked

## Outputs
- `scripts/p1_03_second_venue.py`, `data/raw/<venue>/`

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** not started
- **Next step:** S1
- **Open questions:** none
- **How to resume:** -

## Log

## Result
