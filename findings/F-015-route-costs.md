---
id: F-015
title: The 23 Jun notice cost a buyer of digital dollars about R$ 5,050 per US$ 100k during the spike (+93.9 bps); after it, +11.5 bps (R$ 620) not distinguishable from noise. Bank-route comparisons depend on IOF and on an assumed 50 bps bank spread
status: exploratory
task: P3-01
date: 2026-11-01
checked_by: -
---

## Claim
**What the notice cost (the project's question).** For someone buying US$ 100,000 in USDT on Binance (PTAX R$ 5.38):
- during the spike, 24 Jun – 21 Jul 2026, the premium was 93.9 bps higher, an extra
  **US$ 939 ≈ R$ 5,052** (F-016; placebo p ≈ 0.001);
- after it, +11.5 bps (≈ R$ 621), which is not distinguishable from ordinary
  drift (F-022).

**Context: bank routes.** The table also sets the USDT route (premium + 10 bps fee) beside bank FX routes:
- **Bank FX routes:** 50 bps spread (an assumption; the VET data are not downloaded) + wire + the IOF in force.
- **The IOF in force:** 1.1% on transfers to one's own account abroad before 23 May 2025, 3.5% after (R-02).
- **The USDT route was cheaper in every period:** by R$ 3.3k–6.3k per US$ 100k in 2020 – mid-2025 (vs 1.1% IOF), and by
  about R$ 20k after May 2025 (vs 3.5%).
- **Not verified:** whether the USDT route is a lawful substitute for an FX transfer, and its tax treatment. The 23 Jun
  notice is reported to target exactly this use (E-05). So these differences describe price gaps; they are not savings
  to recommend (`prompt.md` §10). Whether the bank comparison appears in the deck at all is a team decision.

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

### Scenarios (labelled as such)
- **S1, 3.5% IOF on crypto purchases (E-03, unenacted):** USDT route ≈ 387 bps, about the same as the 3.5% bank route.
- **S2, 24 h hold (Res. BCB 584/2026, from 1 Jan 2027):**
  - hedged: + 10 bps (assumed hedge cost, no source);
  - unhedged: no expected cost, but a 95% one-day exchange-rate risk of about 130 bps (1.645 × sd of daily PTAX changes,
    2025–26). A risk, not added to the cost.

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
- 2026-11-02, agent for Renzo (review fixes, on Felipe's behalf, agreed by Renzo): regimes 1–3 compared at the 1.1% IOF then in force (savings R$ 3.3–6.3k, were R$ 16–20k); "cost of the notice" rows added and made the headline; unhedged-hold risk no longer added as a cost; bank spread and hedge cost marked as assumptions; adaptation wording removed; status confirmed → exploratory
- 2026-11-02, Renzo (review, P3-01): arithmetic correct, but regimes 1–3 (2020 – May 2025) are compared with 3.5% IOF although R-02 gives 1.1% then (savings ~5× too high for those regimes); the IOF-savings framing conflicts with prompt.md §10; bank spread, hedge cost and VaR are unsourced constants (VaR is a risk, not a cost). Suggest status exploratory until fixed (tasks/P3-01 → Handoff)
- 2026-11-01, Felipe: Initialized and confirmed finding following completion and verification of `scripts/p3_01_costs.py`, `results/tables/P3-01_route_costs.csv`, and `results/figures/P3-01_route_costs.png`.
