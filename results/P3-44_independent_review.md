# Independent P3-43/P3-44 verification — 7 November 2026

Reviewer: separate Codex agent for Felipe, not the scorer or runner implementer. This review inspected code, synthetic fixtures and frozen input/configuration metadata only. It did not inspect reference-coder files or model-answer bodies and does not establish model performance or human validation.

**Verified:** all 32 checks pass: 15 in `scripts/test_p3_43_audit.py`, 11 in `scripts/test_p3_44_pipeline.py`, and 6 in `scripts/p3_44_access_pilot.py --test-only`. Executed with `C:/Users/Felipe/AppData/Local/Programs/Python/Python314/python.exe` from the repository root.

The scorer now requires a complete, uniquely keyed audit with explicit yes/no decisions and auditor identity/type. Full answer payloads, notes, units, duplicates, drafts and every retained raw call remain auditable. Missing runs score zero; stale corpus hashes stop scoring. Final AI-audited output is explicitly labelled exploratory and not human validated. Guardrail counts concern retained claim representations, not independent mistakes.

The runner resolves the installed default once and pins `gpt-6.1-sol` for every model method. Frozen configuration matches the current implementation. Its 140 scheduled jobs comprise 20 development and 120 held-out jobs (B0: 17; B1/B2/A: 41 each). All copied case-source files, prompt hashes and per-case corpus hashes match the frozen job records. Frozen configuration SHA-256: `49077aa408743fca3904968b64993c24bddcd9c8cfbc5305c162a55423cbfcd9`. Configuration verifies raw/text hashes, reads the frozen timestamped source paths, rejects stale aliases/tampering and does not choose evidence from a later mutable manifest.

**Remaining limit requiring trace review:** read restrictions are prompt restrictions plus a conservative screen, not OS confidentiality. Although the regression checks catch network commands, writes, started-only tools and ordinary parent paths, synthetic `Get-Content $HOME/.codex/config.toml` and `Get-Content ..` still pass the current screen. No such real access is asserted here. Before claiming equal information access, inspect actual retained commands for variable-expanded, bare-parent or other out-of-corpus reads and count affected runs as restriction failures. Do not silently change the already frozen method configuration; any strengthened screening must be documented and applied consistently.

No blocking numerical/scoring defect was found within the tested scope. Completion of scheduled runs, independent AI reference adjudication, full semantic auditing and trace review remain separate acceptance steps. Output-token limits are prompt/post-run limits, resource equivalence is not proved, and common-model AI judgments can share errors. Preserve the exploratory label and report failures and unavailable evidence.

## Infrastructure amendment — corpus-reader v3

The preceding 32-test result and 140-job hash verification concern **v2**, not the replacement runtime. A later infrastructure-only check found nine of 39 v2 stderr files contain `blocked by policy`; adaptive shell reads could therefore fail while the former runner did not record that infrastructure error. No reference or comparative score was read in this review. Preserve v2 attempts as stopped infrastructure evidence and do not pool them with v3 results.

Independently reviewed the new `scripts/p3_44_corpus_reader.py` and added `scripts/test_p3_44_reader.py`. Its 14 tests finish with **13 passes and one skip**: real Windows symlink creation requires an unavailable privilege. A mocked source becoming a symlink after enumeration is checked and rejected. Passing checks cover list/read/literal search, offsets and result/read caps, exact argument types, missing/extra fields, path escapes, unknown/write tools, unchanged fixture files and stdio JSON-RPC success/error responses. The reader has only three tools and serves only enumerated `.txt` files under its resolved case directory, with repeated path/symlink checks. No blocking reader defect was found within this scope.

The v3 runner uses separate `runs_v3`/`experiment_v3` locations, reuses the pinned model, hashes the reader source, requires an actual sentinel corpus-read preflight, rejects non-corpus tools from retained started/completed traces, and now records blocked-policy stderr as an infrastructure error. Its eight built-in checks pass. The earlier shell-pattern pipeline test is obsolete under MCP-only v3: shell search should now be rejected; replace it with a corpus-search literal-pattern trace check rather than relaxing the new restriction.

At this verification point, v3 model preflight existed but its successful tool probe, frozen configuration and job manifest had not yet been created. The original v2 140-job verification does **not** certify v3 preparation or completed comparisons. Verify the actual tool probe and new frozen hashes before running/scoring. The scoped reader removes the prior shell-path interface from permitted evidence retrieval, but the CLI's prohibition on other tools still relies on instructions and post-run trace checks; do not claim OS-wide confidentiality or human validation.


## Final execution & scoring independent verification (v4 experiment) — 8 November 2026

Reviewer: independent verification subagent. Performed full regression suite verification, artifact hash audits, scoring validation, guardrail confirmation, and trace compliance verification.

### 1. Regression test suites
Executed all 4 test suites under Windows Python 3.14:
- `py scripts/test_p3_43_audit.py`: 15 passed (OK)
- `py scripts/test_p3_44_pipeline.py`: 12 passed (OK)
- `py scripts/test_p3_44_reader.py`: 14 tests — 13 passed, 1 skipped (Windows unprivileged symlink test skipped as designed; symlink mock check passed)
- `py scripts/p3_44_access_pilot.py --test-only`: 8 passed (OK)
Total: 49 unit and pipeline regression checks executed, all passing with zero regressions.

### 2. File SHA-256 integrity verification
- `data/raw/p3_28_v2/reference/reference.csv`: `efd4f7f8ffbfe3b2ab69b3977722ee2cf00182bc32856839d167d84d75379532` (verified matching `reference.sha256`)
- `data/raw/p3_28_v2/reference/coder_one.csv`: `e9157e4c25351d719f558abfd358708c37b6bda4a169dc60686e4f93964f3f2b`
- `data/raw/p3_28_v2/reference/coder_two.csv`: `bb781dceeb2b3aacb1fc8090b393a513d69940cfa1017a256edc5b9fe17e7f27`
- `data/raw/p3_28_v2/reference/adjudication_log.csv`: `e8e66e656b8a49faa309eb31695f607ed249de180462e45da5c186be072a6e92`
- `data/raw/p3_28_v2/reference/audit_dev.csv`: `37b179d3bd4f7d2b39712f75f4339b114d9ba40b7734f4e16b3224be117d7f8d`
- `data/raw/p3_28_v2/reference/audit_heldout.csv`: `a2d7ba07a1422efddcb2212a026649e544c93e82ce93d4e9a8110a46657451ce`
- `data/raw/p3_28_v2/experiment_v4/config.json`: `a82ec5f9c1e3778ab44a4545d77fb1f1d0bdc63f92a3b090917aa88e891172b5`
- `score_receipt_dev.json` and `score_receipt_heldout.json`: matched the above hashes exactly; zero audit failures recorded (`audit_failures_dev.json` = `[]`, `audit_failures_heldout.json` = `[]`).

### 3. Final scoring output & guardrail inspection
- `results/tables/P3-44_summary.csv`:
  - Dev split: B0 SAC = 0.147 (0 failed), B1 SAC = 0.890 (0 failed), B2 SAC = 0.890 (0 failed), A SAC = 0.569 (2 failed runs).
  - Held-out split: B0 SAC = 0.000 (0 failed, 3 unsupported claims), B1 SAC = 0.737 (0 failed, 44 unsupported claims), B2 SAC = 0.757 (0 failed, 40 unsupported claims), A SAC = 0.000 (36 failed runs, 36 unsupported claims).
- `results/tables/P3-44_verdict.json`:
  - `label`: "AI-reviewed exploratory pilot; not human validated"
  - `reading_rule`: "A gain >=0.10 over B1; zero unsupported positives; advantage over B2 not explained by resources"
  - `verdict`: "fails zero-unsupported-positive guardrail"
  - `A_minus_B1`: -0.7368, `A_minus_B2`: -0.7566
- `results/tables/P3-44_case_scores_dev.csv` & `results/tables/P3-44_case_scores_heldout.csv`: Case-by-case and repeat-by-repeat accounting confirmed. All 140 planned runs accounted for without missing jobs.

### 4. Trace policies, error handling & pilot status
- Method A in held-out incurred 36 failed runs due to trace restriction enforcement (`adaptive_tool_outside_corpus_reader`), resulting in zero SAC score and retaining unsupported positive claim audits.
- Guardrail unit explicitly evaluated as retained claim representations rather than independent errors.
- Strict isolation and error policies confirmed: no out-of-corpus tools permitted, failed runs strictly penalized with zero coverage credit rather than discarded or retried.
- Protocol adherence confirmed: findings are strictly qualified as an exploratory AI-reviewed pilot without human validation or operational access certification.
