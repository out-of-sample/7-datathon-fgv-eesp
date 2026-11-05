# From competing payment rails to market adaptation: a research agenda

**Date:** 4 November 2026 (Brasília)  
**Prepared by:** Codex for Renzo, task P3-23  
**Status:** Research proposals for team and agent discussion; not adopted conclusions or experiment results.  
**Companion:** [Datathon ranking and investigation plans](competing-rails-datathon-ranking.md)

## Purpose and central question

This page records in English the research brainstorm requested by Renzo after reading Du, Huang and Scharfstein's *Competing Rails for Cross-Border Payments*. The original request deliberately placed no time or feasibility limit on the agenda. The companion page separately assesses what can strengthen the datathon submission.

The proposed question is: **How do stablecoin markets absorb the loss of a dollar-access channel: who replaces it, at what cost, and with what consequences for users?**

The project already documents a temporary Brazilian USDT premium increase. A further contribution would explain its mechanism, establish when that mechanism recurs, and measure consequences that the market price alone misses. Useful results can reject our initial explanation.

For a computer-science analogy, consider a network whose connection fails. Traffic might move to another connection, consume a buffer, or disappear because users stop sending it. Observing the network's price recover does not tell us which happened.

## What the literature check changes

- The supplied February draft has a later [BIS version, published 19 October 2026](https://www.bis.org/publications/working-paper-1385-competing-rails-crossborder-payments-banks-fintechs-and-stablecoins). It compares bank, fintech and stablecoin routes. The accompanying discussion calls attention to comparability, access and delivery conditions. Use version-specific tables; do not silently carry February numbers into a citation of the revised paper.
- The IMF's *Deconstructing the Stablecoin Sandwich* reports a route-cost study spanning 270 directed corridors and more than 4,000 routes. Another static bank-versus-stablecoin table therefore has limited incremental novelty. **Access limitation:** the official indexed abstract was inspected, but the [landing page](https://www.elibrary.imf.org/view/journals/001/2026/230/001.2026.issue-230-en.xml) returned 403 and the full paper was not read. These details remain abstract-level evidence, not a full literature review.
- [Aldasoro, Beltrán and Grinberg, BIS Working Paper 1340](https://www.bis.org/publications/working-paper-1340-stablecoin-flows-and-spillovers-fx-markets), already study stablecoin flows, constrained intermediaries and transmission to conventional FX markets. A price correlation or generic claim that arbitrage faces constraints is not, by itself, our contribution.
- [Graf von Luckner, Koepke and Sgherri (2024)](https://www.imf.org/-/media/files/publications/wp/2024/english/wpiea2024133-print-pdf.pdf) distinguish crypto trading from the underlying movement of capital. This reinforces the need to separate trading turnover, cross-border flows and ownership of existing assets.

The six directions below are our proposed extensions. Their novelty is provisional until a broader literature review is completed. The research designs are not findings from those papers.

## H1. Why did the premium disappear: replacement supply or retreating demand?

**Question.** When the premium declined, had the market restored its ability to supply digital dollars, consumed existing inventories, or lost buyers?

| Competing explanation | Discriminating evidence to seek |
|---|---|
| New suppliers or routes replaced the affected channel | Identifiable intermediary entry and external inflows through alternative connections |
| Existing inventories were consumed | Falling dealer holdings without matching replenishment |
| Buyers reduced or redirected demand | Client purchases, cancellations and movement to other services |
| Gross flows continued while purchases and disposals offset | Gross external acquisitions and disposals, alongside their net balance |

**Measurement issue.** The BC series in [F-024](../findings/F-024-stablecoin-imports.md) measures net external acquisitions. It is not a direct measure of all USDT available in Brazil. Seller-initiated exchange trading is also not an external inflow. Trading the same token repeatedly can produce large turnover without adding stock.

**Investigation.** Obtain anonymized intermediary records linking deposits, withdrawals, inventories and pre-event dependence on the affected channel. Compare more- and less-exposed participants, checking prior trends and concurrent shocks. Existing [F-031](../findings/F-031-who-traded-the-fade.md) and [F-032](../findings/F-032-supply-response.md) are useful starting evidence, but do not identify participants or new imports.

**Falsifier.** If demand retreat explains the recovery and there is no corresponding expansion of replacement supply, the rerouting hypothesis loses support. Failure to identify flows leaves the mechanism unresolved; it does not validate whichever story best fits the price chart.

**Contribution and materials.** An account of recovery speed and market reorganization; a stock-and-flow exhibit; a model of capacity substitution; and a test of whether normal prices conceal lasting dependence on fewer suppliers. Exchange concentration and supplier concentration must be measured separately. Foxbit gaining share does not automatically imply greater market concentration.

## H2. Which gate was closed, and what sign should the effect have?

**Question.** Can the operation affected by a rule predict whether the premium rises, falls or barely changes?

| Restriction | Possible mechanism, holding other conditions fixed |
|---|---|
| USDT inflows to local sellers | Reduced supply can raise the premium |
| BRL deposits by buyers | Reduced demand can lower the premium |
| BRL withdrawals | Trapped funds may generate demand for crypto as an exit route |
| Crypto withdrawals | Reduced usefulness of the asset can generate a discount |

Combined restrictions, substitutions and anticipation make the sign ambiguous. A label such as “capital controls” is too broad to determine a prediction.

**Investigation.** Build an independently sourced event classification: affected operation, affected participant, prior exposure, substitutes, announcement and implementation dates. Derive predictions from this classification before inspecting new outcomes. Compare affected and less-affected venues, while allowing spillovers between them.

**Falsifier.** Predictions fail on new events, or patterns follow unrelated common shocks rather than exposure to the specified channel. Preserve unsuccessful predictions. A non-significant test is not proof of zero effect.

**Contribution and materials.** A generalizable mechanism taxonomy, an event dataset and a prediction scorecard. This could strengthen [P3-22](../tasks/P3-22-other-countries-qualify.md), whose international cases require eligibility checks before tests. [P3-20](../tasks/P3-20-live-predictions.md) contains existing prospective predictions: this agenda must not rewrite them after registration.

## H3. How much can a route deliver by a deadline, especially under stress?

**Question.** What does it cost to deliver a given amount to the recipient, within a specified time, at an acceptable probability of success?

The proposed extension of the cost literature is to measure cost, capacity, speed and availability together. A cheap quote can become expensive at larger size, fail at execution, or vanish during stress.

**Investigation.** Collect repeated matched quotes and actual executions for both directions and multiple transaction sizes. Record final spendable receipt, all relevant fees and taxes, elapsed time, limits, rejected requests, outages and quote-to-execution changes. Retain failed requests in the denominator. Match residency, payment purpose, access rights and endpoint; an institutional route is not universally available to retail users.

Compare normal and stressed conditions, including calendar closures. Use market depth to measure size effects; hourly candles cannot reconstruct executable historical order books.

**Validated data-interface premise.** [Avenia's integration documentation](https://integration-guide.avenia.io/docs/Usecases/pix2Stable&stable2pix/) describes quotes, fee components and ticket states including failures. This establishes a potential recording interface, not historical access, representative pricing, production performance or an existing partnership. Sandbox examples are not observations.

**Falsifier.** A route retains its price advantage, capacity and reliability under stress. That would support its resilience rather than the hypothesis that its apparent advantage disappears when needed.

**Contribution and materials.** A reproducible benchmark of executable payments and a cost/amount/deadline comparison. The commercial use would be supplier and routing decisions; the academic use would be measuring what advertised-price comparisons omit.

## H4. Do BRL stablecoins move the bottleneck or remove it?

**Question.** Does tokenizing reais change access to dollars, or provide a new interface to the same intermediaries?

Measure two distinct conversions:

1. Bank reais to/from a BRL stablecoin.
2. A BRL stablecoin to/from a dollar stablecoin.

**A BRL stablecoin can remain worth R$1 while buying fewer dollars.** A local depeg is therefore not a necessary consequence of a restriction on dollar supply, and an intact local peg does not prove that tokenization solved the FX friction.

**Investigation.** Track minting, redemption access and timing, pool liquidity, and the cost of both conversions. Match amounts and access conditions against alternative routes. Do not estimate the local peg using the same affected USDT pool and then treat the inferred value as independent evidence. A token's backing, its redemption terms and its secondary-market price are distinct objects; [Avenia's terms](https://app.avenia.io/Avenia-TC.pdf) distinguish backing from secondary-price stabilization.

**Discriminating outcomes.** A stable BRL peg with the same FX premium suggests the FX bottleneck remains. A smaller premium with comparable capacity and access is consistent with an additional buffering route. Impaired redemption identifies a different fragility. Each interpretation still needs competing explanations tested.

**Contribution and materials.** A comparison of payment architectures, separating settlement technology from institutional access. Public on-chain records can help, but wallet location, customer residence and economic purpose cannot be read directly from an address.

## H5. Who bore the costs, and which transactions never happened?

**Question.** Who paid more, who received more, and who could no longer complete an intended transaction?

The additional amount paid over observed turnover in [F-025](../findings/F-025-money-moved.md) is not automatically social loss, intermediary profit or the burden on unique retail customers. Funds can circulate repeatedly; sellers and their own costs are not identified.

**Investigation.** Use anonymized client and order records to distinguish commercial payments, remittances, dollar saving and professional trading. Include rejected, canceled, delayed and rerouted orders. Compare users by pre-event dependence on the affected channel, with a design that addresses differences between those groups.

**Hypothesis.** Average prices recover while smaller users continue to face worse fees, limits or access. Price-only analysis could miss this persistent effect.

**Falsifier.** Recovery is similar across user groups, with sufficiently precise evidence against economically meaningful increases in cost, delay or exclusion. Lack of client data leaves the hypothesis untested.

**Contribution and materials.** An incidence study, a service-access comparison and estimates of substitution between payment options. Evaluating the rule's net social effect would also require measuring its benefits; cost-side incidence alone is not a complete welfare evaluation. [P3-21](../tasks/P3-21-who-paid.md) already supplies illustrative user scenarios, not observed household behavior.

## H6. Does channel closure insulate conventional FX or transmit pressure to it?

**Question.** Can a supply interruption raise the local stablecoin premium while weakening transmission to conventional FX, or does customer substitution increase pressure there?

Two mechanisms compete: less intermediation can reduce FX hedging flows, while displaced customers can seek dollars through conventional providers. Existing BIS work on stablecoin demand spillovers makes this distinction between shock types particularly important.

**Investigation.** Combine intermediary exposure and flows with synchronized spot, futures and funding measures. Account for interest differentials when using forward prices. Separate direct effects of the rule on banks from effects mediated by stablecoins.

**Identification limit.** A regulation affecting both banks and stablecoin access cannot automatically be an instrument for stablecoin flows: it may affect conventional FX directly. An event correlation or predictive lead is insufficient to resolve this.

**Falsifier.** Exposure-based predictions fail, or plausible direct and common-shock explanations account for the apparent transmission.

**Contribution and materials.** A model and empirical test of propagation across payment and funding networks. This is an ambitious extension rather than an extra regression added to the current event study.

## How the agenda fits together

The proposed chain is **channel shock → changes in alternatives and capacity → price and quantity adjustment → consequences for users**.

The strongest long-run academic combination is H1 plus H2; H3 provides a directly useful market benchmark, and H4 offers an architectural comparison. H5 and H6 extend relevance to users and macro-finance.

A CS contribution could represent routes as a network with cost, capacity, delay and access restrictions. A cheap route may exist yet have too little capacity to serve the market. A calibrated network that reproduces a known episode is not sufficient validation: evaluate it on another event, venue or transaction-size range, against simple baselines.

Potential shared research outputs:

| Material | Contribution |
|---|---|
| Versioned event/channel dataset | Replicable mechanism tests and transparent exclusions |
| Executable-payment benchmark | Comparable costs, capacity, timing and failure rates |
| Network interruption model | Dependence on suppliers and potential substitution routes |
| Incidence study | Distribution of costs and access losses |
| Prediction register | Visible generalization performance, including failures |

The central discussion prompt is: **When the premium returns to normal, has the market recovered, or is it operating with different participants, different risks and fewer users?**

## Reading and interpretation notes for the team

- This page preserves the broad brainstorm. The [companion ranking](competing-rails-datathon-ranking.md) narrows each direction to what the datathon can substantiate.
- Research proposals are not team decisions. Existing task ownership, registered specifications and core findings remain authoritative for execution.
- “Consistent with” is not identification; a missing reopening announcement is not proof that no operational accommodation occurred; a statistical threshold is not a measured route cost.
- Source status: the supplied PDF and revised BIS paper were examined in the preceding discussion; BIS landing pages were reopened on 4 November. IMF 2024 PDF and the Avenia documentation were opened in that discussion. The IMF 2026 sandwich paper remains an indexed-abstract-only source. Links and access limits are retained to make follow-up review possible.
