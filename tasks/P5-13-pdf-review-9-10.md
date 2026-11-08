---
id: P5-13
title: Review current PDF and propose source-backed graphics for slides 9 and 10
phase: P5
status: review
owner: Economist
working: -
due: 2026-11-08
depends: P5-10, P5-12
---

## Goal
Review Felipe's current Downloads/Datathon FGV 2026.pdf. Preserve slides 1–8 apart from wording suggestions; recommend feasible charts for 9–10 using available data. Follow-up explicitly authorizes the four recommended chart assets; PDF remains unchanged.

## Subtasks
- [x] S1 — Extract all ten pages and visually inspect relevant layouts — done: Codex for Felipe, 8 Nov
- [x] S2 — Confirm available inputs for monitor and conclusion graphics — done: Codex for Felipe, 8 Nov
- [x] S3 — Recommend placements, chart forms and material wording fixes — done: Codex for Felipe, 8 Nov
- [x] S4 — Build CUSUM and three conclusion charts, inspect exports and retain chart data — done: Codex for Felipe, 8 Nov

## Success criteria
- [x] Proposed charts have existing inputs; no new dataset or model needed.
- [x] No edit to supplied PDF; earlier slides receive wording suggestions only.

## Handoff
- **State:** PDF reviewed and all four subsequently authorized chart assets built as transparent PNG/SVG: P5-13_09_cusum, 10a_premio, 10b_rede, 10c_foxbit. Individual and small-size composite renders inspected; F-058 records source/limits. Current PDF unchanged.
- **Next step:** Felipe inserts the CUSUM between the compacted workflow and prediction cards on 9, and the three mini charts under corresponding conclusion paragraphs on 10. Retain existing slide source footers.
- **Open questions:** Chart 10 can be three mini bar charts or just one cost comparison; avoid adding a new experimental result at the conclusion. Existing push rejection remains unresolved; no push attempted.
- **How to resume:** Source PDF `C:/Users/Felipe/Downloads/Datathon FGV 2026.pdf`; monitor input `data/processed/P3-03_monitor_daily.csv`; route costs `results/tables/P3-01_route_costs.csv`; venue shares `results/tables/P3-25_composition.csv`; prediction table `results/tables/P3-20_readout.csv`, reference bands `P3-20_reference.csv`.

## Review notes
- Slide 9: compact five-step row at top, one wide central plot of upward CUSUM through 24 June against its threshold; preserve preregistered prediction cards below. A detector observes the jump; it does not predict it. Frozen F-014 says simple baseline also detected June 24, with more other alarms; do not claim unique same-day detection.
- Slide 10: keep the three conclusion columns; shorten text and put two-value mini summaries at the bottom: pre vs acute premium (F-016), extra premium vs network fee in consistent bps (F-015, network fee assumption), before vs after Foxbit share of the three observed venues (F-036, exploratory). Repetition here is synthesis, not new evidence. This does not identify which aspect of the sole treated notice caused the change.
- Phrase fixes: slide 2 qualify the largest-change claim as the structural-break model; red band through August is the trailing MA20 recovery, not the frozen acute window. Slide 3 distinguish closing one arbitrage route from stopping all arbitrage, and define bp in percentage points. Slide 4 replace "who supplied" and "deviation is the effect" with supported wording. Slide 5 say among five comparators and tested explanations. Slide 7 say premium receded and Foxbit share within three observed venues. Slide 8 outcomes are per decision date, not daily yield; R2 requires premium >60-day median +5 bps. Slide 9 null means no detectable unusual move, not proof of zero; S2 and S1 prediction readouts have different horizons. Slide 10 avoid asserting lack of advance notice independently explains the effect.

## Log
- 2026-11-08 — Codex for Felipe: follow-up authorized construction. Four chart pairs generated, checked and inspected; font glyph and title-clipping defects corrected; F-058 created. No push attempted because earlier publication authorization remains pending.
- 2026-11-08 — Codex for Felipe: review completed, candidate source files inspected; suggestions delivered in chat. No artifact edited or new numerical result estimated.

## Result
Review and authorized chart construction completed; final assets ready for Felipe to insert. No PDF edit performed.
