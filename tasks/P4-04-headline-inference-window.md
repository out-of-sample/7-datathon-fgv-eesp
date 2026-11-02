---
id: P4-04
title: Honest inference and window contents for the +94 bps headline (non-overlapping windows, first-day move, other measures inside the window)
phase: P4
status: todo
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
   every ordinary window, but the smallest possible p is about 0.03.
2. **Window contents.** The pre-committed window [+1, +20] after 23 Jun (24 Jun – 21 Jul) also contains the 26 Jun
   meeting (suspension kept, in-book arbitrage released, a 24-hour-hold draft presented, E-05.5, E-12) and Res. BCB 580
   (1 Jul, E-10), and a second peak on 3 Jul with no identified cause. +93.9 bps is the average over "the notice and
   what followed in the next weeks", not the notice alone. Only the first-day move (23 → 24 Jun) predates the meeting.

Core findings F-001..F-027 stay unchanged until the team re-decides the freeze; this task writes a new finding.

## Subtasks
- [ ] S1 — Spec, committed before the script: (a) the F-016 statistic on non-overlapping clean windows (same clean-date
  rule as `scripts/p2_03_events.py`; stride 41 PTAX days; all 41 offsets; p = (k+1)/(n+1), report the range);
  (b) the first-day change 23 → 24 Jun against every clean one-day change, all years and per year; (c) a dated list of
  regulatory communications inside [+1, +20] with the premium path. Decision rule for the deck wording, written in S1.
- [ ] S2 — `scripts/p4_04_inference.py` and finding F-0NN (next free number) with the commands.
- [ ] S3 — Wording for Felipe (slides 4, 5, 8): e.g. "maior que a variação em todas as 1.073 datas comuns; em 30 janelas
  que não se sobrepõem, p = 0,03"; "+94 bps no mês seguinte ao ofício, janela que inclui a reunião de 26/jun e a Res. 580".

## Success criteria
- [ ] Spec committed before the script runs, with the disclosure below
- [ ] A finding states the non-overlapping p range, the first-day rank, and the list of measures inside the window
- [ ] The deck no longer shows "p ≈ 0.001" without the non-overlapping figure

## Outputs
- `scripts/p4_04_inference.py`, `findings/F-0NN-headline-inference.md`

## Exploratory checks already seen (2 Nov, agent for Renzo; disclose in the spec)
- Non-overlapping 20-day windows: n = 30 for every offset, k = 0 exceedances for every offset, p = 0.032.
- First-day change 23 → 24 Jun: +130.6 bps. Clean one-day changes (n = 1,092): 9 as large, all in 2021 (largest +210.0,
  23 Feb 2021). By year, days ≥ +130.6 (excluding 24 Jun): 2020 0, 2021 6, 2022 1, 2023 0, 2024 2 (max +300.2 on
  5 Aug 2024), 2025 1 (+132.2 on 5 Mar 2025), 2026 0 (max +86.7 on 3 Jul). Single days are noisy; uniqueness comes from
  persistence.
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
- **State:** not started; exploratory values above.
- **Next step:** S1 (spec), then S2.
- **Open questions:** cause of the 3 Jul second peak (no dated source found on 2 Nov; one extended search for a
  resumption of the funds' operations in July also found nothing).
- **How to resume:** read F-016, F-022, E-05.5, E-10, E-12 in `docs/sources.md`.

## Log
- 2026-11-02, agent for Renzo: created (todo) from the deck-plan strategy checks

## Result
