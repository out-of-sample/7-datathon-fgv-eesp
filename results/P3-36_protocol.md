# P3-36: retrospective investigation of BRLA operations

Registered before new evidence collection, 7 Nov 2026. The eight large burns, their dates, amounts and common MiniVM destination are already known from F-042. This protocol does not create a causal test of the BCB notice.

## Question and primary output
Which execution mechanism and economic purpose can be established for the selected Celo BRLA operations? Report separately the count and BRLA amount with (a) decoded technical mechanism and (b) directly supported economic purpose, keeping unresolved cases in the denominator. No model or statistical causal estimate is fitted.

## Sample fixed before investigation
1. All eight burns identified in P3-29 as at least 1% of gross mint-plus-burn volume in 19–30 June 2026 UTC. These include 19 and 22 June comparisons preceding the 23 June notice date.
2. Routine controls: the first mint and first burn by block/log order on each UTC day, 19–30 June, from the existing P3-29 event file. Deduplicate transaction hashes; retain the selection reason and all selected events.
3. Start with the largest burn. Verify one receipt, input and historical implementation before scaling to the sample. Compare the same observables for all cases; a missing trace is unavailable, not an empty trace.

## Evidence and interpretation
- Read the verified proxy/implementation source and historical EIP-1967 implementation at the selected transaction block. Do not substitute the current implementation for the historical one. Preserve source bytes and all API responses.
- Decode transaction calldata only under verified ABI/source semantics. Compare targets, function selectors, arguments, BRLA transfer paths, other token logs and transaction sender. Receipts establish emitted events, not every internal call; use a public trace if needed and feasible.
- Use integer token base units and Decimal for presentation. Label UTC and Brasília (UTC−3). Event order is transaction/log order; do not infer causation from nearby times.
- Routine-operation explanation: repeated execution structure before/on/after 23 June supports recurring technical use only. It does not establish treasury ownership or economic normality.
- Fiat-redemption explanation: requires explicit issuer/payment evidence linking a specific burn to completed fiat payment. Current general redemption terms show a capability, not that a historical burn redeemed reais.
- Cross-chain or cross-asset explanation: requires an explicit message/transaction identifier linking the legs, with the mechanism documented. Matching amounts or timing alone are insufficient.
- A batch/swap/payout mechanism may establish an on-chain economic action when verified calls and token movements agree. Ultimate beneficiary, residence and off-chain purpose may remain unknown.
- Issuer attribution requires a primary public address statement or verifiable contract/deployment relationship. An explorer label, contract name or one shared counterparty is not proof of control.
- Open primary public documentation with exact URLs, short quotes and retrieval dates. Current documentation is not automatically applicable to June. No contact with issuer/provider, paid services, wallet connections or signed transactions.

## Reproduction and bounded scope
Reuse frozen P3-29 inputs read-only. New data under `data/raw/p3_36/`, with request/URL, retrieval UTC and SHA-256 manifest. A script must reproduce the case tables offline. Test ABI bounds and at least one known decoded call against receipt evidence. Preserve failed lookups. Scope is the sampled Celo operations and directly implicated contracts; stop at unavailable off-chain settlement evidence. Additional samples or mechanisms require a dated amendment disclosing what was already observed.

## Amendments
- 7 Nov 2026: renamed P3-35 to P3-36 after a concurrent P3-28 review reused P3-35. Original rules were committed and pushed as b161a85 before collection. No sample or interpretation rule changed.
