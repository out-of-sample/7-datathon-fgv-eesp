---
id: P3-29
title: Reconcile reported BRLA supply changes with on-chain evidence
phase: P3
status: review
owner: Team
working: -
due: 2026-11-07
depends: P3-27
---

## Goal
Build a reproducible reconciliation of reported BRLA supply changes against contract state, token events and verified cross-chain links. Test how much the observable ledger can explain, preserve unresolved differences, and establish whether the project can add evidence about digital-dollar infrastructure beyond its price results.

**Planning status:** formalized at Renzo's request on 6 Nov 2026; no blockchain collection or experiment has started. `owner: Team` means assignment is pending. The due date is a **feasibility/readiness checkpoint**, not a commitment to finish the study before submission. Suggested roles: CS implementer, economist for interpretation, and a different teammate for reproduction. Claim work through `prompt.md` §7.

## Questions and hypotheses

**Primary question:** Can the BRLA supply change reported around 23–24 June be reconciled with independently retrieved on-chain records, and which parts remain unidentified?

| ID | Question / hypothesis | Test | What would weaken or reject it |
|---|---|---|---|
| H1 — accounting | Verified contract changes and the provider's documented circulation definition account for the reported change within a predeclared measurement tolerance. | Reconstruct contract supply and eligible excluded balances at aligned blocks; compare changes with the frozen provider series. | Missing historical state, unknown circulation rules, incomplete contract coverage or a residual beyond tolerance. |
| Q2 — attribution | How much reflects mint/burn activity, documented circulation adjustments, verified migration between networks, or unresolved differences? | An evidence ledger with transaction references and explicit bridge/message links where applicable. | Similar amounts or timing without a documented link; a balanced ledger without evidence of the underlying economic purpose. |
| Q3 — generalization | Does the procedure work outside the already inspected June episode? | Freeze additional episodes before investigating their transactions; report all selected cases. | It works only after case-specific manual adjustments, or other cases lack the required data. |
| H4 — optional tool study | Adaptive investigation produces more correctly supported explanations than a fixed evidence workflow at a comparable resource cost. | Paired held-out comparison with a deterministic baseline and a fixed-context LLM baseline. | No incremental benefit, invented links/causes, or a gain that depends on more information or compute. |

H1 is an accounting-identification hypothesis, not a causal hypothesis about the BCB. H4 is optional and separate: on-chain reconciliation can be useful without an LLM. A negative or incomplete reconciliation is a valid result if its limits are demonstrated.

## Connection to the current project

- F-009/F-016/F-018 establish the observed price episode across the measured venues/pairs. They motivate investigating infrastructure; they do not identify the transactions behind the premium.
- Exploratory F-037 contains a BRLA/USDC price observation and an aggregate Celo supply drop following a prior increase. It **does not inspect mint/burn or bridge logs**. This task adds transaction-level evidence and checks whether the supply series supports the interpretation suggested by its shape.
- F-024 measures recorded **net stablecoin acquisitions** in a separate statistical system. It is not a gross supply measure and cannot be equated to BRLA minting or a blockchain transfer.
- F-028/F-030 leave route availability unresolved. Even a fully reconciled token ledger cannot establish fiat access or reopening.
- P3-18 was dropped because verified Foxbit USDT addresses were unavailable. This task starts with issuer-published token contracts, not guessed exchange wallets. It does not infer geographic capital flows from transfers involving a foreign exchange.

**Incremental contribution required:** new historical contract/event evidence, a reproducible reconciliation method and an explicit residual. Replotting the existing supply series or calling a supply decrease a redemption does not satisfy the task.

## Deliverable and unit of analysis

The minimum product is a read-only script that takes a token, verified contract, network and time interval and produces a supply bridge from opening to closing stock, an evidence ledger and a residual/coverage report. A static figure and machine-readable tables are sufficient. No smart-contract deployment, wallet connection, transaction signing or trading product is required.

**Unit:** token representation × chain × contract × interval between two specified finalized blocks. A multi-chain episode groups these units and any verified linking transactions. Report native token units, not market value, unless conversion is separately specified and sourced.

**Development case:** BRLA around the already observed June episode, initially 19–30 Jun 2026. Include the preceding rise as well as the fall. Freeze exact boundaries after checking timestamp semantics but before classifying events. This is a retrospective case selected after seeing the aggregate outcome; it cannot be sold as a blind detection or an independent test of the original economic hypothesis.

Start with Celo. Extend to other issuer-verified representations only as data permit. The first output may be a one-chain reconciliation with an explicit coverage boundary; it must not be called a global BRLA supply audit.

## Source and data feasibility

Read F-037, P3-24, `scripts/p3_24_brla.py`, `data/README.md` and the Flash-derived `data/raw/flash-mentor-leads/brla/brla_supply_by_chain_daily.csv`. Treat that CSV as a derived input: find its underlying frozen response, transformation, units and timestamp convention. If it cannot be recovered, preserve the old series as supplied and document the provenance gap. A fresh provider response is a new version, not a silent replacement.

**Contract candidates from current issuer terms (T-06/R-11):**

| Network | Candidate contract |
|---|---|
| Polygon | `0xe6a537a407488807f0bbeb0038b79004f19dddfb` |
| Celo | `0xfecb3f7c54e2caae9dc6ac9060a822d47e053760` |
| Gnosis | `0xfecb3f7c54e2caae9dc6ac9060a822d47e053760` |
| Moonbeam | `0xfeb25f3fddad13f82c4d6dbc1481516f62236429` |

These are leads, not proof that each contract/version operated in June. Verify chain ID, historical bytecode, deployment date, issuer attribution, proxy/implementation history, ABI and decimals. The same address on two chains is two different records. Do not include a Base representation without verified attribution. A token name or explorer label is insufficient.

Check the BRLA provider identifier (365 in the existing data notes) against issuer contracts and network metadata. Locate the relevant provider adapter and version history; establish what its `circulating` series actually measures, which representations it includes, and whether historical values were revised. Do not assume current code describes the historical computation. An unknown definition is an identification limit.

**First-session smoke test, before bulk collection:** retrieve chain ID, one historical block/header, historical code and `totalSupply`, a small known log interval, and one transaction receipt. Verify decimals from the implementation or a reliable source; ERC-20 makes the `decimals` method optional. Historical state access and historical log access are separate capabilities. A pruned-state error, rate limit, truncated response or failed endpoint is not a zero balance or an empty event set.

Allocate at most one focused feasibility session (target 90 minutes), with up to two documented public providers per required capability. Respect endpoint limits and cache responses. If access fails, report the specific capability gap and use a disclosed partial scope or stop. Do not assume paid RPC, explorer keys or private wallets are available; no paid procurement is authorized by this specification.

## Accounting model and evidence rules

For one verified contract between blocks `b0` and `b1`, define:

```text
delta_S = totalSupply(b1) - totalSupply(b0)
R_stock = delta_S - (verified_mints - verified_burns + verified_other_adjustments)

C_hat(t) = totalSupply(t) - eligible_excluded_balances(t)
R_provider = delta_reported_circulation - delta_C_hat
```

`verified_other_adjustments` is not a plug. It is allowed only for a documented mechanism, such as a rebase or an implementation migration, with independently reproducible state evidence. When the relevant implementation does not emit complete compatible mint/burn events, ordinary transfer logs cannot establish the first identity on their own. Inspect implementation semantics rather than assuming every zero-address transfer is sufficient evidence.

`eligible_excluded_balances` must follow the verified provider definition and dated address roles. Do not invent a treasury exclusion because it makes the numbers match. If that definition cannot be established, report the stock identity separately and mark the provider reconciliation `not_identifiable`; do not substitute `totalSupply` for circulation.

**Numerical and timing rules:**

- Use integer base units for contract accounting and explicit decimal conversion at presentation. Never use floating-point equality for token balances.
- Expect zero base-unit stock residual when the complete contract mechanism is known; any exception needs a source and a predeclared rule.
- Derive provider tolerance from its documented rounding/precision and timestamp uncertainty, before matching results. Do not tune tolerance to the observed residual. Report raw differences even when within tolerance.
- Map each documented snapshot time to the last canonical finalized block at or before it. Record UTC time, block number/hash and retrieval time; the event interval is `(b0, b1]`.
- If snapshot timing is undocumented, report `time_alignment_unknown`. Show predeclared UTC/Brasília boundary sensitivity if useful, but never select the alignment that closes the ledger and call it verified.
- At multi-chain level, define the economic claim being counted. Locked originals and wrapped representations may refer to the same claim; summing their supplies can double-count. Include bridge escrow/in-flight treatment only when the relevant mechanism and balances are verifiable.

**Evidence categories:**

| Category | Sufficient evidence | Forbidden shortcut |
|---|---|---|
| Contract mint/burn | Verified implementation semantics, transaction receipt/event and matching state change. | Mint = fiat subscription, or burn = completed fiat redemption. |
| Cross-chain migration | Verified bridge/message identifier or other explicit transaction-level linking evidence, plus the documented mechanism and both legs. | Similar amount and nearby timestamps alone. |
| Circulation adjustment | Dated provider rule and verified changes in the excluded addresses/balances. | An assumed treasury address or an unexplained balancing item. |
| Provider revision/timing | Preserved response versions or documented snapshot method that directly establishes the difference. | Calling every mismatch a provider error. |
| Unresolved | Missing link, data, definition or remaining residual, with the failed checks recorded. | LLM confidence, a plausible story or absence of a search hit. |

Keep accounting and economic interpretation in separate columns. A bridge event may also mint/burn: link it to the stock entries rather than adding it twice. Unmatched bridge legs remain unmatched/in flight; an issuer-mediated burn/mint pair needs explicit linking evidence before being called migration. Ledger closure does not establish the purpose of the transaction, ownership, fiat settlement, reserves, liquidity or regulatory causation.

## Collection, schema and reproducibility

Use read-only JSON-RPC calls and documented public sources. Fetch logs in bounded ranges, detect pagination/range limits, retry within the fixed budget, and maintain a coverage manifest. Deduplicate by chain ID, block hash, transaction hash and log index; inspect replaced/noncanonical blocks explicitly. A successful empty response counts as zero events only when the interval and provider completeness checks pass.

| Table | Required fields |
|---|---|
| Contracts | token, chain ID, address, deployment/validity interval, implementation/version, decimals, attribution source, verification state |
| Snapshots | contract key, timestamp, block number/hash, total supply in base units, excluded balances, provider value/version/unit, alignment status |
| Events | contract key, block/hash/time, transaction hash, log index, raw event, decoded type/amount, decoder version, receipt reference |
| Links | source and destination event IDs, mechanism, message/link ID, evidence source, matched/unmatched state; no probabilistic match promoted to verified |
| Reconciliation | case/contract key, interval, opening/closing stocks, gross mints/burns, eligible adjustments, both residuals, tolerance basis, data coverage, limitations |
| Provenance | exact endpoint/document URL, sanitized request parameters, retrieval UTC, raw-file path/hash, decoder/config hash, status and error details |

Store immutable responses under `data/raw/p3_29/`; keep raw data and any optional model traces out of git. Commit manifests, permitted processed tables and scripts according to the latest data policy. Do not write credentials into logs. Script headers must document units, interval endpoints, inputs and commands. Offline reproduction must rebuild tables and figures from the frozen files without network or model calls.

Cross-check all events contributing at least 1% of a case's gross supply-changing volume against a second independent endpoint or receipt source, plus a deterministic sample of smaller events. Also cross-check opening/closing state where available. If independent verification is unavailable, disclose the single-provider limitation. Report gross activity alongside the net change: large offsetting flows must not disappear behind a small residual.

## Evaluation and reading rules

**Primary accounting outputs:** the absolute provider-reconciliation residual in BRLA units for each comparable case, stock-identity residual, and explicit data/definition coverage. Show a supplementary relative residual `abs(R_provider) / max(abs(delta_reported_circulation), 1 BRLA)` with the denominator stated. It may exceed 100%; do not clamp it or relabel it as a fraction of economically explained activity. Cases without an identifiable definition remain in the coverage denominator and have no invented numerical residual.

H1 receives support **for a specified case** only when historical attribution, event/state coverage, snapshot alignment and circulation definition are verified, and both residuals satisfy the predeclared tolerances. Arithmetic closure with unresolved event meaning supports accounting reconciliation only. Report every failed requirement. Do not extrapolate one successful case to all networks, issuers or causes of the June premium.

**Generalization sample:** after the development case, freeze an inventory of available daily observations through 30 Oct 2026 before examining new transactions. Target six large absolute daily changes and six ordinary days outside the development window, using a deterministic selection rule recorded in the protocol. Select large changes in descending absolute size with at least seven days between selected episode centers; select ordinary days from the remaining middle 50% of absolute changes using a recorded seed. Use the available period rather than inventing history. Group linked cross-chain moves into one episode, disclose overlap, and report any reduced sample. Selection on aggregate change is explicit; this is a diagnostic sample, not an estimate of population failure prevalence. A second issuer is a later replication only after its own contract/definition audit.

**Optional H4:** undertake only if H1's pipeline and a sufficiently large unseen case inventory are ready. Compare B0 (fixed queries and deterministic reconciliation), B1 (one LLM explanation from a fixed evidence pack), and A (adaptive evidence retrieval with the same deterministic accounting engine). Use the same permitted sources, actual model/version for B1/A, and predeclared tool/token/time ceilings. Two human reviewers adjudicate the reference explanations; agreement among models is not ground truth. Require at least ten held-out episodes for a pilot, excluding all inspected development cases; fewer means demonstration only. Keep labels hidden during implementation.

Score correctly supported classifications, unresolved-state accuracy, unsupported bridge/cause claims, ledger errors and actual resource cost. A preliminary agentic benefit requires higher supported-classification coverage than both baselines, zero observed unsupported bridge/cause assertions and no accounting errors in the locked sample, with paired per-case results and costs reported. A higher ceiling is not equal cost; if actual costs differ, report the tradeoff and do not claim equal-cost superiority without a matched-budget comparison. No significance or broad reliability claim is implied by this small sample. Preserve failures and timeouts; never choose the best agent run. If the deterministic workflow is sufficient, prefer it. H4 may be explicitly waived without preventing completion of H1/Q2/Q3.

## Procedure and checkpoints

1. **S1 — Source/access feasibility.** Assign implementer/reviewer; recover the aggregate-series provenance; verify one historical Celo contract and the smoke-test capabilities. Produce one opening/closing snapshot and a coverage note. **G1:** historical state, relevant logs and a source-attributed representation are usable. Otherwise close a documented feasibility result or propose a narrower scope; do not start a large collection.
2. **S2 — Freeze the protocol.** Specify the development interval, snapshot semantics, accounting definitions, excluded addresses, tolerances, provider versions, decoder assumptions and selection rule. Mark unresolved definitions explicitly. Commit `P3-29_protocol.md` before classifying the episode. If the provider definition remains unknown, freeze a contract-stock-only scope and state that H1's circulation claim cannot yet be tested.
3. **S3 — Reconstruct one chain.** Collect bounded event ranges, reconstruct the Celo stock identity and compare historical state. Check decimals, duplicate logs, missing intervals, implementation upgrades and large transactions. Produce the first evidence ledger and residual, even if nonzero. **G2:** an independent reader can follow every adjustment to its source.
4. **S4 — Reconcile provider/multi-chain records.** Apply the documented circulation definition where identifiable. Investigate verified representations and candidate bridge links; report unmatched legs and absent chains. Produce separate chain and consolidated views only when consolidation is justified. Never infer a bridge from a visually offsetting change.
5. **S5 — Evaluate beyond June.** Freeze the held-out episode manifest and run the same accounting pipeline on all selected cases. Report failures/coverage as well as successes, timing sensitivity and independent-source checks. Decide and record whether H4 is feasible; if run, freeze its reference, methods and budgets before evaluation. A waived H4 is not an unexecuted success claim.
6. **S6 — Interpretation and project integration.** Have the economist review the difference between on-chain accounting and fiat/economic interpretation. Export reviewed evidence to P3-28 if available, and draft one candidate solution figure plus annex text. Keep exploratory and unidentifiable outcomes visible.
7. **S7 — Independent reproduction and handoff.** A teammate reproduces processed tables/figures offline, checks all large-event explanations and audits coverage/denominators. Write a new finding using the next free ID, register new sources, document raw-data recovery and update the task/board. Changes to frozen findings follow the disclosed bug-fix policy; new results remain separate.

Each step is one focused session or is split further when needed. Prioritize the first verifiable ledger before multi-chain expansion or an agent interface. G1/G2 are data and review checks, not external permission requests.

## Subtasks
- [x] S1 — Verify source provenance and historical RPC capabilities; record G1 and one snapshot pair. — done: Renzo (agent), 2026-11-07 (G1 passed for Celo; F-041)
- [x] S2 — Commit the accounting protocol, scope, definitions, tolerances and selection rule. — done: Renzo (agent), 2026-11-07 (`results/P3-29_protocol.md`, committed before any interval log was collected)
- [x] S3 — Reconstruct the Celo stock identity; audit events/coverage and pass G2. — done: Renzo (agent), 2026-11-07 (F-042; stock residual 0 on every day; **G2 needs the reviewer**: follow `results/tables/P3-29_case_audit.md` to the raw files)
- [x] S4 — Compare circulation and investigate verified multi-chain links; preserve unresolved differences. — done: Renzo (agent), 2026-11-07 (limited scope: other contracts at daily boundaries; P-0045 held; no listed chain absorbed the 23 Jun fall; F-042, F-044)
- [x] S5 — Complete the frozen additional-case evaluation; run or explicitly waive H4. — done: Renzo (agent), 2026-11-07 (12/12 cases close, 24/24 labels consistent, F-044; **H4 waived**, protocol §8)
- [ ] S6 — Review economic interpretation and prepare the integration figure/evidence export. — prepared: Renzo (agent), 2026-11-07 (figure + `results/P3-29_annex_draft_ptbr.md`); **review: Felipe**; P3-28 export not done (no reviewed record format yet)
- [ ] S7 — Independently reproduce outputs, write the finding and finish the handoff. — findings written (F-041, F-042, F-044), sources registered, raw-data recovery documented; **reproduction: a teammate (Jonathan replicated S1)**

## Success criteria
- [x] Historical contract identity, supply semantics, timestamps and data-access coverage are documented; unavailable capabilities are explicit. (F-041, T-14–T-22; other chains: identity by slot/code only)
- [x] The protocol predates event classification and distinguishes total supply, reported circulation and consolidated economic claims. (`cfccbfc` before collection; amendments dated, 7–9 post hoc)
- [x] One development ledger reports gross changes, stock residual and provider residual or an explicit reason why it is unidentifiable. (F-042, `P3-29_reconciliation.csv`)
- [x] Every adjustment/link has evidence; no inferred bridge, fiat redemption, ownership or BCB effect is presented as verified. (no adjustments needed; no link claimed)
- [x] Additional cases follow the committed selection rule; all failures and scope reductions are disclosed. (manifest `d6008bf` before collection)
- [x] Optional agent evaluation is either fully reported against its baselines or explicitly waived without a superiority claim. (waived)
- [ ] Another teammate reproduces the outputs and checks interpretation before main-deck use; negative results are acceptable.

## Outputs

Planned files. **Exist since S1:** `scripts/p3_29_reconcile.py smoke`, `data/raw/p3_29/`, `data/processed/P3-29_snapshots.csv`, `results/tables/P3-29_coverage.csv`, F-041. The rest are planned:

- `scripts/p3_29_reconcile.py` — read-only collection, decoding, deterministic reconciliation, scoring and reporting.
- `results/P3-29_protocol.md` — accounting definitions, cases, timestamps, tolerances, source versions and amendments; optional H4 appendix.
- `data/raw/p3_29/` — immutable source/RPC responses and optional model traces, with manifests/checksums.
- `data/processed/P3-29_contracts.csv`, `P3-29_snapshots.csv`, `P3-29_events.csv`, `P3-29_links.csv`, `P3-29_reconciliation.csv`.
- `results/tables/P3-29_coverage.csv`, `P3-29_case_audit.md`, and, only if H4 runs, `P3-29_agent_scores.csv`.
- `results/figures/P3-29_supply_bridge.png`, `P3-29_case_residuals.png` — accounting waterfall and additional-case/coverage result.
- New `findings/F-NNN-on-chain-reconciliation.md` using the next free ID; integration text and claim limits included.

Proposed command interface, to implement after G1: `.venv/bin/python scripts/p3_29_reconcile.py {collect,reconcile,report,reproduce} --protocol results/P3-29_protocol.md`. `reproduce` uses frozen files only. Record final working commands in the finding; this is not an existing executable.

## Integration, expansion and narrative

**Narrative:** measured digital-dollar cost → a wider infrastructure question → an aggregate signal whose meaning is ambiguous → a transparent ledger showing what the data do and do not establish. Proposed English conclusion: “Price data show the local premium; transaction-level reconciliation tests which changes in the token infrastructure are actually observable.” Replace this with the measured result after execution, including an unresolved outcome if necessary.

P3-28 and P3-29 are independent. Their interface is a reviewed record keyed by token, chain, contract and validity interval, containing block/source references, classification, verification state and limitations. The access map can display a verified representation or migration mechanism; a balanced ledger cannot mark a route as operationally available. No live cross-task dependency is needed for either study.

For the ten-slide PDF, propose at most one combined solution/evaluation slide with P3-28, plus an annex with the full reconciliation. A supply waterfall and a price chart may sit beside each other with separate units; coincidence is not a causal bridge. Deck inclusion follows independent review and the deck owner's integration. Preserve F-037's exploratory status and do not rewrite frozen results merely to strengthen the story.

**Expansion after feasibility:** other dates, verified BRLA representations and a second issuer; later, an automated discrepancy monitor with labeled technical anomalies. This broadens the project toward infrastructure transparency. It does not forecast prices, prove solvency, certify reserves, identify Brazilian residents' flows or recommend a route as cheaper/usable.

## Risks, fallback and open questions

- Historical contract/RPC access fails: deliver the reproducible feasibility audit or a narrower ledger, not simulated chain evidence.
- Circulation definition or snapshot time is unknown: distinguish a successful contract-stock reconciliation from an untestable provider-series reconciliation.
- Cross-chain legs cannot be linked: retain unmatched records; partial evidence does not establish migration.
- Aggregator history changed: preserve both versions and report sensitivity; do not silently overwrite F-037's input.
- Too little time before 8 Nov: prioritize one independently checked case; label it a case study and defer generalization/H4. If review is incomplete, omit numerical extension claims from the PDF.
- S1 must resolve who owns implementation/review, which raw files exist locally, whether historical states are retrievable, and what scope fits the checkpoint. S2 must resolve or explicitly leave unknown the provider's historical supply definition.

## Sources and reading order

Read `prompt.md`, `STATUS.md`, P3-27, F-037/P3-24 and the input script/data notes first. Source-register T-06/R-11 supplies current issuer contract leads, T-07 documents read-only JSON-RPC capabilities, and T-13 defines the ERC-20 interface. These establish technical starting points, not June contract identity, provider methodology or endpoint availability. Verify and register each new exact source used during execution.

## Handoff
- **State (01:57 Brasília, 7 Nov):** S1–S5 done and S6 prepared by Renzo's agent; status `review`, no one working. Findings:
  F-041 (feasibility), F-042 (June Celo ledger: residual 0 on every day; 732.6 mn minted / 724.9 mn burned for +7.7 mn;
  23 Jun burn of 113.6 mn; not absorbed by Polygon/Gnosis/Moonbeam; DefiLlama 26 Jun value matches no on-chain state),
  F-044 (12 frozen cases all close; 24/24 labels consistent; DefiLlama read time 00:04–00:46 UTC; P-0045 held 32/0, 6
  informative). All exploratory. H4 waived.
- **Next steps (people, not agents):**
  1. **S7 reproduction, Jonathan (he replicated S1, `e9e5bf8`) or Nattan:** restore the Flash bundle (`data/README.md`).
     Then run, live (public endpoints, no key; about 4 + 8 + 4 min): `.venv/bin/python scripts/p3_29_reconcile.py ledger`,
     then `... cases`, then `... chains`. Or ask Renzo for `data/raw/p3_29/` (89 MB) and add `P3_29_OFFLINE=1`.
     Compare with `data/processed/P3-29_reconciliation.csv`, `results/tables/P3-29_case_audit.md`, `P3-29_s5_cases.csv`,
     `P3-29_chains_audit.md`. Open 2–3 large burns on https://celo.blockscout.com/tx/<hash> in a browser (G2), and check
     F-042/F-044 wording against protocol §6. Then write `checked_by` and History in the three findings.
  2. **S6 Felipe:** read `results/P3-29_annex_draft_ptbr.md` (figure + one paragraph + three questions). Decide annex or
     repository only. The deck is not touched.
- **Open questions:** why DefiLlama's Celo value is 59,281,880 on 26 Jun and 2 Jul (needs DefiLlama's own records);
  what `MiniVM` (`0xa5e1…d340`) and the Polygon/Moonbeam implementations do (verified source on Blockscout, not read);
  whether the burns are fiat redemptions (no source; do not say so).
- **How to resume or extend:** commands above, plus `... figure` for the figure. Raw answers are under `data/raw/p3_29/`
  (2,841 files; checksums in `data/raw/SHA256SUMS`; not in git); `P3-29_events.csv` (5.8 MB) is git-ignored and rebuilt
  by `ledger`. Endpoint limits are in F-041 and T-22. A further case set needs a new frozen manifest (protocol §8 rule,
  new seed) committed before collection.

## Log
- 2026-11-07 01:57 (Brasília) — agent for Renzo: S4 done (other contracts at 15 boundaries, two providers each, P-0045 32 match / 0 miss / 6 informative; no listed chain absorbed Celo's 23 Jun fall), S5 done (manifest `d6008bf` before collection; 12/12 cases residual 0, 24/24 labels consistent, 317/317 receipts; read time 00:04–00:46 UTC), S6 prepared (figure, pt-BR annex draft for Felipe). F-044 exploratory; F-042/F-037 History notes; T-22. Status review: reproduction (S7) and Felipe's S6 review pending. Ledger code split into reusable parts (offline replay byte-identical).
- 2026-11-07 01:43 (Brasília) — agent for Renzo: tidied the merge from `e9e5bf8`: one `working:` line (Jonathan's value kept), two duplicated log lines with superseded timestamps removed, Jonathan's review line placed in date order. His text is unchanged.
- 2026-11-07 01:32 (Brasília) — agent for Renzo: Renzo: "proceed to the rest of the task". Renzo takes S4, S5 and the S6 preparation (figure + draft annex text; Felipe reviews). S7 reproduction stays with a teammate; H4 stays waived (protocol §8). Amendment 10 (S4 rules, prediction P-0045) and 11 (S5 run order) committed before any non-Celo or S5 data is read.
- 2026-11-07 01:25 (Brasília) – Jonathan (CS 3): Independent replication of S1 smoke test passed. Verified Celo opening (128,106,372.44 BRLA) and closing (135,855,038.46 BRLA) across Forno, Blockscout, and Ankr against frozen DefiLlama series (+179,326 and -36,854 diffs confirmed). Contract implementation (BRLAV1_1, ERC-20, 18 decimals) and S2 protocol frozen prior to bulk collection. Reviewed and approved.
- 2026-11-07 01:05 (Brasília) — agent for Renzo: S3 done. Ledger code and amendments 1–6 pushed before collection (`5d44c1b`); 242 chunks, no gaps; stock residual 0 base units on all 14 days; 38/38 receipts confirmed on Ankr; post hoc amendments 7–9 (2 Jul day, Blockscout metadata, selector naming). F-042 exploratory; F-037/F-041 History notes; sources T-20, T-21; events CSV git-ignored (5.8 MB). Status paused; reviewer needed for G2/S7.
- 2026-11-07 00:49 (Brasília) — agent for Renzo: S2 protocol committed before collection: development interval (69,926,442, 70,963,242], zero-base-unit stock tolerance, DefiLlama definition identified / timing not, ±1 BRLA within-day consistency rule, cross-check and S5 selection rules; H4 waived for the PDF.
- 2026-11-07 00:48 (Brasília) — agent for Renzo: Renzo said "proceed" to the S1 recommendations; read as: S2 then S3 under the recommended scope (Celo case study; S4 limited to other chains' totalSupply; S5/H4 deferred for the 8 Nov PDF) and a fresh DefiLlama version pulled. Reviewer still to be named. Renzo takes S2–S3.
- 2026-11-07 00:40 (Brasília) — agent for Renzo: S1 done, G1 passed for Celo. Script `p3_29_reconcile.py smoke` with frozen answers (112 files), offline replay identical. Celo supply 128,106,372.44 → 135,855,038.46 BRLA (19 Jun → 1 Jul 00:00 UTC; Forno = Ankr); proxy `BRLAV1_1` unchanged at both blocks; mint/burn emit `Transfer` to/from 0x0; DefiLlama = totalSupply with no exclusions, time of day unknown (+179,326 and −36,854 BRLA vs 00:00 UTC). F-041 exploratory; sources T-14–T-19. Status paused.
- 2026-11-07 00:10 (Brasília) — agent for Renzo: Renzo takes S1 (feasibility session, 90-minute target). Reviewer to be named (a teammate other than Renzo).
- 2026-11-06 — Codex for Renzo: formalized from the P3-27 discussion at Renzo's request. Documentation only; no experiment launched or team member assigned.

## Result
**S4–S5 (7 Nov 2026, agent for Renzo), F-044 and F-042, exploratory, not yet reproduced.** Q3 (generalization): the
procedure works unchanged on 12 frozen cases (6 large, 6 ordinary): stock residual 0 on 24/24 days, DefiLlama consistent
within the day on 24/24 labels. The only provider misses among 37 Celo labels are 26 Jun and 2 Jul (same value). S4:
the other listed contracts' supplies agree across two providers. A registered prediction of DefiLlama's daily read held
out of sample (32/32; 6 informative). Celo's 23 Jun fall was not offset on Polygon, Gnosis or Moonbeam. H4: waived.

**S3 (7 Nov 2026, agent for Renzo), F-042, exploratory, not yet reviewed:** the Celo stock identity holds to the base
unit on every UTC day of 19 Jun – 2 Jul 2026 (development case 19–30 Jun: +7,748,666.02 BRLA = 732,612,871.45 minted −
724,864,205.43 burned). The provider series matches on-chain supply within ±1 BRLA on 12 of 13 labels; 26 Jun is
unresolved. H1 as registered is not supported for the case (one label fails). Q2: 100% of the stock change is mint/burn
by two accounts; no circulation adjustment exists in the provider's definition; no cross-chain migration is
established; purposes are unresolved. Q3, H4: deferred.

**S1 / G1 (7 Nov 2026, agent for Renzo): passed for Celo.** Full table in
F-041; capability matrix in `results/tables/P3-29_coverage.csv`.

| G1 requirement | Result |
|---|---|
| Historical state | Yes: Forno and Ankr return the same `totalSupply`, code and EIP-1967 slots at both blocks (Blockscout and dRPC also at the opening block). 1rpc, Stakely: pruned |
| Relevant logs | Yes: Forno ≤ 5,000 blocks per call, Ankr ≤ 1,000 (10,000 refused); identical 35 logs on both in a 1,000-block test range |
| Receipts | Yes: Ankr by hash; Forno by block only (its by-hash answer is `null` for a known June transaction, a capability gap and not a failure label, T-07) |
| Source-attributed representation | Yes: Celo `0xfecb…3760`, proxy created 22 May 2024, listed by Avenia's terms (T-06), CoinGecko (D-20) and DefiLlama (T-14); implementation `BRLAV1_1`, verified source (T-19), the same at both blocks |
| Supply semantics | `_totalSupply` changes only in `_mint`/`_burn`; both emit `Transfer` from/to `0x0`; no rebase or bridge logic in the implementation |
| Provider series provenance | Flash CSV = DefiLlama raw JSON (227 rows, 0 mismatches). June definition: `totalSupply / 10 ** decimals` per contract, no exclusions (T-14, T-15). Time of day per daily value unknown, and values can be replaced (T-16) → `time_alignment_unknown` |
| Snapshot pair | 128,106,372.436 BRLA at block 69,926,442 (19 Jun 00:00 UTC); 135,855,038.456 at block 70,963,242 (1 Jul 00:00 UTC) |

Not covered by G1: Polygon, Gnosis and Moonbeam contracts; upgrades between the two snapshot blocks (S3 scans the logs).
