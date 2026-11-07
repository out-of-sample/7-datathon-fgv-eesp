# Independent review — P3-41 and P3-42

Reviewed 7 November 2026 by a separate Codex review agent for Felipe. Scope: both task specifications and Handoffs, scripts and shared frontier, P1-02 construction, F-050/F-051, explanatory notes, saved tables and all three figures. No model choice, production code, core finding or deck changed. Economist-owned task statuses remain `review` as requested; this agent review does not substitute for a named human teammate or Felipe's adoption decision.

## Verdict

**Pass within the stated exploratory, conditional scope.** No blocking numerical, chronology or claim mismatch found. The result is correctly limited: rolling ridge improves on frozen ridge, but the evidence does not establish an advantage over simple mean reversion or an implementable acquisition strategy. Actual access remains unknown.

## Reproduction

Commands from repository root, using the documented local interpreter:

```text
C:/Users/Felipe/AppData/Local/Programs/Python/Python314/python.exe scripts/p3_41_compression.py
C:/Users/Felipe/AppData/Local/Programs/Python/Python314/python.exe scripts/p3_42_compression_upgrade.py
```

Both complete runs exited successfully: nine P3-41 checks and fourteen combined P3-42 checks passed. SHA-256 comparisons before/after reproduced every one of the 24 existing outputs byte for byte (14 P3-41, 10 P3-42). The underlying input hashes match both audits. No downloads were needed.

## Independent checks beyond the supplied tests

- Reconstructed realized terminal BRL savings for every ridge validation/test row directly from initial and terminal 15h indicative prices, deposit accumulation, fixed USD hedge notional, forward price and K; did not call the shared budget function. Maximum absolute discrepancy was below 5e-12 bps. The observed signal/execution difference is retained rather than silently bought at the signal price.
- Verified every monthly fit's latest terminal timestamp is strictly before its month-start cutoff, and every adaptive band's latest calibration terminal timestamp is strictly before the current signal.
- Verified all six upgrade methods face the same dates within each split/horizon; nonoverlapping origins are strictly later than the prior terminal date; unknown access forces every actionable label to insufficient evidence.
- P1-02's daily feature averages hourly opens at 13–16 UTC, not its future 23 UTC close. The 16 UTC hourly close/24h volume is complete at 17 UTC. Publication eligibility excludes PTAX releases later than that signal.
- Validation-only model selection and chronological maturity purging match the recorded protocols. Upgrade models legitimately incorporate earlier matured 2026 labels for later 2026 predictions; there is no claim of a fresh untouched holdout. Historical forecast issuance is a retrospective reconstruction.
- CSV comparisons reproduce the F-050/F-051 primary metrics, policy counts, bootstrap summaries, June replay and stress extrema. The joint envelope has 216 funding/execution scenarios crossed with two compression endpoints; scenario extrema are not probabilities. Sparse policy gains remain explicitly qualified.
- All three figures were visually inspected: labels and legends are legible with no clipping.

## Non-blocking clarity recommendation

The P3-41 June figure plots **signal-to-terminal** observed compression and a break-even threshold based on the **signal-price** initial outlay. At five days its observed point is above that indicative threshold, while the actual 15h-entry scenario in F-050 loses after K because the premium already fell between 14h signal and 15h execution. The text and CSV correctly disclose this distinction. Before using that figure by itself in an annex, add an execution-gap annotation or a realized-saving row so a reader cannot interpret the diamond as evidence of a profitable five-day wait. This is a display clarification, not a discovered accounting error or a reason to refit.

## Remaining gates

Keep F-050/F-051 exploratory and Economist-owned tasks in review. A named teammate can reproduce the commands above and decide whether these conditional research exhibits merit annex use. Real executable access, hedge basis/margin, slippage, actual settlement calendars, guaranteed coverage and generalization beyond one known shock are not established. No additional model tuning is warranted by this review.
