"""P3-38: buyer cost frontier. Inputs: frozen P1-02 daily CSV; spec in task.
Outputs: P3-38 tables, PNG and audit JSON. Run python scripts/p3_38_buyer_frontier.py
or --test-only. Hypothetical ideal forward; no historical execution claim.
"""
from pathlib import Path
import argparse
import hashlib
import itertools
import json
import math
import unittest
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT/'data/processed/P1-02_premium_daily.csv'
TAB, FIG = ROOT/'results/tables', ROOT/'results/figures'

def gate(access, trade_day, settlement_lag, deadline):
    if access not in (True, False, None):
        raise ValueError('Access must be True, False or None')
    if any(type(v) is not int or v < 0 for v in (trade_day, settlement_lag, deadline)):
        raise ValueError('Nonnegative integer days required')
    if access is False:
        return 'unavailable'
    if access is None:
        return 'unresolved_access'
    return 'late_delivery' if trade_day + settlement_lag > deadline else 'eligible'

def budget(h, x0=5., u0=1., p0=184.35, x1=5., u1=1., p1=184.35,
           deposit=.10, forward_brl=.10, forward_usd=.05, held_yield=0.,
           fee_now=.001, fee_wait=.001, fixed_now=0., fixed_wait=0., q=100000.):
    """Return max additional terminal BRL cost of waiting vs buying now.
    No forward fee/funding charge included: those consume the returned budget.
    Both alternatives deliver q USDT at h; held_yield is hypothetical USDT-unit yield.
    Fixed notional is the initial full-q USD conversion cost; residual remains.
    """
    vals=(x0,u0,p0,x1,u1,p1,deposit,forward_brl,forward_usd,held_yield,
          fee_now,fee_wait,fixed_now,fixed_wait,q)
    if not all(math.isfinite(v) for v in vals):
        raise ValueError('Finite inputs required')
    if type(h) is not int or h < 0 or min(x0,u0,x1,u1,q)<=0:
        raise ValueError('Invalid horizon or prices/quantity')
    if min(p0,p1)<=-10000 or min(deposit,forward_brl,forward_usd,held_yield)<=-1:
        raise ValueError('Invalid premium or annual rate')
    if not (0<=fee_now<1 and 0<=fee_wait<1) or min(fixed_now,fixed_wait)<0:
        raise ValueError('Invalid transaction costs')
    t=h/252
    initial=q/(1+held_yield)**t*x0*u0*(1+p0/10000)*(1+fee_now)+fixed_now
    terminal_now=initial*(1+deposit)**t
    forward=x0*((1+forward_brl)/(1+forward_usd))**t
    n=q*u0*(1+p0/10000)*(1+fee_now)
    conversion=q*x1*u1*(1+p1/10000)*(1+fee_wait)+fixed_wait
    payoff=n*(x1-forward)
    k=terminal_now-conversion+payoff
    return dict(initial_outlay_brl=initial, buy_now_terminal_brl=terminal_now,
                wait_conversion_brl=conversion, hedge_payoff_brl=payoff,
                forward_brl_per_usd=forward, hedge_usd_notional=n,
                max_additional_cost_brl=k, max_additional_cost_bps=k/initial*10000)

def rank(k, lo, hi, eligibility):
    if eligibility!='eligible': return eligibility
    if k<lo: return 'waiting_cheaper_across_scenarios'
    if k>hi: return 'buy_now_cheaper_across_scenarios'
    return 'assumption_sensitive_or_equal'

def delivery_decision(now_access, wait_access, deadline, now_lag=0, wait_lag=0):
    """Gate both alternatives before any monetary ranking; unknown is not denial."""
    now=gate(now_access,0,now_lag,deadline)
    wait=gate(wait_access,deadline,wait_lag,deadline)
    return 'eligible' if now==wait=='eligible' else f'no_cost_ranking:now={now};wait={wait}'

class Tests(unittest.TestCase):
    def test_independent_hand_arithmetic(self):
        r=budget(10,x0=5,u0=1,p0=100,x1=5,u1=1,p1=0,deposit=0,forward_brl=0,forward_usd=0,fee_now=0,fee_wait=0)
        self.assertAlmostEqual(r['max_additional_cost_brl'],5000)
        self.assertAlmostEqual(r['max_additional_cost_bps'],100/1.01)
    def test_zero_and_equal(self):
        self.assertAlmostEqual(budget(0)['max_additional_cost_brl'],0)
    def test_rate_gap(self):
        a=budget(20); b=budget(20,deposit=0)
        self.assertEqual(a['forward_brl_per_usd'],b['forward_brl_per_usd'])
        self.assertLess(b['max_additional_cost_brl'],a['max_additional_cost_brl'])
    def test_cost_and_yield(self):
        a=budget(20); b=budget(20,fixed_wait=100)
        self.assertAlmostEqual(a['max_additional_cost_brl']-b['max_additional_cost_brl'],100)
        self.assertLess(budget(20,held_yield=.04)['max_additional_cost_brl'],a['max_additional_cost_brl'])
    def test_premium_and_fx(self):
        a=budget(20,p1=0); b=budget(20,p1=200)
        self.assertGreater(a['max_additional_cost_brl'],b['max_additional_cost_brl'])
        # Hedge offsets FX exactly only when USD conversion exposure is unchanged.
        self.assertAlmostEqual(budget(10,x1=4)['max_additional_cost_brl'],budget(10,x1=6)['max_additional_cost_brl'])
        self.assertNotAlmostEqual(budget(10,x1=4,p1=0)['max_additional_cost_brl'],budget(10,x1=6,p1=0)['max_additional_cost_brl'])
    def test_deadline_and_access(self):
        self.assertEqual(gate(True,9,1,10),'eligible')
        self.assertEqual(gate(True,10,1,10),'late_delivery')
        self.assertEqual(gate(None,10,0,10),'unresolved_access')
        self.assertEqual(gate(False,10,0,10),'unavailable')
    def test_invalid(self):
        for kw in ({'x1':float('nan')},{'deposit':-1},{'fee_wait':1},{'q':0}):
            with self.assertRaises(ValueError): budget(10,**kw)
    def test_two_alternative_delivery(self):
        self.assertEqual(delivery_decision(True,True,10),'eligible')
        self.assertIn('unresolved_access',delivery_decision(None,True,10))
        self.assertIn('late_delivery',delivery_decision(True,True,10,wait_lag=1))
    def test_threshold_and_gate(self):
        self.assertEqual(rank(5,10,20,'eligible'),'waiting_cheaper_across_scenarios')
        self.assertEqual(rank(15,10,20,'eligible'),'assumption_sensitive_or_equal')
        self.assertEqual(rank(25,10,20,'eligible'),'buy_now_cheaper_across_scenarios')
        self.assertEqual(rank(0,10,20,'unresolved_access'),'unresolved_access')
    def test_prior_default(self):
        from p3_31_holder import b3_hedged_buyer
        old=b3_hedged_buyer(100000,5,1,184.35,5,1,40,20,hedge_fee_bps=0)
        self.assertAlmostEqual(old['savings_brl'],budget(20,p1=40)['max_additional_cost_brl'])

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--test-only',action='store_true'); args=ap.parse_args()
    result=unittest.TextTestRunner().run(unittest.defaultTestLoader.loadTestsFromTestCase(Tests))
    if not result.wasSuccessful(): raise SystemExit(1)
    if args.test_only: return
    TAB.mkdir(parents=True,exist_ok=True); FIG.mkdir(parents=True,exist_ok=True)
    d=pd.read_csv(INPUT,parse_dates=['date_brt']).set_index('date_brt')
    w=d.loc['2026-06-25':].iloc[:21]
    if len(w)!=21 or not w.index.is_unique: raise ValueError('Incomplete historical window')
    cols=['ptax_sell_brl_per_usd','usdtusd_window_usd','premium_bps','usdtbrl_window_brl']
    if not np.isfinite(w[cols].to_numpy()).all(): raise ValueError('Missing input prices')
    if not np.allclose(w[cols[0]]*w[cols[1]]*(1+w.premium_bps/10000),w[cols[3]]): raise ValueError('Price decomposition mismatch')
    x0,u0,p0=map(float,w.iloc[0][cols[:3]])
    base=dict(x0=x0,u0=u0,p0=p0,x1=x0,u1=u0)
    shocks=np.linspace(-100,250,141)
    scenarios=list(itertools.product((0,.05,.10),(0,.04),(.995,1,1.005),(.98,1,1.02),(.001,.003),(0,100)))
    bounds=[]; historical=[]; grid=[]
    fig,axs=plt.subplots(1,3,figsize=(15,6),sharey=True)
    colors=['#dbe6ef','#f2d7a0','#b9d9ca']
    from matplotlib.colors import ListedColormap
    for h,ax in zip((5,10,20),axs):
        lo=[]; hi=[]; mid=[]
        for compression in shocks:
            values=[budget(h,**{**base,'x1':x0*fx,'u1':u0*uf},p1=p0-compression,deposit=dep,held_yield=yld,fee_wait=fw,fixed_wait=fixed)['max_additional_cost_bps'] for dep,yld,uf,fx,fw,fixed in scenarios]
            a,b=min(values),max(values); c=budget(h,**base,p1=p0-compression)['max_additional_cost_bps']
            lo.append(a);hi.append(b);mid.append(c)
            bounds.append(dict(horizon_ptax_days=h,compression_bps=compression,min_budget_bps=a,base_budget_bps=c,max_budget_bps=b))
            for cost in (0,25,50,100,200,300):
                grid.append(dict(horizon_ptax_days=h,compression_bps=compression,additional_terminal_cost_bps=cost,classification=rank(cost,a,b,'eligible'),actual_access='unresolved'))
        yy=np.linspace(0,300,151); z=np.where(yy[:,None]<np.array(lo),2,np.where(yy[:,None]>np.array(hi),0,1))
        ax.pcolormesh(shocks,yy,z,cmap=ListedColormap(colors),vmin=0,vmax=2,shading='nearest')
        ax.plot(shocks,mid,color='#182d46',lw=2,label='Cenário central')
        ax.plot(shocks,lo,'--',color='#4c575f',lw=1);ax.plot(shocks,hi,'--',color='#4c575f',lw=1)
        last=w.iloc[h]
        actual=budget(h,x0=x0,u0=u0,p0=p0,x1=float(last[cols[0]]),u1=float(last[cols[1]]),p1=float(last.premium_bps))
        comp=p0-float(last.premium_bps)
        envelope=[budget(h,**{**base,'x1':x0*fx,'u1':u0*uf},p1=p0-comp,deposit=dep,held_yield=yld,fee_wait=fw,fixed_wait=fixed)['max_additional_cost_bps'] for dep,yld,uf,fx,fw,fixed in scenarios]
        ax.scatter([comp],[actual['max_additional_cost_bps']],marker='D',color='#9c3f20',s=35,zorder=5)
        ax.set(title=f'Prazo: {h} dias PTAX',xlabel='Compressão do prêmio (pb)\ninicial − final',xlim=(-100,250),ylim=(0,300))
        ax.grid(alpha=.15)
        historical.append(dict(horizon_ptax_days=h,start=str(w.index[0].date()),deadline=str(w.index[h].date()),compression_bps=comp,**actual,stress_min_ceiling_bps=min(envelope),stress_max_ceiling_bps=max(envelope),zero_extra_cost_conditional_rank=rank(0,min(envelope),max(envelope),'eligible'),actual_decision=delivery_decision(None,None,h),access='unresolved',settlement='same-day assumed',interpretation='retrospective indicative ceiling; additional cost not observed'))
    axs[0].set_ylabel('Custo adicional terminal de esperar (pb)\nbase: desembolso inicial da compra imediata')
    from matplotlib.patches import Patch
    from matplotlib.lines import Line2D
    fig.legend(handles=[Patch(color=colors[2],label='Esperar custa menos em todos os cenários'),Patch(color=colors[1],label='Depende das hipóteses / empate'),Patch(color=colors[0],label='Comprar agora custa menos em todos os cenários'),Line2D([0],[0],color='#182d46',label='Fronteira central'),Line2D([0],[0],marker='D',color='w',markerfacecolor='#9c3f20',label='Junho: teto retrospectivo')],loc='lower center',ncol=2,fontsize=9,bbox_to_anchor=(.5,.055))
    fig.suptitle('Quanto custo adicional a espera suporta?',fontsize=17,fontweight='bold')
    fig.text(.5,.01,'100 mil USDT; termo ideal, não réplica WDO; juros e custos hipotéticos. Faixas = cenários, não probabilidades.\nCores condicionais à rota disponível e entrega no prazo; acesso real não verificado. K exclui taxas de conversão já contabilizadas.',ha='center',fontsize=9)
    fig.tight_layout(rect=(0,.25,1,.93));fig.savefig(FIG/'P3-38_buyer_frontier.png',dpi=180);plt.close(fig)
    pd.DataFrame(bounds).to_csv(TAB/'P3-38_frontier.csv',index=False)
    pd.DataFrame(grid).to_csv(TAB/'P3-38_classification.csv',index=False)
    pd.DataFrame(historical).to_csv(TAB/'P3-38_june_ceiling.csv',index=False)
    pd.DataFrame([dict(scenario_id=i,deposit=dep,held_yield=yld,terminal_usdtusd_factor=uf,terminal_fx_factor=fx,fee_wait=fw,fixed_wait=fixed,forward_brl=.10,forward_usd=.05) for i,(dep,yld,uf,fx,fw,fixed) in enumerate(scenarios)]).to_csv(TAB/'P3-38_scenarios.csv',index=False)
    checks=[dict(access=a,trade_day=t,lag=l,deadline=10,result=gate(a,t,l,10)) for a in (True,False,None) for t,l in ((10,0),(10,1),(9,1))]
    pd.DataFrame(checks).to_csv(TAB/'P3-38_delivery_gate.csv',index=False)
    (TAB/'P3-38_audit.json').write_text(json.dumps(dict(input_sha256=hashlib.sha256(INPUT.read_bytes()).hexdigest(),tests=result.testsRun,scenario_count=len(scenarios),calendar='observed PTAX dates; assumed common settlement calendar',hedge='ideal maturity-matched forward, not WDO replication',selection='known June episode, retrospective',actual_access='unresolved',cost_denominator='initial buy-now BRL outlay',bounds='user-specified stress envelope; no probabilities'),indent=2),encoding='utf-8')
    print(pd.DataFrame(historical)[['horizon_ptax_days','compression_bps','max_additional_cost_bps','max_additional_cost_brl']].to_string(index=False))

if __name__=='__main__': main()
