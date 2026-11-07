# Review of items awaiting review from P3-25 onward

7 November 2026, Codex for Felipe. Baseline `3c5e568`; initial pull completed, already up to date.

## Assessment
Reviewed all 15 tasks with status review from P3-25 through P3-42. P3-28 was paused, so only its dependency/scorer boundary was inspected. No final PDF certification, fresh live-source audit, or human sign-off is claimed. Numerical results reproduce where inputs are available; remaining issues primarily affect claim wording and the current access benchmark's finalization gate. No production calculation, deck or frozen number changed.

## Coverage and disposition
| Tasks | Evidence | Disposition |
|---|---|---|
| P3-25 | Code/specification/finding reviewed; full replay blocked by missing frozen MB hourly input | review retained; named human gate |
| P3-26, P3-30–P3-33, P3-36, P3-39–P3-40 | Independent duration/treasury review, 37 checks, 20 CSV comparisons, independent accounting | Economist review statuses retained |
| P3-27 | Six options, evidence links, measurable comparators, task criteria and formal specs reviewed | done; historical planning deliverable only |
| P3-29, P3-37 | Five offline ledger/operations replays, integer reconciliation and separate transfer calculation | review retained; named human/economic gates |
| P3-38 | Pinned Git snapshot hashes, all historical synthetic observations reproduced; current selftest passes | done; historical method-review deliverable only |
| P3-41–P3-42 | 23 checks, 24 byte-identical outputs; independent all-row accounting and chronology checks | Economist review statuses retained |

## Priority findings and proposed fixes
1. **Access scoring must not certify an incomplete human audit.** Current code labels a nonempty audit FINAL without checking complete required decisions; note text is excluded from audit identity. Opposite notes can share a decision. Synthetic reproduction only; no real outputs/labels inspected. Follow-up P3-43 is todo under the P3-28 owner. No H1/final guardrail claim should precede this fix and the outstanding human work.
2. **Narrow downstream duration/treasury/incident wording.** The tested duration model's failure to establish an edge does not prove duration cannot be predicted. The ideal fixed-notional hedge does not make waiting depend solely on the local premium. Excluding one incident-day observation does not establish complete incident insulation or restored withdrawals. Exact locations and replacement wording are in the duration/treasury report.
3. **Qualify two displays.** Equal supply at two endpoints is not proof of a flat intervening window (P3-29). P3-41's signal-price chart should identify the execution gap before standalone annex use.
4. **Restore missing P3-25 input and retain human gates.** The frozen MB hourly file is missing locally. Several other tasks require Nattan/Jonathan/Felipe review explicitly; this agent review does not impersonate those decisions.
5. **Refresh stale handoffs when applying changes.** P3-36 has an obsolete P3-35 reference; P3-40's original replay blocker is superseded by its supplement. Historical logs remain intact.

## Supporting review records
- [Ledger and composition](review-2026-11-07-p25-ledger.md)
- [Duration, treasury and prior audits](review-2026-11-07-duration-treasury.md)
- [Access options and scorer](review-2026-11-07-access-options.md)
- [Compression experiments](review-2026-11-07-compression.md)

Proposed interpretation/display repairs remain unapplied in this review pass. Platform path/encoding differences from replay were compared and restored; no result table update is included. Source openings rely on the recorded provenance; this session did not revalidate current law, provider operations or external incident details. Final PDF visual coverage is outside this scoped task review.
