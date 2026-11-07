---
id: F-038
title: Pooling 10 currencies gives enough premium shocks to test duration forecasts, but a model using shock size does not beat the historical base rate; half of the 2020–2024 shocks were back in their band within 20 business days
status: exploratory
task: P3-30
date: 2026-11-06
checked_by: Renzo's agent (review with fixes, 6 Nov); Felipe (fixes accepted, 6 Nov); teammate re-run pending
---

## Claim
A **shock** is a day when the USDT premium over the official rate rises more than 3 robust standard deviations above
its 60-day median. It **recovers** when the premium spends 5 consecutive days back within one standard deviation of
that frozen median.

1. **Brazil alone is too small to test forecasts.** Under this rule Brazil has 11 shocks in 2020–2024, 3 in 2025 and
   1 in 2026, below the floor fixed before fitting (5 episodes in each test year).
2. **Pooling 10 currencies passes the floor** (k = 3: 43 training, 10 validation, 8 test episodes). In the
   2020–2024 training pool, 7% of shocks recover within 5 business days, 27% within 10 and 51% within 20
   (Kaplan-Meier, censoring handled). The median is 20 business days. This is a base rate for the training pool, not a
   forecast for any one country.
3. **Shock size does not reliably predict recovery.** The primary test was set before fitting: onset, 10-day
   horizon, penalty chosen on 2025. On it, the hazard model **loses to the base rate on 2025 validation** (Brier 0.346
   vs 0.330, 9 episodes). It wins narrowly on 2026 test (0.175 vs 0.188, 8 episodes). The paired bootstrap
   interval of the difference is −0.112 to +0.073, so the gap cannot be told apart from chance. With 2 or 4 standard
   deviations instead of 3, the model loses on test (k = 2: 0.239 vs 0.205; k = 4: 0.042 vs 0.037). Once a shock is
   under way, the base rate also beats the model (test, ages 0/5/10 pooled: 0.222 vs 0.255).
4. **The Brazilian 2026 shock does not fit a "20-day" story.** Under this rule it starts on 25 May 2026, a month
   before the 23 Jun notice, and is still open on 30 Oct after 111 PTAX days: the premium fell from its June peak
   but never returned to its pre-May band.

**What this teaches:** this model and small sample do not establish robust predictive improvement over the training-pool base rate. This is not proof that duration is inherently unpredictable; the interval includes both improvement and deterioration.

## Evidence

### 1. Dual-Scope Feasibility Gate Audit (`P3-30_feasibility.csv`)
Strict chronological cutoff re-extraction prevents post-cutoff recoveries from leaking into training or validation labels. The operational feasibility floor requires $\ge 10$ episodes / 5 recoveries in train, and $\ge 5$ episodes / 2 recoveries in validation and test.

| Scope | Threshold ($k$) | Train (Episodes / Rec.) | Val 2025 (Episodes / Rec.) | Test 2026 (Episodes / Rec.) | Feasibility Verdict |
|---|:---:|:---:|:---:|:---:|:---:|
| **BRL_only** | 3 $\sigma$ (primary) | 11 / 10 (Pass) | 3 / 3 (Fail: $3 < 5$) | 1 / 0 (Fail: $1 < 5$) | **Failed (Single-Country)** |
| **BRL_only** | 2 $\sigma$ (sensitivity) | 13 / 12 (Pass) | 2 / 1 (Fail: $2 < 5$) | 1 / 1 (Fail: $1 < 5$) | Failed (Single-Country) |
| **BRL_only** | 4 $\sigma$ (sensitivity) | 6 / 5 (Fail: $6 < 10$) | 2 / 2 (Fail: $2 < 5$) | 1 / 0 (Fail: $1 < 5$) | Failed (Single-Country) |
| **Global 10 Currencies** | 3 $\sigma$ (primary) | **43 / 38** (Pass) | **10 / 8** (Pass) | **8 / 6** (Pass) | **PASSED (Global Pool)** |
| **Global 10 Currencies** | 2 $\sigma$ (sensitivity) | **62 / 55** (Pass) | **17 / 13** (Pass) | **14 / 11** (Pass) | **PASSED (Global Pool)** |
| **Global 10 Currencies** | 4 $\sigma$ (sensitivity) | 33 / 28 (Pass) | 5 / 5 (Pass) | 4 / 3 (Fail: $4 < 5$) | Fails declared floor ($4 < 5$ test); descriptive only |

*Full sample counts without administrative cutoff censoring at $k=2$ are 62/59 train, 17/17 val, 14/11 test.*

### 2. 10-Currency Episode Census (`P3-30_census.csv`)
Total extracted episodes and confirmed recoveries across native trading calendars:

| Currency | Trading Days | $k=2$ (Ep. / Rec.) | $k=3$ (Ep. / Rec.) | $k=4$ (Ep. / Rec.) | Calendar Source / Notes |
|---|:---:|:---:|:---:|:---:|---|
| **BRL** | 1,520 | 16 / 16 | 15 / 14 | 9 / 8 | P1-02 USDT/BRL adjusted premium (PTAX) |
| **EUR** | 1,748 | 21 / 20 | 11 / 10 | 8 / 8 | P1-05 Binance USDT/EUR vs ECB |
| **TRY** | 1,749 | 16 / 15 | 11 / 10 | 12 / 12 | P1-05 Binance USDT/TRY vs ECB cross-rate |
| **ZAR** | 1,115 | 8 / 8 | 2 / 2 | 0 / 0 | P1-05 Binance USDT/ZAR vs ECB cross-rate |
| **MXN** | 655 | 4 / 4 | 3 / 3 | 2 / 2 | P1-05 Binance USDT/MXN vs ECB cross-rate |
| **PLN** | 819 | 14 / 13 | 8 / 8 | 4 / 4 | P1-05 Binance USDT/PLN vs ECB cross-rate |
| **IDR** | 234 | 4 / 4 | 3 / 3 | 1 / 1 | P1-05 Binance USDT/IDR vs ECB cross-rate |
| **COP** | 569 | 1 / 0 | 2 / 2 | 1 / 1 | P1-05 Binance USDT/COP vs TRM |
| **UAH** | 1,615 | 8 / 7 | 5 / 4 | 4 / 3 | P1-05 Binance USDT/UAH vs NBU |
| **ARS** | 851 | 1 / 0 | 1 / 0 | 1 / 0 | P1-05 Binance USDT/ARS vs BCRA |
| **Total Pool** | **10,875** | **93 / 87** | **61 / 56** | **42 / 39** | **Native calendars (zero holiday censoring)** |


Scoring note (P3-40): episodes censored before the horizon are omitted. This is complete-case scoring, not an IPCW censoring-adjusted Brier score; informative censoring can bias it. Bootstrap resampling does not cluster shared global shocks.

### 3. Primary comparison and robustness (`P3-30_model_eval.csv`, `P3-30_brier_bootstrap.csv`)
Brier score = mean squared error of the predicted recovery probability (lower is better). KM = Kaplan-Meier
recovery rate of the 2020–2024 training pool (the naive base rate). Model = penalised discrete-time logistic hazard
with λ = 10, selected on 2025 validation at the 10-day horizon. Episodes censored before the horizon are left out
(their outcome is unknown). The column "Model − KM" gives the mean and 95% paired bootstrap interval over episodes
(10,000 draws, seed 0). A negative value means the model did better.

| k | Split | Horizon | n | KM | Model | Model − KM [95% CI] |
|---|---|---|---|---|---|---|
| 3 | validation 2025 | 10 d (primary) | 9 | 0.330 | 0.346 | +0.016 [−0.048, +0.080] |
| 3 | **test 2026** | **10 d (primary)** | 8 | 0.188 | 0.175 | −0.013 [−0.112, +0.073] |
| 3 | test 2026 | 5 d | 8 | 0.112 | 0.087 | −0.025 [−0.146, +0.051] |
| 3 | test 2026 | 20 d | 7 | 0.249 | 0.254 | +0.005 [−0.100, +0.106] |
| 2 | test 2026 | 10 d | 14 | 0.205 | 0.239 | +0.034 [−0.003, +0.072] |
| 4 | test 2026 | 10 d | 4 | 0.037 | 0.042 | +0.005 [−0.013, +0.016] |
| 3 | test 2026, ages 0/5/10 pooled | 10 d | 20 | 0.222 | 0.255 | — |

The 8 test episodes are BRL (25 May, open), EUR (17 Sep; 8 Oct, open), ZAR (7 May), MXN (20 Feb) and IDR (23 Mar,
9 Jun, 26 Jun). Three are Indonesian, so the independent information is smaller than 8.

### 4. Fitted coefficients
The standardised initial-excess coefficient is negative at every penalty (−0.43 at λ = 10, −0.52 at λ = 1): in the
training data larger shocks recover more slowly. The sign is stable, but it does not translate into better
out-of-sample forecasts (table above).

### 5. Figure (`results/figures/P3-30_global_survival.png`)
Panel A: training-pool Kaplan-Meier curve with the 20-day median. Panel B: the selected model's predicted 10- and
20-day recovery by initial shock size, with the 2026 test outcomes.

## Method and limitations
- The census and feasibility gate were run on BRL first. The 10-currency pool was added after BRL failed the floor
  (a design change after seeing counts, not outcomes, disclosed here).
- The pool mixes open markets (EUR, MXN, PLN) with capital-control regimes (ARS, UAH, TRY), and each uses its own
  official rate and calendar. Pooling assumes the same recovery process.
- "Recovery" means back to the pre-shock band, not "the premium fell". A buyer cares about any fall (see F-039).
- Shocks in different currencies on the same days (global USDT events) are not independent. Of the 8 test episodes,
  3 are Indonesian.
- Nothing here identifies *why* shocks end. The first draft's sentence that recovery is "driven by institutional
  liquidity" had no test behind it and was removed.

## Verification
```bash
.venv/bin/python scripts/p3_30_duration.py --test   # 14 checks
.venv/bin/python scripts/p3_30_duration.py          # tables, bootstrap, figure, run summary
```
(Windows: `py scripts/p3_30_duration.py`.) Input hashes in `P3-30_run_summary.json` are computed on the files as
stored. A Windows checkout with CRLF line endings gives different hashes for byte-identical numbers.

## Used in deck
Not on a slide. If used, one Annex line in pt-BR: "Com 10 moedas, metade dos choques de prêmio de 2020–2024 voltou à
faixa anterior em até 20 dias úteis; o tamanho do choque não previu a duração melhor que essa taxa histórica."

## History
- 2026-11-07 — Codex for Felipe (P3-40): corrected venue/reference-rate provenance labels to match P1-05; clarified complete-case scoring and k=4 feasibility-floor failure. Estimates unchanged.
- 2026-11-06: Initial single-country BRL feasibility audit; 8 tests pass; feasibility gate failed for BRL alone.
- 2026-11-06: Upgraded to Global 10-Currency Pool on native trading calendars; 10 tests pass; feasibility gate passes at $k=3$ (43/38 train, 10/8 val, 8/6 test); penalized discrete-time logistic hazard model fitted and evaluated against KM baseline; generated `P3-30_model_eval.csv`, `P3-30_global_survival.png`, and updated F-038.
- 2026-11-06 — Felipe: fixes accepted; assessment rewritten to match; status stays exploratory pending teammate re-run.
- 2026-11-06 — Renzo's agent (review, with fixes; Felipe to accept): (1) status `confirmed` → `exploratory` (no
  checker had signed); (2) scoring bug fixed: episodes censored before the horizon were counted as "not recovered"
  (1 validation episode at 10 d, 1 test at 20 d); (3) only the validation-selected penalty is reported (λ = 1 and 0.5
  are test-set picks); (4) paired bootstrap added; the model loses on validation and at k = 2 and 4, so "onset
  predictability" and "7.0–12.5% / 25.5% Brier reduction" are withdrawn; (5) "aligns with Brazil's 20-day spike"
  withdrawn: Brazil's 2026 episode starts 25 May and is open after 111 days; (6) the causal sentence about
  institutional liquidity removed; (7) run-summary numbers are computed (the first version typed in 0.2223/0.2575,
  which did not match the table it described).

- 2026-11-07 — Codex for Felipe (P3-36): audit corrections applied; claim limits clarified; original estimates retained. Independent reproduction status is unchanged.
