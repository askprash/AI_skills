"""
gci_convergence.py
Grid-convergence study plot for AIAA V&V requirements.

Shows a target quantity Q (e.g. lift coefficient C_L, thrust coefficient C_T,
or total pressure recovery) vs mesh refinement parameter h, along with:
  - Richardson-extrapolated value Q_exact
  - GCI bands (fine-grid and medium-grid GCI)
  - Observed order of convergence p

Illustrative data representing a RANS simulation of a transonic inlet.
GCI computed per Roache (1994) / Celik et al. (2008) ASME standard.

References:
  Roache (1994), J. Fluids Eng. 116:405.
  Celik et al. (2008), J. Fluids Eng. 130:078001.

Output: gci_convergence.pdf + gci_convergence.png in scripts/
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
from labellines import labelLine

apply_style("print")

# ---------------------------------------------------------------------------
# Mesh levels and simulated quantity
# h = characteristic mesh spacing (normalized so coarsest = 1.0)
# Q = total pressure recovery (illustrative RANS result)
# ---------------------------------------------------------------------------
# Four mesh levels (coarse→fine), h proportional to element size
h_vals   = np.array([1.000, 0.500, 0.250, 0.125])   # normalized
Q_sim    = np.array([0.9521, 0.9618, 0.9664, 0.9678])  # simulated recovery

# Add a small scatter to look realistic
rng = np.random.default_rng(7)
Q_sim_noisy = Q_sim + rng.normal(0, 0.0003, 4)

# Richardson extrapolation using the two finest meshes
# p = log((Q3-Q2)/(Q2-Q1)) / log(r), r = refinement ratio
h1, h2, h3 = h_vals[3], h_vals[2], h_vals[1]
Q1, Q2, Q3 = Q_sim[3], Q_sim[2], Q_sim[1]
r21 = h2 / h1
r32 = h3 / h2

# Observed order (using three finest meshes)
eps21 = Q2 - Q1
eps32 = Q3 - Q2
if abs(eps21) > 1e-10 and abs(eps32) > 1e-10:
    p_obs = np.log(abs(eps32 / eps21)) / np.log(r21)
else:
    p_obs = 2.0  # fallback

Q_exact_RE = Q1 + (Q1 - Q2) / (r21**p_obs - 1)

# GCI (Roache; Fs=1.25 for 3+ meshes)
Fs = 1.25
GCI_fine   = Fs * abs(eps21) / (r21**p_obs - 1) / Q_exact_RE
GCI_medium = Fs * abs(eps32) / (r32**p_obs - 1) / Q_exact_RE

print(f"  Observed order p = {p_obs:.2f}")
print(f"  Richardson extrapolated Q_exact = {Q_exact_RE:.6f}")
print(f"  GCI_fine   = {GCI_fine*100:.3f} %")
print(f"  GCI_medium = {GCI_medium*100:.3f} %")

# ---------------------------------------------------------------------------
# Figure
# ---------------------------------------------------------------------------
OI_BLUE  = "#0072B2"
OI_VERM  = "#D55E00"
OI_GREEN = "#009E73"
OI_GREY  = "#888888"

fig, ax = plt.subplots(figsize=(3.2, 2.5))

# GCI bands around fine and medium mesh points
Q_fine_val   = Q_sim[3]
Q_medium_val = Q_sim[2]
h_fine       = h_vals[3]
h_medium     = h_vals[2]

ax.errorbar([h_fine], [Q_fine_val],
            yerr=[[GCI_fine * Q_exact_RE], [GCI_fine * Q_exact_RE]],
            fmt="none", ecolor=OI_BLUE, elinewidth=0.6, capsize=2.5, capthick=0.6,
            zorder=4, label=f"GCI$_{{\\rm fine}}$ = {GCI_fine*100:.2f} %")

ax.errorbar([h_medium], [Q_medium_val],
            yerr=[[GCI_medium * Q_exact_RE], [GCI_medium * Q_exact_RE]],
            fmt="none", ecolor=OI_GREEN, elinewidth=0.6, capsize=2.5, capthick=0.6,
            zorder=4, label=f"GCI$_{{\\rm medium}}$ = {GCI_medium*100:.2f} %")

# RANS data points (markers kept small; the main line is the thickest element).
rans_line, = ax.plot(h_vals, Q_sim_noisy, "o-", color=OI_BLUE, linewidth=1.0,
                     markersize=3.0, zorder=6)

# Richardson-extrapolated value (h -> 0), drawn in data coords so it can be
# labelled inline rather than via an arrowed annotation.
re_line, = ax.plot([0.0, 1.10], [Q_exact_RE, Q_exact_RE], color=OI_VERM,
                   linewidth=0.9, linestyle="--", zorder=3)

# Label the line series directly on the line with labelLines — preferred over a
# legend entry or an arrowed annotation for labelling curves.
labelLine(rans_line, 0.74, label="RANS simulation", align=True,
          fontsize=5.5, color=OI_BLUE, zorder=10, outline_width=2)
labelLine(re_line, 0.45, label=f"RE extrapolation = {Q_exact_RE:.4f}", align=True,
          fontsize=5.5, color=OI_VERM, zorder=10, outline_width=2)

# Order of convergence annotation — high zorder so no line/marker covers it,
# placed in the empty lower-left region.
ax.text(0.05, 0.10,
        f"Observed order $p={p_obs:.1f}$",
        transform=ax.transAxes, fontsize=6, color=OI_GREY, zorder=10)

ax.set_xlabel("Mesh spacing $h$ (normalized)", fontsize=8)
ax.set_ylabel("Total pressure recovery $\\eta_p$", fontsize=8)
ax.set_xlim(-0.02, 1.10)
ax.set_ylim(0.948, 0.975)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

leg = ax.legend(fontsize=5.5, framealpha=0.85, edgecolor="#CCCCCC",
                loc="upper right", handlelength=1.2)
leg.get_frame().set_linewidth(0.4)

fig.tight_layout()

out = save_figure(fig, "gci_convergence", journal="aiaa", width="single",
                  height_scale=None, formats=["pdf", "png"], out_dir=_SCRIPTS)
plt.close(fig)
print("gci_convergence: done —", [str(p) for p in out])
