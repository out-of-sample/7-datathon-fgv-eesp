# Independent duration and treasury review — 7 November 2026

## Scope and verdict

Reviewed P3-26, P3-30, P3-31, P3-32, P3-33, P3-36, P3-39 and P3-40 at checkout `3c5e568`, for Felipe's review request. All eight remain `review`: Economist ownership must not be promoted by this pass. Named human sign-offs remain outstanding. Computational results can be shared with the existing caveats; several remaining interpretation and handoff sentences need revision before reuse in the PDF.

This pass read current scripts, findings, task handoffs, the assessment, and prior review reports. It did not reopen external incident/regulatory sources or certify the final PDF. Source statements below are comparisons against the existing opened-source register, not new external verification.

## Material findings

1. **P2 — universal forecasting claim remains in P3-33.** `docs/shock-duration-and-holder-decisions-assessment.md`, section 1.3 conclusion, says duration “cannot be forecast better than the historical base rate.” F-038 establishes only an inconclusive comparison for the tested model and small sample. Replace with: “This model and evaluation sample do not establish reliable improvement over the historical base rate; the interval permits both improvement and deterioration.” The reported base-rate median and model scores reproduce. The matching caution already appears in F-038, so this is a stale downstream interpretation.
2. **P2 — pure-premium/complete-hedge claims remain in the treasury handoff and conclusion options.** P3-31's specification still says waiting “is a bet on the USDT premium alone.” Assessment Option B says waiting isolates currency risk and focuses on the premium; Option C says “aposta exclusiva sobre o prêmio local.” Its direction-assessment table also describes Binance execution prices and B3 forward rates as fully verifiable, while the implementation uses indicative PTAX-window prices and a hypothetical ideal forward. The generated `P3-31_historical.png` legend says “só prêmio + juro em USD.” These omit USDT/USD, fixed-notional residual FX exposure and achievable funding/forward differences. Replace with: “O termo ideal reduz a exposição ao USD/BRL; o resultado também depende de USDT/USD, juros, custos, residual do hedge e entrega.” Label prices indicative and forward rates hypothetical. P3-39/F-048 already preserve these qualifications.
3. **P2 — incident task still contradicts the corrected finding.** P3-26's Handoff says S2 is “mathematically insulated,” and its Result says “completely insulated”; Handoff also says post-window parity was restored. Its S1 completion text implies restoration evidence (“98% replenished by 31 Oct”) without the source register verifying USDT/network restoration. Current F-045 and the byte-reproduced generated audit correctly say only that the 30 Oct observation is excluded directly, residual/shared incident effects remain possible, and exact USDT withdrawal restoration is unverified. Replace task summaries with that narrower statement; keep S3 human disclosure review unchecked. Small observed gaps establish price convergence, not operational restoration.
4. **P3 — audit handoffs contain superseded state.** P3-36's Handoff says P3-35 belongs to Renzo, and its report's source list links a now-absent `tasks/P3-35-brla-economic-function.md`; the current task is P3-37. P3-40's main report still lists raw replay as unavailable, while its Handoff and linked supplemental review correctly record successful restoration/replay. Label those main-report paragraphs as audit-time limitations, then point to the supplemental result. P3-32 Result still says “until Felipe accepts” although acceptance is recorded; only the independent human rerun is outstanding. Preserve historical log entries rather than rewriting them.

No new material numerical-accounting defect was found. Existing qualifications remain necessary: complete-case duration scoring, cross-country dependence, non-executable prices, ideal rather than replicated WDO hedge, hypothetical rates and fees, unresolved access/delivery, one retrospective June origin, and E2's primary result not available until 9 November.

## Reproduction evidence

Interpreter: `C:/Users/Felipe/AppData/Local/Programs/Python/Python314/python.exe`. All commands ran offline against existing processed inputs. Full replay used imported modules with output-directory constants redirected to `scratch/review-duration-treasury/`; P3-26's fixed P3-20 reference CSV was copied into its isolated table directory because TAB is used for both input and output. No tracked analysis outputs were overwritten.

Equivalent standard commands from repository root:

```text
python scripts/p3_30_duration.py --test
python scripts/p3_30_duration.py
python scripts/p3_31_holder.py --test-only
python scripts/p3_31_holder.py
python scripts/p3_38_buyer_frontier.py --test-only
python scripts/p3_38_buyer_frontier.py
python scripts/p3_26_binance_incident_audit.py
```

Duration selftests report 14 checks, holder 13 and frontier 10. All full runs complete. All 20 regenerated CSV tables agree with the checked-in tables (numerical tolerance 1e-10 relative / 1e-8 absolute). The generated incident Markdown is byte-identical. P3-30 and P3-31 JSON differ only in stored input byte hashes and the Windows path separator; computed fields match. P3-38 JSON is byte-identical. PNG dimensions match, but pixels differ in this rendering environment; no pixel-identity claim is made. The regenerated holder history figure was visually inspected: numbers are readable and consistent with the tables, but its legend needs the qualification above. Full visual inspection of every chart/PDF was outside this scoped pass.

Local evidence: `scratch/review-duration-treasury/reproduction.json`, module logs and isolated tables/figures. Scratch evidence is not a submission artifact.

## Independent arithmetic

Separately reconstructed the June comparison directly from P1-02, without invoking either model helper: initial cost = Q × initial price × 1.001; terminal buy-now cost = initial cost × 1.1^(h/252); forward = initial PTAX × 1.1^(h/252) / 1.05^(h/252); fixed USD notional = initial cost / initial PTAX; waiting cost = Q × terminal price × 1.001 − notional × (terminal PTAX − forward). The 0.22-bp hedge fee is deducted once for F-039; F-048 retains it as part of the available additional-cost budget. These formulae are implemented in the scripts above and reproduce the saved findings.

| PTAX horizon | Hedged saving (BRL) | Hedged saving (bps, terminal base) | Cost ceiling (BRL) | Cost ceiling (bps, initial base) | Seller wait minus sell now (BRL) |
|---|---:|---:|---:|---:|---:|
| 5 | 4,746.45 | 89.6614 | 4,758.08 | 90.0511 | −4,696.94 |
| 10 | 4,896.28 | 92.3168 | 4,907.90 | 92.8866 | −11,593.57 |
| 20 | 8,733.44 | 164.0429 | 8,745.06 | 165.5085 | −21,703.71 |

Independent slicing of P3-20 daily data gives E1 pre-mean 19.23185 bps, post-mean 21.324 bps and S2 +2.09215 bps. Direct exclusion of the 30 Oct observation is confirmed; this is not proof that all incident effects were excluded.

## Remaining approvals and review limits

Nattan or Jonathan must still sign the specified human reruns for P3-26/P3-30/P3-31/P3-32. Agent reproduction is recorded as evidence, not a substitute for named human gates. P3-33 conclusion choice and P3-39 exhibit adoption remain Felipe's decisions. P3-36/P3-40 are completed scoped audits, not final external-source/PDF certification. Their Economist review status is unchanged by request.
