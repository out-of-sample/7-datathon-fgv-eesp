---
id: F-005
title: Our 2025 model lost to a naive "tomorrow = today" forecast
status: confirmed
task: P0-01
date: 2026-10-30
checked_by: Renzo
---

## Claim
On last year's own data and split, simply repeating yesterday's spread (R2 0.776, MAE 0.169) beat the
hybrid K-Means + SVM model presented in the 2025 deck (R2 0.622, MAE 0.248). This is the core of the
"Lições de 2025" slide.

## Evidence
`raw_data/Y.csv` of the 2025 repo (1,000 days, 12 Feb 2023 - 7 Nov 2025), first 80% train, last 20% test
(from 22 Apr 2025). Snippet in `docs/README.md` -> "Lessons from 2025". Model numbers are from the 2025 deck.

Reproduce (run in a clone of the 2025 repo):
```python
import pandas as pd
y = pd.read_csv("raw_data/Y.csv", index_col=0, parse_dates=True).iloc[:, 0].dropna()
s = int(len(y) * 0.8); t, p = y.iloc[s:], y.shift(1).iloc[s:]
print(1 - ((t - p) ** 2).sum() / ((t - t.mean()) ** 2).sum(), (t - p).abs().mean())
```

## Caveats
The 2025 TFT reported R2 0.912 but MAE 0.766 (4.5x worse than naive): metrics were not comparable across models.

## Used in deck
Planned: "Lições de 2025".

## History
- 2026-10-31, Renzo: re-run on 2025 repo data; persistence baseline reproduces R2 0.776 and MAE 0.169; confirmed.
- 2026-10-30 — agent for Renzo: created
