"""Road-distance and fault-band basis (revision round, WP0, tasks 5-6).

Major road = TIGER MTFCC S1100 (primary) + S1200 (secondary) from
data/tiger/tl_2024_36027_roads.shp (Dutchess Co.). In this county that gives
I-84 / Newburgh-Beacon Bridge (S1100) and US 9, US 44, NY 82, NY 55, NY 376 ...
(S1200). NOTE: Taconic State Pkwy is coded S1400 (local road) in TIGER, so it
is NOT 'major' under this rule; a sensitivity variant adding it by name is
printed. Distances: EPSG:32618 planar, point to nearest line.
Fault-trace offset: distance from each InFault==yes (flagged as just downstream of the fault) SC point to the nearest digitized
Budnik et al. 2010 trace (data/faults_budnik2010.geojson).
Run:  .venv/bin/python src/geo_context.py
"""
import geopandas as gpd
import numpy as np
import pandas as pd
from wappingers import (tidy_salinity, load_faults_metric, load_roads_metric, nearest_dist_m,
                        ROADS_SHP, METRIC_CRS)

t = tidy_salinity()
roads = load_roads_metric()
print("Major-road segments:", len(roads), roads.MTFCC.value_counts().to_dict())
t["road_m"] = nearest_dist_m(t.lat, t.lon, roads)
allr = gpd.read_file(ROADS_SHP).to_crs(METRIC_CRS)
names = ["US Hwy 44", "Rte 44", "Rte 82", "State Rte 82", "Taconic State Pkwy"]
for nm in names:
    sub = allr[allr.FULLNAME == nm]
    t["d_" + nm] = nearest_dist_m(t.lat, t.lon, sub)
print("\nNearest-road name per transect (median distance, m):")
u = {nm: allr[allr.FULLNAME == nm] for nm in names}
print(t.groupby("transect", sort=False)[["road_m"] + ["d_" + n for n in names]].median().round(0).to_string())
rt = allr[allr.MTFCC.isin(["S1100", "S1200"])].copy()
t["nearest_major_name"] = [rt.iloc[int(np.argmin([g.distance(p) for g in rt.geometry]))].FULLNAME
                           for p in gpd.GeoSeries(gpd.points_from_xy(t.lon, t.lat), crs=4326).to_crs(METRIC_CRS)]
print("\nNearest major road name (count per transect):")
print(t.groupby(["transect", "nearest_major_name"]).size().to_string())
print("\nPer-zone, per-day median road distance (m):")
print(t.dropna(subset=["zone"]).groupby(["zone", "date"]).road_m.agg(["size", "median", "min", "max"]).round(0).to_string())
print("\nSensitivity incl. Taconic by name (min of major & Taconic), per transect median:")
print(np.minimum(t.road_m, t["d_Taconic State Pkwy"]).groupby(t.transect).median().round(0).to_string())

faults = load_faults_metric()
inf = t[t.InFault == "yes"].copy()
inf["trace_m"] = nearest_dist_m(inf.lat, inf.lon, faults)
print("\n== InFault points -> nearest digitized trace (m) ==")
print(inf[["transect", "field_row", "dist_m", "trace_m"]].round(1).to_string(index=False))
print("n=%d  min %.0f  median %.0f  max %.0f" % (len(inf), inf.trace_m.min(), inf.trace_m.median(), inf.trace_m.max()))
print(inf.groupby("transect", sort=False).trace_m.agg(["size", "median", "max"]).round(0).to_string())
print("by paper site:\n", inf.groupby("paper_site").trace_m.agg(["size", "min", "median", "max"]).round(0).to_string())
print("per field site 3 (19 Oct) only vs 26 Oct lower: see per-transect above")
