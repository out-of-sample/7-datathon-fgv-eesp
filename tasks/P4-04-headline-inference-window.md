---
id: P4-04
title: Honest inference and window contents for the +94 bps headline (non-overlapping windows, first-day move, other measures inside the window)
phase: P4
status: review
owner: CS 2
working: -
due: 2026-11-04
depends: P2-03, P4-01
---

## Goal
Two weak points in how the headline is stated, found on 2 Nov while checking strategies for the deck
(`docs/deck-plan-10-slides.md`):

1. **Precision.** "p ≈ 0.001" (F-016) counts 1,073 ordinary dates whose 20-day windows overlap (neighbours share 38 of
   40 days), so they behave like ~30 independent comparisons. With non-overlapping windows the June change still beats
   every ordinary window, but the smallest possible p is about 0.03. The windows share no days but are not fully
   independent (the series is autocorrelated).
2. **Window contents.** The pre-committed window [+1, +20] after 23 Jun (24 Jun – 21 Jul) also contains the 26 Jun
   meeting (suspension kept, in-book arbitrage released, a 24-hour-hold draft presented, E-05.5, E-12) and Res. BCB 580
   (1 Jul, E-10), and a second peak on 3 Jul with no identified cause. +93.9 bps is the average over "the notice and
   what followed in the next weeks", not the notice alone. Only the first-day move (23 → 24 Jun) predates the meeting
   and Res. 580; it does not predate Res. 574 (register 18 Jun, DOU 22 Jun, E-11).

Core findings F-001..F-027 stay unchanged until the team re-decides the freeze; this task writes a new finding.

## Subtasks
- [x] S1 — done: Renzo, 2 Nov (`f4071ef`) — Spec, committed before the script: (a) the F-016 statistic on non-overlapping clean windows (same clean-date
  rule as `scripts/p2_03_events.py`; stride 41 PTAX days; all 41 offsets; p = (k+1)/(n+1), report the range);
  (b) the first-day change 23 → 24 Jun against every clean one-day change, all years and per year; (c) a dated list of
  regulatory communications inside [+1, +20] with the premium path. Decision rule for the deck wording, written in S1.
- [x] S2 — done: Renzo, 2 Nov (F-029) — `scripts/p4_04_inference.py` and finding F-0NN (next free number) with the commands.
- [x] S3 — done: Renzo, 2 Nov (in F-029; Felipe decides) — Wording for Felipe (slides 4, 5, 8): e.g. "maior que a variação em todas as 1.073 datas comuns; em 30 janelas
  que não se sobrepõem, p = 0,03"; "+94 bps no mês seguinte ao ofício, janela que inclui a reunião de 26/jun e a Res. 580".

## S1 spec (committed before `scripts/p4_04_inference.py` exists)

**Data and clean dates.** `data/processed/P1-02_premium_daily.csv` (`premium_bps`), events from
`data/processed/P1-04_events_brazil.csv`; clean-date rule identical to `scripts/p2_03_events.py` (blackout ±20 PTAX days
around every announced and effective date; positions 20 to N−21). t0 = 23 Jun 2026, excluded from both windows.

**Statistics**
- **A (headline, F-016):** mean[+1, +20] − mean[−20, −1]. Non-overlapping placebo sets: for each offset o = 0..40, walk
  the clean dates in order and keep one if its position is ≥ o and ≥ 41 positions after the last kept one (41-day
  windows share no day). Per offset: n, k (two-sided |s| ≥ |e|, as F-016; one-sided also reported), p = (k+1)/(n+1).
  Report min-max over offsets.
- **B (secondary, before the 26 Jun meeting):** mean[+1, +2] − mean[−20, −1]. The window ends at +2 because the meeting
  was at +3 (the event calendar, not the premium, sets it). Against all clean dates and against non-overlapping sets
  (stride 23, offsets 0..22). Disclosure: 24 and 25 Jun values (155.4, 184.3 bps) already seen.
- **C (description):** the one-day change 23 → 24 Jun against clean one-day changes, all years and per year, with
  `ptax_window_uncertain` flags. No p-value on slides.
- **D (description):** dated communications and market events within [−20, +20] PTAX days of t0, hand-listed from
  `docs/sources.md` with IDs (E-11, E-05, E-05.5/E-12, E-10, M-04, M-05), with the premium on each date.

**Decision rules for the deck (slides 4, 5, 8)**
1. A: if every offset gives p ≤ 0.05, the slide says "maior que a variação em todas as 1.073 datas comuns; em N janelas
   que não se sobrepõem, p = X" (N, X from the output). If any offset gives p > 0.05, report the range and remove the
   significance wording from the slides.
2. B: if every offset gives p ≤ 0.05, slide 4 or 8 may say "nos dois dias antes da reunião de 26/jun, +X bps"; otherwise
   annex only, as description.
3. C: annex only.
4. D: one line on slide 4 or 8: "janela que inclui a reunião de 26/jun (minuta da retenção de 24 h) e a Res. 580
   (1/jul)"; the full list in the annex.
5. The headline stays +93.9 bps (Renzo, 2 Nov).

## Success criteria
- [x] Spec committed before the script runs, with the disclosure below
- [x] A finding states the non-overlapping p range, the first-day rank, and the list of measures inside the window
- [x] The deck no longer shows "p ≈ 0.001" without the non-overlapping figure (10-slide deck, 2 Nov: slide 4 and the P3-12 figure label)

## Outputs
- `scripts/p4_04_inference.py`, `findings/F-029-headline-inference.md`, `results/tables/P4-04_nonoverlap.csv`,
  `results/tables/P4-04_window_events.csv`

## Exploratory checks already seen (2 Nov, agent for Renzo; disclose in the spec)
- Non-overlapping 20-day windows: n = 30 for every offset, k = 0 exceedances for every offset, p = 0.032.
- First-day change 23 → 24 Jun: +130.6 bps. Clean one-day changes (n = 1,092): 9 as large, all in 2021 (largest +210.0,
  23 Feb 2021). By year, days ≥ +130.6 (excluding 24 Jun): 2020 0, 2021 6, 2022 1, 2023 0, 2024 2 (max +300.2 on
  5 Aug 2024), 2025 1 (+132.2 on 5 Mar 2025), 2026 0 (max +86.7 on 3 Jul). Single days are noisy; uniqueness comes from
  persistence. 5 Mar 2025 spans Carnival (previous PTAX day 28 Feb) and is flagged `ptax_window_uncertain`.
- Re-validated 2 Nov (independent re-run): the reimplemented clean-date rule reproduces F-016 exactly (1,073 dates,
  +93.91, largest placebo +65.7, two-sided p = 0.0009); non-overlapping two-sided k = 0 for all offsets.
- Also seen: premium 155.4 (24 Jun) and 184.3 (25 Jun), the two PTAX days before the 26 Jun meeting.
- Premium path (bps): 23 Jun 24.8; 24 Jun 155.4; 25 Jun 184.3; 26 Jun 75.6 (meeting day); 29 Jun 139.8; 1 Jul 121.1
  (Res. 580 at 18:01); 2 Jul 99.2; 3 Jul 185.9; 6 Jul 177.0; 10 Jul 86.2.

Commands used (to become the script):
```bash
.venv/bin/python - <<'PY'
import pandas as pd, numpy as np
p = pd.read_csv('data/processed/P1-02_premium_daily.csv', parse_dates=['date_brt']).set_index('date_brt')['premium_bps']
ev = pd.read_csv('data/processed/P1-04_events_brazil.csv')
pos_ev = set()
for c in ['date_announced', 'date_effective']:
    for v in ev[c].dropna().astype(str):
        if v not in ('N/A', 'nan'):
            sub = np.where(p.index >= pd.Timestamp(v))[0]
            if len(sub): pos_ev.add(sub[0])
black = {q for e in pos_ev for q in range(max(0, e-20), min(len(p), e+21))}
t0 = p.index.get_loc(pd.Timestamp('2026-06-23'))
d1 = p.diff(); c1 = d1.iloc[[i for i in range(1, len(p)) if i not in black]]
print(d1.iloc[t0+1], (c1 >= d1.iloc[t0+1]).sum(), len(c1))
stat = lambda i: p.iloc[i+1:i+21].mean() - p.iloc[i-20:i].mean()
clean20 = [i for i in range(20, len(p)-20) if i not in black]
for off in range(41):
    ch, last = [], -10**9
    for i in clean20:
        if i >= off and i - last >= 41: ch.append(i); last = i
    s = np.array([stat(i) for i in ch]); print(off, len(s), (s >= stat(t0)).sum())
PY
```

## Handoff
- **State:** S1–S3 done; F-029 written; review. Criterion 3 (deck wording) is Felipe's: the text is in F-029.
- **Next step:** a teammate re-runs `python scripts/p4_04_inference.py` and checks F-029; Felipe applies the wording.
- **Open questions:** cause of the 3 Jul second peak (no dated source found on 2 Nov; one extended search for a
  resumption of the funds' operations in July also found nothing).
- **How to resume:** read F-016, F-022, E-05.5, E-10, E-12 in `docs/sources.md`.

## Log
- 2026-11-02, agent for Renzo: criterion 3 met in the 10-slide deck (P5-01 S5); F-029 slide-5 text date fixed
- 2026-11-02, agent for Renzo: script run, F-029; decision rules 1 and 2 both met (A p = 0.032; B p = 0.020–0.040); Res. 574 coincides with +37.7 bps on 18→19 Jun (one other 2026 day as large); status review
- 2026-11-02, agent for Renzo: Renzo takes the task; exploratory values re-validated (one misquote and two wordings corrected)
- 2026-11-02, agent for Renzo: created (todo) from the deck-plan strategy checks

## Result
Decision rules applied (F-029): rule 1 met (A: p = 0.032 for every offset), rule 2 met (B: p = 0.020–0.040 for every
offset). Res. 574 is not ruled out: +37.7 bps on 18 → 19 Jun, the PTAX day after its register date (only one other 2026
day before the notice rose as much); the event study cannot separate it from the notice.
