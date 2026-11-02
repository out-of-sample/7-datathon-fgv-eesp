---
id: P5-03
title: Red-team review
phase: P5
status: doing
owner: Team
working: Felipe
due: 2026-11-06
depends: P5-01
---

## Goal
Everyone (plus an AI critic agent) attacks the deck as a juror would: rigor, clarity, relevance. Every point is answered or consciously declined.

## Subtasks
- [ ] S1: Run two independent AI critic passes on `deck/deck_v1_ptbr.md` and `deck/annex_v1_ptbr.md` (Pass 1: Econometrician & Central-Bank Policy Juror; Pass 2: Crypto Market-Microstructure & Number/Source Consistency Juror).
- [ ] S2: Consolidate all critiques in `results/review/P5-03_red_team.md`, classifying each point as `fixed` (with immediate patch to deck/annex) or `declined` (with explicit justification).
- [ ] S3: Apply all `fixed` improvements to `deck/deck_v1_ptbr.md` and `deck/annex_v1_ptbr.md`.

## Success criteria
- [ ] Review notes in results/review/P5-03_red_team.md
- [ ] Each point marked fixed / declined with reason

## Outputs
- `results/review/P5-03_red_team.md`

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** `doing` (Felipe running multi-perspective AI red-team review on the 14-slide deck and annex).
- **Next step:** Complete S1–S3 and write `results/review/P5-03_red_team.md`.
- **Open questions:** none
- **How to resume:** See `results/review/P5-03_red_team.md`.

## Log
- 2026-11-02, Felipe: Claimed `P5-03` (`status: doing`, `working: Felipe`) to run parallel red-team critic passes on `deck/deck_v1_ptbr.md` and `deck/annex_v1_ptbr.md`.

## Result
