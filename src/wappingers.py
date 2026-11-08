"""Shared data loading and zone definitions for the Wappingers Creek analysis.

The 2018 EC survey (``data/salinity-dataset.xlsx``) was collected as five
field "sites" that map onto the three study sites in the paper:

    paper Site 1  <- dataset site 1
    paper Site 2  <- dataset site 2
    paper Site 3  <- dataset sites 5, 3, 4 concatenated in that order

The concatenation order (5, 3, 4) reproduces the ``rbind(siteFive, siteThree,
siteFour)`` in the original ``statistics.R`` so that the zone row-slices below
line up with the published analysis.

Zones are contiguous reaches separated by a geologic feature (a fault zone
or a tributary junction). The row ranges below are the author's spatial zone
boundaries, carried over verbatim from ``statistics.R`` -- with one correction:
the original ``siteThreeZoneFour = merged[40:46]`` (R, 1-based inclusive)
overlapped row 40 with Zone 3-3 (``merged[24:40]``), double-counting one
measurement. Zone 3-4 here starts at the next row so the zones are disjoint.
"""

from pathlib import Path
import pandas as pd

DATA = Path(__file__).resolve().parent.parent / "data"
SALINITY_XLSX = DATA / "salinity-dataset.xlsx"
CHLORIDE_XLSX = DATA / "chloride-dataset.xlsx"


def load_salinity():
    """Return the EC survey as a tidy DataFrame (one row per measurement).

    Columns: ``field_site`` (int 1-5), ``gps_point``, ``lat``, ``lon``,
    ``EC`` (specific conductance, uS/cm), ``Temp`` (C), ``InFault`` (yes/no).
    """
    # Sheet layout: row 0 = title, row 1 = header, row 2 = units, row 3+ = data.
    df = pd.read_excel(SALINITY_XLSX, skiprows=1).iloc[1:].reset_index(drop=True)
    df = df.rename(
        columns={
            "Site Number": "field_site",
            "GPS point": "gps_point",
            "lat": "lat",
            "lon": "lon",
        }
    )
    df["field_site"] = df["field_site"].astype(int)
    for c in ("lat", "lon", "EC", "Temp"):
        df[c] = pd.to_numeric(df[c], errors="coerce")
    df["InFault"] = df["InFault"].astype(str).str.strip().str.lower()
    return df


def _site(df, n):
    return df[df["field_site"] == n].reset_index(drop=True)


def site_frames(df):
    """Return the three paper sites as ordered DataFrames.

    paper Site 3 = field sites 5 + 3 + 4 concatenated (matches statistics.R).
    """
    site1 = _site(df, 1)
    site2 = _site(df, 2)
    site3 = pd.concat([_site(df, 5), _site(df, 3), _site(df, 4)]).reset_index(drop=True)
    return site1, site2, site3


def zones(df):
    """Return an ordered dict of zone-label -> EC values (numpy arrays).

    Row slices are 0-based half-open Python equivalents of the 1-based
    inclusive R slices in statistics.R. Zone 3-4 is shifted by one row
    relative to the original to remove the row-40 double-count.
    """
    site1, site2, site3 = site_frames(df)
    ec = lambda frame, sl: frame.iloc[sl]["EC"].to_numpy()
    z = {}
    z["1-1"] = ec(site1, slice(0, 4))     # R 1:4
    z["1-2"] = ec(site1, slice(4, 9))     # R 5:9
    z["2-1"] = ec(site2, slice(0, 10))    # R 1:10
    z["2-2"] = ec(site2, slice(10, 18))   # R 11:18
    z["3-1"] = ec(site3, slice(3, 20))    # R 4:20
    z["3-2"] = pd.concat(
        [site3.iloc[0:3], site3.iloc[20:23]]
    )["EC"].to_numpy()                     # R 1:3 + 21:23
    z["3-3"] = ec(site3, slice(23, 40))   # R 24:40
    z["3-4"] = ec(site3, slice(40, 46))   # R 41:46 (was 40:46 -> overlap fix)
    return z


# Each contrast compares an upstream zone with a downstream zone across a
# geologic feature. ``kind`` records whether the boundary is a mapped fault
# crossing or a tributary junction -- the paper's argument rests on the faults.
CONTRASTS = [
    ("A", "1-1", "1-2", "tributary"),
    ("B", "2-1", "2-2", "fault"),
    ("C", "3-1", "3-2", "tributary"),
    ("D", "3-2", "3-3", "fault"),
    ("E", "3-3", "3-4", "fault"),
]


def zones_as_published(df):
    """Reproduce the EXACT zone arrays behind the published Table 1.

    Two differences from :func:`zones` are deliberate here, purely to
    reproduce the original numbers for a transparent before/after:

    * Site 3 EC is normalized per *original field sub-site* (5, 3, 4 each
      z-scored on its own, then concatenated) -- matching ``normalize()``
      applied to each sub-site in the original scripts -- rather than on the
      merged reach. Sites 1 and 2 are z-scored over the whole site.
    * Zone 3-4 uses the original overlapping slice ``[39:46]`` (row 40 shared
      with Zone 3-3), reproducing the row-40 double-count.

    Returns a dict of zone-label -> normalized values (numpy arrays).
    """
    import numpy as np

    def z(a):
        a = a.astype(float)
        return (a - a.mean()) / a.std(ddof=1)

    site1, site2, _ = site_frames(df)
    n1 = z(site1["EC"].to_numpy())
    n2 = z(site2["EC"].to_numpy())
    # per-sub-site normalization for the merged Site 3
    n3 = np.concatenate(
        [z(_site(df, 5)["EC"].to_numpy()),
         z(_site(df, 3)["EC"].to_numpy()),
         z(_site(df, 4)["EC"].to_numpy())]
    )
    return {
        "1-1": n1[0:4], "1-2": n1[4:9],
        "2-1": n2[0:10], "2-2": n2[10:18],
        "3-1": n3[3:20], "3-2": np.concatenate([n3[0:3], n3[20:23]]),
        "3-3": n3[23:40], "3-4": n3[39:46],   # [39:46] = original overlap
    }


def zone_frames(df):
    """Like :func:`zones`, but returns a full DataFrame per zone (lat/lon/EC/…).

    Adds a per-paper-site z-scored ``NEC`` column for point coloring, matching
    the ``scale()`` normalization used for the maps in the original scripts.
    """
    site1, site2, site3 = site_frames(df)
    for fr in (site1, site2, site3):
        ec = fr["EC"].to_numpy(dtype=float)
        fr["NEC"] = (ec - ec.mean()) / ec.std(ddof=1)
    idx = {
        "1-1": (site1, slice(0, 4)),   "1-2": (site1, slice(4, 9)),
        "2-1": (site2, slice(0, 10)),  "2-2": (site2, slice(10, 18)),
        "3-1": (site3, slice(3, 20)),
        "3-3": (site3, slice(23, 40)), "3-4": (site3, slice(40, 46)),
    }
    out = {k: fr.iloc[sl].copy() for k, (fr, sl) in idx.items()}
    # Zone 3-2 is split around the reach (rows 1:3 + 21:23 in R terms).
    import pandas as pd
    out["3-2"] = pd.concat([site3.iloc[0:3], site3.iloc[20:23]]).copy()
    return out


# Which paper site each zone belongs to, and the contrasts drawn on each map.
SITE_ZONES = {1: ["1-1", "1-2"], 2: ["2-1", "2-2"], 3: ["3-1", "3-2", "3-3", "3-4"]}


def load_chloride():
    """Return the July 2020 chloride transect with cumulative distance (m).

    The x-axis of Figure 5 ("Distance (m)" from point Z) is not stored in the
    file; it is the running great-circle distance along the sampled points in
    collection order, starting at 0 at the first point.
    """
    import numpy as np

    raw = pd.read_excel(CHLORIDE_XLSX)
    # row 0 = sub-header (lat/lon/Temp/Cl/Notes), row 1 = units, row 2+ = data.
    data = raw.iloc[2:].copy()
    data.columns = ["lat", "lon", "Temp", "Cl", "Notes"]
    for c in ("lat", "lon", "Temp", "Cl"):
        data[c] = pd.to_numeric(data[c], errors="coerce")
    data = data.dropna(subset=["lat", "lon", "Cl"]).reset_index(drop=True)

    def haversine_m(lat1, lon1, lat2, lon2):
        r = 6371000.0
        p1, p2 = np.radians(lat1), np.radians(lat2)
        dphi = np.radians(lat2 - lat1)
        dlmb = np.radians(lon2 - lon1)
        a = np.sin(dphi / 2) ** 2 + np.cos(p1) * np.cos(p2) * np.sin(dlmb / 2) ** 2
        return 2 * r * np.arcsin(np.sqrt(a))

    lat, lon = data["lat"].to_numpy(), data["lon"].to_numpy()
    step = np.zeros(len(data))
    step[1:] = haversine_m(lat[:-1], lon[:-1], lat[1:], lon[1:])
    data["distance_m"] = step.cumsum()
    return data


# ---------------------------------------------------------------------------
# Revision-round helpers (WP0). Nothing above this line was changed.
# ---------------------------------------------------------------------------
import numpy as np

REPO = Path(__file__).resolve().parent.parent
FAULTS_GEOJSON = DATA / "faults_budnik2010.geojson"
ROADS_SHP = DATA / "tiger" / "tl_2024_36027_roads.shp"
METRIC_CRS = "EPSG:32618"  # UTM 18N

# Single-day transects: name -> (paper site, field site, flip). ``flip`` means
# the field row order runs DOWNSTREAM->UPSTREAM and must be reversed so each
# transect is ordered upstream->downstream. Orientation rule: the creek flows
# W/SW; site 3 (19 Oct) rows 1->20 and site 4 rows 1->12 run downstream and the
# end of site 3 is 18 m from the start of site 4. Field site 5 re-surveys the
# reach of site 3 gps 1-8 in the opposite direction (site-5 row 1 sits next to
# site-3 gps 8; site-5 row 11 next to site-3 gps 1), so it is reversed.
# Sites 1 and 2 follow zone order (zone x-1 upstream of x-2 by construction).
TRANSECTS = {
    "S1":            dict(paper_site=1, field_site=1, flip=False, date="2018-09-28"),
    "S2":            dict(paper_site=2, field_site=2, flip=False, date="2018-10-05"),
    "S3-19Oct":      dict(paper_site=3, field_site=3, flip=False, date="2018-10-19"),
    "S3-26Oct-upper": dict(paper_site=3, field_site=5, flip=True,  date="2018-10-26"),
    "S3-26Oct-lower": dict(paper_site=3, field_site=4, flip=False, date="2018-10-26"),
}


def haversine_m(lat1, lon1, lat2, lon2):
    r = 6371000.0
    p1, p2 = np.radians(lat1), np.radians(lat2)
    a = (np.sin((p2 - p1) / 2) ** 2
         + np.cos(p1) * np.cos(p2) * np.sin(np.radians(lon2 - lon1) / 2) ** 2)
    return 2 * r * np.arcsin(np.sqrt(a))


def cumulative_distance_m(lat, lon):
    lat, lon = np.asarray(lat, float), np.asarray(lon, float)
    d = np.zeros(len(lat))
    d[1:] = haversine_m(lat[:-1], lon[:-1], lat[1:], lon[1:])
    return d.cumsum()


# 0-based row ranges in the *paper-site* frame (see zones()), per zone.
_ZONE_ROWS = {
    1: {"1-1": [range(0, 4)], "1-2": [range(4, 9)]},
    2: {"2-1": [range(0, 10)], "2-2": [range(10, 18)]},
    3: {"3-2": [range(0, 3), range(20, 23)], "3-1": [range(3, 20)],
        "3-3": [range(23, 40)], "3-4": [range(40, 46)]},
}


def tidy_salinity(df=None):
    """One row per SC measurement with date, transect, zone, along-channel
    distance (upstream->downstream within each single-day transect).

    Columns: paper_site, field_site, field_row (1-based gps_point), date,
    transect, dist_m, lat, lon, EC, Temp, zone (NaN if the point belongs to no
    zone, i.e. site-4 row 12 which statistics.R's slice drops), InFault.
    """
    if df is None:
        df = load_salinity()
    site1, site2, site3 = site_frames(df)
    frames = {1: site1, 2: site2, 3: site3}
    zone_of = {}  # (paper_site, row) -> zone
    for ps, zd in _ZONE_ROWS.items():
        for z, rngs in zd.items():
            for rg in rngs:
                for i in rg:
                    zone_of[(ps, i)] = z
    parts = []
    for ps, fr in frames.items():
        fr = fr.copy()
        fr["paper_row"] = np.arange(len(fr))
        fr["zone"] = [zone_of.get((ps, i)) for i in fr["paper_row"]]
        fr["paper_site"] = ps
        parts.append(fr)
    t = pd.concat(parts, ignore_index=True)
    t["date"] = pd.to_datetime(t["Date"]).dt.strftime("%Y-%m-%d")
    t["field_row"] = pd.to_numeric(t["gps_point"]).astype(int)
    out = []
    for name, cfg in TRANSECTS.items():
        s = t[(t.paper_site == cfg["paper_site"]) & (t.field_site == cfg["field_site"])]
        s = s.sort_values("field_row", ascending=not cfg["flip"]).copy()
        s["transect"] = name
        s["dist_m"] = cumulative_distance_m(s["lat"], s["lon"])
        out.append(s)
    o = pd.concat(out, ignore_index=True)
    return o[["paper_site", "field_site", "field_row", "date", "transect", "dist_m",
              "lat", "lon", "EC", "Temp", "zone", "InFault"]]


def load_faults_metric():
    import geopandas as gpd
    return gpd.read_file(FAULTS_GEOJSON).to_crs(METRIC_CRS)


def load_roads_metric(major=("S1100", "S1200")):
    import geopandas as gpd
    r = gpd.read_file(ROADS_SHP)
    return r[r.MTFCC.isin(major)].to_crs(METRIC_CRS)


def points_metric(lat, lon):
    import geopandas as gpd
    return gpd.GeoSeries(gpd.points_from_xy(lon, lat), crs="EPSG:4326").to_crs(METRIC_CRS)


def nearest_dist_m(lat, lon, lines):
    """Distance (m) from each lon/lat point to the nearest geometry in ``lines``
    (a GeoDataFrame already in METRIC_CRS)."""
    u = lines.geometry.union_all()
    return np.array([p.distance(u) for p in points_metric(lat, lon)])


def chloride_transect():
    """Chloride transect without the 'side tributary' row (as in figures.py)."""
    c = load_chloride()
    return c[~c["Notes"].fillna("").str.contains("side tributary")].reset_index(drop=True)
