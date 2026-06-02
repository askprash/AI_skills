# Global Maps Recipe — Contrail RF / Coverage

Cartopy-based recipe for global maps of contrail radiative forcing or contrail coverage.
Install with `pip install cartopy` (also requires GEOS and Proj; on macOS `brew install proj geos`).

## Use cases

- Spatial distribution of contrail net RF (mW m⁻²) — Lee 2021-style
- Contrail coverage fraction (%) by region
- Difference maps (e.g., future scenario minus baseline)
- Flight-density weighted maps (traffic × EF per flight)

## Recipe: Robinson projection, diverging scale

```python
"""
global_contrail_map.py — Robinson projection contrail RF map (requires cartopy).

pip install cartopy
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import pathlib, sys

# cartopy imports
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# Skill helpers (run from research-figures/scripts/)
_SCRIPTS = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(_SCRIPTS))
from figure_export import apply_style, save_figure
apply_style("print")

# ---------------------------------------------------------------------------
# Synthetic RF field — replace with your xarray/netCDF data
# grid: 2° × 2°
# ---------------------------------------------------------------------------
lons = np.arange(-180, 180, 2)
lats = np.arange(-90, 91, 2)
LON, LAT = np.meshgrid(lons, lats)

# Gaussian bumps over N. Atlantic, N. Pacific, Europe corridors
def gauss(lon0, lat0, sigma=25):
    return np.exp(-((LON - lon0)**2 + (LAT - lat0)**2) / (2 * sigma**2))

RF = (
    0.8  * gauss(-40,  52)  # N. Atlantic
  + 0.6  * gauss(-160, 45)  # N. Pacific
  + 0.9  * gauss(  10, 50)  # Europe
  + 0.4  * gauss( 120, 35)  # E. Asia
  - 0.05 * np.ones_like(LON)  # weak background negative
) * 60   # scale to ~mW m⁻²

# ---------------------------------------------------------------------------
# Figure
# ---------------------------------------------------------------------------
proj = ccrs.Robinson()
fig = plt.figure(figsize=(3.5, 2.1))
ax = fig.add_subplot(1, 1, 1, projection=proj)

# Diverging colormap: blue=cooling, white=zero, red=warming
cmap = plt.cm.RdBu_r
norm = mcolors.TwoSlopeNorm(vmin=-5, vcenter=0, vmax=60)

img = ax.pcolormesh(lons, lats, RF, transform=ccrs.PlateCarree(),
                    cmap=cmap, norm=norm, shading="auto", zorder=2)

ax.add_feature(cfeature.COASTLINE, linewidth=0.3, edgecolor="#555555", zorder=3)
ax.add_feature(cfeature.BORDERS,   linewidth=0.2, edgecolor="#888888", zorder=3)
ax.gridlines(linewidth=0.2, linestyle=":", color="#AAAAAA", zorder=1)

cbar = fig.colorbar(img, ax=ax, orientation="horizontal",
                    fraction=0.046, pad=0.04, shrink=0.85)
cbar.set_label("Contrail net RF (mW m$^{-2}$)", fontsize=7)
cbar.ax.tick_params(labelsize=6)

ax.set_title("Aviation contrail net RF — 2019 (illustrative)", fontsize=7.5, pad=4)

# Regional callout box — N. Atlantic hotspot
from matplotlib.patches import FancyBboxPatch
# (use ax.annotate with transform for geographic coordinates)
ax.annotate("N. Atlantic\ncorridor",
            xy=(-40, 52), xycoords=ccrs.PlateCarree()._as_mpl_transform(ax),
            xytext=(0.35, 0.78), textcoords="axes fraction",
            fontsize=5.5, color="#222222",
            arrowprops=dict(arrowstyle="-|>", color="#333333", lw=0.6))

from figure_export import save_figure
out = save_figure(fig, "global_contrail_map", journal="egu", width="double",
                  height_scale=None, formats=["pdf", "png"], out_dir=_SCRIPTS)
plt.close(fig)
print("global_contrail_map:", [str(p) for p in out])
```

## Design choices

**Projection.** Robinson is preferred for global display in climate papers — it distorts
both area and shape less than Mercator at high latitudes, which is where contrail forming
regions concentrate. Use `ccrs.PlateCarree()` as the data CRS (most reanalysis grids are
lat/lon rectilinear).

**Color scale.** Use `RdBu_r` (warm reds positive, cool blues negative) with
`TwoSlopeNorm(vcenter=0)` so the zero crossing is white, not mid-range. Never use jet —
it creates false isolines and fails grayscale. For purely positive coverage fields use
`viridis` or `plasma`.

**Resolution.** For publication, use your actual model output grid. For EGU single-column
(83 mm), contour lines at 5 mW m⁻² intervals read well; for double-column (170 mm) you
can label selected contours.

**Coastlines.** `cfeature.COASTLINE` at linewidth 0.3 is sufficient for journal print.
Thicker lines at 0.5 lw for slides.

**Colorbar.** Horizontal bar below the map, `fraction=0.046, pad=0.04`, label in
mW m⁻². Show the zero contour as a black isoline for clarity.

**Regional callouts.** Use `ax.annotate` with `xycoords=ccrs.PlateCarree()._as_mpl_transform(ax)`
to anchor arrows to geographic coordinates. Label North Atlantic, Europe, and North Pacific
corridors where applicable.

**Caption template:**
> "Global distribution of contrail net ERF (mW m⁻²) for 2019, computed with [model]
> using ERA5 meteorology. Positive values (red) indicate net warming; negative (blue)
> indicate net cooling. Stippling shows grid cells where the 5–95 % uncertainty range
> spans zero. Coastlines from Natural Earth."

## Dependencies

```
pip install cartopy shapely
# macOS: brew install proj geos
# conda: conda install -c conda-forge cartopy
```

Cartopy is NOT a dependency of the research-figures skill core. The five scripts in
`scripts/` run with only matplotlib + numpy. Install cartopy separately when you need
global maps.
