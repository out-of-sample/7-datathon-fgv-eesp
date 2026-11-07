# Proposal — "O que aprendemos com a solução apresentada? E por que é importante?"

**Date:** 5 Nov 2026, 14h Brasília · **By:** agent for Renzo · **Status:** proposal for the team. Nothing here is adopted,
no frozen result changes, no task is reassigned. Inputs: deck v3 (`deck/v3_claude_slides/`), mentor notes (4 Nov), the
competing-rails ranking (`docs/competing-rails-datathon-ranking.md`), Felipe's conclusions plan, all open task files, and
the Polygon report the mentor sent ("What LATAM Cross-Border Payments Look Like in 2026", Polygon, 2026; PDF in Renzo's
files, not in the repo).

## 1. The question the jury asked

Renzo (5 Nov): the opening presentation of the event asked teams to answer **"O que aprendemos com a solução apresentada?
E por que é importante?"** The organisers want a *solution*: something learned that someone can use, not only a measured
effect. Our current Slide 10 (v3, `slides/conclusao.html`) has three implications ("Para o BCB / Para o desenho de regras
/ Para os trilhos do real"). They are true, but they don't name a solution and don't answer the question in its own
words.

**Proposal in one line:** our solution is **a public, daily gauge of what each rule costs Brazilians who buy digital
dollars, plus a protocol to predict that cost before the rule takes effect**. What we learned with it fits in three
lessons. Every piece already exists in frozen or reviewed findings. The work is mostly framing, one small figure and two
checks.

## 2. Draft Slide 10 (pt-BR, v3 style, no task/finding IDs on the slide)

> **O que aprendemos: no Brasil, o custo do dólar digital se decide na porta de entrada, não na rede**
>
> **Três lições**
> 1. **Fechar uma porta de uma vez custa caro, e rápido.** O ofício imediato de 23/jun elevou o custo do dólar digital
>    em ~0,94% por um mês: R$ 4.842 a mais por US$ 100 mil; R$ 106 mi a mais só na Binance. As regras publicadas com
>    aviso não saíram da faixa das datas comuns.
> 2. **A rede barata não contorna a porta.** Transferir USDT custa uma fração de ponto-base; o ofício somou 94. A rota
>    on-chain Pix → BRLA → USDC pagou o mesmo prêmio. O custo que importa é o acesso ao dólar, e quem o define são as
>    regras.
> 3. **Preço normal não é mercado normal.** O prêmio voltou em um mês, mas as compras de stablecoins no exterior
>    ficaram em um terço e a fatia da Foxbit nas três corretoras passou de 7% para 35%.
>
> **A solução: uma régua pública do custo de cada regra**
> ① medir o prêmio todo dia na janela da PTAX, com dados públicos e código aberto → ② comparar com as datas comuns →
> ③ registrar a previsão no Git antes de a regra valer → ④ conferir e converter em reais.
> Em uso: Res. 574 (previsão "sem movimento": +2,1 bps, mantida) · Res. 589 (6/nov) · Res. 584 (jan/2027).
>
> **Por que importa**
> - **BCB:** as regras do mercado cripto estão sendo escritas agora; a régua dá o custo de cada uma no dia seguinte, sem custo.
> - **Quem paga ou recebe em stablecoin:** a vantagem da rede se mede em frações de ponto-base; o risco de uma porta
>   fechar, em ~100. É esse risco que entra no planejamento.
> - **Escala:** uma porta fechada levou o prêmio a ~1%; onde várias estão fechadas (Argentina, Ucrânia), ele fica em 4–7%.

**Evidence level of each line** (the four levels of `docs/deck-notes-2026-11-02.md`):

| Line | Level | Source | Open before Sunday |
|---|---|---|---|
| Lesson 1: +94 bps, R$ 4,842, R$ 106 mn; published rules inside the band | measured | F-016, F-015, F-025, F-026 (frozen) | — ("inside the band" = no effect above ~35 bps, not zero; form vs content not separated: keep in notes) |
| Lesson 2: network fee is a fraction of a bp | measured, **source missing** | P3-01 uses 1 USDT flat (0.1 bp on US$ 100k) from R-04, which is `[link not opened]` | Open a fee source (§3, item A) |
| Lesson 2: BRLA route paid the same premium | consistent with, exploratory | F-037 | Felipe's P3-24 review + scale caveat (§3, item B) |
| Lesson 3: purchases abroad at one third; Foxbit 7% → 35% | descriptive | F-024 (frozen), F-036 (exploratory) | Teammate re-run of F-036 (P3-25 S5) |
| Gauge steps and "Em uso" | measured / prospective, n = 1 | F-014, F-035 (exploratory), P3-20 registration, F-027 | Teammate re-run of F-035; E2 early reading Fri 6 Nov |
| Escala: Argentina, Ukraine 4–7% | descriptive, two currencies | F-010 (frozen) | — (no causal claim; "várias portas" is our classification, F-010 caveat) |

**Speaker-note sentence** for "por que importa": *"O BCB compra uma estimativa de custo regulatório por zero reais: um
script, dados públicos e um commit antes da regra. Fizemos isso três vezes; a primeira já foi conferida."*

**What this replaces in v3:** the three "Para o..." boxes become "Por que importa". The "monitor disparou no dia" line
moves to step ② (detection, not forecasting, as F-014 and Felipe's 4 Nov note require). The "nossa contribuição" line
stays in the notes.

## 3. What the Polygon report adds, and what it doesn't

**What it is:** marketing material from Polygon about its LATAM partners (Avenia/BRLA, BlindPay, Bitso, Belo, Mercado
Bitcoin, BRL1, BBRL, Minteo, Etherfuse, Ripio, Littio). No author or method, and most numbers are undated or
self-reported. **Never cite it directly on a slide.** Use only primary pages it links, opened and registered in
`docs/sources.md` (prompt.md §6).

**Its useful idea for us:** the industry sells stablecoin rails on *network* cost ("fractions of a penny", "$0.0002 per
USDC transfer", "<1% vs 6.49% traditional remittance fees"). Our evidence shows that in Brazil the dominant cost is
**access to the dollar, set by rules**, and that on-chain rails inherit it. That's lesson 2 and a creative hook,
especially with Ripple (cross-border payments) among the event sponsors.

Proposed explorations, ranked by value for the PDF per hour of work:

| # | Exploration | What it shows | New data / work | Value | Risk | When |
|---|---|---|---|---|---|---|
| **A** | **Cost stack "a rede não é o custo"**: one bar chart of a US$ 100k USDT purchase on Binance before / during / after the spike, split into network fee, exchange fee and premium | Network fee ~0.1 bp vs premium +94 bps (~900×). Lesson 2 in ten seconds | Re-plots frozen numbers: premium 15.2 → 109.1 bps (F-016's windows, so the change is exactly +93.9), 26.8 after (`P3-01_route_costs.csv`, USDT_REGIME_6); fee rows from the same table. **Needs one opened fee source**: Binance withdrawal-fee page opened in a browser (Cloudflare blocks scripts), or Polygon/Tron fees from a public explorer. New finding F-040 (renumbered 6 Nov: F-038 went to P3-30) + figure script, ~1–2 h | High | Low. Stay inside the USDT route: no bank-vs-USDT ranking (F-028, H3 deferred 4 Nov) | PDF |
| **B** | **BRLA scale caveat**: Avenia reports ~US$ 500 mn/month peak payment volume on Polygon; the pool we priced traded ~US$ 5.9 mn in four weeks | The pool is the *public on-chain price*, ~1% of Avenia's reported flow. Most flow is minted/redeemed off-pool at prices we don't see. F-037's "small market" wording should say "the part we can price is small" | Open Avenia's/Polygon's primary page for the volume claim; one line in F-037 History and annex, ~30 min | Medium (honesty; pre-empts a juror who knows Avenia) | None | PDF |
| **C** | **"Escada de portas" annex figure**: premium level in open markets (EUR ~0, MXN ~20–40 bps), Brazil before (~15 bps), Brazil spike (~109), Ukraine (~410–490), Argentina (~550–720; ~3,000 in 2024) | Puts our one-door episode on a scale: what's at stake if more channels close | No new number: F-010 yearly means + F-016 levels; figure only, ~1 h | Medium | Medium: different fix times and benchmarks (F-010 caveats); descriptive only. ARS 2025 mixes pre/post the April 2025 opening | PDF (annex), one phrase on slide 10 |
| **D** | **Other BRL tokens' dollar routes** (BRZ, BRL1 by Foxbit/MB/Bitso): replicate F-037's S20 on their USDC/USDT pools | Whether every on-chain reais rail hit the same door | GeckoTerminal serves 180 days, so **the 25 May pre-window disappears on ~21 Nov**. Snapshot raw pools now even if the analysis waits; spec before computing; ~3 h | Low–medium (F-037 already makes the point) | Thin pools (most BRLA pools failed liquidity) | Snapshot now; analysis for the oral |
| **E** | **BBRL (Banco Braza, an FX-licensed bank)**: does a bank-issued reais token show a smaller dollar-route premium? | A creative limits-to-arbitrage contrast (issuer with official FX access) | Qualification only: does a BBRL–dollar pool with June data exist? ~1 h | Low | High: the notice targeted funds' FX imports, so the bank isn't clearly unaffected; likely no liquid pool | Only if A–C are done |

**Not worth pursuing (off our question):** Mercado Bitcoin RWA tokenisation, Bitso/US–Mexico remittances, Littio/Belo
yields, Paxos card fees, COPM/MXNe, Polygon's chain-share claims.

## 4. The other tasks: how each one feeds the answer

| Task | Status now | Feeds | Proposed next step | Before PDF (8 Nov) or oral (16 Nov) |
|---|---|---|---|---|
| P5-08 Slide 10 | todo, Felipe | the whole answer | Felipe takes §2 as the S1 draft (or rejects it); Renzo checks sentence by sentence | PDF |
| P3-20 predictions | doing, Renzo (agent) | "régua em uso" | Fri 6 Nov after 13:30: E2 early reading; Mercado Bitcoin JSON via browser; **teammate re-run of F-035** (Nattan or Jonathan) | PDF (E1, E2 early); oral (E2 verdict 9 Nov) |
| P3-03 monitor | done | step ② of the gauge | **New, small:** run the frozen alarm (threshold from 2020–2025, no re-tuning) on P3-20's extended series (`data/processed/P3-20_premium_daily.csv`) and report its state on the last day. Gives one line, "em 6/nov a régua marcava X bps, sem alarme": the tool runs today. Spec first, ~1–2 h, teammate re-run | PDF (one line), oral (live) |
| P3-24 BRLA | review, Felipe | lesson 2 | Felipe's S5 review; add the Avenia caveat (§3 B) | PDF |
| P3-25 composition | review | lesson 3 | Teammate re-run (S5); Felipe places it on slide 7 ("o preço voltou, o mercado não") | PDF |
| P3-21 who paid | doing | "por que importa" (people) | Already on v3 slide 8; Felipe's S5 sign-off | PDF |
| P5-09 deck v3 / P5-01 v1–v2 | review / paused | — | Team picks a deck **before** slide 10 is rewritten, so the rewrite lands once | PDF |
| P5-02 figures | todo | A, C | Add the cost-stack and ladder figures to the same style script | PDF |
| P5-03 red team (Fri 6) | review | test of the answer | Add two checklist items: "a juror reads only slide 10: can they say what we learned, and why it matters?" and "does any slide cite the Polygon report directly?" | PDF |
| P5-04 claim map | review, Nattan/Jonathan | traceability | Add F-040 and any new script to the map | PDF |
| P5-05 annex | doing | — | Ladder figure, Polygon context paragraph, Avenia caveat | PDF |
| P3-22 other countries | todo; **deferred by Renzo on 4 Nov** ("not before submission") | generality of the gauge | Argentina's April 2025 opening is the mirror of our closing ("abrir a porta derruba o prêmio?"). Stage 1 qualification + retrospective spec, prior exposure disclosed (F-010 yearly means seen). Needs the 4 Nov decision reopened | Oral, unless Renzo reopens it for the PDF |
| P3-05 / P3-06 "30 AI analysts" | doing (S3–S7 pending) / todo | creativity, robustness | Live runs need Renzo's machine and accounts (~3–5 h). If done: one annex chart, "30 analistas independentes com os mesmos dados", in the spirit of the many-analysts literature (open the reference before citing) | Oral or drop |
| Tasks in `review` (P1-04, P1-09, P2-06, P3-09, P3-15–P3-17, P3-19, P3-23, P4-04) | review | numbers already on slides | One sign-off session by a teammate who didn't author them | PDF |

**Rule that sets the order:** after the 4 Nov freeze, a new number reaches the deck only after a teammate's re-run
(decision log, 4 Nov). Each new finding costs Nattan's or Jonathan's time before Sunday. So the PDF should add at most two
new findings: F-040 (cost stack) and the gauge-today line. Everything else goes to the oral.

## 5. Proposed order

**Thu 5 (today):** team reads this; Felipe accepts, edits or rejects §2. Open the fee source for A and the Avenia page for
B. Snapshot GeckoTerminal pools for D (raw only, no analysis).
**Fri 6:** red team morning with the new checklist items; A built (F-040) and re-run by a teammate; E2 early reading
after 13:30; gauge-today line.
**Sat 7:** P5-02 figures (cost stack, ladder); annex; slide 10 final; P5-04 claim map updated.
**Sun 8:** PDF by 20:00.
**8–16 Nov (oral):** E2 verdict (9 Nov), live gauge, optionally Argentina (P3-22) and D.

## 6. Decisions needed

1. **Felipe:** adopt §2 as the base of slide 10 (it replaces v3's three "Para o..." boxes)?
2. **Team:** approve explorations A, B and C for the PDF (new task(s) and finding F-040)?
3. **Renzo:** keep P3-22 deferred to after submission (4 Nov decision), or reopen it for the PDF?
4. **Renzo:** run P3-05/06 (30 AI analysts) for the oral, or drop it?
5. **Nattan / Jonathan:** who re-runs F-035, F-036 and the new F-040 before Saturday?
