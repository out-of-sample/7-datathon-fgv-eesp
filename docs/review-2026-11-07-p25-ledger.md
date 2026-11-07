# Independent review: P3-25, P3-29 and P3-37 — 7 November 2026

Reviewer: Codex for Felipe, separate review agent. Scope: specifications, producing code, findings, saved outputs and available frozen-input replay. No task or finding promotion: the named teammate and economist gates remain outstanding. No live collection or issuer contact was performed.

## Verdict

P3-29 and P3-37 reproduce their reported numerical results from the available frozen bundles. The accounting and technical-routing claims survive this review. They establish neither fiat settlement nor the economic purpose of a burn. P3-25's implementation and interpretation are consistent with its retrospective specification, but its complete raw-data rerun is blocked locally by the missing Mercado Bitcoin file. Its earlier independent reproduction is recorded, rather than claimed as a new reproduction here.

## Issues requiring attention

1. **P3-29, prediction P-0045: “flat window” is stronger than the implemented check.** `chains()` reads totalSupply at 00:44 and 00:48 and calls equality `flat_window`. Without intervening logs or state reads, equal endpoints do not establish unchanged supply throughout those four minutes: minting and burning could cancel. F-044 already discloses boundary-only evidence and only six informative matches. Describe the criterion as **equal endpoint supply at 00:44 and 00:48**, or add intervening supply-changing logs before claiming a verified flat interval. The 32 matches and zero misses reproduce; this is a limit on interpretation, not evidence that any observed match is wrong.
2. **P3-25, missing reproducibility input in this workspace.** `data/raw/mercadobitcoin/USDT-BRL-1h.csv` is absent. The script correctly fails rather than manufacturing the missing venue. Restore the frozen P1-03 input, then rerun before claiming a new local full reproduction or closing the named-human criterion. Binance and Foxbit inputs were available.
3. **Cross-platform reproduction produces metadata differences.** The Windows replay changes path separators in P3-29 coverage and P3-36 sample/provenance/document tables, and the default text encoding changes the Brasília heading in the generated audit. Numerical outputs agree. The five affected tracked outputs were restored after comparison; no scientific result was replaced. Use UTF-8 mode and normalize recorded paths if byte-identical replay across operating systems is required. These platform differences were already noted in the earlier P3-40 verification and are not newly discovered numerical defects.

## Reproduction evidence

Interpreter: `C:/Users/Felipe/AppData/Local/Programs/Python/Python314/python.exe`. The `python` Windows app alias cannot launch here, and `.venv/bin/python` does not exist locally. From the repository root in PowerShell:

```powershell
$env:P3_29_OFFLINE = '1'
& C:/Users/Felipe/AppData/Local/Programs/Python/Python314/python.exe scripts/p3_29_reconcile.py ledger
& C:/Users/Felipe/AppData/Local/Programs/Python/Python314/python.exe scripts/p3_29_reconcile.py cases
& C:/Users/Felipe/AppData/Local/Programs/Python/Python314/python.exe scripts/p3_29_reconcile.py chains
& C:/Users/Felipe/AppData/Local/Programs/Python/Python314/python.exe scripts/p3_36_brla_operations.py --offline
& C:/Users/Felipe/AppData/Local/Programs/Python/Python314/python.exe scripts/p3_36_brla_operations.py --documents --offline
```

All five commands completed successfully. Ledger residuals are zero on every reported interval. The twelve S5 cases close on both days and confirm 317/317 sampled receipts. Other-chain prediction outputs retain 32 matches, zero misses and six informative matches. The BRLA operation replay verifies 32/32 selected technical mechanisms and identifies zero economic purposes. The eight large burns total 335,396,065.575129 BRLA. A separate calculation from the exported transfer table confirms zero net intermediate-account BRLA balance change for each of those eight transactions.

The code was checked for integer-base-unit accounting, event order, interval coverage, missing-response behavior, historical implementation checks, ABI decoding, selected-receipt consistency, and separation of technical roles from legal ownership. No material error was found in the reproduced numerical claims. Frozen endpoint agreement is corroboration of those saved answers, not a fresh live-chain audit or independent source compilation.

For P3-25, `scripts/p3_25_composition.py` uses the specified ratio of period sums, converts UTC hours to Brasília dates, handles Binance millisecond/microsecond timestamps, rejects duplicate/negative volume, and applies the common-hour and MB-missing-as-zero rule. Its historical pairs overlap and are adjacent whereas the episode windows have a gap; F-036 states both limitations and avoids causal attribution. No new verification of the external exchange-exit webpages was performed in this pass; the earlier opened-source checks and the Bitnuvem failure remain the applicable evidence.

## Remaining gates

- P3-25: restore the frozen MB input; Nattan or Jonathan reruns and signs S5.
- P3-29: Jonathan or Nattan completes S7, including the explorer spot checks and interpretation review. This agent replay is supplemental evidence and does not impersonate that sign-off.
- P3-37: teammate presentation review and Felipe's economic interpretation review remain separate. The public record still does not identify settlement tickets, beneficiaries, legal operator identity or the June burns' off-chain purpose.
