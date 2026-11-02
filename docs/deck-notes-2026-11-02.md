# Deck notes, 2 Nov 2026 — how strongly each claim may be stated

For Felipe (P5-01, P5-05), from Renzo's agent after a review of the "beyond one period" proposals with a second agent.
Suggestions only: the deck owner decides. Line numbers refer to `deck/deck_v1_ptbr.md` at commit `9ca611d`.

## Four levels of language

Every claim in the deck belongs to one level, and its wording should match.

| Level | What belongs here | Wording |
|---|---|---|
| **Measured** | The one-month spike (+93.9 bps, placebo p ≈ 0.001, +74 to +128 bps across 22 variants, F-016, F-022); the money (R$ 106 mn Binance / R$ 145 mn three exchanges, F-025) | "subiu", "mediu-se", "pagaram" |
| **Consistent with the mechanism** | The notice (press reports, LAI answer, F-023); the July drop in stablecoin imports (−78%, p = 0.02, F-024). The import drop is the strongest link, but it is one monthly observation, Res. BCB 580 starts the same month, and the recovery test was inconclusive (R = 0.32) | "coincidiu com", "compatível com", "consistente com" |
| **Illustrative** | SVB/USDC (F-019); the cross-country premiums (F-010, two controlled currencies) | "ilustra", "padrão descritivo" |
| **Not shown** | A lasting effect (p = 0.24, F-022); the cause of the 22 Jul fade; which route set the price (P3-15); whether the notice's form (confidential, immediate) or its content (closing the funds' channel) mattered (F-026) | Say so on the slide |

## Lines that currently claim more than their level

| Slide (line) | Now | Why | Suggested |
|---|---|---|---|
| 1 (41) | "o prêmio descola da paridade até o custo do próximo canal disponível" | Theory stated as if we identified that channel. With Slide 5's 0% vs 3.5%, it invites "why +94 and not +350?" | Add: "qual foi esse canal em 2026 não identificamos (`P3-15`)" |
| 1 (50), 14 (448) | "derrubou em 78% as compras externas" | Causal from one monthly drop; Res. 580 the same month | "coincidiu com a queda de 78% nas compras externas" |
| 6 (190) | "normas publicadas com janela de adaptação permitem reajuste ordenado de rotas sem estresse de liquidez" | We found *no detectable move above ~35 bps*, not orderly adjustment; form and content are confounded (line 192) | "nenhuma das regras publicadas moveu o prêmio de forma detectável (acima de ~35 bps)" |
| 9 (269, 284) | "mostra a mesma lógica"; "vemos o mesmo mecanismo em escala macro" | Two controlled currencies; descriptive | "padrão descritivo compatível com a mesma lógica (2 moedas com controle; sem teste causal)" |
| 11 (335) | "O mesmo mecanismo aparece no próprio dólar" | USDC recovered *before* banks reopened: restored confidence in future redemption, not a reopened route. Access and confidence in the reserves (Circle's US$ 3.3 bn at SVB, F-019 timeline) cannot be separated. It does not test the funds' import channel | "Uma segunda ilustração de por que o acesso crível ao dólar sustenta a paridade" |
| 12 (360, 366, 375, 384) | "A Solução Prática"; "Monitor CUSUM (Nossa Solução)"; "metade dos falsos alarmes"; "Como solução prática" | One true detection, of a +94 bps move obvious after the fact; 2 vs 4 other alarms in 10 months is a small count | "Protótipo de monitor: uma detecção real (24/jun) e 2 outros alarmes em 2026"; keep the 2 vs 4 as counts, drop "metade" |

The prediction (Slide 12, F-027) is worded well: a claim that can be proved wrong, with Res. 580 on the same date as a
caveat. It is a prediction, not a result.

## What the deck can say about "more than one period"

- The effect rests on one shock. The breadth comes from seven published Brazilian rules used as contrasts (F-026),
  three exchanges and BTC (F-009, F-018), and 1,073 placebo dates. Say that plainly rather than reaching for SVB or other
  countries as replications.
- **Argentina (future work, one line in Slide 14):** the April 2025 lifting of dollar-purchase limits for individuals is
  a candidate test in the opposite direction, but it is not the reverse of Brazil's notice (demand side, and it came with a
  new exchange-rate regime and the IMF deal), and the official rate in the premium's denominator jumped at the same time.
  The ARS series is already frozen (P1-05, 28 Apr 2023 – 30 Oct 2026). Not run.

## Correction from Renzo's agent

Earlier I told the team that Decreto 6.306/2007 art. 15-B III had not been opened. Felipe opened it on Planalto on
2 Nov (`docs/sources.md` E-05.10 and R-02). The 0% IOF for the funds' route is sourced.

## Update, 2 Nov (later)

- "Lições de 2025" does not get its own slide: put it as a strip on the method slide (full table in the annex).
- Research continues, so the "future work" lines for Argentina and SVB may become results; keep the four language levels either way.
- Last year's main problem was the presentation time limit: write speaker notes to a time budget and plan rehearsals (P5-01 / P5-03).
