"""P5-12: mentor feedback charts, using existing frozen data (no downloads).

Run: python scripts/p5_12_mentor_charts.py
Requires pandas, numpy, matplotlib. Inputs: P1-02/P1-05 daily CSVs and P3-46 table.
Outputs: results/figures/P5-12_*.png and .svg; results/tables/P5-12_*.csv/json.
Daily historical charts retain all observations, including negatives and extremes.
Cross-country charts are descriptive, using each market's own reference fixing.
"""
from pathlib import Path
import json
import hashlib
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

ROOT = Path(__file__).resolve().parents[1]
FIG, TAB = ROOT/'results/figures', ROOT/'results/tables'
BG, INK, MUTED, GRID = '#F6F4EF', '#14213D', '#5B6573', '#DDD7CC'
BLUE, ORANGE, GOLD = '#3B6EA8', '#D9622B', '#9A7627'
plt.rcParams.update({'font.family':'DejaVu Sans', 'font.size':15,
    'figure.facecolor':BG, 'axes.facecolor':BG, 'text.color':INK,
    'axes.labelcolor':MUTED, 'xtick.color':MUTED, 'ytick.color':MUTED,
    'axes.spines.top':False, 'axes.spines.right':False,
    'axes.spines.left':False, 'axes.edgecolor':GRID, 'svg.fonttype':'none'})

def br(v, n=2):
    return f'{v:.{n}f}'.replace('.', ',').replace('-', '−')

def canvas(title, subtitle, note):
    f, ax = plt.subplots(figsize=(16,8), dpi=200)
    f.subplots_adjust(left=.085, right=.96, bottom=.22, top=.78)
    f.text(.085,.925,title,fontsize=25,weight='bold')
    f.text(.085,.865,subtitle,fontsize=14,color=MUTED)
    f.text(.085,.065,note,fontsize=11,color=MUTED,style='italic',linespacing=1.6)
    ax.grid(axis='y',color=GRID,lw=.7)
    ax.set_axisbelow(True)
    ax.axhline(0,color=INK,lw=1)
    ax.tick_params(length=0,pad=10)
    return f,ax

def save(f,name):
    for ext in ('png','svg'):
        f.savefig(FIG/f'P5-12_{name}.{ext}', dpi=200,facecolor=BG)
    plt.close(f)

paths = [ROOT/'data/processed/P1-02_premium_daily.csv',
         ROOT/'data/processed/P1-05_donor_premiums_daily.csv',
         TAB/'P3-46_country_direct_comparison.csv']
d = pd.read_csv(paths[0],parse_dates=['date_brt']).set_index('date_brt')
q = pd.read_csv(paths[1],parse_dates=['date']).set_index('date')
t = pd.read_csv(paths[2]).set_index('currency')
assert d.index.is_unique and q.index.is_unique
assert d[['premium_bps','premium_unadj_bps']].notna().all().all()
np.testing.assert_allclose(d.premium_bps,(d.usdtbrl_window_brl/(d.ptax_sell_brl_per_usd*d.usdtusd_window_usd)-1)*10000,atol=1e-8)
np.testing.assert_allclose(d.premium_unadj_bps,(d.usdtbrl_window_brl/d.ptax_sell_brl_per_usd-1)*10000,atol=1e-8)
stats = {'inputs_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
         'first':str(d.index.min().date()),'last':str(d.index.max().date()),'days':len(d),
         'incomplete_windows':int((d.window_hours!=4).sum()),
         'uncertain_windows':int(d.ptax_window_uncertain.sum())}

# Main definition matches the deck. Literal price/PTAX companion answers the mentor's wording.
for col,name,adj in [('premium_bps','01_premio_historico',True),('premium_unadj_bps','01b_premio_ptax_direto',False)]:
    s = d[col]/100
    stats[col] = {'negative_days':int((s<0).sum()),'negative_share_pct':float((s<0).mean()*100),
                  'min_pct':float(s.min()),'min_date':str(s.idxmin().date()),
                  'max_pct':float(s.max()),'max_date':str(s.idxmax().date())}
    formula = 'USDT/BRL ÷ (PTAX venda × USDT/USD) − 1' if adj else 'USDT/BRL ÷ PTAX venda − 1'
    f, ax = canvas('Prêmio do dólar digital sobre a PTAX desde 2020',
        'Binance • 13/out/2020 a 30/out/2026 • 1.520 dias com PTAX • valores em %',
        f'Fontes: Binance e BCB. {formula}. Média dos preços nas horas de consulta da PTAX.\n'
        'Linha diária completa, sem cortar picos ou valores negativos. A PTAX é referência, não uma oferta de câmbio executável.')
    ax.plot(s.index,s,color=BLUE,lw=.8,alpha=.55,label='Diário')
    ax.plot(s.index,s.rolling(20,min_periods=20).mean(),color=INK,lw=2,label='Média móvel de 20 dias observados')
    event = s.loc['2026-06-24':'2026-07-21']
    ax.plot(event.index,event,color=ORANGE,lw=1.8,label='24/jun–21/jul/2026')
    ax.set_ylim(s.min()-.38,s.max()+.45)
    ax.set_xlim(s.index.min(),s.index.max())
    ticks = [s.index.min()]+[pd.Timestamp(f'{y}-01-01') for y in range(2022,2027)]+[s.index.max()]
    ax.set_xticks(ticks,['out/2020','2022','2023','2024','2025','2026','out/2026'])
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v,_:br(v,1)+'%'))
    ax.legend(loc='upper center',bbox_to_anchor=(.5,1.18),frameon=False,ncol=3,fontsize=12)
    for date,dy in [(s.idxmax(),.3),(s.idxmin(),-.3)]:
        ax.scatter(date,s.loc[date],color=INK,s=23,zorder=5)
        ax.annotate(f'{br(s.loc[date])}% em {date:%d/%m/%Y}',(date,s.loc[date]),
                    xytext=(date,s.loc[date]+dy),ha='center',fontsize=11,color=INK)
    save(f,name)

# Common calendar window, but each currency keeps its observed dates and own fix.
view = q.loc['2026-01-01':'2026-09-30',['BRL_ptax','EUR','MXN']]/100
view.to_csv(TAB/'P5-12_country_daily_pct.csv')
f,ax = canvas('Brasil, euro e peso mexicano: o prêmio em 2026',
    'USDT sobre o dólar oficial de cada mercado • média móvel de 5 observações • valores em %',
    'Fontes: Binance, BCB (Brasil) e BCE (euro e México). Prêmios ajustados por USDT/USD; horários dos fixings diferem.\n'
    'Comparação descritiva. A faixa destaca 24/jun–21/jul; médias móveis suavizam picos. Não é uma nova estimativa causal.')
ax.axvspan(pd.Timestamp('2026-06-24'),pd.Timestamp('2026-07-21'),color=ORANGE,alpha=.10)
for c,label,color,ls in [('BRL_ptax','Brasil (BRL)',ORANGE,'-'),('EUR','Zona do euro (EUR)',BLUE,'--'),('MXN','México (MXN)',GOLD,'-.')]:
    s = view[c].dropna().rolling(5).mean()
    ax.plot(s.index,s,color=color,lw=2.3,ls=ls,label=label)
ax.set_xlim(view.index.min(),view.index.max())
ax.set_xticks(pd.to_datetime(['2026-01-02','2026-03-01','2026-05-01','2026-07-01','2026-09-30']),['02/jan','mar','mai','jul','30/set'])
ax.yaxis.set_major_formatter(FuncFormatter(lambda v,_:br(v,1)+'%'))
ax.legend(loc='upper center',bbox_to_anchor=(.5,1.17),ncol=3,frameon=False)
save(f,'02_brasil_euro_peso')

# Before-after differences use each market's own days, exactly as F-053.
windows = [('2026-05-25','2026-06-22'),('2026-06-24','2026-07-21')]
rows=[]
for currency,code in [('BRL','BRL_ptax'),('EUR','EUR'),('MXN','MXN')]:
    raw = d.premium_bps if currency=='BRL' else q[code]
    pre,post=[raw.loc[a:b].dropna() for a,b in windows]
    delta=post.mean()-pre.mean()
    assert abs(delta-t.loc[currency,'usdt_premium_change_bps'])<.02
    rows.append({'currency':currency,'before_bps':pre.mean(),'after_bps':post.mean(),
                 'change_bps':delta,'days_before':len(pre),'days_after':len(post)})
out=pd.DataFrame(rows).set_index('currency')
out.to_csv(TAB/'P5-12_country_before_after.csv')
f,ax=canvas('A alta do prêmio se concentrou no Brasil',
    'Variação do prêmio médio após 23/jun/2026 • pontos-base (100 bps = 1%)',
    'Fontes: Binance, BCB e BCE. Depois: 24/jun–21/jul; antes: 25/mai–22/jun. Média depois menos média antes.\n'
    'Brasil: 20/20 observações; euro e México: 21/20. Comparação descritiva, sem teste de significância adicional.')
f.subplots_adjust(left=.24)
ax.lines[0].remove()  # horizontal zero guide belongs to the line charts, not bar categories
ax.grid(False)
ax.grid(axis='x',color=GRID,lw=.7)
ax.axvline(0,color=INK,lw=1)
vals=out.change_bps.values
ax.barh([2,1,0],vals,color=[ORANGE,BLUE,GOLD],height=.5)
for y,v in zip([2,1,0],vals):
    ax.text(v+(2 if v>=0 else -2),y,('+' if v>=0 else '')+br(v,1)+' bps',ha='left' if v>=0 else 'right',va='center',weight='bold',fontsize=21)
ax.set_yticks([2,1,0],['Brasil (BRL)','Zona do euro (EUR)','México (MXN)'])
ax.set_xlim(-40,125)
ax.set_ylim(-.6,2.6)
ax.set_xlabel('Variação do prêmio (bps)')
save(f,'03_variacao_por_moeda')

d[['premium_bps','premium_unadj_bps','window_hours','ptax_window_uncertain']].to_csv(TAB/'P5-12_historical_daily.csv')
(TAB/'P5-12_checks.json').write_text(json.dumps(stats,indent=2,ensure_ascii=False),encoding='utf-8')
print(json.dumps(stats,indent=2,ensure_ascii=False))
print(out.to_string())
