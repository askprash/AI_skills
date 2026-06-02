"""
figure_export.py — Export helper for research-figures skill.

Key functions
-------------
apply_style(variant)
    Load prash_slides.mplstyle or prash_print.mplstyle from the assets/ directory.

save_figure(fig, name, journal, width, formats, out_dir, dpi_override)
    Resize fig to the correct column width and DPI for the target journal,
    then write PDF and/or PNG.

grayscale_preview(path)
    Load a saved PNG/TIFF and display it in grayscale to check legibility
    without color.

Journal specs (from references/journal_guidelines.md)
-------------------------------------------------------------
E&ES (RSC)   : 600 dpi TIFF, single 86 mm / double 174 mm
AIAA         : line-art 600 dpi / photos 300 dpi, single 3.25 in / double 7 in, >=8 pt fonts
EGU (ACP/AMT): 300 dpi vector, single ~83 mm / double ~170 mm, embed fonts
AGU          : 300-600 dpi, single ~89 mm / double ~178 mm, 8 pt fonts
Nature family: 300 dpi, single 90 mm / double 180 mm, 5-7 pt fonts
Science      : 300 dpi, single 89 mm / double 127 mm / triple 185 mm
"""

from __future__ import annotations
import os
import sys
import pathlib
import warnings
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# ---------------------------------------------------------------------------
# Resolve paths
# ---------------------------------------------------------------------------
_THIS_DIR = pathlib.Path(__file__).resolve().parent          # scripts/
_SKILL_ROOT = _THIS_DIR.parent                               # research-figures/
_ASSETS_DIR = _SKILL_ROOT / "assets"


def _style_path(variant: str) -> str:
    name = "prash_slides.mplstyle" if variant == "slides" else "prash_print.mplstyle"
    p = _ASSETS_DIR / name
    if not p.exists():
        raise FileNotFoundError(f"Style file not found: {p}")
    return str(p)


def apply_style(variant: str = "print") -> None:
    """
    Apply the named style variant.

    Parameters
    ----------
    variant : 'print' | 'slides'
        'print'  → prash_print.mplstyle  (7-9 pt labels, thinner lines, grid off)
        'slides' → prash_slides.mplstyle (14-18 pt labels, thick lines, grid on)
    """
    if variant not in ("print", "slides"):
        raise ValueError(f"variant must be 'print' or 'slides', got {variant!r}")
    matplotlib.style.use(_style_path(variant))


# ---------------------------------------------------------------------------
# Journal specs table
# ---------------------------------------------------------------------------
# Each entry: (single_mm, double_mm, triple_mm_or_None, dpi_line_art, dpi_raster, notes)
_MM_PER_INCH = 25.4

_JOURNAL_SPECS: dict[str, dict] = {
    # E&ES = Environmental Science & Engineering (RSC)
    "ees": dict(
        single_mm=86.0, double_mm=174.0, triple_mm=None,
        dpi_line=600, dpi_raster=600,
        notes="TIFF preferred; embed fonts; 600 dpi for all artwork",
    ),
    # AIAA journals (Journal of Aircraft, AIAA Journal, JPP, etc.)
    "aiaa": dict(
        single_mm=82.55,   # 3.25 in
        double_mm=177.8,   # 7.0 in
        triple_mm=None,
        dpi_line=600, dpi_raster=300,
        notes=">=8 pt fonts at final size; line art 600 dpi; photos 300 dpi",
    ),
    # EGU journals: ACP, AMT, GMD, etc.
    "egu": dict(
        single_mm=83.0, double_mm=170.0, triple_mm=None,
        dpi_line=300, dpi_raster=300,
        notes="Vector (PDF/EPS) strongly preferred; embed fonts",
    ),
    "acp": dict(
        single_mm=83.0, double_mm=170.0, triple_mm=None,
        dpi_line=300, dpi_raster=300,
        notes="Alias for EGU / ACP",
    ),
    "amt": dict(
        single_mm=83.0, double_mm=170.0, triple_mm=None,
        dpi_line=300, dpi_raster=300,
        notes="Alias for EGU / AMT",
    ),
    # AGU journals: GRL, JGR-Atmos, AGU Advances, etc.
    "agu": dict(
        single_mm=89.0, double_mm=178.0, triple_mm=None,
        dpi_line=600, dpi_raster=300,
        notes="300-600 dpi; 8 pt minimum fonts",
    ),
    "grl": dict(
        single_mm=89.0, double_mm=178.0, triple_mm=None,
        dpi_line=600, dpi_raster=300,
        notes="Alias for AGU / GRL",
    ),
    # Nature family: Nature, Nat. Clim. Change, Nat. Geosci., Nat. Commun.
    "nature": dict(
        single_mm=90.0, double_mm=180.0, triple_mm=None,
        dpi_line=300, dpi_raster=300,
        notes="5-7 pt fonts at final size; line art PDF/EPS; 300 dpi for raster",
    ),
    "ncc": dict(
        single_mm=90.0, double_mm=180.0, triple_mm=None,
        dpi_line=300, dpi_raster=300,
        notes="Nature Climate Change — alias for nature",
    ),
    "ngeo": dict(
        single_mm=90.0, double_mm=180.0, triple_mm=None,
        dpi_line=300, dpi_raster=300,
        notes="Nature Geoscience — alias for nature",
    ),
    "natcommun": dict(
        single_mm=90.0, double_mm=180.0, triple_mm=None,
        dpi_line=300, dpi_raster=300,
        notes="Nature Communications — alias for nature",
    ),
    # Science / Science Advances
    "science": dict(
        single_mm=89.0, double_mm=127.0, triple_mm=185.0,
        dpi_line=300, dpi_raster=300,
        notes="Single 89mm / 1.5-col 127mm / double 185mm; 300 dpi",
    ),
}

# Convenient aliases
_JOURNAL_ALIASES = {
    "atmospheric chemistry and physics": "acp",
    "atmospheric measurement techniques": "amt",
    "journal of geophysical research": "agu",
    "geophysical research letters": "grl",
    "nature climate change": "ncc",
    "nature geoscience": "ngeo",
    "nature communications": "natcommun",
    "environmental science and engineering": "ees",
}


def _resolve_journal(journal: str) -> dict:
    key = journal.lower().strip()
    key = _JOURNAL_ALIASES.get(key, key)
    if key not in _JOURNAL_SPECS:
        warnings.warn(
            f"Journal {journal!r} not recognised; using AGU defaults. "
            f"Known journals: {list(_JOURNAL_SPECS.keys())}",
            UserWarning,
            stacklevel=3,
        )
        return _JOURNAL_SPECS["agu"]
    return _JOURNAL_SPECS[key]


def _width_inches(journal_key: str, width: str) -> float:
    """Return figure width in inches for the given journal and column spec."""
    spec = _resolve_journal(journal_key)
    if width == "single":
        mm = spec["single_mm"]
    elif width == "double":
        mm = spec["double_mm"]
    elif width in ("triple", "full"):
        mm = spec.get("triple_mm") or spec["double_mm"]
    else:
        try:
            mm = float(width)          # user passed a numeric mm value
        except ValueError:
            raise ValueError(f"width must be 'single', 'double', 'triple', or a mm float; got {width!r}")
    return mm / _MM_PER_INCH


# ---------------------------------------------------------------------------
# Main export function
# ---------------------------------------------------------------------------

def save_figure(
    fig: plt.Figure,
    name: str,
    journal: str = "agu",
    width: str = "single",
    height_scale: float = 0.75,
    formats: list[str] | None = None,
    out_dir: str | pathlib.Path | None = None,
    dpi_override: int | None = None,
    line_art: bool = True,
) -> list[pathlib.Path]:
    """
    Resize *fig* to the correct journal column width and save to disk.

    Parameters
    ----------
    fig          : matplotlib Figure to export.
    name         : Base filename (no extension), e.g. "forcing_bar_chart".
    journal      : Journal key (see _JOURNAL_SPECS) or full journal name.
    width        : 'single' | 'double' | 'triple' | numeric mm value.
    height_scale : height = width_inches * height_scale (default 0.75 = 4:3).
                   Override by setting fig height before calling, then pass
                   height_scale=None to preserve the current height.
    formats      : List of extensions to write, e.g. ['pdf', 'png'].
                   Default: ['pdf', 'png'].
    out_dir      : Directory to write files (default: cwd).
    dpi_override : Override the journal's DPI (useful for quick previews).
    line_art     : Use line-art DPI (higher) vs raster DPI. Default True.

    Returns
    -------
    list of pathlib.Path objects for the written files.
    """
    if formats is None:
        formats = ["pdf", "png"]

    spec = _resolve_journal(journal)
    dpi = dpi_override if dpi_override else (spec["dpi_line"] if line_art else spec["dpi_raster"])

    w_in = _width_inches(journal, width)
    if height_scale is not None:
        h_in = w_in * height_scale
        fig.set_size_inches(w_in, h_in)
    else:
        h_in = fig.get_size_inches()[1]
        fig.set_size_inches(w_in, h_in)

    out_dir = pathlib.Path(out_dir) if out_dir else pathlib.Path.cwd()
    out_dir.mkdir(parents=True, exist_ok=True)

    written = []
    for fmt in formats:
        out_path = out_dir / f"{name}.{fmt}"
        fig.savefig(
            out_path,
            dpi=dpi,
            bbox_inches="tight",
            pad_inches=0.01,
            format=fmt,
        )
        written.append(out_path)
        print(f"  Saved: {out_path}  ({w_in:.2f} in × {h_in:.2f} in, {dpi} dpi)")

    return written


# ---------------------------------------------------------------------------
# Panel labels
# ---------------------------------------------------------------------------

def add_panel_label(
    ax,
    label: str,
    x: float = -0.02,
    y: float = 1.04,
    *,
    fontsize: float = 9,
    fontweight: str = "bold",
    ha: str = "left",
    va: str = "bottom",
    **kwargs,
):
    """
    Add a panel label such as '(a)' to one subplot of a multi-panel figure.

    Convention for this skill: **titles, super-titles, and source/provenance
    text do NOT go on the figure** — they belong in the manuscript (LaTeX/Word)
    caption. The only text on the axes is the data, axis labels, legends,
    in-plot data annotations, and — for multi-panel figures — a panel label
    placed just above the top-left corner.

    Parameters
    ----------
    ax       : the Axes to label.
    label    : panel tag, e.g. '(a)', '(b)'.
    x, y     : position in axes-fraction coordinates (default just above the
               top-left corner, clear of the plot content and the y-axis label).
    """
    ax.text(
        x, y, label,
        transform=ax.transAxes,
        fontsize=fontsize, fontweight=fontweight,
        ha=ha, va=va, **kwargs,
    )
    return ax


# ---------------------------------------------------------------------------
# Grayscale preview
# ---------------------------------------------------------------------------

def grayscale_preview(path: str | pathlib.Path, show: bool = True) -> plt.Figure:
    """
    Load a raster figure and display it in grayscale.

    Use this to verify that your figure communicates without color —
    a requirement for accessibility and many print journals.

    Parameters
    ----------
    path : Path to a PNG, TIFF, or JPEG figure.
    show : If True, call plt.show() (interactive sessions). Set False in scripts.

    Returns
    -------
    matplotlib Figure with the grayscale rendering.
    """
    import matplotlib.image as mpimg
    img = mpimg.imread(str(path))
    # Luminosity-weighted grayscale (ITU-R BT.601)
    if img.ndim == 3:
        gray = 0.299 * img[:, :, 0] + 0.587 * img[:, :, 1] + 0.114 * img[:, :, 2]
    else:
        gray = img
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    axes[0].imshow(img)
    axes[0].set_title("Original", fontsize=9)
    axes[0].axis("off")
    axes[1].imshow(gray, cmap="gray", vmin=0, vmax=1 if gray.max() <= 1 else 255)
    axes[1].set_title("Grayscale check", fontsize=9)
    axes[1].axis("off")
    fig.tight_layout()
    if show:
        plt.show()
    return fig


def list_journals() -> None:
    """Print available journal keys and their width/DPI specs."""
    print(f"{'Journal':<15} {'single mm':>10} {'double mm':>10} {'DPI (line)':>12}  Notes")
    print("-" * 75)
    for key, spec in _JOURNAL_SPECS.items():
        print(f"{key:<15} {spec['single_mm']:>10.1f} {spec['double_mm']:>10.1f} "
              f"{spec['dpi_line']:>12}  {spec['notes'][:50]}")


if __name__ == "__main__":
    list_journals()
