# Georeferencing the Budnik (2010) fault map for the overview overlay

The right panel of Figure 1 (`figures/overview.png`) can show the **actual
Budnik et al. (2010) high-angle faults** overlaid on OpenStreetMap, instead of
the survey-located traces used as a fallback. To do that, the scanned fault map
(Budnik Fig. 3.10) has to be georeferenced. Automatic shape-matching against the
county boundary was attempted and did not converge (the scan's blue rivers,
boundary gaps, and hatching defeat silhouette extraction), so this is a short
manual step in QGIS. The county shape makes control points easy — you snap them
to the county corners, which are unambiguous.

## Inputs (already on disk)

- `~/papers/budnik_fig3.10_faultmap.png` — the fault map to georeference (high-res).
- `~/Downloads/NYS_Civil_Boundaries.shp/Counties.shp` — county boundaries
  (NAD83 UTM 18N); filter to Dutchess for a reference outline.

## Steps (QGIS, ~15 min)

1. **Load references.** Add `Counties.shp`; select Dutchess and zoom to it. Add
   an OSM base (Browser → XYZ Tiles → OpenStreetMap) for extra snapping targets.
2. **Open the Georeferencer** (Layer → Georeferencer). Open
   `budnik_fig3.10_faultmap.png`.
3. **Add ground control points.** For each of the county's sharp corners, click
   the corner on the scanned map, then "From map canvas" and click the same
   corner on the Dutchess polygon. Use at least these five, which are
   unambiguous on both:
   - southern tip (near Beacon, bottom-left),
   - SE corner (where the south border meets the straight CT border),
   - NE corner (the notch where the east border juts out near the top),
   - northern top point,
   - one distinctive Hudson-River bend on the west edge.
   More corners → better fit. Aim for a residual well under a pixel-km.
4. **Transform settings.** Type = *Thin Plate Spline* (absorbs scan warp) or
   *Polynomial 2*; Resampling = Cubic; Target CRS = `EPSG:4326`.
5. **Export.** Two options, either works — the pipeline auto-detects both:
   - **Raster overlay:** run the georeferencer to write a GeoTIFF. (I can then
     overlay the whole georeferenced map semi-transparently.)
   - **Clean fault lines (preferred for the figure):** after georeferencing,
     add a new line layer, trace the high-angle faults over the georeferenced
     raster, and export as **GeoJSON (EPSG:4326, lon/lat)**.

## Drop-in

Save the traced faults as:

```
data/faults_budnik2010.geojson      (LineString / MultiLineString, lon/lat)
```

(or `data/faults_budnik2010.csv` with columns `fault_id, lon, lat`).

Then re-run `python src/maps.py`. `load_budnik_faults()` picks it up
automatically: the right panel switches to the real Budnik faults and the
subtitle changes from "survey-located" to "Budnik et al. 2010 (georeferenced)".
No code changes needed.
