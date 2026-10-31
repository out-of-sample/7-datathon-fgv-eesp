# Project 4 — Forecast-driven treasury allocation

**Status:** not recommended. Kept so that the reasoning is on record and the project can be revived if the
opening briefing points strongly at it.
**Deck title (pt-BR draft):** "Prever o rendimento vale dinheiro? Um mapa de quando mudar de protocolo compensa"

## 1. Question in one line

For a company holding stablecoins, does forecasting lending yields improve where it deposits them, after
transaction costs, compared with simply assuming today's rate persists?

## 2. Plain-English example

$100k earns 4.0% at Aave and 4.5% at Compound. The 0.5% gap is worth about $500 a year, or $1.37 a day. If moving
costs $15 in fees, the switch needs 11 days to break even, and the gap often disappears before then. With $10M
the same switch pays back in about 3 hours. The useful output is a **break-even map**: below a certain size and
gap, never switch; above it, switch when the gap exceeds a threshold.

## 3. Why it is not recommended

- **Our own data already answers the core question.** On the 2025 target, a naive "tomorrow = today" forecast
  (R² 0.776) beat our best interpretable model (R² 0.622). This project bets that forecasts beat persistence;
  the likely result is that they do not.
- **Low novelty.** Yield aggregators and curated vaults (Yearn, Morpho vaults) already automate this.
- **Weak maturity signal.** Same topic and data as 2025, plus a backtest.
- **Low Brazil relevance** unless the user is reframed as a Brazilian firm holding stablecoin receivables.

## 4. If revived: the mature version

Lead with the measurement, not the model race.

1. **Break-even map** over capital size × rate gap × chain (Ethereum mainnet vs a layer-2 network with near-zero
   fees). On the layer-2 network switching is almost free, which isolates whether forecasts carry value.
2. **Venues:** Aave V3 USDC, Compound V3 USDC, and one tokenized T-bill fund with an on-chain NAV
   (e.g., BUIDL, USYC or OUSG; eligibility and redemption rules `[verify]`). Continues 2025's SOFR comparison
   with an investable product.
3. **Real-world benchmark:** the realised share-price return of an existing curated vault (ERC-4626). "Does a
   three-line rule match what deployed products earned?"
4. **Policies compared** on identical dates, costs and cash obligations: hold; chase the highest APY;
   cost-aware persistence; cost-aware trailing average; learned forecast.

## 5. Data

| Need | Source | Status |
|---|---|---|
| Supplier index / realised return | Aave `ReserveDataUpdated` events (liquidity index) via Dune; Compound III supply index via contract reads | `[verify]` |
| Quoted APY, TVL | DeFiLlama (already used in 2025) | In hand for 2023–2025 |
| Gas cost per operation | Historical gas price × estimated gas units per supply/withdraw | 2025 repo has a gas series |
| Tokenized T-bill NAV | Issuer pages or on-chain | `[verify]` |
| Vault share price | ERC-4626 `convertToAssets` history via Dune | `[verify]` |

## 6. Method

1. Daily decision at a fixed time, using only data available then.
2. Target: realised 7-day supplier return per venue (from the index, not the quoted APY).
3. Forecasts: persistence, trailing mean, one regularised regression. Walk-forward, with a 7-day purge at split
   boundaries.
4. Policy: compare expected dollar gain over the horizon with the one-time switch cost; include "do nothing".
5. Ledger: every simulated trade, fee and payment recorded; manual check of one switch.
6. Primary metric: paired difference in net earnings versus cost-aware persistence.

## 7. Go / no-go

If the learned forecast does not beat persistence on validation data by Mon 2 Nov, stop forecasting and
deliver the break-even map plus the vault benchmark as the result.

## 8. Salvage value for the active project

The naive-baseline table belongs in the "Lições de 2025" slide (see `README.md`), whichever project is chosen.
