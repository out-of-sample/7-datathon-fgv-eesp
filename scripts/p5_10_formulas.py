"""P5-10: render the methods-slide formulas as LaTeX images (deck v4, slide 3).

Inputs: none (formulas are written below). Needs a LaTeX install (pdflatex + dvipng).
Outputs: results/figures/P5-10_eq_<name>.png, rendered at 2x (show at half the pixel size).
Run: .venv/bin/python scripts/p5_10_formulas.py
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams.update({"text.usetex": True,
                     "text.latex.preamble": r"\usepackage{amsmath,amssymb,bm}"})
INK = "#14213D"
OUT = Path("results/figures")
FS, DPI = 11.5, 350  # 11.5 pt at 350 dpi, shown at half size: ~28 px per em on the 1920-px slide

EQ = {
    "quebras": r"$\min\limits_{T_1,\dots,T_m}\ \sum_{j=1}^{m+1}\sum_{t\in T_j}\left(p_t-\mu_j\right)^2$",
    "evento_p": r"$\begin{gathered}\Delta_e=\bar p_{[+1,+20]}-\bar p_{[-20,-1]}\\ \hat\pi=\dfrac{1+\#\{s:|\Delta_s|\ge|\Delta_e|\}}{1+N}\end{gathered}$",
    "sintetico": r"$\min\limits_{\mathbf{w}}\ \sum_{t<T_0}\Big(p_t^{\mathrm{BR}}-\sum_j w_j\,p_t^{\,j}\Big)^2$",
    "bandtar": r"$\Delta z_t=\beta\,\big(z_{t-1}-c\,\mathrm{sgn}\,z_{t-1}\big)+\varepsilon_t$",
    "fluxos": r"$\hat\pi=\left(1+\#\{m:\,g_m\le g_{\mathrm{jul}}\}\right)/(1+n)$",  # p3_10_imports.py T1
    "ordens": r"$\mathrm{OF}_t^{\,\mathrm{tarde}}=\alpha+\beta_1\,p_t+\beta_2\,g_t^{\mathrm{Fox/Bin}}+\varepsilon_t$",  # p3_19 daily OLS
    "transferencia": r"$T=\sum_{t\,\in\,\mathrm{choque}}\left(p_t-\bar p_{\mathrm{pr\acute{e}}}\right)V_t\,\mathrm{PTAX}_t$",  # p3_11_money.py
    "ledger": r"$\Delta S_t=\sum \mathrm{mint}_t-\sum \mathrm{burn}_t$",
    "cusum": r"$S_t^{+}=\max\left(0,\ S_{t-1}^{+}+z_t-k\right)$",
    "hazard": r"$h_\tau(x)=\Lambda\left(\alpha_\tau+\bm\beta^{\top}x\right)$",
}

# Larger renders for the problem-definition slide: the premium formula and its symbols, explained one by one.
BIG = {
    "premio_big": (r"$p_t=\dfrac{P_t^{\mathrm{USDT/BRL}}}{\mathrm{PTAX}_t\cdot P_t^{\mathrm{USDT/USD}}}-1$", 17),
    "sym_brl": (r"$P_t^{\mathrm{USDT/BRL}}$", 12.5),
    "sym_ptax": (r"$\mathrm{PTAX}_t$", 12.5),
    "sym_usd": (r"$P_t^{\mathrm{USDT/USD}}$", 12.5),
    # On-chain route (slide 6): BRLA per USDC on the Polygon pool over PTAX, assuming 1 BRLA = R$ 1 (P3-24)
    # Market slide (slide 7): how each of the three panels is measured (F-022, F-024, F-036)
    "resto": (r"$\Delta=\bar p_{[+21,\,+60]}-\bar p_{[-20,\,-1]}$", 12.5),
    "fatia": (r"$s^{\mathrm{Fox}}=\frac{V^{\mathrm{Fox}}}{V^{\mathrm{Bin}}+V^{\mathrm{Fox}}+V^{\mathrm{MB}}}$", 12.5),
    # Slide 8: value of waiting h days with a currency hedge (F-055, P3-48)
    "espera": (r"$W=q\,X_T\left[U_t\,(1+p_t)-U_T\,(1+p_T)\right]$", 11.5),
    "espera_m": (r"$W=q\,X_T\left[U_t\,(1+p_t)-U_T\,(1+p_T)\right]$", 8.7),  # narrower, methods slide
    # Slide 9: the waiting rule tested on every decision date (F-055)
    "regra": (r"$\text{esperar se }\; g_t=p_t-\mathrm{med}\left(p_{t-60},\ldots,p_{t-1}\right)>k$", 11.5),
    "premio_onchain": (r"$p_t^{\mathrm{on\text{-}chain}}=\dfrac{P_t^{\mathrm{USDC/BRLA}}}{\mathrm{PTAX}_t}-1$", 14),
}

for name, (tex, size) in {**{k: (v, FS) for k, v in EQ.items()}, **BIG}.items():
    fig = plt.figure(figsize=(0.01, 0.01))
    fig.text(0, 0, tex, fontsize=size, color=INK)
    path = OUT / f"P5-10_eq_{name}.png"
    fig.savefig(path, dpi=DPI, transparent=True, bbox_inches="tight", pad_inches=0.02)
    plt.close(fig)
    print(path)
