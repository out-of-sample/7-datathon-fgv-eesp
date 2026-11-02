---
id: P2-06
title: Freeze our 23 Jun before/after estimate in the agents' answer format
phase: P2
status: review
owner: CS 2
working: -
due: 2026-11-02
depends: P2-03
---

## Goal
Record our own estimate in the same format the AI analysts will use, and commit it **before** anyone opens
an agent result. This keeps extension A honest even if we decide on A later.

## Subtasks
- [x] S1 — Take the 23 Jun row of P2-03. — done: Felipe, 2 Nov
- [x] S2 — Write `results/agentic/team_estimate.json` using the schema in `docs/05-agentic-robustness.md`. — done: Felipe, 2 Nov
- [x] S3 — Commit with the message `P2-06: team estimate frozen`; paste the commit hash in the Result section. — done: Felipe, 2 Nov (`80fc866`)

## Success criteria
- [x] JSON file valid against the schema fields (`results/agentic/team_estimate.json`)
- [x] Commit hash recorded here, dated before any agent run in P3-06 (`80fc866`, 2026-11-02)

## Outputs
- `results/agentic/team_estimate.json`

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** S1–S3 completed (`status: review`). `results/agentic/team_estimate.json` generated, validated against schema, and frozen in commit `80fc866`.
- **Next step:** Teammate verification (`status -> done`) and comparison in P3-06 if Extension A runs.
- **Open questions:** none
- **How to resume:** `git show 80fc866` or inspect `results/agentic/team_estimate.json`.

## Log
- 2026-11-02, Felipe: S1–S3 completed via `scripts/p2_03_events.py`. `results/agentic/team_estimate.json` written with estimate_bps = 93.9, std_error_bps = 16.2 (Newey-West HAC), committed in `80fc866`. Status -> review.

## Result
Frozen team estimate in `results/agentic/team_estimate.json`:
- `run_id`: "team_estimate"
- `model`: "team_out_of_sample"
- `direction`: "up"
- `estimate_bps`: 93.9
- `std_error_bps`: 16.2
- `estimator`: "difference in means (OLS with Newey-West HAC Bartlett kernel, maxlags=5)"
- `windows`: 20 days pre (15.2 bps), 20 days post (109.1 bps)
- `commit_hash`: `80fc866` (2026-11-02)
