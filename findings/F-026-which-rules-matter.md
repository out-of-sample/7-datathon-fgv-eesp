---
id: F-026
title: Of eight dated Brazilian rules, only the confidential, immediate notice of 23 Jun 2026 moved the premium detectably; the published rules, with 1 to 175 days of notice, stayed within the range of ordinary dates
status: frozen
task: P3-12
date: 2026-11-02
checked_by: Felipe
---

## Claim
Ordered by how they reached the market, the eight dated rules split cleanly. The one confidential notice with immediate
effect (23 Jun 2026, E-05) moved the premium +94 bps, beyond every ordinary date (p ≈ 0.001). The seven others (a
presidential IOF decree, its suspension by Congress and the STF, four BCB resolutions and an IOF proposal) were public,
most with weeks or months of notice, and every change at announcement or entry into force stayed inside the range of
ordinary dates (−35 to +38 bps). For a regulator, the premium shows which rule closed the channel arbitrageurs actually
used. This is a rearrangement of P2-03 (F-016), not a new estimate.

## Evidence

| Rule | How issued | Notice | Change at announcement, bps (p) | Change at entry into force, bps (p) |
|---|---|---|---|---|
| E-01 IOF-Câmbio decree, 22 May 2025 | presidential decree | 1 day | +13.2 (0.38) | +15.4 (0.31) |
| E-01b Congress and STF suspend it, 27 Jun 2025 | legislative decree, STF injunction | 7 days | −23.9 (0.16) | −24.9 (0.15) |
| E-02 Res. BCB 519–521, 10 Nov 2025 | BCB resolution | 84 days | −3.8 (0.75) | −4.3 (0.72) |
| E-04 Res. BCB 521 art. 4 (reporting) | BCB resolution (announced with E-02) | 175 days | – | +7.2 (0.61) |
| E-03 IOF on crypto purchases, 5 Feb 2026 | Fazenda proposal, never enacted | – | −2.1 (0.84) | – |
| E-06a Res. BCB 561 (stablecoins out of eFX), 30 Apr 2026 | BCB resolution | 154 days | +6.0 (0.65) | −5.3 (0.68) |
| **E-05 BCB notice on funds' FX imports, 23 Jun 2026** | **confidential supervisory notice** | **immediate** | – | **+93.9 (0.001)** |
| E-06b Res. BCB 584 (24-hour hold), 7 Aug 2026 | BCB resolution | 147 days (in force after the sample) | −22.0 (0.19) | – |

Change = mean premium 20 PTAX days after minus 20 before (P2-03); p = two-sided placebo p over all 1,073 clean dates.
Ordinary-date range = 2.5–97.5% of the 200 P2-03 placebo draws: −35.0 to +37.6 bps. Sources for each rule:
`docs/sources.md` (E-01 to E-06b; E-05.1 and E-05.2 for the notice).

Reproduce: `python scripts/p3_12_rules.py` → `results/tables/P3-12_rules.csv`, `results/figures/P3-12_rules.png`.

## Caveats
- **Res. BCB 574 omitted from the frozen eight-rule comparison.** Registered by the BCB on 18 Jun and published on
  22 Jun 2026 (E-11), it requires reporting of virtual-asset operations carried out from 3 Nov. The premium rose
  37.7 bps on 18→19 Jun (F-029), but that one-day rebound does not identify the resolution's effect. A 20-day window
  around its publication includes the 24 Jun jump after the notice, so the event test cannot separate the two.
  Renzo chose an explicit deck/annex caveat in P3-16, without changing this frozen estimate.
- **Form and content move together.** The notice was the only confidential, immediate rule *and* the only one that
  closed the funds' import channel (F-024). The chart cannot say which of the two mattered.
- **"No effect" means "no effect above about 35 bps".** Smaller effects would not be detected.
- **One treated rule.** The contrast rests on a single confidential notice.
- E-01b's announcement date (27 Jun 2025) is also the day Binance cut the USDT/BRL tick size (M-03); their changes are
  the same number and cannot be separated.
- Hypotheses were written after the probe had seen the 23 Jun jump (`docs/02-dolar-cripto.md` §3); the other rules
  serve as within-Brazil placebos with that caveat (H2).

## Used in deck
Slide 6 (`deck/deck_v1_ptbr.md`) & Anexo A (`deck/annex_v1_ptbr.md`).

## History
- 2026-11-05, Codex for Renzo (P3-16): added the E-11 omission caveat after Renzo chose the caveat route; estimate and eight-row table unchanged, independent Claude review requested.
- 2026-11-04, agent for Renzo (P4-03, Renzo's decision): status confirmed -> frozen (tag `results-frozen`); from now on only bug fixes, each disclosed here
- 2026-11-02, agent for Renzo: created (P3-12).
