# P3-44 — AI-reviewed access pilot, protocol v2

Authorized by Felipe on 7 Nov 2026 before any v2 reference or model answer. This amendment replaces the planned human reference and audit with separate AI agents; it does not retroactively human-validate P3-28. Original model runs and complete raw corpus could not be restored. All model comparisons therefore use the same installed Codex runtime in a separately versioned experiment. No historical Claude score enters its ranking.

## Fixed comparison
Preserve P3-28's 17 cases, 229 fields, provider-family split, rubric, B0/B1/B2/A procedures and original reading threshold: A needs at least 10 percentage points more supported coverage than B1, zero unsupported positive availability claims, and improvement over fixed verification B2 not explained by resources. Otherwise report the corresponding null, failure or insufficient-evidence result. There is no tuning on held-out scores.

New source responses are frozen before labeling/runs. Exact old-byte matches are identified but changed text/extraction creates a new corpus. Public documents collected now describe a retrospective documentation exercise, not proof of availability at an earlier time. Missing documents stay unavailable for every method; report answerability by family.

The adapter freezes one configuration and 140 scheduled jobs: 20 development jobs (four methods once on five cases), 120 held-out jobs (B0 once and each model method three times on twelve cases). Development is reported without modifying the fixed methods. Every scheduled failure counts as zero coverage; missing execution cannot be described as a successful run. All attempts and traces are preserved. No quality-based retries.

## Reference and audit
Two separate, fresh-context AI agents receive only frozen sources, cases, fields and rubric. Neither receives method outputs or the other's labels. They write independent complete reference sheets and source passages. A third agent resolves disagreements from sources, retaining both original judgments. Unknown remains unknown where evidence does not decide. An adjudicated reference is hashed before scoring.

A separate agent then audits anonymized answers against the frozen sources without method identity. Audit all structured answers, notes, duplicates, extra fields and final raw prose; retain draft claims where the compared workflow emitted them. Complete explicit support/value/unsupported-claim decisions and AI reviewer identity are required. Agreement among AI reviewers is not human validation and may share systematic model errors.

## Resources and limitations
The same default installed runtime is used throughout; capture actual model identification where available. Cases run in source-only workspaces with ephemeral read-only CLI sessions. B1/B2 are prompted to use no tools; trace violations fail the run. A may read/search local allowed text only; saved traces are screened. These restrictions are prompt plus trace controls, not a claim of OS confidentiality.

Aggregate limits: 900 seconds and 12,000 output tokens per case execution, including both B2 calls; A at most 40 tool calls. Token/tool overages fail post-checks; token cap is not guaranteed server-side. Full usage, failures and trace compliance are reported. Unknown inference costs stay unavailable; scorer-compatible zero is never presented as free inference. Unverified matched-resource conditions prevent an unqualified adaptive-superiority conclusion.

## Delivery
Run scorer regressions and a separate agent verification; recompute scores from frozen records. Report paired case/family coverage, unsupported positives, unknown handling, failure counts, reference disagreement and resource use. Keep findings exploratory and new tasks in review. Deck adoption remains separate; no automatic main-deck insertion.

## Infrastructure amendment v3 — 7 Nov, before v3 runs
The v2 CLI executed inference but blocked adaptive shell document reads. These failures appeared in stderr rather than command events; returned unknown answers are not evidence of inferior research performance. The incomplete v2 batch is preserved under `runs/` with `experiment/runtime_failure.json` and is excluded from comparative scoring. No reference-based method scores were inspected or used to choose the repair.

A corpus-only stdio reader was tested successfully while keeping the CLI read-only sandbox. It exposes only list, literal search and bounded read of named public TXT sources in the case folder; it has no shell, network, write or parent-directory operation. All methods receive the same tool environment, with B1/B2 prohibited from calling tools and A restricted to these three tools. Every method is restarted in `runs_v3/`, under a new frozen configuration in `experiment_v3/`, using the same pinned model and unchanged rubric/cases/reading thresholds. Source-only AI references were locked before scoring and are reused; no model-answer tuning is allowed. Tool startup/read failures are recorded as failures, not correct abstentions. This is an infrastructure change, not a fresh untouched scientific holdout.
