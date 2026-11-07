---
id: P3-36
title: Investigate the economic function of BRLA mint and burn operations
phase: P3
status: doing
owner: CS 1
working: Renzo (Codex agent)
due: 2026-11-07
depends: P3-29
---

## Goal
Determine what publicly observable mechanism produced the large Celo BRLA burns, and whether public evidence identifies their economic purpose. Authorized by Renzo on 7 Nov 2026 after discussing P3-29. This is a retrospective follow-up; P3-29's independent review remains with another teammate. Originally P3-35 (b161a85); renumbered P3-36 after a concurrent access-method review reused P3-35.

## Subtasks
- [ ] S1 — Freeze the investigation rules and transaction sample before reading new evidence. — doing: Renzo (agent)
- [ ] S2 — Inspect historical execution contracts, full receipts and transaction inputs; compare large burns with routine controls.
- [ ] S3 — Open issuer/protocol documentation and assess competing economic explanations.
- [ ] S4 — Produce reproducible tables, English finding, source register and reviewer handoff.

## Success criteria
- [ ] Every selected case has a verified mechanism or an explicit unresolved classification.
- [ ] Contract execution, address attribution and fiat settlement have separate evidence requirements.
- [ ] All new raw responses are frozen with provenance/checksums and excluded from git.
- [ ] Offline replay and parser self-checks pass; an English finding reports failures and limitations.
- [ ] Another teammate checks the result before presentation use.

## Outputs
- `results/P3-36_protocol.md`
- `scripts/p3_36_brla_operations.py`
- `results/tables/P3-36_*.csv`, `results/P3-36_evidence.md`
- A new exploratory finding and sources in `docs/sources.md`.

## Handoff
- **State:** scope authorized; protocol being registered before new transaction/source inspection.
- **Next step:** S2, inspect the MiniVM proxy active at each of the eight large burns already listed in P3-29.
- **Open questions:** operator identity; operation type; fiat settlement; whether large burns differ from earlier operations.
- **How to resume:** read `results/P3-36_protocol.md`, then P3-29's case audit and frozen raw files.
- **Workspace:** isolated main checkout `/tmp/p3-35-brla-operations`, because concurrent P3-28 changes prevent pulling the shared checkout. Remote read at d281bff; P3-29 S6 is complete there. Existing STATUS conflict markers require Renzo's instruction; question pending.

## Log
- 2026-11-07 — Codex for Renzo: claimed S1–S4 for the user-requested economic-function investigation. No new evidence inspected before protocol registration. No external messages or paid services authorized.

## Result
Pending.
