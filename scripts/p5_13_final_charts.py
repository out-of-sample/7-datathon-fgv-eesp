"""P5-13: four slide-ready charts matching the current PDF palette.
Run: python scripts/p5_13_final_charts.py
Requires pandas, numpy, matplotlib. Optional DECK_FONT_DIR with IBM Plex Sans TTFs.
Inputs: frozen P1-02 premium, P3-03 monitor, P3-01 cost and P3-25 composition CSVs.
Outputs: results/figures/P5-13_*.png/.svg (transparent), source CSVs/checks JSON.
No model fitting or source downloads. Network range is benchmark fees, not uncertainty.
"""
from pathlib import Path
import os, json, hashlib
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.ticker import FuncFormatter

ROOT=Path(__file__).resolve().parents[1]
FIG,TAB=ROOT/'results/figures',ROOT/'results/tables'
BLUE,ORANGE,INK,MUTED,GRID='#3B6EA8','#D9622B','#14213D','#5B6573','#DDD7CC'
font='DejaVu Sans'
if os.environ.get('DECK_FONT_DIR'):
    for path in Path(os.environ['DECK_FONT_DIR']).glob('*.ttf'):
        fm.fontManager.addfont(str(path))
    font='IBM Plex Sans'
plt.rcParams.update({'font.family':font,'font.size':17,'text.color':INK,
    'axes.labelcolor':MUTED,'xtick.color':MUTED,'ytick.color':INK,
    'axes.edgecolor':GRID,'axes.spines.top':False,'axes.spines.right':False,
    'axes.spines.left':False,'svg.fonttype':'path','savefig.transparent':True})

def br(v,n=1): return f'{v:.{n}f}'.replace('.',',').replace('-','−')
def save(f,name):
    for ext in ('png','svg'):
        f.savefig(FIG/f'P5-13_{name}.{ext}',dpi=240,transparent=True)
    plt.close(f)

paths=[ROOT/'data/processed/P1-02_premium_daily.csv',
       ROOT/'data/processed/P3-03_monitor_daily.csv',TAB/'P3-01_route_costs.csv',TAB/'P3-25_composition.csv']
d=pd.read_csv(paths[0],parse_dates=['date_brt']).set_index('date_brt')
m=pd.read_csv(paths[1],parse_dates=['date']).set_index('date')
cost=pd.read_csv(paths[2]).set_index('route_id')
share=pd.read_csv(paths[3]).set_index('period')
assert d.index.is_unique and m.index.is_unique
before=d.loc['2026-05-25':'2026-06-22','premium_bps']
after=d.loc['2026-06-24':'2026-07-21','premium_bps']
delta=after.mean()-before.mean()
assert len(before)==len(after)==20 and abs(delta-93.9073)<.001
assert abs(delta-cost.loc['NOTICE_COST_SPIKE','premium_bps'])<.02
netlo=float(cost.loc['USDT_REGIME_5','wire_or_onchain_bps'])
nethi=float(cost.loc['USDT_REGIME_6_FOXBIT','wire_or_onchain_bps'])
assert (netlo,nethi)==(.1,.2)
np.testing.assert_allclose(share.foxbit_share_pct,100*share.foxbit_volume_usdt/(share.binance_volume_usdt+share.foxbit_volume_usdt+share.mb_volume_usdt),atol=1e-5)

# Slide 9: operational signal, not a forecast. End at first triggered day to avoid
# presenting the mechanical post-alarm reset as a market normalization.
event=pd.Timestamp('2026-06-24')
monitor=m.loc['2026-05-04':event,['cusum_pos','h','alarm']].copy()
monitor['signal_over_threshold']=monitor.cusum_pos/monitor.h
assert monitor.loc[event,'alarm']==1 and monitor.loc[event,'signal_over_threshold']>1
assert (monitor.loc[:'2026-06-23','signal_over_threshold']<1).all()
monitor.to_csv(TAB/'P5-13_cusum_source.csv')
f,ax=plt.subplots(figsize=(16,3.8),dpi=240)
f.subplots_adjust(left=.065,right=.97,bottom=.24,top=.79)
f.text(.065,.90,'O alarme identificou o salto em 24/jun',fontsize=23,weight='bold')
f.text(.065,.055,'Sinal acumulado / limite de disparo. Cálculo somente com dados disponíveis em cada dia.',fontsize=14,color=MUTED)
ax.plot(monitor.index,monitor.signal_over_threshold,color=BLUE,lw=2.6)
last=monitor.iloc[-2:]
ax.plot(last.index,last.signal_over_threshold,color=ORANGE,lw=2.8)
ax.axhline(1,color=INK,lw=1.25,ls=(0,(5,4)))
ax.text(pd.Timestamp('2026-05-06'),1.09,'Limite de disparo',fontsize=15,color=INK)
y=float(monitor.loc[event,'signal_over_threshold'])
ax.scatter([event],[y],s=65,color=ORANGE,zorder=5)
ax.annotate('24/jun · alarme',xy=(event,y),xytext=(-18,12),textcoords='offset points',ha='right',va='bottom',color=ORANGE,fontsize=18,weight='bold')
ax.set_ylim(0,3)
ax.set_yticks([0,1,2,3],['0','1×','2×','3×'])
ax.set_xlim(pd.Timestamp('2026-05-04'),pd.Timestamp('2026-06-27'))
ax.set_xticks(pd.to_datetime(['2026-05-04','2026-05-18','2026-06-01','2026-06-15','2026-06-24']),['04/mai','18/mai','01/jun','15/jun','24/jun'])
ax.grid(axis='y',color=GRID,lw=.65)
ax.set_axisbelow(True)
ax.tick_params(length=0,pad=8)
save(f,'09_cusum')

def mini(title,subtitle,foot):
    f,ax=plt.subplots(figsize=(7.6,3.7),dpi=240)
    f.subplots_adjust(left=.27,right=.92,bottom=.24,top=.69)
    f.text(.035,.93,title,fontsize=21,weight='bold')
    f.text(.035,.82,subtitle,fontsize=15,color=MUTED)
    f.text(.035,.045,foot,fontsize=12.5,color=MUTED,style='italic')
    ax.set_ylim(-.65,1.65)
    ax.tick_params(length=0,pad=9)
    ax.spines['bottom'].set_color(GRID)
    ax.axvline(0,color=GRID,lw=.8)
    ax.set_axisbelow(True)
    return f,ax

# Slide 10, first existing column. The event-study baseline, not the longer
# structural-regime mean of 9 bps used elsewhere.
f,ax=mini('Prêmio médio na Binance','Antes e durante o choque · bps',
          'Antes: 25/mai–22/jun · Choque: 24/jun–21/jul/2026')
vals=[before.mean(),after.mean()]
ax.barh([1,0],vals,color=[BLUE,ORANGE],height=.48)
for y,v in zip([1,0],vals): ax.text(v+2,y,br(v),va='center',fontsize=24,weight='bold')
ax.set_yticks([1,0],['Antes','Choque'])
ax.set_xlim(0,139)
ax.set_xticks([0,50,100])
save(f,'10a_premio')

# Slide 10, middle column. Fee bar uses actual 0.1 bps; never inflate its length.
f,ax=mini('Prêmio adicional e taxa de rede','Por US$ 100 mil · mesma escala em bps',
          'Rede: referência de 1–2 USDT por transferência')
ax.barh([1,0],[delta,netlo],color=[ORANGE,MUTED],height=.48)
ax.hlines(0,netlo,nethi,color=MUTED,lw=2)
ax.text(delta+2,1,br(delta),va='center',fontsize=24,weight='bold',color=ORANGE)
ax.text(3,0,'0,1–0,2',va='center',fontsize=22,weight='bold',color=MUTED)
ax.set_yticks([1,0],['Prêmio\nadicional','Taxa\nde rede'])
ax.set_xlim(0,125)
ax.set_xticks([0,50,100])
save(f,'10b_rede')

# Slide 10, third column. Explicitly limited to the three observed exchanges.
f,ax=mini('Fatia da Foxbit no volume','Binance + Foxbit + Mercado Bitcoin',
          'Antes: 1/mai–22/jun · Depois: 22/jul–30/out/2026')
vals=[float(share.loc[k,'foxbit_share_pct']) for k in ('pre','after')]
ax.barh([1,0],vals,color=[BLUE,ORANGE],height=.48)
for y,v in zip([1,0],vals): ax.text(v+.7,y,br(v)+'%',va='center',fontsize=24,weight='bold')
ax.set_yticks([1,0],['Antes','Depois'])
ax.set_xlim(0,46)
ax.set_xticks([0,20,40],['0','20%','40%'])
save(f,'10c_foxbit')

summary=pd.DataFrame([
    {'chart':'10a_premio','category':'Antes','value':before.mean(),'unit':'bps'},
    {'chart':'10a_premio','category':'Choque','value':after.mean(),'unit':'bps'},
    {'chart':'10b_rede','category':'Prêmio adicional','value':delta,'unit':'bps'},
    {'chart':'10b_rede','category':'Taxa de rede mínimo','value':netlo,'unit':'bps'},
    {'chart':'10b_rede','category':'Taxa de rede máximo','value':nethi,'unit':'bps'},
    {'chart':'10c_foxbit','category':'Antes','value':vals[0],'unit':'percent'},
    {'chart':'10c_foxbit','category':'Depois','value':vals[1],'unit':'percent'}])
summary.to_csv(TAB/'P5-13_conclusion_source.csv',index=False)
(TAB/'P5-13_checks.json').write_text(json.dumps({'inputs_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},'font':font,'cusum_event':str(event.date()),'network_range_type':'benchmark fee range, not confidence interval','figure_count':4},indent=2),encoding='utf-8')
print(summary.to_string(index=False))
print('Four PNG/SVG pairs exported; source arithmetic checks passed.')
