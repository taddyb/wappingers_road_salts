"""Regenerate the site maps (Figures 1-4) from source data.

Each map places the surveyed points on a full-colour OpenStreetMap basemap
(blue rivers, labelled roads), coloured by specific conductance, and overlays:
shaded survey zones, contrast arrows (fault = red, tributary = blue) carrying
the Welch significance, a mapped high-angle fault, a colour bar, a legend, a
north arrow, and a scale bar.

Fault handling (hybrid, per the project decision):
  * Site maps -- the fault is anchored to this site's ``InFault`` survey points
    (where the crossing was actually observed in the field), attributed to
    Budnik et al. 2010.
  * Overview -- one fault trace per site, located from that site's ``InFault``
    GPS points and extended along the fitted strike (see ``site_fault_lines``).
    This pins each Budnik-mapped crossing precisely, rather than tracing the
    1:340,000 county figure (whose raster georeferencing carries multi-km error
    at overview scale). To use hand-digitized county traces instead, drop a
    ``data/faults_budnik2010.csv`` (columns: fault_id, lon, lat) and it wins.

Run:  .venv/bin/python src/maps.py
"""

from pathlib import Path
import csv
import math
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable
from matplotlib.lines import Line2D
from matplotlib.patches import FancyArrowPatch, Polygon as MplPolygon, Patch
import contextily as cx

from wappingers import load_salinity, zone_frames, SITE_ZONES, CONTRASTS
from stats import analyze

FIG = Path(__file__).resolve().parent.parent / "figures"
DATA = Path(__file__).resolve().parent.parent / "data"

# Full-colour OSM theme (blue rivers, green space, labelled roads).
BASEMAP = cx.providers.OpenStreetMap.Mapnik
# Low -> high specific conductance: blue -> yellow -> red.
EC_CMAP = "RdYlBu_r"


def merc(lon, lat):
    r = 6378137.0
    x = r * math.radians(lon)
    y = r * math.log(math.tan(math.pi / 4 + math.radians(lat) / 2))
    return x, y


def cy_to_lat(y):
    r = 6378137.0
    return math.degrees(2 * math.atan(math.exp(y / r)) - math.pi / 2)


def add_basemap_safe(ax, zoom="auto", source=None):
    try:
        cx.add_basemap(ax, source=source or BASEMAP, zoom=zoom,
                       attribution_size=5)
    except Exception as e:  # noqa: BLE001
        print(f"  basemap fetch failed ({e!r}); leaving blank background")


def load_county_outline():
    """Exterior rings (lon/lat) of the Dutchess County polygon, or []."""
    gj = DATA / "dutchess_county.geojson"
    if not gj.exists():
        return []
    import json

    rings = []
    for feat in json.load(open(gj)).get("features", []):
        geom = feat.get("geometry") or {}
        if geom.get("type") == "Polygon":
            polys = [geom["coordinates"]]
        elif geom.get("type") == "MultiPolygon":
            polys = geom["coordinates"]
        else:
            continue
        rings.extend(poly[0] for poly in polys)  # exterior ring of each part
    return rings


def load_rivers():
    """TIGER linear-water segments as lon/lat point lists, or []."""
    shp = DATA / "tiger" / "tl_2024_36027_linearwater.shp"
    if not shp.exists():
        return []
    import shapefile

    sf = shapefile.Reader(str(shp))
    out = []
    for sh in sf.iterShapes():
        parts = list(sh.parts) + [len(sh.points)]
        for i in range(len(parts) - 1):
            seg = sh.points[parts[i]:parts[i + 1]]
            if len(seg) >= 2:
                out.append(seg)
    return out


def load_roads():
    """TIGER highways and county roads as lon/lat point lists, or [].

    Keeps primary/secondary roads (MTFCC S1100/S1200) and interstate / US /
    state / county routes (RTTYP I/U/S/C); drops the ~11k local streets.
    """
    shp = DATA / "tiger" / "tl_2024_36027_roads.shp"
    if not shp.exists():
        return []
    import shapefile

    sf = shapefile.Reader(str(shp))
    fld = [f[0] for f in sf.fields[1:]]
    keep_m, keep_r = {"S1100", "S1200"}, {"I", "U", "S", "C"}
    out = []
    for sh, rec in zip(sf.iterShapes(), sf.iterRecords()):
        d = dict(zip(fld, rec))
        if d.get("MTFCC") in keep_m or d.get("RTTYP") in keep_r:
            parts = list(sh.parts) + [len(sh.points)]
            for i in range(len(parts) - 1):
                seg = sh.points[parts[i]:parts[i + 1]]
                if len(seg) >= 2:
                    out.append(seg)
    return out


def add_scalebar(ax, length_m, lat):
    """Clean scale bar (bar + end ticks + label) sized to the axis extent.

    ``length_m`` is a ground distance; it is drawn in Web-Mercator units,
    correcting for the projection's latitude stretch.
    """
    x0d, x1d = ax.get_xlim()
    y0d, y1d = ax.get_ylim()
    xr, yr = x1d - x0d, y1d - y0d
    w = length_m / math.cos(math.radians(lat))
    x0 = x0d + 0.06 * xr
    y0 = y0d + 0.07 * yr
    th = 0.010 * yr
    ax.add_patch(plt.Rectangle((x0, y0), w, th, fc="black", ec="black", zorder=7))
    for xx in (x0, x0 + w):  # end ticks
        ax.plot([xx, xx], [y0, y0 + 2.2 * th], color="black", lw=1.1, zorder=7)
    label = f"{length_m/1000:g} km" if length_m >= 1000 else f"{length_m:g} m"
    ax.text(x0 + w / 2, y0 + 2.6 * th, label, ha="center", va="bottom",
            fontsize=8, zorder=7,
            bbox=dict(boxstyle="round,pad=0.12", fc="white", ec="none", alpha=0.75))


def north_arrow(ax):
    """Prominent, fixed-size north arrow (axes fraction, extent-independent)."""
    ax.annotate("N", xy=(0.94, 0.965), xytext=(0.94, 0.83),
                xycoords="axes fraction", textcoords="axes fraction",
                arrowprops=dict(arrowstyle="-|>,head_width=0.5,head_length=0.9",
                                color="black", lw=3),
                ha="center", va="bottom", fontsize=17, fontweight="bold",
                zorder=8)


def _round_scale(ground_half):
    target = ground_half * 0.8
    for v in (100, 200, 500, 1000, 2000, 5000, 10000):
        if v >= target:
            return v
    return 10000


def _runs(xs, ys):
    """Split a zone's points into contiguous runs in survey order.

    A break is made only where a step is much larger than the zone's typical
    spacing (gap > max(3x median step, 300 m)). This keeps ordinary zones whole
    (fixing the Site-1 over-split) while still separating Zone 3-2's two
    physically disconnected clusters.
    """
    if len(xs) < 2:
        yield xs, ys
        return
    steps = np.hypot(np.diff(xs), np.diff(ys))
    thresh = max(3 * np.median(steps), 300.0)
    idx = [0, *(np.where(steps > thresh)[0] + 1).tolist(), len(xs)]
    for s, e in zip(idx[:-1], idx[1:]):
        yield xs[s:e], ys[s:e]


def _zone_patch(ax, xs, ys, pad):
    """Shade a survey zone as a padded convex hull (grey, translucent)."""
    from scipy.spatial import ConvexHull, QhullError

    pts = np.column_stack([xs, ys])
    poly = None
    if len(pts) >= 3:
        try:
            poly = pts[ConvexHull(pts).vertices]
        except QhullError:
            poly = None
    if poly is None:  # collinear or <3 points -> bounding box
        x0, x1, y0, y1 = xs.min(), xs.max(), ys.min(), ys.max()
        poly = np.array([[x0, y0], [x1, y0], [x1, y1], [x0, y1]])
    c = poly.mean(axis=0)
    d = poly - c
    n = np.linalg.norm(d, axis=1, keepdims=True)
    poly = poly + d / np.maximum(n, 1e-9) * pad  # push vertices out by `pad`
    # Outline-only (no fill) so the data points are never obscured.
    ax.add_patch(MplPolygon(poly, closed=True, facecolor="none",
                            edgecolor="0.30", lw=1.0, ls=(0, (4, 3)), zorder=2))


def _fault_line(ax, fault_pts, cx0, cy0, half):
    """Fit and draw a dashed fault line through this site's InFault points."""
    if len(fault_pts) < 2:
        return False
    fx, fy = zip(*[merc(lo, la) for lo, la in zip(fault_pts["lon"], fault_pts["lat"])])
    fx, fy = np.array(fx), np.array(fy)
    if np.ptp(fx) >= np.ptp(fy):
        m, b = np.polyfit(fx, fy, 1)
        xl = np.array([cx0 - half, cx0 + half])
        yl = m * xl + b
    else:
        m, b = np.polyfit(fy, fx, 1)
        yl = np.array([cy0 - half, cy0 + half])
        xl = m * yl + b
    ax.plot(xl, yl, color="#5a3d1e", lw=2.2, ls=(0, (7, 4)), zorder=4)
    return True


def draw_site(site, df, zframes, welch):
    import pandas as pd
    zones = SITE_ZONES[site]
    site_pts = pd.concat([zframes[z] for z in zones])
    clat = float(site_pts["lat"].mean())

    px, py = zip(*[merc(lo, la) for lo, la in zip(site_pts["lon"], site_pts["lat"])])
    px, py = np.array(px), np.array(py)
    cx0, cy0 = (px.min() + px.max()) / 2, (py.min() + py.max()) / 2
    span = max(np.ptp(px), np.ptp(py))
    half = span * 0.72 + 90  # points fill ~60% of the frame

    fig, ax = plt.subplots(figsize=(6.0, 5.4))
    ax.set_xlim(cx0 - half, cx0 + half)
    ax.set_ylim(cy0 - half, cy0 + half)
    ax.set_aspect("equal")

    ec_all = site_pts["EC"].to_numpy(dtype=float)
    norm = Normalize(vmin=ec_all.min(), vmax=ec_all.max())

    # shaded zones (one region per contiguous run; only 3-2 splits)
    centroids = {}
    for z in zones:
        fr = zframes[z]
        xs, ys = zip(*[merc(lo, la) for lo, la in zip(fr["lon"], fr["lat"])])
        xs, ys = np.array(xs), np.array(ys)
        for rx, ry in _runs(xs, ys):
            _zone_patch(ax, rx, ry, pad=span * 0.05)
        ax.annotate(f"Zone {z}", (xs.mean(), ys.max()),
                    textcoords="offset points", xytext=(0, 9),
                    fontsize=10, fontweight="bold", zorder=7, ha="center",
                    bbox=dict(boxstyle="round,pad=0.15", fc="white",
                              ec="0.5", alpha=0.85))
        centroids[z] = (xs.mean(), ys.mean())

    add_basemap_safe(ax)
    has_fault = _fault_line(ax, site_pts[site_pts["InFault"] == "yes"],
                            cx0, cy0, half)

    # survey points coloured by specific conductance
    for z in zones:
        fr = zframes[z]
        xs, ys = zip(*[merc(lo, la) for lo, la in zip(fr["lon"], fr["lat"])])
        ax.scatter(xs, ys, c=fr["EC"].to_numpy(dtype=float), cmap=EC_CMAP,
                   norm=norm, s=56, edgecolor="white", linewidth=0.7, zorder=6)

    # contrast arrows (fault = red, tributary = blue) with Welch significance;
    # drawn UNDER the data points so the points stay visible.
    for name, a, b, kind in CONTRASTS:
        if a in centroids and b in centroids:
            (xa, ya), (xb, yb) = centroids[a], centroids[b]
            color = "firebrick" if kind == "fault" else "steelblue"
            ax.add_patch(FancyArrowPatch((xa, ya), (xb, yb), arrowstyle="-|>",
                                         mutation_scale=13, color=color, lw=1.6,
                                         zorder=4, shrinkA=16, shrinkB=16,
                                         alpha=0.9))
            sig = "*" if welch[name] < 0.05 else "n.s."
            # place the label offset perpendicular to the arrow, off the points
            dx, dy = xb - xa, yb - ya
            L = math.hypot(dx, dy) or 1.0
            ox, oy = -dy / L, dx / L
            off = half * 0.13
            ax.text((xa + xb) / 2 + ox * off, (ya + yb) / 2 + oy * off,
                    f"{name}{sig}", color=color, fontsize=9.5, fontweight="bold",
                    zorder=8, ha="center", va="center",
                    bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=color,
                              lw=1.1))

    _decorate(ax, fig, cx0, cy0, half, clat, norm, has_fault)
    fig.tight_layout(pad=0.3)
    out = FIG / f"site{site}.png"
    fig.savefig(out, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"wrote {out.relative_to(FIG.parent)}")


def _decorate(ax, fig, cx0, cy0, half, clat, norm, has_fault):
    """Add scale bar, north arrow, colour bar, and legend."""
    add_scalebar(ax, _round_scale(half * math.cos(math.radians(clat))), clat)
    north_arrow(ax)
    ax.set_axis_off()

    sm = ScalarMappable(norm=norm, cmap=EC_CMAP)
    cb = fig.colorbar(sm, ax=ax, fraction=0.035, pad=0.02)
    cb.set_label(r"Specific conductance ($\mu$S cm$^{-1}$)", fontsize=9)
    cb.ax.tick_params(labelsize=8)

    handles = [
        Line2D([0], [0], color="firebrick", lw=2, marker=">",
               label="Fault contrast (t-test)"),
        Line2D([0], [0], color="steelblue", lw=2, marker=">",
               label="Tributary contrast"),
        Patch(facecolor="0.35", alpha=0.2, edgecolor="0.25", label="Survey zone"),
    ]
    if has_fault:
        handles.insert(0, Line2D([0], [0], color="#5a3d1e", lw=2.2,
                                 ls=(0, (7, 4)),
                                 label="High-angle fault (Budnik et al. 2010)"))
    ax.legend(handles=handles, loc="upper left", fontsize=7.5,
              framealpha=0.9, borderpad=0.5).set_zorder(9)


def merc_inv(x, y):
    r = 6378137.0
    return math.degrees(x / r), cy_to_lat(y)


def load_budnik_faults():
    """Load digitized Budnik Fig 3.10 fault polylines, if supplied.

    Looks for a QGIS-georeferenced fault layer, in order of preference:
      1. ``data/faults_budnik2010.geojson`` -- LineString/MultiLineString in
         WGS84 lon/lat (what QGIS "Export Features" produces).
      2. ``data/faults_budnik2010.csv`` -- columns fault_id, lon, lat.
    Returns {fault_id: [(lon, lat), ...]}. Empty if neither exists (the
    overview then falls back to the survey-derived traces).
    """
    gj = DATA / "faults_budnik2010.geojson"
    if gj.exists():
        import json

        faults = {}
        for i, feat in enumerate(json.load(open(gj)).get("features", [])):
            geom = feat.get("geometry") or {}
            t = geom.get("type")
            if t == "LineString":
                lines = [geom["coordinates"]]
            elif t == "MultiLineString":
                lines = geom["coordinates"]
            else:
                continue
            for j, line in enumerate(lines):
                faults[f"{i}_{j}"] = [(c[0], c[1]) for c in line]
        return faults

    csvp = DATA / "faults_budnik2010.csv"
    if csvp.exists():
        faults = {}
        with open(csvp) as fh:
            for row in csv.DictReader(fh):
                faults.setdefault(row["fault_id"], []).append(
                    (float(row["lon"]), float(row["lat"])))
        return faults
    return {}


def site_fault_lines(df, zframes, extend_m=2600):
    """Fault trace per site, located from that site's ``InFault`` GPS points.

    The crossing position and local strike come from the field survey (real
    coordinates); the line is extended ``extend_m`` past the outermost fault
    point along the fitted strike so it reads as a regional trace. These are
    the high-angle faults mapped by Budnik et al. (2010); the survey points
    pin their creek crossings precisely.
    """
    import pandas as pd

    lines = {}
    for site, zs in SITE_ZONES.items():
        sp = pd.concat([zframes[z] for z in zs])
        fp = sp[sp["InFault"] == "yes"]
        if len(fp) < 2:
            continue
        pts = np.array([merc(lo, la) for lo, la in zip(fp["lon"], fp["lat"])])
        c = pts.mean(axis=0)
        # principal direction (first PCA eigenvector) = local fault strike
        _, _, vt = np.linalg.svd(pts - c)
        d = vt[0]
        t = (pts - c) @ d
        p0 = c + d * (t.min() - extend_m)
        p1 = c + d * (t.max() + extend_m)
        lines[f"site{site}"] = [merc_inv(*p0), merc_inv(*p1)]
    return lines


def load_budnik_raster():
    """Load the QGIS-georeferenced clipped Budnik map (EPSG:3857).

    Returns (display_rgb, ink_rgba, extent) or None if the file is absent:
      * display_rgb -- county map on a white background (for the left panel);
      * ink_rgba    -- only the interior line-work, recoloured brown with an
                       alpha channel so it overlays OSM cleanly (outside-fill,
                       white background and the blue river are transparent);
      * extent      -- [left, right, bottom, top] in Web-Mercator metres.
    """
    tif = DATA / "clipped_budnik.tif"
    if not tif.exists():
        return None
    import rasterio
    from scipy import ndimage

    src = rasterio.open(tif)
    img = np.stack([src.read(i) for i in (1, 2, 3)], axis=-1).astype(int)
    b = src.bounds
    extent = [b.left, b.right, b.bottom, b.top]
    lum = img.mean(2)

    # outside = black clip-fill connected to the image border
    black = lum < 30
    lbl, _ = ndimage.label(black)
    border = set(lbl[0]).union(set(lbl[-1]), set(lbl[:, 0]), set(lbl[:, -1]))
    outside = np.isin(lbl, list(border))

    r, g, bl = img[..., 0], img[..., 1], img[..., 2]
    blue = (bl > 90) & (bl > r + 15) & (bl > g + 10)

    # left-panel display: county on white
    disp = img.copy()
    disp[outside] = 255
    disp = disp.astype("uint8")

    # right-panel overlay: interior dark ink only, recoloured brown
    ink = (~outside) & (~blue) & (lum < 160)
    rgba = np.zeros((*lum.shape, 4), dtype="uint8")
    rgba[ink] = (90, 61, 30, 255)
    return disp, rgba, extent


def _budnik_extent():
    """Geographic extent (Web Mercator) of the clipped Budnik raster, or None."""
    tif = DATA / "clipped_budnik.tif"
    if not tif.exists():
        return None
    import rasterio
    b = rasterio.open(tif).bounds
    return [b.left, b.right, b.bottom, b.top]


def draw_overview(df, zframes):
    """Two-panel regional figure (Figure 1).

    Left  (a) -- the *published* Budnik et al. (2010) Fig. 3.10 (with thrust-
                 fault areas and legend), reproduced directly, with attribution.
    Right (b) -- the same region on OpenStreetMap with the mapped high-angle
                 faults overlaid and the three study reaches boxed.

    Panel-(b) faults, in priority order:
      1. traced vector lines in ``data/faults_budnik2010.geojson`` (bold, clean);
      2. else the clipped georeferenced raster's line-work (recoloured);
      3. else survey-located traces.
    """
    import pandas as pd
    src = FIG / "budnik_faultmap.png"
    if not src.exists():
        return _draw_overview_fallback(df, zframes)

    vec = load_budnik_faults()
    ras = load_budnik_raster()
    extent = _budnik_extent()
    if extent is None:  # frame panel (b) on the sites if there is no raster
        pts = df.dropna(subset=["lat", "lon"])
        mx, my = zip(*[merc(lo, la) for lo, la in zip(pts["lon"], pts["lat"])])
        mx, my = np.array(mx), np.array(my)
        h = max(np.ptp(mx), np.ptp(my)) * 0.62 + 1500
        extent = [mx.mean() - h, mx.mean() + h, my.mean() - h, my.mean() + h]
    left, right, bottom, top = extent
    clat = cy_to_lat((bottom + top) / 2)

    fig, (axL, axR) = plt.subplots(1, 2, figsize=(11.0, 6.6))

    # -- (a) the published figure, reproduced with attribution --
    axL.imshow(plt.imread(src))
    axL.set_axis_off()
    axL.set_title("(a) Budnik et al. (2010) fault map", fontsize=11)
    axL.text(0.5, -0.02, "Reproduced from Budnik, Walker & Menking (2010), "
             "Fig. 3.10,\nNatural Resource Inventory of Dutchess County, NY.",
             transform=axL.transAxes, ha="center", va="top", fontsize=7,
             color="0.3")

    # -- (b) clean vector map: roads + rivers + faults + county outline + sites --
    axR.set_xlim(left, right)
    axR.set_ylim(bottom, top)
    axR.set_aspect("equal")
    axR.set_axis_off()
    axR.set_facecolor("white")

    # highways and county roads (brown)
    for seg in load_roads():
        rx, ry = zip(*[merc(lo, la) for lo, la in seg])
        axR.plot(rx, ry, color="#8a5a2b", lw=0.7, zorder=3)

    # rivers / streams (blue)
    for seg in load_rivers():
        rx, ry = zip(*[merc(lo, la) for lo, la in seg])
        axR.plot(rx, ry, color="#2b6fb0", lw=0.6, alpha=0.8, zorder=3)

    # county outline (dashed, lighter)
    for ring in load_county_outline():
        ox, oy = zip(*[merc(lo, la) for lo, la in ring])
        axR.plot(ox, oy, color="0.45", lw=0.8, ls=(0, (6, 4)), zorder=6)

    # faults (thin, black)
    if vec:
        for i, (fid, coords) in enumerate(vec.items()):
            fx, fy = zip(*[merc(lo, la) for lo, la in coords])
            axR.plot(fx, fy, color="black", lw=1.6, solid_capstyle="round",
                     zorder=5, label="High-angle fault (Budnik et al. 2010)"
                     if i == 0 else None)
        faultsrc = "traced"
    elif ras is not None:
        _, ink_rgba, rext = ras
        axR.imshow(ink_rgba, extent=[rext[0], rext[1], rext[2], rext[3]],
                   origin="upper", interpolation="bilinear", zorder=5)
        axR.plot([], [], color="black", lw=1.6, label="Budnik faults")
        faultsrc = "raster"
    else:
        for i, (fid, coords) in enumerate(site_fault_lines(df, zframes).items()):
            fx, fy = zip(*[merc(lo, la) for lo, la in coords])
            axR.plot(fx, fy, color="black", lw=1.6, ls=(0, (7, 4)), zorder=5,
                     label="Fault (survey-located)" if i == 0 else None)
        faultsrc = "survey"

    # highlighted site boxes with labels above
    for site, zs in SITE_ZONES.items():
        sp = pd.concat([zframes[z] for z in zs])
        sx, sy = zip(*[merc(lo, la) for lo, la in zip(sp["lon"], sp["lat"])])
        sx, sy = np.array(sx), np.array(sy)
        pad = (top - bottom) * 0.012
        x0, y0 = sx.min() - pad, sy.min() - pad
        w, h = np.ptp(sx) + 2 * pad, np.ptp(sy) + 2 * pad
        axR.add_patch(plt.Rectangle((x0, y0), w, h, facecolor="yellow",
                                    alpha=0.35, edgecolor="red", lw=1.8,
                                    zorder=8))
        axR.annotate(f"Site {site}", (x0 + w / 2, y0 + h),
                     textcoords="offset points", xytext=(0, 6), ha="center",
                     va="bottom", fontsize=10, fontweight="bold", zorder=9,
                     bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="red",
                               alpha=0.95))

    from matplotlib.lines import Line2D
    handles = [
        Line2D([0], [0], color="black", lw=1.6,
               label="High-angle fault (Budnik et al. 2010)"),
        Line2D([0], [0], color="#8a5a2b", lw=1.2, label="Highway / county road"),
        Line2D([0], [0], color="#2b6fb0", lw=1.2, label="River / stream"),
        Line2D([0], [0], color="0.45", lw=0.8, ls=(0, (6, 4)),
               label="Dutchess County"),
    ]
    axR.legend(handles=handles, loc="upper left", fontsize=8,
               framealpha=0.9).set_zorder(10)
    axR.set_title("(b) Faults, roads and rivers; study reaches boxed", fontsize=11)

    fig.tight_layout(pad=0.4)
    out = FIG / "overview.png"
    fig.savefig(out, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"wrote {out.relative_to(FIG.parent)}  (panel-b faults: {faultsrc})")


def _draw_overview_fallback(df, zframes):
    """Pre-georeference layout: Budnik PNG (left) + OSM/sites/survey-faults."""
    import pandas as pd
    pts = df.dropna(subset=["lat", "lon"])
    xs, ys = zip(*[merc(lo, la) for lo, la in zip(pts["lon"], pts["lat"])])
    xs, ys = np.array(xs), np.array(ys)
    cx0, cy0 = (xs.min() + xs.max()) / 2, (ys.min() + ys.max()) / 2
    half = max(np.ptp(xs), np.ptp(ys)) * 0.62 + 1500
    clat = cy_to_lat(cy0)
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(11.5, 5.6),
                                   gridspec_kw={"width_ratios": [1, 1.15]})
    src = FIG / "budnik_faultmap.png"
    if src.exists():
        axL.imshow(plt.imread(src))
    axL.set_axis_off()
    axL.set_title("(a) Budnik et al. (2010) fault map", fontsize=10)
    axR.set_xlim(cx0 - half, cx0 + half)
    axR.set_ylim(cy0 - half, cy0 + half)
    axR.set_aspect("equal")
    add_basemap_safe(axR)
    faults = site_fault_lines(df, zframes)
    for i, (fid, coords) in enumerate(faults.items()):
        fx, fy = zip(*[merc(lo, la) for lo, la in coords])
        axR.plot(fx, fy, color="#5a3d1e", lw=1.8, ls=(0, (7, 4)), zorder=4,
                 label="High-angle fault (Budnik et al. 2010)" if i == 0 else None)
    for site, zs in SITE_ZONES.items():
        sp = pd.concat([zframes[z] for z in zs])
        sx, sy = zip(*[merc(lo, la) for lo, la in zip(sp["lon"], sp["lat"])])
        sx, sy = np.array(sx), np.array(sy)
        pad = half * 0.05
        axR.add_patch(plt.Rectangle((sx.min() - pad, sy.min() - pad),
                                    np.ptp(sx) + 2 * pad, np.ptp(sy) + 2 * pad,
                                    fill=False, edgecolor="black", lw=1.6, zorder=6))
        axR.annotate(f"Site {site}", (sx.mean(), sy.max() + pad),
                     textcoords="offset points", xytext=(0, 7), ha="center",
                     fontsize=12, fontweight="bold", zorder=7,
                     bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="0.4", alpha=0.9))
    add_scalebar(axR, _round_scale(half * math.cos(math.radians(clat))), clat)
    north_arrow(axR)
    if faults:
        axR.legend(loc="upper left", fontsize=8, framealpha=0.9).set_zorder(9)
    axR.set_title("(b) Study sites on OpenStreetMap", fontsize=10)
    fig.tight_layout(pad=0.4)
    out = FIG / "overview.png"
    fig.savefig(out, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"wrote {out.relative_to(FIG.parent)}  (fallback layout)")


if __name__ == "__main__":
    df = load_salinity()
    zframes = zone_frames(df)
    welch = {r["contrast"]: r["welch_p"] for r in analyze()}
    draw_overview(df, zframes)
    for site in (1, 2, 3):
        draw_site(site, df, zframes, welch)
