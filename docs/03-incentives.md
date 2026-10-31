# Project 3 — How much of DeFi yield is subsidy, and does subsidised capital stay?

**Status:** (a) a 10-minute check feeding one "Lições de 2025" slide (do it now); (b) the full study is the
fallback if project 2 (the primary) fails its go/no-go on Sun 1 Nov.
**Deck title (pt-BR draft):** "Juros ou propaganda? Quanto do rendimento DeFi é subsídio e quanto capital fica quando ele acaba"

## 1. Question in one line

How much deposit does $1 of token incentives buy, and how much of it leaves when the incentives end?

## 2. Plain-English example

Pool X pays $1M in token rewards over 30 days. Deposits rise from $50M to $90M. A similar pool with no rewards
grows from $50M to $55M over the same month, so roughly $35M is attributable to the campaign. Two weeks after
rewards end, pool X is back at $58M. Result: $1M bought about $35M of deposits, and about 75% of it left within
two weeks ("mercenary capital").

## 3. The link to 2025 (do this first, either way)

Last year's code (`src/DefiLlama/search.py` in the 2025 repo) used DeFiLlama's `apy` column, which is
**base interest + token rewards**. If Compound's COMP rewards were included, part of the "risk spread" we
modelled was promotional spending, not a risk premium.

**10-minute check:** pull `apyBase` and `apyReward` for the 2025 pools from the DeFiLlama chart endpoint and
compute the reward share of the spread over 2023–2025. Result → one slide: "X% do spread de 2025 era subsídio".

## 4. Hypotheses (full study)

- **H1:** deposits rise when incentives start and fall when they end, relative to comparable pools without changes.
- **H2:** retention after the end is lower in pools whose yield depended more on rewards.
- **H0:** deposit changes around incentive changes are no different from comparable pools.

## 5. Data

| Need | Source | Status |
|---|---|---|
| Daily `tvlUsd`, `apy`, `apyBase`, `apyReward` per pool | DeFiLlama yields API: `https://yields.llama.fi/pools` (pool ids), `https://yields.llama.fi/chart/{pool}` | Documented; per-pool coverage `[verify]` |
| Incentive start/end dates | Compound governance (reward-speed changes executed on-chain), Aave governance forum, Merkl campaign data, Arbitrum STIP/LTIPP records | `[verify]` each source |
| Exact reward-speed changes (best case) | Compound III configurator events / governance proposals on Dune or Etherscan | `[verify]` |

**Design advantage:** use **stablecoin pools** (USDC, USDT). Their USD TVL is approximately their token
quantity, so crypto price moves do not contaminate the deposit measure.

## 6. Method

1. **Event list.** Incentive starts, cuts and ends with dates known at the time (`known_at` separate from
   `effective_at`). Several pools changed by one announcement count as one event cluster.
2. **Outcome.** Log deposits at +7, +14 and +30 days relative to the day before the event.
3. **Controls.** Same-asset pools on the same chain without a change in the window; market controls
   (total stablecoin supply, ETH return).
4. **Estimation.** Event study / difference-in-differences with pool and date fixed effects; standard errors
   clustered by event; placebo dates.
5. **Metrics.** Cost per incremental dollar-day of deposits; half-life of incentive-driven deposits after
   the end.
6. **Baselines.** Raw before/after change (no control) versus the matched control. The matched estimate is
   the result.

## 7. Headline chart

Average deposits (indexed to 100 on the event day) for treated vs control pools, from −30 to +30 days around
incentive ends, with confidence bands.

## 8. Day-1 test (only if needed as fallback)

Find at least 8 dated incentive changes on stablecoin pools with DeFiLlama history covering ±30 days.
Fewer than 8 → not viable as a standalone project.

## 9. Schedule (if promoted to primary)

| Date | Work |
|---|---|
| Sat 31 Oct | Event list; pool ids; history download |
| Sun 1 – Mon 2 Nov | Controls matched; event-study v1 |
| Tue 3 Nov | Robustness (placebos, windows, leave-one-protocol-out) |
| Wed 4 Nov | Freeze |
| Thu 5 – Sun 8 Nov | Deck, review, submit (same as the primary) |

## 10. Risks

| Risk | Mitigation |
|---|---|
| Incentives respond to outflows (reverse causality) | Prefer scheduled ends announced in advance; check pre-trends |
| Capital moves to another pool, not out of DeFi | Measure protocol-level and chain-level flows as well |
| `apyReward` missing ≠ zero | Treat missing as unknown; drop or verify |
| Jury unfamiliar with liquidity mining | One diagram slide; analogy: promotional rates on bank deposits |

## 11. Literature anchors

- Liquidity-mining / yield-farming papers `[verify specific references]`.
- BIS work on DeFi lending participation and outside options (cited in the earlier comparison document) `[verify]`.
