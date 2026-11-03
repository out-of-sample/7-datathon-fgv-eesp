# Deck proposal, 3 Nov 2026: the 10 slides after the 3 Nov decisions

Written by the agent for Renzo, for Felipe (deck owner) and the team. **A proposal only: `deck/deck_v1_ptbr.md` is not
changed by this file.** Felipe accepts, edits or rejects each row in §3; the decisions the team must take are in §4.

## 1. What changed since the 10-slide cut (2 Nov)

| Decision or result | Source | Effect on the deck |
|---|---|---|
| Cost of the notice converted at each day's PTAX: **R$ 4.842** per US$ 100 mil (was R$ 5.052 at a Binance bid of R$ 5,38) | decision log 3 Nov; F-015, F-033 | Already applied to slide 1, slide 9 and annex B.5/D.2 (`b64b847`). **Two spoken notes still say "cerca de 5 mil reais"** (slides 1 and 9) |
| Bank-route table stays in the annex, at a labelled illustrative rate of R$ 5,38 (option A + a) | decision log 3 Nov | No slide change; annex B.5 already explains the rate |
| "Who paid and who gained": four users with rules fixed in advance | F-033 (exploratory, independently re-derived) | Candidate for slide 9 (illustration, not evidence) |
| Seller-initiated trading on Foxbit during the fade, rising with the premium over PTAX | F-031, F-032 (exploratory, post hoc) | Optional half-line on slide 8 |
| Two more predictions registered before the data: Res. 574 reporting (3 Nov), Res. 589 ban (6 Nov) | P3-20 (`9a522e9`, `ce283dc`, `abc603f`) | Slide 10: three dated predictions instead of one |

## 2. The deck at a glance

The storyline does not change: question → the closed channel → method → jump → other rules → not something else →
mechanism → limits → money → implications. It follows Art. 7 (motivação → delimitação → dados e metodologia →
resultados → discussão). Only slides 8, 9 and 10 change in content; slides 1 and 9 get corrected notes.

| # | Title (pt-BR) | Change | Level of language |
|---|---|---|---|
| 1 | Quanto custa fechar a porta? | Notes: "cerca de 4,8 mil reais" | measured |
| 2 | A porta que fechou: o ofício de 23/jun | none | measured (sources) |
| 3 | Dados e método | none | — |
| 4 | O salto | none | measured |
| 5 | Entre as oito regras testadas, só o ofício saiu da faixa comum | Res. 574 wording follows the P3-16 outcome | measured |
| 6 | Não foi o real, nem o USDT, nem o mundo | none | measured |
| 7 | O mecanismo: as importações caíram | none | consistent with the mechanism |
| 8 | Robusto, mas de um mês | optional: one exploratory half-line on the fade | measured + not shown |
| 9 | **Quanto custou e para quem** | **restructured: market total + four users** | measured (total) + illustrative (users) |
| 10 | **Implicações e três previsões datadas** | **three registered predictions** | prediction |

## 3. Slide-by-slide changes

### Slide 1 — fix the spoken number
- Notes: replace "cerca de 5 mil reais a mais" with **"cerca de 4,8 mil reais a mais"**.
- Nothing else. The title, caption and bullet already say R$ 4.842.

### Slides 2–7 — unchanged
- Slide 5 only: when P3-16 decides whether Res. 574 enters the event list or stays a caveat, the Res. 574 bullet follows
  that decision. Today's text (caveat) is consistent with "caveat".

### Slide 8 — Robusto, mas de um mês (optional addition)
Keep the slide as it is. Option to add one half-line to "O que não mostramos", in the not-shown level:

> - a causa do recuo: nenhum evento datado a até 5 dias úteis de 22/jul, e as compras no exterior não voltaram. **Durante
>   a queda, houve vendas fortes na Foxbit, que cresciam com o prêmio (exploratório, Anexo F); quem vendeu não foi
>   identificado.**

Recommendation: **add it only if F-031/F-032 get a teammate's re-check before the freeze**; otherwise leave it in the
annex and the Q&A sheet. It answers the jury's obvious question ("what brought it back?") without claiming a cause.

### Slide 9 — Quanto custou e para quem (restructured)

**Title (proposed):**
> Em quatro semanas, quem comprou USDT pagou R$ 106 milhões a mais na Binance; para uma pessoa, depende de quando precisou
> de dólar

**Caption (10 seconds):**
> De 24/jun a 21/jul, compradores na Binance pagaram R$ 106 milhões acima do prêmio anterior (maior valor em 194 janelas
> comuns: R$ 35,5 milhões). Abaixo, o que isso significou para quatro pessoas, com regras fixadas antes do cálculo.

**Top line (measured, F-025):** R$ 106 mi na Binance, R$ 145 mi nas três corretoras; transferência de compradores para
vendedores, sem arrecadação; não inclui balcão (OTC) nem P2P.

**Table (illustration, F-033; per US$ 100 mil unless stated; only the premium, without fees or taxes):**

| Quem | Regra fixada antes | Resultado |
|---|---|---|
| Precisou de dólar no pico | comprou num dia entre 24/jun e 21/jul | pagou **R$ 4.842** a mais, em média (R$ 1.895 a R$ 8.824 conforme o dia) |
| Poupa US$ 10 mil por mês | comprou no 1º dia útil de cada mês | nas 4 compras após o ofício (US$ 40 mil), **R$ 753** a mais |
| Já tinha USDT em 23/jun | vendeu em 24/jun, 21/jul ou 30/out | posição valorizada em R$ 6.802, R$ 1.407 ou −R$ 2.992 |
| Comprou no pânico, em 24/jun | manteve até 21/jul ou 30/out | posição desvalorizada em R$ 5.223 ou R$ 10.070 |

Footnote: "Ilustração com regras fixadas antes do cálculo (commit `79e15d1`) sobre um caminho de preços já conhecido.
Compras são transferências; valorização de posições mantidas não é dinheiro que mudou de mão. Anexo B.5."

**Moved out:** the "por que +94 e não +350 bps?" paragraph goes to the annex (B.5, next to the route table) and stays
in `deck/qa_ptbr.md` as a rehearsed answer. Reason: the slide cannot hold both the users' table and that argument and
stay readable in ten seconds. **This is the main trade-off of the proposal** (§4, decision 2).

**Notes (proposed):** "Em dinheiro: nas quatro semanas após o ofício, os compradores de USDT na Binance pagaram 106
milhões de reais a mais do que pagariam ao prêmio anterior; nenhuma janela comum passou de 36 milhões. Esse dinheiro foi
de quem comprava para quem vendia, não para o governo. Para uma pessoa, dependeu de quando precisou de dólar: quem comprou
no pico pagou cerca de 4,8 mil reais a mais por 100 mil dólares; quem poupava todo mês sentiu pouco; quem já tinha USDT
ganhou se vendeu logo; quem comprou no pânico e segurou ficou para trás. As regras de cada pessoa foram fixadas antes do
cálculo."

### Slide 10 — Implicações e três previsões datadas

**Title (proposed):**
> Fechar um canal de uma vez gerou um custo agudo que se desfez em cerca de um mês; deixamos três previsões datadas que
> podem nos desmentir

Keep the "Para o Brasil", "termômetro" and "limites" bullets. Replace the single prediction box with:

| Regra | Vigência | Previsão registrada antes dos dados | Conferência |
|---|---|---|---|
| Res. BCB 574 (reporte de operações com ativos virtuais) | 3/nov/2026 | sem movimento detectável (`9a522e9`) | resultado em 4/nov à noite; **no slide se pronto antes do envio** |
| Res. BCB 589, art. 91 (veda contrapartes não autorizadas) | 6/nov/2026 | ramo escolhido pelo texto legal até 6/nov 10h (`abc603f`) | 10/nov; apresentado na final, se formos finalistas |
| Res. BCB 584 (retenção de até 24 h) | 1/jan/2027 | sem movimento detectável; faixa −35,0 a +37,6 bps (`393a14a`) | fevereiro de 2027 |

Footnote: "Um resultado dentro da faixa exclui apenas movimentos maiores que ela, não prova efeito zero."

Why: three predictions registered with Git hashes, one of them checkable before submission, are much harder to dismiss
than one prediction due in 2027, and they speak directly to the slide-5 limit (published rule vs confidential notice).

## 4. Decisions needed (Felipe and the team)

1. **Slide 9: users' table in, "+350" paragraph out to the annex?** Recommended: yes. Alternative: keep the current
   slide and put F-033 in annex B.5.
2. **Slide 10: report the Res. 574 result if it is ready before 7 Nov?** It is a result produced after the 4 Nov freeze,
   and `docs/phases.md` allows only bug fixes after it. Recommended: allow this one exception, because the rule, the
   statistic and the reading were committed before the data (`9a522e9`, `ce283dc`), and log it in the decision log. If the
   team says no, the row shows the prediction and "conferência após o envio".
3. **Slide 8: the exploratory half-line on the fade?** Only if F-031/F-032 get a teammate's re-check before the freeze.
4. **Slide 5: Res. 574 as event or caveat** (P3-16; pending since 2 Nov).

## 5. Before the freeze, independent of these choices
- A teammate re-runs `scripts/p3_01_costs.py` and checks the R$ 4.842 on slides 1 and 9 (STATUS blocker).
- Slides 1 and 9: replace "cerca de 5 mil reais" in the notes (stale after the 3 Nov change).
- `P5-02`: the overlapping bank-route labels at the top of `results/figures/P3-01_route_costs.png` (annex figure).
