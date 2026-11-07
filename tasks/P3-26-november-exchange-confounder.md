---
id: P3-26
title: Audit the Binance security incident as a competing explanation for the November readout
phase: P3
status: review
owner: Economist
working: -
due: 2026-11-07
depends: P3-20
---

## Goal
Disclose and assess a newly located exchange event around P3-20's baseline and November observations. Preserve the registered prediction and scoring rule; do not turn a post-outcome audit into a new preregistration.

## Subtasks
- [x] S1 — Confirm the withdrawal suspension and asset-specific restoration timeline from Binance primary announcements, including USDT and the networks relevant to Brazilian arbitrage. — done: Felipe, 7 Nov (M-11, M-12, FBI/TRM Labs attribution; attack onset 29 Oct 20:05 UTC, withdrawals suspended, 98% replenished by 31 Oct)
- [x] S2 — Map the verified timeline to P3-20's existing pre/post windows and venue comparisons; state what can and cannot be separated. Any additional numerical analysis needs a retrospective specification and isolated outputs. — done: Felipe, 7 Nov (`scripts/p3_26_binance_incident_audit.py`, `results/tables/P3-26_incident_timeline.csv`, `results/tables/P3-26_window_sensitivity.csv`, `results/P3-26_audit.md`, F-045)
- [ ] S3 — Have an independent teammate review a disclosure for the November result and the monitor demonstration; preserve the registered verdict and distinguish it from causal validation.

## Success criteria
- [x] Exact opened sources and timestamps distinguish the incident, suspension and restoration.
- [x] The interpretation addresses the competing event without asserting that it caused the observed Binance dip.
- [ ] Any deck disclosure is reviewed independently, without changing the registered scoring rule.

## Outputs
- `scripts/p3_26_binance_incident_audit.py`
- `results/tables/P3-26_incident_timeline.csv`
- `results/tables/P3-26_window_sensitivity.csv`
- `results/P3-26_audit.md`
- `findings/F-045-november-binance-incident-audit.md`
- Source register M-11/M-12 and a reviewed interpretation for P3-20/P5-08.

## Handoff
- **State:** S1 and S2 completed (`scripts/p3_26_binance_incident_audit.py`, F-045). Audit confirms E1 S2 is mathematically insulated (pre-window ended 29 Oct 17:00 UTC, 3h before the 20:05 UTC attack; post-window 3–4 Nov after parity restored, gap −1.0 bps vs Foxbit). S1 (+47.9 bps) directly used the 30 Oct trough, confirming why it was disqualified at pre-registration. E2 pre-mean sensitivity is minor (~2.3 bps). P3-03 monitor silence is a mechanical 10-day quiet pause following the 30 Oct alarm.
- **Next step:** S3, an independent teammate (Nattan or Jonathan) reviews `results/P3-26_audit.md` and finding F-045, checks disclosure text for Slide 10 / Annex, and signs off.
- **Open questions:** none on computation; teammate verification of disclosure language before PDF export.
- **How to resume:** run `py scripts/p3_26_binance_incident_audit.py` to reproduce tables and markdown audit.

## Log
- 2026-11-07 — Felipe: executed S1 and S2 (`scripts/p3_26_binance_incident_audit.py`); generated `results/tables/P3-26_incident_timeline.csv`, `results/tables/P3-26_window_sensitivity.csv`, and audit report `results/P3-26_audit.md`; filed F-045 (exploratory); status -> review for S3 teammate sign-off.
- 2026-11-07 — Felipe: claimed task (owner: Economist, working: Felipe, status: doing) for incident timeline and confounder audit.
- 2026-11-05 — Codex for Renzo: filed follow-up under prompt.md §7 after opening Binance's own announcements. Research interpretation pending; June findings unchanged.

## Result
S1 and S2 complete. The Binance incident (29 Oct 20:05 UTC) coincided with a transient −30.3 bps dip in Binance USDT/BRL on 30 Oct (gap +49.0 bps vs Foxbit), but E1 primary statistic S2 is completely insulated from this anomaly by the pre-registered design (pre-window ended 29 Oct 17:00 UTC, post-window 3–4 Nov). E2 pre-mean shift is ~2.3 bps (small relative to ±75 bps band). CUSUM monitor silence is a mechanical 10-PTAX-day pause (`QUIET = 10`). Finding F-045 produced; awaiting S3 independent teammate review.
