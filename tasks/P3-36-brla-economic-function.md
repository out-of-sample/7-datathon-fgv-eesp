---
id: P3-36
title: Investigate the economic function of BRLA mint and burn operations
phase: P3
status: review
owner: CS 1
working: -
due: 2026-11-07
depends: P3-29
---

## Goal
Determine what publicly observable mechanism produced the large Celo BRLA burns, and whether public evidence identifies their economic purpose. Authorized by Renzo on 7 Nov 2026 after discussing P3-29. This is a retrospective follow-up; P3-29's independent review remains with another teammate. Originally P3-35 (b161a85); renumbered P3-36 after a concurrent access-method review reused P3-35.

## Subtasks
- [x] S1 — Freeze the investigation rules and transaction sample before reading new evidence. — done: Renzo (agent), 2026-11-07
- [x] S2 — Inspect historical execution contracts, full receipts and transaction inputs; compare large burns with routine controls. — done: Renzo (agent), 2026-11-07
- [x] S3 — Open issuer/protocol documentation and assess competing economic explanations. — done: Renzo (agent), 2026-11-07
- [x] S4 — Produce reproducible tables, English finding, source register and reviewer handoff. — done: Renzo (agent), 2026-11-07

## Success criteria
- [x] Every selected case has a verified mechanism or an explicit unresolved classification.
- [x] Contract execution, address attribution and fiat settlement have separate evidence requirements.
- [x] All new raw responses are frozen with provenance/checksums and excluded from git.
- [x] Offline replay and parser self-checks pass; an English finding reports failures and limitations.
- [ ] Another teammate checks the result before presentation use.

## Outputs
- `results/P3-36_protocol.md`
- `scripts/p3_36_brla_operations.py`
- `results/tables/P3-36_*.csv`, `findings/F-047-brla-operator-routing.md`
- A new exploratory finding and sources in `docs/sources.md`.

## Handoff
- **State:** S1–S4 complete; 32/32 mechanisms verified, 0/32 economic purposes identified. F-047 remains exploratory; independent reproduction and economist review pending.
- **Next step:** another teammate obtains both raw bundles (see `data/README.md`), runs `python3 scripts/p3_36_brla_operations.py --offline` and `python3 scripts/p3_36_brla_operations.py --documents --offline`, and checks F-047 against the tables and source snapshots. Record reviewer and verdict before presentation use; P3-29 S7 remains separate.
- **Open questions:** legal account/operator identities and exact ticket/settlement purpose. A voluntarily supplied redacted hash-to-ticket/settlement mapping is needed; no issuer contact or private API access was attempted.
- **Scope:** no deck edits or causal conclusion. The eight large burns use a routine also observed before the notice; that does not explain their economic size.
- **Coordination:** initial ID P3-35 was renamed P3-36 in de4fbc5. Renzo explicitly authorized main-branch pushes for this investigation. Existing unrelated STATUS conflict markers are preserved pending the requested instruction.

## Log
- 2026-11-07 — Coordination: this BRLA investigation is P3-36, published in de4fbc5. The independent access-method review may retain P3-35; please do not also rename that review P3-36.
- 2026-11-07 — Codex for Renzo: claimed S1–S4 for the user-requested economic-function investigation. No new evidence inspected before protocol registration. No external messages or paid services authorized.

## Result
See F-047: eight large burns (335,396,065.575129 BRLA) all transfer from e3a2… to bd22… then burn in the same transaction. The intermediate account has zero net change. Controls show the same route and its mint counterpart; current documentation allows multiple economic purposes. Public evidence does not identify completed fiat redemption, cross-chain migration or a regulatory cause.
