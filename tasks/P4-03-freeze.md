---
id: P4-03
title: Freeze results
phase: P4
status: done
owner: Team
working: -
due: 2026-11-04
depends: P4-01, P4-02
---

## Goal
Stop changing results. After this only bug fixes, each disclosed.

## Subtasks
- [x] S1 — Confirmed findings → `frozen`; exploratory findings keep their label, numbers frozen; History line in every finding — done: Renzo (agent), 4 Nov
- [x] S2 — Decision log entry; P4 gate criteria in `docs/phases.md` — done: Renzo (agent), 4 Nov
- [x] S3 — Link check of `docs/sources.md` and the event tables — done: Renzo (agent), 4 Nov
- [x] S4 — Tag `results-frozen` on the freeze commit and push — done: Renzo (agent), 4 Nov

## Success criteria
- [x] Every finding used in the deck has status frozen (27 confirmed → frozen; the 6 exploratory ones, F-012 and F-029 to F-033, keep
      their label because nobody has re-run them: the deck may use them only at the level their Claim states)
- [x] Git tag results-frozen on the commit
- [x] Decision log entry
- [x] Every link in `docs/sources.md` and the event tables opens and says what we cite (link check below; open by hand
      anything that is not 200 and is not an API endpoint or a site that blocks scripts)

## Outputs
- tag `results-frozen`

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** done 4 Nov (Renzo's decision). Findings F-001 to F-033 frozen; tag `results-frozen`. New work goes into new
  findings (F-034 P3-20, F-035 P3-24, F-036 P3-25), which the deck cites only after a teammate's re-run.
- **Next step:** none. A bug found in a frozen finding is fixed and disclosed in that finding's History.
- **Open questions:** blockers still open from before the freeze (F-015 teammate re-check after the PTAX conversion; F-029
  re-run) stay in `STATUS.md`; they are bug-fix checks, not new results.
- **How to resume:** `git show results-frozen --stat`.

## Log
- 2026-11-04 23:50, agent for Renzo: freeze at Renzo's request. 27 findings confirmed → frozen, 6 exploratory keep their
  label (numbers frozen). Link check (108 addresses, 8 in parallel, 20 s timeout, then 60 s for timeouts): 87 return 200
  (4 Planalto/Avenia pages only on the 60 s retry); 1 returns 202 (Binance announcement); 8 are API endpoints or URL
  templates (Binance, Bitstamp, Coinbase, Foxbit, Mercado Bitcoin ×2, DeFiLlama, ECB); 1 is a directory prefix, not a cited
  page (C-04 `eesp.fgv.br/evento/`, 404); 11 return 403 to scripts (Investing, Coinbase help, IMF PDF, letsmoney, Mercado
  Bitcoin ×3, SEC, The Block ×3), excluded from hand-opening by the criterion. No address failed for another reason.
- 2026-11-02, agent for Renzo: link-check criterion added (decision 2 Nov). Command: `grep -ohE 'https?://[^ )|`"<>,;]+' docs/sources.md data/processed/P1-0[46]_events_*.csv | sed 's/[.]$//' | sort -u | while read u; do echo "$(curl -s -o /dev/null -L --max-time 20 -A 'Mozilla/5.0' -w '%{http_code}' "$u") $u"; done | grep -v '^200'`

## Result
Results frozen on 4 Nov 2026 (tag `results-frozen`): 27 findings `frozen`, 6 `exploratory` with frozen numbers. No cited
address is broken; 11 sites refuse scripts and were not reopened by hand.
