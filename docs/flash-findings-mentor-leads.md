# Flash Findings: Mentor Leads & Empirical Investigation Dossier

**Status:** Confirmed & Verified Data (Exploratory / Mentor Follow-up)  
**Gathered by:** Flash Subagent Fleet (5 specialized agents)  
**Date:** 2026-11-04 / 2026-11-05  
**Context:** Verification of mentor leads (David Wasserman, FGV Datathon) & quantitative checks for the "So What?" project conclusion.  
**Storage Location of Raw Data:** `C:\Users\Felipe\.gemini\antigravity\brain\6be391f7-dc46-42d8-a268-f953dd3fb640\scratch\mentor-leads\`

---

## 1. Executive Summary & Scorecard of Mentor Leads

| Lead | Mentor Hypothesis | Flash Investigation Verdict | Empirical Finding |
|---|---|---|---|
| **Lead 1: Hyperliquid & 24/7 EWZ** | Hyperliquid trades EWZ 24/7; tokenized offshore contract might show flight from Real / price discovery when B3 is closed. | **Verified exists; No 24-Jun depeg** | `xyz:EWZ` was live on 24 Jun 2026. However, when time-matched to the NYSE 16:00 close, the perp basis was **0.0 bps**. 24-hour volume doubled (+95%), but price dislocation was zero. |
| **Lead 2: BRLA Stablecoin (Avenia)** | Asymmetric liquidity squeeze on digital dollars should cause BRLA to decouple from fiat Real (discount/premium). | **STRONGLY CONFIRMED (+85.4 bps jump & -48.9% supply run)** | BRLA/USDC on Uniswap v3 Polygon implied BRL/USD rate jumped from +54.5 bps to +139.9 bps (**+85.4 bps**, peaking at +164.9 bps on 24 Jun). BRLA total supply plunged from **228.0M to 116.6M (-48.9%)** as 111.4M BRLA were burned. |
| **Lead 3: Coinext Closure** | A Brazilian exchange (Coinnext) shut down as a result of the 23 Jun supervisory *ofício*. | **DISPROVEN / Disambiguated** | Coinext announced retail closure on **3 Sep 2026** (effective 15 Oct). Stated reason was failure to meet BCB's **minimum regulatory capital (R$ 10.8M–37.2M)** under SPSAV / Res. 519–521, not the 23 Jun FX *ofício*. |
| **Lead 4: Expert "Ludolf"** | Crypto professor at FGV, ex-QR Asset, Binance & B3 off-hours FX expert. | **100% IDENTIFIED** | **Alexandre Ludolf** (CIO/Partner at QR Asset Management, ex-Transfero/BRZ, FGV professor). Co-author with Prof. Jéfferson Colombo. Contact to be routed via David. |
| **Lead 5: B3 / Macro Spillover & Receita Data** | Secondary effects on dollar futures, macro FX flows, and who bought. | **DOWNLOADED & AUDITED** | RFB crypto declarations (IN 1888/2019) show USDT represents >70% of declared volume. BCB FX flows and B3 series frozen in scratch. |

---

## 2. Detailed Flash Findings by Workstream

### Flash Finding 1: BRLA Dislocation & On-Chain Bank Run (Scratch: `brla/`)
* **Issuer & Architecture:** BRLA is issued by Avenia SPSAV / VASP (CNPJ 50.224.164/0001-70) with 1:1 fiat backing in Tesouro SELIC and bank deposits via Pix 24/7.
* **On-Chain DEX Liquidity:** The primary pool is Uniswap v3 on Polygon (`0x0e77...c956`), which averaged ~$1.0M USDC/day ($27.6M traded during the 4-week acute spike).
* **The Spread Move:**
  - **Pre-Notice Baseline (25 May – 23 Jun):** BRLA-implied BRL/USD traded at a mean premium of **+54.5 bps** over PTAX.
  - **Post-Notice Spike (24 Jun – 21 Jul):** Jumped to a mean of **+139.9 bps** (**+85.4 bps increase**; 24 Jun daily close at **+164.9 bps**).
  - **Fade (22 Jul – 31 Aug):** Returned to **+54.4 bps**.
* **The Liquidity / Supply Contraction:**
  - On 24 June 2026, total BRLA supply experienced an unprecedented contraction from **228.0M BRLA to 116.6M BRLA (-48.9%)**, driven by a 111.4M burn/redemption (primarily on Celo).
* **Takeaway:** This independently mirrors the +93.9 bps USDT/BRL spike. When dollar imports were severed, market participants redeemed BRLA for fiat Reais to buy digital dollars, creating a parallel liquidity squeeze on local stablecoin rails.

### Flash Finding 2: Hyperliquid & EWZ Reality Check (Scratch: `hyperliquid/`)
* **Asset & Protocol:** `xyz:EWZ` is a builder-deployed perpetual contract on Hyperliquid (Trade[XYZ]), settled in USDC with up to 20× leverage. Active since 4 May 2026.
* **The ICE Partnership:** Announced on 29 Oct 2026 (ICE investment in Trade[XYZ] for 24/7 regulated perps). It was not active in June 2026.
* **Data Download:** 4,420 hourly candles and funding rates downloaded (0 gaps).
* **The Price Test:**
  - When comparing Hyperliquid's 24:00 UTC close with NYSE's 20:00 UTC (16:00 NY) close, a naive comparison suggests a +78 bps gap.
  - **When strictly time-matched at 16:00 NY close:** The gap on 24 June 2026 was **0.0 bps** (compared to a median of +8 bps and range of -45 to +163 bps across the year).
* **Takeaway:** The offshore tokenized Brazilian equity market did not experience an acute flight/depeg on 24 June. The shock was strictly confined to foreign exchange and stablecoin on-ramps.

### Flash Finding 3: Coinext Closure Disambiguation (Scratch: `coinnext/`)
* **Timeline of Closure:**
  - Announcement: 3 September 2026 (CEO LinkedIn & public FAQ).
  - Order book trading terminated: 15 October 2026.
  - Crypto withdrawals ceased: 16 October 2026.
  - Compulsory liquidation to BRL: 17 October 2026.
* **Verbatim Stated Cause:**
  > *"A regulamentação brasileira aplicável às prestadoras de serviços de ativos virtuais passou a exigir um capital regulatório mínimo como condição para o pedido de autorização de funcionamento junto ao Banco Central do Brasil. A Coinext não atingiu esse capital mínimo e, nessas condições, não há fundamento econômico que justifique a apresentação do pedido."*
* **Link to 23 Jun Notice:** Zero public sources link Coinext's shutdown to the 23 June supervisory *ofício*. It was caused by the **30 Oct 2026 licensing deadline under Res. BCB 519–521 (R$ 10.8M–37.2M capital requirement)**.
* **Takeaway:** The deck must not claim the 23 June notice shut down Coinext. However, Coinext, NovaDAX (8 Jun), Bitnuvem (29 May), and Digitra (20 Aug) provide valuable macro backdrop showing that 2026 was defined by severe regulatory consolidation that eliminated smaller domestic brokerages.

### Flash Finding 4: Expert Identification (Scratch: `context/`)
* **Identified:** **Alexandre Ludolf** (CIO & Partner, QR Asset Management / QR Capital Group).
* **Background:** Former executive at Transfero (creator of BRZ stablecoin), lecturer at FGV EESP in digital finance/crypto, co-author with Prof. Jéfferson Colombo (*"A tokenização de ativos na nova economia digital"*). Regular writer on B3 vs Binance arbitrage and institutional order flow.
* **Action:** Direct WhatsApp/email contact to be received from David Wasserman for a narrative sanity check.

### Flash Finding 5: Macro & Regulatory Literature Anchors (Scratch: `context/` & `b3-fx/`)
The Flash context agent retrieved five core academic/institutional papers providing theoretical foundations for our conclusion:
1. **Aldasoro, Beltrán & Grinberg (BIS WP 1340, 2026):** Stablecoins transmit into spot FX and cross-currency bases (CIP deviations) in emerging markets.
2. **Reuter (IMF WP/24/211, 2024):** Capital controls lead to an immediate, persistent surge (+30%) in stablecoin usage as "stealth dollarization".
3. **Makarov & Schoar (JFE 2020) & Choi et al. (2022):** Institutional capital controls and banking barriers sustain persistent price premia between crypto and fiat (the Kimchi Premium mechanism).
4. **Hautsch et al. (2019):** Settlement latency creates limits to arbitrage and widens no-arbitrage thresholds (directly supporting our Band-TAR F-021 model).
5. **Lyons & Viswanath-Natraj (JIMF 2023):** Stablecoin pegs are maintained by private arbitrageurs, not issuer stabilization algorithms.

---

## 3. Meeting Synthesis Corrections (Transcripts & Notes)

The verbatim transcript audit revealed essential corrections to earlier draft notes:
1. **The Notice was Not Wholly Secret:** Felipe noted in the team debrief that the *ofício* went to banks on 23 June, then brokerages, and was made public in the press on 24–25 June. The distortion arose because market participants had zero transition window, not because it remained permanently confidential.
2. **David's "So What?" Challenge:** David was constructive and enthusiastic about the project's econometric depth. His challenge was to answer: *Who paid? Who captured the rent? What does this mean for payment rails, on/off-ramps, and market structure?*
3. **Political EWZ Shocks Dropped:** The team mutually agreed to reject political event studies (e.g. 2022 elections) to prevent noise and maintain academic neutrality.

---

## 4. Master Data Inventory in Scratch

All raw scripts and frozen CSVs are preserved in `scratch/mentor-leads/`:
- `hyperliquid/`: `hyperliquid_xyz_ewz_1h.csv`, `ewz_nyse_daily.csv`, `hyperliquid_xyz_ewz_funding.csv`, `report.md`
- `brla/`: `brla_polygon_ptax_merged_daily.csv`, `brla_total_supply_daily.csv`, `ohlcv_polygon_pos_..._day_token.csv`, `report.md`
- `coinnext/`: `report.md` (with 15 primary press links and full regulatory timeline)
- `b3-fx/`: `rfb_crypto_by_asset_monthly.csv`, `rfb_crypto_usdt_share_monthly.csv`, `report.md`
- `context/`: `report.md` (containing full Ludolf biography, academic abstracts, and press citations)
