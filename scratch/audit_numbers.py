import sys, os, glob, re, json
import pandas as pd

sys.stdout.reconfigure(encoding='utf-8')

print("="*60)
print("AUDIT: NUMBER MATCHING CHECK")
print("="*60)

# 1. Check P2-03_event_table.csv for E-05
df_e = pd.read_csv('results/tables/P2-03_event_table.csv')
e05 = df_e[df_e['event_id'].str.startswith('E-05')].iloc[0]
print(f"E-05 event_date: {e05['event_date']}, t0_ptax: {e05['t0_ptax']}")
print(f"E-05 pre_mean_bps: {e05['pre_mean_bps']:.4f}, post_mean_bps: {e05['post_mean_bps']:.4f}, diff_bps: {e05['diff_bps']:.4f}")
print(f"E-05 p_param: {e05['p_param']:.6e}, p_placebo_all_clean_2s: {e05['p_placebo_all_clean_2s']}")

# 2. Check P2-04_synth_results.csv
df_s = pd.read_csv('results/tables/P2-04_synth_results.csv')
print("\nP2-04 Synth Results:")
for idx, r in df_s.iterrows():
    print(f"  {r['specification']}: acute_gap={r['acute_gap_sc_bps']}, did_acute={r['did_acute_gap_bps']}, plateau_gap={r['plateau_gap_sc_bps']}, rmspe_ratio={r['rmspe_ratio']}, rank={r['placebo_rank']}, p={r['permutation_p_value']}")

# 3. Check P3-11_transfer.csv
df_t = pd.read_csv('results/tables/P3-11_transfer.csv')
print("\nP3-11 Transfer Results:")
for idx, r in df_t.iterrows():
    if 'headline' in str(r['variant']):
        print(f"  {r['variant']} | {r['venue']} | vol_bn: {r['volume_brl_bn']} | transfer_mn: {r['transfer_brl_mn']} | tariff_bps: {r['tariff_equivalent_bps']} | p: {r['placebo_p']}")

# 4. Check P3-10_imports.csv
df_i = pd.read_csv('results/tables/P3-10_imports.csv')
print("\nP3-10 Imports Results:")
for idx, r in df_i.iterrows():
    print(f"  {r['test']} | val: {r['value']} | pct_change: {r['pct_change']} | p: {r['p_empirical']}")

# 5. Check P3-25_composition.csv
df_c = pd.read_csv('results/tables/P3-25_composition.csv')
print("\nP3-25 Composition Results:")
for idx, r in df_c.iterrows():
    print(f"  {r['period']} ({r['start_brt']} to {r['end_brt']}): share={r['foxbit_share_pct']:.2f}%, vol_usdt={r['foxbit_volume_usdt']}, median_daily_trade={r['foxbit_median_daily_trade_usdt']}, biz_hours={r['foxbit_business_hour_volume_pct']:.2f}%")

# 6. Check P3-20_readout.csv
df_r = pd.read_csv('results/tables/P3-20_readout.csv')
print("\nP3-20 Readout Results:")
for idx, r in df_r.iterrows():
    if r['status'] == 'observed' or 'pending' in str(r['status']):
        print(f"  {r['event']} | {r['series']} | {r['statistic']} | post_days={r['post_days']} | obs={r['observed_bps']} | p={r['p_two_sided']} | band=[{r['band_lo_bps']}, {r['band_hi_bps']}] | status={r['status']}")

# 7. Check P3-34_cost_stack.csv
df_cs = pd.read_csv('results/tables/P3-34_cost_stack.csv')
print("\nP3-34 Cost Stack:")
for idx, r in df_cs.iterrows():
    print(f"  {r['cenario_ou_rota']} | premio={r['premio_acesso_bps']} | neg={r['taxa_negociacao_bps']} | saque={r['taxa_saque_onchain_bps']} | total={r['custo_total_bps']} | custo_brl={r['custo_reais_por_100k_ptax']} | razao={r['razao_choque_vs_rede']}")

# 8. Check P3-31 Buyer Hedged
df_h = pd.read_csv('results/tables/P3-31_buyer_hedged_comparison.csv')
print("\nP3-31 Buyer Hedged:")
for h in [5, 6, 10, 20]:
    row = df_h[df_h['horizon_ptax_days'] == h].iloc[0]
    print(f"  horizon={h}d: deadline={row['deadline']}, hedged_savings_bps={row['hedged_savings_bps']:.1f}, hedged_savings_brl={row['hedged_savings_brl']:.2f}, seller_wait_brl={row['seller_wait_minus_sell_now_brl']:.2f}")

# 9. Check P3-30 Census & Duration
if os.path.exists('results/tables/P3-30_feasibility.csv'):
    df_f = pd.read_csv('results/tables/P3-30_feasibility.csv')
    print("\nP3-30 Feasibility:")
    print(df_f)
if os.path.exists('results/tables/P3-30_census.csv'):
    df_cen = pd.read_csv('results/tables/P3-30_census.csv')
    print("\nP3-30 Census:")
    print(df_cen)
if os.path.exists('results/tables/P3-30_descriptive_km.csv'):
    df_km = pd.read_csv('results/tables/P3-30_descriptive_km.csv')
    print("\nP3-30 KM:")
    print(df_km.head(10))
if os.path.exists('results/tables/P3-30_run_summary.json'):
    with open('results/tables/P3-30_run_summary.json') as f:
        print("\nP3-30 run_summary.json:")
        print(json.dumps(json.load(f), indent=2))
