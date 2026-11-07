# P3-29 protocol: BRLA on Celo, 19–30 Jun 2026 (S2)

Committed 7 Nov 2026 by the agent for Renzo, **before any log of the interval was collected or classified**. S1 (F-041)
saw only two `totalSupply` values and 35 logs in (b0, b0 + 1,000]. The aggregate shape (DefiLlama: rise 19–23 Jun,
fall 24–26 Jun) was known before this protocol (F-037). So this is a **retrospective case study**, not a blind test.
Changes after this commit go to "Amendments" with a timestamp and say whether they were made after seeing S3 output.

## 1. Scope
- One representation: BRLA on Celo, chain ID 42220, proxy `0xfecb3f7c54e2caae9dc6ac9060a822d47e053760`,
  implementation `BRLAV1_1` `0xe6a537a407488807f0bbeb0038b79004f19dddfb` (F-041, T-14–T-19). Not a global BRLA audit.
- For the 8 Nov PDF (Renzo, 7 Nov): Celo case study only. S4 is limited to other chains' `totalSupply` at the same
  boundaries (if their public RPCs serve history), with no cross-chain linking. S5 (generalization) and H4 (agent
  comparison) are deferred. Their rules (§8) are frozen now so a later run cannot pick them after seeing results.
- Native units only (BRLA base units, 18 decimals). No market value, no fiat or BCB interpretation.

## 2. Boundaries and timing
- Daily boundaries T_d = d 00:00:00 UTC for d = 19 Jun … 2 Jul 2026 (14 boundaries). Block b_d = last block with
  timestamp ≤ T_d (Forno headers; Celo L2 makes 1-second blocks, so b_d is expected at b0 + 86,400·k and is verified
  with the header of b_d and b_d + 1). Interval for day d = (b_d, b_{d+1}].
- **Development interval (stock identity):** (b0, b1] = (69,926,442, 70,963,242], 19 Jun 00:00 → 1 Jul 00:00 UTC,
  12 days. **Collected interval:** through b(2 Jul) = 71,049,642, so the DefiLlama label of 1 Jul can be compared
  with its whole UTC day (§5). The 1 Jul day is reported separately and is not part of the development totals.
- Times are UTC. Sensitivity, description only: daily mint/burn totals by Brasília day (UTC−3).

## 3. Accounting definitions
- S(b) = `totalSupply()` at block b by `eth_call`, integer base units. Read at every boundary on Forno and Ankr.
  Also read at every boundary on Forno: `decimals()` and the EIP-1967 implementation slot.
- Event = log emitted by the proxy address. **Mint:** topic0 = `Transfer`
  (`0xddf2…b3ef`) with `from` (topic1) = 0x0, amount = `data` as uint256. **Burn:** `Transfer` with `to` (topic2) = 0x0.
  Basis: verified `BRLAV1_1` source (`_totalSupply` changes only in `_mint`/`_burn`, each emits that `Transfer`; T-19).
- Gross mints M, gross burns B, gross supply-changing volume G = M + B (base units) over an interval.
- **Stock residual:** R_stock = [S(b_end) − S(b_start)] − (M − B), per day and for the development interval.
  `verified_other_adjustments` = none (no documented mechanism). **Tolerance: 0 base units.** A non-zero residual is
  reported as is, investigated, and never plugged.
- Any log with topic0 `Upgraded`, `AdminChanged`, `BeaconUpgraded` or `Initialized`, or an implementation slot that
  differs between boundaries, ends the identity at that point. The two sides are then reported separately.
- Ordinary transfers are counted per day but not decoded further. `Paused`/`Unpaused` and role events are listed.

## 4. Collection and completeness
- `eth_getLogs` on Forno with an address filter and **no topic filter**, in consecutive 5,000-block chunks from
  b0 + 1 to b(2 Jul). Any error halves the chunk, down to 500 blocks, after up to 4 retries. A chunk that still fails is
  a **coverage gap**: its day gets no identity and the gap is never counted as zero events.
- Every frozen response is kept under `data/raw/p3_29/` with checksums. Coverage manifest = chunk ranges, statuses and
  log counts; the chunks must tile the interval exactly.
- Deduplicate on (blockHash, transactionHash, logIndex); report duplicates and any `removed: true`. All blocks are
  far below the finalized head (S1: 82,119,124), so they are treated as canonical; log block hashes at the boundary
  blocks are checked against headers.
- **Independent checks:** (a) S(b_d) on Ankr equals Forno at every boundary. (b) Every mint/burn of at least 1% of G
  (development interval) is checked against a receipt from a second source: Ankr `eth_getTransactionReceipt`
  (`status` 0x1, a log with the same logIndex, topics, data and blockHash), or else Forno `eth_getBlockReceipts`,
  labelled same-provider. The same goes for a sample of 30 smaller mint/burn events, drawn with
  `random.Random(20261107).sample` from all of them sorted by (block, logIndex). (c) For events ≥ 1% of G, the
  transaction is also fetched (`from`, `to`, 4-byte selector), to name the contract function used (mint, burn,
  burnFrom, burnFromWithPermit). This says which mechanism ran, not why.

## 5. Provider comparison (DefiLlama ID 365, Celo)
- **Definition: identified.** June code = `totalSupply / 10 ** decimals` of this contract, no excluded balances
  (T-14, T-15), so C_hat(b) = S(b) / 10^18 and `eligible_excluded_balances` = 0 by DefiLlama's own rule.
- **Timing: not identified** (T-16). The daily value for label D comes from an hourly run inside UTC day D and may be
  replaced later. Status `time_alignment_unknown` for every label.
- **Versions:** v1 = Flash response of 4 Nov (the F-037 input, primary). v2 = a fresh pull of
  `https://stablecoins.llama.fi/stablecoin/365`, made after this commit and before event collection. Any label where
  v2 ≠ v1 is reported as a revision.
- **Raw residuals (always reported):** r_D = reported_D − C_hat(b_D) at the label's nominal 00:00 UTC, for labels
  19 Jun … 1 Jul. Case residual R_provider = (reported_1Jul − reported_19Jun) − (C_hat(b1) − C_hat(b0)), with the
  relative version |R_provider| / max(|Δreported|, 1 BRLA), denominator stated.
- **Tolerance, derived from the documentation before matching:** rounding = stored values are whole BRLA, so ±1 BRLA
  per value. Timing = the value was read at some block of UTC day D. Label D is `consistent_within_day` if reported_D
  lies within ±1 BRLA of S at some point of day D's path. The path is S(b_D) followed by S after each mint/burn in
  (b_D, b_{D+1}], built only when day D's stock residual is 0. Otherwise the label is `outside_day_range` (unresolved)
  or `not_tested`. For consistent labels, the first and last time the path is within ±1 BRLA are reported as
  **description**. They are never called the snapshot time or a verified alignment.
- Reading: H1 for this case is **supported only as "consistent within the day"**, since exact-time reconciliation is
  impossible without a documented snapshot time. It needs all of: zero stock residual on every day, complete
  coverage, no upgrade, passing cross-checks, and all 13 labels consistent. Any failed requirement is reported.

## 6. Evidence categories and claim limits
- Accounting columns: event type (mint/burn/other), amount, block/time, tx hash, log index, counterparty address
  (recipient of a mint, holder of a burn), function selector (large events), raw file.
- Interpretation column: `unresolved` for every event. The implementation has no bridge logic, and no
  message or bridge ID is collected, so **no burn/mint pair is called a migration**. Cross-chain coincidence (S4) is
  described, not linked. Mint ≠ fiat subscription, burn ≠ fiat redemption, address ≠ owner.
- Allowed reading if the stock identity closes: "On Celo, BRLA's supply rose/fell by X through N mints and M burns,
  concentrated in K addresses; on-chain records do not say why." Not allowed: "corrida", "resgate", "migração",
  any BCB effect.

## 7. Outputs
`scripts/p3_29_reconcile.py collect` / `reconcile` (and `P3_29_OFFLINE=1` for frozen-only replay) →
`data/processed/P3-29_snapshots.csv` (boundaries × providers; the S1 table becomes `P3-29_s1_snapshots.csv`),
`P3-29_events.csv` (supply-changing and non-Transfer events), `P3-29_reconciliation.csv` (per day and interval),
`results/tables/P3-29_coverage.csv` (chunks and checks), `results/tables/P3-29_case_audit.md` (large events,
counterparty concentration, cross-checks, provider labels). New finding with the next free ID.

## 8. Deferred rules, frozen now
- **S5 sample:** inventory = v1 Celo daily changes Δ_D = reported_D − reported_{D−1}, 25 Mar – 30 Oct 2026, excluding
  labels 18 Jun – 2 Jul. **Large:** descending |Δ_D|, keep a label only if ≥ 7 days from every label already kept,
  take 6. **Ordinary:** labels whose |Δ_D| is between the 25th and 75th percentile of the inventory, ≥ 7 days from the
  large ones, 6 drawn with `random.Random(20261107)`. Case interval for label D = (b(D−1 00:00), b(D+1 00:00)]. The
  same accounting and provider rules apply. Every case is reported, including failures.
- **H4:** waived for the 8 Nov submission. It needs at least 10 held-out episodes and two human reviewers (task spec).
  No claim of agent benefit is made.
- **S4 (limited):** `totalSupply` on Polygon `0xe6a5…ddfb`, Gnosis and Moonbeam at the same boundaries, only after a
  capability check like S1's. Each chain's contract identity is checked separately. Coincident moves are not linked.

## Amendments
- 2026-11-07 01:25 Brasília, **before any S3 output was seen** (implementation details, no rule changed):
  (1) one command, `ledger`, does collection and reconciliation (§7 named `collect`/`reconcile`). (2) Event topics
  and function selectors are computed with `web3_sha3` on Forno and Ankr (they must agree), from the eleven event
  declarations of the verified source. No local Keccak is installed. (3) Added: the block hash of every
  ≥ 1%-event block is checked against its header; every block number must carry one hash only. (4) The S1 tables are
  renamed `P3-29_s1_snapshots.csv` / `P3-29_s1_coverage.csv`. (5) The 2 Jul label falls outside the collected days
  and is reported `not_tested`. (6) DefiLlama path points are end-of-block states, because `eth_call` at a block
  cannot see a state between two logs of the same block.
