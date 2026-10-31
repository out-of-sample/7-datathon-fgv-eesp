---
id: P1-05
title: USDT premiums for the comparison currencies
phase: P1
status: doing
owner: CS 2
working: Renzo
due: 2026-11-01
depends: P1-01
---

## Goal
Build the same premium for other currencies (the "donor pool") so we can build a synthetic Brazil that did
not receive the 23 Jun 2026 shock.

## Subtasks
- [ ] S1 — Binance 1h klines: `USDTTRY, USDTZAR, USDTUAH, EURUSDT, USDTMXN, USDTCOP, USDTPLN, USDTIDR, USDTARS`
   (coverage in `docs/02-dolar-cripto.md` §6). Note `EURUSDT` is quoted the other way round. — doing: Renzo
- [ ] S2 — An official daily rate for each currency with its fixing time (central bank, FRED or ECB); record each
   source in `docs/sources.md` (D-05).
- [ ] S3 — Daily premium per currency at a time matched to each fix (or a documented approximation).
- [ ] S4 — Flag currencies with capital controls (ARS, UAH likely) and write the exclusion rule **before** fitting
   anything.

## Success criteria
- [ ] `data/processed/P1-05_donor_premiums_daily.csv` (date x currency, bps)
- [ ] At least 4 currencies with full coverage 1 Nov 2025 - 30 Sep 2026
- [ ] Exclusion rule written in the Result section before P2-04 starts

## Outputs
- `scripts/p1_05_donors.py`, `data/raw/binance/<PAIR>/`, `data/raw/fx_official/`, `data/processed/P1-05_donor_premiums_daily.csv`

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** not started
- **Next step:** S1
- **Open questions:** none
- **How to resume:** -

## Log
- 2026-10-31, agent for Renzo: Renzo takes P1-05 (planned for Nattan; Renzo covers CS 2's P1 work and tells him)

## Result
### Donor exclusion rule (S4)
Written 31 Oct 2026 **before any donor premium was computed** (this commit precedes the first run of
`scripts/p1_05_donors.py` on Binance data). Proposed by the agent for Renzo; **the team confirms or changes it at the P2 gate,
before P2-04 fits anything.** It never uses the premium after 23 Jun 2026.

A currency enters the P2-04 donor pool only if all three hold:
1. **Market-set rate, open access.** Its official rate is market-determined and residents face no binding controls on
   buying US dollars at any time from 1 Nov 2025 to 30 Sep 2026.
2. **No rule change of its own around the shock.** No rule dated 1 Jun – 30 Sep 2026 that restricts or eases crypto or
   stablecoin purchases, or residents' access to FX (from P1-06, human-checked). Rules earlier in the pre-period are
   listed and handled by a robustness run without that currency.
3. **Data.** A premium on at least 90% of the currency's own fix days in both the pre-period (1 Nov 2025 – 22 Jun 2026)
   and the post-period (24 Jun – 30 Sep 2026). Hours without trades on Binance count as missing.

First screen, from public secondary sources (`[verify]`; P1-06 does the formal check):
- **ARS: out (rules 1, 2).** Companies are still under the "cepo" in 2026 and the BCRA said in Jul 2026 that lifting it
  is not a priority; cepo changes in the window (e.g. Com. "A" 8446, 11 Jun 2026).
  https://www.iprofesional.com/finanzas/455102-banco-central-argentino-revelo-que-levantar-cepo-cambiario-para-empresas-no-es-prioridad
- **UAH: out (rules 1, 2).** Martial-law FX controls since Feb 2022; an NBU easing package for individuals and firms took
  effect 11 Aug 2026, inside the post-period.
  https://unn.ua/en/news/the-national-bank-is-introducing-a-major-package-of-foreign-exchange-restrictions-easing-measures-how-the-limits-will-change
- **PLN: expected out (rule 3).** Binance `USDTPLN` ends in Jul 2026.
- **EUR:** Binance restricted USDT for EEA users under MiCA from about 31 Mar 2025 `[verify]`; before the window, so kept,
  but flagged for P1-06.
- EUR, TRY, ZAR, MXN, COP, IDR: rule 3 checked below; rule 2 waits for P1-06.
