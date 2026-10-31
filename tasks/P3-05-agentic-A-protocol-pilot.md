---
id: P3-05
title: Extension A - protocol, memory test and pilot on the three CLIs
phase: P3
status: todo
owner: CS 3
working: -
due: 2026-11-02
depends: P1-01, P1-08
---

## Goal
Prepare the 30-AI-analysts test so it is credible: a frozen data bundle, the final prompt, a memory test,
three isolated agent setups (Claude Code, Codex CLI, Gemini CLI on Renzo's plans) and a pilot run per CLI.
Starts Sun 1 Nov if the gate says go. Plan: `docs/05-agentic-robustness.md` §A.

## Subtasks
- [ ] S1 — Build `data/agentic_bundle/`: raw USDTBRL, USDCUSDT, PTAX files from P1-01 plus the providers'
  public column documentation; write `SHA256SUMS`. Nothing from `docs/`, `findings/` or processed data.
- [ ] S2 — Freeze the prompt and the answer schema (from `docs/05`) in `results/agentic/protocol.md`, with
  the models to use, runs per family (~10) and the analysis plan.
- [ ] S3 — Memory test: in each family's chat app, web search off, ask what happened to Brazilian
  stablecoin regulation on 23 Jun 2026. Save the answers verbatim in `results/agentic/memory_test.md`.
- [ ] S4 — Isolation setup per CLI (on Renzo's machine and accounts): fresh empty folder per run containing
  only the bundle; agent web tools disabled; network blocked for the agent's shell where the CLI allows it;
  no personal instructions or memory files loaded (e.g., Renzo's global `~/.claude/CLAUDE.md`,
  `~/.codex/AGENTS.md`, `~/.gemini/GEMINI.md`); model pinned and recorded. Exact flags/settings per CLI are
  `[verify]`: write what you used in `protocol.md`. Note: the CLI itself must still reach its own model
  service; "no internet" means no web access for the agent.
- [ ] S5 — Isolation test per CLI in a throwaway session: ask the agent to open a web page and to read a file
  outside its folder. Both must fail. Record the evidence.
- [ ] S6 — Pilot: one full run per CLI end to end; record time, whether the usage limit was hit, and any
  harness fixes.
- [ ] S7 — Commit `protocol.md`, the bundle checksums and the harness script **before** P3-06; paste the
  commit hash in Result.

## Success criteria
- [ ] Bundle with checksums contains raw files and provider docs only
- [ ] Memory-test answers saved verbatim for the three families
- [ ] Isolation test passed (evidence saved) for every CLI used
- [ ] One pilot run per CLI completed end to end, with time and limit notes
- [ ] Protocol commit hash recorded here, dated before the first P3-06 run

## Outputs
- `data/agentic_bundle/` (git-ignored), `results/agentic/protocol.md`, `results/agentic/memory_test.md`,
  `results/agentic/isolation_test.md`, harness script `scripts/p3_05_run_agent.sh`

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** not started
- **Next step:** S1 (after the Sun 1 Nov gate says go)
- **Open questions:** none
- **How to resume:** -

## Log

## Result
