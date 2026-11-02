---
id: P2-03
title: Before/after test for every dated rule, with placebo dates
phase: P2
status: review
owner: CS 2
working: -
due: 2026-11-02
depends: P1-02, P1-04
---

## Goal
For each rule in the event list, measure how the premium changed, including the rules that did nothing.
The 23 Jun 2026 row is also the number the AI analysts (extension A) are compared with.

## Subtasks
- [x] S1 — Mean premium in [-20, -1] vs [+1, +20] trading days around each effective date; Newey-West standard errors.
   Repeat with announcement dates where they differ. — done: Felipe, 2 Nov
- [x] S2 — 200 random placebo dates (same weekday distribution); report where each real event falls. — done: Felipe, 2 Nov
- [x] S3 — Baseline: pre-period mean (no-change forecast). — done: Felipe, 2 Nov

## Success criteria
- [x] `results/tables/P2-03_event_table.csv` with every P1-04 event, including nulls
- [x] Placebo distribution figure (`results/figures/P2-03_placebo_dist.png`)
- [x] Finding written (`findings/F-016-event-studies-placebos.md`)

## Outputs
- `scripts/p2_03_events.py`, table, figure, finding, `results/agentic/team_estimate.json`

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** Completed, in review. All 13 Brazilian events evaluated for effective and announcement dates across 20-PTAX-day windows.
- **Next step:** Review by CS 2 (Nattan/Renzo) or CS 3 (Jonathan).
- **Open questions:** None. All criteria met.
- **How to resume:** Re-run `python scripts/p2_03_events.py`.

## Log
- 2026-11-02, Felipe: Completed S1, S2, S3 in `scripts/p2_03_events.py`. Generated `results/tables/P2-03_event_table.csv`, `results/tables/P2-03_placebo_draws.csv`, `results/figures/P2-03_placebo_dist.png`, and `results/agentic/team_estimate.json`. Written `findings/F-016-event-studies-placebos.md`. Status -> review.
- 2026-11-01, Felipe (Economist gate call): For the 23 Jun 2026 shock, report both the acute 20-day spike window ([+1, +20] trading days, 24 Jun – 21 Jul, ~109 bps) and the post-adaptation plateau ([+21, +60] trading days, 22 Jul – Oct, ~27 bps) separately. Within-Brazil placebo distribution (200 random dates) serves as primary statistical p-value. Event 23 Jun 2026 is framed as empirically confirmed break across 3 venues coinciding with reported BCB supervisory ofício (ConJur secondary source, not public DOU norm).
- 2026-10-31, agent for Renzo (note from P2-02): the high regime after 23 Jun 2026 lasts about 20 PTAX days (24 Jun – 21 Jul; F-011), so the planned [+1, +20] window measures the spike almost exactly. The lasting effect is smaller (regime mean 9.3 → 26.8 bps after 22 Jul). Suggest reporting a later window too (e.g. [+21, +60]) as a pre-declared extra, decided before running.
- 2026-10-31, agent for Renzo (note from P3-03, nobody working here yet): the real-time monitor's upward sum starts building on 25 May 2026 and is at 92% of its threshold on 23 Jun; weekly premium 10–22 bps from mid-May vs 5.8 in Jan–Apr. Check a pre-trend before 23 Jun when fixing the windows (F-014).

## Result
Only the 23 Jun 2026 BCB supervisory ofício (E-05) moved the premium:
- Pre-mean (25 May – 22 Jun, 20 PTAX days): 15.2 bps
- Post-mean (24 Jun – 21 Jul, 20 PTAX days): 109.1 bps
- Jump: **+93.9 bps** ($t = 5.80$, Newey-West HAC $SE = 16.2$ bps, parametric $p = 6.44 \times 10^{-9}$)
- Empirical placebo p-value (vs 200 clean non-event draws, range -57.5 to +62.7 bps): **$p = 1/201 = 0.0050$** (100th percentile, 0/200 placebos exceeded +93.9 bps)
- Extended windows: Pre-trend [-40, -21] = 7.0 bps (drift +8.3 bps); Post-adaptation plateau [+21, +60] = 34.5 bps (+19.3 bps vs pre); Full plateau [+21, end] = 26.8 bps (+11.5 bps vs pre)
- Naive baseline RMSE: 103.1 bps vs post-regime RMSE 42.5 bps
- All other 12 Brazilian events produced changes between -5.3 and +15.4 bps ($p_{\text{placebo}} \ge 0.19$, inside normal noise).
