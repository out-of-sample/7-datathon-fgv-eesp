---
id: P5-03
title: Red-team review
phase: P5
status: review
owner: Team
working: -
due: 2026-11-06
depends: P5-01
---

## Goal
Everyone (plus an AI critic agent) attacks the deck as a juror would: rigor, clarity, relevance. Every point is answered or consciously declined.

## Subtasks
- [x] S1: Run two independent AI critic passes on `deck/deck_v1_ptbr.md` and `deck/annex_v1_ptbr.md` (Pass 1: Econometrician & Central-Bank Policy Juror; Pass 2: Crypto Market-Microstructure & Number/Source Consistency Juror).
- [x] S2: Consolidate all critiques in `results/review/P5-03_red_team.md`, classifying each point as `fixed` (with immediate patch to deck/annex) or `declined` (with explicit justification).
- [x] S3: Apply all `fixed` improvements to `deck/deck_v1_ptbr.md` and `deck/annex_v1_ptbr.md`.

## Success criteria
- [x] Review notes in results/review/P5-03_red_team.md
- [x] Each point marked fixed / declined with reason

## Outputs
- `results/review/P5-03_red_team.md`

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** `review` (32 red-team critiques reviewed: 29 fixed immediately in deck & annex, 3 declined with explicit justification in `results/review/P5-03_red_team.md`).
- **Next step:** Team review and final sign-off before presentation freeze.
- **Open questions:** Option C vs Option A on Slide 10 / Annex B.5 (kept both open for team decision).
- **How to resume:** Read `results/review/P5-03_red_team.md` and check `deck/deck_v1_ptbr.md`.

## Log
- 2026-11-02, Felipe: Completed multi-perspective red-team audit across econometrics, BCB policy, crypto microstructure, and number/source traceability. Consolidated all 32 items in `results/review/P5-03_red_team.md`, patched Band-TAR parameters in Annex B.6, clarified VIP maker vs taker in Slide 10, updated commit hashes, harmonized figures, and moved status to `review`.

## Result
