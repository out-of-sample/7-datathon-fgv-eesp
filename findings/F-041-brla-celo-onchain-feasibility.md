---
id: F-041
title: BRLA's Celo supply can be rebuilt from public chain records - two free providers serve June 2026 state and logs, the contract changes supply only through mint and burn events, and DefiLlama's Celo series is that contract's total supply at an undocumented hour of each day
status: exploratory
task: P3-29
date: 2026-11-07
checked_by: -
---

## Claim
**Feasibility result (P3-29 S1), not a reconciliation.** Free public endpoints serve everything a ledger of BRLA on Celo
needs for June 2026. Two independent providers (Forno and Ankr) return the same total supply at both snapshot blocks.
On-chain supply was **128,106,372.44 BRLA** at 19 Jun 2026 00:00 UTC and **135,855,038.46 BRLA** at 1 Jul 2026 00:00 UTC,
a change of **+7,748,666.02 BRLA**. In the contract active over that period, supply changes only through `mint` and
`burn`, and each one emits a `Transfer` event from or to the zero address. So the stock identity can be tested to
the base unit.

DefiLlama's Celo series (the input to F-037) is, by its own June 2026 code, the contract's `totalSupply` / 10^18 with no
excluded balances. Each daily value is stored under 00:00 UTC but comes from an hourly run at an unrecorded time of that
day. Against 00:00 UTC on-chain values it differs by **+179,325.56 BRLA** (19 Jun label) and **−36,854.46 BRLA** (1 Jul
label). Its 19 Jun → 1 Jul change (+7,532,486) is 216,180 BRLA smaller than the on-chain change between the two
midnights. These are raw differences. Snapshot time is unknown, so they are **not** provider errors and not yet residuals.

## Evidence
Reproduce: `.venv/bin/python scripts/p3_29_reconcile.py smoke` (live; reuses frozen answers) or
`P3_29_OFFLINE=1 .venv/bin/python scripts/p3_29_reconcile.py smoke` (frozen files only; rebuilt both tables byte for byte
on 7 Nov). Inputs `data/raw/p3_29/` (112 files, checksums in `data/raw/SHA256SUMS`) and the Flash DefiLlama JSON
(`data/README.md` → restore). Outputs `data/processed/P3-29_s1_snapshots.csv`, `results/tables/P3-29_s1_coverage.csv`.

| Item | Result |
|---|---|
| Chain | Celo mainnet, chain ID 42220 (Forno, Blockscout, Ankr) |
| Contract | `0xfecb3f7c54e2caae9dc6ac9060a822d47e053760`: EIP-1967 proxy created 22 May 2024 (block 25,746,892); attributed by Avenia's current terms (T-06), CoinGecko (D-20) and DefiLlama since 22 Mar 2026 (T-14) |
| Implementation at both blocks | `0xe6a5…ddfb` (`BRLAV1_1`, verified source on Blockscout, T-19); same proxy and implementation code hashes at open and close; admin slot empty (UUPS); decimals 18 |
| Opening block | 69,926,442 (`0xbdff…8acc`), 2026-06-19 00:00:00 UTC; same hash on Blockscout |
| Closing block | 70,963,242 (`0x482f…27ef`), 2026-07-01 00:00:00 UTC; same hash on Blockscout; below Forno's finalized head (82,119,124) |
| `totalSupply`, base units | open 128106372436012947246956951 (Forno = Ankr = Blockscout = dRPC); close 135855038456484705968642568 (Forno = Ankr) |
| Logs | Forno: up to 5,000 blocks per call; Ankr: 1,000 works, 10,000 refused. Same 35 `Transfer` logs on both in (b0, b0+1,000]; 18 of them involve the zero address (not classified) |
| Receipts | Ankr by hash; Forno only by block (`eth_getBlockReceipts`), identical; Forno by hash returns `null` for a transaction it knows |
| Gaps | Blockscout eth-rpc rate-limited (HTTP 429) after its first calls; 1rpc and Stakely pruned; dRPC free tier lacks `eth_getCode` and receipts |
| Provider definition | June code: `totalSupply / 10 ** decimals` per issued contract, no exclusions (T-14, T-15); daily value from an hourly run within the UTC day, replaceable later (T-16); stored as whole BRLA on 226 of 227 Celo days |

## Caveats
- Feasibility only. No interval has been collected or classified yet. The stock identity (supply change = mints − burns) and
  the provider comparison are S3/S4 work under a protocol committed first (S2).
- The implementation was checked at the two snapshot blocks only. An upgrade and roll-back between them would not show
  there; S3 collects every log of the contract in (b0, b1] and checks `Upgraded` events.
- The verified source is Blockscout's verification of the implementation address; matching it to the bytecode was not
  repeated here.
- Celo only. Polygon, Gnosis and Moonbeam are other contracts with their own checks (S4). No claim about who minted or
  burned, fiat redemption, reserves or the BCB.
- The snapshot boundaries are the task's initial 19–30 Jun case; S2 may change them.

## Used in deck
Not used.

## History
- 2026-11-07, agent for Renzo: S1 tables renamed `data/processed/P3-29_s1_snapshots.csv` and
  `results/tables/P3-29_s1_coverage.csv` (byte-identical; the old names now hold S3's tables). S3 result in F-042
- 2026-11-07, agent for Renzo: created (P3-29 S1, G1 passed for Celo)
