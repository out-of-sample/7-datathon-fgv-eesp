---
id: F-047
title: BRLA's large June burns use an authorized transfer-and-burn routine also seen before the notice; their fiat purpose remains unidentified
status: exploratory
task: P3-37
date: 2026-11-07
checked_by: -
---

## Claim
The eight large Celo BRLA burns already identified by P3-29, totalling **335,396,065.575129 BRLA**, all use the same two-step operation: move tokens from `0xe3a2…53c1` to `0xbd22…855e`, then burn the identical amount from `0xbd22…855e` within the same transaction. The second account therefore has **zero net BRLA balance change from those two steps**. It is an intermediate account in these operations, not evidence of the ultimate economic owner. This includes the **113,589,603.97 BRLA** burn at **13:15:03 UTC / 10:15:03 Brasília on 23 June 2026**, as well as the earlier large burns on 19 and 22 June.

The intermediary contract is an **authorized batch executor**: its historical MiniVM implementation restricts execution to operator-role holders, and the executor itself has BRLA's operator role, which permits minting. All **32 selected transactions** have decoded commands consistent with successful execution events and token transfers. The same transfer-and-burn sequence appears in **10 of 12 first-burn-of-day controls**; the other two burn directly from `0xe3a2…53c1`. These results identify a recurring issuance/collection mechanism. They do **not** identify the specific customer operation, a completed fiat redemption, a bridge migration or a regulatory cause. Directly supported off-chain economic purposes: **0/32 transactions**; this measures identification, not whether off-chain payments happened.

Current Avenia documentation explicitly describes both ticket-payment burns and end-of-day settlement mints/burns. It also describes unsuccessful payouts that leave or return value to a token balance. These documented alternatives make a burn an insufficient standalone proxy for completed withdrawal, customer flight or capital outflow. The current pages do not establish which alternative applied in June.

## Evidence

### Fixed sample and reproduction
The rules were committed and pushed as **b161a85**, under the initial ID P3-35, before new evidence collection. The task was renamed P3-36 in **de4fbc5** after an unrelated concurrent review reused P3-35; its final task ID is P3-37 because upstream also independently used P3-36. Artifact prefixes remain P3-36 for provenance. No sampling rule changed. The June episode and large burns were already known: this is a retrospective diagnostic study.

- Eight large burns: the pre-existing P3-29 rule, each at least 1% of that case's gross mint-plus-burn amount.
- Controls: first mint and first burn by block/log order on each UTC day from 19 to 30 June. All selected transaction hashes are distinct. Controls are concentrated near midnight by construction and are not a representative sample of daily operations.
- Reproduce: `python3 scripts/p3_36_brla_operations.py --offline`.
- Live collection: the same command without `--offline`; reuses existing responses and retrieves only missing public records.
- Document snapshots: `python3 scripts/p3_36_brla_operations.py --documents --offline`; omit `--offline` to retrieve missing pages.
- Outputs: `results/tables/P3-36_sample.csv`, `P3-36_operations.csv`, `P3-36_commands.csv`, `P3-36_transfers.csv`, `P3-36_summary.csv`, `P3-36_provenance.csv` and `P3-36_documents.csv`.
- Inputs: `data/processed/P3-29_events.csv` (rebuild with P3-29's ledger command), frozen `data/raw/p3_29/` and new `data/raw/p3_36/`. New files have request/URL, retrieval date and checksums. Raw responses remain outside git.

| Selected group | Transactions | Commands | Selected mint amount (BRLA) | Selected burn amount (BRLA) |
|---|---:|---|---:|---:|
| Large burns | 8 | All TRANSFER → BURN | 0 | 335,396,065.575129 |
| First burn of each day | 12 | 10 TRANSFER → BURN; 2 BURN | 0 | 8,859,608.770003 |
| First mint of each day | 12 | 10 MINT → TRANSFER; 2 MINT | 219,450.64 | 0 |
| Total | 32 | All technically decoded | 219,450.64 | 344,255,674.345132 |

Ten mint controls create BRLA at `0xbd22…855e` and move the same amount to `0xe3a2…53c1`. The other two mint directly to `0xe3a2…53c1`. Thus the sampled mint and burn routes mirror one another, and some operations bypass the intermediate account. Every decoded command in this sample concerns BRLA; no swap or bridge command is present. This is a statement about these transactions only, not about separate transactions on other chains.

### Contract and event checks
Full addresses:
- BRLA Celo proxy: `0xfecb3f7c54e2caae9dc6ac9060a822d47e053760`.
- MiniVM proxy: `0xa5e1a81738259256181f9a0e478188553062d340`.
- MiniVM implementation: `0x37f794f3f586a76a643be0be0d107d6b671afa78`.
- Intermediate account: `0xbd22c4c78da827c686217ba17946de11b489855e`.
- Source/destination account: `0xe3a25228e83bbb63eb502d34aa4f7626185053c1`.

For each selected transaction, Forno and Ankr agree on the MiniVM implementation at its block; the prior-block slot agrees too. Historical deployed implementation bytecode equals the bytecode attached to Blockscout's verified source. The source maps command `0x03` to TRANSFER and `0x01` to BURN; BURN calls `burnFrom(address,uint256)` when its wallet is external to MiniVM. Historical role reads confirm both the transaction sender's MiniVM permission and MiniVM's BRLA permission. This establishes technical authorization, not the legal identity of the operator.

Each command's decoded token, source/destination and amount agrees exactly with the transfer event before its `ExecutionComplete` event. All selected transactions and commands succeeded. Receipt transaction/block hashes and the originally selected event amounts are checked. Malformed ABI inputs are rejected by assert-based self-checks; unknown commands or unresolved balance sentinels cannot be silently classified as verified. Full execution traces and an independent source compilation were not performed.

The 23 June transaction is `0xe27fabe8004d4693cfeb41921f69db88ad5a3b5fd338f4f1cfe46df1bcd8ab23`, block 70,319,745. Its input encodes `TRANSFER(BRLA, e3a2…, bd22…, 113589603.97)` followed by `BURN(BRLA, bd22…, 113589603.97)`. Its receipt contains those two BRLA transfers and two successful command-completion events. The visible economic effect is destruction of a BRLA claim held at `e3a2…`; the holder's compensation or reason is not on this record.

### Competing explanations

| Explanation | Evidence obtained | Verdict |
|---|---|---|
| Recurring authorized issuance/collection operation | Same contract and two-step route before/on the notice date; matching small controls; historical roles | Supported at the technical-mechanism level. Recurrence does not prove the June amount was economically ordinary. |
| Internal settlement or treasury adjustment | Current issuer docs list settlement mints/burns; intermediate account has no net change in the two-step transactions | Plausible candidate, not attributed to these transactions. Accounts are not publicly identified as treasury/customer accounts. |
| Customer redeems BRLA and receives reais | Current issuer docs describe token-funded payouts and payment status | Unresolved: no matched ticket, beneficiary settlement record or PIX end-to-end identifier. |
| Cross-chain migration or on-chain token swap | No such command or other token transfer in selected receipts | Not observed within these transactions. Separate linked transactions remain possible; none is identified. |
| BCB notice caused the 23 June burn | Same mechanism appears in large burns before 23 June; notice hour unknown | Not identified; no causal design or timing bridge. |

### Opened documentation
See `docs/sources.md`, T-23–T-28, and the snapshot manifest. Public docs were read on 7 Nov 2026; they are descriptions of current functionality, not historical transaction confirmations.

- The reporting guide distinguishes ticket inputs, deliveries, conversions and settlement entries. This supplies competing explanations, not labels for our cases.
- The payout FAQ says a successful PIX outcome is tracked by ticket status; failures can leave the value in an Avenia balance. Therefore the burn leg cannot certify beneficiary payment.
- The reconciliation guide identifies ticket and PIX end-to-end IDs. The PIX/stable use case shows a `blockchainSenderInfo.txHash` field alongside ticket/payment information. These are example schemas, not observed matches.

## Caveats
- One token, one chain and a selected sample. Large-event selection is retrospective; midnight controls cannot estimate a market-wide frequency or a causal effect.
- A technical operator role is not a named legal entity. Neither the controller nor ultimate beneficiaries of the two accounts have been independently attributed.
- All economic purposes remain unresolved. The source account may aggregate operations for many parties; token quantities are not counts of users or payments. Gross burns are not net cross-border flows.
- Same-transaction equality establishes token routing, not fiat settlement or a bridge. Absence of other token logs here does not rule out off-chain or separate on-chain legs.
- Implementation checks use block-boundary states and verified source/bytecode matching, not full historical execution tracing or a fresh compilation. Receipts are from Ankr; the underlying P3-29 large-event checks and two-provider state comparisons are documented separately.
- Current documentation cannot establish June availability, operator identity or specific June outcomes. Searches of the exact addresses/MiniVM with Avenia/BRLA and official domains found no primary public owner attribution in the inspected results; this is not proof none exists.
- Not yet independently reproduced. Findings remain exploratory and do not replace F-042/F-044 or close P3-29 S7.

## What would resolve the economic purpose
For each large burn, obtain a voluntarily supplied, redacted issuer/authorized account export linking the exact Celo transaction hash and amount to a ticket or settlement entry. It should identify the operation type, input/output currencies and networks, status and timestamps. For a claimed PIX redemption, require a matching settlement confirmation/end-to-end ID; for a treasury adjustment, require the ledger category and account-role explanation; for migration, require the explicit destination transaction/message. A single burn could aggregate several tickets, so the mapping may be one-to-many. No issuer contact or private API access was attempted.

## Used in deck
Not used. Candidate interpretation note for the existing BRLA annex after independent reproduction and Felipe's review. No main-deck or causal claim is proposed.

## History
- 2026-11-07 — Codex for Renzo: registered protocol, decoded the fixed sample, checked historical permissions and bytecode, froze issuer documentation and recorded this exploratory follow-up in English. Task renamed P3-35 → P3-36 solely to avoid a concurrent identifier collision.
- 2026-11-07 — Assigned F-047 before publication because a concurrent access-method review reserved F-046. No analysis changed.
