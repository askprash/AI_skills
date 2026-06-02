"""
palettes.py — Color palettes for research-figures skill.

Provides:
    OKABE_ITO       : 8-color colorblind-safe palette (Okabe & Ito 2008)
    WARMING_COOLING : diverging scheme for forcing charts (warm=positive, cool=negative)
    get_forcing_color(value) : returns warming or cooling color for a scalar forcing value
    forcing_palette(values)  : list of colors mapped to sign of each value
    COLORMAP_RECS   : recommended perceptually-uniform colormaps by use case
"""

from __future__ import annotations
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from typing import Sequence

# ---------------------------------------------------------------------------
# Okabe-Ito 8-color palette (Okabe & Ito 2008, coloruniversaldesign.com)
# Safe for deuteranopia, protanopia, and tritanopia.
# ---------------------------------------------------------------------------
OKABE_ITO = {
    "blue":          "#0072B2",
    "vermilion":     "#D55E00",
    "bluish_green":  "#009E73",
    "reddish_purple":"#CC79A7",
    "sky_blue":      "#56B4E9",
    "orange":        "#E69F00",
    "yellow":        "#F0E442",
    "black":         "#000000",
}

# As an ordered list (drop yellow for most uses — poor on white)
OKABE_ITO_LIST = [
    "#0072B2",  # blue
    "#D55E00",  # vermilion
    "#009E73",  # bluish green
    "#CC79A7",  # reddish purple
    "#56B4E9",  # sky blue
    "#E69F00",  # orange
    "#F0E442",  # yellow
    "#000000",  # black
]

# ---------------------------------------------------------------------------
# Warming / Cooling diverging scheme for aviation forcing bar charts.
# Positive ERF (warming) → warm reds/oranges; negative (cooling) → blues.
# Based on Lee et al. (2021) convention.
# ---------------------------------------------------------------------------
WARMING_COOLING = {
    "strong_warm":  "#C0392B",   # deep red — large positive forcing
    "warm":         "#E74C3C",   # red
    "mild_warm":    "#F39C12",   # amber/orange — small positive
    "neutral":      "#7F8C8D",   # grey — near-zero / uncertain sign
    "mild_cool":    "#5DADE2",   # light blue — small negative
    "cool":         "#2980B9",   # blue
    "strong_cool":  "#154360",   # deep blue — large negative
    # Convenience aliases used in forcing_bar_chart
    "positive":     "#D55E00",   # Okabe-Ito vermilion (warming)
    "negative":     "#0072B2",   # Okabe-Ito blue (cooling)
    "total":        "#2C3E50",   # dark charcoal for net total bar
    "zero_line":    "#555555",   # color for the zero reference line
}


def get_forcing_color(value: float, threshold: float = 0.0) -> str:
    """Return a hex color string: warm if value > threshold, cool otherwise."""
    return WARMING_COOLING["positive"] if value > threshold else WARMING_COOLING["negative"]


def forcing_palette(values: Sequence[float]) -> list[str]:
    """Return a list of hex colors, one per value, mapped to sign."""
    return [get_forcing_color(v) for v in values]


# ---------------------------------------------------------------------------
# Recommended perceptually-uniform colormaps by use case.
# Never use 'jet' — it creates false gradient perception and fails grayscale.
# ---------------------------------------------------------------------------
COLORMAP_RECS = {
    # Sequential — for physical fields with one meaningful extreme
    "default_sequential":        "viridis",
    "altitude_or_pressure":      "cividis",   # deuteranopia-safe alternative to viridis
    "temperature_anomaly_seq":   "inferno",   # dark background contours
    "fuel_burn_density":         "plasma",
    # Diverging — for anomalies / differences centred at zero
    "forcing_diverging":         "RdBu_r",    # warm positive / cool negative
    "temperature_diff":          "coolwarm",
    "delta_performance":         "PiYG",
    # Qualitative
    "categorical_8":             OKABE_ITO_LIST,
    # NOT recommended
    "_avoid":                    ["jet", "rainbow", "hsv", "spectral"],
}


def register_okabe_ito_cycle():
    """Register Okabe-Ito as the default matplotlib color cycle."""
    import matplotlib as mpl
    from cycler import cycler
    mpl.rcParams["axes.prop_cycle"] = cycler(color=OKABE_ITO_LIST)


def demo_palettes(save_path: str | None = None):
    """Quick visual check of the palettes — useful during figure development."""
    fig, axes = plt.subplots(1, 2, figsize=(10, 3))

    # Okabe-Ito swatches
    ax = axes[0]
    for i, (name, color) in enumerate(OKABE_ITO.items()):
        ax.barh(i, 1, color=color, edgecolor="white", linewidth=0.5)
        ax.text(1.05, i, name, va="center", fontsize=9)
    ax.set_xlim(0, 2.2)
    ax.set_yticks([])
    ax.set_title("Okabe-Ito palette", fontsize=10)
    ax.axis("off")

    # Warming/cooling swatches
    ax = axes[1]
    wc_keys = ["strong_warm", "warm", "mild_warm", "neutral", "mild_cool", "cool", "strong_cool"]
    for i, key in enumerate(wc_keys):
        ax.barh(i, 1, color=WARMING_COOLING[key], edgecolor="white", linewidth=0.5)
        ax.text(1.05, i, key, va="center", fontsize=9)
    ax.set_xlim(0, 2.5)
    ax.set_yticks([])
    ax.set_title("Warming/Cooling diverging", fontsize=10)
    ax.axis("off")

    fig.tight_layout()
    if save_path:
        fig.savefig(save_path, dpi=150, bbox_inches="tight")
    else:
        plt.show()
    return fig


if __name__ == "__main__":
    demo_palettes()
    print("Okabe-Ito list:", OKABE_ITO_LIST)
    print("Forcing colors for +10, -5:", forcing_palette([10, -5]))
