# P3-26: October incident and November evaluation

E1 S2 excludes the 30 Oct observation directly. Small later cross-venue gaps do not rule out persistent or shared incident effects. Exact USDT withdrawal restoration is not verified by the source register.

## Observed daily premiums (bps)

date_brt,Binance,Foxbit,Mercado Bitcoin,gap_foxbit,gap_mb
2026-10-29,12.483,13.412,11.317,0.929,-1.166
2026-10-30,-30.346,18.612,17.411,48.958,47.757
2026-11-03,17.599,16.597,,-1.003,
2026-11-04,25.049,22.032,,-3.016,
2026-11-05,22.19,23.429,,1.239,
2026-11-06,16.764,16.899,,0.135,

## Window sensitivity (computed)

event,specification,pre_window_dates,pre_mean_bps,post_window_dates,post_mean_bps,s2_bps,s2_reference_band_bps,p_two_sided,status,interpretation
E1 (Res. 574),Registered P3-20 rule (excludes 30 Oct from pre-mean),2026-10-01..2026-10-29,19.23,2026-11-03..2026-11-04,21.32,2.09,-75.5 / +59.8,0.8966,registered_verdict,30 Oct observation excluded directly; residual incident effects possible
E1 (Res. 574),Diagnostic check (including 30 Oct in 20d pre-window),2026-10-02..2026-10-30,17.48,2026-11-03..2026-11-04,21.32,3.84,-75.5 / +59.8,0.8203,diagnostic_sensitivity_only,Diagnostic S2=3.84 bps; p=0.8203; registered score unchanged
E2 (Res. 589),"Registered P3-20 rule (20d pre-window ending 4 Nov, contains 30 Oct)",2026-10-06..2026-11-04,15.94,pending (6 Nov / 9 Nov),,,-75.5 / +59.8,,registered_baseline,30 Oct (-30.3 bps) pulls down 20d pre-mean by ~2.4 bps vs 19d unweighted mean
E2 (Res. 589),"Diagnostic check (excluding 30 Oct from pre-window, 19 days)",2026-10-06..2026-11-04 (excl 30 Oct),18.38,pending (6 Nov / 9 Nov),,,-75.5 / +59.8,,diagnostic_sensitivity_only,Pre-mean rises from 15.94 to 18.38 bps (+2.44 bps shift). Small relative to +-75 bps band
E2 (Res. 589),Diagnostic check (replacing 30 Oct with neutral 15.0 bps baseline),2026-10-06..2026-11-04 (30 Oct=15 bps),18.21,pending (6 Nov / 9 Nov),,,-75.5 / +59.8,,diagnostic_sensitivity_only,Pre-mean rises by +2.27 bps to 18.21 bps. Pre-registered score remains unchanged

## Timeline

timestamp_utc,timestamp_brt,market_event,binance_premium_bps,foxbit_premium_bps,mb_premium_bps,gap_foxbit_binance_bps,gap_mb_binance_bps,cusum_state,p3_20_window_role
2026-10-29 13:00-17:00,2026-10-29 10:00-14:00,Pre-incident normal trading (PTAX window),12.5,13.4,11.3,0.9,-1.2,Normal (cumulative monitoring),E1 pre-window final day (t0-1); clean pre-baseline
2026-10-29 20:05,2026-10-29 17:05,"Binance hot-wallet compromise & withdrawal freeze (M-11, M-12)",,,,,,Incident onset (after the PTAX measurement window),Occurred 3h after 29 Oct PTAX window closed
2026-10-30 13:00-17:00,2026-10-30 10:00-14:00,PTAX window during withdrawal suspension (sharp Binance-only dip),-30.3,18.6,17.4,49.0,47.8,Alarm triggered: Downward alarm 2026-10-30(-),E1 t0 (EXCLUDED from S2 pre-mean; contaminates S1 baseline)
2026-10-31 to 2026-11-01,2026-10-31 to 2026-11-01,Phased restoration planned (M-11); exact USDT restoration unverified,,,,,,Mandatory quiet pause day 0 (weekend),Weekend (no PTAX window)
2026-11-02,2026-11-02,Dia de Finados bank holiday in Brazil,,,,,,Mandatory quiet pause day 0 (holiday),Holiday (no PTAX window)
2026-11-03 13:00-17:00,2026-11-03 10:00-14:00,Res. 574 effective; observed cross-venue gap small,17.6,16.6,,-1.0,,Pause day 1/10 (QUIET=10 active),E1 post-day 1 (t0+1); S1 reading (+47.9 bps vs 30 Oct)
2026-11-04 13:00-17:00,2026-11-04 10:00-14:00,E1 post-day 2; Copom decision evening; US midterms,25.0,22.0,,-3.0,,Pause day 2/10 (QUIET=10 active),E1 post-day 2 (t0+2); S2 evaluation window completes
2026-11-05 13:00-17:00,2026-11-05 10:00-14:00,Last PTAX day before Res. 589 art. 91 ban (E2 t0),22.2,23.4,,1.2,,Pause day 3/10 (QUIET=10 active),E2 t0 (pre-window ending on 4 Nov contains 30 Oct)
2026-11-06 13:00-17:00,2026-11-06 10:00-14:00,Res. 589 art. 91 ban in force; US payrolls (10:30 BRT),16.8,16.9,,0.1,,Pause day 4/10 (QUIET=10 active through 16 Nov),E2 post-day 1 (t0+1); S1 early reading window

E2 S1 is an early reading only. The registered two-day verdict requires 9 November, after submission. Reference bands are historical distributions, not causal effect confidence bounds. CUSUM silence during its ten-observation quiet pause is mechanical.
