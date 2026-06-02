"""
pareto_front.py
Contrail mitigation Pareto front:
  x-axis — fuel penalty (% increase relative to unmitigated flight plan)
  y-axis — contrail energy forcing reduction (%)

Each point represents a flight re-routed to avoid persistent-contrail regions.
The Pareto front (non-dominated solutions) is highlighted. The knee point
balances maximum benefit with minimum cost.

Illustrative data consistent with Teoh et al. (2020) trade-off analysis.
Reference: Teoh et al. (2020), Environ. Sci. Technol. 54:2941-2950.

Output: pareto_front.pdf + pareto_front.png in scripts/
"""

import pathlib
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

_SCRIPTS = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(_SCRIPTS))

from figure_export import apply_style, save_figure

apply_style("print")

# ---------------------------------------------------------------------------
# Generate synthetic flight mitigation data
# Each point = one flight with a proposed re-routing
# ---------------------------------------------------------------------------
rng = np.random.default_rng(2024)
N = 180

# Fuel penalty: 0–15 %
fuel_pen = rng.exponential(scale=2.5, size=N).clip(0, 15)

# ERF reduction: loosely correlated with fuel penalty but with scatter
# High-penalty options tend to give high reduction; many low-penalty options
# give near-zero reduction (not in contrail-forming regions)
base_reduction = 70 * (1 - np.exp(-0.35 * fuel_pen))
noise = rng.normal(0, 8, N)
erf_red = (base_reduction + noise).clip(0, 98)

# Also add a cluster of high-value low-cost options (3-5 % fuel, 60-80 % ERF)
n_good = 25
fuel_pen_good = rng.uniform(2, 6, n_good)
erf_red_good  = rng.uniform(55, 82, n_good)
fuel_pen = np.concatenate([fuel_pen, fuel_pen_good])
erf_red  = np.concatenate([erf_red, erf_red_good])

# ---------------------------------------------------------------------------
# Compute Pareto front (minimise fuel_pen, maximise erf_red simultaneously)
# A point is dominated if another point has LOWER fuel_pen AND HIGHER erf_red.
# ---------------------------------------------------------------------------
def pareto_front(x, y):
    """Return mask of non-dominated points (min x, max y)."""
    dominated = np.zeros(len(x), dtype=bool)
    for i in range(len(x)):
        for j in range(len(x)):
            if i == j:
                continue
            if x[j] <= x[i] and y[j] >= y[i] and (x[j] < x[i] or y[j] > y[i]):
                dominated[i] = True
                break
    return ~dominated

mask = pareto_front(fuel_pen, erf_red)
pf_x = fuel_pen[mask]
pf_y = erf_red[mask]
order = np.argsort(pf_x)
pf_x, pf_y = pf_x[order], pf_y[order]

# ---------------------------------------------------------------------------
# Identify knee point via maximum curvature / distance from line joining ends
# ---------------------------------------------------------------------------
def knee_point(x, y):
    """Index of max perpendicular distance from line joining first to last point."""
    p1 = np.array([x[0], y[0]])
    p2 = np.array([x[-1], y[-1]])
    d = p2 - p1
    d_norm = d / np.linalg.norm(d)
    dists = []
    for xi, yi in zip(x, y):
        p = np.array([xi, yi])
        t = np.dot(p - p1, d_norm)
        proj = p1 + t * d_norm
        dists.append(np.linalg.norm(p - proj))
    return np.argmax(dists)

ki = knee_point(pf_x, pf_y)

# ---------------------------------------------------------------------------
# Figure
# ---------------------------------------------------------------------------
OI_BLUE  = "#0072B2"
OI_GREY  = "#BBBBBB"
OI_VERM  = "#D55E00"
OI_GREEN = "#009E73"

fig, ax = plt.subplots(figsize=(3.2, 2.6))

# All flights (background scatter)
ax.scatter(fuel_pen[~mask], erf_red[~mask],
           color=OI_GREY, s=8, alpha=0.6, linewidth=0, zorder=2,
           label="Re-routed flights")

# Pareto-optimal flights
ax.scatter(pf_x, pf_y,
           color=OI_BLUE, s=14, alpha=0.85, linewidth=0, zorder=4,
           label="Pareto-optimal")

# Pareto front line
ax.plot(pf_x, pf_y, color=OI_BLUE, linewidth=0.8, zorder=3, alpha=0.7)

# Knee point
ax.scatter([pf_x[ki]], [pf_y[ki]], color=OI_VERM, s=50, zorder=6,
           marker="*", label=f"Knee: {pf_x[ki]:.1f}% fuel, {pf_y[ki]:.0f}% ERF")
ax.annotate(
    f"  Knee point\n  ({pf_x[ki]:.1f} %, {pf_y[ki]:.0f} %)",
    xy=(pf_x[ki], pf_y[ki]),
    xytext=(pf_x[ki] + 1.2, pf_y[ki] - 12),
    fontsize=5.5, color=OI_VERM,
    arrowprops=dict(arrowstyle="-|>", color=OI_VERM, lw=0.6),
)

ax.set_xlabel("Fuel penalty (%)", fontsize=8)
ax.set_ylabel("Contrail ERF reduction (%)", fontsize=8)
ax.set_xlim(-0.5, 16)
ax.set_ylim(-2, 102)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

leg = ax.legend(fontsize=5.5, framealpha=0.85, edgecolor="#CCCCCC",
                loc="lower right", handlelength=1.0, scatterpoints=1)
leg.get_frame().set_linewidth(0.4)

fig.tight_layout()

out = save_figure(fig, "pareto_front", journal="egu", width="single",
                  height_scale=None, formats=["pdf", "png"], out_dir=_SCRIPTS)
plt.close(fig)
print("pareto_front: done —", [str(p) for p in out])
