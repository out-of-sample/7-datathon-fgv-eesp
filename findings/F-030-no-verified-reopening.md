---
id: F-030
title: No source shows the BCB let funds resume the FX imports the 23 Jun notice stopped, so the reopening test cannot be run; the fall from 22 Jul came while stablecoin purchases abroad stayed at a third of their earlier level
status: exploratory
task: P3-17
date: 2026-11-02
checked_by: -
---

## Claim
**Verdict: unresolved. The reopening test cannot be run.** We found no public source, from 23 Jun to 30 Oct 2026, saying
that the BCB allowed funds to resume FX operations to import crypto for clients (the activity the 23 Jun notice stopped).
The only route back the BCB set out was confidential: each bank or broker had to show the BCB's conduct supervisor how it
told a fund's own trades apart from intermediation, and "até que esse alinhamento ocorra, as operações permanecerão
suspensas" (26 Jun, E-05.5). No source reports that this alignment was completed. In a written answer published on 29 Jul,
one week after the premium began to fall, the BCB said these operations "carecem do atributo de licitude" under current
rules (E-05.3). The one later rule on crypto imports through FX (Res. BCB 599, 9 Oct, E-13) adds a record-keeping code for
FX-authorised institutions, not funds, and "não cria atividade permitida nem mexe em vedação". This does **not** mean the
June notice had no effect; it means the opposite move cannot be observed.

**What the data say about the fall from 22 Jul** (rule fixed before the comparison, task file S2; a consistency check, not
a causal test). The premium fell while BCB-measured stablecoin purchases abroad stayed low: **US$ 702 mn in August and
US$ 843 mn in September, against a January–May mean of US$ 2,428 mn (R = 0.32)**. The import channel as a whole did not come
back at its earlier scale. But trading on the exchanges mostly returned to its pre-notice pattern (average trade size and
buyer share revert on 3 of 4 venue-metrics), as a reopening would predict. Under the pre-committed rule the result is
**mixed**: it neither fits a reopening nor rules one out. A fall in demand does not fit: Binance volume after 22 Jul was
only 5.4% below the pre-notice level (log change −0.056; the rule needed a fall of more than 25%, log < −0.29).

## Evidence
- **Source table**: 12 dated candidates, each with quoted operative language, publication and effective dates and a class
  (`results/tables/P3-17_candidates.md`). Full restoration 0; partial change 0; clarification 2 (C1 26 Jun meeting,
  C7 Res. BCB 599); substitution through another channel 1 (C8 Foxbit Infra, company claim, not verified); no verified
  change 9.
- **Screen of BCB rules and press notes, 20 Jun – 31 Oct 2026**: 893 normativos (779 Comunicados, 35 Resoluções CMN,
  35 INs BCB, 29 Resoluções BCB, 15 others) and 115 press notes and news; none mentions funds' FX operations. Res. BCB 589
  (23 Sep, E-14) tightens the counterparty ban; the Oct 2026 Financial Stability Report does not mention crypto.
  Reproduce: `python scripts/p3_17_restoration.py` (part A) → `results/tables/P3-17_bcb_screen.csv`.
- **BCB's later statements**: 29 Jul LAI answer (E-05.3): "pelas normas vigentes, os fundos não podem atuar como
  intermediadores de ativos virtuais"; 27 Aug, head of BCB statistics on the July fall in purchases: "reorganização do
  mercado de ativos virtuais num contexto de intensificação da regulação e da supervisão de conduta" (E-16). The vote behind
  Res. 599 (7 Oct) plans a public consultation in Q4 2026 and a rule "no primeiro semestre de 2027" (E-13).
- **Purchases abroad** (SGS 29644, US$ mn per month, residents' net acquisition): Jan–May 2026 mean 2,428; Jun 2,542;
  Jul 572; Aug 702; Sep 843. R = mean(Aug, Sep) / mean(Jan–May) = 0.32. Reproduce: same script, line `B1`.
- **Exchange order flow** (PTAX-day windows around 23 Jun: before 25 May–22 Jun, spike 24 Jun–21 Jul, after from 22 Jul;
  table `results/tables/P3-17_s4_structure.csv`, from `P3-10_order_flow.csv`):

  | Venue, metric | Before | Spike | After | Reverts? |
  |---|---|---|---|---|
  | Binance, average trade (USDT) | 1,432 | 1,641 | 1,520 | yes |
  | Binance, buyer-initiated share | 0.521 | 0.493 | 0.511 | yes |
  | Foxbit, average trade (USDT) | 730 | 4,687 | 6,297 | no |
  | Foxbit, buyer-initiated share | 0.621 | 0.303 | 0.596 | yes |
  | Binance, volume per day (mn USDT) | 58.4 | 77.6 | 55.2 | (demand test: −5.4%, not a fall of more than 25%) |

  Mercado Bitcoin has hourly candles only, so no trade size or buyer share. Reproduce: same script, lines `B2`, `B3`.
- **H4 test**: not run; the S2 credible set (rows classed full or partial restoration) is empty.

## Caveats
- **Absence of evidence.** The alignment of C1 was confidential and institution by institution. Some banks may have
  resumed operations for some funds without any public trace. Our search covers BCB rules, BCB press notes, the BCB's
  stability report and the press; it does not cover CVM fund filings one by one or BCB FX data by purpose code (not public).
- **R mixes channels.** The BCB series covers every resident buyer, not only funds; it cannot separate funds resuming from
  substitute imports by FX-authorised institutions (the C7 channel). A low R says the import channel as a whole did not
  return at scale; it does not say which importers were active.
- **The structure test discriminates weakly** (observed after seeing the result): trade size and buyer share may simply
  follow the premium back once the shock fades, whatever happened to supply. Foxbit's trades stayed about 8.6 times larger
  than before the notice, which fits new institutional flow (M-05) but is a single venue and timing only.
- **Not blind.** R ≈ 0.32 (F-024) and Foxbit's larger trades (F-008) were known before the S2 rule was written (disclosed in
  the task file). The premium had already halved by 10 Jul, before the 22 Jul break, so a single reopening date would not
  fit the price path anyway.
- Press quotes (E-05.5, E-05.11, E-16) are reports, not BCB transcripts; the 26 Jun meeting has no BCB minutes.

## Used in deck
Not used (deck owner Felipe decides). Language level for the fade's cause: **not shown**. If used, a safe sentence:
"Não encontramos registro público de que o BC tenha liberado a operação suspensa; em 29 de julho o BC reafirmou que ela
carece de licitude. A queda do prêmio a partir de 22 de julho ocorreu com as compras de stablecoins no exterior ainda em
um terço do nível anterior."

## History
- 2026-11-02, agent for Renzo: created (P3-17 S1–S5), status exploratory; needs a teammate's re-check of the source table
  and a re-run of the script
