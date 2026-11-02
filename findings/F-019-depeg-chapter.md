---
id: F-019
title: In dollars too, a stablecoin left parity while its redemption channel was closed: USDC closed at $0.863 on the SVB weekend and was back at $0.989 an hour after Sunday's deposit guarantee, before banks reopened; 11 other falls below $1 form a case table (too few for curves)
status: exploratory
task: P3-04
date: 2026-11-02
checked_by: -
---

## Claim
The dollar side shows the same pattern as the BRL premium, described here, not tested: a price leaves parity when the
channel that enforces it is closed.
- **SVB weekend (USDC, Bitstamp USDC/USD).** US banks were closed from Fri 16h to Mon 9h30 (New York). USDC's lowest
  hourly close was **$0.863** (Sat 11 Mar 2023, 07h UTC; intra-hour low $0.805). The joint Treasury/Fed/FDIC deposit
  guarantee was released at 22:15 UTC on Sunday (D-13). USDC closed that hour at **$0.989**, before banks reopened. The
  last step, to $0.999, came at Monday's opening.
- **The other 11 falls below $1 (P1-07 v2, F-013).** Too few for Kaplan–Meier curves (the rule needs ≥ 12), so they form
  a case table. In these cases:
  - the two that started on the closed banking weekend (USDC, USDP) recovered within 51–65 h;
  - the one coin without external reserves (UST, May 2022) never recovered;
  - the others took 21 h to 2,719 h.

  The categories were assigned after seeing the cases (n = 2 / 7 / 1 / 2), so this is a description, not evidence that
  backing "determines" recovery. The cause of each case is not yet sourced
  (`mechanism_lead_unsourced` in the case table).

## Evidence

### 1. SVB Weekend Timeline (Bitstamp USDC/USD OHLC 1h)
The canonical case study measures USDC directly against the US dollar on Bitstamp (`results/figures/P3-04_svb_weekend.png`):
- **Friday 10 Mar 2023, 21:00 UTC**: US banking hours close (16:00 New York); Circle announces $3.3B stuck at SVB; USDC drops below $0.995.
- **Saturday 11 Mar 2023, 07:00 UTC**: USDC touches intra-hour low of **US$ 0.805** and closes at **US$ 0.863** (1,370 bps discount on close; 1,950 bps intra-hour).
- **Sunday 12 Mar 2023, 21:00 UTC**: Secondary market consolidates at US$ 0.968.
- **Sunday 12 Mar 2023, 22:15 UTC**: Joint Statement by Department of the Treasury, Federal Reserve, and FDIC guaranteeing all SVB deposits.
- **Sunday 12 Mar 2023, 23:00 UTC**: Price surges to **US$ 0.989** (arbitrageurs buy anticipating Monday wire redemptions).
- **Monday 13 Mar 2023, 12:00 UTC**: USDC trades at **US$ 0.991** before US banks open.
- **Monday 13 Mar 2023, 14:00 UTC**: Full recovery to **US$ 0.999** as primary redemptions resume.

### 2. The 11 USD-Confirmed Downward Depeg Events
Filtered from `results/tables/P1-07_v1_vs_v2.csv` (`direction == "below"` and `classification_v2 == "USD-confirmed"`):

| Event ID | Coin | Category | Start Date (UTC) | End Date (UTC) | Duration (h) | Trough (USD) | Max Dev (bps) | Recovery Status | Core Mechanism |
|---|---|---|---|---|---|---|---|---|---|
| **CASE-USDC-SVB** | USDC | Cat 1 | 2023-03-10 21:00 | 2023-03-13 14:00 | 65.0 | $0.863 | 1,370.0 | Recuperado | SVB receivership + weekend bank closure; recovered on FDIC guarantee |
| **P1-07-USDPUSDT-02** | USDP | Cat 1 | 2023-03-11 14:00 | 2023-03-13 17:00 | 51.0 | $0.974 | 261.1 | Recuperado | SVB weekend contagion fear (Signature deposits); recovered Monday |
| **P1-07-USTUSDT-01** | UST | Cat 2 | 2022-01-28 10:00 | 2022-01-29 07:00 | 21.0 | $0.990 | 101.0 | Recuperado | DeFi liquidation cascade (MIM); market arbitrage restored peg |
| **P1-07-TUSDUSDT-11** | TUSD | Cat 2 | 2024-01-12 16:00 | 2024-02-29 08:00 | 1,144.0 | $0.954 | 464.7 | Recuperado | Redemption operational delays & Binance fee promo shift |
| **P1-07-FDUSDUSDT-04** | FDUSD | Cat 2 | 2024-03-05 18:00 | 2024-03-10 23:00 | 125.0 | $0.991 | 94.8 | Recuperado | Flash market volatility; 1:1 primary redemption cleared discount |
| **P1-07-TUSDUSDT-13** | TUSD | Cat 2 | 2024-10-03 16:00 | 2024-11-10 01:00 | 897.0 | $0.992 | 85.0 | Recuperado | Thin secondary liquidity post-fee changes; slow banking arbitrage |
| **P1-07-TUSDUSDT-14** | TUSD | Cat 2 | 2024-11-14 04:00 | 2024-11-18 15:00 | 107.0 | $0.992 | 80.1 | Recuperado | Post-US election market volatility; rapid return to parity |
| **P1-07-FDUSDUSDT-07** | FDUSD | Cat 2 | 2025-04-02 15:00 | 2025-04-23 03:00 | 492.0 | $0.965 | 349.2 | Recuperado | Custodian insolvency rumors; attestations & redemptions proved par |
| **P1-07-TUSDUSDT-16** | TUSD | Cat 2 | 2025-06-11 00:00 | 2025-10-02 07:00 | 2,719.0 | $0.986 | 139.3 | Recuperado | Low-volume secondary trading; absorbed through slow issuer burns |
| **P1-07-USTUSDT-03** | UST | Cat 3 | 2022-05-07 21:00 | Censored | N/A | $0.245 | 7,547.1 | Não recuperado | Insolvent death spiral: Anchor run, LUNA hyperinflation, zero reserves |
| **P1-07-USDPUSDT-09** | USDP | Cat 4 | 2026-09-15 16:00 | 2026-09-18 04:00 | 60.0 | $0.994 | 58.1 | Recuperado | Pre-delisting secondary drift on Binance; recovered before halt |
| **P1-07-USDPUSDT-10** | USDP | Cat 4 | 2026-09-23 17:00 | Censored | N/A | $0.988 | 120.0 | Não recuperado | Terminal trading halt on Binance; censored at dataset end |

*Note: CASE-USDC-SVB is evaluated from Bitstamp direct USDC/USD 1h data (P1-07 v2); P1-07 automated candidates derive from Binance stablecoin/USDT adjusted by Coinbase direct USDT/USD.*

### 3. Summary by Economic Category
From `results/tables/P3-04_category_summary.csv`:

| Category | N | Stablecoins | Recovery Rate | Median Duration (Recovered) | Trough Price Range | Core Economic Mechanism |
|---|---|---|---|---|---|---|
| **1. Weekend / Redemption-Gate Closure** | 2 | USDC, USDP | 100% | 58h (51h–65h) | $0.863 – $0.974 | Arbitrage blocked by bank hours; par restored instantly once redemption is guaranteed |
| **2. Frictions de Liquidez / Operacionais** | 7 | UST, TUSD, FDUSD | 100% | 492h (21h–2,719h) | $0.954 – $0.992 | Solvency preserved; operational frictions delay arbitrage but parity is preserved |
| **3. Colapso Algorítmico / Insolvência** | 1 | UST | 0% | N/A (Terminal) | $0.000 – $0.245 | Complete balance-sheet insolvency; death spiral with zero external reserves |
| **4. Fim dos dados na Binance (deslistagem a verificar)** | 2 | USDP | 50% | 60h | $0.988 – $0.994 | Secondary order-book thinning driven by planned exchange delisting |

### 4. Reproduction
```powershell
py scripts/p3_04_depeg_chapter.py
```
Generated artifacts:
- `results/tables/P3-04_depeg_case_table.csv`
- `results/tables/P3-04_category_summary.csv`
- `results/figures/P3-04_svb_weekend.png`
- `results/figures/P3-04_depeg_cases.png`

## Caveats
1. **Sample Size & Kaplan-Meier Pre-Commitment**: The screening criteria yielded 11 independent downward events (9 excluding pre-delisting drift; 8 excluding terminal collapse). Because this is strictly below the pre-specified threshold of $n \ge 12$, Kaplan-Meier survival curves and Cox proportional hazard regressions were not run, as doing so would pool wildly heterogeneous economic mechanisms (insolvency vs weekend illiquidity) under insufficient degrees of freedom.
2. **Binance Mid-Weekend Relisting**: USDC/USDT spot pairs on Binance were temporarily suspended and relisted during the peak of the SVB weekend, requiring direct Bitstamp USDC/USD data for the case study figure.
3. **Dual-Venue Dollar Adjustment**: Converting Binance stablecoin/USDT into direct dollar prices via Coinbase USDT/USD introduces minor multi-venue noise (within $\pm 10$ bps), slightly widening measured recovery times inside the 0.1% recovery band for FDUSD in April 2025.

## Used in deck
Recommended for Slide 13 ("O mesmo mecanismo em dólares: o fim de semana do SVB") and Slide 14 ("Anatomia dos depegs: por que resgate e solvência importam") of the final presentation deck.

## History
- 2026-11-02, agent for Renzo (review fixes, on Felipe's behalf, agreed by Renzo): title and claim rewritten as description (no "confirms"/"proving"); SVB in hourly closes with D-13 timing; case causes marked unsourced in the table (kept as leads); category 4 renamed pending a delisting source
- 2026-11-02, Renzo (review, P3-04): reproduces with the v2 events. Requested: sources for each case's mechanism (none in sources.md); title/claim as description, not "confirm"/"proving" (n = 2/7/1/2, categories assigned after the fact); USDP delisting still [verify] (tasks/P3-04 → Handoff)
- 2026-11-02, Felipe (Economist): created (exploratory) following execution of P3-04, incorporating the 11-event v2 screen, pre-committed KM threshold gate check ($11 < 12$), SVB weekend Bitstamp timeline, and 4-category comparative taxonomy.
