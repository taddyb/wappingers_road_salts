# Analysis pipeline

Reproducible statistics and figures for the Wappingers Creek fault-salinity
paper. Everything here reads from `../data/` and writes into `../figures/`,
which `../main.tex` includes.

## Setup

```bash
python3 -m venv ../.venv
../.venv/bin/pip install numpy pandas scipy matplotlib openpyxl contextily rasterio \
    ruptures geopandas shapely pyogrio pyproj
```

## Run

```bash
../.venv/bin/python stats.py     # corrected Table 1  -> figures/table1_corrected.tex
../.venv/bin/python figures.py   # chloride transect (Fig 5)
../.venv/bin/python maps.py      # overview + three site maps (fetches OSM tiles)
# --- revision round (WP1): revised figures; originals above stay reproducible and untouched ---
../.venv/bin/python maps.py --revised     # figures/rev_overview.png, rev_site{1,2,3}.png (needs internet for tiles)
../.venv/bin/python figures.py --revised  # figures/rev_chloride.png (needs docs/logs/changepoint_summary.csv)
../.venv/bin/python rev_figures.py [overview|1|2|3|chloride ...]   # same code, any subset
# --- revision round (WP0): within-day statistics, change-points, context ---
../.venv/bin/python within_day.py   # figures/table1_revised{,_support}.tex, figures/appendix_data.tex, data/salinity_tidy*.csv, day-offset analysis
../.venv/bin/python changepoint.py  # figures/rev_changepoint_{sc,cl}.png, docs/logs/changepoint*.{txt,csv}
../.venv/bin/python geo_context.py  # road distance + InFault->fault-trace distances (console)
```

`maps.py` needs internet the first time to download basemap tiles.

## Files

| File | Purpose |
|------|---------|
| `wappingers.py` | Data loading, zone definitions, contrast list (shared by the others) |
| `stats.py` | Welch two-sample $t$-tests (headline) + Student + Mann-Whitney; also reproduces the published Table 1 for a transparent before/after |
| `figures.py` | Figure 5 (chloride transect) |
| `maps.py` | Figures 1-4 (regional overview + three site maps) |
| `rev_figures.py` | Revised Figs 1-5 (`rev_overview/site1-3/chloride.png`): raw-SC colouring, within-day zone mean ± SD, digitized fault traces (no uncertainty bands), flow arrows, contrast labels, day-coded markers + inset (Fig 4), Z–Z′ line, chloride fit/breakpoint (Fig 5). Basemap Esri WorldGrayCanvas. |
| `within_day.py` | Single-survey-day zone contrasts (Welch CI/df, Mann-Whitney, lag-1 autocorrelation n_eff), revised Table 1, raw-data appendix longtable (needs `\usepackage{longtable,booktabs}`), 19/26 Oct day-offset check, road distance per zone |
| `changepoint.py` | Segmented regression (0/1/2 breakpoints, BIC), profile + bootstrap intervals, PELT cross-check, distances to InFault points / digitized traces / junctions; SC and chloride; two figures |
| `geo_context.py` | TIGER major-road distance (MTFCC S1100+S1200) and InFault-to-trace distances (offsets of flagged points from the digitized traces) |

`wappingers.py` gained `tidy_salinity()`, `TRANSECTS`, `haversine_m`, `cumulative_distance_m`, `chloride_transect()` and geo helpers; existing functions are unchanged. Console output of each revision script is saved in `docs/logs/`.

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

- **Overview (Figure 1)** — two panels. Panel (a) reproduces the published
  Budnik et al. (2010) Fig. 3.10 (`figures/budnik_faultmap.png`, with the
  thrust-fault areas + legend) with attribution. Panel (b) overlays the mapped
  high-angle faults on OSM. Panel-(b) fault source, in priority order:
  1. `data/faults_budnik2010.geojson` — 42 fault lines traced in QGIS over the
     georeferenced raster. Traced as `data/fault_lines.gpkg` (EPSG:3857) and
     converted to lon/lat GeoJSON with:
     `ogr2ogr -f GeoJSON -t_srs EPSG:4326 data/faults_budnik2010.geojson data/fault_lines.gpkg`
  2. else the clipped raster line-work (`data/clipped_budnik.tif`);
  3. else survey-located traces.
- **Site maps** — (submitted version) a line fitted through each site's `InFault == yes` survey points, which were flagged in the field as believed to be just downstream of the fault (not observed fault positions). The revised figures draw the digitized Budnik et al. (2010) traces.

`data/dutchess_county.gpkg` is the county mask used for the clip (kept for
reproducibility).

## Stream data for the revised figures (USGS NHD)

TIGER linear water omits the creek along Site 2 (survey points up to 1.4 km from any TIGER stream), so the revised figures draw streams from the USGS National Hydrography Dataset instead:
`data/nhd/nhd_flowline_dutchess.geojson` = NHD "Flowline - Large Scale" (layer 6) of The National Map NHD service, queried for bbox lon -73.99..-73.49, lat 41.45..42.01 (8,644 features; fields GNIS_NAME, FTYPE, FCODE, LENGTHKM, REACHCODE), retrieved 2026-11-08 from
`https://hydro.nationalmap.gov/arcgis/rest/services/nhd/MapServer/6/query` (f=geojson, outSR=4326, paged by 1000).
`rev_figures.nhd_network()` snaps flowline ends within 25 m into a graph. Wappinger Creek = all flowlines named Wappinger Creek or East Branch Wappinger Creek (asserted to be one connected network that reaches the Hudson). "Other major streams" = the six longest named streams (excluding the Hudson, the Wappinger system and the Delaware Aqueduct), each reduced to its largest connected piece after bridging gaps by shortest path (<= 3 km). `fig_overview()` asserts every 2018 SC point and 2020 chloride point is within 150 m of the Wappinger line. Roads remain TIGER (`data/tiger`).

**Hudson River polygon (Fig 1b).** `data/nhd/nhd_area_hudson.geojson` = NHD "Area - Large Scale" (layer 9, FTYPE 460 StreamRiver kept), queried in four latitude strips for lon -74.12..-73.80, lat 41.45..42.01 (fields GNIS_NAME, FTYPE, AREASQKM), retrieved 2026-11-08 from `https://hydro.nationalmap.gov/arcgis/rest/services/nhd/MapServer/9/query`. `data/nhd/nhd_waterbody_dutchess.geojson` = NHD "Waterbody - Large Scale" (layer 12), same date/bbox as the flowlines; its FTYPE 493 Estuary polygon covers the tidal Hudson south of Poughkeepsie. `rev_figures.hudson_polygons()` unions both. (Layer 9 rejects queries that request REACHCODE/FCODE; request only GNIS_NAME, FTYPE, AREASQKM.)

## Line-number references in the response letter

`response_to_reviewers.tex` cites changes as `{L123}`: line numbers in the latexdiff highlighted-changes manuscript (`revisions_diff.pdf`). `revisions.tex` loads `lineno` and carries `\linelabel{L:key}` markers at the start of every passage the letter quotes. After editing `revisions.tex` (adding, moving or rewording quoted passages), run

```
.venv/bin/python src/letter_linerefs.py
tectonic response_to_reviewers.tex
```

The script runs `latexdiff original.tex revisions.tex > revisions_diff.tex`, builds it with `tectonic --keep-intermediates`, reads each `\newlabel{L:key}{{N}...}` from the aux file, writes `letter_linerefs.tex` (`\Lref{L:key}` expands to N, or a bold `??` for an unknown key) and deletes the intermediate files. `letter_linerefs.tex` is committed so Overleaf builds the letter without running Python. In the letter, `\Ln{key}` prints `{L<N>}` and `\mq{...}` marks a verbatim quote from `revisions.tex`.
