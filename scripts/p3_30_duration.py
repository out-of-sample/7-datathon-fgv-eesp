"""P3-30: Global 10-currency shock duration census, feasibility audit,
and penalized discrete-time survival model evaluation.
Inputs: frozen P1-02/P1-05 processed CSVs.
Outputs: P3-30 tables and figures.
Run: py scripts/p3_30_duration.py [--test]   (Linux/macOS: .venv/bin/python scripts/p3_30_duration.py)
Review 6 Nov 2026 (Renzo's agent): censored-before-horizon episodes are no longer scored as failures;
paired bootstrap of the Brier gap added (P3-30_brier_bootstrap.csv); summary numbers computed, not typed.
"""
from pathlib import Path
import hashlib
import json
import sys
import numpy as np
import pandas as pd
from scipy.optimize import minimize
from scipy.special import expit
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
OUT_TABLES = ROOT / 'results/tables'
OUT_FIGURES = ROOT / 'results/figures'

def extract(s, threshold=3, store_series=False):
    """Extract episodes based on locked rolling median and robust dispersion.
    s: pd.Series of daily premium (bps) on its native calendar.
    """
    rows = []
    active = None
    history = []
    streak = 0
    last = None
    for date, value in s.items():
        if not np.isfinite(value):
            if active is not None:
                active.update(event=0, end=last, reason='missing_observation')
                rows.append(active)
                active = None
            history = []
            streak = 0
            continue
        if active is None and len(history) >= 60:
            reference = np.array(history[-60:])
            median = float(np.median(reference))
            sigma = float(1.4826 * np.median(np.abs(reference - median)))
            if sigma > 0 and value > median + threshold * sigma:
                active = dict(
                    start=date,
                    median_bps=median,
                    sigma_bps=sigma,
                    initial_excess_bps=float(value - median),
                    duration=0
                )
                if store_series:
                    active['dates'] = [date]
                    active['values'] = [float(value)]
                streak = 0
        elif active is not None:
            active['duration'] += 1
            if store_series:
                active['dates'].append(date)
                active['values'].append(float(value))
            streak = streak + 1 if abs(value - active['median_bps']) <= active['sigma_bps'] else 0
            if streak == 5:
                active.update(event=1, end=date, reason='five_in_band')
                rows.append(active)
                active = None
                streak = 0
        history.append(float(value))
        last = date
    if active is not None:
        active.update(event=0, end=last, reason='sample_end')
        rows.append(active)
    return rows

def km(rows, horizon, age=0):
    """Conditional Kaplan-Meier recovery probability; undefined beyond observed risk support."""
    if not rows or max(r['duration'] for r in rows) < age + horizon:
        return np.nan
    surv = 1.0
    initial = 1.0
    for t in sorted(set(r['duration'] for r in rows)):
        risk = sum(r['duration'] >= t for r in rows)
        events = sum(r['duration'] == t and r['event'] == 1 for r in rows)
        if risk == 0:
            continue
        if t <= age:
            initial *= (1.0 - events / risk)
        if t <= age + horizon:
            surv *= (1.0 - events / risk)
    return 1.0 - surv / initial if initial > 0 else np.nan

def outcome(ep, age0, h):
    """Known recovery label by age0 + h: 1 recovered, 0 still open, None unknown
    (censored before age0 + h; such episodes are left out of the score, not counted as failures).
    Review fix 6 Nov (Renzo's agent): the first version scored them as 0."""
    D, E = ep['duration'], ep['event']
    if E == 1 and D <= age0 + h:
        return 1
    if D >= age0 + h:
        return 0
    return None


def paired_bootstrap(diff, draws=10_000, seed=0):
    """Mean and 95% percentile interval of a per-episode difference (resampling episodes)."""
    diff = np.asarray(diff, dtype=float)
    rng = np.random.default_rng(seed)
    boot = diff[rng.integers(0, len(diff), size=(draws, len(diff)))].mean(axis=1)
    return float(diff.mean()), float(np.percentile(boot, 2.5)), float(np.percentile(boot, 97.5))


def fit_logistic_hazard(X, y, l2=1.0, w0=None):
    """Fit discrete-time logistic hazard model with L2 regularization on non-intercept features."""
    def loss(w):
        z = np.clip(X @ w, -30.0, 30.0)
        p = expit(z)
        eps = 1e-15
        ll = y * np.log(p + eps) + (1.0 - y) * np.log(1.0 - p + eps)
        pen = 0.5 * l2 * np.sum(w[1:]**2)
        return -np.sum(ll) + pen

    def grad(w):
        z = np.clip(X @ w, -30.0, 30.0)
        p = expit(z)
        g = X.T @ (p - y)
        g[1:] += l2 * w[1:]
        return g

    if w0 is None:
        w0 = np.zeros(X.shape[1])
        my = max(min(float(np.mean(y)), 0.99), 0.01)
        w0[0] = np.log(my / (1.0 - my))

    res = minimize(loss, w0, jac=grad, method='BFGS')
    return res.x

def tests():
    """Verify episode extraction, censoring rules, Kaplan-Meier arithmetic,
    and regularized discrete-time hazard shrinkage and scoring."""
    idx = pd.bdate_range('2020-01-01', periods=90)
    base = ([0., 1., -1.] * 20)
    s = pd.Series(base + [10.] * 10 + [0.] * 20, index=idx)
    r = extract(s)
    assert len(r) == 1 and r[0]['duration'] == 14 and r[0]['event'] == 1
    truncated = extract(s.iloc[:70])
    assert truncated[0]['event'] == 0 and truncated[0]['duration'] == 9
    broken = s.copy()
    broken.iloc[72] = np.nan
    r = extract(broken)
    assert r[0]['event'] == 0 and r[0]['reason'] == 'missing_observation'
    flat = pd.Series([0.] * 60 + [100.] * 30, index=idx)
    assert extract(flat) == []
    prefix = extract(s.iloc[:70])
    altered = s.copy()
    altered.iloc[70:] = 10000
    assert prefix == extract(altered.iloc[:70])
    assert km([dict(duration=5, event=1), dict(duration=10, event=0)], 5) == 0.5
    assert np.isnan(km([dict(duration=5, event=1)], 10))
    below = pd.Series(base + [10.] * 10 + [-10.] * 20, index=idx)
    assert extract(below)[0]['event'] == 0  # overshoot is not frozen-band recovery

    # Discrete-time regularized hazard shrinkage and Brier scoring tests
    X_test = np.array([[1.0, 1.0], [1.0, 2.0], [1.0, 3.0], [1.0, 4.0]])
    y_test = np.array([0, 0, 1, 1])
    w_low = fit_logistic_hazard(X_test, y_test, l2=0.1)
    w_high = fit_logistic_hazard(X_test, y_test, l2=10.0)
    assert abs(w_high[1]) < abs(w_low[1])  # regularization strictly shrinks slope
    brier_test = float(np.mean((y_test - expit(X_test @ w_low))**2))
    assert 0.0 <= brier_test <= 1.0
    # Review fix: an episode censored before the horizon has no label
    assert outcome(dict(duration=3, event=0), 0, 10) is None
    assert outcome(dict(duration=10, event=0), 0, 10) == 0
    assert outcome(dict(duration=7, event=1), 0, 10) == 1
    assert outcome(dict(duration=12, event=1), 0, 10) == 0
    return 14

def main():
    ntests = tests()
    if '--test' in sys.argv:
        print(f'{ntests} duration and survival model checks passed')
        return

    OUT_TABLES.mkdir(exist_ok=True, parents=True)
    OUT_FIGURES.mkdir(exist_ok=True, parents=True)

    sources = [
        'data/processed/P1-02_premium_daily.csv',
        'data/processed/P1-05_donor_premiums_daily.csv'
    ]
    provenance = {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in sources}

    # Load BRL series (P1-02) and donor series (P1-05)
    br = pd.read_csv(ROOT / sources[0], parse_dates=['date_brt']).set_index('date_brt')['premium_bps'].sort_index()
    donor = pd.read_csv(ROOT / sources[1], parse_dates=['date']).set_index('date').sort_index()

    currencies = ['BRL', 'EUR', 'TRY', 'ZAR', 'MXN', 'PLN', 'IDR', 'COP', 'UAH', 'ARS']
    series_dict = {'BRL': br}
    for c in currencies[1:]:
        series_dict[c] = donor[c].dropna()

    combined_calendar = pd.Index(sorted(set(br.index).union(set(donor.index))))

    # 1. Input audit
    audits = []
    for c in currencies:
        s = series_dict[c]
        audits.append(dict(
            currency=c,
            rows=len(s),
            valid=len(s),
            missing=int(s.isna().sum()),
            first=str(s.index.min().date()),
            last=str(s.index.max().date()),
            eligibility='primary_brazil' if c == 'BRL' else 'global_pool_native_calendar'
        ))
    pd.DataFrame(audits).to_csv(OUT_TABLES / 'P3-30_input_audit.csv', index=False)

    # 2. Extract episodes across all currencies and thresholds k in [3, 2, 4]
    all_episodes = []
    for c in currencies:
        s = series_dict[c]
        for k in [3, 2, 4]:
            ep_list = extract(s, threshold=k, store_series=True)
            for i, r in enumerate(ep_list):
                row = dict(
                    currency=c,
                    threshold=k,
                    episode_id=f'{c}-{k}-{i+1}',
                    start=r['start'],
                    median_bps=r['median_bps'],
                    sigma_bps=r['sigma_bps'],
                    initial_excess_bps=r['initial_excess_bps'],
                    duration=r['duration'],
                    event=r['event'],
                    end=r['end'],
                    reason=r['reason'],
                    dates=r['dates'],
                    values=r['values']
                )
                all_episodes.append(row)

    df_ep = pd.DataFrame(all_episodes)

    # Dependency clusters across combined calendar
    df_ep['dependency_group'] = ''
    for k in [3, 2, 4]:
        group = 0
        previous_pos = -100
        sub_indices = df_ep[df_ep.threshold == k].sort_values('start').index
        for idx in sub_indices:
            start_date = df_ep.loc[idx, 'start']
            pos = combined_calendar.get_loc(start_date)
            if pos - previous_pos > 10:
                group += 1
            df_ep.loc[idx, 'dependency_group'] = f'k{k}-g{group}'
            previous_pos = pos

    # Export clean scalar episodes table
    export_cols = ['currency', 'threshold', 'episode_id', 'start', 'median_bps',
                   'sigma_bps', 'initial_excess_bps', 'duration', 'event', 'end',
                   'reason', 'dependency_group']
    df_ep[export_cols].to_csv(OUT_TABLES / 'P3-30_episodes.csv', index=False)

    # 3. Census table
    counts = df_ep.groupby(['threshold', 'currency']).agg(
        episodes=('event', 'size'),
        recoveries=('event', 'sum')
    )
    idx_prod = pd.MultiIndex.from_product([[2, 3, 4], currencies], names=['threshold', 'currency'])
    counts = counts.reindex(idx_prod, fill_value=0).reset_index()
    counts.to_csv(OUT_TABLES / 'P3-30_census.csv', index=False)

    # 4. Feasibility evaluation: BRL_only vs Global_10_currencies
    gates = []
    descriptive_km = []

    # A. BRL_only scope
    for k in [3, 2, 4]:
        s_brl = series_dict['BRL']
        train_brl = extract(s_brl.loc[:'2024-12-31'], k)
        val_brl = [r for r in extract(s_brl.loc[:'2025-12-31'], k) if r['start'].year == 2025]
        test_brl = [r for r in extract(s_brl, k) if r['start'].year == 2026]
        brl_splits = {'train': train_brl, 'validation': val_brl, 'test': test_brl}

        for name, rs in brl_splits.items():
            evs = sum(r['event'] for r in rs)
            min_n, min_e = (10, 5) if name == 'train' else (5, 2)
            passed = len(rs) >= min_n and evs >= min_e
            gates.append(dict(
                scope='BRL_only',
                threshold=k,
                split=name,
                episodes=len(rs),
                recoveries=evs,
                censored=len(rs) - evs,
                minimum_episodes=min_n,
                minimum_recoveries=min_e,
                passed=passed
            ))
            for age in [0, 5, 10]:
                for h in [5, 10, 20]:
                    descriptive_km.append(dict(
                        scope='BRL_only',
                        threshold=k,
                        split=name,
                        age_ptax_days=age,
                        horizon_ptax_days=h,
                        km_recovery_probability=km(rs, h, age),
                        at_risk_at_age=sum(r['duration'] > age or (age == 0 and r['duration'] >= 0) for r in rs)
                    ))

    # B. Global_10_currencies scope
    global_splits_by_k = {}
    for k in [3, 2, 4]:
        train_pool = []
        val_pool = []
        test_pool = []
        for c in currencies:
            s = series_dict[c]
            tr = [dict(currency=c, **r) for r in extract(s.loc[:'2024-12-31'], k, store_series=True)]
            va = [dict(currency=c, **r) for r in extract(s.loc[:'2025-12-31'], k, store_series=True) if r['start'].year == 2025]
            te = [dict(currency=c, **r) for r in extract(s, k, store_series=True) if r['start'].year == 2026]
            train_pool.extend(tr)
            val_pool.extend(va)
            test_pool.extend(te)

        global_splits_by_k[k] = {'train': train_pool, 'validation': val_pool, 'test': test_pool}

        for name, rs in global_splits_by_k[k].items():
            evs = sum(r['event'] for r in rs)
            min_n, min_e = (10, 5) if name == 'train' else (5, 2)
            passed = len(rs) >= min_n and evs >= min_e
            gates.append(dict(
                scope='Global_10_currencies',
                threshold=k,
                split=name,
                episodes=len(rs),
                recoveries=evs,
                censored=len(rs) - evs,
                minimum_episodes=min_n,
                minimum_recoveries=min_e,
                passed=passed
            ))
            for age in [0, 5, 10]:
                for h in [5, 10, 20]:
                    descriptive_km.append(dict(
                        scope='Global_10_currencies',
                        threshold=k,
                        split=name,
                        age_ptax_days=age,
                        horizon_ptax_days=h,
                        km_recovery_probability=km(rs, h, age),
                        at_risk_at_age=sum(r['duration'] > age or (age == 0 and r['duration'] >= 0) for r in rs)
                    ))

    df_gates = pd.DataFrame(gates)
    df_gates.to_csv(OUT_TABLES / 'P3-30_feasibility.csv', index=False)
    pd.DataFrame(descriptive_km).to_csv(OUT_TABLES / 'P3-30_descriptive_km.csv', index=False)

    # 5. Penalized Discrete-Time Survival Model vs Kaplan-Meier
    # Focus on k=3 (primary), with k=2, 4 robustness
    eval_records = []
    models_by_k = {}
    per_episode = {}

    for k in [3, 2, 4]:
        train_pool = global_splits_by_k[k]['train']
        val_pool = global_splits_by_k[k]['validation']
        test_pool = global_splits_by_k[k]['test']

        # Construct person-period training data
        train_rows = []
        for ep in train_pool:
            D = ep['duration']
            E = ep['event']
            m = ep['median_bps']
            sig = ep['sigma_bps']
            init_ex = ep['initial_excess_bps']
            vals = ep['values']
            for t in range(1, D + 1):
                y_val = 1 if (t == D and E == 1) else 0
                lag_idx = max(0, t - 1)
                v = vals[lag_idx] if lag_idx < len(vals) else vals[-1]
                cur_ex = v - m
                cur_z = cur_ex / sig if sig > 0 else 0.0
                train_rows.append(dict(age=t, init_ex=init_ex, cur_ex=cur_ex, cur_z=cur_z, y=y_val))

        df_train_pp = pd.DataFrame(train_rows)
        f1 = np.log1p(df_train_pp['age'].values)
        f2 = np.log1p(np.maximum(0, df_train_pp['init_ex'].values))
        f3 = np.sign(df_train_pp['cur_ex'].values) * np.log1p(np.abs(df_train_pp['cur_ex'].values))
        f4 = np.clip(df_train_pp['cur_z'].values, -5.0, 20.0)

        F_raw = np.column_stack([f1, f2, f3, f4])
        mu = np.mean(F_raw, axis=0)
        sd = np.std(F_raw, axis=0)
        sd[sd == 0] = 1.0

        F_std = (F_raw - mu) / sd
        X_train = np.column_stack([np.ones(len(df_train_pp)), F_std])
        y_train = df_train_pp['y'].values

        # Fit models across candidate L2 penalties
        candidate_l2 = [0.5, 1.0, 5.0, 10.0]
        weights = {}
        for l2 in candidate_l2:
            weights[l2] = fit_logistic_hazard(X_train, y_train, l2=l2)

        # Select l2 on Validation 2025 at onset (age0=0) and h=10 days
        val_briers = {}
        for l2 in candidate_l2:
            w = weights[l2]
            sq_errs = []
            for ep in val_pool:
                if outcome(ep, 0, 10) is None:
                    continue
                init_ex = ep['initial_excess_bps']
                sig = ep['sigma_bps']
                cur_ex = init_ex
                cur_z = init_ex / sig if sig > 0 else 0.0
                surv = 1.0
                for s in range(1, 11):
                    f_s = np.array([
                        np.log1p(s),
                        np.log1p(max(0, init_ex)),
                        np.sign(cur_ex) * np.log1p(abs(cur_ex)),
                        np.clip(cur_z, -5.0, 20.0)
                    ])
                    x_s = np.array([1.0, *((f_s - mu) / sd)])
                    h_s = expit(np.dot(w, x_s))
                    surv *= (1.0 - h_s)
                p_pred = 1.0 - surv
                sq_errs.append((outcome(ep, 0, 10) - p_pred)**2)
            val_briers[l2] = float(np.mean(sq_errs))

        selected_l2 = min(val_briers, key=val_briers.get)
        models_by_k[k] = {
            'mu': mu,
            'sd': sd,
            'weights': weights,
            'selected_l2': selected_l2,
            'val_briers': val_briers
        }

        # Evaluate Validation and Test across models, horizons, and landmarks
        for split_name, pool in [('validation', val_pool), ('test', test_pool)]:
            for h in [5, 10, 20]:
                p_km_train_0 = km(train_pool, h, age=0)

                # 1. Baseline Kaplan-Meier at onset (age0 = 0)
                scored = [ep for ep in pool if outcome(ep, 0, h) is not None]
                sq_km_0 = [(outcome(ep, 0, h) - p_km_train_0)**2 for ep in scored]
                per_episode[(k, split_name, h, 'KM')] = sq_km_0

                eval_records.append(dict(
                    threshold=k,
                    split=split_name,
                    evaluation_scope='onset',
                    age0=0,
                    horizon_days=h,
                    model='Kaplan-Meier',
                    l2_penalty=np.nan,
                    n_scored=len(scored),
                    brier_score=round(float(np.mean(sq_km_0)), 4),
                    km_train_prob=round(p_km_train_0, 4),
                    pred_mean=round(p_km_train_0, 4),
                    w_intercept=np.nan,
                    w_age=np.nan,
                    w_init=np.nan,
                    w_cur=np.nan,
                    w_z=np.nan
                ))

                # 2. Penalized Hazard Models at onset (age0 = 0)
                for l2 in candidate_l2:
                    w = weights[l2]
                    sq_haz_0 = []
                    preds_0 = []
                    for ep in scored:
                        init_ex = ep['initial_excess_bps']
                        sig = ep['sigma_bps']
                        cur_ex = init_ex
                        cur_z = init_ex / sig if sig > 0 else 0.0
                        surv = 1.0
                        for s in range(1, h + 1):
                            f_s = np.array([
                                np.log1p(s),
                                np.log1p(max(0, init_ex)),
                                np.sign(cur_ex) * np.log1p(abs(cur_ex)),
                                np.clip(cur_z, -5.0, 20.0)
                            ])
                            x_s = np.array([1.0, *((f_s - mu) / sd)])
                            h_s = expit(np.dot(w, x_s))
                            surv *= (1.0 - h_s)
                        p_pred = 1.0 - surv
                        preds_0.append(p_pred)
                        sq_haz_0.append((outcome(ep, 0, h) - p_pred)**2)
                    per_episode[(k, split_name, h, l2)] = sq_haz_0

                    eval_records.append(dict(
                        threshold=k,
                        split=split_name,
                        evaluation_scope='onset',
                        age0=0,
                        horizon_days=h,
                        model=f'Hazard_l2_{l2}',
                        l2_penalty=l2,
                        n_scored=len(scored),
                        brier_score=round(float(np.mean(sq_haz_0)), 4),
                        km_train_prob=round(p_km_train_0, 4),
                        pred_mean=round(float(np.mean(preds_0)), 4),
                        w_intercept=round(float(w[0]), 4),
                        w_age=round(float(w[1]), 4),
                        w_init=round(float(w[2]), 4),
                        w_cur=round(float(w[3]), 4),
                        w_z=round(float(w[4]), 4)
                    ))

                # 3. Ongoing ages pooled (age0 in [0, 5, 10])
                if h == 10:
                    for model_type in ['KM', 'Hazard_l2_1.0', f'Hazard_l2_{selected_l2}']:
                        l2_val = 1.0 if '1.0' in model_type else (selected_l2 if 'Hazard' in model_type else np.nan)
                        w_curr = weights[l2_val] if not np.isnan(l2_val) else None
                        pooled_sq = []
                        pooled_preds = []

                        for age0 in [0, 5, 10]:
                            p_km_age = km(train_pool, h, age=age0)
                            for ep in pool:
                                D = ep['duration']
                                E = ep['event']
                                m = ep['median_bps']
                                sig = ep['sigma_bps']
                                init_ex = ep['initial_excess_bps']
                                vals = ep['values']
                                is_active = (D > age0 or (age0 == 0 and D >= 0))
                                if not is_active or outcome(ep, age0, h) is None:
                                    continue
                                y_true = outcome(ep, age0, h)

                                if model_type == 'KM':
                                    pred = p_km_age
                                else:
                                    # Hold current excess at landmark value
                                    v_age0 = vals[age0] if age0 < len(vals) else vals[-1]
                                    cur_ex = v_age0 - m
                                    cur_z = cur_ex / sig if sig > 0 else 0.0
                                    surv = 1.0
                                    for s in range(age0 + 1, age0 + h + 1):
                                        f_s = np.array([
                                            np.log1p(s),
                                            np.log1p(max(0, init_ex)),
                                            np.sign(cur_ex) * np.log1p(abs(cur_ex)),
                                            np.clip(cur_z, -5.0, 20.0)
                                        ])
                                        x_s = np.array([1.0, *((f_s - mu) / sd)])
                                        h_s = expit(np.dot(w_curr, x_s))
                                        surv *= (1.0 - h_s)
                                    pred = 1.0 - surv

                                pooled_preds.append(pred)
                                pooled_sq.append((y_true - pred)**2)

                        eval_records.append(dict(
                            threshold=k,
                            split=split_name,
                            evaluation_scope='pooled_ongoing_ages_0_5_10',
                            age0=np.nan,
                            horizon_days=h,
                            model=model_type,
                            l2_penalty=l2_val,
                            n_scored=len(pooled_sq),
                            brier_score=round(float(np.mean(pooled_sq)), 4),
                            km_train_prob=np.nan,
                            pred_mean=round(float(np.mean(pooled_preds)), 4),
                            w_intercept=round(float(w_curr[0]), 4) if w_curr is not None else np.nan,
                            w_age=round(float(w_curr[1]), 4) if w_curr is not None else np.nan,
                            w_init=round(float(w_curr[2]), 4) if w_curr is not None else np.nan,
                            w_cur=round(float(w_curr[3]), 4) if w_curr is not None else np.nan,
                            w_z=round(float(w_curr[4]), 4) if w_curr is not None else np.nan
                        ))

    df_eval = pd.DataFrame(eval_records)
    df_eval.to_csv(OUT_TABLES / 'P3-30_model_eval.csv', index=False)

    # Review addition: is the selected model's gain over KM larger than episode-sampling noise?
    # Primary comparison: onset, h = 10, lambda selected on validation. Negative = model better.
    boot_rows = []
    for k in [3, 2, 4]:
        sel = models_by_k[k]['selected_l2']
        for split_name in ['validation', 'test']:
            for h in [5, 10, 20]:
                d = np.array(per_episode[(k, split_name, h, sel)]) - np.array(per_episode[(k, split_name, h, 'KM')])
                mean, lo, hi = paired_bootstrap(d)
                boot_rows.append(dict(threshold=k, split=split_name, horizon_days=h, selected_l2=sel,
                                      n_scored=len(d), brier_model_minus_km=round(mean, 4),
                                      ci95_low=round(lo, 4), ci95_high=round(hi, 4),
                                      model_better=bool(hi < 0), km_better=bool(lo > 0)))
    df_boot = pd.DataFrame(boot_rows)
    df_boot.to_csv(OUT_TABLES / 'P3-30_brier_bootstrap.csv', index=False)

    # 6. Plotting: Global survival curves & Hazard Model Predictions (Figure P3-30_global_survival.png)
    plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5), dpi=150)

    # Panel A: Kaplan-Meier Recovery Curve (Global 10 Pool vs Brazil acute spike fade)
    train_pool_k3 = global_splits_by_k[3]['train']
    days_grid = np.arange(1, 41)
    km_curve = [km(train_pool_k3, int(d), age=0) for d in days_grid]
    km_median = int(next(d for d, v in zip(days_grid, km_curve) if v >= 0.5))

    ax1.step(days_grid, km_curve, where='post', color='#1f77b4', lw=2.5, label='Training pool 2020-2024, 10 currencies (k=3)')
    ax1.axhline(0.50, color='#d62728', ls='--', lw=1.5, alpha=0.8,
                label=f'Median recovery = {km_median} days ({km(train_pool_k3, km_median, 0):.1%})')
    ax1.axvline(km_median, color='#d62728', ls=':', lw=1.5, alpha=0.8)

    # Key landmark annotations
    ax1.scatter([5, 10, 20], [km(train_pool_k3, 5, 0), km(train_pool_k3, 10, 0), km(train_pool_k3, 20, 0)],
                color='#1f77b4', s=60, zorder=5)
    ax1.annotate(f'5d: {km(train_pool_k3, 5, 0)*100:.1f}%', (5, km(train_pool_k3, 5, 0)),
                 xytext=(7, 0.05), arrowprops=dict(arrowstyle='->', color='#1f77b4'))
    ax1.annotate(f'10d: {km(train_pool_k3, 10, 0)*100:.1f}%', (10, km(train_pool_k3, 10, 0)),
                 xytext=(12, 0.23), arrowprops=dict(arrowstyle='->', color='#1f77b4'))
    ax1.annotate(f'20d: {km(train_pool_k3, 20, 0)*100:.1f}%\n(Median)', (20, km(train_pool_k3, 20, 0)),
                 xytext=(22, 0.44), arrowprops=dict(arrowstyle='->', color='#d62728'))

    # Review fix: the shaded 'Brazil 20-day spike' band was removed. Under this script's own rule the
    # Brazilian 2026 episode starts 25 May 2026 and is still open after 111 days (no 20-day match).
    ax1.set_title('Panel A: Kaplan-Meier recovery, training pool (k=3)', fontsize=12, fontweight='bold', pad=10)
    ax1.set_xlabel('Trading Days Since Shock Onset', fontsize=11)
    ax1.set_ylabel('Cumulative Recovery Probability', fontsize=11)
    ax1.set_ylim(-0.02, 1.02)
    ax1.set_xlim(0, 40)
    ax1.legend(loc='lower right', frameon=True, fontsize=9)

    # Panel B: Predicted Recovery Probability by Initial Shock Size from Penalized Hazard Model
    m3 = models_by_k[3]
    sel_k3 = m3['selected_l2']
    w_k3 = m3['weights'][sel_k3]  # review fix: plot the validation-selected penalty, not lambda = 1
    mu_k3 = m3['mu']
    sd_k3 = m3['sd']

    shock_sizes = np.linspace(25, 500, 100)
    median_sig = float(np.median([r['sigma_bps'] for r in train_pool_k3]))

    p_rec_10 = []
    p_rec_20 = []
    for s_bps in shock_sizes:
        # Horizon 10
        surv10 = 1.0
        for step in range(1, 11):
            f_s = np.array([
                np.log1p(step),
                np.log1p(max(0, s_bps)),
                np.sign(s_bps) * np.log1p(abs(s_bps)),
                np.clip(s_bps / median_sig, -5.0, 20.0)
            ])
            x_s = np.array([1.0, *((f_s - mu_k3) / sd_k3)])
            surv10 *= (1.0 - expit(np.dot(w_k3, x_s)))
        p_rec_10.append(1.0 - surv10)

        # Horizon 20
        surv20 = 1.0
        for step in range(1, 21):
            f_s = np.array([
                np.log1p(step),
                np.log1p(max(0, s_bps)),
                np.sign(s_bps) * np.log1p(abs(s_bps)),
                np.clip(s_bps / median_sig, -5.0, 20.0)
            ])
            x_s = np.array([1.0, *((f_s - mu_k3) / sd_k3)])
            surv20 *= (1.0 - expit(np.dot(w_k3, x_s)))
        p_rec_20.append(1.0 - surv20)

    ax2.plot(shock_sizes, p_rec_10, color='#2ca02c', lw=2.5, label=f'Predicted 10-day recovery (l2={sel_k3})')
    ax2.plot(shock_sizes, p_rec_20, color='#ff7f0e', lw=2.5, label=f'Predicted 20-day recovery (l2={sel_k3})')

    # Annotate test episodes
    test_k3 = global_splits_by_k[3]['test']
    for ep in test_k3:
        ex = ep['initial_excess_bps']
        if ex <= 500:
            rec_10_actual = 1 if (ep['event'] == 1 and ep['duration'] <= 10) else 0
            ax2.scatter(ex, rec_10_actual, color='purple' if rec_10_actual else 'red',
                        marker='o' if rec_10_actual else 'x', s=45, alpha=0.8)

    ax2.text(0.98, 0.70, f'w_init = {w_k3[2]:+.3f} (standardised)\nTest outcomes at 10 days: o recovered, x not',
             transform=ax2.transAxes, ha='right', fontsize=9,
             bbox=dict(boxstyle='round,pad=0.4', facecolor='white', alpha=0.9))

    ax2.set_title('Panel B: hazard model predictions by initial shock size (k=3)',
                  fontsize=12, fontweight='bold', pad=10)
    ax2.set_xlabel('Initial Shock Size (Excess bps Over 60d Median)', fontsize=11)
    ax2.set_ylabel('Predicted Recovery Probability', fontsize=11)
    ax2.set_ylim(-0.05, 1.05)
    ax2.set_xlim(20, 505)
    ax2.legend(loc='upper right', frameon=True, fontsize=9)

    plt.tight_layout()
    plt.savefig(OUT_FIGURES / 'P3-30_global_survival.png', dpi=150)
    plt.close(fig)

    # 7. Summary JSON (review fix: every number computed here, none typed in)
    def ev(split, h, model, k=3, scope='onset'):
        q = df_eval[(df_eval.threshold == k) & (df_eval.split == split) & (df_eval.horizon_days == h)
                    & (df_eval.evaluation_scope == scope) & (df_eval.model == model)]
        return float(q.brier_score.iloc[0])
    sel = models_by_k[3]['selected_l2']
    b = df_boot.set_index(['threshold', 'split', 'horizon_days'])
    fe = df_gates.set_index(['scope', 'threshold', 'split'])
    summary = dict(
        status='evaluated; reviewed 6 Nov 2026 (Renzo agent)',
        tests_passed=ntests,
        input_sha256_lf=provenance,
        feasibility={f'{sc}_k{k}_{sp}': f"{int(r.episodes)}/{int(r.recoveries)} ({'pass' if r.passed else 'fail'})"
                     for (sc, k, sp), r in fe.iterrows()},
        km_training_pool_k3=dict(
            horizon_5d=round(km(train_pool_k3, 5, 0), 4),
            horizon_10d=round(km(train_pool_k3, 10, 0), 4),
            horizon_20d=round(km(train_pool_k3, 20, 0), 4),
            median_recovery_days=km_median,
        ),
        primary_onset_10d_k3=dict(
            selected_l2=sel,
            validation=dict(km=ev('validation', 10, 'Kaplan-Meier'), model=ev('validation', 10, f'Hazard_l2_{sel}'),
                            n=int(b.loc[(3, 'validation', 10), 'n_scored']),
                            diff_ci95=[float(b.loc[(3, 'validation', 10), c]) for c in ['ci95_low', 'ci95_high']]),
            test=dict(km=ev('test', 10, 'Kaplan-Meier'), model=ev('test', 10, f'Hazard_l2_{sel}'),
                      n=int(b.loc[(3, 'test', 10), 'n_scored']),
                      diff_ci95=[float(b.loc[(3, 'test', 10), c]) for c in ['ci95_low', 'ci95_high']]),
        ),
        robustness_test_10d_model_minus_km={f'k{k}': float(b.loc[(k, 'test', 10), 'brier_model_minus_km']) for k in [2, 4]},
        test_pooled_ongoing_10d_k3=dict(km=ev('test', 10, 'KM', scope='pooled_ongoing_ages_0_5_10'),
                                        model=ev('test', 10, f'Hazard_l2_{sel}', scope='pooled_ongoing_ages_0_5_10')),
        test_episodes_k3=[f"{r['currency']} {r['start'].date()} d={r['duration']} e={r['event']}"
                          for r in global_splits_by_k[3]['test']],
    )

    with open(OUT_TABLES / 'P3-30_run_summary.json', 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2)

    print('=== Feasibility Summary ===')
    print(df_gates.to_string(index=False))
    print('\n=== Paired bootstrap, selected model minus KM ===')
    print(df_boot.to_string(index=False))
    print('\n=== Model Evaluation (k=3, Test 2026) ===')
    print(df_eval[(df_eval.threshold == 3) & (df_eval.split == 'test')].to_string(index=False))
    print('\n=== Run Summary ===')
    print(json.dumps(summary, indent=2))

if __name__ == '__main__':
    main()
