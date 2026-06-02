"""
time_series_uncertainty.py
Annual aviation contrail ERF time series (1990–2022) with uncertainty band
and a visible 2020 COVID-19 activity dip.

Illustrative data based on trends consistent with Lee et al. (2021) and
Teoh et al. (2024). Not intended for quantitative citation.

Output: time_series_uncertainty.pdf + .png in scripts/
"""

import pathlib
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

_SCRIPTS = pathlib.Path(__file__).resolve().parent
_SKILL_ROOT = _SCRIPTS.parent
sys.path.insert(0, str(_SCRIPTS))

from figure_export import apply_style, save_figure

apply_style("print")

# ---------------------------------------------------------------------------
# Synthetic annual contrail ERF (mW m⁻²) 1990–2022
# Constructed to be consistent with:
#   ~10 mW m⁻² in 1990, rising to ~57 mW m⁻² by 2018,
#   sharp COVID dip to ~15 mW m⁻² in 2020, partial recovery.
# ---------------------------------------------------------------------------
rng = np.random.default_rng(42)
years = np.arange(1990, 2023)
n = len(years)

# Logistic-ish growth scaled to reach ~57 mW m⁻² by 2018
def logistic(t, L=57, k=0.12, t0=2004):
    return L / (1 + np.exp(-k * (t - t0)))

central = logistic(years.astype(float))

# COVID dip: 2020 → sharp drop, 2021 partial, 2022 near recovery
covid_factor = np.ones(n)
covid_factor[years == 2020] = 0.27   # ~73 % reduction in RPK
covid_factor[years == 2021] = 0.55
covid_factor[years == 2022] = 0.80

central = central * covid_factor

# Small year-to-year variability (meteorological interannual)
noise = rng.normal(0, 1.5, n)
central = central + noise

# Uncertainty band ±20 % of central (5–95 % illustrative)
frac_lo = 0.60   # lower = 40 % below central
frac_hi = 1.50   # upper = 50 % above central
lower = central * frac_lo
upper = central * frac_hi

# ---------------------------------------------------------------------------
# Figure
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(3.4, 2.4))

# Shaded uncertainty band — clean soft fill, no edge stroke
ax.fill_between(years, lower, upper, alpha=0.20, color="#0072B2",
                linewidth=0, edgecolor="none", label="5–95 % range")

# Central estimate line
ax.plot(years, central, color="#0072B2", linewidth=1.2, zorder=3, label="Best estimate")

# COVID annotation
covid_val = central[years == 2020][0]
ax.annotate(
    "COVID-19\n(2020)",
    xy=(2020, covid_val),
    xytext=(2015.5, covid_val + 8),
    fontsize=6,
    arrowprops=dict(arrowstyle="-|>", color="#555555",
                    connectionstyle="arc3,rad=-0.25",
                    lw=0.7),
    color="#555555",
)

ax.set_xlabel("Year", fontsize=8)
ax.set_ylabel("Contrail cirrus ERF (mW m$^{-2}$)", fontsize=8)
ax.set_xlim(1990, 2022)
ax.set_ylim(0, None)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

leg = ax.legend(fontsize=6.5, framealpha=0.8, edgecolor="#CCCCCC",
                loc="upper left")
leg.get_frame().set_linewidth(0.4)

fig.tight_layout()

out = save_figure(fig, "time_series_uncertainty", journal="acp", width="single",
                  height_scale=None, formats=["pdf", "png"], out_dir=_SCRIPTS)
plt.close(fig)
print("time_series_uncertainty: done —", [str(p) for p in out])
