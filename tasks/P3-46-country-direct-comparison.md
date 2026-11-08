---
id: P3-46
title: Direct country comparison of dollar exchange rates and USDT premiums
phase: P3
status: review
owner: Team
working: -
due: 2026-11-08
depends: P1-05, P2-04
---

## Goal
Answer Renzo's question directly: did the dollar exchange rate and the USDT premium move in the same way in the five comparison currencies around 23 June 2026? Report each country separately, without synthetic weights, and add Argentina as a clearly excluded illustration.

## Subtasks
- [x] S1 — Reuse frozen official FX and premium series; fix the same calendar windows as the Brazilian headline. — done: Codex for Renzo, 8 Nov
- [x] S2 — Calculate before/after changes in local currency per USD and premium basis points for each country. — done: Codex for Renzo, 8 Nov
- [x] S3 — Record the limits and a reproducible table. — done: Codex for Renzo, 8 Nov
- [x] S4 — Add Argentina as an illustrative case outside the clean control group. — done: Codex for Renzo, 8 Nov

## Success criteria
- [x] Each country appears separately, with observation counts and units.
- [x] Brazilian premium change reproduces F-016's +93.9 bps after rounding.
- [x] No causal claim or statistical significance claim is attached to this descriptive check.

## Outputs
- `scripts/p3_46_country_direct_comparison.py`
- `results/tables/P3-46_country_direct_comparison.csv`
- `findings/F-053-country-direct-comparison.md`

## Handoff
- **State:** Direct descriptive comparison completed, including Argentina as an excluded illustrative case; new finding is exploratory and not adopted into the deck.
- **Next step:** A teammate may independently review the series alignment and decide whether its simpler presentation should replace the synthetic-control panel.
- **Open questions:** The Colombian TRM dating remains marked `[verify]` in P1-05. Deck inclusion belongs to the team.
- **How to resume:** `.venv/bin/python scripts/p3_46_country_direct_comparison.py`; read the output CSV and F-053.

## Log
- 2026-11-08 — Codex for Renzo: added Argentina on Renzo's request; retained its exclusion from the control group.
- 2026-11-08 — Codex for Renzo: calculated direct official-FX and premium changes around the event using frozen data; submitted for review.

## Result
All five donor currencies had a far smaller change in their USDT premium than Brazil in the fixed calendar windows. Argentina's premium also rose, but it is an illustrative case excluded from the control group because of capital controls and its own June rule change. Official USD exchange rates moved differently, showing why a raw dollar-price comparison alone does not answer the premium question. See F-053.
