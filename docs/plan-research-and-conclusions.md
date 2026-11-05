# Strategic Plan: Research Leads & Project Conclusion Synthesis

**Document:** `docs/plan-research-and-conclusions.md`  
**Created:** 2026-11-04  
**Author:** Felipe (Economist / Deck Owner, Team *Out of Sample*)  
**Trigger:** Post-mentoring debrief with David Wasserman (FGV EESP / ex-QR Asset)  
**Target Deadline:** Submission on Sunday, 2026-11-08 (20:00 Brasília) | Rehearsal: Sat 2026-11-07  

---

## 1. Executive Context & The "So What?" Diagnosis

In our mentoring session on 4 Nov, David Wasserman validated our econometric core:
* The +93.9 bps spike on 24 June 2026 is clean, causal, robust across 22 specifications, replicated on 3 exchanges (Binance, Foxbit, Mercado Bitcoin), and confirmed by official BCB macro data (−78% stablecoin imports).
* **The Fatal Vulnerability:** The project currently risks losing first place because its ending is too defensive. Slide 10 currently states *"the effect faded for reasons we do not identify"* and lists three future predictions that do not resolve before Sunday.
* **The Mentor's Direct Challenge:** *"A conclusão está fazendo todo o heavy lifting. Se não tiver uma conclusão bombástica e tangível sobre o que isso significa para o sistema financeiro, rails on/off-ramp e desenho regulatório, o projeto fica parecendo apenas um exercício econométrico descritivo."*

This document outlines:
1. **Triaged Research Leads:** What to investigate in the remaining 48 hours vs. what to deliberately drop.
2. **Three Cohesive Conclusion Architectures:** Three alternative ways to tie the whole paper together into an undeniable, thesis-driven contribution.
3. **Deck Slide 10 Overhaul:** Exact proposed replacement copy for the presentation.
4. **Execution Roadmap:** Step-by-step tasks leading up to the Saturday rehearsal with David.

---

## 2. Evaluation & Triaging of Mentor Leads

| Lead / Idea | Operational Cost | Likelihood of Impact | Action Plan / Verdict |
|---|---|---|---|
| **1. Hyperliquid & 24/7 EWZ** | High (DEX data scraping, EVM index mapping) | Low / High Noise | **DROP (Context only).** The team agreed that exploring elections or political shocks introduces uncontrolled noise and alienates an FGV jury. Hyperliquid will only be cited in Annex F as evidence of offshore tokenized Brazilian risk discovery when B3 is closed. |
| **2. BRLA (Avenia) Stablecoin Depeg** | Medium (pulling DEX pool prices or order books) | **High** | **EXECUTE FAST CHECK.** If domestic on-ramp/off-ramp rails were severely bottlenecked by the 23 Jun notice, the local Real-backed stablecoin (BRLA) should have traded at a dislocation (discount or premium against BRL). If confirmed, this proves the dislocation was in the *fiat/on-chain conversion pipe*, not Tether-specific. |
| **3. Exchange Casualties: Coinnext Exit** | Low (corporate filings, press announcements) | **Very High** | **EXECUTE QUALITATIVE AUDIT.** Document that the elimination of the zero-IOF channel removed the margin buffer of domestic brokerages, accelerating shutdowns (e.g., Coinnext) and driving market concentration toward Binance and institutional B2B infrastructure (Foxbit Infra). |
| **4. Expert Chat: Felipe Ludolf** | Low (30-min WhatsApp / call) | **High** | **SCHEDULE VIA DAVID.** Use Ludolf to sanity-check our narrative on how offshore B2B liquidity bridges order books when domestic banking rails close. |
| **5. Live Prediction: Res. BCB 574 (3 Nov)** | Very Low (`scripts/p3_20_live.py`) | **Critical** | **EXECUTE IMMEDIATELY.** Yesterday (3 Nov) was the enforcement date for Res. 574. Verifying that the premium did *not* jump completes our out-of-sample falsification test before the jury! |

---

## 3. High-Yield Research Tasks (Next 24 Hours)

### Task R-1: The Institutional Fallout (Coinnext & Market Structure)
* **Objective:** Establish the real-world industrial impact of the 23 June notice.
* **Mechanism:** Domestic exchanges operated on razor-thin margins, relying on zero-IOF foreign exchange loops to source digital dollar liquidity for local order books. When BCB issued the immediate supervisory *ofício*, smaller brokerages without foreign credit lines or institutional FX tables could not absorb the 3.5% cost spread or legal liability.
* **Data Sources:** Press coverage of Coinnext shutdown (July–August 2026), ABToken public statements, and CVM/BCB registry records.
* **Deliverable:** 2 sentences in Slide 9/10 and a dedicated paragraph in Annex A documenting that the notice acted as an anti-competitive shock that consolidated retail flow into foreign platforms.

### Task R-2: BRLA Peg Stress Verification
* **Objective:** Test whether local currency stablecoins exhibited dislocation.
* **Mechanism:** In a standard currency board / stablecoin model, 1 BRLA = R$ 1.00. But if arbitrageurs cannot bring dollars into Brazil to mint Tether, capital fleeing to digital dollars creates extreme pressure on domestic fiat off-ramps.
* **Check:** Screen Uniswap v3 / Curve pools (or CoinGecko hourly closes) for BRLA/USDC and BRLA/BRL between 20 June and 15 July 2026.
* **Fallback:** If data is sparse or noisy, state the theoretical hypothesis in Annex B.5 as a testable prediction for local on-ramps.

### Task R-3: Execution of Live Prediction E1 (Res. BCB 574)
* **Objective:** Verify whether the live prediction committed on 3 Nov in `P3-20` (`commit 9a522e9`) held true.
* **Prediction:** Res. BCB 574 (reporting virtual asset transactions) will produce no detectable move outside $[-35, +38]$ bps.
* **Action:** Run `py scripts/p3_20_live.py` with the 3–4 Nov PTAX data. If within the bound, report it on Slide 10 as an executed out-of-sample success.

---

## 4. Three Candidate Conclusions to Tie the Project Together

To answer *"So what?"*, our empirical findings must be structured into an overarching economic thesis. Below are three candidate conclusions. The team can adopt one as the primary narrative on Slide 10:

```
                            THE EMPIRICAL SPINE
               +93.9 bps spike  |  -78% imports (BCB)
               R$ 106-145M transfer  |  26x Band-TAR widening
               Recovery via Foxbit B2B (~362M USDT selling)
                                     │
         ┌───────────────────────────┼───────────────────────────┐
         ▼                           ▼                           ▼
   CONCLUSION 1                CONCLUSION 2                CONCLUSION 3
  "The Private Tariff"       "Limits to Arbitrage"     "The Shadow Macro Rail"
  Regulatory Architecture   Market Microstructure        Capital Flight & FX
  • Secret ofício = Quota   • Parity requires pipes     • Stablecoins are FX
  • Zero Treasury revenue   • Slow-moving capital       • Clamping supply
  • Public rules work         heals the peg               spikes retail costs
```

---

### Candidate 1: The Regulatory Architecture View — *"The Private Tariff"* (Recommended)
> **Core Proposition:** *Regulation by unpublished supervisory decree acts as an unlegislated import quota, transferring hundreds of millions from retail savers to offshore incumbents while collecting zero tax revenue.*

* **The Economic Logic:**
  1. **Quota Equivalence:** Closing the fund channel without warning cut import volume by 78% (BCB data) and raised prices by +94 bps. This is textbook trade theory: a quantity restriction produces an identical price wedge to a tariff.
  2. **Welfare Loss without Public Revenue:** Under a standard 3.5% IOF tariff, the price difference generates fiscal revenue for the Treasury. Under the confidential 23 June *ofício*, the resulting R$ 106M (Binance) to R$ 145M (3 exchanges) surplus was entirely captured by private sellers and foreign market-makers holding pre-existing dollar inventory.
  3. **The Governance Cost:** Why did formal, published normative resolutions (Res. 561, 574, 580, 584) produce **0 bps** of detectable price dislocation, while the confidential *ofício* caused an acute market crisis? Because published rules with transition windows allow market makers to adjust pipelines smoothly. Regulation by sudden administrative decree destroys liquidity and imposes a private tax on residents.
* **Why this wins Datathon FGV:** It speaks directly to policy, regulatory impact analysis (AIR), and public finance.

---

### Candidate 2: The Market Microstructure View — *"Limits to Arbitrage & Slow-Moving Capital"*
> **Core Proposition:** *Digital dollar parity is not an algorithmic property; it is maintained by institutional liquidity pipes. When those pipes are severed, slow-moving capital takes a full month to re-establish market equilibrium.*

* **The Economic Logic:**
  1. **The Fragility of Crypto Parity:** Cryptocurrencies do not stay pegged to the dollar by magic. They require active triangular arbitrage connecting fiat banking rails with on-chain order books.
  2. **Band Widening:** When the BCB severed the zero-IOF fund loop, the no-arbitrage band expanded by 26× (from 1.6 bps to 42.0 bps in our Band-TAR model, `F-021`). 
  3. **The Anatomy of Recovery:** The mentor noted the mystery of why the premium fell back after 22 July. Our repository already solved this: it wasn't regulatory forgiveness (`F-030` confirms BCB never reopened the fund channel). It was **Duffie (2010) Slow-Moving Capital**: once the premium widened past 35 bps, alternative institutional pipes mobilized—proven by the massive 362M USDT seller-initiated volume on Foxbit (`F-031`, `F-032`) and Foxbit’s B2B infrastructure relaunch (`M-05`).
* **Why this wins Datathon FGV:** It demonstrates master-level financial econometrics and order-book microstructure knowledge.

---

### Candidate 3: The Macro-Finance View — *"The Shadow FX Rail"*
> **Core Proposition:** *In an economy with FX friction and asymmetric IOF, stablecoins have evolved into Brazil's shadow foreign exchange conduit. Administrative capital controls do not stop dollar demand; they merely tax the exit door.*

* **The Economic Logic:**
  1. **Scale of Adoption:** Brazilians bought US$ 2.4B/month in foreign stablecoins prior to June 2026. This is not speculative crypto trading; it is institutional and retail dollarization.
  2. **Inelastic Demand:** Even after the channel was blocked, volume on domestic exchanges surged, and buyers paid up to 185 bps premium to acquire dollars.
  3. **Market Casualties:** The supervisory clampdown destroyed domestic on-ramps (accelerating exchange shutdowns like Coinnext) and pushed liquidity into global conglomerates, creating systemic counterparty risk outside the central bank’s direct supervision.
* **Why this wins Datathon FGV:** Connects crypto to macroeconomics, monetary policy, and balance-of-payments statistics.

---

## 5. Proposed Overhaul for Slide 10 (Deck v2)

Replace the passive / defensive Slide 10 in `deck/deck_v2_ptbr.md` with an authoritative, high-impact conclusion:

### Draft: Slide 10 — Conclusão e Implicações de Política
```markdown
<!-- SLIDE 10 -->
## Slide 10 — Conclusão: Quanto Custa Fechar a Porta?

### O ofício sigiloso operou como uma cota de importação privada: encareceu o dólar em R$ 106 milhões sem gerar R$ 1 para o Tesouro, até o capital institucional restabelecer a paridade

#### Pontos Principais (pt-BR)
1. **O Custo da Incerteza Regulatória:**
   - O ofício sigiloso e imediato de 23/jun gerou um prêmio de +94 bps (R$ 4.842 a cada US$ 100 mil) e transferiu R$ 106 milhões dos compradores para vendedores na Binance (R$ 145 milhões em 3 corretoras).
   - Em contraste, as **7 regras normativas públicas** com prazo de transição (Res. 561, 574, 580, 584) tiveram impacto **estatisticamente nulo** no prêmio (dentro do ruído de ±35 bps).

2. **Equivalência com Cota vs. Tarifa:**
   - O ofício não extinguiu a demanda por dólares digitais; operou como uma cota não-tarifária: derrubou as importações em 78% e gerou um prêmio privado. Nenhuma fração desses R$ 106 milhões foi recolhida como imposto público.

3. **Como o Mercado se Ajustou (Limites à Arbitragem):**
   - O BCB não reabriu a rota dos fundos. A volta à paridade após 22/jul ocorreu pela entrada de capital lento (*slow-moving capital*): mesas institucionais e novas rotas B2B (comprovadas pelo saldo vendedor de 362 mi USDT na Foxbit) responderam ao incentivo quando o prêmio superou 35 bps.

4. **Três Previsões Datadas:**
   - Registramos antes dos dados: Res. 574 (3/nov) não moveu o prêmio [resultado ao vivo]; Res. 589 (6/nov) e Res. 584 (jan/2027) testam se o mercado já aprendeu a absorver regras normativas transparentes.
```

---

## 6. Action Plan & Timeline Leading to Submission

```
Wed 4 Nov (Tonight) ──► Thu 5 Nov ────────────► Fri 6 Nov ────────────► Sat 7 Nov ────────────► Sun 8 Nov (20:00)
• Push Plan Doc      • Execute R-3 (P3-20)   • Red-team review      • Rehearsal with        • Final PDF Export
• Triage team vote   • Check Coinnext (R-1)  • Polish 10-slide deck   David Wasserman       • Code bundle zip
  on Conclusion 1    • Check BRLA peg (R-2)  • Update HTML slides     (Saturday afternoon)  • SUBMISSION
```

### Next Steps for Felipe and Team:
1. **Confirm Preferred Conclusion:** Select between **Candidate 1 (The Private Tariff)** vs. **Candidate 2 (Microstructure & Slow Capital)** — *Recommendation: merge Candidate 1 as the headline, with Candidate 2 explaining the recovery mechanism.*
2. **Execute Live Verification (P3-20):** Pull the 3–4 Nov PTAX and Binance data to seal the Res. 574 prediction.
3. **Draft the Final 10 Slides:** Lock `deck/deck_v2_ptbr.md` and rebuild `deck/deck_v2_apresentacao.html`.
4. **Confirm Saturday Rehearsal:** Ping David Wasserman on WhatsApp/Discord to schedule Saturday afternoon.
