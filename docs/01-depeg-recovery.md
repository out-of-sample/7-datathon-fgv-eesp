# Project 1 — What brings a stablecoin back to $1?

**Status:** **chapter of project 2** (2–3 slides: "the same mechanism in dollars"), changed on 30 Oct after the
probe made project 2 the primary. Owner: CS 3. The full plan below stays on record. It becomes primary again
only if project 2 fails its go/no-go on Sun 1 Nov. **Deck title if primary (pt-BR draft):**
"O que traz uma stablecoin de volta a US$ 1? Resgate, lastro e os limites da arbitragem"

**Chapter scope (what CS 3 builds):**
1. The SVB weekend: USDC vs USD reference, Fri 10 – Tue 14 Mar 2023, with bank-closed hours shaded. The probe
   already shows USDC/USDT at 0.9128 on Sat 11 Mar 2023, 15:00 UTC.
2. Automatic detector over the stablecoin pairs (§6.1 definition). If it finds ≥ 12 independent events:
   Kaplan–Meier curves by redemption open/closed at start, with the event count on the slide. If not:
   a case table only, no curves.
3. One sentence tying it to project 2: on both sides of the dollar, the price leaves parity when the door
   (redemption, or the FX channel) closes.

Not in the chapter: the Cox model, double coding of all variables, leave-one-issuer-out.

## 1. Question in one line

When a stablecoin loses its peg, does it recover faster because of **what backs it**, or because holders
**can redeem it for $1 at that moment**?

## 2. Plain-English example

In March 2023 Circle had $3.3B of USDC reserves stuck at Silicon Valley Bank. USDC fell to about $0.88 on
Saturday 11 March, while banks were closed and nobody could redeem. It recovered on Monday 13 March, after the
US authorities guaranteed SVB deposits on Sunday evening. Its reserves were never lost; the redemption channel was
shut for the weekend.

Compare UST (May 2022), which had no external reserves and never recovered, and DAI, which followed USDC down in
March 2023 because USDC was a large part of its backing. If events where **redemption was closed** systematically
last longer than events with **weaker backing**, regulators should care at least as much about guaranteed,
always-open redemption as about reserve composition.

## 3. Why it can win

- **Relevance:** stablecoins are the centre of the "moedas digitais" theme. Brazil's central bank and other
  regulators are writing stablecoin rules now. Redemption rights versus reserve requirements is a live
  policy question.
- **Creativity:** a hand-built cross-issuer event dataset with redemption-channel coding. Most student work
  stops at "detect the depeg".
- **Maturity versus 2025:** last year depeg risk was one of 38 features. This year it is the question, studied
  with survival analysis, independent events and explicit identification.
- **Bridge sentence for the deck:** "Em 2025, o risco de depeg era uma variável entre 38. Em 2026, é a pergunta."

## 4. Hypotheses

- **H1 (redemption channel):** holding backing type and shock size fixed, depegs that start while primary
  redemption is unavailable (weekend, bank holiday, issuer pause) last longer than depegs that start while it
  is available.
- **H2 (backing):** holding redemption status fixed, fiat-reserve coins recover faster than crypto-collateralised
  coins, which recover faster than algorithmic or synthetic ones.
- **H0:** neither variable explains time to recovery beyond the initial deviation size.

Any of these outcomes is a reportable finding. Falsification of H1: hazard ratios for "redemption open" near 1
with tight confidence intervals.

## 5. Data

| Need | Source | Status |
|---|---|---|
| Minute prices of stablecoins against USDT | Binance public archive, [data.binance.vision](https://data.binance.vision) (spot klines 1m: `USDCUSDT`, `FDUSDUSDT`, `TUSDUSDT`, `DAIUSDT`, `BUSDUSDT`, `USTUSDT`, …) | Archive documented; per-pair coverage `[verify]` |
| A USD reference (USDC/USDT is a *relative* price) | Kraken downloadable OHLCVT (USDT/USD, USDC/USD, DAI/USD); cross-check with Curve/Uniswap on Dune | `[verify]` coverage |
| On-chain prices during events | Dune: `dex.trades` or Curve 3pool swaps (2025 repo has a Curve 3pool USDC series) | Partly in hand |
| Event metadata | Issuer announcements, status pages, news, governance posts | Hand-coded |
| Redemption availability | US bank and Fed holiday calendars, weekend flags, issuer redemption terms and pauses | Hand-coded |
| Backing type | Issuer docs and attestations | Hand-coded |
| Supply response (optional) | Token supply (mint/burn) from Dune or issuer transparency pages | Optional |

**Numeraire warning.** On Binance every stablecoin is quoted in USDT. A USDC/USDT drop can be a USDT rise.
Define each deviation against a USD reference, or show that the result holds with two different quote assets.

### Candidate events (all `[verify]` before use)

USDC and DAI (Mar 2023, SVB); UST (May 2022, terminal); USDT dips (May 2022; Curve 3pool imbalance Jun 2023);
FDUSD (Apr 2025, custodian allegations); USDe (Oct 2025 crash, venue-specific); TUSD (2023–24 episodes);
USDD (repeated); BUSD (Feb 2023 wind-down, possibly not a depeg); plus every automatically detected deviation
that meets the definition in §6.1. Target: **at least 20 independent events.**

## 6. Method

1. **Event definition (freeze on day 2).** Start: the first minute when |price − 1| > 0.5% and the deviation
   lasts at least 30 minutes. End (recovery): |price − 1| < 0.1% sustained for 6 hours. Unrecovered events are
   censored at the last observation or at delisting. Merge episodes that occur less than 24 hours apart.
   Robustness: thresholds of 0.3% and 1%, recovery bands of 0.05% and 0.25%.
2. **Automatic detection, then manual review.** Scan all pairs for candidate events. Reject bad ticks
   (single-minute spikes on one venue only) and log every rejection with its reason.
3. **Event coding.** Two people code each event independently and compare. Variables:
   - `redemption_open_at_start` (yes / no / partial)
   - `redemption_channel` (issuer-bank with business hours / on-chain 24/7, e.g. a PSM / none)
   - `backing_type` (fiat reserves / crypto-collateral / algorithmic / delta-neutral synthetic)
   - `trigger` (reserve or custodian news / market-wide shock / venue-specific / contagion)
   - `max_deviation`, `start_ts`, `end_ts`, `censored`
   - market controls at start: BTC 24h return, stablecoin market volume
4. **Descriptive layer.** Table of all events; time-to-recovery and depth distributions by group.
5. **Survival analysis.** Kaplan–Meier curves of "probability still depegged after *t* hours" by redemption
   status and by backing type, with log-rank tests. Cox proportional-hazards model with redemption status,
   backing type, initial deviation and market controls. Check the proportional-hazards assumption and stratify
   if it fails. Python `lifelines` or R `survival`.
6. **Baselines.** (a) Initial deviation alone; (b) pooled median recovery time. The main model must add
   something beyond (a).
7. **Robustness.** Alternative thresholds; drop UST (the terminal outlier); drop each issuer in turn
   (leave-one-issuer-out); weekend placebo (assign fake "closed" status shifted by one day).

## 7. Headline chart

Two Kaplan–Meier curves (redemption **open** vs **closed** at start) with confidence bands. X-axis: hours since
the depeg started. Y-axis: share of events still off the peg. A second panel splits by backing type.

## 8. Deck storyline (≈12 slides)

1. Title. 2. Question + why regulators care. 3. Lições de 2025. 4. How a stablecoin holds its peg (the
arbitrage loop, one diagram). 5. Hypotheses H1/H2. 6. Data and event definition (counts, exclusions).
7. Event map (timeline of all events). 8. Headline Kaplan–Meier chart. 9. Cox model table (hazard ratios,
plain-language reading). 10. Robustness. 11. Implications for Brazil's stablecoin rules + limitations.
12. Optional Brazil chapter (project 2) or conclusion. Annex: event table, coding rules, sources.

## 9. Day-1 test (applies only if this becomes primary again)

- Download USDCUSDT 1m for March 2023 and reproduce the SVB depeg curve, with the USD-reference issue handled.
- Run the automatic detector on 3–4 pairs over 2020–2026 and count candidate events.
- **Go** if there are ≥ 20 plausible independent events. **Narrow** to a comparative case study of 8–12
  events if there are 12–19. **Switch** to the fallback (project 3) if fewer than 12, or if minute data for
  the key events is unavailable.

## 10. Schedule

As a chapter: detector Sat 31 Oct; SVB figure and event count Sun 1 Nov; chapter v1 Mon 2 Nov; frozen with
everything else on Wed 4 Nov. The table below is the schedule if this project becomes primary again.

| Date | Work |
|---|---|
| Fri 30 Oct | Day-1 test; draft coding rules (economist) |
| Sat 31 Oct | Freeze event definition; full price download; detector over all pairs |
| Sun 1 Nov | Event list v1; double coding starts |
| Mon 2 Nov | Coding complete and reconciled; descriptive tables |
| Tue 3 Nov | Kaplan–Meier + Cox v1; headline chart draft |
| Wed 4 Nov | Robustness; **freeze results** |
| Thu 5 Nov | Deck v1 |
| Fri 6 Nov | Red-team review; fixes |
| Sat 7 Nov | Final figures; scripts → `.txt` |
| Sun 8 Nov | Submit by 20:00 |

## 11. Risks and mitigations

| Risk | Mitigation |
|---|---|
| Too few independent events | Lower the threshold for major coins; include smaller coins; switch to a comparative case study |
| Redemption status hard to code | Use objective proxies (weekend / US bank holiday / announced pause); report coder agreement |
| Heterogeneous designs pooled | Stratify by backing type; leave-one-issuer-out |
| Venue-specific prices (USDe on one exchange) | Require the deviation on ≥ 2 venues, or code it as `venue-specific` and test with and without |
| Small-sample Cox instability | Few covariates; report confidence intervals; lead with Kaplan–Meier |

## 12. Literature anchors

- Shleifer, A. & Vishny, R. (1997). The limits of arbitrage. *Journal of Finance*.
- Lyons, R. & Viswanath-Natraj, G. (2023). What keeps stablecoins stable? *Journal of International Money and Finance*.
- Add 1–2 recent stablecoin run / depeg papers after a literature check `[verify]`.
