"""
forcing_bar_chart.py
Aviation effective radiative forcing (ERF) components — horizontal bar chart.

Illustrative values derived from Lee et al. (2021) Table 2 central estimates
and 5–95 % uncertainty bounds. Clearly labeled as ILLUSTRATIVE — do not use
for quantitative analysis without consulting the primary source.

Reference: Lee et al. (2021), Atmospheric Environment 244:117834.
           https://doi.org/10.1016/j.atmosenv.2020.117834

Output: forcing_bar_chart.pdf + forcing_bar_chart.png in scripts/
"""

import pathlib
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# ---------------------------------------------------------------------------
# Resolve paths and import skill helpers
# ---------------------------------------------------------------------------
_SCRIPTS = pathlib.Path(__file__).resolve().parent
_SKILL_ROOT = _SCRIPTS.parent
sys.path.insert(0, str(_SCRIPTS))

from figure_export import apply_style, save_figure

# Apply print style
apply_style("print")

# Also import palette
sys.path.insert(0, str(_SKILL_ROOT / "assets"))
from palettes import WARMING_COOLING

# ---------------------------------------------------------------------------
# Data — illustrative, Lee et al. (2021)-like central estimates and 5–95 % CI
# Units: mW m⁻²  (positive = warming, negative = cooling)
# ---------------------------------------------------------------------------
# (label, best_estimate, lower_5pct, upper_95pct)
# lower/upper are the ABSOLUTE uncertainty bounds (not relative to estimate)
COMPONENTS = [
    # label                   best   low    high
    ("Contrail cirrus",        57.4,  17.0,  98.0),
    ("CO$_2$",                 34.3,  28.0,  40.0),
    ("NO$_x$ (net)",            7.4,  -4.0,  30.0),
    ("Water vapour",            0.9,   0.2,   1.8),
    ("Aerosol–radiation",      -4.4,  -7.0,  -1.0),
    ("Aerosol–cloud",          -5.0, -21.0,   0.6),
    ("Contrail (linear only)",  6.3,   3.0,  12.0),
]

# Net total (sum of non-contrail-overlap components — not purely additive)
NET_BEST  = 100.9
NET_LOW   =  55.0
NET_HIGH  = 145.0
NET_LABEL = "Net aviation ERF"

# Order by absolute magnitude of best estimate (largest at top)
COMPONENTS_SORTED = sorted(COMPONENTS, key=lambda x: abs(x[1]), reverse=True)

labels = [c[0] for c in COMPONENTS_SORTED]
bests  = np.array([c[1] for c in COMPONENTS_SORTED])
lows   = np.array([c[2] for c in COMPONENTS_SORTED])
highs  = np.array([c[3] for c in COMPONENTS_SORTED])

# Asymmetric error bar sizes (distance from best estimate to each bound)
xerr_lo = bests - lows    # positive = leftward whisker length
xerr_hi = highs - bests   # positive = rightward whisker length

# Colors: warming=positive, cooling=negative
colors = [
    WARMING_COOLING["positive"] if v > 0 else WARMING_COOLING["negative"]
    for v in bests
]

# ---------------------------------------------------------------------------
# Build figure
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(3.5, 3.0))

y_pos = np.arange(len(labels))
BAR_H = 0.55

# Component bars
ax.barh(
    y_pos, bests, height=BAR_H, color=colors, zorder=3, alpha=0.9,
    linewidth=0, edgecolor="none",
)

# Asymmetric error bars (5–95 %)
ax.errorbar(
    bests, y_pos,
    xerr=[np.maximum(0, xerr_lo), np.maximum(0, xerr_hi)],
    fmt="none",
    ecolor="#2C3E50",
    elinewidth=0.8,
    capsize=2.5,
    capthick=0.8,
    zorder=4,
)

# Net total — separate bar below, with gap
NET_Y = -2.0
ax.barh(
    NET_Y, NET_BEST, height=BAR_H,
    color=WARMING_COOLING["total"], zorder=3, alpha=0.95,
    linewidth=0, edgecolor="none",
)
ax.errorbar(
    NET_BEST, NET_Y,
    xerr=[[NET_BEST - NET_LOW], [NET_HIGH - NET_BEST]],
    fmt="none",
    ecolor="#2C3E50",
    elinewidth=0.8,
    capsize=2.5,
    capthick=0.8,
    zorder=4,
)

# Zero reference line — drawn above the bars so it reads as a clean vertical axis
ax.axvline(0, color=WARMING_COOLING["zero_line"], linewidth=0.8, zorder=5)

# Axis formatting
all_y = list(y_pos) + [NET_Y]
all_labels = labels + [NET_LABEL]
ax.set_yticks(all_y)
ax.set_yticklabels(all_labels, fontsize=7)

# Separator line between components and total
ax.axhline(-1.1, color="#AAAAAA", linewidth=0.5, linestyle="--", zorder=1)

ax.set_xlabel("ERF (mW m$^{-2}$)", fontsize=8)
ax.set_xlim(-30, 160)
ax.set_ylim(-2.7, len(labels) - 0.5)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.tick_params(left=False)

# Lightweight vertical grid on x-axis only
ax.xaxis.grid(True, linestyle=":", linewidth=0.3, color="#BBBBBB", zorder=0)
ax.set_axisbelow(True)

# Legend patches
warm_patch = mpatches.Patch(color=WARMING_COOLING["positive"], label="Warming")
cool_patch = mpatches.Patch(color=WARMING_COOLING["negative"], label="Cooling")
leg = ax.legend(
    handles=[warm_patch, cool_patch],
    fontsize=6.5, framealpha=0.8,
    loc="upper right", handlelength=1.0, handleheight=0.8,
    edgecolor="#CCCCCC",
)
leg.get_frame().set_linewidth(0.4)

fig.tight_layout()

# ---------------------------------------------------------------------------
# Export
# ---------------------------------------------------------------------------
out = save_figure(fig, "forcing_bar_chart", journal="egu", width="single",
                  height_scale=None, formats=["pdf", "png"],
                  out_dir=_SCRIPTS)
plt.close(fig)
print("forcing_bar_chart: done —", [str(p) for p in out])
