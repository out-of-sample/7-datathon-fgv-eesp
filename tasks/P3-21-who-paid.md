---
id: P3-21
title: Who paid and who gained - the 23 Jun notice seen from five kinds of users of the digital dollar
phase: P3
status: doing
owner: CS 1
working: Renzo (agent)
due: 2026-11-04
depends: P1-02, P3-03, P3-11
---

## Goal
Turn the money result (F-015, F-025) into a table a reader understands in ten seconds: what the notice meant for a person
who needed dollars that month, a monthly saver, someone already holding USDT, someone who bought in the panic, and those who
sold. Each row follows a rule fixed in advance on the measured premium path. No trading strategy, no optimisation, no rule
chosen after seeing the path. It is an **illustration** (four language levels: illustrative), not new evidence. It
replaces the content of slide 9 if Felipe agrees; it does not add a slide.

## Specification (fixed before the script runs)
The premium path is already known (F-016, F-022, F-024), so this is not a blind test. The specification only prevents
picking convenient dates.

**Data.** `data/processed/P1-02_premium_daily.csv` (frozen to 30 Oct 2026): `premium_bps` and the PTAX sell rate per PTAX
day. No download.

**Counterfactual.** The premium had the notice not happened = the pre-notice level, the mean of the 20 PTAX days before
t0 = 23 Jun 2026 (15.2 bps, F-025). Variant: the post-spike level as the counterfactual (mean premium of the PTAX days 22 Jul – 30 Oct 2026, the after-spike window of F-015), to show how much depends on that
choice (F-022: the post-spike level is not distinguishable from drift).

**Money.** For a purchase of US$ X on PTAX day d: extra cost in R$ = (premium_d − counterfactual) / 10,000 × X × PTAX_d.
For a holder: gain from t0 to day d = (premium_d − premium_t0) / 10,000 × X × PTAX_d. Fees, spreads and taxes are the same
with and without the notice and are left out, except that spreads widened during the spike (F-021, exploratory): stated
as a limit, not modelled.

**The five users** (every date is a calendar rule or a signal available on the day):

| ID | Who | Rule | Reported |
|---|---|---|---|
| U1 | Needed dollars during the spike | Buys US$ 100k on one PTAX day in [t0+1, t0+20] | Average extra cost over the 20 days, and the range across days. Must reproduce F-015 (R$ 5,052, computed at a fixed PTAX of R$ 5.38) within 2%; daily PTAX used here, so a small gap is expected |
| U2 | Monthly saver | Buys US$ 10k on the first PTAX day of each month, Jan–Oct 2026 (US$ 100k in total) | Extra cost per month and in total. Variants: last PTAX day of the month; equal amounts every PTAX day |
| U3 | Already held USDT | Holds US$ 100k of USDT at t0 | Gain over the official dollar if sold on t0+1, t0+5, t0+20 or 30 Oct (fixed dates; never "at the peak") |
| U4 | Bought in the panic | Buys US$ 100k on t0+1 (24 Jun: the day the press reported the notice and the real-time monitor fired, F-014, F-023) and holds | Loss over the official dollar at t0+20 and at 30 Oct |
| U5 | Sellers as a group | – | Cited from F-025, not recomputed: R$ 106 mn on Binance (R$ 145 mn on three exchanges) went from buyers to sellers; who they were is inferred (F-025, F-031/F-032 exploratory) |

**Wording rules for the deck.** "Transferência", never "perda de bem-estar"; "ilustração com regras fixadas antes";
no advice on how to trade; no tax-avoidance framing ("diferença de alíquota", never "brecha").

## Subtasks
- [x] S1 — Commit this Specification before writing the script (the commit order is the record) — done: Renzo (agent), 2026-11-03
- [x] S2 — done: Renzo (agent), 2026-11-03 — `scripts/p3_21_who_paid.py`: U1–U4 and the variants → `results/tables/P3-21_who_paid.csv`; U1 reproduces F-015
  within 2%
- [x] S3 — done: Renzo (agent), 2026-11-03 (F-033) — Finding (illustrative) with the command; figure only if Felipe wants one for slide 9
- [ ] S4 — pt-BR slide-9 table and one-sentence takeaway for Felipe (deck owner), within the 10-slide limit
- [ ] S5 — Review by Felipe (money layer owner, P3-11)

## Success criteria
- [x] Specification committed before the script's first run
- [ ] U1 reproduces F-015 (R$ 5,052 per US$ 100k) within 2%
- [x] Every number in a finding with its command; the counterfactual variant reported next to the main one
- [ ] Felipe accepts or rejects the slide-9 replacement

## Outputs
- `scripts/p3_21_who_paid.py` (header: purpose, inputs, outputs, how to run)
- `results/tables/P3-21_who_paid.csv`; finding F-0xx (next free number)

## Handoff
- **State:** S1–S3 done and independently reviewed 3 Nov (Codex, see Review below): U1–U4 reproduce within R$ 1. Review fixes
  applied: U2 split by purchase date + every-day monthly rows, lower-bound claim removed, U3/U4 called revaluations, CSV
  committed, reviewer's scripts committed (`scripts/p3_21_review_rederive.py`, `scripts/p3_21_review_audit.py`, output
  identical to the review). F-033 stays exploratory. Criterion 2 (within 2% in R$) is **not met**: 93.91 vs 93.9 bps, but
  R$ 4,842 vs 5,052 (−4.2%) because F-015's R$ 5.38 is a Binance bid of 31 Oct (D-10), not a PTAX.
- **Next step:** S4, pt-BR slide-9 table (use the "purchases after t0" U2 numbers) + one-sentence takeaway; S5 Felipe.
- **Open questions:** (1) Team: accept the criterion checked in bps? (2) Resolved 3 Nov (Renzo): cover and F-015 now
  R$ 4,842 at daily PTAX, the same number as U1 here (decision log). (3) Felipe: slide 9 takes this table?
- **How to resume:** `.venv/bin/python scripts/p3_21_who_paid.py`; check with `.venv/bin/python scripts/p3_21_review_rederive.py`.

## Log
- 2026-11-03, agent for Renzo: created at Renzo's request (brainstorm version 2: who paid and who gained).
- 2026-11-03, agent for Renzo: claimed; post-spike counterfactual window pinned (22 Jul – 30 Oct, as F-015); Specification committed before any script (S1).
- 2026-11-03, agent for Renzo: S2–S3: script + F-033; U1 vs F-015 differs 4.2% in R$ only because of F-015's fixed PTAX 5.38; check made in bps (deviation disclosed).
- 2026-11-03, agent for Renzo: review fixes applied (U2 split by purchase date, every-day monthly rows, wording of F-033); CSV and the reviewer's two scripts committed with repo-relative paths.
- 2026-11-03, agent for Renzo: cover/F-015 switched to daily PTAX (R$ 4,842), so U1 and the cover now agree; review script extended to the new rows (90 of 90 match).
- 2026-11-03, Codex for Renzo (independent review): arithmetic reproduces; interpretation/reporting corrections requested below. Reviewed S1–S3 and prepared the cover decision for Felipe; S4/S5 remain open. Handoff preserved as requested; no analysis script, deck or F-015 changed; F-033 receives only a History entry.

## Result
<!-- fill when done -->

## Review — 2026-11-03, Codex for Renzo

**Verdict: reproduces with corrections to interpretation/reporting.** All reported U1–U4 amounts reproduce within R$ 1; there is no window, allocation, reference-premium or sign bug. The original reais acceptance criterion still fails. This review is not Felipe's S5 approval or a decision to replace the cover/slide.

### Evidence and commands

Reviewed checkout: `7a8534f`, after `git pull --rebase` (already up to date). Commands below run from the repository root. Scratch code and output are outside the repository, as requested; they are local review artifacts, not files shipped to teammates by this commit.

- **A — independent arithmetic:** `.venv/bin/python /tmp/p3-21-review/rederive.py` (output saved as `/tmp/p3-21-review/rederive.txt`). A retained copy is at `/home/renzo/.codex/visualizations/2026/11/03/01a1a22b-b587-7d01-8934-64f3939ea8af/p3-21-review/rederive.py` (same command with that path). Uses only stdlib CSV parsing, date comparisons, explicit transaction lists and the Specification's formulas; never imports or executes the author's script. Script SHA-256 (`sha256sum /tmp/p3-21-review/rederive.py`): `538210510775e776c4262663544f0fe2a485a25395b7730fb7c0ec2e9e103f81`. Input SHA-256, printed by A: `47982f7940d3dac8c4a127083fd3322ff9aa25bb4e1568ae3b09ac54411289b4`. A prints the monthly values, all table comparisons, U2 time decomposition, conversion alternatives and the U5 citation check. All computed amounts below are from A unless another command is named. The author's portable reproduction command remains `.venv/bin/python scripts/p3_21_who_paid.py`; the independent scratch artifact is intentionally not added to Git.
- **B — registration:** `git log --reverse --format='%h %aI %cI %s' -- tasks/P3-21-who-paid.md scripts/p3_21_who_paid.py`; `git show --stat 79e15d1`; `git show --stat 7a8534f`; `git show 79e15d1:tasks/P3-21-who-paid.md`; `git ls-tree -r --name-only 79e15d1 -- scripts/p3_21_who_paid.py`; `git diff 79e15d1 7a8534f -- tasks/P3-21-who-paid.md`.
- **C — FX provenance:** `rg -n 'D-10|5\.380|5\.38|5,38' docs/sources.md tasks/P3-01-money-layer.md findings/F-007-noise-floor.md scripts/p3_01_costs.py`; `git log --all -S 'BENCHMARK_PTAX' --oneline -- scripts/p3_01_costs.py`; `git show 339782f:scripts/p3_01_costs.py | head -55`; `sed -n '10,27p' findings/F-015-route-costs.md`.
- **D — requested occurrence inventory:** `grep -rn "5.052\|5,052\|5.050\|5,050\|621\|620" deck/ findings/ docs/ notebooks/ STATUS.md > /tmp/p3-21-cover-grep.txt`. Supplement for unseparated digits: `rg -n '5052|5050' notebooks/p5_07_story.ipynb --max-columns 300 --max-columns-preview`. See the complete relevant file/line inventory below; line numbers refer to the reviewed checkout, before this append.
- **E — accounting/wording:** `cat findings/F-033-who-paid.md findings/F-025-money-moved.md findings/F-021-band-tar.md`; `cat scripts/p3_11_money.py`; `sed -n '65,87p' scripts/p1_02_premium.py`.
- **F — original rounded conversion:** `.venv/bin/python -c 'import csv; r=next(r for r in csv.DictReader(open("results/tables/P2-03_event_table.csv")) if r["event_id"]=="E-05" and r["eval_date_kind"]=="effective"); print(r["diff_bps"], float(r["diff_bps"])*10*5.38)'` → `93.91 5052.358` (floating-point display may end in repeated nines).
- **G — calendar and inventory counts:** `.venv/bin/python /tmp/p3-21-review/audit_sources.py` cross-checks the savings dates against the frozen raw PTAX calendar, groups D's captured matches and counts the explicit freeze work list below. Script/output retained beside A's retained copy. The occurrence inventory is a snapshot of the reviewed revision; later review annotations will themselves add matches.

### Registration, departures and delivery

B confirms the Specification is in `79e15d1` (committer time 3 Nov, 10:01:20 −06:00), with no tracked script at that revision. The next commit, `7a8534f` (10:02:30 −06:00), introduces the script and finding. The Specification itself is unchanged between them. This proves the Git ordering, not what might have existed untracked on the author's machine. The path was already known; this is not a blind design or preregistration before seeing the data.

- **Disclosed departure:** the final assertion tests the premium in bps instead of the specified reais tolerance. U1 is R$ 4,842.04 versus R$ 5,052.36 in F-015, about 4.16% lower, so the ±2% reais criterion remains unmet (A, F). The S2 checkbox/header/error message still describe the old check. Matching bps does not retroactively satisfy that criterion; the team must explicitly accept a revised criterion if desired.
- **Additional reporting omission:** U2 promises cost per month and in total, with first-day, last-day and every-day variants. The script exports monthly rows for the first two but only the total for the every-day variant. Under the per-month reporting requirement, add those monthly rows; A supplies them. If the author intended the per-month promise to apply only to the main rule, state that narrower interpretation explicitly. This omission does not alter any reported value.
- **No other formula or date departure found.** U3/U4's counterfactual columns are correctly left empty in the finding; their own buy-day reference is used. U5 is cited rather than recomputed, as specified. Applying the constant reference to pre-notice U2 purchases follows the Specification; its economic problem is in the Specification/claim, not an undisclosed implementation change.
- **Delivery mismatch:** the CSV is not in `7a8534f` despite the Handoff saying the table was committed. `git show --stat 7a8534f` lists no CSV; `git ls-files results/tables/P3-21_who_paid.csv` is empty; `git status --short` showed `?? results/tables/P3-21_who_paid.csv` at session start. It exists locally and reproduces, but teammates must generate it. Left untouched/uncommitted in this review.

### Independent results and specific bug checks

A checks chronological unique dates and finite inputs. Pre-notice: 20 PTAX days, 25 May–22 Jun, mean 15.23655124 bps; spike: 20 PTAX days, 24 Jun–21 Jul, mean 109.14385169 bps; post-spike: 71 PTAX days, 22 Jul–30 Oct, mean 26.77926977 bps. The event day is excluded from both pre and spike. The frozen input ends on 30 Oct. Dates at t0+1, +5 and +20 are 24 Jun, 30 Jun and 21 Jul. The source table has no missing PTAX dates during the savings horizon (cross-check against `data/raw/bcb/ptax.json`, using its `dataHoraCotacao` dates).

Every numeric U1–U4 cell in F-033 is checked below. Amounts are R$, rounded only at the end; **all match F-033** (A).

| Quantity | Independent, pre-notice reference | Independent, post-spike reference |
|---|---:|---:|
| U1 mean | 4,842 | 4,249 |
| U1 minimum | 1,895 | 1,308 |
| U1 maximum | 8,824 | 8,227 |
| U2 first day total | 492 | −104 |
| U2 last day total | 345 | −251 |
| U2 every day total | 402 | −192 |
| U3 sold 24 Jun | 6,802 | not applicable |
| U3 sold 30 Jun | 5,487 | not applicable |
| U3 sold 21 Jul | 1,407 | not applicable |
| U3 sold 30 Oct | −2,992 | not applicable |
| U4 valued 21 Jul | −5,223 | not applicable |
| U4 valued 30 Oct | −10,070 | not applicable |

The displayed reference levels 15.24/26.78 bps also round correctly. A checks all 58 CSV rows (including monthly first/last-day amounts): no rounded mismatch; largest absolute discrepancy from the unrounded independent value is R$ 0.496. U5's R$ 106/145 mn correctly rounds F-025's stored headline amounts 106.091/145.267 mn; checked as a citation, not an independent volume recomputation.

For U2 every-day, monthly PTAX counts Jan–Oct are 21, 18, 22, 20, 20, 21, 23, 21, 21, 21. A explicitly allocates US$ 10,000 divided by each month's count and verifies the monthly total. The original `groupby(...).transform("size").rdiv(10_000)` implements that same allocation; it does not distribute the entire horizon uniformly. U3 references the 23 Jun premium (24.83676824 bps); U4 references 24 Jun (155.39943686 bps), never either mean counterfactual. Positive means purchase cost for U1/U2 and gain for U3; U4 negatives mean deterioration in the premium component. No sign reversal found.

### Interpretation corrections before jury use

1. **U2 is mis-specified as a cost caused by the notice.** For the main first-day rule, Jan–Jun contributes −R$ 260.63 and Jul–Oct +R$ 752.98, net +R$ 492.35. Under the post-spike reference those pieces are −R$ 618.98 and +R$ 514.83, net −R$ 104.15 (A). A later notice cannot cause an earlier purchase cost. The same flaw affects the main reference, not just the post-spike variant. June's last-day purchase is after the notice; every-day June straddles it, so any treatment split must be by transaction date, not by month. A prints that split for every rule.
   A comparison with a constant premium across Jan–Oct is meaningful **as a descriptive benchmark scenario**, including an ex-post reference, but is not a defensible no-notice treatment counterfactual over the whole horizon. Keep the registered totals if clearly relabelled; if the team wants an attributable post-notice cost, register and disclose a revised comparison with identical pre-event histories. The diagnostic split above is not a new causal estimate. "Almost nothing for a regular monthly saver" and "only ... in the year" overreach: this is one notional, one Jan–Oct schedule, one known episode; it is not a full year or a general saver result.
2. **F-021 does not establish widened transaction bid–ask spreads.** It estimates a no-arbitrage band from premium dynamics (E). Therefore "U1 and U4 are lower bounds in size" is unsupported. Equal fees cancel in a comparison; the differential execution costs against the hypothetical alternative are not observed. Say these are premium-only illustrations excluding fees, taxes and execution costs, without a bound. The Specification itself inherited this spread/band confusion; the lower-bound claim in F-033 strengthens it further.
3. **U3/U4 are premium revaluations, not identified notice gains/losses or complete portfolio P&L.** The buy-day premium reference and sale-day FX follow the requested formula, but do not isolate the notice from all other changes through October, model fixed-token USDT/USD moves, or subtract actual execution costs. U4 has not sold: "Every amount is a transfer" incorrectly treats an unrealised mark as cash changing hands. Restrict transfer language to actual/hypothetical purchases and sales and the gross-flow U5 calculation; label held positions as revaluations. U5 is gross trading flow, not sellers' net profit or evidence identifying who sold.
4. **Language rules otherwise pass.** F-033 explicitly says illustration on an already known path and rejects welfare-loss interpretation; it gives no trading or tax-avoidance advice. Still, "the notice cost/gave" needs the qualifications above. "Up to R$ 6,800" is only among the selected U3 sale dates, not a maximum over all possible sales; retain the fixed-date wording. A calendar/signal day and a PTAX-window average are not evidence that a user could execute at that price after observing the signal.

### Cover: provenance, options and recommendation for Felipe

**The reference is mislabelled.** C traces `BENCHMARK_PTAX = 5.3800` to **Binance USDT/BRL best bid**, with ask 5.3804, checked **31 Oct 2026 at 16:43 UTC** in D-10 and F-007. It is neither a dated BCB PTAX nor a mean over the spike. The script cites D-10 in its comment and the P3-01 task repeats that provenance; F-015 merely calls it reference PTAX, with no date/source for the rate. The initial script already used this fallback; the later audit fixed it as a constant. A current API quote would not verify the historical snapshot, so this review uses the repository's dated record rather than replacing it with a live quote. There is no cited BCB source for **5.38 as PTAX** in this chain.

The conversions are distinct (A and F):

| Method | Spike cost per US$ 100k |
|---|---:|
| F-015: rounded event-table 93.91 bps × fixed 5.38 | R$ 5,052.36 |
| Full-precision daily-data premium change × mean PTAX 5.14177 | R$ 4,828.50 (about R$ 4,830) |
| Rounded 93.9 bps × mean PTAX 5.14177 | R$ 4,828.12 |
| Mean of each day's excess premium × that day's PTAX | R$ 4,842.04 |

Mean of products is not product of means: premium/FX covariance accounts for R$ 13.54 between the full-precision mean-rate and daily-rate calculations. F-015 also takes an already rounded premium from the event table; this is immaterial at the stated R$ 1 tolerance, but the discrepancy is not literally only an FX ratio. For the post-spike descriptive amount, the corresponding fixed-rate / mean-period-rate / daily-rate values are R$ 621.00 / 592.87 / 583.10 (A). None establishes a persistent effect.

- **Keep R$ 5,052:** a constant exchange-rate numeraire is valid for comparing standardized route scenarios; it preserves existing reais tables, and the multiplication is easy to reproduce. It must be labelled a **reference exchange rate**, sourced to D-10, not a PTAX observation or actual period cost. Stating "PTAX R$ 5.38" alone would preserve a factual error. For a jury reading without a presenter, the cover must itself carry the hypothetical-rate qualification. It also leaves a conversion convention different from F-025 and F-033, requiring explanation.
- **Switch to actual-window PTAX:** directly links the reais illustration to its dates and the frozen input, removes the arbitrary later snapshot, and makes it easier to reconcile the cover with F-033. Using daily products follows F-025's conversion convention (E); F-025 remains volume-weighted over calendar days, while U1 equally weights PTAX days, so their numerical averages need not coincide. The mean-rate approximation is reproducible but does not fully match that convention. The disadvantage is coordinated edits and rebuilt outputs before the Wed 4 Nov freeze, not a need to rerun the event study or change the bps finding.

**One recommendation:** switch to actual-window conversion and use **R$ 4,842**, the daily-PTAX implementation of the “about R$ 4,830” option, rather than introduce a second approximate convention beside F-033/F-025. Exact proposed cover line:

> De 24/jun a 21/jul/2026, o prêmio do USDT na Binance ficou 93,9 bps acima da média pré-ofício: R$ 4.842 a mais por US$ 100 mil, em média, à PTAX de cada dia.

On the cover or immediately visible source note, identify the pre-ofício mean as the preceding PTAX-day window and the amount as a premium-only illustration; put the precise averaging formula and source in the annex. This recommends a presentation choice, not a team decision. Felipe owns acceptance and all ensuing edits.

### Every occurrence and change surface

D produced the following **10 files with relevant text** at the reviewed revision. Historical entries should retain their history, with an appended correction/reference rather than a silent global replacement.

| File | Lines with requested figures | Location/use |
|---|---|---|
| `deck/deck_v1_ptbr.md` | 31, 35, 39, 45; 235, 249 | Slide 1 cover/notes; slide 9 per-lot cost/notes |
| `deck/annex_v1_ptbr.md` | 116, 117, 300 | B.5 spike/post-spike rows; D.2 cover traceability |
| `deck/deck_apresentacao.html` | 385, 388, 395, 732 | Rendered slides 1 and 9 |
| `findings/F-015-route-costs.md` | 3, 12, 13, 26, 27, 66 | Title, claim, table, prior History |
| `findings/F-033-who-paid.md` | 32 | Comparison with F-015 |
| `docs/deck-changes-2026-11-02.md` | 72 | Historical review gap |
| `docs/handoff-prompt-2026-11-02.md` | 15 | Historical headline summary |
| `docs/deck-plan-10-slides.md` | 18, 68, 131 | Cover plan and review notes |
| `notebooks/p5_07_story.ipynb` | 595, 610, 611; also 594 | Cached post-spike output, narrative; supplemental search finds unseparated `5052.36` at 594 |
| `STATUS.md` | 16, 59, 64, 70, 185, 208, 238 | Current summary/decisions, generated finding title, historical activity |

The raw requested regex also matches unrelated data: annex line 38 and F-018 line 45 (`0.6219`); F-030 line 52 (`0.621`); base64 image payloads at HTML 549/553/583/614/644/674, story notebook 200/417/707, and premium-plots notebook 278/323. These are not textual money occurrences. Do not replace digit sequences inside image data; rebuild any affected figures from their source. Outside the requested search scope, the P3-01 script's header and figure subtitle contain the figures (`rg -n '5,052|5.052|621|620' scripts/p3_01_costs.py`); its CSV and PNG are generated outputs.

**Freeze workload:** the affected main-deck content is **two slides (1 and 9)**, plus annex B.5/D.2, not a deck redesign. For a consistent switch, the explicit work list is nine source/document files (`scripts/p3_01_costs.py`, `tasks/P3-01-money-layer.md`, `docs/sources.md` for the mislabeled reference-rate use, F-015, F-033, deck Markdown, annex Markdown, story notebook, STATUS) and three generated files (P3-01 CSV/PNG and deck HTML): **12 existing files plus the final PDF export**. This is a planning count of the enumerated files, not a claim all regex hits are live deliverables. The three historical docs above can receive dated pointers if they remain active handoff material. Keeping the reference requires fewer recalculations, but still needs provenance/wording fixes and regenerated presentation outputs; it is not a zero-edit option. Route-comparison scenarios may retain the explicitly labelled reference exchange rate while the headline rows use daily PTAX. Do not silently rescale all bank-route comparisons.

**Next step:** Felipe/team accept or reject the conversion and wording; owner resolves U2's interpretation, the lower-bound/transfer language, and the reporting/delivery omissions. This review leaves the Handoff, task status, S4/S5, F-033 body/status and F-015 untouched.
