"""P3-41: retrospective compression forecasts linked to the buyer cost frontier.
Inputs: frozen P1-02 daily/hourly CSVs; no network or model downloads.
Outputs: results/tables/P3-41_*.csv and audit JSON, results/figures/P3-41_*.png.
Run: python scripts/p3_41_compression.py [--test-only]. Protocol: task P3-41.
Units: premium/compression in bps; budgets in bps of initial BRL outlay.
All prices indicative; funding/forward/cost assumptions hypothetical; access unknown.
"""
from pathlib import Path
import argparse
import hashlib
import json
import unittest

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from p3_38_buyer_frontier import budget, delivery_decision

ROOT = Path(__file__).resolve().parents[1]
DAILY = ROOT / 'data/processed/P1-02_premium_daily.csv'
HOURLY = ROOT / 'data/processed/P1-02_premium_hourly.csv'
TAB, FIG = ROOT / 'results/tables', ROOT / 'results/figures'
FIT_END = pd.Timestamp('2024-06-30 23:59:59')
CAL_END = pd.Timestamp('2024-12-31 23:59:59')
VAL_END = pd.Timestamp('2025-12-31 23:59:59')
HORIZONS = (5, 10, 20)
METHODS = ('persistence', 'mean_reversion', 'ridge')
FEATURES = ['signal_premium', 'daily_premium', 'daily_lag1', 'daily_lag5',
            'signal_change1', 'signal_change5', 'signal_mean5', 'signal_mean20',
            'signal_minus_mean60', 'signal_vol20', 'log_volume24', 'return_vol24']
COLORS = {'persistence': '#777777', 'mean_reversion': '#c48220', 'ridge': '#246ca6'}


def build_panel(d, hourly):
    """Build only backward-looking features; future columns are explicit targets."""
    if not d.index.is_unique or not hourly.index.is_unique:
        raise ValueError('Duplicate input timestamps')
    if not d.index.is_monotonic_increasing or not hourly.index.is_monotonic_increasing:
        raise ValueError('Unsorted input timestamps')
    out = pd.DataFrame(index=d.index)
    out['signal_time_utc'] = d.index + pd.Timedelta(hours=17)
    out['execution_time_utc'] = d.index + pd.Timedelta(hours=18)
    # Publication is stored in naive Brasília time. UTC = Brasília + 3 hours.
    out['ptax_publication_utc'] = pd.to_datetime(d.ptax_published_brt) + pd.Timedelta(hours=3)
    out['ptax'] = d.ptax_sell_brl_per_usd
    close16 = hourly.reindex(d.index + pd.Timedelta(hours=16)).set_axis(d.index)
    open18 = hourly.reindex(d.index + pd.Timedelta(hours=18)).set_axis(d.index)
    out['signal_price'] = close16.usdtbrl_close_brl
    out['signal_usdtusd'] = close16.usdtusd_close_usd
    out['execution_price'] = open18.usdtbrl_open_brl
    out['execution_usdtusd'] = open18.usdtusd_open_usd
    for clock in ('signal', 'execution'):
        out[f'{clock}_premium'] = (out[f'{clock}_price'] /
                                   (out.ptax * out[f'{clock}_usdtusd']) - 1) * 10000
    s = out.signal_premium
    out['daily_premium'] = d.premium_bps
    out['daily_lag1'] = d.premium_bps.shift(1)
    out['daily_lag5'] = d.premium_bps.shift(5)
    out['signal_change1'] = s.diff()
    out['signal_change5'] = s.diff(5)
    for w in (5, 20, 60):
        out[f'signal_mean{w}'] = s.rolling(w).mean()
    out['signal_minus_mean60'] = s - out.signal_mean60
    out['signal_vol20'] = s.diff().rolling(20).std()
    # Reindex to a complete UTC grid: an absent candle cannot disappear inside a 24h window.
    hourgrid = hourly.reindex(pd.date_range(hourly.index.min(), hourly.index.max(), freq='h'))
    volume = hourgrid.usdtbrl_volume_usdt.rolling(24).sum()
    volatility = np.log(hourgrid.usdtbrl_close_brl).diff().rolling(24).std() * 10000
    idx16 = d.index + pd.Timedelta(hours=16)
    out['log_volume24'] = np.log1p(volume.reindex(idx16).to_numpy())
    out['return_vol24'] = volatility.reindex(idx16).to_numpy()
    out['quality_ok'] = (d.window_hours.eq(4) & ~d.ptax_window_uncertain.astype(bool))
    out['publication_ok'] = out.ptax_publication_utc.le(out.signal_time_utc)
    out['features_ok'] = np.isfinite(out[FEATURES].to_numpy()).all(axis=1)
    out['execution_ok'] = np.isfinite(out[['execution_price', 'execution_usdtusd', 'ptax']]).all(axis=1)
    return out


def dataset(panel, horizon):
    q = panel.copy()
    for col in ('execution_premium', 'execution_price', 'execution_usdtusd', 'ptax',
                'execution_time_utc', 'quality_ok', 'publication_ok', 'execution_ok'):
        q['terminal_' + col] = panel[col].shift(-horizon)
    q['target_compression_bps'] = q.signal_premium - q.terminal_execution_premium
    q['origin_eligible'] = q.quality_ok & q.publication_ok & q.features_ok & q.execution_ok
    q['terminal_eligible'] = (q.terminal_quality_ok.eq(True) & q.terminal_publication_ok.eq(True)
                              & q.terminal_execution_ok.eq(True))
    return q


def split_masks(q):
    end = q.terminal_execution_time_utc
    return {'fit': end.le(FIT_END),
            'calibration': (q.index > FIT_END.normalize()) & end.le(CAL_END),
            'validation': (q.index.year == 2025) & end.le(VAL_END),
            'test': (q.index.year == 2026) & end.notna()}


def fit_ridge(x, y, alpha):
    mu, scale = x.mean(axis=0), x.std(axis=0)
    scale = np.where(scale > 1e-10, scale, 1.)
    z = np.column_stack([np.ones(len(x)), (x - mu) / scale])
    penalty = np.eye(z.shape[1]) * alpha
    penalty[0, 0] = 0
    coef = np.linalg.solve(z.T @ z + penalty, z.T @ y)
    return dict(mu=mu, scale=scale, coef=coef)


def predict(q, method, model=None):
    if method == 'persistence':
        return np.zeros(len(q))
    if method == 'mean_reversion':
        return .5 * q.signal_minus_mean60.to_numpy()
    x = q[FEATURES].to_numpy()
    z = np.column_stack([np.ones(len(x)), (x - model['mu']) / model['scale']])
    return z @ model['coef']


def residual_radius(errors, coverage=.90):
    errors = np.abs(np.asarray(errors, float))
    if not len(errors) or not np.isfinite(errors).all():
        raise ValueError('Finite calibration errors required')
    k = min(len(errors), int(np.ceil((len(errors) + 1) * coverage)))
    return float(np.sort(errors)[k - 1])


def conditional_signal(lo_budget, hi_budget, additional_cost):
    if lo_budget > additional_cost:
        return 'waiting_may_compensate'
    if hi_budget < additional_cost:
        return 'buy_now'
    return 'insufficient_evidence'


def assess(p0, compression, radius, h, x0, u0, additional_cost=25.,
           now_access=None, wait_access=None, now_lag=0, wait_lag=0):
    """Ex-ante central scenario, not an executable price or a forecast of FX/U."""
    vals = [p0, compression, radius, x0, u0, additional_cost]
    if not np.isfinite(vals).all() or radius < 0 or additional_cost < 0:
        raise ValueError('Invalid forecast or costs')
    if min(p0 - compression - radius, p0 - compression + radius) <= -10000:
        raise ValueError('Forecast implies nonpositive USDT price')
    def ceiling(c):
        return budget(h, x0=x0, u0=u0, p0=p0, x1=x0, u1=u0,
                      p1=p0-c)['max_additional_cost_bps']
    center, lo, hi = ceiling(compression), ceiling(compression-radius), ceiling(compression+radius)
    base, slope = ceiling(0), ceiling(1)-ceiling(0)
    eligibility = delivery_decision(now_access, wait_access, h, now_lag, wait_lag)
    conditional = conditional_signal(lo, hi, additional_cost)
    return dict(predicted_cost_budget_bps=center, budget_lo_bps=lo, budget_hi_bps=hi,
                break_even_compression_bps=(additional_cost-base)/slope,
                conditional_signal=conditional,
                actionable_signal=conditional if eligibility == 'eligible' else 'insufficient_evidence',
                eligibility=eligibility)


def nonoverlap(q):
    """No shared origin/terminal date, including the endpoint."""
    keep, last = [], pd.Timestamp.min
    for origin, row in q.sort_index().iterrows():
        if origin > last:
            keep.append(origin)
            last = row.terminal_execution_time_utc.normalize()
    return pd.Index(keep)


def bootstrap_gap(gaps, seed=41):
    a = np.asarray(gaps)
    if len(a) < 3:
        return (float('nan'), float('nan'))
    rng = np.random.default_rng(seed)
    means = []
    for _ in range(2000):
        starts = rng.integers(0, len(a), size=int(np.ceil(len(a)/3)))
        idx = ((starts[:, None] + np.arange(3)) % len(a)).ravel()[:len(a)]
        means.append(a[idx].mean())
    return tuple(map(float, np.quantile(means, [.025, .975])))


def audit_inputs(d, hourly, panel):
    decomp = d.ptax_sell_brl_per_usd * d.usdtusd_window_usd * (1+d.premium_bps/10000)
    if not np.allclose(decomp, d.usdtbrl_window_brl, rtol=1e-9, atol=1e-9):
        raise ValueError('Daily price decomposition fails')
    finite_prices = panel[['ptax', 'signal_price', 'signal_usdtusd', 'execution_price', 'execution_usdtusd']]
    if (finite_prices.le(0) & finite_prices.notna()).any().any():
        raise ValueError('Nonpositive prices')
    return dict(daily_rows=len(d), hourly_rows=len(hourly), first=str(d.index.min().date()),
                last=str(d.index.max().date()), incomplete_window=int(d.window_hours.ne(4).sum()),
                uncertain_window=int(d.ptax_window_uncertain.sum()),
                late_or_missing_publication=int((~panel.publication_ok).sum()),
                missing_features=int((~panel.features_ok).sum()),
                missing_execution=int((~panel.execution_ok).sum()),
                input_sha256={str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                              for p in (DAILY, HOURLY)})


def run():
    d = pd.read_csv(DAILY, parse_dates=['date_brt']).set_index('date_brt')
    hourly = pd.read_csv(HOURLY, parse_dates=['time_utc']).set_index('time_utc')
    panel = build_panel(d, hourly)
    audit = audit_inputs(d, hourly, panel)
    print('INPUT AUDIT', json.dumps(audit, indent=2))
    sets, fits, selection, counts = {}, {}, [], []
    for h in HORIZONS:
        q = dataset(panel, h)
        valid = q.origin_eligible & q.terminal_eligible & q.target_compression_bps.notna()
        masks = split_masks(q)
        sets[h] = {name: q.loc[mask & valid].copy() for name, mask in masks.items()}
        for name, frame in sets[h].items():
            if len(frame) < 30:
                raise ValueError(f'Insufficient {name} rows at horizon {h}: {len(frame)}')
            counts.append(dict(horizon=h, split=name, n=len(frame), first=str(frame.index.min().date()),
                               last=str(frame.index.max().date()),
                               last_terminal=str(frame.terminal_execution_time_utc.max())))
        fit, val = sets[h]['fit'], sets[h]['validation']
        for alpha in (1., 10., 100., 1000.):
            model = fit_ridge(fit[FEATURES].to_numpy(), fit.target_compression_bps.to_numpy(), alpha)
            fits[h, alpha] = model
            mae = np.mean(np.abs(val.target_compression_bps.to_numpy()-predict(val, 'ridge', model)))
            selection.append(dict(horizon=h, alpha=alpha, validation_mae_bps=mae,
                                  selection_eligible=(h == 10)))
    selected = min((r for r in selection if r['selection_eligible']),
                   key=lambda r: (r['validation_mae_bps'], r['alpha']))['alpha']
    predictions, intervals, latest, parameters = [], [], [], []
    for h in HORIZONS:
        model = fits[h, selected]
        parameters.append(dict(horizon=h, alpha=selected, feature='intercept', coefficient=model['coef'][0],
                               fit_mean=np.nan, fit_scale=np.nan))
        parameters.extend(dict(horizon=h, alpha=selected, feature=f, coefficient=model['coef'][j+1],
                               fit_mean=model['mu'][j], fit_scale=model['scale'][j]) for j, f in enumerate(FEATURES))
        cal = sets[h]['calibration']
        for method in METHODS:
            radius = residual_radius(cal.target_compression_bps.to_numpy()-predict(cal, method, model))
            intervals.append(dict(horizon=h, method=method, calibration_n=len(cal), radius_bps=radius,
                                  nominal_coverage=.90, fitted_through='2024-06-30', calibration_through='2024-12-31'))
            for split in ('validation', 'test'):
                q = sets[h][split]
                non = nonoverlap(q)
                preds = predict(q, method, model)
                for (origin, row), pred in zip(q.iterrows(), preds):
                    actual = budget(h, x0=float(row.ptax), u0=float(row.execution_usdtusd),
                                    p0=float(row.execution_premium), x1=float(row.terminal_ptax),
                                    u1=float(row.terminal_execution_usdtusd),
                                    p1=float(row.terminal_execution_premium))['max_additional_cost_bps']
                    for cost in (0., 25., 50.):
                        decision = assess(row.signal_premium, pred, radius, h, row.ptax,
                                          row.signal_usdtusd, cost)
                        waits = decision['conditional_signal'] == 'waiting_may_compensate'
                        gain = actual-cost
                        predictions.append(dict(origin=origin, signal_time_utc=row.signal_time_utc,
                            execution_time_utc=row.execution_time_utc, terminal_time_utc=row.terminal_execution_time_utc,
                            split=split, horizon=h, method=method, additional_cost_bps=cost,
                            signal_premium_bps=row.signal_premium, execution_premium_bps=row.execution_premium,
                            signal_execution_gap_bps=row.execution_premium-row.signal_premium,
                            actual_compression_bps=row.target_compression_bps, predicted_compression_bps=pred,
                            compression_lo_bps=pred-radius, compression_hi_bps=pred+radius,
                            interval_covers=(abs(row.target_compression_bps-pred) <= radius),
                            nonoverlapping=origin in non, **decision,
                            realized_wait_saving_bps=gain, policy_wait=waits,
                            conditional_policy_saving_bps=gain if waits else 0.,
                            hindsight_regret_bps=max(0., gain)-(gain if waits else 0.)))
            # Last available origin, with no future price required; this is an archive-as-of forecast.
            last = panel.loc[panel.quality_ok & panel.publication_ok & panel.features_ok].iloc[[-1]]
            pred = float(predict(last, method, model)[0]); row = last.iloc[0]
            latest.append(dict(as_of=last.index[0], horizon=h, method=method,
                               predicted_compression_bps=pred, compression_lo_bps=pred-radius,
                               compression_hi_bps=pred+radius, additional_cost_bps=25.,
                               **assess(row.signal_premium, pred, radius, h, row.ptax, row.signal_usdtusd)))
    pred = pd.DataFrame(predictions)
    metrics, policies, comparisons = [], [], []
    for (split, h, method), group in pred[pred.additional_cost_bps.eq(25)].groupby(['split','horizon','method']):
        for scope in ('daily', 'nonoverlapping'):
            a = group if scope == 'daily' else group[group.nonoverlapping]
            error = a.predicted_compression_bps-a.actual_compression_bps
            metrics.append(dict(split=split, horizon=h, method=method, scope=scope, n=len(a),
                mae_bps=error.abs().mean(), rmse_bps=np.sqrt((error**2).mean()),
                coverage=a.interval_covers.mean(), width_bps=(a.compression_hi_bps-a.compression_lo_bps).mean()))
    for (split, h, cost), group in pred.groupby(['split','horizon','additional_cost_bps']):
        for scope in ('daily', 'nonoverlapping'):
            a = group if scope == 'daily' else group[group.nonoverlapping]
            for method, b in a.groupby('method'):
                policies.append(dict(split=split,horizon=h,additional_cost_bps=cost,scope=scope,
                    policy=method,n=len(b),wait_fraction=b.policy_wait.mean(),
                    abstain_fraction=b.conditional_signal.eq('insufficient_evidence').mean(),
                    mean_saving_bps=b.conditional_policy_saving_bps.mean(),
                    mean_regret_bps=b.hindsight_regret_bps.mean(),
                    worst_saving_bps=b.conditional_policy_saving_bps.min()))
            b = a[a.method.eq('persistence')]
            for name, gains in [('buy_now',np.zeros(len(b))),('always_wait',b.realized_wait_saving_bps.to_numpy())]:
                policies.append(dict(split=split,horizon=h,additional_cost_bps=cost,scope=scope,
                    policy=name,n=len(b),wait_fraction=float(name=='always_wait'),abstain_fraction=0.,
                    mean_saving_bps=np.mean(gains), mean_regret_bps=np.mean(np.maximum(0,b.realized_wait_saving_bps)-gains),
                    worst_saving_bps=np.min(gains)))
    primary = pred[pred.additional_cost_bps.eq(25) & pred.nonoverlapping]
    for (split, h), group in primary.groupby(['split','horizon']):
        wide = group.assign(abs_error=lambda x: abs(x.predicted_compression_bps-x.actual_compression_bps)).pivot(
            index='origin', columns='method', values='abs_error').sort_index()
        for baseline in ('persistence','mean_reversion'):
            gap = wide.ridge-wide[baseline]
            lo, hi = bootstrap_gap(gap.to_numpy())
            comparisons.append(dict(split=split,horizon=h,baseline=baseline,n=len(wide),
                                    ridge_minus_baseline_mae_bps=gap.mean(),lo95_bps=lo,hi95_bps=hi))
    TAB.mkdir(parents=True, exist_ok=True); FIG.mkdir(parents=True, exist_ok=True)
    tables = {'predictions':pred,'metrics':pd.DataFrame(metrics),'policies':pd.DataFrame(policies),
              'comparisons':pd.DataFrame(comparisons),'selection':pd.DataFrame(selection),
              'calibration':pd.DataFrame(intervals),'splits':pd.DataFrame(counts),
              'parameters':pd.DataFrame(parameters),'latest':pd.DataFrame(latest)}
    audit['selected_alpha'] = selected
    audit['source_sha256'] = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
        for p in (Path(__file__), ROOT/'scripts/p3_38_buyer_frontier.py',
                  ROOT/'tasks/P3-41-premium-compression.md')}
    audit['excluded_origins_by_horizon'] = {h:dict(total=len(panel),
        origin_ineligible=int((~dataset(panel,h).origin_eligible).sum()),
        terminal_ineligible=int((~dataset(panel,h).terminal_eligible).sum()),
        valid_pairs=int((dataset(panel,h).origin_eligible & dataset(panel,h).terminal_eligible).sum())) for h in HORIZONS}
    audit['protocol'] = 'tasks/P3-41-premium-compression.md; committed before fitting'
    audit['interpretation'] = 'retrospective chronological evaluation; 2026 was already seen in earlier work'
    audit['actual_access'] = 'unknown; all actionable signals insufficient_evidence'
    audit['intervals'] = '90% empirical historical absolute-residual bands; no coverage guarantee'
    audit['chronos'] = 'not run; pretrained overlap and dependencies not audited'
    audit['environment'] = dict(numpy=np.__version__, pandas=pd.__version__, matplotlib=matplotlib.__version__)
    tables['june_replay'] = pred[pred.origin.eq(pd.Timestamp('2026-06-25')) & pred.additional_cost_bps.eq(25)].copy()
    for name, table in tables.items():
        table.to_csv(TAB / f'P3-41_{name}.csv',index=False,lineterminator='\n')
    panel.reset_index().to_csv(TAB/'P3-41_input_panel.csv',index=False,lineterminator='\n')
    (TAB/'P3-41_audit.json').write_text(json.dumps(audit,indent=2),encoding='utf-8')
    make_figures(pred, tables['metrics'])
    print('SELECTED ALPHA', selected)
    print(tables['metrics'].query("split == 'test' and scope == 'nonoverlapping'").to_string(index=False))
    print(tables['policies'].query("split == 'test' and scope == 'nonoverlapping' and horizon == 10 and additional_cost_bps == 25").to_string(index=False))


def make_figures(pred, metrics):
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,
                         'axes.spines.right':False,'axes.titleweight':'bold','savefig.dpi':180})
    a = pred[(pred.origin.eq(pd.Timestamp('2026-06-25'))) & pred.additional_cost_bps.eq(25) & pred.method.eq('ridge')].sort_values('horizon')
    if len(a) != 3:
        raise ValueError('Fixed June replay unavailable; do not silently substitute a date')
    fig, ax = plt.subplots(figsize=(10,6))
    ax.errorbar(a.horizon,a.predicted_compression_bps,
                yerr=[a.predicted_compression_bps-a.compression_lo_bps,a.compression_hi_bps-a.predicted_compression_bps],
                fmt='o',capsize=6,color=COLORS['ridge'],label='Ridge + faixa residual histórica de 90%')
    ax.plot(a.horizon,a.actual_compression_bps,'D--',color='#333333',label='Compressão observada (até a compra às 15h)')
    ax.plot(a.horizon,a.break_even_compression_bps,'s:',color='#c48220',label='Queda necessária: cenário central, K = 25 pb')
    ax.axhline(0,color='#888888',lw=.7)
    ax.set(xticks=[5,10,20],xlabel='Prazo (dias com PTAX)',ylabel='Compressão do prêmio (pb; sinal − preço futuro)',
           title='25/06/2026: a previsão cobre o custo de esperar?')
    ax.grid(axis='y',alpha=.2)
    ax.legend(loc='lower left',bbox_to_anchor=(0,1.02),fontsize=9)
    fig.text(.08,.025,'Sinal às 14h BRT; compras indicativas às 15h. Ajuste até jun/2024; calibração jul–dez/2024; seleção em 2025.\nReconstituição histórica conhecida; faixa sem garantia de cobertura. Juros/custos hipotéticos; acesso e entrega não verificados.',fontsize=9)
    ax.set_title('25/06/2026: a previsão cobre o custo de esperar?',pad=85)
    fig.tight_layout(rect=(0,.11,1,1));fig.savefig(FIG/'P3-41_june_replay.png');plt.close(fig)
    fig, axs = plt.subplots(1,2,figsize=(12,5))
    m = metrics.query("split == 'test' and scope == 'nonoverlapping'")
    for method in METHODS:
        q=m[m.method.eq(method)].sort_values('horizon')
        axs[0].plot(q.horizon,q.mae_bps,'o-',color=COLORS[method],label=method.replace('_',' '))
        axs[1].plot(q.horizon,100*q.coverage,'o-',color=COLORS[method],label=method.replace('_',' '))
    axs[0].set(ylabel='Erro absoluto médio (pb)',title='Erro da previsão',ylim=(0,None))
    axs[1].axhline(90,color='#333333',ls='--',lw=1,label='Nominal: 90%')
    axs[1].set(ylabel='Origens cobertas pela faixa (%)',title='Cobertura fora da calibração',ylim=(0,105))
    for ax in axs:
        ax.set(xticks=[5,10,20],xlabel='Prazo (dias com PTAX)');ax.grid(axis='y',alpha=.2);ax.legend(fontsize=9)
    counts=m[m.method.eq('ridge')].sort_values('horizon')
    fig.suptitle('2026: comparação em janelas sem sobreposição',fontsize=15,fontweight='bold')
    fig.text(.08,.02,'N por prazo: '+', '.join(f'{int(r.horizon)}d = {int(r.n)}' for r in counts.itertuples())+
             '. Sem sobreposição não implica independência; um único choque brasileiro em 2026.\nFonte: Binance + BCB, arquivos P1-02. Faixas históricas de 2024; dados de 2026 já conhecidos no projeto.',fontsize=9)
    fig.tight_layout(rect=(0,.12,1,.92));fig.savefig(FIG/'P3-41_evaluation.png');plt.close(fig)


class Tests(unittest.TestCase):
    @staticmethod
    def sample():
        dates=pd.bdate_range('2023-01-02',periods=180)
        hidx=pd.date_range(dates.min(),dates.max()+pd.Timedelta(hours=23),freq='h')
        t=np.arange(len(hidx))
        hourly=pd.DataFrame({'usdtbrl_close_brl':5*(1+.001*np.sin(t/31)),
            'usdtusd_close_usd':1.,'usdtbrl_open_brl':5*(1+.001*np.sin((t-1)/31)),
            'usdtusd_open_usd':1.,'usdtbrl_volume_usdt':100.+t%11},index=hidx)
        d=pd.DataFrame({'ptax_published_brt':dates+pd.Timedelta(hours=13,minutes=10),
            'ptax_sell_brl_per_usd':5.,'premium_bps':np.sin(np.arange(len(dates))),
            'window_hours':4,'ptax_window_uncertain':False},index=dates)
        return d,hourly

    def test_future_perturbation_and_clock(self):
        d,h=self.sample(); cutoff=d.index[100]+pd.Timedelta(hours=17)
        p=build_panel(d,h)
        # Anything after signal, including execution and same-day close, cannot alter features.
        changed=h.copy();changed.loc[changed.index>=cutoff,'usdtbrl_close_brl']*=2
        changed.loc[changed.index>=cutoff,'usdtbrl_volume_usdt']*=20
        pd.testing.assert_frame_equal(p.loc[:d.index[100],FEATURES],build_panel(d,changed).loc[:d.index[100],FEATURES])
        d2=d.copy();d2.loc[d2.index>d.index[100],'premium_bps']=10000
        pd.testing.assert_frame_equal(p.loc[:d.index[100],FEATURES],build_panel(d2,h).loc[:d.index[100],FEATURES])
        self.assertLess(p.loc[d.index[100],'signal_time_utc'],p.loc[d.index[100],'execution_time_utc'])

    def test_target_and_execution_gap(self):
        d,h=self.sample();p=build_panel(d,h);q=dataset(p,10);i=100
        self.assertAlmostEqual(q.iloc[i].target_compression_bps,p.iloc[i].signal_premium-p.iloc[i+10].execution_premium)
        self.assertNotEqual(p.iloc[i].signal_price,p.iloc[i].execution_price)
        self.assertTrue(pd.isna(q.iloc[-1].target_compression_bps))

    def test_late_publication_and_missing_hour(self):
        d,h=self.sample();day=d.index[100]
        d.loc[day,'ptax_published_brt']=day+pd.Timedelta(hours=14,minutes=1)
        h=h.drop(day+pd.Timedelta(hours=10))
        p=build_panel(d,h)
        self.assertFalse(p.loc[day,'publication_ok'])
        self.assertFalse(p.loc[day,'features_ok'])

    def test_split_purging(self):
        q=pd.DataFrame({'terminal_execution_time_utc':pd.to_datetime(['2024-06-28 18:00','2024-07-01 18:00','2025-01-02 18:00','2026-01-02 18:00'])},
                       index=pd.to_datetime(['2024-06-20','2024-06-21','2024-12-20','2025-12-20']))
        masks=split_masks(q)
        self.assertEqual(masks['fit'].tolist(),[True,False,False,False])
        self.assertFalse(masks['calibration'].any())
        self.assertFalse(masks['validation'].any())

    def test_ridge_and_calibration(self):
        x=np.column_stack([np.arange(30),np.ones(30)])
        m=fit_ridge(x,np.repeat(7.,30),10)
        self.assertAlmostEqual(m['coef'][0],7.)
        self.assertTrue(np.isfinite(m['coef']).all())
        self.assertEqual(residual_radius(np.arange(1,10)),9.)
        with self.assertRaises(ValueError):residual_radius([])

    def test_frontier_break_even_and_access(self):
        a=assess(100,50,10,10,5,1,25)
        self.assertEqual(a['actionable_signal'],'insufficient_evidence')
        b=assess(100,a['break_even_compression_bps'],0,10,5,1,25,True,True)
        self.assertAlmostEqual(b['predicted_cost_budget_bps'],25,places=7)
        self.assertIn('late_delivery',assess(100,50,10,10,5,1,25,True,True,wait_lag=1)['eligibility'])
        self.assertEqual(conditional_signal(30,40,25),'waiting_may_compensate')
        self.assertEqual(conditional_signal(0,20,25),'buy_now')
        self.assertEqual(conditional_signal(20,30,25),'insufficient_evidence')

    def test_independent_terminal_cost_arithmetic(self):
        # 100k USDT, price now 5.05 and later 5.00; no rate or fee: saving R$5k.
        r=budget(10,x0=5,u0=1,p0=100,x1=5,u1=1,p1=0,
                 deposit=0,forward_brl=0,forward_usd=0,fee_now=0,fee_wait=0)
        self.assertAlmostEqual(r['max_additional_cost_brl'],5000.)
        self.assertAlmostEqual(r['max_additional_cost_bps'],5000/505000*10000)

    def test_invalid_forecast_and_unavailable_route(self):
        with self.assertRaises(ValueError): assess(100,0,-1,10,5,1)
        with self.assertRaises(ValueError): assess(100,float('nan'),1,10,5,1)
        with self.assertRaises(ValueError): assess(100,20000,1,10,5,1)
        r=assess(100,100,1,10,5,1,now_access=True,wait_access=False)
        self.assertIn('unavailable',r['eligibility'])
        self.assertEqual(r['actionable_signal'],'insufficient_evidence')

    def test_nonoverlap_and_bootstrap(self):
        q=pd.DataFrame({'terminal_execution_time_utc':pd.date_range('2025-01-06 18:00',periods=9)},
                       index=pd.date_range('2025-01-01',periods=9))
        keep=nonoverlap(q)
        self.assertEqual(keep.tolist(),[pd.Timestamp('2025-01-01'),pd.Timestamp('2025-01-07')])
        self.assertEqual(bootstrap_gap(np.zeros(12)),(0.,0.))


if __name__ == '__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--test-only',action='store_true');args=ap.parse_args()
    result=unittest.TextTestRunner().run(unittest.defaultTestLoader.loadTestsFromTestCase(Tests))
    if not result.wasSuccessful(): raise SystemExit(1)
    if not args.test_only: run()
