"""
drag_polar.py
Dual-panel aerodynamics figure:
  Panel A — drag polar: C_L vs C_D (incl. parabolic fit and design point)
  Panel B — L/D vs angle of attack alpha

Illustrative values representative of a clean transonic transport wing
(e.g. BWB or tube-and-wing at M 0.80). Not from a specific aircraft.

Output: drag_polar.pdf + drag_polar.png in scripts/
"""

import pathlib
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

_SCRIPTS = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(_SCRIPTS))

from figure_export import apply_style, save_figure, add_panel_label

apply_style("print")

# ---------------------------------------------------------------------------
# Aerodynamics model — parabolic drag polar
# C_D = CD0 + k * C_L^2
# ---------------------------------------------------------------------------
CD0 = 0.0155       # zero-lift drag coefficient
k   = 0.0365       # induced drag factor (≈1/(pi*AR*e), AR~9, e~0.85)
CL_max = 1.45      # max lift coefficient (clean)

CL = np.linspace(0.0, CL_max, 200)
CD = CD0 + k * CL**2

# L/D vs alpha (linear lift slope below stall + rudimentary stall model)
alpha_range = np.linspace(-4, 18, 200)   # degrees
CL_a = 2 * np.pi * (alpha_range - (-2.5)) * np.pi / 180   # simple 2π slope, alpha_0 = -2.5°
# Gentle stall above alpha ~ 14°
stall = np.where(alpha_range > 14.0,
                 CL_a * np.exp(-0.35 * (alpha_range - 14.0)**2),
                 CL_a)
stall = np.clip(stall, 0, None)   # no negative CL below alpha_0 for this plot
CD_alpha = CD0 + k * stall**2
with np.errstate(divide="ignore", invalid="ignore"):
    LD = np.where(CD_alpha > 0.002, stall / CD_alpha, np.nan)

# Design / max L/D point from analytical formula
CL_opt = np.sqrt(CD0 / k)
CD_opt = 2 * CD0
LD_max = CL_opt / CD_opt

# Corresponding alpha for CL_opt
alpha_opt = (CL_opt / (2 * np.pi * np.pi / 180)) + (-2.5)

# ---------------------------------------------------------------------------
# Figure — two panels
# ---------------------------------------------------------------------------
OI_BLUE = "#0072B2"
OI_VERM = "#D55E00"
OI_GREEN = "#009E73"

fig = plt.figure(figsize=(3.4, 2.5))
gs = gridspec.GridSpec(1, 2, wspace=0.42, left=0.12, right=0.97,
                       top=0.91, bottom=0.15)
ax1 = fig.add_subplot(gs[0])
ax2 = fig.add_subplot(gs[1])

# --- Panel A: drag polar ---
ax1.plot(CD, CL, color=OI_BLUE, linewidth=1.2, zorder=3)
# Design point (max L/D)
ax1.scatter([CD_opt], [CL_opt], color=OI_VERM, s=20, zorder=5,
            label=f"Max L/D\n= {LD_max:.1f}")
ax1.annotate(f" (L/D)$_{{\\rm max}}$={LD_max:.0f}",
             xy=(CD_opt, CL_opt), fontsize=5.5, color=OI_VERM,
             xytext=(CD_opt + 0.003, CL_opt - 0.08))

# Constant L/D tangent lines
for ld_val, ls_ in [(12, ":"), (LD_max, "--")]:
    cd_line = np.linspace(0.0, 0.04, 50)
    cl_line = ld_val * cd_line
    ax1.plot(cd_line, cl_line, color="#AAAAAA", linewidth=0.5,
             linestyle=ls_, zorder=1)
    ax1.text(0.038, ld_val * 0.038 + 0.02, f"L/D={ld_val:.0f}",
             fontsize=5, color="#999999", ha="right")

ax1.set_xlabel("$C_D$", fontsize=8)
ax1.set_ylabel("$C_L$", fontsize=8)
ax1.set_xlim(0.010, 0.105)
ax1.set_ylim(0.0, 1.55)
leg = ax1.legend(fontsize=5.5, loc="upper left", framealpha=0.8,
                 edgecolor="#CCCCCC", handlelength=0.8)
leg.get_frame().set_linewidth(0.4)
ax1.spines["top"].set_visible(False)
ax1.spines["right"].set_visible(False)

# --- Panel B: L/D vs alpha ---
ax2.plot(alpha_range, LD, color=OI_GREEN, linewidth=1.2, zorder=3)
# Mark max L/D point
LD_arr = LD.copy()
LD_arr[np.isnan(LD_arr)] = 0
idx_max = np.argmax(LD_arr)
ax2.scatter([alpha_range[idx_max]], [LD_arr[idx_max]],
            color=OI_VERM, s=20, zorder=5)
ax2.axhline(LD_max, color="#AAAAAA", linewidth=0.5, linestyle="--", zorder=1)
ax2.text(16.5, LD_max + 0.3, f"{LD_max:.0f}", fontsize=5.5,
         color="#AAAAAA", va="bottom", ha="right")

# Stall annotation
ax2.axvline(14.0, color="#888888", linewidth=0.5, linestyle=":", zorder=1)
ax2.text(14.2, 2.5, "Stall", fontsize=5.5, color="#888888")

ax2.set_xlabel(r"$\alpha$ (°)", fontsize=8)
ax2.set_ylabel("L/D", fontsize=8)
ax2.set_xlim(-4, 18)
ax2.set_ylim(0, 22)
ax2.spines["top"].set_visible(False)
ax2.spines["right"].set_visible(False)

# Panel labels (a)/(b). Titles and source/provenance go in the manuscript caption.
add_panel_label(ax1, "(a)")
add_panel_label(ax2, "(b)")

out = save_figure(fig, "drag_polar", journal="aiaa", width="double",
                  height_scale=None, formats=["pdf", "png"], out_dir=_SCRIPTS)
plt.close(fig)
print("drag_polar: done —", [str(p) for p in out])
