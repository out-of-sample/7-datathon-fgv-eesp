---
id: P2-06
title: Freeze our 23 Jun before/after estimate in the agents' answer format
phase: P2
status: todo
owner: CS 2
working: -
due: 2026-11-02
depends: P2-03
---

## Goal
Record our own estimate in the same format the AI analysts will use, and commit it **before** anyone opens
an agent result. This keeps extension A honest even if we decide on A later.

## Subtasks
- [ ] S1 — Take the 23 Jun row of P2-03.
- [ ] S2 — Write `results/agentic/team_estimate.json` using the schema in `docs/05-agentic-robustness.md`.
- [ ] S3 — Commit with the message `P2-06: team estimate frozen`; paste the commit hash in the Result section.

## Success criteria
- [ ] JSON file valid against the schema fields
- [ ] Commit hash recorded here, dated before any agent run in P3-06

## Outputs
- `results/agentic/team_estimate.json`

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** not started
- **Next step:** S1
- **Open questions:** none
- **How to resume:** -

## Log

## Result
