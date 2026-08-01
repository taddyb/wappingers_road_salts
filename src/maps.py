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


def add_basemap_safe(ax, zoom="auto"):
    try:
        cx.add_basemap(ax, source=BASEMAP, zoom=zoom, attribution_size=5)
    except Exception as e:  # noqa: BLE001
        print(f"  basemap fetch failed ({e!r}); leaving blank background")


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


def draw_overview(df, zframes):
    """Two-panel regional figure (Figure 1).

    Left  -- Budnik et al. (2010) Fig. 3.10, the source county fault map.
    Right -- OpenStreetMap of the study area with the three site boxes and the
             mapped high-angle faults. The right-panel faults come from the
             QGIS-georeferenced Budnik layer if present
             (``data/faults_budnik2010.geojson`` / ``.csv``); until that is
             supplied they fall back to the survey-derived traces.
    """
    import pandas as pd
    pts = df.dropna(subset=["lat", "lon"])
    xs, ys = zip(*[merc(lo, la) for lo, la in zip(pts["lon"], pts["lat"])])
    xs, ys = np.array(xs), np.array(ys)
    cx0, cy0 = (xs.min() + xs.max()) / 2, (ys.min() + ys.max()) / 2
    half = max(np.ptp(xs), np.ptp(ys)) * 0.62 + 1500
    clat = cy_to_lat(cy0)

    fig, (axL, axR) = plt.subplots(1, 2, figsize=(11.5, 5.6),
                                   gridspec_kw={"width_ratios": [1, 1.15]})

    # -- left panel: Budnik source map --
    src = FIG / "budnik_faultmap.png"
    if src.exists():
        axL.imshow(plt.imread(src))
    axL.set_axis_off()
    axL.set_title("(a) Budnik et al. (2010) fault map", fontsize=10)

    # -- right panel: OSM + sites + georeferenced faults --
    axR.set_xlim(cx0 - half, cx0 + half)
    axR.set_ylim(cy0 - half, cy0 + half)
    axR.set_aspect("equal")
    add_basemap_safe(axR)

    georef = bool(load_budnik_faults())
    faults = load_budnik_faults() or site_fault_lines(df, zframes)
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
                                    fill=False, edgecolor="black", lw=1.6,
                                    zorder=6))
        axR.annotate(f"Site {site}", (sx.mean(), sy.max() + pad),
                     textcoords="offset points", xytext=(0, 7), ha="center",
                     fontsize=12, fontweight="bold", zorder=7,
                     bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="0.4",
                               alpha=0.9))

    add_scalebar(axR, _round_scale(half * math.cos(math.radians(clat))), clat)
    north_arrow(axR)
    axR.set_axis_off()
    if faults:
        axR.legend(loc="upper left", fontsize=8, framealpha=0.9).set_zorder(9)
    note = "faults: Budnik et al. 2010 (georeferenced)" if georef \
        else "faults: survey-located (awaiting georeferenced Budnik layer)"
    axR.set_title(f"(b) Study sites on OpenStreetMap\n{note}", fontsize=10)

    fig.tight_layout(pad=0.4)
    out = FIG / "overview.png"
    fig.savefig(out, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"wrote {out.relative_to(FIG.parent)}  (georef faults: {georef})")


if __name__ == "__main__":
    df = load_salinity()
    zframes = zone_frames(df)
    welch = {r["contrast"]: r["welch_p"] for r in analyze()}
    draw_overview(df, zframes)
    for site in (1, 2, 3):
        draw_site(site, df, zframes, welch)
