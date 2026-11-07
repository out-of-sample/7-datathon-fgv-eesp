---
id: F-042
title: On Celo, BRLA's supply from 19 Jun to 1 Jul 2026 reconciles to the base unit with 17,536 mints and burns (732.6 mn minted, 724.9 mn burned, net +7.7 mn), almost all by one account; DefiLlama's daily values match on-chain supply on 12 of 13 days, but its 26 Jun low (59.3 mn) matches no on-chain state
status: exploratory
task: P3-29
date: 2026-11-07
checked_by: -
---

## Claim
**Retrospective case study** (the aggregate shape was known from F-037; protocol committed before collection,
`cfccbfc`). Over 19 Jun 00:00 → 1 Jul 00:00 UTC 2026, BRLA's `totalSupply` on Celo rose by **+7,748,666.02 BRLA**
(128.11 → 135.86 mn). That change equals mints minus burns **to the base unit**, on every UTC day and over the whole
period. Two providers agree on the stock at all 15 daily boundaries, and no contract upgrade occurred. The net change hides
gross flows about 190 times larger: **732.6 mn BRLA minted in 8,884 mints and 724.9 mn burned in 8,652 burns.**
Only two addresses, both plain accounts (not contracts), received the mints and held the burned tokens. One of them,
`0xbd22…855e`, took **96.2%** of the mints and **92.7%** of the burns.

The fall that F-037 dates to 24 Jun happened on Celo during **23 Jun (UTC)**. That day had 185.3 mn of burns against
72.5 mn of mints, including **one burn of 113.6 mn BRLA at 13:15 UTC (10:15 Brasília)**. DefiLlama's 24 Jun label,
read the next morning, shows the result. On-chain records say who executed each change, not why.

DefiLlama's Celo series is, by its own code, this contract's total supply (F-041). On **12 of 13** daily labels its value
equals the on-chain supply at some block of that UTC day within ±1 BRLA, and every match falls at about 00:45–00:46 UTC.
That time is description, not a documented snapshot time. The **26 Jun value, 59,281,880 BRLA, matches no on-chain
state:** Celo supply ranged from 98.9 to 119.4 mn that day and never fell below 87.1 mn at any block from 19 Jun to 3 Jul.
The same number is repeated under the 2 Jul label, which is also outside its day's range (91.1–109.7 mn). Unresolved.

## Evidence
Reproduce: restore the Flash bundle (`data/README.md`), then `.venv/bin/python scripts/p3_29_reconcile.py ledger` (live:
reuses the frozen answers and re-downloads missing ones, ~4 min) or `P3_29_OFFLINE=1 .venv/bin/python
scripts/p3_29_reconcile.py ledger` (frozen files only; byte-identical outputs on 7 Nov). Raw: `data/raw/p3_29/` (527 files,
checksums in `data/raw/SHA256SUMS`). Outputs: `data/processed/P3-29_reconciliation.csv`, `P3-29_snapshots.csv`,
`P3-29_events.csv` (20,455 rows, 5.8 MB, not in git, rebuilt by the command), `results/tables/P3-29_coverage.csv`,
`results/tables/P3-29_case_audit.md` (every table below). Protocol: `results/P3-29_protocol.md` (`cfccbfc`; amendments
1–6 before output, `5d44c1b`; 7–9 post hoc).

| Day (UTC) | Supply start → end (mn BRLA) | Mints, mn (n) | Burns, mn (n) | Stock residual | DefiLlama label |
|---|---|---:|---:|---:|---|
| 19 Jun | 128.11 → 190.31 | 217.84 (727) | 155.63 (732) | 0 | consistent (00:45) |
| 20 Jun | 190.31 → 192.37 | 5.51 (633) | 3.46 (829) | 0 | consistent |
| 21 Jun | 192.37 → 196.80 | 7.46 (674) | 3.04 (789) | 0 | consistent |
| 22 Jun | 196.80 → 208.38 | 114.12 (824) | 102.53 (638) | 0 | consistent |
| 23 Jun | 208.38 → 95.64 | 72.54 (774) | 185.28 (686) | 0 | consistent |
| 24 Jun | 95.64 → 109.99 | 57.75 (774) | 43.40 (685) | 0 | consistent |
| 25 Jun | 109.99 → 115.66 | 25.63 (788) | 19.97 (671) | 0 | consistent |
| 26 Jun | 115.66 → 101.60 | 51.90 (787) | 65.96 (672) | 0 | **outside day range** (59.28 reported) |
| 27 Jun | 101.60 → 112.70 | 15.51 (656) | 4.40 (808) | 0 | consistent |
| 28 Jun | 112.70 → 113.55 | 4.71 (593) | 3.86 (871) | 0 | consistent |
| 29 Jun | 113.55 → 136.03 | 80.92 (814) | 58.44 (648) | 0 | consistent |
| 30 Jun | 136.03 → 135.86 | 78.73 (840) | 78.90 (623) | 0 | consistent |
| 1 Jul (outside the case) | 135.86 → 97.01 | 42.83 (729) | 81.68 (728) | 0 | consistent |
| 2 Jul (post hoc) | 97.01 → 100.45 | 31.82 (773) | 28.38 (689) | 0 | **outside day range** (59.28 reported) |

- **Coverage and integrity:** 242 log chunks tile 19 Jun 00:00:01 – 3 Jul 00:00:00 UTC with no gap. There are 0 duplicate
  and 0 removed logs, one block hash per block (20,272 blocks), and 0 unknown event topics; event hashes come from
  `web3_sha3` on two nodes. Exactly 86,400 blocks per day. Forno = Ankr `totalSupply` at all 15 boundaries. The
  implementation slot is the same at every boundary, and no `Upgraded`/`AdminChanged`/`Initialized`/`Paused` log appears.
- **Cross-checks:** every mint/burn of at least 1% of gross volume (8 events, all burns) plus 30 seeded smaller ones
  (seed 20261107) appear in a successful Ankr receipt with identical log index, topics, data and block hash. The 8 large
  events' block hashes match Forno headers.
- **Large events:** the 8 burns are 14.6–113.6 mn BRLA on 19, 22 and 23 Jun. All come from `0xbd22…855e`, and every
  transaction called `execute(bytes,bytes[])` (selector `0x24856bc3`, hash-checked) on `0xa5e1…d340`. Blockscout lists
  that address as a verified `ERC1967Proxy` with implementation `MiniVM`, created by `0xBA00…a8dC`, no public tags (T-21).
  The second account is `0xe3a2…53c1`: 3.8% of mints, 7.3% of burns.
- **Provider residual (development case):** DefiLlama's change between the 19 Jun and 1 Jul labels (+7,532,486) minus
  the on-chain change between the two midnights = **−216,180.02 BRLA** (2.87% of the reported change). Both end labels are
  consistent within their days, so this difference fits the reading time (about 00:45 vs 00:00 UTC). Raw differences at
  00:00 UTC per label range from −1.11 mn to +5.73 mn on consistent days, and are −56.38 mn on 26 Jun.
- **Versions:** v1 (Flash, 4 Nov) and v2 (pulled 7 Nov 03:53 UTC, T-20) agree on every June–July label. The only
  difference among 227 common labels is 5 Nov, a float in v1 stored as a whole number in v2.
- **Brasília days** (description, audit table): the 23 Jun Brasília day has 185.1 mn of burns, nearly the same as the
  UTC day.

## Caveats
- **Accounting, not economics.** A mint is not a fiat subscription and a burn is not a redemption. An address is not an
  owner, and no burn/mint pair is linked across chains (no bridge or message ID was collected; the implementation has
  no bridge logic). Whether the burned BRLA went to reais, to another chain or elsewhere is **not shown**.
- **Same date as the BCB notice, not linked to it.** The 113.6 mn burn fell on 23 Jun, the date of the BCB notice; the
  hour of the notice is not known to us. The same account also burned 100.0 mn on 19 Jun and 65.7 mn within seven
  minutes on 22 Jun, before the notice. Size alone does not single out 23 Jun, and the protocol forbids a causal
  reading.
- **The 00:45 UTC match** is a pattern in the data, not DefiLlama's documented snapshot time (T-16). It is consistent
  with one hourly run per day, read at about 21:45 Brasília of the day before the label.
- **26 Jun / 2 Jul:** a repeated value below every on-chain state in the period. Calling it a provider error would need
  DefiLlama's own records. Celo only; other chains' contracts were not checked (S4).
- **Retrospective**, one chain, one 12-day case; no generalization (S5 deferred). Not yet reproduced by a teammate (S7).

## Used in deck
Not used. Candidate annex line after review (P3-29 S6/S7), not before.

## History
- 2026-11-07, agent for Renzo: created (P3-29 S3)
