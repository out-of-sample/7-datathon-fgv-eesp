# Independent frozen-bundle review — 9ab1ad8

Reviewed 7 Nov 2026 by Codex subagent for Felipe. Requested commit: `9ab1ad8dd99af7e8cac94c167a76b2b9e83f6645`; checkout after parent pull: `115bf9b89c2b0427365fedec7b0be92ec509f3fa`. Both commits change only `data/README.md`; the follow-up adds the GitHub release download location. This is agent verification, not the pending human teammate sign-off.

## Verdict

The frozen archive is available and sufficient for offline reproduction. All five analysis/document commands passed without fresh chain downloads. Computed accounting and operation classifications reproduce. Exact output identity has a Windows portability limitation: generated paths use backslashes and change the ledger's provenance hash. No economic-result discrepancy was found in this replay.

## Recovery and checks

Initially `data/raw/p3_29/`, the events CSV and archive were absent; `data/raw/p3_36/` was empty. No archive was found in the repository, Downloads or Desktop tree. The release asset was retrieved from the authenticated GitHub API for `out-of-sample/7-datathon-fgv-eesp`, tag `data-p3-29-p3-36-20261107`, asset ID `719861819`. The asset has exactly 10,157,721 bytes and SHA-256 `ba98b6105582fe2f7626e0c8f7c876cf0dc07352e33d0db70d879ac9ed54080f`, matching the requested commit. The download location is supplied by follow-up `115bf9b`, not by `9ab1ad8` itself.

The archive was restored with Python `tarfile`, checking each path stayed within the repository and checking any existing file before writing. The Flash bundle was restored from `git archive 79b71f1 results/flash-mentor-leads` without a PowerShell binary pipeline. All 3,158 manifest entries referencing p3_29, p3_36 or Flash passed SHA-256 verification; no failures. Existing raw data was not refreshed.

## Exact replay

Interpreter: `C:/Users/Felipe/AppData/Local/Programs/Python/Python314/python.exe` (3.14.8). The `python` Windows alias and `py` launcher did not locate a usable interpreter. README examples use Bash/Linux syntax, so equivalent PowerShell commands were used.

Scripts, relevant committed tables/processed files, and frozen inputs were copied to the ignored workspace `data/raw/review_9ab1ad8/replay/`. From that workspace, with `$env:P3_29_OFFLINE='1'` and `$env:PYTHONUTF8='1'`, each command below exited 0 (replace `python` with the interpreter above):

```text
python scripts/p3_29_reconcile.py ledger
python scripts/p3_29_reconcile.py cases
python scripts/p3_29_reconcile.py chains
python scripts/p3_36_brla_operations.py --offline
python scripts/p3_36_brla_operations.py --documents --offline
```

Local runner and evidence are retained, ignored, at `data/raw/review_9ab1ad8_runner.py`, `data/raw/review_9ab1ad8/verification.json` and `command_0.log` through `command_4.log` in that evidence directory. The downloaded archive is also there. Original tracked analysis outputs were not overwritten.

The ledger checks pass: 242 chunks with zero gaps, zero duplicate/removed logs, zero unknown topics, and 38/38 selected receipts. The twelve additional cases have zero stock residuals and consistent provider labels. Operation replay reports 32 transactions, 32 verified mechanisms and zero verified economic purposes. These are reproductions of exploratory findings, not evidence identifying fiat settlement or regulatory causation.

## Output comparison and actionable limitation

Every pre-existing P3-29/P3-36 table and processed output in the replay workspace was compared byte-for-byte with its source copy. Five files differed:

| File | Difference |
|---|---|
| `results/tables/P3-29_coverage.csv` | 242 path fields use backslashes |
| `results/tables/P3-36_documents.csv` | 5 path fields use backslashes |
| `results/tables/P3-36_sample.csv` | 32 raw-file paths use backslashes |
| `data/processed/P3-29_events.csv` | 20,455 raw-file paths use backslashes |
| `results/tables/P3-36_provenance.csv` | 285 paths use backslashes; rebuilt events-file hash changes |

CSV field comparisons of the first four files are identical after converting backslashes to slashes. The provenance difference consists of the same path normalization plus the hash of the rebuilt ledger (original `17ade99a340f7b26d9fa9bf99f5bdae8b433f941727a8e2aa59333e668abe6b5`, Windows replay `935e9cec2cf82573652c67e0c023b6017c9a4b983bbf1fd033f049e9939fd444`). All other compared files are byte-identical.

Recommendation: qualify README's `git status --short` expectation as applying to the tested Linux environment, or serialize repository-relative paths with `as_posix()` and deliberately update the affected provenance hash. Also compare ignored generated outputs explicitly: empty git status alone cannot establish their equality. No code/output fixes were made by this review.

Human P3-29 S7/P3-37 review, selected transaction inspection in a browser and economist approval remain pending. The figure command and full source/interpretation audit were outside this replay.
