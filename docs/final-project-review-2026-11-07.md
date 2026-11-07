# Project review and repairs — 7 November 2026

## Verdict

The buyer frontier and prior holder accounting pass the checked arithmetic and boundary tests. The reproducible errors found in this pass concern evidence identity, provenance and interpretation, rather than changed headline estimates. Corrections preserve the frozen core and keep exploratory extensions labelled as such.

This is a scoped repository review, not a certification of every external source or the final PDF. It combines three focused independent agent reviews with offline computational checks, code parsing, identifier checks, report inspection and independent reconciliation of exported buyer cash flows.

## Corrections

1. **Unique finding IDs.** Two independent streams published F-047. The access development pilot keeps F-047; BRLA operator routing is now F-049. Updated its task, protocol, data instructions and STATUS references. Original script/table prefixes remain unchanged for reproducibility.
2. **Treasury annex.** Removed the remaining claim that CIP makes waiting a pure bet on the premium. The annex now distinguishes ideal forward pricing from an actual WDO position and names deposit returns, USDT/USD and hedge residuals. No old numerical estimate was replaced by an unobserved executable quote.
3. **Duration provenance.** F-038's table incorrectly attributed MXN/COP data to Bitso, IDR to Tokocrypto, and several rates to domestic central banks. The producing P1-05 script uses Binance prices and ECB cross-rates for TRY/ZAR/MXN/PLN/IDR, plus TRM for COP. Corrected the labels.
4. **Duration inference.** Clarified that omitting episodes censored before the scoring horizon is a complete-case comparison, not IPCW adjustment. Informative censoring and shared global shocks limit inference. The four-sigma sensitivity fails the declared feasibility floor and is labelled accordingly. The small test advantage does not establish a general forecasting gain or impossibility theorem.
5. **Placebo bands.** Corrected presentation copies that treated historical reference bands as bounds excluding causal effects. They describe the reference distribution and cannot prove zero effect.
6. **Causal wording.** F-040's headline now names an observed premium jump rather than presenting a banking closure as uniquely identified. Fee-ratio denominators and retrospective status remain explicit.
7. **Agent-budget compliance.** P3-28 reports CLI turn counts above its configured limit. The mapping from the reported count to the enforced cap has not been verified. Removed the unsupported inference that tool-result counting explains it. Until verified, equal enforced turn-budget compliance must not be claimed. Frozen runs, scores and original limits are retained; no retrospective retuning is performed.
8. **Reproduction guidance.** F-048 explicitly explains why its task is P3-39 but its script and output prefixes remain P3-38. Added an offline integrity checker to prevent duplicate IDs and reconcile saved buyer results independently of the model function.

## Checks performed

Using `C:/Users/Felipe/AppData/Local/Programs/Python/Python314/python.exe` from the repository root:

```text
scripts/p3_30_duration.py --test          14 passed
scripts/p3_31_holder.py --test-only       13 passed
scripts/p3_38_buyer_frontier.py --test-only 10 passed
scripts/p3_28_access_map.py selftest      passed
scripts/p3_40_project_review.py           IDs, Python syntax, markers and buyer table identities
```

The integrity checker parses all top-level Python scripts without executing downloads, checks task/finding identifier uniqueness, checks active presentation/dashboard files for conflict markers, and independently reconciles the three exported June buyer rows: terminal buy-now minus waiting conversion plus hedge payoff, divided by initial outlay for bps. This is an arithmetic check, not execution evidence.

The P3-31/P3-39 reviewer independently ran the 23 holder/frontier tests and found no material accounting defect. The evidence reviewer checked the finding/deck trace, while the pipeline reviewer checked duration, ledger dependencies and access-study status. No new model family or outcome-selected parameter was introduced.

## Checks that remain unavailable or pending

- **Ledger/BRLA raw replay:** `scripts/p3_36_brla_operations.py --offline` cannot run here because `data/processed/P3-29_events.csv` and the corresponding raw bundles are absent. This is missing input, not proof of a failed reconciliation. Obtain the documented bundles and perform the independent S7/operations replay before claiming full reproduction.
- **Access benchmark:** human reference coding, semantic audit, full held-out coverage and verified turn-budget accounting remain pending. The access pilot is development-only.
- **Duration:** self-tests do not resolve the limited sample, censoring assumptions or cross-country dependence. No new forecast claim is made.
- **November E2:** its primary statistic needs 9 November. The first-day observation stays preliminary; no future result was invented.
- **Final PDF:** this pass rebuilds relevant HTML presentation copies but does not select a deck version or certify a final exported PDF.
- **Parallel ML audit:** `docs/audit-ml-duration-timeseries.md` contains model/theorem claims without registered reproducible support in the reviewed outputs. It must not supply deck claims until separately substantiated. It, `scratch/` and the band-TAR PNG modification were unrelated local work at review start; a concurrent process committed the whole checkout in `1766dfd` while this review prepared its targeted commit. They were not independently validated here. A verification-status notice now distinguishes the ML notes from findings; the combined commit is preserved.

## Handoff

Review the corrected wording and F-049 identity. Then prioritize missing raw-bundle reproduction, blind access coding, and a final ten-slide PDF read-through. These remaining checks need evidence or human review, not additional model fitting. Task P3-40 records the changes and the targeted commit.
