---
id: P4-03
title: Freeze results
phase: P4
status: todo
owner: Team
working: -
due: 2026-11-04
depends: P4-01, P4-02
---

## Goal
Stop changing results. After this only bug fixes, each disclosed.

## Subtasks
_Write the subtasks (S1, S2, ...) when the phase starts; see `docs/phases.md` and the plan section in the goal._

## Success criteria
- [ ] Every finding used in the deck has status frozen
- [ ] Git tag results-frozen on the commit
- [ ] Decision log entry
- [ ] Every link in `docs/sources.md` and the event tables opens and says what we cite (link check below; open by hand
      anything that is not 200 and is not an API endpoint or a site that blocks scripts)

## Outputs
- tag `results-frozen`

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** not started
- **Next step:** S1
- **Open questions:** none
- **How to resume:** -

## Log
- 2026-11-02, agent for Renzo: link-check criterion added (decision 2 Nov). Command: `grep -ohE 'https?://[^ )|`"<>,;]+' docs/sources.md data/processed/P1-0[46]_events_*.csv | sed 's/[.]$//' | sort -u | while read u; do echo "$(curl -s -o /dev/null -L --max-time 20 -A 'Mozilla/5.0' -w '%{http_code}' "$u") $u"; done | grep -v '^200'`

## Result
