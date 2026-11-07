# P3-28 protocol — agentic access map, evaluation (S3)

**Status: v1, frozen at the commit that adds this file, before any held-out run.** Later changes create v2 with a
dated entry in §10 and, after any held-out score is seen, a fresh test set for any new claim (spec S4). Spec:
`tasks/P3-28-agentic-access-map.md`. Code: `scripts/p3_28_access_map.py` (corpus, forms, adjudication, cards) and
`scripts/p3_28_methods.py` (methods, scoring).

## 1. Question, metric, reading rule (from the spec, unchanged)

- **H1:** with the same corpus, model and resource ceilings, does a tool-using agent (A) answer more access-condition
  questions correctly **with valid supporting evidence** than one retrieval pass plus one model answer (B1)?
- **Primary metric, SAC (supported answer coverage):** per case, the answerable reference fields answered correctly
  with valid evidence, divided by the answerable reference fields. Macro-average over the case's repeats, then over
  held-out cases. A field is answerable when the reference state is not `unknown`/`not_applicable` (for value fields:
  when the reference has a value).
- **Guardrail:** count every `supported` answer on an availability field where the reference is not `supported`, or
  whose evidence is invalid. A passes only with **zero** in the held-out runs.
- **Reading rule:** H1 gets preliminary support if A's held-out SAC is at least **10 percentage points above B1**, A
  passes the guardrail, and the gain is not explained by budget alone. **B2 is mandatory:** if A does not beat B2 at
  comparable quality, the conclusion is "verification helps; agentic adaptation is not established". Paired
  differences by case and per-family results are reported; with 12 held-out cases in 3 families, uncertainty is
  descriptive. Repeats and fields are not independent events.

## 2. Cases and split (`results/tables/P3-28_cases.csv`)

| Split | Families | Cases |
|---|---|---|
| development | Foxbit (D-01 company USDT TRC-20, D-02 company USDC ERC-20, D-03 individual USDT TRC-20); funds' channel (D-04 intermediation, D-05 own account / in-book arbitrage, as of 26 Jun 2026) | 5 |
| held-out | Avenia (H-01–H-04), Binance (H-05–H-08), Mercado Bitcoin (H-09–H-12) | 12 |

Whole provider families are held out, never single pages. Fields (`results/tables/P3-28_fields.csv`): F01–F15 for
exchange cases (15 each), G01–G02 for the funds' cases: 229 case × field rows. **Smaller than the spec's targets (12 development, 24
held-out): this is a pilot.** It reports case results and limitations, not a broad reliability claim. Cases were
fixed from the source inventory before any model output.

## 3. Corpus

- Sources: `results/tables/P3-28_sources.csv`; frozen snapshots in `data/raw/p3_28/` (out of git, SHA-256 in
  `data/raw/SHA256SUMS`); text extracts and per-source hashes in `results/tables/P3-28_corpus.csv` (committed).
- Each case sees only its provider family plus shared context (BCB rules E-14/E-06b, Blue Consult E-20, issuer pages
  A-11/A-24). Every method sees the same set (`permitted()` in the methods script).
- **Binance and Mercado Bitcoin refuse scripts.** No automated workaround was used. Renzo saves those pages in his own
  browser (`data/raw/p3_28/manual/<id>.html`). `snapshot` freezes them with `fetch=manual, saved_by=Renzo`, and the
  corpus is re-hashed (v2) before held-out runs. Pages Renzo cannot find stay missing; the affected fields then have
  reference `unknown`.
- **What the implementer saw of held-out documents.** Avenia pages were picked from the site map by URL path. The
  implementer read their titles, the first 600 characters of A-13 and the first 400 of A-23 (extraction checks), and
  nothing else. Binance and Mercado Bitcoin pages were picked from web-search titles and snippets. No held-out document
  shaped the prompts or the field keywords.

## 4. Reference

- Two human coders, **Felipe and Jonathan**, code all 229 rows independently from the corpus zip, with the rubric
  `results/P3-28_rubric.md`. No AI, no web, no discussion before both sheets are in. Sheets go privately to Renzo and
  are kept **outside the repository** until all held-out runs are complete and hashed.
- `adjudicate` prints counts only; the coders settle `disagreements.csv`, Felipe ruling on scope. Initial agreement is
  reported. The adjudicated reference gets a SHA-256 hash, committed before scoring.
- G1: both coders could apply the rubric; critical unknowns stay explicit.
- **Development reference used to build the methods:** `data/processed/P3-28_dev_reference_agent.csv`, coded by
  Renzo's agent (one coder, development only). Final development results are also re-scored against the human
  reference.
- **Deviation from the spec's order:** the spec has reference labels before held-out runs. Here held-out runs come
  first and their outputs are hashed (§8) before the reference exists. Outputs cannot be tuned to labels that do not
  yet exist, and the coders never see outputs. The protection against test-set tuning is the same or stronger; the
  deviation is disclosed.

## 5. Methods (all frozen)

| | B0 | B1 | B2 | A |
|---|---|---|---|---|
| Model | none | `claude-sonnet-5-5` | same | same |
| What it does | regex rules on 3 fields + the taker fee; `unknown` otherwise | fixed BM25 keyword retrieval (TOP_K = 8 chunks of 700 characters per field; field keywords, plus asset/network and profile words for listed fields), one call, no tools | same retrieval; extract call; verify call against the same chunks; deterministic verbatim filter | Read/Grep/Glob over the permitted .txt files in a sandbox; chooses its own searches; must confirm passages with Grep |
| Model calls / tools | 0 / 0 | 1 / 0 | 2 / 0 | 1 session, ≤ 40 turns |
| Ceiling | – | 900 s | 900 s per call | 900 s |

Shared system prompt (rubric condensed) and JSON schema: `SYSTEM`, `SCHEMA` in `scripts/p3_28_methods.py`. Each run
logs the prompt hash (system prompt + schema + keywords + case text). **CLI:** Claude Code 2.1.318, bundled with the
VS Code extension, run with `--restricted --strict-mcp-config --no-session-persistence --tools <set> --system-prompt`.
That means no user, project or local settings, no MCP servers, file tools confined to the sandbox, no shell, no web.
Isolation test passed on 7 Nov: no instructions or memory loaded, reads outside the sandbox denied, no web or shell
tool. Leaks: the CLI injects the account e-mail into context, and makes a small internal `claude-haiku-5-5` call (logged
in `usage`). Runs use Renzo's plan, no API key; `notional_usd` is the CLI's estimate, not money spent.

**Repeats:** 3 scheduled for B1/B2/A, 1 for B0 (deterministic). No run is selected, dropped or re-run for quality. A
failed or timed-out run is scored as zero answered fields. An infrastructure-wide outage is reported separately and
re-run only in full (all methods for those cases).

## 6. Scoring (`score()` in `scripts/p3_28_methods.py`)

- state fields: same state. F02: state plus yes/no. F13: state, plus the date when the reference gives one.
- numeric fields F04, F08, F12: same number (1% tolerance). Limit basis F05, F14: same category (case by case / by
  level / fixed amount, the last also needing the same number). G02: both null or both non-null.
- valid evidence: at least one `{source_id, passage}`, every passage found verbatim (after whitespace and entity
  normalisation) in a permitted source. Semantic support is checked by hand at G2 for every positive claim.
- secondary: unknown kept on reference-unknown fields, all-unknown rate, failed runs, calls, turns, tokens, wall time.

## 7. Commands

```bash
.venv/bin/python scripts/p3_28_access_map.py snapshot && .venv/bin/python scripts/p3_28_access_map.py corpus
.venv/bin/python scripts/p3_28_methods.py run B0 heldout
.venv/bin/python scripts/p3_28_methods.py run B1 heldout --repeats 3 --workers 2   # same for B2, A
.venv/bin/python scripts/p3_28_methods.py score <adjudicated_reference.csv> heldout
```

## 8. Held-out run record

- **Avenia family (H-01–H-04), 7 Nov 2026:** 40 runs (B0 ×4; B1, B2, A ×3 repeats ×4 cases), all complete: 15 answers
  each, no errors or timeouts. Hashes: `results/tables/P3-28_heldout_run_hashes.csv`, committed before any reference
  label exists (the coders have not started). The implementer checked run health only (counts, turns, errors), not
  the answers. A used 28–58 turns as reported by the CLI's `num_turns`, above the `--max-turns 40` ceiling with no run
  stopped by it. The CLI's `num_turns` therefore counts more than the turns the ceiling limits (for example tool
  results). Reported as is; the ceiling setting is unchanged.
- **Binance and Mercado Bitcoin (H-05–H-12):** pending Renzo's manual saves, then corpus v2 (`corpus`), then the same
  commands; hashes appended to the same file before the reference hash.

## 9. Development results (agent-coded development reference, one run per case)

Pilot-1, 7 Nov 2026, 5 development cases, after the pilot-0 changes and the two pilot-1 corrections in §10:

| Method | SAC (macro over 5 cases) | Unsupported positives | Reference unknowns kept unknown | All-unknown rate |
|---|---|---|---|---|
| B0 | 0.147 | 0 | 8/8 | 0.84 |
| B1 | 0.754 | 1 | 8/8 | 0.12 |
| B2 | 0.854 | 1 | 8/8 | 0.12 |
| A | 0.866 | 1 | 8/8 | 0.11 |

All three unsupported positives are D-05 G01: every model method reads the press report that the BCB "'liberou'" in-book
arbitrage as `supported`; the agent's development label is `conditional` (the FX suspension stays until each
institution's alignment). This label is contested, and the human reference decides it. These development numbers use
labels written by the implementer and adjusted twice after seeing outputs (§10), so they are **not** evidence for H1.
Reproduce: `.venv/bin/python scripts/p3_28_methods.py score data/processed/P3-28_dev_reference_agent.csv dev --tag _dev`.

## 10. Development amendment history (before freeze)

- Pilot-0 (D-01 only, one run each; kept in `data/raw/p3_28/runs_pilot0/`): A 0.92, B1 0.54, B2 0.38, B0 0.15 SAC.
  Changes after it: (1) evidence became `{source_id, passage}` pairs, because A's one-source/two-passage answer was
  misread as invalid (a scoring artefact, for all methods); (2) the B1/B2 retrieval query no longer uses the English
  question text or the asset/network on every field: Tether's page was crowding out every field (bug); (3) TOP_K 4 → 8
  and profile words added for profile fields (fair baseline); (4) two rubric rules added to both the rubric and the
  prompt ("can" questions and ordinary requirements; F06 for applicants, per Felipe's D-01 ruling); (5) the
  development reference corrected: D-01/D-02 F07 is `conditional` (separate commercial analysis), not `supported`.
- Pilot-1 (all 5 development cases, one run each), scoring and labels only, with no change to the methods or
  prompts: (6) cited source IDs are stripped of a trailing `.txt` (the agent cites the sandbox file name), for all
  methods; (7) development label D-03 F05 corrected to "by account level" (Foxbit: R$ 5,000 simplified, R$ 75,000
  verified). Kept as is, for the human coders: D-01/D-02 F04 (A-03 "costumam ser aprovadas em 1 a 3 dias úteis" against
  A-07 "pode levar até 72h"); D-05 G01.
- **Freeze:** v1 is frozen at the commit that adds this text. Settings: MODEL `claude-sonnet-5-5`, CLI 2.1.318,
  TOP_K 8, CHUNK 700, MAX_TURNS 40, TIMEOUT_S 900, repeats 3 (B0: 1).

