---
id: P3-05
title: Extension A - protocol, memory test and pilot on the three CLIs
phase: P3
status: doing
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
- [x] S1 — Build `data/agentic_bundle/`: raw USDTBRL, USDCUSDT, PTAX files from P1-01 plus the providers'
  public column documentation; write `SHA256SUMS`. Nothing from `docs/`, `findings/` or processed data. — done: Felipe, 2 Nov
- [x] S2 — Freeze the prompt and the answer schema (from `docs/05`) in `results/agentic/protocol.md`, with
  the models to use, runs per family (~10) and the analysis plan. — done: Felipe, 2 Nov
- [x] S3 — Memory test: in each family's chat app, web search off, ask what happened to Brazilian
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
- [x] S7 — Commit `protocol.md`, the bundle checksums and the harness script **before** P3-06; paste the
  commit hash in Result. — done: Felipe, 2 Nov (`ac8b72e`)

## Success criteria
- [x] Bundle with checksums contains raw files and provider docs only — done: Felipe, 2 Nov
- [ ] Memory-test answers saved verbatim for the three families
- [ ] Isolation test passed (evidence saved) for every CLI used
- [ ] One pilot run per CLI completed end to end, with time and limit notes
- [x] Protocol commit hash recorded here, dated before the first P3-06 run (`ac8b72e`, 2026-11-02)

## Outputs
- `data/agentic_bundle/` (git-ignored, 276 raw files + neutral docs)
- `results/agentic/bundle_SHA256SUMS.txt` (tracked in git)
- `results/agentic/protocol.md` (pre-registered protocol & dispersion plan)
- `results/agentic/memory_test.md` (structured memory test template)
- `results/agentic/isolation_test.md` (CLI isolation verification template)
- `scripts/p3_05_build_bundle.py` (bundle generator)
- `scripts/p3_05_harness.py` (cross-platform CLI runner and schema validator)
- `scripts/p3_05_run_agent.sh` (bash CLI runner)

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** S1 and S2 completed. Frozen bundle built and verified (6.52 MB, 276 files), SHA256 checksums mirrored to `results/agentic/bundle_SHA256SUMS.txt`, protocol pre-registered in `results/agentic/protocol.md`, and test templates + runner harness prepared. Ready for Jonathan and Renzo to run live on Renzo's machine and authenticated accounts.
- **Next step:** S3, S4, S5, S6 (takes ~15 minutes on Renzo's machine):
  1. **S3 (Memory Test — 2 min):** In Claude, ChatGPT, and Gemini chat/CLI (web search toggled OFF), ask:
     `"What changes or regulatory notices occurred regarding Brazilian stablecoins and crypto foreign exchange on 23 June 2026?"`
     Paste the verbatim answers into `results/agentic/memory_test.md`.
  2. **S4 & S5 (Isolation Negative Tests — 3 min):**
     In a throwaway CLI session for each of `claude`, `codex`, and `gemini`, verify that asking to browse the web (`curl -I https://example.com`) and read outside files (`cat ../../STATUS.md`) fail. Paste terminal output into `results/agentic/isolation_test.md`.
  3. **S6 (Pilots — 8 min):** Run 1 test pilot per family using the automated harness:
     ```bash
     # Windows (PowerShell / cmd):
     py scripts/p3_05_harness.py --family claude --run-id pilot-claude
     py scripts/p3_05_harness.py --family codex --run-id pilot-codex
     py scripts/p3_05_harness.py --family gemini --run-id pilot-gemini

     # Linux / macOS / WSL:
     ./scripts/p3_05_run_agent.sh claude pilot-claude
     ./scripts/p3_05_run_agent.sh codex pilot-codex
     ./scripts/p3_05_run_agent.sh gemini pilot-gemini
     ```
     Verify that `results/agentic/runs/pilot-*/answer.json` passes schema validation.
  4. **S7 (Pre-registration Commit — 2 min):**
     Stage and commit the pre-registered protocol and harness before launching the 30 production runs:
     ```bash
     git add results/agentic/ scripts/p3_05_* tasks/P3-05-agentic-A-protocol-pilot.md .gitignore
     git commit -m "P3-05: pre-register agentic protocol, freeze bundle checksums, and add harness"
     ```
     Record the commit hash under `## Result
- **Pre-registered protocol & bundle checksums commit hash:** `ac8b72e` (2026-11-02, committed prior to any P3-06 agent run).
- **Bundle manifest:** `results/agentic/bundle_SHA256SUMS.txt` (276 raw price files + neutral `DATA_README.txt`).
- **Pending on Renzo's CLI machine:** S3 memory test, S4–S5 isolation check, S6 1-run pilot per CLI.` in this file.
- **Open questions:** Verify quota consumption rate on Renzo's entry-level plans during S6 pilot.
- **How to resume:** Follow steps 1–4 above on Renzo's machine.

## Log
- 2026-11-07, Jonathan (CS 3): Executed clean S3 memory tests across Claude (Sonnet 5.5), OpenAI (ChatGPT), and Google (Gemini 3.8 Pro in AI Studio) with web tools disabled. All models returned Unaware/Cutoff. Logged verbatim outputs to results/agentic/memory_test.md. Handing off S4-S6 to CLI environment.
- 2026-11-02 Felipe: Completed S1 and S2. Wrote `scripts/p3_05_build_bundle.py` which populated `data/agentic_bundle/` with 276 raw price files and neutral provider documentation (`DATA_README.txt`), computed SHA256 checksums, and mirrored them to `results/agentic/bundle_SHA256SUMS.txt`. Wrote `results/agentic/protocol.md` pre-registering prompt, schema, isolation rules, and dispersion analysis plan. Built `scripts/p3_05_harness.py` and `scripts/p3_05_run_agent.sh` with schema validation and test harness. Prepared templates `results/agentic/memory_test.md` and `results/agentic/isolation_test.md`. Updated `.gitignore` to explicitly ignore `data/agentic_bundle/`. Ready for live CLI execution by Jonathan/Renzo.

## Result
- **Pre-registered protocol & bundle checksums commit hash:** `ac8b72e` (2026-11-02, committed prior to any P3-06 agent run).
- **Bundle manifest:** `results/agentic/bundle_SHA256SUMS.txt` (276 raw price files + neutral `DATA_README.txt`).
- **Pending on Renzo's CLI machine:** S3 memory test, S4–S5 isolation check, S6 1-run pilot per CLI.
