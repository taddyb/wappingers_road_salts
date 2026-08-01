# Analysis pipeline

Reproducible statistics and figures for the Wappingers Creek fault-salinity
paper. Everything here reads from `../data/` and writes into `../figures/`,
which `../main.tex` includes.

## Setup

```bash
python3 -m venv ../.venv
../.venv/bin/pip install numpy pandas scipy matplotlib openpyxl contextily rasterio
```

## Run

```bash
../.venv/bin/python stats.py     # corrected Table 1  -> figures/table1_corrected.tex
../.venv/bin/python figures.py   # chloride transect + zone-EC significance figure
../.venv/bin/python maps.py      # overview + three site maps (fetches OSM tiles)
```

`maps.py` needs internet the first time to download basemap tiles.

## Files

| File | Purpose |
|------|---------|
| `wappingers.py` | Data loading, zone definitions, contrast list (shared by the others) |
| `stats.py` | Welch two-sample $t$-tests (headline) + Student + Mann-Whitney; also reproduces the published Table 1 for a transparent before/after |
| `figures.py` | Figure 5 (chloride) and the zone-EC significance figure |
| `maps.py` | Figures 1-4 (regional overview + three site maps) |

## What was corrected vs. the original R scripts

The original `statistics.R` computed `t = (x̄₂ − x̄₁)/(s₂/√n₂)` — a
one-sample-style statistic that uses only the downstream zone's spread, which
inflated the $t$ values. `stats.py` replaces this with a proper two-sample
**Welch** $t$-test on the raw specific-conductance data (what the Methods text
describes), and reports a Mann-Whitney $U$ test as a nonparametric check. It
also fixes a row-index bug that double-counted one measurement between Zones
3-3 and 3-4.

Result: the two clean fault crossings (Contrasts B and E) remain significant
at $p < 0.001$; the weaker fault crossing (D) and the two tributary-confounded
contrasts (A, C) are not significant. The paper's central claim — significant
salinity increases at fault crossings — is unchanged and now rests on a
defensible test. The `pub. t` column in `stats.py`'s output reproduces the
original published $t$ values exactly, so the correction is auditable.

## Faults

- **Overview (Figure 1)** — the regional faults come from
  `data/clipped_budnik.tif`: Budnik et al. (2010) Fig. 3.10, georeferenced in
  QGIS, clipped to the Dutchess County polygon, and exported in EPSG:3857
  (Web Mercator). `maps.load_budnik_raster()` reads it, drops the black
  clip-fill / white background / blue river to transparency, recolours the
  interior line-work brown, and overlays it on OSM at the same extent as the
  source panel (1:1). If the `.tif` is absent, the overview falls back to a
  survey-trace layout.
- **Site maps** — the fault line is drawn through each site's `InFault == yes`
  survey points (real GPS crossings), attributed to Budnik et al. 2010.

`data/dutchess_county.gpkg` is the county mask used for the clip (kept for
reproducibility).
