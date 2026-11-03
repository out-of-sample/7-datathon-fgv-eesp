---
id: F-015
title: The 23 Jun notice cost a buyer of digital dollars about R$ 4,840 per US$ 100k during the spike (+93.9 bps, at each day's PTAX); after it, +11.5 bps (R$ 583) not distinguishable from noise. Bank-route comparisons are now sourced (BCB EE 48/2019 corporate spread 20 bps; statutory IOF by period)
status: confirmed
task: P3-01
date: 2026-11-01
checked_by: Jonathan
---

## Claim
**What the notice cost (the project's headline question).** For someone buying US$ 100,000 in USDT on Binance, converted at each day's PTAX and averaged over the window:
- during the spike, 24 Jun – 21 Jul 2026, the premium was **+93.9 bps** higher, an extra **US$ 939 ≈ R$ 4,842** (PTAX averaged R$ 5.1418; F-016; placebo p ≈ 0.001);
- after the spike, **+11.5 bps (≈ R$ 583)**, which is not distinguishable from ordinary drift (placebo p = 0.24, F-022).

**Context: bank routes (sourced, neutral comparison).** Setting the USDT route (premium + 10 bps fee) beside formal bank FX routes (for either a single slide or a neutral annex table):
- **Bank FX spread:** **20.0 bps** (0.20%), the volume-weighted corporate FX spread across 25.1M primary contracts in BCB *Estudo Especial nº 48/2019* (`R-01`, where the 4th quartile > US$ 55,600 has a 15–25 bps median; a 50 bps upper bound adds R$ 1,614 per US$ 100k). Direct SWIFT wire communication fee is **US$ 25 (2.5 bps)** (`R-01b`, Banco do Brasil *Tabela de Tarifas PJ*: R$ 100 SWIFT event / R$ 440 full online wire order).
- **The IOF in force (`R-02`):** **0%** on goods imports (RIOF Art. 15-B, I); **1.10%** on availability abroad before 23 May 2025 (Dec. 11.153/2022) and on investment remittances after (Dec. 12.467/2025, XXI-A); **3.50%** on general availability abroad from 23 May 2025 (Dec. 12.466/2025, XXI; STF ADC 96 `R-03`).
- **Relative transaction frictions:** in 2020 – May 2025, the USDT route (45.0–101.4 bps) cost R$ 1,673–4,708 less per US$ 100k than the 1.1% IOF bank route (132.5 bps = R$ 7,129; or R$ 3,287–6,322 at a 50 bps bank spread). After May 2025, the pre-notice USDT route (19.4 bps = R$ 1,044) sat well below the 3.5% IOF availability route (372.5 bps = R$ 20,041; or 402.5 bps = R$ 21,655 at 50 bps spread) and close to the 0% IOF import route (22.5 bps = R$ 1,211).
- **Legal and operational non-equivalence (`docs/02-dolar-cripto.md` §10):** a bank FX contract settles sovereign USD with Sisbacen registration and statutory IOF withheld at source (Lei 14.286/2021) and is required for formal customs clearance (Siscomex). Domestic USDT acquisition via Pix is purchase of a virtual asset (Lei 14.478/2022, reported under IN RFB 1.888/2019), carries private issuer and smart-contract risk, and cannot settle formal imports or eFX (Res. BCB 561/2026; BCB LAI response in `E-05`). These figures measure relative frictions across channels, not tax savings to recommend.

## Evidence
Benchmark transaction: institutional acquisition of US$ 100,000; route and scenario rows in R$ at one illustrative reference rate of R$ 5.3800, the Binance USDT/BRL bid of 31 Oct 2026 (`D-10`; not a PTAX), so routes compare on a common basis; the two cost-of-the-notice rows at each day's PTAX (column `fx_basis`). Corporate bank spread: 20.0 bps (`R-01`, BCB EE 48/2019; 50.0 bps sensitivity noted); SWIFT wire fee: US$ 25.00 flat (2.5 bps, `R-01b`). Exchange trading fee: 10.0 bps (Binance VIP0 taker benchmark, `R-04`); on-chain transfer: 0.1 bps (1 USDT flat on TRC-20/TON). Domestic VIP tiers: Foxbit VIP 6–7 (R$ 5M–25M) is 7–9 bps taker (8.0 bps midpoint, `R-05`); Mercado Bitcoin VIP 6.0 bps is the passive *maker* fee (>R$ 10M), while active *taker* for R$ 500k–10M is 60.0 bps (`R-06`).

| Route / Regime / Scenario | Category | Premium (bps) | Spread (bps) | IOF / CIP Carry (bps) | Network / Wire (bps) | Total (bps) | Cost (USD per 100k) | Cost (BRL per 100k) | Diff. vs Bank Avail. in Force (BRL) |
|---|---|---|---|---|---|---|---|---|---|
| **Cost of the notice: spike (24 Jun – 21 Jul 2026)** | **Headline** | **+93.9** | **0.0** | **0.0** | **0.0** | **+93.9** | **$939.10** | **R$ 4,842.04** | — |
| **Cost of the notice: after spike (22 Jul – 30 Oct, p=0.24)** | **Headline** | **+11.5** | **0.0** | **0.0** | **0.0** | **+11.5** | **$115.43** | **R$ 583.10** | — |
| **Bank Import (0% IOF)** | Bank Route | 0.0 | 20.0 | 0.0 | 2.5 | 22.5 | $225.00 | R$ 1,210.50 | R$ 18,830.00 |
| **Bank Investment / Pre-May 2025 Avail. (1.1% IOF)** | Bank Route | 0.0 | 20.0 | 110.0 | 2.5 | 132.5 | $1,325.00 | R$ 7,128.50 | R$ 12,912.00 |
| **Bank Availability Post-May 2025 (3.5% IOF)** | Bank Route | 0.0 | 20.0 | 350.0 | 2.5 | 372.5 | $3,725.00 | R$ 20,040.50 | R$ 0.00 |
| **USDT Regime 1 (Oct 2020 – Jul 2021, vs 1.1% IOF)** | Historical | 91.3 | 10.0 | 0.0 | 0.1 | 101.4 | $1,014.00 | R$ 5,455.32 | R$ 1,673.18 |
| **USDT Regime 2 (Jul 2021 – Aug 2024, vs 1.1% IOF)** | Historical | 54.5 | 10.0 | 0.0 | 0.1 | 64.6 | $646.00 | R$ 3,475.48 | R$ 3,653.02 |
| **USDT Regime 3 (Aug 2024 – Jul 2025, vs 1.1% IOF)** | Historical | 34.9 | 10.0 | 0.0 | 0.1 | 45.0 | $450.00 | R$ 2,421.00 | R$ 4,707.50 |
| **USDT Regime 4: Pre-Notice Baseline (2025–2026, vs 3.5% IOF)** | Historical | 9.3 | 10.0 | 0.0 | 0.1 | 19.4 | $194.00 | R$ 1,043.72 | R$ 18,996.78 |
| **USDT Regime 5: Acute Spike (24 Jun – 21 Jul 2026)** | Historical | 109.1 | 10.0 | 0.0 | 0.1 | 119.2 | $1,192.00 | R$ 6,412.96 | R$ 13,627.54 |
| **USDT Peak Shock (24–25 Jun 2026)** | Historical | 169.9 | 10.0 | 0.0 | 0.1 | 180.0 | $1,799.75 | R$ 9,682.66 | R$ 10,357.84 |
| **USDT Regime 6: After the Spike (Jul–Oct 2026, p=0.24)** | Historical | 26.8 | 10.0 | 0.0 | 0.1 | 36.9 | $369.00 | R$ 1,985.22 | R$ 18,055.28 |
| **USDT Regime 6 (Foxbit VIP 6–7 Taker)** | Domestic Onshore | 26.8 | 8.0 | 0.0 | 0.2 | 35.0 | $350.00 | R$ 1,883.00 | R$ 18,157.50 |
| **USDT Regime 6 (Mercado Bitcoin VIP Maker; Taker=60 bps)** | Domestic Onshore | 26.8 | 6.0 | 0.0 | 0.2 | 33.0 | $330.00 | R$ 1,775.40 | R$ 18,265.10 |
| **Scenario S1: 3.5% Crypto IOF Enacted (E-03)** | Policy Scenario | 26.8 | 10.0 | 350.0 | 0.1 | 386.9 | $3,869.00 | R$ 20,815.22 | -R$ 774.72 |
| **Scenario S2a: 24h Hold Hedged via CIP (Res. 584/2026)** | Policy Scenario | 26.8 | 10.0 | 2.5 | 0.1 | 39.4 | $394.00 | R$ 2,119.72 | R$ 17,920.78 |
| **Scenario S2b: 24h Hold Unhedged (Res. 584/2026)** | Policy Scenario | 26.8 | 10.0 | 0.0 | 0.1 | 36.9 | $369.00 | R$ 1,985.22 | R$ 18,055.28 |

### Scenarios (labelled as such)
- **S1, 3.5% IOF on crypto purchases (`E-03`, unenacted draft):** USDT route rises to **386.9 bps (R$ 20,815)**, matching or exceeding the 3.5% bank route (372.5 bps at 20 bps bank spread, or 402.5 bps at 50 bps bank spread).
- **S2, 24 h precautionary hold (Res. BCB 584/2026, effective 1 Jan 2027, `R-07`, `F-027`):**
  - **hedged (`S2a`):** **+2.5 bps** (1-day Covered Interest Parity carry $(\text{CDI } 10.75\% - \text{SOFR } 5.00\%)/252 = 2.28\text{ bps}$ plus ~0.22 bps B3 DOL fee, `R-07`); total **39.4 bps (R$ 2,120)**;
  - **unhedged (`S2b`):** **0 bps expected cost**, total **36.9 bps (R$ 1,985)**. Because Art. 2º-B of Res. 142 (added by Res. 584/2026) delays *outgoing* transfers ("transferência de ativo virtual ... para cliente ou terceiro"), the customer already holds USDT during the 24-hour hold: as computed in `P3-13` (`F-027`), 1 business day of Selic financing (13.75% a.a., `SGS 432` = **5.5 bps**) plus 95% 1-day `USDT/USD` risk (**3.7 bps**) totals **~9.1 bps**. (If a buyer were instead exposed to BRL/USD during a 24h hold, the 95% 1-day PTAX risk would be **130 bps**, $1.645 \times \text{sd}$ of daily PTAX log changes in 2025–26, `P1-02`). Risk is reported separately, not added to expected cost.

### Reproduction
```powershell
py scripts/p3_01_costs.py
```
Outputs:
- Table: `results/tables/P3-01_route_costs.csv`
- Chart: `results/figures/P3-01_route_costs.png`

## Caveats
- **Corporate vs Retail Spreads**: BCB *Estudo Especial nº 48/2019* (`R-01`) shows 15–25 bps (20 bps volume-weighted average) for primary corporate contracts > US$ 55,600, whereas BCB *Ranking do VET* covers retail PF operations (150–350 bps). We report 20 bps as the sourced corporate benchmark and note 50 bps (+30 bps = +R$ 1,614 per US$ 100k) as a conservative upper bound.
- **Legal Non-Equivalence**: As detailed above, formal bank FX and domestic USDT purchases have distinct legal, tax, and compliance statuses (`docs/02-dolar-cripto.md` §10).

## Used in deck
Slide 10 ("Quanto custou: R$ 5 mil por US$ 100 mil") of `deck/deck_v1_ptbr.md` and Annex B.5 / C.2 of `deck/annex_v1_ptbr.md` (keeping both presentation options open for the team: Option C on Slide 10 or Option A in Annex B.5).

## History
- 2026-11-03, agent for Renzo (decided by Renzo; Felipe owns F-015): headline rows converted at each day's PTAX, R$ 5,052.36 → R$ 4,842.04 (spike) and R$ 621.00 → R$ 583.10 (after); the R$ 5.38 used until now is a Binance USDT/BRL bid (D-10), not a PTAX, found by the P3-21 review. bps unchanged; route rows keep R$ 5.38, now labelled an illustrative reference rate (option a). Status kept; the conversion needs a re-run by a teammate who did not make it.
- 2026-11-03, Jonathan: independently re-ran `scripts/p3_01_costs.py` from raw data; all 17 route/scenario rows and headline spike cost (+93.9 bps = R$ 5,052.36 per US$ 100k) reproduced exactly; status -> confirmed.
- 2026-11-02, agent for Felipe (P3-01 S6–S7): opened and quoted primary sources for every parameter in `docs/sources.md` (`R-01` BCB Estudo Especial nº 48/2019 20 bps corporate spread median for >US$ 55.6k; `R-01b` Banco do Brasil Tarifas PJ R$ 100 SWIFT / R$ 440 online wire; `R-02` RIOF + Decretos 12.466/12.467; `R-05` Foxbit VIP 6–7 7–9 bps taker; `R-06` MB VIP 6 bps maker vs 60 bps taker; `R-07` 1-day CIP carry 2.5 bps); removed `"economiza R$"` from `P3-01_route_costs.png`; documented legal/operational comparability for both Slide 10 (Option C) and Annex B.5 (Option A)
- 2026-11-02, agent for Renzo (review fixes, on Felipe's behalf, agreed by Renzo): regimes 1–3 compared at the 1.1% IOF then in force (savings R$ 3.3–6.3k, were R$ 16–20k); "cost of the notice" rows added and made the headline; unhedged-hold risk no longer added as a cost; bank spread and hedge cost marked as assumptions; adaptation wording removed; status confirmed → exploratory
- 2026-11-02, Renzo (review, P3-01): arithmetic correct, but regimes 1–3 (2020 – May 2025) are compared with 3.5% IOF although R-02 gives 1.1% then (savings ~5× too high for those regimes); the IOF-savings framing conflicts with prompt.md §10; bank spread, hedge cost and VaR are unsourced constants (VaR is a risk, not a cost). Suggest status exploratory until fixed (tasks/P3-01 → Handoff)
- 2026-11-01, Felipe: Initialized and confirmed finding following completion and verification of `scripts/p3_01_costs.py`, `results/tables/P3-01_route_costs.csv`, and `results/figures/P3-01_route_costs.png`.
