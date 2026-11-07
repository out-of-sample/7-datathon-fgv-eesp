"""P3-30: locked retrospective duration census and feasibility gate.
Inputs: frozen P1-02/P1-05 processed CSVs. Outputs: P3-30 tables only.
Run: python scripts/p3_30_duration.py [--test]
Does not overwrite frozen research. See task specification before changing rules.
"""
from pathlib import Path
import hashlib, json, sys
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'results/tables'

def extract(s, threshold=3):
    rows=[]; active=None; history=[]; streak=0
    for date, value in s.items():
        if not np.isfinite(value):
            if active is not None:
                active.update(event=0, end=last, reason='missing_observation')
                rows.append(active); active=None
            history=[]; streak=0
            continue
        if active is None and len(history)>=60:
            reference=np.array(history[-60:]); median=float(np.median(reference))
            sigma=float(1.4826*np.median(np.abs(reference-median)))
            if sigma>0 and value>median+threshold*sigma:
                active=dict(start=date, median_bps=median, sigma_bps=sigma,
                            initial_excess_bps=float(value-median), duration=0)
                streak=0
        elif active is not None:
            active['duration']+=1
            streak=streak+1 if abs(value-active['median_bps'])<=active['sigma_bps'] else 0
            if streak==5:
                active.update(event=1,end=date,reason='five_in_band')
                rows.append(active); active=None; streak=0
        history.append(float(value)); last=date
    if active is not None:
        active.update(event=0,end=last,reason='sample_end'); rows.append(active)
    return rows

def km(rows,horizon,age=0):
    """Conditional recovery probability; undefined beyond observed risk support."""
    if not rows or max(r['duration'] for r in rows)<age+horizon:
        return np.nan
    surv=1.; initial=1.
    for t in sorted(set(r['duration'] for r in rows)):
        risk=sum(r['duration']>=t for r in rows)
        events=sum(r['duration']==t and r['event']==1 for r in rows)
        if t<=age: initial*=1-events/risk
        if t<=age+horizon: surv*=1-events/risk
    return 1-surv/initial if initial>0 else np.nan

def tests():
    idx=pd.bdate_range('2020-01-01',periods=90)
    base=([0.,1.,-1.]*20)
    s=pd.Series(base+[10.]*10+[0.]*20,index=idx)
    r=extract(s); assert len(r)==1 and r[0]['duration']==14 and r[0]['event']==1
    truncated=extract(s.iloc[:70]); assert truncated[0]['event']==0 and truncated[0]['duration']==9
    broken=s.copy(); broken.iloc[72]=np.nan
    r=extract(broken); assert r[0]['event']==0 and r[0]['reason']=='missing_observation'
    flat=pd.Series([0.]*60+[100.]*30,index=idx); assert extract(flat)==[]
    prefix=extract(s.iloc[:70]); altered=s.copy(); altered.iloc[70:]=10000
    assert prefix==extract(altered.iloc[:70])
    assert km([dict(duration=5,event=1),dict(duration=10,event=0)],5)==0.5
    assert np.isnan(km([dict(duration=5,event=1)],10))
    below=pd.Series(base+[10.]*10+[-10.]*20,index=idx)
    assert extract(below)[0]['event']==0 # overshoot is not frozen-band recovery
    return 8

def main():
    ntests=tests()
    if '--test' in sys.argv:
        print(f'{ntests} duration checks passed'); return
    OUT.mkdir(exist_ok=True,parents=True)
    sources=['data/processed/P1-02_premium_daily.csv','data/processed/P1-05_donor_premiums_daily.csv']
    provenance={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in sources}
    br=pd.read_csv(ROOT/sources[0],parse_dates=['date_brt']).set_index('date_brt')
    donor=pd.read_csv(ROOT/sources[1],parse_dates=['date']).set_index('date')
    assert br.index.is_unique and donor.index.is_unique
    br=br.sort_index(); donor=donor.sort_index()
    panel=pd.DataFrame({'BRL':br.premium_bps})
    for c in ['EUR','TRY','ZAR','MXN','COP']: panel[c]=donor[c].reindex(panel.index)
    audits=[]; episodes=[]; gates=[]; descriptive=[]
    for c in panel:
        valid=panel[c].dropna()
        audits.append(dict(currency=c,rows=len(panel),valid=len(valid),missing=int(panel[c].isna().sum()),
                           first=str(valid.index.min().date()),last=str(valid.index.max().date()),
                           eligibility='primary' if c=='BRL' else 'descriptive_only_historical_regimes_not_audited'))
        for k in [3,2,4]:
            rows=extract(panel[c],k)
            for i,r in enumerate(rows):
                episodes.append(dict(currency=c,threshold=k,episode_id=f'{c}-{k}-{i+1}',**r))
            if c!='BRL': continue
            # Re-extraction at cutoff prevents later recoveries changing training labels.
            train=extract(panel[c].loc[:'2024-12-31'],k)
            val=[r for r in extract(panel[c].loc[:'2025-12-31'],k) if r['start'].year==2025]
            test=[r for r in rows if r['start'].year==2026]
            splits={'train':train,'validation':val,'test':test}
            passed=True; reasons=[]
            for name,rs in splits.items():
                events=sum(r['event'] for r in rs)
                min_n,min_e=(10,5) if name=='train' else (5,2)
                good=len(rs)>=min_n and events>=min_e
                if not good: reasons.append(f'{name}: {len(rs)} episodes/{events} recoveries; floor {min_n}/{min_e}')
                passed &= good
                gates.append(dict(threshold=k,split=name,episodes=len(rs),recoveries=events,
                                  censored=len(rs)-events,minimum_episodes=min_n,minimum_recoveries=min_e,passed=good))
                for age in [0,5,10]:
                    for h in [5,10,20]:
                        descriptive.append(dict(threshold=k,split=name,age_ptax_days=age,horizon_ptax_days=h,
                            km_recovery_probability=km(rs,h,age),at_risk_at_age=sum(r['duration']>age for r in rs)))
            if passed:
                raise RuntimeError('Feasibility passed: implement locked hazard/IPCW evaluation before claiming completed analysis.')
    ep=pd.DataFrame(episodes)
    # Descriptive dependency clusters only: transitive <=10 PTAX-day onset proximity.
    ep['dependency_group']=''
    for k in [3,2,4]:
        group=0; previous=-100
        for row in ep[ep.threshold==k].sort_values('start').itertuples():
            pos=panel.index.get_loc(row.start)
            if pos-previous>10: group+=1
            ep.loc[row.Index,'dependency_group']=f'k{k}-g{group}'
            previous=pos
    ep.to_csv(OUT/'P3-30_episodes.csv',index=False)
    pd.DataFrame(audits).to_csv(OUT/'P3-30_input_audit.csv',index=False)
    pd.DataFrame(gates).to_csv(OUT/'P3-30_feasibility.csv',index=False)
    pd.DataFrame(descriptive).to_csv(OUT/'P3-30_descriptive_km.csv',index=False)
    counts=ep.groupby(['threshold','currency']).agg(episodes=('event','size'),recoveries=('event','sum'))
    counts=counts.reindex(pd.MultiIndex.from_product([[2,3,4],panel.columns],names=['threshold','currency']),fill_value=0).reset_index()
    counts.to_csv(OUT/'P3-30_census.csv',index=False)
    summary=dict(status='predictive_validation_unavailable',reason='Locked episode/recovery feasibility floor fails',
                 tests_passed=ntests,input_sha256=provenance,model_fitted=False,
                 caveats=['PTAX observation calendar; foreign missing days censor episodes',
                          'Donor full-history regime/source-change audit not complete; descriptive only',
                          'Strict return to frozen band excludes downward overshoots',
                          'KM is descriptive; random independent censoring is unverified',
                          'No predictive Brier score, calibration or profitable strategy established'])
    (OUT/'P3-30_run_summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
    print(pd.DataFrame(gates).to_string(index=False)); print(counts.to_string(index=False))
    print(json.dumps(summary,indent=2))

if __name__=='__main__': main()
