# Deck changes, 2 Nov 2026: 14 slides → 10

For Felipe (deck owner, P5-01) and the team, from Renzo's agent. Renzo asked the agent to apply the 10-slide plan
(`docs/deck-plan-10-slides.md`) to the deck itself and to keep this record. Felipe can reverse any change. The
14-slide version stays in git: `git show 1bce097:deck/deck_v1_ptbr.md`.

## Files changed

| File | Change |
|---|---|
| `deck/deck_v1_ptbr.md` | Rewritten as 10 slides, in the format `scripts/build_deck_html.py` reads (same file name, so links and the build still work) |
| `deck/deck_apresentacao.html` | Rebuilt with `.venv/bin/python scripts/build_deck_html.py`: 10 slides, 6 figures, 4 tables |
| `deck/annex_v1_ptbr.md` | New **Anexo F** (material moved off the slides); D.2 traceability matrix rewritten for 10 slides; L-09 added to C.5 |
| `deck/qa_ptbr.md` | New: 13 hard questions with ~20-second answers and pointers, for rehearsal (plan, strategy row 7) |
| `scripts/p3_12_rules.py`, `results/figures/P3-12_rules.png` | Figure title and label only: "Só o ofício sigiloso moveu o prêmio" → "Entre as oito regras testadas, só o ofício sigiloso saiu da faixa das datas comuns"; "(nenhuma data comum chega perto: p ≈ 0,001)" → "(maior que em todas as 1.073 datas comuns)". `results/tables/P3-12_rules.csv` is unchanged (no diff after the re-run) |
| `docs/sources.md` | L-09 (Gelbach, Helland & Klick 2013), record re-opened 2 Nov; used only in the Annex F.1 method note |
| `findings/F-029-headline-inference.md` | Slide-5 text: "datada quatro dias antes" was wrong (register 18 Jun is 5 calendar days before; DOU 22 Jun is 1); now names both dates. "Used in deck" filled |

## Slide map

| New | Title | Came from (14-slide numbers) |
|---|---|---|
| 1 | Quanto custa fechar a porta? | 1 (question and answer only) |
| 2 | A porta que fechou: o ofício de 23/jun | 1 (parity idea), 5 (first half), new timeline table |
| 3 | Dados e método | 2 (hypotheses, compressed), 3 (data), 13 (one "Lições de 2025" strip) |
| 4 | O salto | 3 (break test), 4 (three exchanges), F-029 |
| 5 | Entre as oito regras testadas, só o ofício saiu da faixa comum | 6 |
| 6 | Não foi o real, nem o USDT, nem o mundo | 4 (the real, USDT/USD), 7 |
| 7 | O mecanismo: as importações caíram | 5 (second half) |
| 8 | Robusto, mas de um mês | 8, 14 (limits) |
| 9 | Quanto custou e para quem | 10 (money only), F-028 |
| 10 | Implicações, previsão e limites | 12 (prediction, monitor as one line), 14 |

Moved to the annex: slide 9 (countries) → F.2; slide 11 (SVB) → F.3 (case table already in B.6); slide 12 (monitor
table) → F.4; slide 13 (Lições table) → F.5; slide 14 (hypothesis scoreboard) → F.6; slide 10's bank-route block
(Option C) → B.5 (Option A, already there) and F.7; Band-TAR (old slide 3) → already in B.6.

## Wording changes and why

Each change follows the four language levels (`docs/deck-notes-2026-11-02.md`) or a finding.

| Where | Was | Now | Why |
|---|---|---|---|
| Headline inference (old 6, 14) | "p = 0,0009" / "p ≈ 0,001" on slides | "maior que a mudança em todas as 1.073 datas comuns (a maior: +65,7 bps)"; "em 30 janelas que não se sobrepõem, p = 0,03" | Overlapping windows overstate precision; P4-04 decision rule 1 met (F-029) |
| Headline window (new 4) | not mentioned | The month also holds the 26 Jun meeting and Res. 580; +155 bps in the two days before the meeting (p 0.02–0.04) | F-029, P4-04 decision rules 2 and 4 |
| Rules slide title (old 6 → new 5) | "Só o ofício de efeito imediato moveu o prêmio" | "Entre as oito regras testadas, só o ofício saiu da faixa comum" | Res. 574 coincides with +37.7 bps on 18→19 Jun and was not tested (F-029, P3-16). **Deviation from the plan**, which said "Entre as regras com data": Res. 574 is a dated rule, so "das regras com data" would overclaim |
| New 5 | – | Res. 561 as the closest contrast (banned virtual assets in eFX, 154 days' notice, +6.0 / −5.3 bps), with "the eFX channel's size is unknown" | Plan, strategy N3 |
| Old 6 | "normas publicadas com janela de adaptação permitem reajuste ordenado de rotas sem estresse de liquidez" | "não moveram o prêmio de forma detectável (acima de ~35 bps)" (new 10) | Deck notes: not shown |
| Old 1, 14 | "derrubou em 78% as compras externas" | "coincidiu com" / "compatível com" (new 7) | One monthly observation; Res. 580 the same month (F-024) |
| Old 1 | "o prêmio descola da paridade até o custo do próximo canal disponível" + equation | Parity in one plain sentence (new 2); "why +94 and not +350" answered on new 9 | F-028: route not identified |
| Old 4 → new 6 | "o real teve um dia comum" | "PTAX +0,68% em 24/jun, um dia comum … já descontado" | The real moved; the premium removes it by construction (F-009) |
| Old 10 → new 9 | "capturada por quem ainda conseguia trazer ou ofertar stablecoins"; "p = 0,005" | "de quem comprava para quem vendia"; "a maior de 194 janelas comuns de quatro semanas: R$ 35,5 mi", no p | F-025 says who received it is inferred; its 194 windows overlap (same issue as F-016), so no p on the slide |
| Old 10 | R$ 106 mn and R$ 145 mn side by side | R$ 106 mn as the number; R$ 145 mn in brackets and in the table | One number per concept (plan, strategy 6; F-025 uses Binance because of F-008) |
| Old 12 | "A Solução Prática", "Nossa Solução", "metade dos falsos alarmes" | "protótipo", "uma detecção real, não uma validação", "2 outros alarmes (contra 4)" | Deck notes: one detection; small counts |
| Old 9, 11 (now F.2, F.3) | "mostra a mesma lógica", "o mesmo mecanismo aparece no próprio dólar" | "padrão descritivo … sem teste causal"; "uma segunda ilustração" | Deck notes: illustrative level |
| Old 14 | Drex / Ripple ODL / RLUSD "reduz o custo de fricção cambial" | removed | No finding or source supports it |
| Old 13 (now F.5) | "53,6% do spread … era subsídio" as a title fact | "uma reanálise sugere 37,5% a 53,6% (`exploratory`, sem revisão independente)" | F-020 was re-checked by its own author |
| New 3 | – | Disclosure: the jump was seen in the 30 Oct probe, before the hypotheses; tests registered in git before running; the notice date comes from outside sources | `docs/02-dolar-cripto.md` §13 ("Declare it"); plan |
| New 2 | – | Market operators quoted on 24 Jun linked the spread to the notice (E-05.6) | Plan, strategy N4 |
| New 10 | – | Res. 584 prediction labelled a partial test (it does not touch the incoming channel); Res. 574 reporting as a future data source, "se os dados se tornarem disponíveis" | Plan, strategies 4 and 2b |

Also: finding IDs moved from slide bodies to one "Fontes" line per slide; speaker notes rewritten to ~110–150 words
(~60 s each, ~10 min total); action titles state each slide's result.

## Not done (open)

| Item | Who |
|---|---|
| Review the whole deck; accept or reverse any change above | Felipe |
| Option C vs A: the plan's choice (A, bank-route table in the annex) was applied | Team confirms |
| P3-16 S1: Res. 574 in the event list or as a caveat. The deck carries it as a caveat on slide 5 either way | Felipe + team |
| F-015 (R$ 5,052 on slides 1 and 9) is still `exploratory`; F-029 (slides 4 and 5) is `exploratory` and needs a teammate re-run; F-028 has no reviewer | A teammate who did not author them |
| New figures (P5-02): slide 2 timeline + channel diagram; slide 3 design diagram; slide 4 headline chart focused on 2025–26 with the hourly inset and Portuguese labels (`P2-02_premium_breaks.png` is in English); slide 9 transfer vs the 194 windows. Check the language of the P2-04, P3-10 and P4-01 figures | Renzo (P5-02) |
| F-025's p = 0.005 rests on overlapping windows. Not on the slides; F-025 itself is unchanged until the freeze is re-decided | Team, at the freeze |
| `notebooks/p5_07_story.ipynb` still follows the 15-section, 14-slide flow | Optional |
| Two timed rehearsals with a timekeeper, using `deck/qa_ptbr.md`; the oral time limit is unknown until the finalist e-mail | Team (P5-03) |
| PDF (P5-01 S4) after the freeze (P4-03) | Felipe |
