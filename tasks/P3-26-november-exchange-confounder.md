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
- [x] S1 — Confirm the withdrawal suspension and asset-specific restoration timeline from Binance primary announcements, including USDT and the networks relevant to Brazilian arbitrage. — done: Felipe, 7 Nov (M-11, M-12, FBI/TRM Labs attribution; attack onset 29 Oct 20:05 UTC, withdrawals suspended, reported 98% replenishment by 31 Oct does not verify USDT/network withdrawal restoration)
- [x] S2 — Map the verified timeline to P3-20's existing pre/post windows and venue comparisons; state what can and cannot be separated. Any additional numerical analysis needs a retrospective specification and isolated outputs. — done: Felipe, 7 Nov (`scripts/p3_26_binance_incident_audit.py`, `results/tables/P3-26_incident_timeline.csv`, `results/tables/P3-26_window_sensitivity.csv`, `results/P3-26_audit.md`, F-045)
- [x] S3 — Independent AI review of the November disclosure and monitor demonstration — done: separate Codex reviewer, 7 Nov; named-human requirement replaced by Felipe's explicit AI-review authorization. Registered verdict preserved; no causal validation claimed.

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
- **State:** Independent AI technical review and available frozen-output reproduction are recorded. Felipe authorized AI technical review in place of the pending named-human reruns; no human validation is claimed. Economist ownership keeps status review by his earlier instruction.
- **Next step:** Felipe reviews economic interpretation and deck/annex adoption. Use the current findings and review evidence; further agent checks may inspect the amendments without refitting or changing frozen results.
- **Open questions:** Residual/shared incident effects and exact USDT/network restoration remain unidentified; E2 primary verdict needs 9 Nov.
- **How to resume:** read the applicable 7 Nov independent review and exact commands linked below; preserve historical findings and audit-time logs.

## Log
- 2026-11-07 — Felipe: executed S1 and S2 (`scripts/p3_26_binance_incident_audit.py`); generated `results/tables/P3-26_incident_timeline.csv`, `results/tables/P3-26_window_sensitivity.csv`, and audit report `results/P3-26_audit.md`; filed F-045 (exploratory); status -> review for S3 teammate sign-off.
- 2026-11-07 — Felipe: claimed task (owner: Economist, working: Felipe, status: doing) for incident timeline and confounder audit.
- 2026-11-05 — Codex for Renzo: filed follow-up under prompt.md §7 after opening Binance's own announcements. Research interpretation pending; June findings unchanged.

## Result
S1 and S2 complete. The Binance incident (29 Oct 20:05 UTC) coincided with a transient −30.3 bps dip in Binance USDT/BRL on 30 Oct (gap +49.0 bps vs Foxbit), but E1 primary statistic S2 directly excludes the 30 Oct observation under the pre-registered design (pre-window ended 29 Oct 17:00 UTC, post-window 3–4 Nov). E2 pre-mean shift is ~2.3 bps (small relative to ±75 bps band). CUSUM monitor silence is a mechanical 10-PTAX-day pause (`QUIET = 10`). Finding F-045 produced; independent AI disclosure review is recorded below. Residual/shared incident effects remain possible; exact USDT/network withdrawal restoration is unverified.

## Independent review — 7 Nov 2026 (Codex for Felipe)

Reviewed in `docs/review-2026-11-07-duration-treasury.md`. Full offline duration/holder/frontier/incident replay passes; all 20 regenerated CSVs match numerically and 37 checks pass. Remaining interpretation/handoff corrections and verification limits are listed in that report. This is agent evidence only: required named human sign-offs remain pending. Economist-owned `status: review` is preserved as Felipe requested.

## Review amendment — 7 Nov 2026
Felipe explicitly authorized separate AI agents to replace pending human technical coding/audit/reproduction steps. Existing independent review evidence is accepted within its stated scope; no human sign-off is implied. Historical pending-human statements above describe the earlier protocol. Economist-owned statuses remain review; deck adoption and unsupported economic claims are not approved by this amendment.
