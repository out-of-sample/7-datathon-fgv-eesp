---
id: P3-18
title: Where did the USDT sold on Foxbit during the fade come from? (on-chain check of F-031)
phase: P3
status: blocked
owner: CS 1
working: -
due: 2026-11-04
depends: P3-17
---

## Goal
F-031 (post hoc) found that while the premium fell, a new business-hours seller sold about 362 mn USDT net on Foxbit
(30 Jun – 21 Jul 2026), but not who it was or where the coins came from. This task looks at USDT deposits to Foxbit's wallets
on the blockchain to see whether the coins arrived from abroad (other exchanges, the issuer) or were already in Brazil.
Approved by Renzo on 2 Nov 2026. Optional for the deck: F-031 stays "consistent with", whatever this finds.

## Blocker (2 Nov 2026)
We need Foxbit's wallet addresses from a source we can open and quote (`prompt.md` §6). None was reachable without an
account or key: Arkham entity page (https://arkm.com/explorer/entity/foxbit: HTTP 403 to automated access, needs login);
Tronscan tag search (https://apilist.tronscanapi.com/api/search/v2?term=foxbit: HTTP 401, needs a free API key); Etherscan
labels and the acionista.com.br article on Arkham's Brazilian-exchange labels (Cloudflare 403); foxbit.com.br has no
proof-of-reserves page (`/prova-de-reservas/`, `/proof-of-reserves/`, `/transparencia/`: 404). **Arkham checked by Renzo (logged in, 2 Nov 2026):** https://arkm.com/explorer/entity/foxbit exists ("Foxbit.com.br",
tags "Centralized Exchange", "High Transacting", "267.1k Addresses", balance $0); with the Tron filter: "No assets found" and
"No transfers match these filters"; the only asset shown on any network is BTC. Arkham attributes no Tron or Ethereum USDT
address to Foxbit, so option 1 is closed. Addresses are **not** to be
guessed. Ways to unblock, any one:
1. ~~A teammate with an Arkham login opens the Foxbit entity~~ (done 2 Nov: no Tron addresses), copies the TRON (and Ethereum) addresses tagged as Foxbit with
   the tag text, and pastes them into S1 (quickest).
2. Renzo creates a free Tronscan API key and puts it in `.env` as `TRONSCAN_API_KEY` (never in git); the agent searches tags.
3. A teammate's own Foxbit USDT (TRC-20) deposit address plus a small test deposit reveals the sweep address. Costs a few
   USDT and fees; outward-facing, so only with the team's OK.

## Plan (fixed before any on-chain data is downloaded)
- **Data.** USDT TRC-20 transfers to and from the S1 addresses, 1 May – 30 Sep 2026, from TronGrid
  (`https://api.trongrid.io/v1/accounts/{address}/transactions/trc20`, works without a key at low rates; check the USDT
  contract address on Tronscan before use). Ethereum only if S1 finds tagged Ethereum addresses and someone provides an
  Etherscan key. Raw files to `data/raw/onchain/` with URL and retrieval date.
- **Measures.** Daily net USDT inflow to Foxbit addresses (UTC days); for the wave (30 Jun – 21 Jul) and the pre window
  (1 May – 22 Jun): inflow by sender type, (a) addresses tagged as other exchanges, (b) the issuer (Tether), (c) untagged;
  share of large inflows (≥ 100,000 USDT) between 09:00 and 18:00 Brasília.
- **Reading rule.** If wave net inflow is at least half of the 361.9 mn USDT net selling (F-031) and most of it comes from
  (a) or (b), the coins came from abroad by crypto rails: supply was imported on-chain, not drawn from domestic inventory.
  If wave net inflow is under a quarter of it, the coins came from inventory already at Foxbit or off-chain (internal
  transfers, other chains), and this check cannot say more. In between: inconclusive. Either way it does not identify the
  seller or show that it caused the fall.
- **Caveats to carry.** Third-party tags (Arkham, Tronscan) are attributions, not proof of ownership; exchanges use many
  deposit addresses that are swept to a few hot wallets, so a tag list may miss part of the flow; internal transfers inside
  an exchange do not touch the chain.

## Subtasks
- [ ] S1 — Foxbit addresses from an opened source (see Blocker), quoted and registered in `docs/sources.md`
- [ ] S2 — Download transfers (plan above), freeze raw files with checksums
- [ ] S3 — Measures and reading rule; script `scripts/p3_18_onchain.py`
- [ ] S4 — Add the result to F-031 (History and Evidence) or a new finding

## Success criteria
- [ ] Addresses come from an opened, quoted source; none guessed
- [ ] Wave inflow compared with the 361.9 mn USDT net selling under the rule above, with the command that reproduces it

## Outputs
- `scripts/p3_18_onchain.py`, `data/raw/onchain/`, `results/tables/P3-18_*.csv`, update to `findings/F-031-who-traded-the-fade.md`

## Handoff
- **State:** plan written; blocked on S1 (no keyless, citable source for Foxbit's wallet addresses).
- **Next step:** option 2 (free Tronscan key in `.env`, then search Tronscan tags for Foxbit) or drop; Arkham (option 1) has no
  Tron addresses for Foxbit.
- **Open questions:** which unblock option the team prefers (Renzo). If none before the freeze (Wed 4 Nov), drop the task;
  F-031 already states that the seller and the source of the USDT are unknown.
- **How to resume:** read F-031 and `results/tables/P3-17_daily_flow.csv`; the wave dates and the 361.9 mn figure come
  from `python scripts/p3_17_restoration.py` (line C2).

## Log
- 2026-11-02, agent for Renzo: created from Renzo's approval of the on-chain check; blocked on Foxbit addresses (Arkham 403,
  Tronscan 401, Etherscan 403, no Foxbit proof-of-reserves page)
- 2026-11-02, Renzo with agent: Arkham checked logged in: Foxbit entity has only BTC, no Tron/Ethereum addresses; option 1 closed

## Result
