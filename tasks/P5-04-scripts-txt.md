---
id: P5-04
title: Export scripts as .txt with headers
phase: P5
status: review
owner: CS 1
working: -
due: 2026-11-07
depends: P4-03
---

## Goal
Prepare the code deliverable: each script as .txt with purpose, inputs, outputs and how to run, re-running from raw data to the figures.

## Subtasks
- [x] S1: Inventory the figures and quantitative claims in both current deck drafts, trace each to its source script, and record the required execution order. — done: Codex for Renzo, 2026-11-05
- [x] S2: Export the required analysis scripts to `submission/scripts/*.txt`, each with purpose, inputs, outputs, and an exact run command. — done: Codex for Renzo, 2026-11-05
- [x] S3: Re-run the exported scripts from the frozen raw data and check that the deck figures are reproduced. — done: Codex for Renzo, 2026-11-05
- [x] S4: Record the contents, remaining limitations, and exact review steps for an independent Claude agent. — done: Codex for Renzo, 2026-11-05

## Success criteria
- [x] Every script used by the two current deck drafts exported to `submission/scripts/*.txt` (18 files; reconcile after Felipe chooses the final draft and P5-02 finishes its new figures)
- [x] Clean re-run from copied frozen raw data reproduces all six existing deck figures pixel for pixel

## Outputs
- `submission/scripts/` (18 executable `.txt` exports), `submission/README.md` (run order and figure/claim map), `submission/reproduction.json` (19 commands passed, six charts exact), `docs/agent-prompt-P5-04-review.md` (independent Claude handoff)
- `scripts/p5_04_export.py`, `scripts/p5_04_reproduce.py`

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** implementation complete and ready for independent Claude review. The 18 exports cover both existing 10-slide drafts; an isolated run of 19 commands passed. Six existing deck charts match pixel for pixel. Frozen P2-03 placebo and P3-11 money tables match byte for byte.
- **Next step:** send `docs/agent-prompt-P5-04-review.md` to Renzo's Claude agent. After Felipe selects the final deck and P5-02 adds or replaces figures, reconcile the PDF against `submission/README.md`, add any new scripts, then mark P5-04 done.
- **Open questions:** v1 vs v2 is still Felipe's choice. P5-02's planned visuals are not present. P3-20 E2's observation window is not complete. The checked-in P2-03 event table has an older E-05 description; current event codes and numbers reproduce within float rounding.
- **How to resume:** run `.venv/bin/python scripts/p5_04_export.py` after any source-script change; then `.venv/bin/python scripts/p5_04_reproduce.py` (about 2 minutes), inspect `submission/reproduction.json`, and compare final PDF figures/claims to `submission/README.md`.

## Log
- 2026-11-05 01:25 (Brasília), agent for Renzo (Claude, independent review per `docs/agent-prompt-P5-04-review.md`): **passes
  for what it covers, with two gaps.** Checked: export script changes only ROOT, the monitor lookup and whitespace; all 18
  header SHA-256 match the current `scripts/*.py`; `reproduction.json` shows 19 commands exit 0 and six figures with pixel
  difference 0; the P2-03 weekday-order fix reproduces `P2-03_placebo_draws.csv` byte for byte under PYTHONHASHSEED 0, 1, 7
  and 42 (the bug was real: datetime hashes are seeded per process); F-016 and F-025 disclose it as a bug fix, numbers
  unchanged. **Gap 1:** the annex (`deck/annex_v1_ptbr.md`) names four scripts not exported: `p3_04_depeg_chapter`
  (F-019), `p3_07_tar` (F-021), `p3_08_subsidy` (F-020), `p3_14_press_check` (F-023); if the annex goes into the PDF
  they must be exported (and `p1_07_depeg_v2` behind F-013/F-019 checked). **Gap 2:** no data-download script is
  exported (`p1_01_download`, `p1_03_second_venue`; P3-20's `download` mode is in its export but omitted from the run), so
  a juror cannot rebuild `data/raw/`; export them as a documented first step even though the reproduction check copies
  frozen files. Also new since: `p3_24_brla` (F-037) and `p3_25_composition` (F-036) if their lines reach the PDF.
- 2026-11-05, Codex for Renzo: P5-04 → review. Exported 18 scripts for both deck drafts. A clean temporary re-run passed 19 commands; all six existing deck figures match pixel for pixel. Found and fixed P2-03's variable weekday draw order, preserving frozen placebo and money tables. Claude review brief prepared; final-deck reconciliation remains for the reviewer/team.
- 2026-11-05, Renzo + Codex: Renzo assigned P5-04 to Codex; owner moved from CS 2 to CS 1, four subtasks written and shown before execution.

## Result
The required `.txt` exports are ready for the current deck drafts and reproducible from copied frozen raw data plus the manually curated P1-04 event table. The final PDF must be checked against the manifest after deck selection and P5-02's figure work.
