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
- **Assigned (5 Nov, Renzo):** Nattan or Jonathan, whoever takes it first (claim it: `working: <name>`).
- **Scope changed (5 Nov, Renzo, decision log):** the submission is the **GitHub link + the 10-slide PDF**; no `.txt`
  scripts go to the jury. The repo itself is the code deliverable, so the job is now: a juror who opens the repo can find
  and re-run the script behind every deck/annex number.
- **State:** 18 exports + clean replay pass (review 5 Nov 01:25, two gaps in Log). `submission/scripts/*.txt` can stay as
  a convenience or be removed; not required.
- **Next step:** (1) in `submission/README.md` (or the repo README), map each deck/annex claim to its `scripts/*.py`,
  including the annex scripts `p3_04_depeg_chapter`, `p3_07_tar`, `p3_08_subsidy`, `p3_14_press_check` and the download
  scripts `p1_01_download`, `p1_03_second_venue` as the documented first step; add `p3_24_brla` / `p3_25_composition`
  only if Felipe puts F-037 / F-036 in the PDF; (2) after Felipe picks v1/v2 and P5-02 lands, re-run
  `scripts/p5_04_reproduce.py` and check the final PDF figures against it; (3) mark done.
- **How to resume:** `.venv/bin/python scripts/p5_04_export.py` then `.venv/bin/python scripts/p5_04_reproduce.py` (~2 min).

## Log
- 2026-11-05 01:55 (Brasília), agent for Renzo: Renzo assigned the rest to Nattan or Jonathan; submission format is GitHub link + 10-slide PDF, no `.txt` scripts to the jury; Handoff rewritten.
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
