---
id: F-023
title: Two outlets saw the 23 Jun notice (or an excerpt) the next days, the BCB confirmed its position in writing, and the price moves they reported match our premium series
status: exploratory
task: P3-09
date: 2026-11-02
checked_by: -
---

## Claim
The 23 Jun 2026 notice is documented by two news reports from outlets that had the document or an excerpt
(Cointelegraph Brasil 24 Jun; Exame 25 Jun) and by the BCB's own written answer to an information request (LAI),
not only by later opinion pieces. The price moves the press reported (about 0.1% before, 1–2% at the peak on 24 Jun,
0.5% on Friday 26 Jun) match our premium series in size and timing: 15 bps before, an hourly peak of 246 bps on
24 Jun, 76 bps on 26 Jun, then back to 130–160 bps.

## Evidence
- Sources, each opened on 2 Nov 2026 with a quote checked against the page text: `docs/sources.md` → "E-05: every
  source found" (E-05.1 to E-05.10).
  - E-05.1 Cointelegraph Brasil, 24 Jun: "segundo uma notificação compartilhada com o Cointelegraph Brasil"; the
    notice orders the "imediata descontinuidade desse tipo de operação".
  - E-05.2 Exame, 25 Jun: quotes "um trecho da notificação ao qual a EXAME teve acesso"; 13 banks notified; ABToken:
    the funds "usavam contas em bancos para comprarem criptomoedas no exterior e depois venderem esses ativos para as
    corretoras" ("um choque de oferta").
  - E-05.3 the BCB's LAI answer (Cointelegraph Brasil, 29 Jul): "as operações de câmbio de importação de ativos
    virtuais por eles realizadas carecem do atributo de licitude".
  - E-05.5 Cointelegraph Brasil, 26 Jun: the suspension was kept; the BCB allowed funds' arbitrage inside exchange
    order books.
  - E-05.10 (Brotto, reported): the fund channel paid zero IOF-Câmbio (Decreto 6.306/2007, art. 15-B, III) against
    3.5% for ordinary buyers.
- Our series, 22–30 Jun 2026 (bps; hourly values use the last published PTAX):

| Day (UTC) | Hourly min | Hourly median | Hourly max | Daily (PTAX window) |
|---|---|---|---|---|
| Mon 22 Jun | −8 | 29 | 57 | 23 |
| Tue 23 Jun (notice) | 36 | 70 | 107 | 25 |
| Wed 24 Jun | 69 | 96 | 246 | 155 |
| Thu 25 Jun | 79 | 161 | 189 | 184 |
| Fri 26 Jun (meeting) | 11 | 80 | 169 | 76 |
| Mon 29 Jun | 104 | 129 | 161 | 140 |
| Tue 30 Jun | 116 | 134 | 178 | 131 |

  Pre-notice level (mean of the 20 PTAX days to 22 Jun): 15.2 bps.
- Reproduce: `python scripts/p3_09_press_check.py` → `results/tables/P3-09_press_vs_series.csv`.

## Caveats
- The BCB's full text has not been seen; what we know of its content comes from E-05.1, E-05.2 (excerpt) and the LAI
  answer. The notice was not published in the DOU.
- The press "spread" is not one defined measure: E-05.6 calls it a level "acima do mercado", E-05.7 a bid-ask difference.
  The match is in size and timing, not a test.
- The premium was already moving on 23 Jun in the hours after the PTAX window (hourly median 70 bps against 29 the
  day before), consistent with a notice sent on 23 Jun; the hour it was sent is not known.
- E-05.3 is the BCB's position on fund imports, not a confirmation of the notice's date or wording.

## Used in deck
Not yet (candidate: the "notice and its sources" slide).

## History
- 2026-11-02, agent for Renzo: created (P3-09 sweep). Exame 25 Jun was first pointed out by another agent's review.
