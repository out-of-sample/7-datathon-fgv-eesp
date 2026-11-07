---
id: P3-44
title: Complete a separately versioned AI-reviewed access comparison
phase: P3
status: doing
owner: CS 1
working: Codex for Felipe
due: 2026-11-08
depends: P3-28, P3-43
---

## Goal
Finish the access-document comparison under Felipe's explicit 7 Nov authorization to use separate AI reference coders, adjudication and evidence audit instead of the unavailable human reviewers. This is an exploratory AI-reviewed pilot, not human validation or operational access certification.

## Subtasks
- [x] S1 — Attempt original restoration; collect separate immutable sources and verify a replacement runner — done: Codex, 7 Nov. Old runs/Claude runner unavailable; 31 registered sources recovered, browser PDFs in progress.
- [ ] S2 — Freeze protocol, corpus and full run schedule before labels or model results.
- [ ] S3 — Obtain two independent source-only AI references and separate adjudication; run every comparison method under the same replacement runtime.
- [ ] S4 — Audit anonymized emitted claims, score all scheduled runs, preserve failures and report comparisons/limits.
- [ ] S5 — Independent agent checks scorer/results; update board, commit and push; leave new work in review.

## Success criteria
- [ ] Frozen corpus/config/run identities and reviewer provenance reproduce.
- [ ] Every case/question is referenced; every emitted claim is audited, including notes and duplicates.
- [ ] No mixing of historical Claude results and replacement-runner scores.
- [ ] Paired methods, provider results, failures, resource use and disagreement are reported; unknown costs remain unknown.
- [ ] Claims remain exploratory and explicitly AI-reviewed; new work is ready for further agent review.

## Outputs
- `scripts/p3_44_collect.py`, `scripts/p3_44_access_pilot.py`
- `results/P3-44_protocol.md`, `results/tables/P3-44_*.csv`
- Immutable source/run/reviewer records in ignored `data/raw/p3_28_v2/`.
- A new exploratory finding and a short plain-language result summary.

## Handoff
- **State:** implementation in progress; no replacement experiment result yet. Existing P3-28 outputs remain historical.
- **Next step:** finish/validate manual PDFs, freeze corpus and protocol, then label and run without inspecting answers to tune methods.
- **Open questions:** missing manual pages, model metadata and resource equivalence are explicit limitations.
- **How to resume:** use Python 3.14 at `C:/Users/Felipe/AppData/Local/Programs/Python/Python314/python.exe`; run collector freeze then adapter prepare only when sources are final.

## Log
- 2026-11-07 — Felipe explicitly approved full implementation, separate AI reviewers, status cleanup, commit and push. Original two-human-coder/one-human-auditor requirement is replaced for this version only; no human sign-off is invented. Economist-owned statuses stay unchanged.

## Result
Pending.
