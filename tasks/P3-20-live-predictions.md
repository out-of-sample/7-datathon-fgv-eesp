---
id: P3-20
title: Predictions registered before the data - Res. 574 reporting (3 Nov 2026) and Res. 589 ban on unauthorised counterparties (6 Nov 2026)
phase: P3
status: doing
owner: CS 1
working: Renzo (agent)
due: 2026-11-16
depends: P1-02, P1-03, P3-03, P4-04
---

<!-- Specification reviewed and approved by Renzo on 3 Nov 2026 ("Proceed with P3-20"); this commit + push is the registration. -->

## Goal
Test the project's idea (the premium is set by the cheapest channel still open; proposal §7.3 in
`docs/improvements-proposal.md`) on two dated rules whose outcome nobody has seen yet. We write what the premium should
do, push it to GitHub before the first trading window under each rule, and check it with data that arrives before the
submission (8 Nov) and the oral final (16 Nov). This answers "you saw the jump first, then tested it" with the reverse
order: registered first, checked later. The result is reported whatever it shows.

## Specification (fixed before any data after 30 Oct 2026 is downloaded or viewed)
Written 3 Nov 2026, about 02:45 Brasília, by the agent for Renzo. Last data seen: the frozen raw data up to 30 Oct 2026
(P1-01). Nothing after 30 Oct has been downloaded or looked at.

**Events.**

| ID | Rule | In force | What it does | Source |
|---|---|---|---|---|
| E1 | Res. BCB 574 (and IN BCB 756) | operations from 3 Nov 2026 | FX-authorised institutions report their virtual-asset operations "realizadas a partir de 3 de novembro de 2026". A reporting rule | E-11, E-15 |
| E2 | Res. BCB 589, art. 91 | 6 Nov 2026 | "É vedado, a partir de 6 de novembro de 2026, às instituições financeiras [...] realizar ou viabilizar operações no mercado de ativos virtuais que tenham como contrapartes instituições ou entidades que prestem serviços de ativos virtuais e não estejam autorizadas a funcionar no país". The exception for firms "em processo de autorização" was dropped. Published 23 Sep 2026, six weeks ahead | E-14 |

**Outcome.** The P1-02 premium (`premium_bps`): Binance USDT/BRL in the PTAX window (10–13h Brasília) over PTAX,
USDT/USD-adjusted, in bps. Same code (`scripts/p1_02_premium.py`) on extended raw data; no change of method.
Checks: Foxbit and Mercado Bitcoin, measured as in P2-05 (`scripts/p2_05_checks.py`, `scripts/p1_03_second_venue.py`),
and the cross-venue gaps (Foxbit − Binance, Mercado Bitcoin − Binance).

**Event day.** t0 = the last PTAX day before the first PTAX window in which the rule is in force (the same reading as the
23 Jun notice, where t0 = 23 Jun and 24 Jun was the first treated window). E1: t0 = the last PTAX day before 3 Nov
(expected 30 Oct, because 2 Nov is the Finados holiday; the script takes it from the BCB PTAX series). E2: t0 = the last
PTAX day before 6 Nov (expected 5 Nov).

**Statistics** (the functions in `scripts/p4_04_inference.py`, unchanged):

| Name | Definition | Role |
|---|---|---|
| S2 | mean premium over [t0+1, t0+2] minus mean over [t0−20, t0−1] (F-029, statistic B) | **Primary**, both events |
| S1 | premium(t0+1) − premium(t0) | Early reading only. For E1 it is not used for the verdict: the premium on 30 Oct was −30.3 bps, far below its usual level, so a plain rebound on 3 Nov would show as a rise. S2's pre-window excludes t0 |
| S20 | mean over [t0+1, t0+20] minus mean over [t0−20, t0−1] (F-016, F-026) | Secondary. The E1 and E2 windows overlap, so S20 cannot separate them; reported jointly |

**Reference distribution.** The same statistic at every clean date (the P2-03 / P4-04 rule, event list
`data/processed/P1-04_events_brazil.csv` as it stands), using only data up to 30 Oct 2026. It is computed and committed
(S2 below) before any November data is downloaded. Two-sided p = (k + 1) / (n + 1), k = clean dates with
|statistic| ≥ |observed|. The non-overlapping p (P4-04 method) is reported next to it.

**Decision rule.** A "detectable move" means S2 two-sided p < 0.05 on Binance. A move on Binance alone, with neither other
venue at p < 0.05, is reported as "Binance only, probably venue-specific".

A result inside the reference band is **not** evidence of zero effect. It only rules out a move larger than the band,
whose half-width S2 computes and every null states next to it. With two days of data the band is wide, so a null can say
"no move of the June kind", never "no effect". The two events and the three venues are reported one by one; no "at least
one of them moved" claim.

**Predictions.**
- **E1 (Res. 574): no detectable move.** S2 stays inside the reference band (two-sided p ≥ 0.05), read as "no move larger
  than the band", not as "no effect". Reason: a reporting rule leaves every supply channel open
  (prediction 3, proposal §7.3); the seven published rules stayed inside the ordinary range (F-026). Proved wrong if
  Binance S2 p < 0.05 in either direction.
- **E2 (Res. 589, art. 91): the branch is chosen from the legal text before 6 Nov 10:00 Brasília (S5), not from data.**
  - **A.** Firms whose applications are pending may keep operating, or the ban does not cover exchanges' bank accounts and
    Pix: it bites only on providers that did not apply. The venues in our data say they applied (news, to be opened in S5).
    Predict **no detectable move** (same rule as E1).
  - **B.** The ban cuts bank access for firms not yet authorised, including venues in our data. A channel closes for buyers
    on those venues. Predict **a rise** on the affected venues (S2 one-sided p < 0.05) and a cross-venue gap opening between
    affected and unaffected venues. If an affected venue's data stops, that is reported as a result, not a gap to fill.
  - **C.** The text does not settle it: two-sided rule, no direction; p reported either way.
- **What E2 can add.** E2 was published six weeks ahead. Under branch B, no move would fit "notice lets the market
  reorganise" (the rule's form matters); a rise would fit "closing a channel moves the price even with notice" (content
  matters). That is the first evidence on the form-vs-content limit, from one event, worded as "compatível com".

**Overlapping developments known at registration.** Dates come from news and calendars; S2 opens and registers them.
None of them is a reason to change the rules above.

| Date | Development | Window it touches |
|---|---|---|
| Fri 30 Oct | Reported deadline for providers' authorisation requests (news, not opened); premium −30.3 bps that day | E1 t0, which S2's pre-mean excludes |
| Mon 2 Nov | Finados holiday, no PTAX | – |
| Tue 3 Nov | US midterm elections; results arrive after the Brazilian PTAX window | E1 S2 (the 4 Nov window) |
| 3–4 Nov | Copom meeting; decision expected on the evening of 4 Nov, after the PTAX window | 5 Nov is E2's t0, which both E2 means exclude |
| Fri 6 Nov | US October jobs report, 8:30 ET = 10:30 Brasília, inside the PTAX window | E2 S1 and S2 |

The premium removes the official dollar measured in the same window. These events should therefore matter only through
timing inside the window or through demand for crypto. That is an assumption, not a result, and the finding lists these
events next to the verdict.

**Prospective, not retrospective.** E1 and E2 are predictions in the strict sense: the outcome did not exist when this was
written. Any cross-country work (P3-22) is a retrospective specification and is never called a prediction.

**Not allowed after registration:** changing windows, venues, the statistic, the clean-date rule or the event list; adding
events; dropping a venue whose result is unwelcome.

**Data (download only after Renzo approves this plan).** Binance USDTBRL and USDCUSDT daily 1h files from 31 Oct 2026; PTAX
from the BCB Olinda API; Coinbase USDT/USD; Foxbit and Mercado Bitcoin hourly. New pulls go to **new file names** next to
the 30 Oct freeze (no overwrite of frozen files), with checksums added to `data/raw/SHA256SUMS`.

**Code isolation.** `p4_04_inference.py` and `p1_02_premium.py` write core outputs when run, so `p3_20_live.py` imports
neither. It copies the clean-date rule, `stat()` and the premium formula, and writes its own extended series
`data/processed/P3-20_premium_daily.csv`. It asserts that every row up to 30 Oct equals `P1-02_premium_daily.csv`. Core
files and findings F-001 to F-032 stay unchanged.

**Timeline.**

| When (Brasília) | What |
|---|---|
| Before 10:00, Tue 3 Nov | Specification reviewed, committed and pushed (S1). If missed: E1 is labelled "registered after the first treated window opened, before any data was viewed" |
| Tue 3 Nov, before any download | Reference distributions committed (S2) |
| Wed 4 Nov, after 13:30 | E1 readout: S2 = 3–4 Nov, both before E2 (S4) |
| By 23:59, Thu 5 Nov | E2 branch committed and pushed (S5) |
| Fri 6 Nov, after 13:30 | E2 early reading, S1 only, labelled as such: the only E2 number that can be in the PDF (S6) |
| Mon 9 Nov | E2 S2 = 6 and 9 Nov: the E2 verdict, shown at the oral final (16 Nov) if we are finalists |
| Early Dec | S20 for both, jointly (S7) |

### S5 legal reading (3 Nov 2026) and the E2 branch rule (fixed now, applied on 5 Nov)
Texts opened 3 Nov 2026 by the agent for Renzo through the BCB normativos API (Res. BCB 520 consolidated, Res. BCB 589)
and the Voto PDF (both URLs in E-14):
- Res. 520, art. 88 §6: providers that applied on time "podem manter a prestação dos serviços de ativos virtuais até a
  conclusão do seu processo de autorização"; §7: those that did not apply "devem cessar a prestação de serviços de ativos
  virtuais em até trinta dias após o fim do prazo". The deadline is 270 days from 2 Feb 2026, i.e. 30 Oct 2026.
- Art. 91 as amended by Res. 589 (in force 1 Oct 2026): from 6 Nov, banks and payment institutions may not "realizar ou
  viabilizar operações no mercado de ativos virtuais" with providers that "não estejam autorizadas a funcionar no país";
  the words "ou em processo de autorização" are gone. Its single paragraph, kept by Res. 589, extends the ban to "abertura e
  manutenção de contas de pagamento e realização de transações de pagamento" and "operações de câmbio". So **bank
  accounts and Pix are covered**.
- Voto 108/2026-BCB, §7: the delay to 6 Nov "permitirá que esta Autarquia sistematize e publique a lista oficial de
  instituições em transição, incluindo as sociedades prestadoras de serviços de ativos virtuais [...] que [...]
  protocolaram pedido de autorização"; §8: "fica expressamente vedado às instituições reguladas operar com contrapartes
  que não estejam devidamente autorizadas, salvo nas exceções previstas na norma".
- Reading: the ban is aimed at providers that are not on the BCB's official list, while providers in transition may keep
  operating (§6). The text alone does not say whether a provider in transition counts as "devidamente autorizada" for
  art. 91. A GSGA law-firm note (5 Oct 2026) restates the rule without settling this. No official list was found on 3 Nov.

**Branch rule** (applied to each venue on 5 Nov from sources, never from prices; committed and pushed by 23:59):
- **A** if the BCB's official list (or a BCB statement) shows the venue as authorised or in transition and allowed to keep
  bank and Pix access → no detectable move for that venue (S2 inside the band).
- **B** if the venue is absent from a published list, or a primary source (BCB, the venue itself, or a bank) says its
  bank, Pix or FX access ends on 6 Nov → rise on that venue (S2 one-sided p < 0.05) and its gap to listed venues widens.
- **C** if no list is published by 5 Nov 23:59 and there is no venue-specific statement → two-sided rule, no direction.
- In every branch, the ban also cuts providers that never applied (offshore platforms serving Brazilians). That could
  shift buyers and sellers onto the venues we measure, in a direction we cannot sign; it is reported as a limit.

## Subtasks
- [x] S1 — Renzo reviews this Specification; agent commits and pushes it; hash recorded here. Deadline 10:00 Brasília, 3 Nov — done: Renzo, 3 Nov (`9a522e9`, pushed 05:55 UTC = 02:55 Brasília)
- [x] S2 — `scripts/p3_20_live.py` part 1: reference distributions of S1, S2 and S20 at all clean dates from data up to
  30 Oct (Binance, Foxbit, Mercado Bitcoin, the two cross-venue gaps) → `results/tables/P3-20_reference.csv`; commit before
  any download — done: Renzo, 3 Nov (commit below; missing-data rule fixed here, before any November data: a pre-window
  needs >= 15 of 20 days; S1 and S2 need every post day; S20 needs >= 15 of 20)
- [x] S3 — Download November data into new raw files with checksums; point `p1_02_premium.py` and the venue checks at them
  without changing the method; the 30 Oct series must reproduce exactly — done: Renzo (agent), 5 Nov (Binance, PTAX,
  Foxbit; Mercado Bitcoin's API returned a Cloudflare redirect, retry pending; Coinbase not needed by any statistic)
- [x] S4 — E1 readout (S1 and S2, all venues, monitor alarm in [t0+1, t0+5] via `scripts/p3_03_monitor.py`) →
  `results/tables/P3-20_readout.csv`; finding written either way — done: Renzo (agent), 5 Nov (F-035)
- [ ] S5 — E2 branch (rule fixed 3 Nov, see above; branch applied 5 Nov) — doing: Renzo. E2 branch: read Res. BCB 520's transition rules and Res. 589 in full; open any BCB list of authorised or pending
  providers and the exchanges' own statements; write the branch (A, B or C) with quotes; commit and push before 6 Nov 10:00
- [ ] S6 — E2 early reading (S1, 6 Nov) for the PDF; E2 S2 on 9 Nov; update the finding
- [ ] S7 — S20 for both events (early Dec); independent re-run by a teammate who did not write the script
- [ ] S8 — pt-BR box for slide 10 with the registered prediction and whatever came out; Felipe places it

## Success criteria
- [x] Specification pushed before 10:00 Brasília on 3 Nov (hash and push time recorded); otherwise E1 relabelled as above
- [x] Reference distributions committed before any November data was downloaded (commit order in git: `ce283dc`, then
      readout code `30de591`, then the first download on 5 Nov)
- [ ] E2 branch pushed before 10:00 Brasília on 6 Nov, with quotes from the legal text
- [ ] E1 and E2 results in a finding with exact commands, reported whatever they show; nothing in the Specification
  changed after registration
- [ ] A teammate who did not write `p3_20_live.py` re-runs it and gets the same numbers

## Outputs
- `scripts/p3_20_live.py` (header: purpose, inputs, outputs, how to run)
- `results/tables/P3-20_reference.csv`, `results/tables/P3-20_readout.csv`
- New raw files under `data/raw/` (November pulls), checksums in `data/raw/SHA256SUMS`
- Finding F-035 (reserved 4 Nov; F-034 is the BRLA check, P3-25 holds F-036)

## Handoff
- **State:** E1 read out (F-035, exploratory): Binance S2 +2.1 bps, p = 0.90 (non-overlapping 0.92); Foxbit −1.9, p = 0.92;
  prediction held. Mercado Bitcoin's November pull failed (Cloudflare 302 to our script), so MB and the MB gap are
  "missing". E2 pending.
- **Next step:** S5, by 23:59 Thu 5 Nov: look for the BCB's official list of authorised / in-transition providers and the
  three venues' own statements; apply the registered branch rule (A/B/C per venue, from sources only, never prices);
  commit and push. Then S6 on Fri 6 Nov after 13:30 Brasília: `python scripts/p3_20_live.py download` and `readout`
  (E2 S1 = early reading, the only E2 number for the PDF).
- **Open questions:** (1) Mercado Bitcoin: retried 5 Nov 02:30 Brasília, still HTTP 302 with no Location on every
  endpoint, also with curl's default agent: Cloudflare is challenging this machine's connection, which only a real
  browser passes (the 31 Oct frozen pull worked). **Fix (Renzo, ~2 min, after 14:00 Brasília so the day's PTAX window
  is complete):** open
  `https://api.mercadobitcoin.net/api/v4/candles?symbol=USDT-BRL&resolution=1h&from=1793404800&to=1794009600`
  (31 Oct – 7 Nov 2026 UTC) in a browser, save the JSON as `data/raw/live/mercadobitcoin/USDT-BRL-1h_browser_<YYYYMMDD>.json`,
  then convert it to the readout's format:
  `.venv/bin/python -c "import json,sys,pandas as pd; f=sys.argv[1]; r=json.load(open(f)); pd.DataFrame({k: r[k] for k in 'tohlcv'}).to_csv(f.replace('_browser_', '_to_browser_').replace('.json', '.csv'), index=False)" data/raw/live/mercadobitcoin/USDT-BRL-1h_browser_<YYYYMMDD>.json`
  and append both files to `data/raw/SHA256SUMS`. Then `python scripts/p3_20_live.py readout`. If the browser also gets a
  challenge page, try another network (phone hotspot) and run `python scripts/p3_20_live.py download` as usual. (2) A teammate who did not write `p3_20_live.py` re-runs E1 (criterion 5)
  before it goes on Slide 10 (P5-08 S2).
- **How to resume:** `python scripts/p3_20_live.py readout` reproduces F-035 from `data/raw/live/` (checksums in
  `data/raw/SHA256SUMS`; `grep data/raw/live data/raw/SHA256SUMS | sha256sum -c`). Each `download` writes new files named
  `_to_<UTC hour>`; a later pull wins for the same hour.

## Log
- 2026-11-05 01:10 (Brasília), agent for Renzo: S3 + S4. Downloaded Binance USDTBRL/USDCUSDT 31 Oct – 4 Nov (Binance
  checksums OK), PTAX to 4 Nov (October rows equal the freeze), Foxbit to 5 Nov 01h UTC; Mercado Bitcoin returned HTTP 302
  (Cloudflare) and was not worked around. Fixed one readout bug before the first run (a series with no November price
  scored k = 0). P1-02 reproduced exactly on 1,520 days. E1: Binance S2 +2.1 bps (p = 0.897, non-overlapping 0.920),
  Foxbit −1.9 (0.923), Foxbit gap −4.0 (0.607); S1 +47.9 (p = 0.12, not the verdict: 30 Oct was a Binance-only dip, gap
  +49 bps). Prediction "no detectable move" held (F-035).
- 2026-11-05 00:35, agent for Renzo: S3/S4 code committed before any November data was downloaded: `download` writes to
  `data/raw/live/` (separate folder, so the core scripts' globs never pick up November files); `readout` rebuilds the
  P1-02 premium from raw (formula copied), asserts equality on all 1,520 days to 30 Oct (passes on frozen data), and the
  rebuilt venue series reproduce every stored reference value within 0.001 bps. Monitor: the CUSUM's 30 Oct down-alarm
  (P3-03 false alarm) starts its 10-day pause, so no alarm is possible in [t0+1, t0+5] for E1 by construction. Coinbase
  USDT/USD not pulled: no registered statistic uses it.
- 2026-11-03, agent for Renzo: S5 part 1. Res. 520 art. 88 §6–7, art. 91 (Res. 589) and its single paragraph (accounts, Pix,
  FX covered), and Voto 108 §7–8 read. Status of providers in transition is ambiguous and the BCB list is not out, so a
  branch rule (A/B/C by venue, from sources only) is registered now; the branch is applied on 5 Nov.
- 2026-11-03, agent for Renzo: S2 done. Reference from frozen data only (1,073 clean dates, 20 Nov 2020 – 30 Mar 2026; reproduces
  F-029: largest |S2| 202.8, |S20| 65.7). Binance bands: S1 −74.8/+75.0, **S2 −75.5/+59.8**, S20 −35.4/+37.7 bps. So a
  null on S2 rules out only moves beyond about 75 bps; the bands reflect 2020–26 volatility, wider than 2026's. Rule kept
  as registered. Foxbit is far noisier (S2 −166/+129), Mercado Bitcoin tighter (S2 −43/+39). No November data downloaded.
- 2026-11-03, agent for Renzo: Renzo approved the Specification and the November download; registration commit and push.
- 2026-11-03 03:10 (Brasília), agent for Renzo: second agent's review of the cross-country plan applied here too: overlap
  screen (Copom 3–4 Nov, US midterms, US jobs report 6 Nov), null results worded as a bound and not as zero, code
  isolation, no multiple-venue claims, prospective vs retrospective label. Still a draft for Renzo's review.
- 2026-11-03 02:45 (Brasília), agent for Renzo: created as a plan draft at Renzo's request ("let 3 be reviewed"); not committed.

## Result
<!-- fill when done -->
