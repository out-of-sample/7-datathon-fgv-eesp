# P3-15 — Routes that can bring dollars or USDT into Brazil, before and after the 23 Jun 2026 notice

Built 2 Nov 2026 by Renzo's agent, after the S2 rule was committed (`6393330`, `tasks/P3-15-route-comparison.md`).
No script: costs come from F-015 (`results/tables/P3-01_route_costs.csv`, sources R-01, R-01b, R-02); statuses from the
E-05 sources. Framing rule (`docs/02-dolar-cripto.md` §10): this table measures frictions across legal categories; it
does not say which routes are lawful for virtual assets or recommend any of them.

**Units.** All-in cost = bank FX spread (20 bps, R-01) + wire (2.5 bps, R-01b) + IOF-Câmbio (R-02), in bps of the
dollar amount, as in F-015. $e_r$ = all-in cost minus the closed funds' route (22.5 bps). $g_r$ = all-in cost minus the
pre-notice premium (15.2 bps, F-022). "Close to the spike" = [+73.7, +128.3] bps (F-022).

| # | Route | Who can use it (per source) | IOF | All-in, bps | $e_r$ | $g_r$ | Adds USDT supply in Brazil? | Before 23 Jun | After 23 Jun | Sources |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Funds' FX import **with intermediation**: a fund buys virtual assets abroad and delivers them to local agents | Investment funds (the BCB's concern: "que caracterize a atividade de intermediação por parte de fundos de investimento") | 0% (art. 15-B, III) | 22.5 | 0 (reference) | 7.3 | **Yes**: "esses fundos usavam contas em bancos para comprarem criptomoedas no exterior e depois venderem esses ativos para as corretoras" (ABToken, E-05.2) | In use | **Closed**: "imediata descontinuidade" (E-05.1); suspension kept on 26 Jun "até que esse alinhamento ocorra" (E-05.5) | E-05.1, E-05.2, E-05.5, E-05.10, R-01, R-01b, R-02 |
| 2 | Funds' **own-account** investment abroad, including arbitrage inside exchange order books | Investment funds within CVM limits | 0% (art. 15-B, III) | 22.5 | 0 | 7.3 | **Unknown**: arbitrage funds "ajudam a reduzir diferenças entre exchanges locais e plataformas internacionais" (E-05.5), but no source says how their USDT entered Brazil after 26 Jun | Open | **Unknown**: on 26 Jun the BCB "'liberou' a arbitragem de fundos cripto feita dentro do livro de ordens de exchanges" (E-05.5); Brotto (opinion): the notice "não atinge o fundo que investe" (E-05.10); the line between own account and intermediation was still being agreed with the BCB (E-05.5) | E-05.5, E-05.10, R-02 |
| 3 | Ordinary purchase of foreign currency / availability abroad | Residents: "pessoa física ou pessoa jurídica não financeira" (E-05.10) | 3.5% from 23 May 2025 | 372.5 | 350 | 357.3 | **Unknown**: Brotto compares the funds' 0% with this 3.5% for importing crypto ("vantagem de até 3,5%", E-05.10, opinion); no source says how much crypto it carries | Open | Open (rate in force, R-02, R-03; no E-05 source concerns it) | E-05.10, R-02, R-03 |
| 4 | Remittance abroad "com finalidade de investimento" | Residents (R-02 quote is elided; who qualifies is not quoted) | 1.10% (Dec. 12.467, XXI-A) | 132.5 | **110** | **117.3** | **Unknown**: no opened source says purchases of virtual assets abroad fall in this category | Open | Open as a tax category (R-02); use for virtual assets unknown | R-02 |
| 5 | Goods-import FX | Importers of goods | 0% (art. 15-B, I) | 22.5 | 0 | 7.3 | **Unknown** `[not opened]`: no opened source on whether it can carry virtual assets (Res. BCB 561 concerns eFX settlement, E-06a, not opened with a quote) | Open | Open as a category; not mentioned in the E-05 sources | R-02 |
| 6 | USDT or dollars **already abroad** (held by residents or non-residents), moved on-chain to a Brazilian exchange and sold for reais | Anyone holding USDT abroad | None on the on-chain transfer itself `[not opened]` | **Not measured**: on-chain fee ~0.1 bps and exchange fee ~10 bps (R-04 `[link not opened]`), plus the cost of having the dollars abroad, which depends on how they got there (routes 1-5) or on an existing stock | – | – | **Unknown** (no source) | Open | **Unknown**: no source says it changed; the 24-hour hold of Res. BCB 584 applies only from 1 Jan 2027 and only to outgoing transfers (E-06b) | R-04, E-06b |

**Not routes into Brazil, but sources of USDT supply:** stocks already held in Brazil (exchanges, market makers,
holders) and domestic OTC/P2P desks. They move existing USDT; they can supply the market for a while without any route
being open. The press reports that the BCB's concern was "operações fora do livro de ordens, especialmente negociações
P2P ou OTC entre partes relacionadas" (E-05.6). Cost not measured.

## Applying the S2 rule

| Condition (S2) | Result | Why |
|---|---|---|
| 1. Exactly one route with $e_r$ and $g_r$ in [+73.7, +128.3] | **Holds** | Route 4 only ($e$ = 110, $g$ = 117.3). Routes 1, 2, 5: 0 / 7.3. Route 3: 350 / 357.3. Route 6: not measured |
| 2. That route is open after 23 Jun and adds USDT supply (opened sources) | **Fails** | Route 4 is open as a tax category, but no opened source says it can carry virtual assets (supply = unknown) |
| 3. Every cheaper route is closed or adds no supply (opened sources) | **Fails** | Route 2 (0% IOF): status and supply unknown. Route 5 (0%): supply unknown. Route 6: cost not measured, status unknown. Routes 2 and 5 alone are enough for the failure |
| 4. Every component of $e_{r*}$ from an opened source | Holds | $e$ for route 4 is the IOF difference, 1.10% − 0% (R-02, opened by Felipe's agent; art. 15-B, III opened by Felipe) |

**Outcome (b): we cannot identify the marginal route.** Route 4's excess cost (110 bps over the closed route) lies
inside the spike's range (+73.7 to +128.3 bps; synthetic control +109.3). Under the rule this is a **coincidence of
magnitude we cannot interpret**, not a candidate: no source shows that route carries virtual assets, and cheaper routes
of unknown status were open.

## Bound check (pre-committed; answers "why not +350")

| Window | Days | Highest daily premium | On | Minus pre-notice level (15.2) | Below 350? |
|---|---|---|---|---|---|
| 24 Jun – 30 Oct 2026 | 91 | 185.9 bps | 3 Jul 2026 | **170.7 bps** | Yes |
| 22 Jul – 30 Oct 2026 | 71 | 67.3 bps | 5 Oct 2026 | **52.1 bps** | Yes |

The premium never came near the 3.5% route's excess cost on any day after the notice. That route was an upper
bound that never became binding: on every day, some USDT was supplied at a lower cost, or buyers who would have paid 3.5%
stopped buying. The data do not say which.

Command: see `findings/F-028-route-comparison.md`.

## Notes on sources

- **Inciso number of the 3.5% rate.** R-02 gives Dec. 12.466, art. 15-B, **XXI**; Brotto (E-05.10, opened 2 Nov 2026 by
  Renzo's agent) writes "nos termos do inciso **XXIV** do mesmo artigo 15-B". The rate agrees (3.5%); the numbering may
  differ between the original decree and the consolidated text after Dec. 12.499/2025. Planalto blocks automated
  requests, so this agent could not check; Felipe (owner of R-02) can, in a browser.
- New quotes used above, opened 2 Nov 2026 by Renzo's agent (curl, text copied from the page): E-05.1 "ilegalidade das
  operações de câmbio para a finalidade de importação de ativos virtuais que caracterize a atividade de intermediação
  por parte de fundos de investimento"; E-05.5 "Porém, até que esse alinhamento ocorra, as operações permanecerão
  suspensas"; E-05.6 "estaria em operações fora do livro de ordens, especialmente negociações P2P ou OTC entre partes
  relacionadas"; E-05.10 "A interrupção determinada pelo Banco Central não atinge o fundo que investe; atinge o fundo
  que, a pretexto de investir, intermedeia" and "O investidor comum, pessoa física ou pessoa jurídica não financeira,
  enfrenta outro regime. Quando compra moeda estrangeira pelo canal convencional, paga IOF-Câmbio à alíquota geral de
  3,5%, nos termos do inciso XXIV do mesmo artigo 15-B".
- The SWIFT fee in F-015 (US$ 25 = 2.5 bps) differs from R-01b (R$ 100 = US$ 18.59 = 1.9 bps). It cancels in $e_r$ and
  moves $g_r$ by 0.6 bps; no condition changes.
