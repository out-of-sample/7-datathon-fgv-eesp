import sys, os, re
import pandas as pd
import numpy as np

sys.stdout.reconfigure(encoding='utf-8')

print("="*60)
print("EXHAUSTIVE TABLE-BY-TABLE NUMBER VERIFICATION")
print("="*60)

# Slide 1 & 4:
# +93.9 bps (from 15.2 to 109.1 bps)
df_events = pd.read_csv('results/tables/P2-03_event_table.csv')
e05 = df_events[df_events['event_id'].str.startswith('E-05')].iloc[0]
print("Check E-05 event table:")
print(f"  pre_mean_bps: {e05['pre_mean_bps']:.1f} (deck says 15,2)")
print(f"  post_mean_bps: {e05['post_mean_bps']:.1f} (deck says 109,1)")
print(f"  diff_bps: {e05['diff_bps']:.1f} (deck says +93,9)")
print(f"  t_stat: {e05['t_stat']:.2f}, p_param: {e05['p_param']:.6e}")
print(f"  p_placebo_all_clean_2s: {e05['p_placebo_all_clean_2s']}")

# Check Robustness table P4-01
df_rob = pd.read_csv('results/tables/P4-01_robustness.csv')
print("\nCheck Robustness table for venues & variants (22 variants):")
print(f"  Total rows in P4-01: {len(df_rob)}")
for idx, r in df_rob.iterrows():
    print(f"  [{idx+1}] {r['dimension']} | {r['specification']} | effect = {r['effect_or_gap_bps']} bps | p/rank = {r['p_value_or_rank']}")

effects = df_rob['effect_or_gap_bps'].dropna().astype(float)
print(f"  Min effect across variants: {effects.min():.1f} bps (deck says +73,7)")
print(f"  Max effect across variants: {effects.max():.1f} bps (deck says +128,3)")

# Check R$ 4,842 in P3-01
df_route = pd.read_csv('results/tables/P3-01_route_costs.csv')
print("\nCheck P3-01 route costs for headline cost:")
spike_row = df_route[df_route['regime_or_scenario'].str.contains('Cost of the notice: spike', case=False, na=False)].iloc[0]
print(f"  Spike cost BRL: {spike_row['cost_brl_per_100k']:.2f} (deck says R$ 4.842)")
after_row = df_route[df_route['regime_or_scenario'].str.contains('Cost of the notice: after', case=False, na=False)].iloc[0]
print(f"  After spike cost BRL: {after_row['cost_brl_per_100k']:.2f} (deck says R$ 583)")

# Check 1.073 common dates, max = +65.7 bps:
df_placebos = pd.read_csv('results/tables/P2-03_placebo_draws.csv')
print("\nCheck Placebos in P2-03:")
print(f"  Total draws in P2-03_placebo_draws.csv: {len(df_placebos)}")
print(f"  Max placebo_diff_bps in 200 draws: {df_placebos['placebo_diff_bps'].max():.1f}")
# Let's check where 1.073 clean dates come from: F-016!
# In F-016: out of 1,073 clean dates, max was +65.7 bps!

# Check Bai-Perron breaks P2-02_breaks.csv
df_breaks = pd.read_csv('results/tables/P2-02_breaks.csv')
print("\nCheck P2-02 Breaks:")
for idx, r in df_breaks.iterrows():
    print(f"  break_date: {r['break_date']} | ci_lower: {r.get('ci_lower_hetero', r.get('ci_lower_homo', ''))} | ci_upper: {r.get('ci_upper_hetero', r.get('ci_upper_homo', ''))} | pre_mean: {r.get('pre_mean_bps', '')} | post_mean: {r.get('post_mean_bps', '')}")

# Check Synth control P2-04_synth_results.csv
df_synth = pd.read_csv('results/tables/P2-04_synth_results.csv')
h_synth = df_synth[df_synth['specification'].str.contains('Headline')].iloc[0]
print("\nCheck Synth Control Headline:")
print(f"  acute_gap_sc_bps: {h_synth['acute_gap_sc_bps']} (deck says +109,3)")
print(f"  did_acute_gap_bps: {h_synth['did_acute_gap_bps']} (deck says +103,3)")
print(f"  plateau_gap_sc_bps: {h_synth['plateau_gap_sc_bps']} (deck says +28,2)")
print(f"  rmspe_ratio: {h_synth['rmspe_ratio']} (deck says 9,31)")
print(f"  rank: {h_synth['placebo_rank']} (deck says 1/6)")
print(f"  p-value: {h_synth['permutation_p_value']} (deck says 0,167 or 1/6)")

# Check BTC jump F-018
df_btc = pd.read_csv('results/tables/P3-02_btc_events.csv')
print("\nCheck BTC events in P3-02:")
btc_e05 = df_btc[df_btc['event_id'].str.startswith('E-05')]
for idx, r in btc_e05.iterrows():
    print(f"  {r['event_id']} | series: {r['series']} | pre: {r['pre_mean_bps']:.1f} | post: {r['post_mean_bps']:.1f} | diff: {r['diff_bps']:.1f}")

# Check Imports P3-10
df_imp = pd.read_csv('results/tables/P3-10_imports.csv')
print("\nCheck Imports P3-10:")
for idx, r in df_imp.iterrows():
    print(f"  {r['test']} | val: {r['value']} | pct_change: {r['pct_change']:.1f}% | p: {r['p_empirical']}")

# Check Transfer P3-11
df_trans = pd.read_csv('results/tables/P3-11_transfer.csv')
print("\nCheck Transfer P3-11:")
h_trans = df_trans[df_trans['variant'].str.contains('headline')]
for idx, r in h_trans.iterrows():
    print(f"  {r['venue']} | vol: {r['volume_brl_bn']} bi | transfer: {r['transfer_brl_mn']:.1f} mi | tariff: {r['tariff_equivalent_bps']:.1f} bps | p: {r['placebo_p']}")

# Check Who paid P3-21
df_who = pd.read_csv('results/tables/P3-21_who_paid.csv')
print("\nCheck Who paid P3-21:")
for idx, r in df_who.iterrows():
    print(f"  {r['user']} | {r['case']} | {r['counterfactual']} | BRL: {r['brl']}")

# Check Rules P3-12_rules.csv
df_rules = pd.read_csv('results/tables/P3-12_rules.csv')
print("\nCheck Rules P3-12:")
for idx, r in df_rules.iterrows():
    print(f"  {r['event_id']} | type: {r['type']} | diff: {r['diff_bps']:.1f} bps | p_placebo: {r['p_placebo']}")
