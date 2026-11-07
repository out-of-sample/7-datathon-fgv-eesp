---
id: F-044
title: Outside June the same procedure works unchanged - 12 frozen BRLA cases on Celo close to the base unit and DefiLlama matches on-chain supply on all 24 of their labels; on Polygon, Gnosis and Moonbeam a registered prediction of DefiLlama's daily read held (32 matches, 0 misses, 6 of them informative)
status: exploratory
task: P3-29
date: 2026-11-07
checked_by: -
---

## Claim
**Generalization (P3-29 S5).** Twelve cases were chosen by a rule frozen before the June study (protocol §8): the 6
largest daily changes in DefiLlama's Celo series from 25 Mar to 30 Oct 2026, at least 7 days apart, and 6 ordinary days
drawn with a fixed seed. The manifest was committed (`d6008bf`) before any case was collected. In all 12 cases the
Celo stock identity closes to **0 base units on both days** (24 of 24 days). Every integrity check passes and
**317 of 317** sampled events are confirmed by a second provider's receipt. DefiLlama's value equals the on-chain
supply at some block of its UTC day on **24 of 24** labels. The procedure needed no case-specific change. Across the 37
Celo labels tested so far (13 in June, 24 here), the only misses are 26 Jun and 2 Jul, both carrying the same value
(F-042).

**When DefiLlama reads the chain** (description, not a documented snapshot time): the matching block falls at
00:44–00:46 UTC from 3 May to 1 Sep, and at 00:04–00:07 UTC on 29 Mar and from 13 Sep on (13 Sep, 15 Oct, 26–27 Oct).
On Polygon, Gnosis and Moonbeam, a prediction registered before their data were read (P-0045) said DefiLlama's
value should equal the supply in any 00:44–00:48 UTC window where supply did not change. It held on **32 of 32**
testable labels (0 misses). Most matches are trivial, because supply did not change between 00:00 and 00:44
(Moonbeam's supply is constant at 4,385 BRLA). Only **6** are informative: Polygon 5, Gnosis 1.

**Who mints and burns:** the account that dominated June (`0xbd22…855e`) is the largest minter/burner in 11 of 12 cases
(84.8–99.9% of mint+burn volume). In the 29 Mar case the other June account (`0xe3a2…53c1`) does 100%. Over two days,
gross mints + burns are 2 to 22 times the net change.

## Evidence
Reproduce: `.venv/bin/python scripts/p3_29_reconcile.py cases` (S5) and `... chains` (S4); add `P3_29_OFFLINE=1` to
use the frozen answers only. Inputs: `data/raw/p3_29/` (2,841 files with checksums, not in git) and the Flash DefiLlama
JSON. Outputs: `results/tables/P3-29_s5_manifest.csv` (frozen selection; 205 inventory days, |Δ| quartiles 1.45 and
17.13 mn BRLA, 71 eligible ordinary days), `results/tables/P3-29_s5_cases.csv`, `data/processed/P3-29_s5_days.csv`,
`data/processed/P3-29_chains.csv`, `results/tables/P3-29_chains_prediction.csv`, `results/tables/P3-29_chains_audit.md`.
Rules: `results/P3-29_protocol.md` §8 and amendments 10–11 (`19a878f`, before any other-chain or case data).

| Case | Label | Δ reported (mn BRLA) | Residual day 1 / day 2 | DefiLlama D−1 / D | Read time (UTC) | Receipts | Top account share |
|---|---|---:|---|---|---|---|---:|
| L1 | 27 Oct | −76.30 | 0 / 0 | consistent / consistent | 00:04 | 25/25 | 97.2% |
| L2 | 21 Aug | −62.50 | 0 / 0 | consistent / consistent | 00:45 | 25/25 | 87.1% |
| L3 | 13 Jun | −51.95 | 0 / 0 | consistent / consistent | 00:45 | 36/36 | 99.9% |
| L4 | 29 Jul | +50.45 | 0 / 0 | consistent / consistent | 00:45 | 43/43 | 99.3% |
| L5 | 1 Sep | −46.85 | 0 / 0 | consistent / consistent | 00:44–00:45 | 29/29 | 88.8% |
| L6 | 15 Oct | +41.52 | 0 / 0 | consistent / consistent | 00:04 | 20/20 | 96.7% |
| O1 | 29 Mar | −1.93 | 0 / 0 | consistent / consistent | 00:07 | 18/18 | 100.0% (`0xe3a2`) |
| O2 | 3 May | −1.76 | 0 / 0 | consistent / consistent | 00:45 | 23/23 | 99.0% |
| O3 | 28 May | −9.64 | 0 / 0 | consistent / consistent | 00:46 | 29/29 | 91.4% |
| O4 | 8 Jul | −3.94 | 0 / 0 | consistent / consistent | 00:45 | 26/26 | 98.7% |
| O5 | 7 Aug | −9.19 | 0 / 0 | consistent / consistent | 00:45 | 30/30 | 96.2% |
| O6 | 13 Sep | +11.58 | 0 / 0 | consistent / consistent | 00:04 | 13/13 | 84.8% |

- **Other contracts (S4), 15 boundaries 19 Jun – 3 Jul:** two archive providers agree at every boundary on each chain
  (Polygon: dRPC = Tenderly; Gnosis: gnosischain.com = gateway.fm; Moonbeam: dRPC = OnFinality; T-22). Implementation slot
  and code hash constant; decimals 18. Gnosis's implementation is the same `BRLAV1_1` address as Celo's; Polygon
  (`0xe919…3244`) and Moonbeam (`0x116a…01a1`) use others, which were not inspected.
- **P-0045 detail:** Polygon 6 match / 7 window not flat; Gnosis 13 match; Moonbeam 13 match; misses none.

## Caveats
- **Diagnostic sample, not a population estimate.** Selection on the aggregate change is explicit; 12 cases on one
  chain. The development case (June) was retrospective.
- **Read time:** a regularity seen in the data and confirmed out of sample on three chains, but not DefiLlama's
  documented rule (T-16). It moved between 1 and 13 Sep. Only 6 of the 32 held-out matches could have failed.
- **Other chains:** boundary reads only (no logs), so no within-day check there and no transaction-level link to Celo.
- **Accounting only:** dominant account ≠ owner; mint ≠ fiat subscription; burn ≠ redemption.
- Not yet reproduced by a teammate (S7). H4 (agent comparison) waived (protocol §8): no claim about AI tools.

## Used in deck
Not used.

## History
- 2026-11-07, agent for Renzo: created (P3-29 S4 prediction and S5 cases)
