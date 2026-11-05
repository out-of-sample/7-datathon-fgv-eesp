---
id: P5-04
title: Export scripts as .txt with headers
phase: P5
status: doing
owner: CS 1
working: Codex for Renzo
due: 2026-11-07
depends: P4-03
---

## Goal
Prepare the code deliverable: each script as .txt with purpose, inputs, outputs and how to run, re-running from raw data to the figures.

## Subtasks
- [ ] S1: Inventory the figures and quantitative claims in the selected deck, trace each to its source script, and record the required execution order. — doing: Codex for Renzo, 2026-11-05
- [ ] S2: Export the required analysis scripts to `submission/scripts/*.txt`, each with purpose, inputs, outputs, and an exact run command.
- [ ] S3: Re-run the exported scripts from the frozen raw data and check that the deck figures are reproduced.
- [ ] S4: Record the contents, remaining limitations, and exact review steps for an independent Claude agent.

## Success criteria
- [ ] Every script used by the deck exported to submission/scripts/*.txt
- [ ] Clean re-run from raw data reproduces the figures

## Outputs
- `submission/scripts/`

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** claimed by Codex for Renzo; S1 in progress.
- **Next step:** trace the selected deck's figure references and quantitative claims to scripts.
- **Open questions:** Felipe has not yet selected deck v1 or v2; export the common figure pipeline first and reconcile any final difference before review.
- **How to resume:** inspect `deck/deck_v1_ptbr.md`, `deck/deck_v2_ptbr.md`, and the script references in their findings.

## Log
- 2026-11-05, Renzo + Codex: Renzo assigned P5-04 to Codex; owner moved from CS 2 to CS 1, four subtasks written and shown before execution.

## Result
