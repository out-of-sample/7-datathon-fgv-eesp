---
id: P1-06
title: Extension B - AI event coder for the comparison currencies
phase: P1
status: todo
owner: CS 3
working: -
due: 2026-11-01
depends: P1-04
---

## Goal
Use an AI agent with web search to list rule changes in each comparison country, check it against human
coding, and remove contaminated countries from the synthetic control. Plan: `docs/05-agentic-robustness.md` §B.

## Subtasks
- [ ] S1 — Write the agent prompt (countries, window 1 Nov 2025 - 30 Sep 2026, output columns as in P1-04). Save it
   in `data/raw/agentic_B/prompt.md` with the model name and date.
- [ ] S2 — Run the agent; save its raw output unchanged in `data/raw/agentic_B/`.
- [ ] S3 — Human check: open every source the agent gives for events between 1 Jun and 31 Jul 2026; mark real /
   wrong date / not supported.
- [ ] S4 — Accuracy: precision and recall against the P1-04 Brazil list and two comparison countries coded by hand
   by a teammate; Cohen's kappa on the event type.
- [ ] S5 — Propose donor exclusions with reasons.
- [ ] S6 — If not finished by the Sun 1 Nov gate: a human screens the donors manually and we say so.

## Success criteria
- [ ] Every event used has a human-checked source
- [ ] `results/tables/P1-06_coder_accuracy.csv` (precision, recall, kappa, counts)
- [ ] Donor exclusion list with reasons in the Result section
- [ ] Any paid tool used was approved (decision log)

## Outputs
- `data/raw/agentic_B/`, `data/processed/P1-06_events_donors.csv`, `results/tables/P1-06_coder_accuracy.csv`

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** not started
- **Next step:** S1
- **Open questions:** none
- **How to resume:** -

## Log

## Result
