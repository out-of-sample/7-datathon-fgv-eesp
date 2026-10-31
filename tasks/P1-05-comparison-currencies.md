---
id: P1-05
title: USDT premiums for the comparison currencies
phase: P1
status: done
owner: CS 2
working: -
due: 2026-11-01
depends: P1-01
---

## Goal
Build the same premium for other currencies (the "donor pool") so we can build a synthetic Brazil that did
not receive the 23 Jun 2026 shock.

## Subtasks
- [x] S1 — Binance 1h klines: `USDTTRY, USDTZAR, USDTUAH, EURUSDT, USDTMXN, USDTCOP, USDTPLN, USDTIDR, USDTARS`
   (coverage in `docs/02-dolar-cripto.md` §6). Note `EURUSDT` is quoted the other way round. — done: Renzo, 31 Oct
- [x] S2 — An official daily rate for each currency with its fixing time (central bank, FRED or ECB); record each
   source in `docs/sources.md` (D-05). — done: Renzo, 31 Oct
- [x] S3 — Daily premium per currency at a time matched to each fix (or a documented approximation). — done: Renzo, 31 Oct
- [x] S4 — Flag currencies with capital controls (ARS, UAH likely) and write the exclusion rule **before** fitting
   anything. — done: Renzo, 31 Oct (rule committed in 9ad0591, before the premiums were computed)

- [x] S5 — Independent review: reproduce outputs, audit quote direction, timestamps, coverage and exclusion rules. — done: Renzo (second agent), 31 Oct

## Success criteria
- [x] `data/processed/P1-05_donor_premiums_daily.csv` (date x currency, bps)
- [x] At least 4 currencies with full coverage 1 Nov 2025 - 30 Sep 2026
- [x] Exclusion rule written in the Result section before P2-04 starts

## Outputs
- `scripts/p1_05_donors.py`, `data/raw/binance/<PAIR>/`, `data/raw/fx_official/`, `data/processed/P1-05_donor_premiums_daily.csv`,
  `results/tables/P1-05_donor_coverage.csv`, finding F-010

## Handoff
- **State:** independent data review passed; status `done`. Production outputs reproduce byte for byte. An independent raw-data reconstruction matches the core pre/post periods within CSV rounding. Evidence and limits are in F-010 History.
- **Next step:** P1-06 screens donor events; the team confirms exclusions and the Brazil outcome definition at the P2 gate before P2-04 fitting. P1-09 records a non-blocking historical boundary defect.
- **Open questions:** IDR's pre-period start; PTAX versus ECB-based Brazil; primary-source verification of capital-control classifications and COP/UAH/ARS matching hours. These are not resolved by numerical reproduction. F-010 remains exploratory.
- **How to reproduce:** `.venv/bin/python scripts/p1_02_premium.py`, `.venv/bin/python scripts/p1_05_donors.py`, `.venv/bin/python scripts/p1_05_review.py`, `sha256sum --quiet -c data/raw/SHA256SUMS`. Existing frozen inputs are sufficient; no re-download required. Review tables are `results/tables/P1-05_review*.csv`.

## Log
- 2026-10-31, second agent for Renzo: S5 passed; independent raw reconstruction, coverage, raw checksums and quote-inversion negative check; historical UAH boundary defect deferred to P1-09; status → done. Corrected exclusion-rule commit reference and BCRA effective-date documentation.
- 2026-10-31, second agent for Renzo: claims S5 independent review with Renzo's approval; S1–S4 implementation stays unchanged during review.
- 2026-10-31, agent for Renzo: S1–S4 done; 654 Binance files + 4 official-rate files frozen, checksums added (1,177 OK); official files re-downloaded byte-identical; F-010; status → review
- 2026-10-31, agent for Renzo: exclusion rule written and committed (9ad0591) before any donor premium was computed
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

### Data and premiums (S1–S3)
`data/processed/P1-05_donor_premiums_daily.csv`: one row per date, one column per currency, bps. `BRL_ptax` is the P1-02
premium; `BRL_ecb` is Brazil measured the donor way (a check). Method and fix times in the script header and D-05.
Command: `python scripts/p1_05_donors.py` (table also in `results/tables/P1-05_donor_coverage.csv`).

| Currency | Binance pair, first hour (UTC) | Official rate | Matched at | Pre: fix days, share with premium | Post: fix days, share | Rule 3 |
|---|---|---|---|---|---|---|
| EUR | EURUSDT, 2020-01-03 | ECB | 14:00 Frankfurt | 160, 100% | 71, 100% | pass |
| TRY | USDTTRY, 2019-12-25 | ECB | 14:00 Frankfurt | 160, 100% | 71, 100% | pass |
| ZAR | USDTZAR, 2020-03-27 (gap Apr 2021 – Jun 2023) | ECB | 14:00 Frankfurt | 160, 100% | 71, 100% | pass |
| MXN | USDTMXN, 2024-04-10 | ECB | 14:00 Frankfurt | 160, 100% | 71, 100% | pass |
| COP | USDTCOP, 2024-06-05 | TRM | mean 08–13h Bogotá, previous weekday | 146, 100% | 65, 100% | pass |
| IDR | USDTIDR, **2025-11-29** | ECB | 14:00 Frankfurt | 160, **87.5%** | 71, 100% | **fail** |
| PLN | USDTPLN, ends **2026-07-01** | ECB | 14:00 Frankfurt | 160, 100% | 71, **7%** | **fail** |
| UAH | USDTUAH, ends 2026-09-28 | NBU | mean 10–16h Kyiv, calc day | 166, 100% | 71, 95.8% | pass (out by rules 1–2) |
| ARS | USDTARS, 2023-04-28 | BCRA A 3500 | mean 10–15h Buenos Aires | 149, 100% | 68, 100% | pass (out by rules 1–2) |

Six currencies have full coverage 1 Nov 2025 – 30 Sep 2026 (EUR, TRY, ZAR, MXN, COP, ARS), so the "at least 4"
criterion is met. **Donor pool after rules 1 and 3: EUR, TRY, ZAR, MXN, COP**; rule 2 waits for P1-06.

Checks:
- **Brazil measured the donor way** tracks the PTAX premium: correlation 0.79 over 1,510 days, mean difference +3.9 bps,
  and it finds the 23 Jun jump (+82.5 vs +93.9 bps). So the ECB-based measure works for the donors.
- **TRM dating:** dating the TRM to the previous weekday's trades gives a calmer COP premium (sd of daily change 52.4 vs
  77.0 bps for same-day dating). We use the previous weekday.
- Liquidity on Binance (Nov 2025 – Jun 2026, million USD a month): TRY 1,182, EUR 667, IDR 107, MXN 40, ZAR 19, COP 15,
  PLN 10 (Brazil 1,462). The thin ones give noisier premiums; the rule does not screen on liquidity. P2-04 may weight this.
- No Binance hour without trades at 12–13h UTC in the pre-period for any ECB currency; official-rate files have no
  duplicates or gaps beyond weekends and holidays.


### Independent review (S5)
Approved for the task's data-delivery criteria, not as a causal finding or final donor-selection decision.
The four ECB candidates EUR, TRY, ZAR and MXN and the approximate COP series reproduce; the exclusion rule
was committed in 9ad0591 before the results commit 3588cc7. Rule 2 still needs P1-06. The original
"ECB-based measure works" wording above is a measurement sanity check, not evidence of a good synthetic-control fit.

The BCRA formal notice A 8359 gives **2 Jan 2026** as the effective date of its new method (source D-11),
correcting the 1 Jan date in the original source-register description. The script header is corrected;
no premium values changed. Exact local matching hours remain documented approximations.
