---
id: P3-29
title: Reconcile reported BRLA supply changes with on-chain evidence
phase: P3
status: doing
owner: Team
working: Renzo (agent)
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
- [ ] S2 — Commit the accounting protocol, scope, definitions, tolerances and selection rule. — doing: Renzo (agent)
- [ ] S3 — Reconstruct the Celo stock identity; audit events/coverage and pass G2. — doing: Renzo (agent)
- [ ] S4 — Compare circulation and investigate verified multi-chain links; preserve unresolved differences.
- [ ] S5 — Complete the frozen additional-case evaluation; run or explicitly waive H4.
- [ ] S6 — Review economic interpretation and prepare the integration figure/evidence export.
- [ ] S7 — Independently reproduce outputs, write the finding and finish the handoff.

## Success criteria
- [ ] Historical contract identity, supply semantics, timestamps and data-access coverage are documented; unavailable capabilities are explicit.
- [ ] The protocol predates event classification and distinguishes total supply, reported circulation and consolidated economic claims.
- [ ] One development ledger reports gross changes, stock residual and provider residual or an explicit reason why it is unidentifiable.
- [ ] Every adjustment/link has evidence; no inferred bridge, fiat redemption, ownership or BCB effect is presented as verified.
- [ ] Additional cases follow the committed selection rule; all failures and scope reductions are disclosed.
- [ ] Optional agent evaluation is either fully reported against its baselines or explicitly waived without a superiority claim.
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
- **State (7 Nov 00:40 Brasília):** S1 done by Renzo's agent; **G1 passed for Celo** (record in Result; F-041
  exploratory). Nothing has been collected beyond the smoke test and no event has been classified. Status `paused`, no
  one working. S2 is the next step and must be committed before any S3 collection.
- **Next step — S2, freeze `results/P3-29_protocol.md` before collecting the interval.** Decisions the protocol must fix
  (draft them, show the team member, commit, then S3):
  1. Development interval: (b0, b1] = blocks 69,926,442 → 70,963,242 (19 Jun 00:00 → 1 Jul 00:00 UTC), or other
     boundaries chosen now. The rise on 19–23 Jun and the fall on 24–26 Jun both fall inside it, as the spec asks.
  2. Stock identity: ΔS = Σ `Transfer` from `0x0` − Σ `Transfer` to `0x0` in (b0, b1]. Expected residual **0 base units**
     (from the verified `BRLAV1_1` source: `_totalSupply` changes only in `_mint`/`_burn`, both emit `Transfer`).
     `verified_other_adjustments` = none. Any `Upgraded`/`AdminChanged`/`Initialized` log in the interval stops the
     identity there and is reported.
  3. Collection: all logs of the contract (no topic filter) in 5,000-block chunks on Forno (208 calls); count check per
     chunk; cross-check every mint/burn ≥ 1% of gross supply-changing volume, plus a seeded sample of smaller ones,
     against Ankr (1,000-block calls) and a receipt (Ankr by hash or Forno by block).
  4. Provider comparison: the definition is **identified** (June code: totalSupply / 10^18, no exclusions, T-14/T-15),
     so `eligible_excluded_balances` = 0 by DefiLlama's rule. Timing is **not** (T-16): fix in advance how to report it.
     Suggested: R_provider at the 00:00 UTC label, raw, with tolerance = 1 BRLA rounding only. Then, as description and
     not alignment, whether DefiLlama's value equals the on-chain supply at any block of its UTC day (± 1 BRLA). Never
     pick the matching hour and call it verified.
  5. Selection rule and seed for S5's generalization sample (spec text), or an explicit deferral given the deadline.
- **Open questions (need the team):** (a) reviewer for S3/S7: a teammate other than Renzo (Nattan or Jonathan;
  Felipe for S6 interpretation); (b) scope for the 8 Nov PDF: recommendation = Celo case study (S2–S3) plus an annex
  line at most, with S4 limited to other chains' `totalSupply` and S5/H4 deferred; (c) whether to pull a fresh
  DefiLlama response as a second version (T-16: daily values can be replaced).
- **How to resume:** restore the Flash bundle (`data/README.md`), then
  `P3_29_OFFLINE=1 .venv/bin/python scripts/p3_29_reconcile.py smoke` rebuilds S1's tables from `data/raw/p3_29/`
  (112 files; `grep p3_29 data/raw/SHA256SUMS | sha256sum -c`). Raw responses are not in git; on another clone the live
  run (`... smoke` without the variable) re-downloads them (~90 s). Endpoint limits: Forno ≤ 5,000 blocks per
  `eth_getLogs`, receipts only via `eth_getBlockReceipts`; Ankr ≤ 1,000 blocks; Blockscout eth-rpc rate-limits (429).

## Log
- 2026-11-07 00:50 (Brasília) — agent for Renzo: Renzo said "proceed" to the S1 recommendations; read as: S2 then S3 under the recommended scope (Celo case study; S4 limited to other chains' totalSupply; S5/H4 deferred for the 8 Nov PDF) and a fresh DefiLlama version pulled. Reviewer still to be named. Renzo takes S2–S3.
- 2026-11-07 00:40 (Brasília) — agent for Renzo: S1 done, G1 passed for Celo. Script `p3_29_reconcile.py smoke` with frozen answers (112 files), offline replay identical. Celo supply 128,106,372.44 → 135,855,038.46 BRLA (19 Jun → 1 Jul 00:00 UTC; Forno = Ankr); proxy `BRLAV1_1` unchanged at both blocks; mint/burn emit `Transfer` to/from 0x0; DefiLlama = totalSupply with no exclusions, time of day unknown (+179,326 and −36,854 BRLA vs 00:00 UTC). F-041 exploratory; sources T-14–T-19. Status paused.
- 2026-11-07 00:15 (Brasília) — agent for Renzo: Renzo takes S1 (feasibility session, 90-minute target). Reviewer to be named (a teammate other than Renzo).
- 2026-11-06 — Codex for Renzo: formalized from the P3-27 discussion at Renzo's request. Documentation only; no experiment launched or team member assigned.

## Result
**S1 / G1 (7 Nov 2026, agent for Renzo): passed for Celo.** Accounting reconciliation (S3 onward) not run. Full table in
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
