---
id: P1-08
title: Decide the API budget and models for extension A
phase: P1
status: done
owner: Team
working: -
due: 2026-11-01
depends: -
---

## Goal
Decide how we pay for ~30 AI-agent runs (extension A), with which model families, and whose accounts run
them. Without this decision, A cannot start.

## Subtasks
- [x] S1 — Choose the funding and the model families — done: Renzo, 31 Oct
- [x] S2 — Decide whose accounts run the agents; no credentials in the repo — done: Renzo, 31 Oct
- [x] S3 — Record the decision in `docs/README.md` (decision log) — done: agent for Renzo, 31 Oct

## Success criteria
- [x] Decision logged before the Sun 1 Nov gate (yes with ceiling and models, or no)

## Outputs
- Decision log entry (31 Oct)

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** closed
- **Next step:** -
- **Open questions:** none
- **How to resume:** -

## Log
- 2026-10-31 — agent for Renzo: decision recorded; consequences written into P3-05 and `docs/05-agentic-robustness.md`
- 2026-10-31 — Renzo: use the existing Claude, ChatGPT and Gemini plans

## Result
**No API spend.** Extension A runs on Renzo's existing entry-level paid plans for Claude, ChatGPT and Gemini,
through each plan's coding agent in the terminal (Claude Code, Codex CLI, Gemini CLI): three model families,
about 10 runs each. Consequences:
- Runs execute on Renzo's accounts and machine; Jonathan (CS 3) prepares, Renzo launches or lends the session.
- Usage limits, not money, cap the number of runs. Report the number actually completed per family.
- Claude runs share limits with Renzo's development work: schedule them outside working hours.
- Each CLI's isolation (no web tools, no personal instructions or memory) must be set up and tested (P3-05).
- Whether each plan includes its CLI at the needed volume is `[verify]` in the P3-05 pilot.
