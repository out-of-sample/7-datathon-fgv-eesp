---
id: P4-02
title: Independent re-run of every headline number
phase: P4
status: doing
owner: CS 3
working: Felipe
due: 2026-11-04
depends: P4-01
---

## Goal
A teammate who did not produce a number re-runs its script from raw data and confirms the output.

## Subtasks
- [ ] S1: Audit code correctness and independently re-run Renzo-authored scripts (`p0_probe_dolar_cripto.py`, `p1_02_premium_v2.py`, `p1_03_second_venue.py`, `p1_05_donors.py`, `p2_02_breaks.py`) from raw data, verifying `F-001`–`F-004`, `F-006`, `F-008`, `F-010`, and `F-011`.
- [ ] S2: Verify and synchronize finding headers (`status: confirmed`, `checked_by: Renzo`) for tasks already peer-reviewed and closed (`done`) by Renzo (`P2-03` / `F-016`, `P2-04` / `F-017`, `P3-02` / `F-018`, `P4-01` / `F-022`), plus re-verify their exact reproduction from raw data.
- [ ] S3: Write a complete cross-verification ledger in `results/review/P4-02_recheck.md` mapping every headline number in `deck/deck_v1_ptbr.md` to its script, producer, independent checker, and exact output.

## Success criteria
- [ ] Every finding used in the deck marked checked-by with the re-runner's name
- [ ] Mismatches resolved or disclosed

## Outputs
- `results/review/P4-02_recheck.md`
- updates in each finding file

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** `doing` (Felipe running independent code & execution re-check across all unconfirmed findings used in the deck).
- **Next step:** Complete S1–S3 and update finding headers.
- **Open questions:** none
- **How to resume:** See `results/review/P4-02_recheck.md`.

## Log
- 2026-11-02, Felipe: Claimed `P4-02` (`status: doing`, `working: Felipe`) to run independent code + execution re-checks on all Renzo-authored findings (`F-001`–`F-004`, `F-006`, `F-008`, `F-010`, `F-011`) and synchronize findings from tasks already reviewed/closed by Renzo (`F-016`, `F-017`, `F-018`, `F-022`).

## Result
