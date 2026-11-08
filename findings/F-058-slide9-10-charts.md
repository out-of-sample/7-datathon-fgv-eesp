---
id: F-058
title: Source-backed slide 9 CUSUM and slide 10 conclusion graphics
status: exploratory
task: P5-13
date: 2026-11-08
checked_by: -
---

## Claim
Presentation of existing results only; no new fitted model or causal inference. CUSUM accumulated signal divided by its threshold exceeds one on 24 June 2026 (F-014). Before/acute premium means are 15.236551 and 109.143852 bps, a 93.907300 bps difference (F-016). Network benchmark 1–2 USDT per transfer is approximately 0.1–0.2 bps per US$100k (F-015 convention). Foxbit's volume share in the three observed exchanges is 6.798264% before and 34.738240% after (F-036, exploratory).

## Evidence
Reproduce: `python scripts/p5_13_final_charts.py` with pandas, numpy, matplotlib. Optional `DECK_FONT_DIR` points to full IBM Plex Sans Regular/Bold/Italic TTF files. Fonts in original PDF were subsets missing needed glyphs; final PNGs use complete IBM fonts downloaded from https://raw.githubusercontent.com/IBM/plex/master/packages/plex-sans/fonts/complete/ttf/IBMPlexSans-Regular.ttf and analogous Bold/Italic paths. Font repository inspected via https://github.com/IBM/plex/blob/master/packages/plex-sans/fonts/complete/ttf/IBMPlexSans-Regular.ttf on 8 Nov 2026.

- Source input hashes in `results/tables/P5-13_checks.json`.
- Plotted CUSUM series: `P5-13_cusum_source.csv`, 4 May–24 June 2026. Signal remains below threshold before 24 June; saved alarm column equals 1 on that day. Series ends on alarm day to avoid presenting the subsequent automatic reset as market normalization.
- Conclusion values: `P5-13_conclusion_source.csv`. Premium before 25 May–22 June vs after 24 June–21 July, 20 observations each. Before value is different from the longer 9 bps structural regime, intentionally matching event-study windows.
- Foxbit before period 1 May–22 June; after 22 July–30 October. Share recalculated from saved period venue sums and matches within 1e-5 percentage points.
- Network reference range comes from frozen Binance and domestic venue fee assumptions; no inferred confidence interval. Same zero-based linear bps scale as the incremental premium; tiny fee bar is not inflated.

## Caveats
Core source statuses retained; these are presentation assets, not independent teammate verification. CUSUM detects observed change, not advance warning of the notice; the simple baseline also detects 24 June (F-014). No claim of unique detection. Network fee range is a benchmark comparison, not a universal current price or all-in transaction cost. Foxbit share is not a national market share. No uploaded PDF or slide layout edited.

## Used in deck
Not inserted. Four transparent PNG/SVG pairs under `results/figures/P5-13_`: `09_cusum` for slide 9, and `10a_premio`, `10b_rede`, `10c_foxbit` for the three existing slide 10 conclusion columns. PNG dimensions: 3840×912 and 1824×888. SVG text converted to vector paths, avoiding a local font-install requirement. Colours match the supplied PDF: navy #14213D, blue #3B6EA8, orange #D9622B, muted #5B6573 and light grid #DDD7CC.

## History
- 2026-11-08 — Codex for Felipe: built and inspected four final PNGs, and a composite on the PDF's beige background at approximate insertion sizes; corrected CUSUM title clipping and subset-font missing glyphs. Verified source arithmetic. Earlier decks unchanged.
