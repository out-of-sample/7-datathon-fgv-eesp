# Flash Findings — Mentor leads

**Status:** Exploratory. Five Flash workstreams collected public-source data and leads. Codex audited selected claims against the saved files. The measurements below do not change the submission's frozen results.

## BRLA

- The Polygon Uniswap v3 BRLA/USDC pool (0x0e7754127dedd4097be750825dbb4669bc32c956) showed a wider implied dollar premium versus PTAX during the acute window. The Flash daily-close means reproduce at 54.5, 139.9 and 54.4 bps in the baseline, spike and fade windows. The daily close uses a later price than the PTAX fixing. The 164.9 bps reading on 24 June was the day's reading. The largest saved daily reading in the acute window was 241.8 bps.
- Matching the main study's four hourly opens gives **36.4, 145.9 and 46.6 bps**, an acute increase of **109.6 bps**. This is one pool during the same episode. The calculation assumes USDC is worth USD 1 and does not isolate the BRLA peg or the affected conversion route. Check contemporaneous USDC/USD, raw swaps, depth, a second pool and placebo windows before using this in the deck. The 25 June daily candle high near 654 BRLA/USDC warrants inspection.
- DefiLlama's circulating-supply snapshots labelled 23 and 24 June are 228.0M and 116.6M BRLA. The fall is concentrated on Celo. Historical block-level supply, mint/burn logs, bridge transfers, treasury balances and snapshot timing need reconciliation. Fiat settlement records would be needed to establish redemptions.

## Hyperliquid EWZ

- Trade[XYZ]'s `xyz:EWZ` is a perpetual referencing EWZ. ICE announced a proposed regulated market in October, subject to approvals ([ICE](https://ir.theice.com/press/news-details/2026/Intercontinental-Exchange-and-TradeXYZ-to-Bring-Hyperliquid-Based-Perpetual-Markets-Onshore/default.aspx)).
- Flash's +78 bps compared prices four hours apart. The apparent zero at the 24 June ETF close pairs the daily ETF close with a Hyperliquid candle at 33.85 that recorded zero trades in the hour ending at 20:00 UTC. The saved ETF intraday close is about 33.86. This is a stale-price observation and provides no test of equity spillovers. Use fresh trades or executable quotes and a separate off-hours return design.
- Spot index `@298` is Brila Finance, a different asset from Avenia BRLA. Its snapshot is archived for provenance and must be excluded from Avenia comparisons.

## Coinext

Coinext attributed its retail wind-down to falling short of the regulatory capital requirement for applying for authorization. The sources reviewed provide no link to the 23 June notice. Use this as licensing background. Distinguish application and wind-down provisions from the bank-counterparty restriction in Article 91, which the consolidated rule dates to 6 November. [Coinext FAQ](https://coinext.com.br/suporte/coinext-encerramento-duvidas-frequentes) · [BCB Resolution 520](https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?numero=520&tipo=resolu%C3%A7%C3%A3o+bcb)

## B3, FX and Receita

- Flash collected BCB FX and balance-of-payments series, equity prices and a Yahoo CME BRL futures proxy. B3 dollar futures, investor positions and foreign equity flows were not obtained. The CME file contains OHLC and volume. It cannot identify investor positions.
- The Receita extract ends in June 2026. USDT was 65.6% of the value of purchases and sales for assets listed in Report 4 in that month. Report 1 covers a different reporting universe. Use the workbook to reconcile declaration-type amounts before quoting them. These monthly data cannot identify who bought after the notice or test July substitution.
- Alexandre Ludolf is the likely referral. FGV verifies his co-authorship with Jéfferson Colombo. David can confirm the intended contact. [FGV](https://portal.fgv.br/artigos/tokenizacao-ativos-nova-economia-digital)
- BIS WP 1340 motivates a spillover test. Reuter's IMF WP 2026/211 estimates roughly 30% more cross-border stablecoin activity over the following six months after tighter outflow restrictions. Neither result estimates this Brazilian episode. [BIS](https://www.bis.org/publications/working-paper-1340-stablecoin-flows-and-spillovers-fx-markets) · [Reuter](https://cepr.org/voxeu/columns/stablecoins-vehicle-dollarisation-evidence-capital-controls-and-currency-crises)

## Evidence and handoff

See the [mentor synthesis](mentor-meeting-2026-11-04.md), [data bundle](../data/README.md#flash-mentor-leads-bundle) (raw files in `data/raw/flash-mentor-leads/`, not in git since 5 Nov) and [reproduction finding](../findings/F-034-flash-brla-price-check.md).
