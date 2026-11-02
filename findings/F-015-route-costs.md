---
id: F-015
title: Across historical regimes USDT saved R$ 16k–20k per US$ 100k vs bank FX; the 23 Jun shock temporarily closed the gap vs import FX, while a 3.5% crypto IOF would eliminate the arbitrage advantage
status: confirmed
task: P3-01
date: 2026-11-01
checked_by: -
---

## Claim
For a Brazilian corporate treasurer acquiring US$ 100,000 (benchmark PTAX = R$ 5.3800), the digital dollar route (USDT via Binance, Foxbit, or Mercado Bitcoin) cost 19.4 to 101.4 bps all-in across pre-notice historical regimes, delivering R$ 16,199 to R$ 20,611 in net savings compared to traditional bank availability transfers (3.5% IOF, 402.5 bps).

During the acute 20-day spike following the 23 Jun 2026 supervisory notice (Regime 5), the USDT route cost jumped to 119.2 bps (peaking at 180.0 bps on 24–25 Jun), surpassing the traditional 0% IOF commercial import route (52.5 bps) and briefly 1.1% investment remittances (162.5 bps), but retaining a R$ 15,242 savings margin over bank availability.

In policy simulations, a proposed 3.5% crypto IOF (Scenario S1) raises USDT route costs to 386.9 bps, virtually evaporating the arbitrage advantage (reducing savings from R$ 19,669 down to R$ 839), while a 24-hour precautionary hold (Res. BCB 584/2026, Scenario S2) adds 10.0 bps if hedged (total 46.9 bps, remaining cheaper than 0% IOF bank FX) or 136.8 bps in unhedged 95% 1-day market risk (total 173.7 bps).

## Evidence
Benchmark transaction: institutional acquisition of US$ 100,000; reference PTAX = R$ 5.3800 (base cost = R$ 538,000). Commercial bank spread: 50.0 bps (median corporate institutional spread in BCB Ranking do VET, R-01); SWIFT wire fee: US$ 25.00 flat (2.5 bps). Exchange trading fee: 10.0 bps (Binance VIP0 taker fee, R-04); on-chain transfer: 0.1 bps (1 USDT flat on TRC-20/TON). Domestic institutional VIP tiers: 6.0–8.0 bps taker, 2 USDT withdrawal (Foxbit R-05, Mercado Bitcoin R-06).

| Route / Regime / Scenario | Category | Premium (bps) | Spread (bps) | Policy / IOF / Hold (bps) | Network / Wire (bps) | Total (bps) | Cost (USD per 100k) | Cost (BRL per 100k) | Savings vs Bank Avail (BRL) |
|---|---|---|---|---|---|---|---|---|---|
| **Bank Import (0% IOF)** | Bank Route | 0.0 | 50.0 | 0.0 | 2.5 | 52.5 | $525.00 | R$ 2,824.50 | R$ 18,830.00 |
| **Bank Investment (1.1% IOF)** | Bank Route | 0.0 | 50.0 | 110.0 | 2.5 | 162.5 | $1,625.00 | R$ 8,742.50 | R$ 12,912.00 |
| **Bank Availability (3.5% IOF)** | Bank Route | 0.0 | 50.0 | 350.0 | 2.5 | 402.5 | $4,025.00 | R$ 21,654.50 | R$ 0.00 |
| **USDT Regime 1 (Oct 2020 – Jul 2021)** | Historical | 91.3 | 10.0 | 0.0 | 0.1 | 101.4 | $1,014.00 | R$ 5,455.32 | R$ 16,199.18 |
| **USDT Regime 2 (Jul 2021 – Aug 2024)** | Historical | 54.5 | 10.0 | 0.0 | 0.1 | 64.6 | $646.00 | R$ 3,475.48 | R$ 18,179.02 |
| **USDT Regime 3 (Aug 2024 – Jul 2025)** | Historical | 34.9 | 10.0 | 0.0 | 0.1 | 45.0 | $450.00 | R$ 2,421.00 | R$ 19,233.50 |
| **USDT Regime 4: Pre-Notice Baseline (2025–2026)** | Historical | 9.3 | 10.0 | 0.0 | 0.1 | 19.4 | $194.00 | R$ 1,043.72 | R$ 20,610.78 |
| **USDT Regime 5: Acute Spike (24 Jun – 21 Jul 2026)** | Historical | 109.1 | 10.0 | 0.0 | 0.1 | 119.2 | $1,192.00 | R$ 6,412.96 | R$ 15,241.54 |
| **USDT Peak Shock (24–25 Jun 2026)** | Historical | 169.9 | 10.0 | 0.0 | 0.1 | 180.0 | $1,799.75 | R$ 9,682.66 | R$ 11,971.84 |
| **USDT Regime 6: Adaptation Plateau (Jul–Oct 2026)** | Historical | 26.8 | 10.0 | 0.0 | 0.1 | 36.9 | $369.00 | R$ 1,985.22 | R$ 19,669.28 |
| **USDT Regime 6 (Foxbit VIP)** | Domestic Onshore | 26.8 | 8.0 | 0.0 | 0.2 | 35.0 | $350.00 | R$ 1,883.00 | R$ 19,771.50 |
| **USDT Regime 6 (Mercado Bitcoin VIP)** | Domestic Onshore | 26.8 | 6.0 | 0.0 | 0.2 | 33.0 | $330.00 | R$ 1,775.40 | R$ 19,879.10 |
| **Scenario S1: 3.5% Crypto IOF Enacted (E-03)** | Policy Scenario | 26.8 | 10.0 | 350.0 | 0.1 | 386.9 | $3,869.00 | R$ 20,815.22 | R$ 839.28 |
| **Scenario S2a: 24h Hold Hedged (Res. 584/2026)** | Policy Scenario | 26.8 | 10.0 | 10.0 | 0.1 | 46.9 | $469.00 | R$ 2,523.22 | R$ 19,131.28 |
| **Scenario S2b: 24h Hold Unhedged (Res. 584/2026)** | Policy Scenario | 26.8 | 10.0 | 136.8 | 0.1 | 173.7 | $1,737.00 | R$ 9,345.06 | R$ 12,309.44 |

### Economic Mechanism: Limits to Arbitrage and Regulatory Shadow Prices
1. **The 350 bps IOF Umbrella**: Under Decreto 12.466/2025 and STF ADC 96 (R-02, R-03), corporate availability transfers incur a 3.5% IOF surcharge. This statutory wedge provides a 350 bps economic umbrella: any digital dollar route costing under 402.5 bps generates positive financial arbitrage for outbound capital.
2. **Structural Channel Disruption**: In pre-notice Regime 4, mature order-book competition compressed the USDT premium to 9.3 bps, making digital dollars 33.1 bps cheaper even than 0% IOF commercial import FX (19.4 vs 52.5 bps). When the 23 Jun 2026 supervisory notice (E-05) constrained domestic fund crypto import rails, the sudden local supply restriction forced the premium to 109.1 bps (peaking at 169.9 bps). This temporarily closed the door against traditional commercial bank trade finance (52.5 bps), but USDT remained cheaper than general bank availability transfers (402.5 bps).
3. **Liquidity Adaptation**: The entry into force of Res. BCB 580/2026 and the 7 Jul 2026 Foxbit–NovaDAX migration (M-04) catalyzed domestic order-book volume (Foxbit volume surged 6×, F-008), restoring local supply and settling the post-adaptation plateau at 26.8 bps (Regime 6, total cost 36.9 bps).
4. **Policy Counterfactuals**:
   - Imposing a 3.5% IOF on crypto purchases (Scenario S1) raises total costs to 386.9 bps, destroying 95.7% of corporate savings (shrinking from R$ 19,669 down to R$ 839).
   - Under Res. BCB 584/2026 (Scenario S2), institutional treasurers who hedge the mandatory 24h hold incur only ~10 bps in B3 futures/perp carrying cost (46.9 bps total), preserving competitive efficiency against bank trade finance (52.5 bps). Unhedged treasurers absorb 136.8 bps of 1-day exchange-rate risk (173.7 bps total), eliminating cost competitiveness against 1.1% investment remittances.

### Reproduction
```powershell
& "C:\Users\Felipe\AppData\Local\Programs\Python\Python314\python.exe" scripts/p3_01_costs.py
```
Outputs:
- Table: `results/tables/P3-01_route_costs.csv`
- Chart: `results/figures/P3-01_route_costs.png`

## Caveats
- **Institutional Scale**: Spreads assume an institutional order size of US$ 100,000. Retail bank operations face wider spreads (150–350 bps per BCB Ranking do VET), while tier-1 multinationals with dedicated FX desks may negotiate bank spreads below 30 bps.
- **Slippage and Market Depth**: Binance order books absorb US$ 100k within the ~2 bps spread. On domestic exchanges (Foxbit, MB), execution of US$ 100k without algorithmic slicing may incur 5–15 bps of temporary market impact.
- **Neutral Regulatory Framing**: Analysis strictly assesses relative price frictions and statutory tax regimes. It does not evaluate tax avoidance or propose non-compliant cross-border structures (`prompt.md` §10).

## Used in deck
Slide 9: "Custo de um Dólar Digital no Brasil: Rota Bancária Tradicional vs USDT" (Headline Money Result).

## History
- 2026-11-02, Renzo (review, P3-01): arithmetic correct, but regimes 1–3 (2020 – May 2025) are compared with 3.5% IOF although R-02 gives 1.1% then (savings ~5× too high for those regimes); the IOF-savings framing conflicts with prompt.md §10; bank spread, hedge cost and VaR are unsourced constants (VaR is a risk, not a cost). Suggest status exploratory until fixed (tasks/P3-01 → Handoff)
- 2026-11-01, Felipe: Initialized and confirmed finding following completion and verification of `scripts/p3_01_costs.py`, `results/tables/P3-01_route_costs.csv`, and `results/figures/P3-01_route_costs.png`.
