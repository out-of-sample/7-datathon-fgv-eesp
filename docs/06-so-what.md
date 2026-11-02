# Plan — answering "so what?"

**Status:** active since 2 Nov 2026 (Renzo). Tasks P3-09 to P3-13. Freeze is Wed 4 Nov, so every task here is
small and has a stop rule.

## The problem

The measured effect is a +94 bps spike in the USDT/BRL premium for about one month after the 23 Jun 2026 BCB
notice; the lasting effect is not distinguishable from noise (F-016, F-022). A juror can fairly ask "so what?".
We cannot make the effect bigger. We can show what it means: how much money it moved, which rules matter, what
mechanism produced it, and what to watch next.

## Step 0 — the notice itself (P3-09)

Our account of the notice rests on two opinion pieces and a LAI answer (E-05). A contemporaneous report exists
(Cointelegraph Brasil, 24 Jun 2026: the notification was shared with the reporter). P3-09 sweeps for every
report and official text about the notice, opens each one and adds it to `docs/sources.md` with a quote.

## The four answers

| # | Answer | Task | What it uses | Can show | Cannot show |
|---|---|---|---|---|---|
| 3 | **Mechanism.** The notice closed the channel arbitrage funds used to bring stablecoins in. BCB statistics: stablecoin purchases abroad fell from US$ 2.54 bn (Jun) to US$ 0.57 bn (Jul 2026), per InvestNews 28 Aug. Price up, quantity down = a supply channel closing. Fade test: did imports recover when the premium fell back? | **P3-10** (first) | BCB external-sector statistics (new download); frozen exchange data for on-exchange volume and order flow | That price and imported quantity moved as a closed supply channel predicts; whether the fade coincides with imports recovering | How much of the drop came from funds rather than other buyers; a causal estimate (monthly data, few points) |
| 1 | **Money.** 0.9% on a market of about R$ 16 bn in four weeks is about R$ 100–145 mn paid by buyers over the pre-notice level. The notice worked like an import quota; its tariff equivalent was about 0.9%, and the rent went to whoever could still bring dollars in, not to the Treasury | **P3-11** | P1-02 premium, frozen venue volumes | Size of the transfer, with a range (venues, windows) and the same number at placebo dates | A welfare loss (it is a transfer); OTC desks and other venues are missing |
| 2 | **Which rules matter.** A confidential notice moved the premium; published rules (IOF decree, Res. 561, Res. 584) did not | **P3-12** | P2-03 event table (no new analysis) | That only the rule that closed the channel arbitrageurs used moved the price | Whether "confidential" or "content" did it (they differ in both); effects below the ~25–37 bps detection limit |
| 4 | **A tool and a dated prediction.** The monitor flags the jump the same day (F-014). We commit, before the final, what should happen when Res. 584's 24-hour hold starts on 1 Jan 2027 | **P3-13** | P3-03 monitor, P3-01 one-day FX risk | A falsifiable claim the jury can check later | Anything now: it is a scenario |

Order: P3-09 and P3-10 first (they decide the story), then P3-11, P3-12, P3-13. The numbers in this table are
rough sizing from 2 Nov; they become findings only through the tasks.

## Stop rules

- If the BCB series does not reproduce the press numbers (US$ 2,540 mn Jun, US$ 572 mn Jul), stop P3-10 and
  report the mismatch before testing anything.
- If P3-10's July drop is within the series' normal monthly range, the mechanism stays "reported, not
  measured" and answer 3 is dropped from the deck.
- Every result is reported whichever way it goes, including a fade that imports do not explain.

## What this plan does not change

The headline estimate (+93.9 bps, F-016) and its robustness (F-022) stay as they are. Side experiments
(Extension A, Band-TAR, 2025 subsidy share) are not part of this plan; their place in the deck is a team call.
