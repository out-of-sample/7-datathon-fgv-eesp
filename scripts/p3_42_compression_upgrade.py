"""P3-42 rolling compression upgrade. No downloads; preserves P3-41.
Run python scripts/p3_42_compression_upgrade.py [--test-only].
Inputs P1-02 daily/hourly and P3-41 prediction CSV. Outputs P3-42 CSV/JSON/PNG.
Protocol: tasks/P3-42-compression-upgrade.md. All results exploratory/scenario-only.
"""
import argparse
import hashlib
import itertools
import json
from pathlib import Path
import unittest
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import p3_41_compression as v1
from p3_38_buyer_frontier import budget

ROOT=v1.ROOT; TAB=v1.TAB; FIG=v1.FIG
CONFIGS={'persistence':('persistence',0), 'mean_reversion':('mean_reversion',0),
         'rolling_ridge_100':('linear',100), 'rolling_ridge_1000':('linear',1000),
         'rolling_hinge_100':('hinge',100), 'rolling_hinge_1000':('hinge',1000)}


def mature(q, cutoff, limit=756):
    return q.loc[q.origin_eligible & q.terminal_eligible &
                 q.terminal_execution_time_utc.lt(cutoff)].tail(limit)


def fit(x,y,kind,alpha):
    mu=x.mean(axis=0); sd=x.std(axis=0);sd=np.where(sd>1e-10,sd,1.)
    z=(x-mu)/sd
    knots=np.quantile(z,[.25,.5,.75],axis=0)
    b=basis(z,knots,kind)
    return dict(mu=mu,sd=sd,knots=knots,kind=kind,model=v1.fit_ridge(b,y,alpha))


def basis(z,knots,kind):
    if kind=='linear': return z
    return np.column_stack([z,*[np.maximum(z-k,0) for k in knots]])


def forecast(model,x):
    z=basis((x-model['mu'])/model['sd'],model['knots'],model['kind'])
    m=model['model']; design=np.column_stack([np.ones(len(x)),(z-m['mu'])/m['scale']])
    return design@m['coef']


def issue_forecasts(q,h):
    """All model fits use only outcomes matured before the month start."""
    records=[]; traces=[]
    origins=q.loc[q.origin_eligible & (q.index.year>=2024)]
    for month,frame in origins.groupby(origins.index.to_period('M')):
        cutoff=month.start_time
        train=mature(q,cutoff)
        if len(train)<250: continue
        x=train[v1.FEATURES].to_numpy(); y=train.target_compression_bps.to_numpy()
        for name,(kind,alpha) in CONFIGS.items():
            if kind in ('linear','hinge'):
                model=fit(x,y,kind,alpha); pred=forecast(model,frame[v1.FEATURES].to_numpy())
            else: pred=v1.predict(frame,kind)
            traces.append(dict(month=str(month),horizon=h,method=name,n_fit=len(train),
                fit_first_origin=str(train.index.min()),fit_last_origin=str(train.index.max()),
                fit_last_terminal=str(train.terminal_execution_time_utc.max()),fit_cutoff=str(cutoff)))
            for (origin,row),value in zip(frame.iterrows(),pred):
                records.append(dict(origin=origin,signal_time_utc=row.signal_time_utc,
                    execution_time_utc=row.execution_time_utc,terminal_time_utc=row.terminal_execution_time_utc,
                    terminal_eligible=bool(row.terminal_eligible),horizon=h,method=name,
                    predicted_compression_bps=float(value),actual_compression_bps=row.target_compression_bps))
    return pd.DataFrame(records),traces


def attach_bands(raw):
    records=[]
    for (_, _), group in raw.groupby(['horizon','method']):
        group=group.sort_values('origin')
        for _,row in group.iterrows():
            hist=group.loc[group.terminal_eligible & group.terminal_time_utc.lt(row.signal_time_utc)].tail(126)
            if len(hist)<60: continue
            radius=v1.residual_radius(hist.actual_compression_bps-hist.predicted_compression_bps)
            records.append(dict(**row.to_dict(),radius_bps=radius,calibration_n=len(hist),
                                last_calibration_terminal=hist.terminal_time_utc.max()))
    return pd.DataFrame(records)


def stress_card(row,panel):
    h=int(row.horizon); origin=pd.Timestamp(row.origin); signal=panel.loc[origin]
    vals=[]
    for dep,yld,uf,fx,fee,fixed in itertools.product((0,.05,.10),(0,.04),(.995,1,1.005),(.98,1,1.02),(.001,.003),(0,100)):
        for compression in (row.predicted_compression_bps-row.radius_bps,row.predicted_compression_bps+row.radius_bps):
            vals.append(budget(h,x0=signal.ptax,u0=signal.signal_usdtusd,p0=signal.signal_premium,
                x1=signal.ptax*fx,u1=signal.signal_usdtusd*uf,p1=signal.signal_premium-compression,
                deposit=dep,held_yield=yld,fee_wait=fee,fixed_wait=fixed)['max_additional_cost_bps'])
    decision=v1.assess(signal.signal_premium,row.predicted_compression_bps,row.radius_bps,h,
                       signal.ptax,signal.signal_usdtusd,25)
    return dict(origin=origin,horizon=h,method=row.method,forecast_bps=row.predicted_compression_bps,
        radius_bps=row.radius_bps,**decision,stress_min_budget_bps=min(vals),stress_max_budget_bps=max(vals),
        stress_conditional_signal=v1.conditional_signal(min(vals),max(vals),25),
        stress_actionable_signal='insufficient_evidence',scenario_count=216,
        note='compression interval endpoints crossed with scenario envelope; not probability bounds')


def run():
    d=pd.read_csv(v1.DAILY,parse_dates=['date_brt']).set_index('date_brt')
    hourly=pd.read_csv(v1.HOURLY,parse_dates=['time_utc']).set_index('time_utc')
    panel=v1.build_panel(d,hourly); audit=v1.audit_inputs(d,hourly,panel)
    raw=[]; traces=[]
    for h in v1.HORIZONS:
        a,t=issue_forecasts(v1.dataset(panel,h),h);raw.append(a);traces.extend(t)
    raw=pd.concat(raw,ignore_index=True); banded=attach_bands(raw)
    valid=banded.terminal_eligible & (((banded.origin.dt.year==2025) & banded.terminal_time_utc.le(v1.VAL_END)) |
                                     (banded.origin.dt.year==2026))
    ev=banded.loc[valid].copy()
    # Complete-case intersection ensures all methods face identical evaluation dates.
    counts=ev.groupby(['horizon','origin']).method.nunique()
    common=set(counts[counts.eq(len(CONFIGS))].index)
    ev=ev.loc[[(h,o) in common for h,o in zip(ev.horizon,ev.origin)]].copy()
    ev['split']=np.where(ev.origin.dt.year.eq(2025),'validation','test')
    errors=abs(ev.predicted_compression_bps-ev.actual_compression_bps)
    selection=ev.assign(abs_error=errors).query("split == 'validation' and horizon == 10").groupby('method').abs_error.mean()
    candidates=selection[[k for k in CONFIGS if k.startswith('rolling_')]]
    selected=candidates.sort_values(kind='stable').index[0]
    ev['selected']=ev.method.eq(selected)
    ev['nonoverlapping']=False
    for (_,h),g in ev.groupby(['split','horizon']):
        q=g[g.method.eq('persistence')].set_index('origin').rename(columns={'terminal_time_utc':'terminal_execution_time_utc'})
        dates=v1.nonoverlap(q)
        ev.loc[g.index,'nonoverlapping']=g.origin.isin(dates)
    enriched=[]
    for row in ev.itertuples(index=False):
        p=panel.loc[row.origin]; terminal=panel.loc[row.terminal_time_utc.normalize()]
        decision=v1.assess(p.signal_premium,row.predicted_compression_bps,row.radius_bps,int(row.horizon),p.ptax,p.signal_usdtusd,25)
        actual=budget(int(row.horizon),x0=p.ptax,u0=p.execution_usdtusd,p0=p.execution_premium,
            x1=terminal.ptax,u1=terminal.execution_usdtusd,p1=terminal.execution_premium)['max_additional_cost_bps']-25
        waits=decision['conditional_signal']=='waiting_may_compensate'
        enriched.append(dict(**row._asdict(),**decision,realized_wait_saving_bps=actual,
            policy_saving_bps=actual if waits else 0.,policy_wait=waits,
            covers=abs(row.actual_compression_bps-row.predicted_compression_bps)<=row.radius_bps))
    ev=pd.DataFrame(enriched)
    old=pd.read_csv(TAB/'P3-41_predictions.csv',parse_dates=['origin'])
    old=old[old.additional_cost_bps.eq(25) & old.method.eq('ridge')].copy()
    matched=ev[ev.method.eq(selected)].merge(old,on=['origin','horizon','split'],suffixes=('_new','_v1'),validate='one_to_one')
    metrics=[]; comparisons=[]; baseline_gaps=[]
    for (split,h,method),g in ev.groupby(['split','horizon','method']):
        for scope in ('daily','nonoverlapping'):
            a=g if scope=='daily' else g[g.nonoverlapping]
            err=abs(a.predicted_compression_bps-a.actual_compression_bps)
            metrics.append(dict(split=split,horizon=h,method=method,selected=method==selected,scope=scope,n=len(a),
                mae_bps=err.mean(),coverage=a.covers.mean(),width_bps=(2*a.radius_bps).mean(),
                wait_count=int(a.policy_wait.sum()),abstain_fraction=a.conditional_signal.eq('insufficient_evidence').mean(),
                mean_saving_bps=a.policy_saving_bps.mean(),worst_saving_bps=a.policy_saving_bps.min(),
                always_wait_mean_bps=a.realized_wait_saving_bps.mean()))
    for (split,h),g in matched.groupby(['split','horizon']):
        for scope in ('daily','nonoverlapping'):
            a=g if scope=='daily' else g[g.nonoverlapping_new]
            gap=abs(a.predicted_compression_bps_new-a.actual_compression_bps_new)-abs(a.predicted_compression_bps_v1-a.actual_compression_bps_v1)
            lo,hi=v1.bootstrap_gap(gap.to_numpy()) if scope=='nonoverlapping' else (np.nan,np.nan)
            comparisons.append(dict(split=split,horizon=h,scope=scope,n=len(a),selected=selected,
                selected_mae_bps=abs(a.predicted_compression_bps_new-a.actual_compression_bps_new).mean(),
                v1_mae_bps=abs(a.predicted_compression_bps_v1-a.actual_compression_bps_v1).mean(),
                gap_bps=gap.mean(),lo95_bps=lo,hi95_bps=hi))
    for (split,h),g in ev[ev.nonoverlapping].groupby(['split','horizon']):
        wide=g.assign(error=abs(g.predicted_compression_bps-g.actual_compression_bps)).pivot(index='origin',columns='method',values='error').sort_index()
        for baseline in ('persistence','mean_reversion'):
            gap=wide[selected]-wide[baseline];lo,hi=v1.bootstrap_gap(gap.to_numpy())
            baseline_gaps.append(dict(split=split,horizon=h,selected=selected,baseline=baseline,n=len(gap),gap_bps=gap.mean(),lo95_bps=lo,hi95_bps=hi))
    cards=[]
    for h in v1.HORIZONS:
        a=banded[banded.horizon.eq(h) & banded.method.eq(selected)].sort_values('origin')
        for label, rows in [('june',a[a.origin.eq(pd.Timestamp('2026-06-25'))]),('archive_latest',a.tail(1))]:
            if len(rows)!=1: raise ValueError('Missing fixed decision-card origin')
            cards.append(dict(card=label,**stress_card(next(rows.itertuples(index=False)),panel)))
    metrics=pd.DataFrame(metrics); comparisons=pd.DataFrame(comparisons)
    outputs={'predictions':ev,'issued_forecasts':raw,'fit_trace':pd.DataFrame(traces),'metrics':metrics,
             'selection':selection.reset_index(name='validation_mae_bps').assign(selected=lambda x:x.method.eq(selected)),
             'v1_comparison':comparisons,'baseline_gaps':pd.DataFrame(baseline_gaps),'decision_cards':pd.DataFrame(cards)}
    for name,table in outputs.items():table.to_csv(TAB/f'P3-42_{name}.csv',index=False,lineterminator='\n')
    audit.update(selected=selected,protocol='tasks/P3-42-compression-upgrade.md; ce91d8b',
        source_sha256={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in
        (Path(__file__),ROOT/'scripts/p3_41_compression.py',ROOT/'scripts/p3_38_buyer_frontier.py')},
        interpretation='exploratory upgrade after seeing 2026 v1; not a fresh holdout',
        calibration='prior-issued errors only, terminal timestamp strictly earlier than signal',
        environment=dict(numpy=np.__version__,pandas=pd.__version__,matplotlib=matplotlib.__version__))
    (TAB/'P3-42_audit.json').write_text(json.dumps(audit,indent=2),encoding='utf-8')
    chart(metrics,comparisons,selected)
    print('SELECTED:',selected)
    print(metrics.query("split == 'test' and horizon == 10").to_string(index=False))
    print(comparisons.query("split == 'test' and horizon == 10").to_string(index=False))
    print(outputs['decision_cards'][['card','horizon','conditional_signal','stress_conditional_signal']].to_string(index=False))


def chart(metrics,comparison,selected):
    a=metrics.query("split == 'test' and horizon == 10 and scope == 'daily'").set_index('method')
    labels=['Persistência','Reversão simples','Ridge v1 (mesmas datas)','Modelo escolhido em 2025']
    values=[a.loc['persistence'].mae_bps,a.loc['mean_reversion'].mae_bps,
            comparison.query("split == 'test' and horizon == 10 and scope == 'daily'").iloc[0].v1_mae_bps,a.loc[selected].mae_bps]
    fig,axs=plt.subplots(1,2,figsize=(12,5),gridspec_kw={'width_ratios':[1.4,1]})
    bars=axs[0].barh(labels,values,color=['#999999','#c48220','#777777','#246ca6'])
    for b,v in zip(bars,values):axs[0].text(v+.3,b.get_y()+b.get_height()/2,f'{v:.2f}',va='center')
    axs[0].invert_yaxis();axs[0].set(xlim=(0,max(values)*1.2),xlabel='Erro absoluto médio (pb)',title='Previsão de 10 dias em 2026')
    for method,label,color in [('mean_reversion','Reversão simples','#c48220'),(selected,'Modelo escolhido','#246ca6')]:
        b=metrics.query("split == 'test' and scope == 'daily'");b=b[b.method.eq(method)].sort_values('horizon')
        axs[1].plot(b.horizon,100*b.coverage,'o-',label=label,color=color)
    axs[1].axhline(90,ls='--',color='#777777',label='Nominal: 90%')
    axs[1].set(xticks=[5,10,20],ylim=(0,105),xlabel='Prazo (dias PTAX)',ylabel='Cobertura (%)',title='Faixas atualizadas com erros conhecidos')
    axs[1].legend(fontsize=8)
    for ax in axs:ax.spines[['top','right']].set_visible(False)
    fig.suptitle('Upgrade: ajuste mensal e calibração adaptativa',fontweight='bold',fontsize=15)
    fig.text(.03,.02,f'Escolha em 2025: {selected}. Comparação retrospectiva; 2026 já visto no projeto.\nCustos hipotéticos; acesso desconhecido. Faixas sem garantia. Fonte: Binance/BCB, P1-02; protocolos P3-41/P3-42.',fontsize=9)
    fig.tight_layout(rect=(0,.13,1,.92));fig.savefig(FIG/'P3-42_upgrade.png',dpi=180);plt.close(fig)


class Tests(unittest.TestCase):
    def test_maturity_strict_and_limit(self):
        dates=pd.date_range('2024-01-01',periods=5)
        q=pd.DataFrame({'origin_eligible':True,'terminal_eligible':True,'terminal_execution_time_utc':dates},index=dates)
        self.assertEqual(mature(q,pd.Timestamp('2024-01-04'),2).index.tolist(),list(dates[1:3]))

    def test_calibration_future_outcome_perturbation(self):
        dates=pd.date_range('2024-01-01',periods=90)
        raw=pd.DataFrame({'origin':dates,'signal_time_utc':dates+pd.Timedelta(hours=17),
            'terminal_time_utc':dates+pd.Timedelta(days=5,hours=18),'terminal_eligible':True,
            'horizon':5,'method':'persistence','predicted_compression_bps':0.,'actual_compression_bps':np.arange(90)})
        a=attach_bands(raw); cutoff=dates[75]+pd.Timedelta(hours=17)
        raw.loc[raw.terminal_time_utc>=cutoff,'actual_compression_bps']=100000
        b=attach_bands(raw)
        pd.testing.assert_series_equal(a[a.signal_time_utc<=cutoff].radius_bps,b[b.signal_time_utc<=cutoff].radius_bps)
        self.assertTrue((a.last_calibration_terminal<a.signal_time_utc).all())

    def test_hinge_knots_and_constant(self):
        x=np.column_stack([np.arange(300.),np.ones(300)])
        m=fit(x,np.ones(300)*7,'hinge',100)
        self.assertTrue(np.allclose(forecast(m,x),7))
        self.assertTrue(np.allclose(m['knots'],np.quantile((x-m['mu'])/m['sd'],[.25,.5,.75],axis=0)))

    def test_month_fit_ignores_unmatured_labels(self):
        dates=pd.bdate_range('2021-01-01','2024-02-29')
        rng=np.random.default_rng(42)
        q=pd.DataFrame(rng.normal(size=(len(dates),len(v1.FEATURES))),index=dates,columns=v1.FEATURES)
        q['origin_eligible']=True;q['terminal_eligible']=True
        q['terminal_execution_time_utc']=dates+pd.Timedelta(days=20,hours=18)
        q['signal_time_utc']=dates+pd.Timedelta(hours=17);q['execution_time_utc']=dates+pd.Timedelta(hours=18)
        q['target_compression_bps']=rng.normal(size=len(q))
        a,_=issue_forecasts(q,10)
        q.loc[q.terminal_execution_time_utc>=pd.Timestamp('2024-02-01'),'target_compression_bps']=100000
        b,_=issue_forecasts(q,10)
        pd.testing.assert_series_equal(a.predicted_compression_bps,b.predicted_compression_bps)

    def test_stress_encloses_central_and_unknown_access(self):
        from types import SimpleNamespace
        day=pd.Timestamp('2026-06-25')
        panel=pd.DataFrame({'ptax':[5.], 'signal_usdtusd':[1.], 'signal_premium':[150.]},index=[day])
        row=SimpleNamespace(horizon=10,origin=day,method='example',predicted_compression_bps=80.,radius_bps=10.)
        c=stress_card(row,panel)
        self.assertLessEqual(c['stress_min_budget_bps'],c['budget_lo_bps'])
        self.assertGreaterEqual(c['stress_max_budget_bps'],c['budget_hi_bps'])
        self.assertEqual(c['stress_actionable_signal'],'insufficient_evidence')


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--test-only',action='store_true');args=ap.parse_args()
    suite=unittest.TestSuite([unittest.defaultTestLoader.loadTestsFromTestCase(v1.Tests),unittest.defaultTestLoader.loadTestsFromTestCase(Tests)])
    result=unittest.TextTestRunner().run(suite)
    if not result.wasSuccessful():raise SystemExit(1)
    if not args.test_only:run()
