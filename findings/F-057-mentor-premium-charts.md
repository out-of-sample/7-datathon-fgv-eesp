---
id: F-057
title: Full daily premium history includes negative days and larger isolated peaks than June 2026
status: exploratory
task: P5-12
date: 2026-11-08
checked_by: -
---

## Claim
Across 1,520 PTAX observations from 13 October 2020 to 30 October 2026, the deck's USDT/USD-adjusted premium is negative on 85 days (5.59%). The literal USDT/BRL price divided by PTAX premium is negative on 99 days (6.51%). Therefore the feedback phrase "never cheaper than PTAX" cannot be used literally. The adjusted daily maximum is 3.61393% on 23 February 2021; June 2026 is not the highest daily premium in this history. Claims about a persistent structural change remain separate, based on the frozen break analysis.

## Evidence
Reproduce: `python scripts/p5_12_mentor_charts.py` with pandas, numpy and matplotlib installed.

- Adjusted premium: `100 * [USDTBRL / (PTAX_sell * USDTUSD) - 1]`. Minimum −1.27522% on 26 September 2022; maximum 3.61393% on 23 February 2021.
- Direct PTAX premium: `100 * [USDTBRL / PTAX_sell - 1]`. Minimum −1.31278% on 17 November 2022; maximum 3.60617% on 23 February 2021.
- Data checks: unique dates, no missing premiums, arithmetic recalculation matches both saved series within 1e-8 bps. Two observations have fewer than four window hours, fourteen have uncertain-window flags; retained, following the original series rather than changing sample rules after the freeze.
- Country before/after means reproduce F-053 within 0.02 bps: Brazil +93.9073 bps (20/20 observations); EUR −0.55095 bps (21/20); MXN −12.30726 bps (21/20). Before: 25 May–22 June; after: 24 June–21 July 2026. Brazil is measured at PTAX, euro and Mexico at their ECB reference.
- Inputs and SHA256 hashes: `results/tables/P5-12_checks.json`. Exact plotted historical data: `P5-12_historical_daily.csv`; country data: `P5-12_country_daily_pct.csv` and `P5-12_country_before_after.csv` under `results/tables/`.
- Sources reused from the frozen study: Binance, BCB PTAX and ECB, registered in `docs/sources.md` and scripts P1-02/P1-05. No new download or external economic fact was added.

## Caveats
Charts describe the existing frozen snapshot, not refreshed market data. They retain isolated daily observations without independently establishing their economic cause. Historic lines retain all daily values; a 20-observation rolling mean is secondary. Cross-country time series uses trailing five observations separately for each market and shows smoothing explicitly. Country fix times and holiday calendars differ. F-053 country differences are descriptive, not a new causal estimate or significance test. Mexico is the peso selected because it is a highlighted donor in deck v4, not Argentina. Argentina remains excluded from the clean control pool.

## Used in deck
Not inserted. Four PNG/SVG pairs available in `results/figures/`: `P5-12_01_premio_historico` (same definition as deck), `P5-12_01b_premio_ptax_direto` (literal PTAX comparison), `P5-12_02_brasil_euro_peso` and `P5-12_03_variacao_por_moeda`. PNGs are 3200×1600 pixels, using the supplied deck's background and palette. Recommended candidates: historical chart for slide 2; country time series or change bars for slide 5. Preserve the synthetic-control inference if replacing its graphic.

## History
- 2026-11-08 — Codex for Felipe, follow-up: expanded comparison to all five slide-5 donors in the requested order: EUR, MXN, TRY, ZAR, COP, alongside Brazil. New PNG/SVG pairs `P5-12_02_brasil_cinco_moedas` and `P5-12_03_variacao_cinco_moedas`; earlier three-currency images retained. Six-row data tables now supersede their initial three-row versions. All six differences match F-053 within 0.02 bps. Additional changes: TRY −15.11748 bps, ZAR −39.90905 bps (both 21/20 days), COP −34.79353 bps (17/17 days). Labels, full ranges and country caveat inspected in both final renders. No new causal inference. Coloured lines show individual markets, not the synthetic weighted combination.
- 2026-11-08 — Codex for Felipe: created from the mentor feedback. Recalculated arithmetic and F-053 comparison, inspected all four final PNGs, corrected bar-chart left-label clipping and stray horizontal guide. No independent teammate review yet.
