# Mentor Session Synthesis — David Wasserman (FGV Datathon)

**Date:** 2026-11-04 (Wednesday evening)  
**Context:** Mentoring session for 7º Datathon FGV EESP (Team *Out of Sample*)  
**Participants:**  
- **David Wasserman** (Mentor; ex-QR Asset, crypto/macro specialist, FGV network)  
- **Renzo Real Machado Filho** (Team *Out of Sample*, CS / Data)  
- **Felipe Cordeiro Caram** (Team *Out of Sample*, Economist / Deck Owner)  
- **Jonathan Pereira** (Team *Out of Sample*, CS / Validation)  
**Submission Deadline:** Sunday, 2026-11-08 (Deck freeze target: Wed–Thu)  

---

## 1. Executive Summary

The team presented their primary research project: **"Quanto custa fechar a porta? O preço do dólar digital no Brasil"**, analyzing the +93.9 bps acute premium spike on USDT/BRL following the confidential Banco Central do Brasil (BCB) supervisory *ofício* of 23 June 2026.

### Key Takeaway
The mentor strongly validated the empirical and econometric foundation (robustness across multiple venues, placebo distributions, causal identification, and volume drops). However, he delivered a critical warning: **The project currently lacks a punchy, tangible "So What?" economic conclusion.** The heavy lifting is in the conclusion: without a definitive answer on what this price distortion means for market participants, domestic stablecoins, on/off-ramps, and macro rails, the project risks being evaluated as a narrow econometric exercise rather than a first-place institutional contribution.

---

## 2. Core Discussion Points & Feedback

### A. Project Assessment & Strengths
* **Not overly "exotic":** While the team feared the topic might appear overly specialized compared to traditional portfolio optimization projects, David clarified that evaluating a specific, high-stakes institutional event is an asset, provided it speaks to broader economic mechanisms.
* **Econometric Rigor Validated:** The multi-exchange validation (Binance, Foxbit, Mercado Bitcoin), placebo tests across 1,000+ non-event dates, and matching to official BCB cross-border supply drops (-78%) provide solid empirical proof of causality.

### B. The Crucial Gap: The "So What?" (Conclusion & Economic Meaning)
* **The "Heavy Lifting" is in the Conclusion:** David emphasized that achieving 1st place depends almost entirely on framing a compelling, substantive answer to: *"And so what? What does this mean for the financial system?"*
* **Descriptive vs. Economic Impact:** Knowing that the spread rose 94 bps and cost buyers ~R$ 106M (Binance) / R$ 145M (3 exchanges) is only the baseline. The presentation must explicitly articulate:
  1. Who paid vs. who captured the economic rent?
  2. How do on-chain rails interact with traditional FX (fiat) channels when regulatory friction is introduced?
  3. What are the broader spillover effects into domestic liquidity, exchange viability, and capital flight?

---

## 3. Specific Leads & Hypotheses Suggested by the Mentor

### Lead 1: Hyperliquid & 24/7 Offshore Tokenized Price Discovery
* **Concept:** Hyperliquid is an on-chain perpetual DEX / EVM Layer-1 (top 10–12 crypto protocol by market cap). It features tokenized synthetic assets trading 24/7, including partnerships with ICE (Intercontinental Exchange, parent company of NYSE) for continuous S&P contracts.
* **Relevance to Brazil:** Hyperliquid lists **EWZ** (iShares MSCI Brazil ETF) trading around the clock. When B3 and Brazilian domestic banking rails close overnight or on weekends, price discovery for Brazilian equities/macro risk often shifts to offshore/on-chain venues.
* **Application/Question:** Did the closure of crypto-arbitrage FX channels spill over into offshore tokenized Brazilian assets or indicate offshore dollar demand when domestic rails were shut?

### Lead 2: Domestic Stablecoin Peg Stress (BRLA by Avenia)
* **Concept:** Avenia issues **BRLA**, a fiat-backed Brazilian Real stablecoin.
* **Hypothesis:** Under standard conditions, stablecoins trade at 1.00 BRL. However, during acute liquidity shocks (such as the June 23 notice), the restriction on FX arbitrage channels must exert asymmetric pressure on on-ramp and off-ramp rails.
* **Testable Implication:** Did BRLA experience a premium or discount (depeg/dislocation) against fiat BRL during the 94 bps USDT/BRL spike? Such dislocation would directly corroborate that the bottleneck was in the on/off-ramp fiat rails rather than an idiosyncratic USDT issue.

### Lead 3: Industry Casualties & Market Structure (Coinnext Exit)
* **Observation:** The regulatory tightening on zero-IOF FX arbitrage loops caused severe operational strain on domestic exchanges. David and the team noted the shutdown of **Coinnext** around this period.
* **Implication:** The notice did not just raise prices for retail; it altered market structure by eliminating business models reliant on triangular offshore arbitrage, concentrating volume on surviving venues (e.g., Foxbit B2B infrastructure adaptation).

### Lead 4: Expert Referral (Felipe Ludolf)
* **Profile:** Crypto lecturer at FGV, ex-QR Asset colleague of David, close associate of Jefferson.
* **Specialty:** FX mechanics, Binance order flow, and price formation during B3 non-trading hours.
* **Action:** David offered to share Ludolf's direct contact for rapid technical alignment on B3/Binance order flows before the weekend submission.

---

## 4. Post-Meeting Team Debrief & Internal Strategy

Following the call with David, the team (Felipe, Renzo, Jonathan) debriefed and made several immediate strategic decisions:

1. **Clarification on the 23 June Notice Mechanism:**
   * Felipe noted the notice was issued on 23 June first to authorized banks, then disseminated to crypto brokerages/exchanges, before reaching the financial press on 24–25 June.
   * The structural reason for the clampdown: domestic funds were using triangular offshore loops to purchase foreign exchange under zero IOF (under the guise of virtual asset investment) rather than standard commercial FX schedules. When BCB closed this loophole, domestic dollar liquidity dried up instantly.

2. **Filtering Out Political & High-Noise Rabbit Holes:**
   * David’s mention of EWZ on Hyperliquid prompted a discussion about looking at political shocks (e.g., 2022 presidential election market dislocation).
   * **Consensus decision:** **Reject political event studies.** Including election/political slides would introduce immense noise, weaken econometric identification, and alienate an FGV academic panel.

3. **Avoiding Overfitting with Predictive Models:**
   * Felipe warned against attempting complex predictive ML models for such shocks: with $N=1$ extreme regulatory intervention in the target window, any predictive model would heavily overfit. The strength of the study lies in structural inference, event-study placebos, and economic welfare accounting.

4. **Validation of AI Pre-Critique:**
   * Renzo noted that an automated Claude research critic agent had previously flagged the exact same critique: *"The jury will ask 'So what?'"*. The mentor's feedback directly confirmed that the repository's narrative priority must be answering this question cleanly in the 10-slide deck.

5. **Follow-up Checkpoint:**
   * David proposed a follow-up dry run / slide review on **Friday or Saturday afternoon** before the Sunday night submission.

---

## 5. Structured Data for AI Prompt Ingestion

```json
{
  "meeting_metadata": {
    "date": "2026-11-04",
    "event": "7º Datathon FGV EESP",
    "team": "Out of Sample",
    "mentor": "David Wasserman",
    "mentor_background": "Ex-QR Asset, FGV Crypto Network",
    "deadline_submission": "2026-11-08T20:00:00-03:00"
  },
  "project_status_at_review": {
    "title": "Quanto custa fechar a porta? O preço do dólar digital no Brasil",
    "core_finding": "+93.9 bps acute spike on USDT/BRL post-23 June 2026 BCB notice",
    "empirical_evidence": [
      "Placebo p ≈ 0.001 across 1,073 clean dates",
      "Replicated on Binance, Foxbit, Mercado Bitcoin",
      "Matches 78% drop in BCB foreign stablecoin import data (Jul 2026)",
      "Total estimated transfer: R$ 106M (Binance) / R$ 145M (3 venues)"
    ],
    "deck_constraint": "Strict maximum of 10 slides"
  },
  "mentor_critique": {
    "verdict": "Technically robust, strong methodology, high winning potential",
    "primary_risk": "Lack of a punchy, economically consequential conclusion (The 'So What?' question)",
    "recommendation": "Elevate the deck from an econometric anomaly report to a macro/market structure contribution with tangible policy/welfare conclusions"
  },
  "mentor_suggestions": [
    {
      "topic": "Hyperliquid & Tokenized 24/7 EWZ",
      "rationale": "Assess offshore tokenized Brazilian equity/FX price discovery during B3 closed hours",
      "team_verdict": "Keep as exploratory/annex context; avoid political noise"
    },
    {
      "topic": "BRLA (Avenia) Stablecoin Depeg",
      "rationale": "Check whether local BRL stablecoin depegged/discounted due to on/off-ramp liquidity squeeze",
      "team_verdict": "High value as corroborating evidence if data is readily accessible"
    },
    {
      "topic": "Market Exits (Coinnext)",
      "rationale": "Concrete evidence of industrial fallout from supervisory channel closure",
      "team_verdict": "Integrate as market structure context on the slide explaining institutional impact"
    },
    {
      "topic": "Expert Contact: Felipe Ludolf",
      "rationale": "Validate B3 vs Binance off-market trading flows with an FGV crypto/FX lecturer",
      "team_verdict": "Pursue contact for deck narrative sanity-check"
    }
  ],
  "action_items_for_deck_v2": [
    "Refine Slide 10 / Final Conclusion to directly state 'So What?' in clear economic terms",
    "Quantify consumer/arbitrageur transfer without overstepping causality into unsubstantiated recovery claims",
    "Explicitly frame the BCB 23 Jun notice as a capital control / quota equivalent on digital foreign exchange",
    "Schedule follow-up pitch rehearsal with mentor for Saturday afternoon"
  ]
}
```

---

## 6. Actionable Next Steps for Repository Workstreams

1. **Deck Architecture (P5-01 / `deck/deck_v2_ptbr.md`):**
   - Ensure the 10-slide limit is strictly adhered to.
   - Dedicate Slide 9 & 10 to answering the mentor's "So What?":
     - Quantified buyer tax / quota equivalent: R$ 5,052 per US$ 100k, R$ 106–145M transfer.
     - Channel economics: Zero-IOF fund closure $\to$ immediate domestic supply freeze (-78%) $\to$ premium surge.
     - Regulatory takeaway: Unpublished supervisory notices produce severe short-term dislocations, whereas formal published rules (with notice periods) show zero detectable premium dislocation.
2. **Sanity Check on Complementary Data:**
   - Quick check on BRLA or Coinnext announcements as qualitative corroborating points in the Annex.
3. **Rehearsal Scheduling:**
   - Coordinate with David Wasserman on WhatsApp/Discord for a Saturday afternoon rehearsal before the final PDF export.
