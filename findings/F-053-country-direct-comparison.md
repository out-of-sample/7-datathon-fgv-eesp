---
id: F-053
title: Direct comparison separates ordinary USD exchange-rate moves from the Brazilian USDT premium jump
status: exploratory
task: P3-46
date: 2026-11-08
checked_by: -
---

## Claim
Across fixed calendar windows around the 23 June 2026 Brazilian notice, the official dollar rose 1.03% in reais, while Brazil's USDT premium over that dollar rose 93.91 basis points (bps). The five comparison currencies' official dollar rates moved by −6.12% to +1.62%, but their USDT premiums changed by −39.91 to −0.55 bps. Argentina, excluded from the control group, had a +3.42% official-dollar change and +62.69 bps premium change. This direct comparison needs no synthetic weights; the Argentine rise shows why the comparison-group rule matters.

## Evidence
Before: 25 May–22 June 2026; after: 24 June–21 July 2026. Each country uses its own available aligned observations within the same calendar windows. A positive official-rate change means one USD costs more units of that country's currency. A premium change is in basis points, after removing the official USD rate and USDT/USD, following P1-05.

| Country | Currency | Days before/after | Official USD change | USDT premium change |
|---|---:|---:|---:|---:|
| Brazil | BRL | 20/20 | +1.03% | +93.91 bps |
| Euro area | EUR | 21/20 | +1.53% | −0.55 bps |
| Turkey | TRY | 21/20 | +1.62% | −15.12 bps |
| South Africa | ZAR | 21/20 | +0.38% | −39.91 bps |
| Mexico | MXN | 21/20 | +1.07% | −12.31 bps |
| Colombia | COP | 17/17 | −6.12% | −34.79 bps |
| Argentina (illustrative; excluded from the donor pool) | ARS | 19/18 | +3.42% | +62.69 bps |

The Brazilian +93.91 bps reproduces F-016 after rounding. This table uses the 20-day event window, whereas F-017's donor-average difference-in-differences uses its longer pre-period and common trading days; do not compare the two row-for-row.

Reproduce: `.venv/bin/python scripts/p3_46_country_direct_comparison.py` → `results/tables/P3-46_country_direct_comparison.csv`. Inputs: frozen `data/processed/P1-05_donor_premiums_daily.csv`, `data/processed/P1-02_premium_daily.csv`, `data/raw/fx_official/ecb_exr.csv`, `data/raw/fx_official/trm_cop.csv`, and `data/raw/fx_official/bcra_a3500.json`. Original source register: `docs/sources.md` D-02, D-05 and D-11.

## Caveats
- Descriptive comparison at a single Brazilian event date; no country placebo p-value or independent local event screen is added here. It neither identifies a cause nor establishes statistical significance on its own.
- USD exchange-rate changes reflect ordinary currency movements; the USDT premium subtracts those movements. Comparing raw USD prices alone would conflate the two questions.
- Colombian TRM trade-day alignment is marked `[verify]` in P1-05/D-05, and Colombia has fewer aligned days.
- Argentina is not an eligible control under P1-05's pre-specified rule: capital controls remained, and P1-05 records an Argentine FX-rule change on 11 June 2026, within the pre-window. The event classification was based on secondary-source screening and still warrants primary-source verification. The observed +62.69 bps cannot be attributed to the Brazilian notice or to the Argentine rule from this table.
- Country data and time matching follow the frozen P1-05 series. This new table has not been independently reproduced by a teammate.

## Used in deck
Not used; candidate simple companion or replacement for the synthetic-control explanation, subject to team decision.

## History
- 2026-11-08 — Codex for Renzo: added Argentina as an excluded illustration, without changing the original five-country donor interpretation.
- 2026-11-08 — Codex for Renzo: created from frozen data in response to a direct country-comparison request; exploratory.
