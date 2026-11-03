# P3-17 S1 — Did the stopped activity resume? Dated source table (23 Jun – 30 Oct 2026)

Built 2 Nov 2026 by the agent for Renzo, **before any premium, volume or order-size number around these dates was looked
at for this task**. Every quote was copied from the page or file named in the Source column (opened 2 Nov 2026).
Source IDs refer to `docs/sources.md`.

**The activity the notice stopped** (E-05.1, E-05.3): FX operations to import virtual assets in which an investment fund
acts as intermediary, i.e. buys abroad to supply a particular client in Brazil. Anything else (in-book arbitrage, imports
by authorised institutions, new rules on other channels) is not restoration.

**Classes.** *full restoration*: the BCB (or a rule) allows that activity again. *partial change*: it is allowed again for
some funds, institutions or structures (for example after a fund's "alinhamento" with the supervisor). *clarification*:
the BCB states or narrows what is covered, without allowing the activity. *substitution through another channel*: the same
supply moves through a different, permitted route. *no verified change*: the item does not change who may do the activity.

## Candidates

| # | Published (Brasília) | Effective | Source | Operative language (quoted) | Class | Why |
|---|---|---|---|---|---|---|
| C1 | 26 Jun 2026 (meeting; Cointelegraph Brasil 17:15) | 26 Jun 2026 | E-05.5 | "o Banco Central do Brasil manteve a suspensão das operações de câmbio ligadas a fundos cripto no país"; "O objetivo será explicar ao regulador como cada instituição identifica a finalidade econômica das transações e diferencia uma operação própria de uma estrutura de intermediação. Porém, até que esse alinhamento ocorra, as operações permanecerão suspensas."; "durante a reunião o BC 'liberou' a arbitragem de fundos cripto feita dentro do livro de ordens de exchanges" | clarification | Suspension kept. In-book arbitrage (the fund does not choose its counterparty) is a different activity. Sets the only stated route back: a per-institution alignment with the conduct supervisor (Decon). No source found says any alignment was completed. The draft 24-hour hold (E-12) was presented at the same meeting |
| C2 | 6 Jul 2026 (opinion) | – | E-05.10 (republished by Jornal Empresas & Negócios, 6 Jul) | "Em nova reunião, realizada em 26 de junho, a autarquia manteve a suspensão até o alinhamento com a área de fiscalização, mas, e o ponto é decisivo, reconheceu a necessidade de separar operações por conta própria, arbitragem de estruturas que efetivamente configurem intermediação" | no verified change | Restates C1 on 6 Jul; no resumption reported |
| C3 | 29 Jul 2026 (LAI answer reported; the answer itself is undated) | – | E-05.3, E-05.4 | "Portanto, pelas normas vigentes, os fundos não podem atuar como intermediadores de ativos virtuais e, assim, as operações de câmbio de importação de ativos virtuais por eles realizadas carecem do atributo de licitude" | no verified change | The BCB's own written position, published one week after the 22 Jul break: the restricted activity is unlawful "pelas normas vigentes" (Res. BCB 520's exhaustive list excludes funds). Restoring it would need a rule change; none was found (C6, C7) |
| C4 | 10 Aug 2026 | – | E-05.11 | "No fim do mês passado, o portal especializado em cripto Cointelegraph divulgou que, em uma reunião com o BC, também foi mencionada a suspensão de operações de câmbio envolvendo fundos de criptoativos." | no verified change | Contemporaneous press still describes a suspension; no resumption mentioned |
| C5 | 28 Aug 2026 (BCB press conference 27 Aug, reported) | – | E-16 | Fernando Rocha (BCB, Departamento de Estatísticas): "Essa redução das transações reflete um momento de reorganização do mercado de ativos virtuais num contexto de intensificação da regulação e da supervisão de conduta do Banco Central sobre esse setor, em especial as exigências de governança e de procedimentos para prevenção das operações de lavagem de dinheiro" | no verified change | The BCB's explanation of July's fall in stablecoin purchases abroad (F-024). It cites tighter supervision, not a reopening |
| C6 | 23 Sep 2026 (BCB 18:04; DOU 25 Sep) | art. 91: 1 Oct 2026 (ban applies from 6 Nov 2026); rest 1 Jan 2027 | E-14 | Res. BCB 589, art. 91: "É vedado, a partir de 6 de novembro de 2026, às instituições financeiras, às instituições de pagamento e às demais instituições autorizadas [...] realizar ou viabilizar operações no mercado de ativos virtuais que tenham como contrapartes instituições ou entidades que prestem serviços de ativos virtuais e não estejam autorizadas a funcionar no país" | no verified change | Reporting rules plus a one-week delay (30 Oct → 6 Nov) of the ban on unauthorised counterparties, which also drops the earlier exception "ou em processo de autorização". Tightens another channel; says nothing about funds' FX imports |
| C7 | 8 Oct 2026 (BCB 09:00; DOU 9 Oct) | 9 Oct 2026 (on publication) | E-13 | Res. BCB 599, new FX purpose code: "Ajustes de posição decorrentes de compra ou venda de ativos virtuais com instituições do exterior 99516". Voto 120/2026 §1: "Os recursos em moeda estrangeira obtidos a partir de tais operações [...] podem ser utilizados, entre outras finalidades, para a aquisição de ativos virtuais no exterior que podem ser posteriormente ofertados aos clientes dessas instituições por meio da prestação de serviços de ativos virtuais no Brasil, conforme a regulamentação em vigor." | clarification | A record-keeping code for **institutions authorised to operate in FX**, not funds, for a channel the vote calls already permitted ("conforme a regulamentação em vigor"). Let's Money (13 Oct): "A resolução não cria atividade permitida nem mexe em vedação". The vote (§3) says this channel had produced an "acúmulo progressivo de posição de câmbio comprada", which shows that authorised institutions were importing (no date or amount). §5: a public consultation on virtual-asset services in the FX market is planned for Q4 2026, with a rule "no primeiro semestre de 2027" |
| C8 | 18 Jul 2026 | – | M-05 | Livecoins on Foxbit Infra: "uma fatia de mais de 41% do volume de USDT e USDC negociado no país nas últimas duas semanas" | substitution through another channel (company claim, not verified) | An exchange's institutional desk (own market making, liquidity for banks and fintechs) could replace supply the funds used to bring. Nothing in the source says it imports through FX or replaces the funds. Company claim, no independent check |
| C9 | 1 Jul 2026 (BCB 18:01) | 1 Jan 2027 | E-10 | Res. BCB 580: "devem observar, a partir de 1º de janeiro de 2027, os seguintes regramentos" | no verified change | Prudential classification of crypto firms. Not about funds or FX imports |
| C10 | 2 Jul 2026 (DOU 3 Jul) | 3 Jul 2026 | E-15 | IN BCB 756: "as informações [...] devem ser remetidas ao Banco Central do Brasil a partir da data-base de novembro de 2026" | no verified change | Moves a reporting start date to match Res. 574 (E-11) |
| C11 | 7 Aug 2026 | 1 Jan 2027 | E-06b | Res. BCB 584, art. 2-B: "somente podem executar ordens de transferência desses ativos vinte e quatro horas após o recebimento dos respectivos recursos de aporte na carteira" | no verified change | Tightens outgoing transfers; not about funds' imports |
| C12 | 7 Jul 2026 | – | M-04 | "uma parceria estratégica com a NovaDAX, corretora que está encerrando suas operações no país" | no verified change | Client migration between exchanges; not a supply channel |

## Screening log (what was searched and found nothing)

- **BCB normativos, 20 Jun – 31 Oct 2026** (`scripts/p3_17_restoration.py`, part A → `results/tables/P3-17_bcb_screen.csv`):
  893 items (779 Comunicados, 35 Resoluções CMN, 35 INs BCB, 29 Resoluções BCB, 15 others). Every non-Comunicado subject was
  read. Comunicados flagged by keyword are FX auctions, swap rollovers or authorisation notices for named FX brokers.
  Read in full on 2 Nov (text via the normativos API): Res. BCB 588, 589, 591, 599; IN BCB 756, 757, 761; Res. CMN 5.343
  (Res. BCB 584 was opened earlier, E-06b). Only 589 and 599 deal with virtual-asset services in a way that touches FX or
  counterparties (C6, C7); 588 and 591 add, to the Coaf reporting list (Circular 3.978, art. 49), "as operações relativas a
  transferências de ativos virtuais para ou de carteiras autocustodiadas de valor igual ou superior ao equivalente a
  US$10.000,00"; 757 and 761 do not mention virtual assets or funds; CMN 5.343 is about FIDCs. No normativo mentions
  investment funds' FX operations.
- **BCB press notes and news, 17 Jun – 29 Oct 2026** (same script; 115 items). Read: 21167 and 21191 (Res. 575, foreign-currency
  accounts for exporters and firms with foreign debt or capital, from 1 Oct; no funds, no virtual assets), 21192 (Res. 580),
  21218 and 21224 (Res. 584), 21267 (Res. 589), the external-sector notes 21210, 21243, 21274, 21295 (short stubs; their PDF
  annexes were not opened) and 21298 (Financial Stability Report). None mentions the funds' operations.
- **Relatório de Estabilidade Financeira, Oct 2026** (https://www.bcb.gov.br/content/publicacoes/ref/202610/RELESTAB202610-refPub.pdf,
  opened 2 Nov 2026): no mention of virtual assets, crypto or stablecoins.
- **Web searches (2 Nov 2026)**, Portuguese and English: BCB "liberou"/"retomada"/"autoriza" funds' FX imports; funds
  "voltam a operar"; ABToken; CVM ofícios-circulares on funds and virtual assets (2026); "alinhamento"/Decon; IOF on funds'
  foreign investments (2026); Cointelegraph Brasil (the outlet that broke the story) restricted search; Exame; one extended
  search. Results repeat C1–C5 or predate the notice. No source reports a resumption, a completed alignment, or a fund or
  bank saying it resumed.
- **Not searched**: CVM fund filings (fato relevante, regulamentos) one by one; BCB's Sistema Câmbio data by purpose code
  (not public at this detail).

## Result of S1

**No candidate is classed full restoration or partial change.** The only stated route back is the per-institution
alignment of C1, which is confidential and has no public date. The BCB's own later statements (C3, published 29 Jul;
C5, 27 Aug) describe the activity as unlawful under current rules and the market as reorganising under tighter
supervision. The one later rule that touches crypto imports through FX (C7, 9 Oct) records a channel for authorised
institutions, not funds, and does not change what is allowed.

Under the S2 rule ("credible" = any row classed full or partial restoration), **the credible set is empty**: the
reopening test cannot be run. This does not mean the June notice had no effect; it means we cannot observe the opposite
move.
