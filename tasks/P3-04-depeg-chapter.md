---
id: P3-04
title: Depeg chapter v1 (the same mechanism in dollars)
phase: P3
status: review
owner: CS 3
working: -
due: 2026-11-03
depends: P1-07
---

## Goal
Turn P1-07 into 1-3 slides: the SVB weekend, and Kaplan-Meier curves only if there are at least 12 independent events. If extension A is a go, this shrinks to the SVB slide only. Plan: `docs/01-depeg-recovery.md` (chapter scope).

## Subtasks
- [x] S1: Filter verified v2 depeg screen (`results/tables/P1-07_v1_vs_v2.csv`) to the 11 USD-confirmed downward depeg events (`direction == "below"`, 9 ex-drift, 8 ex-terminal & drift) — done: Felipe, 2 Nov
- [x] S2: Verify pre-committed sample threshold rule (`n = 11 < 12`, KM curves omitted per protocol); create `scripts/p3_04_depeg_chapter.py` and output `results/tables/P3-04_depeg_case_table.csv` and `results/tables/P3-04_category_summary.csv` — done: Felipe, 2 Nov
- [x] S3: Generate chapter figures `results/figures/P3-04_svb_weekend.png` (SVB weekend timeline) and `results/figures/P3-04_depeg_cases.png` (11-event comparative trough and duration visualization) — done: Felipe, 2 Nov
- [x] S4: Document empirical evidence in `findings/F-019-depeg-chapter.md` and draft polished Portuguese (`pt-BR`) text for the 2 chapter slides in `## Result` — done: Felipe, 2 Nov

## Success criteria
- [x] SVB figure final — done: Felipe, 2 Nov
- [x] Event count stated — done: Felipe, 2 Nov
- [x] KM only if >= 12 events — done: Felipe, 2 Nov
- [x] Draft slide text (pt-BR) in the Result section — done: Felipe, 2 Nov

## Outputs
- `scripts/p3_04_depeg_chapter.py`
- `results/tables/P3-04_depeg_case_table.csv`
- `results/tables/P3-04_category_summary.csv`
- `results/figures/P3-04_svb_weekend.png`
- `results/figures/P3-04_depeg_cases.png`
- `findings/F-019-depeg-chapter.md`

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** reviewed by Renzo (2 Nov). **Data and design hold; sources and claims need work** (owner: Felipe / CS 3).
  `scripts/p3_04_depeg_chapter.py` reproduces the tables (differences only at 10⁻¹³). It uses the v2 events (F-013): 11 falls
  below $1 + the USDC SVB case from Bitstamp, with the $0.863 hourly close. A case table instead of curves, per the
  ≥ 12 rule. Good.
- **Changes requested:**
  1. **Each case's "mechanism" needs a source** (rule: sources are opened, `prompt.md` §6), or a neutral label. Examples:
     "boatos sobre solvência de custodiante" (FDUSD Apr 2025), "escrutínio regulatório" (TUSD Jan 2024),
     "choque de demanda pós-eleição americana" (TUSD Nov 2024), "MIM/Abracadabra" (UST Jan 2022).
     None is in `docs/sources.md`.
  2. **F-019's title and claim overreach.**
     - "11 downward depegs confirm that backing solvency, not open banking hours, determines survival" and "proving that
       external reserve backing is a necessary condition" rest on categories assigned after the fact, with
       n = 2 / 7 / 1 / 2 and one algorithmic case.
     - Say instead: "in our 12 cases, the two closed-weekend cases recovered within 51–65 h; the one coin without
       external reserves (UST) never recovered". That is a description, not a test.
  3. **Category 4 "pré-deslistagem" (USDP Sep 2026).** The delisting is still `[verify]`; cite a source or call it
     "end of data on Binance".
  4. **SVB wording.** Recovery came with the Sunday deposit guarantee (D-13), before banks reopened. "Parity restored as soon
     as redemption became credible" is fair; "redemption reopened" is not.
- **Next step:** owner applies 1–4; then status → done.
- **How to resume:** `.venv/bin/python scripts/p3_04_depeg_chapter.py`.

## Log
- 2026-11-02, agent for Renzo: review done (Handoff): reproduces; mechanisms unsourced; F-019 claims overreach.
- 2026-11-02, agent for Renzo: Renzo takes the review.
- 2026-11-02, Felipe (Economist): claimed task; structured subtasks S1–S4; inspected `P1-07_v1_vs_v2.csv` and verified 11 USD-confirmed downward depeg events; checked pre-committed threshold ($11 < 12$), formally omitting Kaplan-Meier survival curves in accordance with `docs/01-depeg-recovery.md` §5 and decision log line 96; developed `scripts/p3_04_depeg_chapter.py`; created case table `P3-04_depeg_case_table.csv` and category summary `P3-04_category_summary.csv`; generated `P3-04_svb_weekend.png` and `P3-04_depeg_cases.png`; authored `findings/F-019-depeg-chapter.md`; drafted 2 chapter slides in Portuguese (`pt-BR`) in Result section; set status to review.

## Result

### Summary of Empirical Evidence
1. **The Economic Bridge to the Primary Project**:
   Both the domestic USDT/BRL premium and dollar stablecoin parity are governed by **limits to arbitrage**:
   - In Brazil, when formal banking/FX rails are closed or restricted (e.g. the 23 Jun 2026 supervisory notice), secondary market USDT drifts up to a premium of over 100 bps;
   - In the US dollar ecosystem, when primary issuer redemption rails close (e.g., commercial banks and Fedwire closing over the weekend following the Silicon Valley Bank failure), secondary market USDC drifts down to a discount of up to 1,950 bps intra-hour;
   - In both cases, as soon as credible 1:1 primary redemption is assured, market arbitrageurs close the gap immediately — in USDC's case, hours before commercial banks even opened on Monday morning.

2. **The Natural Experiment of the SVB Weekend (10–13 Mar 2023)**:
   - Circle held $3.3B (8.2% of reserves) at SVB when the FDIC placed it in receivership on Friday afternoon.
   - Bank wires (Fedwire/ACH) shut down for the weekend, eliminating Circle's ability to process primary 1:1 wire redemptions.
   - On secondary exchanges without primary arbitrage, USDC dropped to an hourly close low of **US$ 0.863** and intra-hour low of **US$ 0.805** on Saturday 11 Mar (07:00 UTC).
   - On Sunday 12 Mar at 22:15 UTC, the Federal Reserve, US Treasury, and FDIC announced a systemic risk exception guaranteeing all uninsured deposits.
   - Within 45 minutes (by 23:00 UTC Sunday), arbitrageurs bid USDC back to **US$ 0.989**, reaching US$ 0.991 at 12:00 UTC Monday before US banks opened, and US$ 0.999 at 14:00 UTC once wire redemptions resumed.

3. **Screen Results and Pre-Committed Rule**:
   - The automated screening across 7 major stablecoin pairs yielded exactly **11 USD-confirmed downward depegs** (9 excluding 2 USDP pre-delisting drift events in Sep 2026; 8 excluding UST's terminal collapse).
   - Pre-committed protocol (`docs/01-depeg-recovery.md` §5): Kaplan-Meier survival curves and Cox proportional hazard models require $n \ge 12$ independent events. Because $11 < 12$, KM survival curves were **strictly omitted**, avoiding spurious pooling of heterogeneous mechanisms.
   - The data was organized into a 4-category comparative taxonomy (`results/tables/P3-04_depeg_case_table.csv` and `P3-04_category_summary.csv`):
     * **Categoria 1 (Fim de semana bancário / canal de resgate fechado - USDC, USDP)**: 100% de recuperação em 51–65 horas;
     * **Categoria 2 (Fricções operacionais de liquidez/resgate - FDUSD, TUSD, UST pré-colapso)**: 100% de recuperação em mediana de 492 horas (21h a 2.719h), com piso restrito (US$ 0,954 a US$ 0,992);
     * **Categoria 3 (Insolvência algorítmica terminal - UST mai/2022)**: 0% de recuperação (colapso a zero e deslistagem);
     * **Categoria 4 (Deriva pré-deslistagem em exchange - USDP set/2026)**: 50% de recuperação em 60 horas.

---

### Polished Draft Slide Text in Portuguese (`pt-BR`)

#### Slide 1: O Mesmo Mecanismo em Dólares — O Fim de Semana do Silicon Valley Bank (SVB)
**Título:** O preço se afasta da paridade quando o canal bancário fecha — e volta antes dele reabrir
**Subtítulo:** Como o colapso do SVB em março de 2023 comprova os limites da arbitragem em stablecoins

- **O fechamento da porta bancária (Sexta-feira, 10 de março de 2023):**
  - A Circle (emissora do USDC) mantinha US$ 3,3 bilhões (8,2% do total de reservas) depositados no Silicon Valley Bank quando a FDIC decretou intervenção na sexta-feira à tarde.
  - Com o encerramento do expediente bancário e os trilhos de liquidação (Fedwire/ACH) fechados no fim de semana, o resgate primário oficial de US$ 1,00 ficou bloqueado.

- **O descolamento sem arbitragem (Sábado, 11 de março de 2023):**
  - Sem a âncora do resgate a US$ 1,00 operando no fim de semana, a pressão vendedora no mercado secundário derrubou o USDC para uma **mínima de fechamento de US$ 0,863** e **mínima intra-hora de US$ 0,805** (desconto de até 19,5%).
  - O mercado cobrava um prêmio maciço pela incerteza da perda de capital e pela iliquidez do fim de semana.

- **O anúncio conjunto e a volta imediata (Domingo, 12 de março de 2023):**
  - Às **22h15 UTC** (18h15 em Nova York), o Federal Reserve, o Tesouro dos EUA e a FDIC emitiram comunicado conjunto garantindo integralmente todos os depósitos do SVB.
  - A certeza de que os resgates bancários seriam honrados a US$ 1,00 na manhã seguinte ativou os arbitradores instantaneamente: às **23h00 UTC** (apenas 45 minutos após o anúncio), o USDC já saltava para **US$ 0,989**.

- **Conclusão:**
  - O preço retornou à paridade **antes mesmo da reabertura física das agências e dos trilhos bancários** na segunda-feira (quando atingiu US$ 0,999). A paridade é sustentada pela credibilidade do resgate; na ausência deste canal, os mercados secundários sofrem descontos severos.

*Figura do slide:* `results/figures/P3-04_svb_weekend.png` (Evolução horária Bitstamp USDC/USD com sombreamento dos horários bancários e linha vertical do comunicado conjunto).

---

#### Slide 2: Anatomia dos Depegs — Por que o Resgate e o Lastro Importam
**Título:** A anatomia dos descolamentos: moedas solventes recuperam a paridade; moedas sem lastro colapsam
**Subtítulo:** Triagem sistemática de 11 eventos confirma que a solvência do lastro dita a sobrevida das stablecoins

- **Rigor metodológico e regra pré-comprometida:**
  - A triagem automática em 7 pares de stablecoins identificou **11 eventos confirmados em dólar de queda abaixo de US$ 1,00** (9 excluindo deriva de deslistagem; 8 excluindo o colapso terminal da UST).
  - Em obediência ao plano pré-especificado ($n \ge 12$ para análise de sobrevida de Kaplan-Meier), evitou-se agregar artificialmente eventos de naturezas distintas. Os eventos foram estruturados em quatro categorias econômicas claras:

- **1. Fim de semana bancário / canal de resgate fechado (USDC, USDP — mar/2023):**
  - **Recuperação:** 100% dos eventos. **Duração:** 51 a 65 horas.
  - **Mecanismo:** Emissores plenamente solventes cujo resgate foi travado por calendário bancário. A paridade voltou tão logo a garantia do resgate foi restabelecida.

- **2. Fricções operacionais e liquidez secundária (FDUSD, TUSD, UST jan/2022):**
  - **Recuperação:** 100% dos eventos (7 casos). **Duração mediana:** 492 horas (21h a 2.719h).
  - **Piso de preço:** Desconto contido (mínimas entre US$ 0,954 e US$ 0,992).
  - **Mecanismo:** Dúvidas sobre custodiantes ou lentidão no processamento de resgates institucionais atrasam a arbitragem, mas a honra dos resgates preserva a paridade no médio prazo.

- **3. Colapso algorítmico e insolvência patrimonial (UST — mai/2022):**
  - **Recuperação:** 0% (colapso terminal para US$ 0,00 e deslistagem).
  - **Mecanismo:** Sem ativos de reserva externos e independentes, a corrida de saques gerou hiperinflação do token de suporte (LUNA). A perda da paridade foi permanente.

- **4. Deriva pré-deslistagem em exchange (USDP — set/2026):**
  - Descontos marginais resultantes de baixa liquidez nos dias anteriores à deslistagem da moeda na plataforma.

- **Implicação central para a regulação (BCB / FGV):**
  - Stablecoins fiduciárias com reservas segregadas e auditadas suportam choques severos de liquidez e preservam sua paridade; o risco crítico está nos gargalos operacionais e no horário de funcionamento dos trilhos bancários de resgate.

*Figura do slide:* `results/figures/P3-04_depeg_cases.png` (Painel A: Preço mínimo atingido por categoria; Painel B: Tempo até a recuperação em escala logarítmica com destaque para a UST permanente).
