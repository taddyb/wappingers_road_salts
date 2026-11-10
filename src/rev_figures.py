"""Revised figures for the manuscript revision (WP1).

Writes NEW files only (the submitted figures used by original.tex are untouched):
  figures/rev_overview.png   Fig 1  regional overview (a: Budnik map, b: simplified study area)
  figures/rev_site1.png      Fig 2  Site 1 (Contrast A)
  figures/rev_site2.png      Fig 3  Site 2 (Contrast B), all fault-trace/channel intersections
  figures/rev_site3.png      Fig 4  Site 3 (Contrasts C, D, E), day-coded markers, fault traces,
                                    Z-Z' chloride line, inset resolving 19/26 Oct overlap
  figures/rev_chloride.png   Fig 5  chloride along Z -> Z' with segmented fit, fault points and trace crossing

Run:  .venv/bin/python src/rev_figures.py        (or maps.py --revised / figures.py --revised)
Needs internet for basemap tiles.  Every plotted value comes from data/ via
wappingers.py (raw SC in uS/cm, no normalisation) and, for Fig 5, from
docs/logs/changepoint_summary.csv (written by changepoint.py).
"""
import math
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable
from matplotlib.lines import Line2D
from matplotlib.patches import Patch, FancyArrowPatch
from shapely.geometry import LineString, Point, box
import contextily as cx

sys.path.insert(0, str(Path(__file__).resolve().parent))
from wappingers import (nearest_dist_m, tidy_salinity, chloride_transect, load_faults_metric, points_metric,
                        DATA, REPO, METRIC_CRS)
from maps import add_basemap_safe, add_scalebar, north_arrow, _round_scale, load_budnik_raster

FIG = REPO / "figures"
DPI = 300
WEB = "EPSG:3857"

# Okabe-Ito colour-blind-safe palette
OI = dict(black="#000000", orange="#E69F00", sky="#56B4E9", green="#009E73", yellow="#F0E442",
          blue="#0072B2", verm="#D55E00", purple="#CC79A7")
CMAP = "viridis"                      # raw SC, perceptually uniform, colour-blind safe
BASE = cx.providers.Esri.WorldGrayCanvas
STREAM = OI["blue"]
WATER = "#b9dcf1"   # Hudson River fill: light water blue, same family as the streams
ROAD = "#555555"
FAULT_LABEL = "High-angle fault, county-scale map (Budnik et al. 2010; approximate)"
KIND = {"A": "tributary", "B": "fault zone", "C": "tributary", "D": "fault zone", "E": "fault zone"}

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 8, "axes.labelsize": 8,
                     "legend.fontsize": 7, "savefig.dpi": DPI})


# ----------------------------------------------------------------- geometry
def to_web(geom_series):
    return geom_series.to_crs(WEB)


def faults_web():
    F = load_faults_metric()
    return to_web(F.geometry), None, F


def pts_web(lat, lon):
    g = gpd.GeoSeries(gpd.points_from_xy(lon, lat), crs="EPSG:4326").to_crs(WEB)
    return np.column_stack([g.x.to_numpy(), g.y.to_numpy()])


def tiger_streams():
    w = gpd.read_file(DATA / "tiger" / "tl_2024_36027_linearwater.shp")
    return w


NHD_FILE = DATA / "nhd" / "nhd_flowline_dutchess.geojson"   # USGS NHD flowlines, see src/README.md
SNAP_M = 25.0


def nhd_network():
    """Continuous stream geometries from USGS NHD flowlines (EPSG:3857).

    Flowline ends within SNAP_M are snapped into graph nodes.  Wappinger Creek = all flowlines
    named Wappinger Creek or East Branch Wappinger Creek (they form one connected network;
    asserted).  Other major streams = the longest named streams other than the Hudson, Wappinger
    system and Little Wappinger; each is reduced to its largest connected piece after bridging
    its gaps by the shortest path through the full network (<= 3 km), so nothing is fragmentary.
    Returns dict(all=GeoSeries, wappinger=GeoSeries, others=GeoSeries) plus metric versions
    under keys *_m.
    """
    from scipy.spatial import cKDTree
    from scipy.sparse import coo_matrix
    from scipy.sparse.csgraph import connected_components, dijkstra
    n = gpd.read_file(NHD_FILE).to_crs(METRIC_CRS).explode(index_parts=False).reset_index(drop=True)
    n["name"] = n.gnis_name.fillna("")
    ends = np.array([[g.coords[0][:2], g.coords[-1][:2]] for g in n.geometry]).reshape(-1, 2)
    par = list(range(len(ends)))

    def find(i):
        while par[i] != i:
            par[i] = par[par[i]]
            i = par[i]
        return i
    for a_, b_ in cKDTree(ends).query_pairs(SNAP_M):
        par[find(a_)] = find(b_)
    _, node = np.unique([find(i) for i in range(len(ends))], return_inverse=True)
    u, v, N = node[0::2], node[1::2], node.max() + 1
    L = n.length.to_numpy()

    def graph(idx):
        return coo_matrix((np.r_[L[idx], L[idx]], (np.r_[u[idx], v[idx]], np.r_[v[idx], u[idx]])), shape=(N, N)).tocsr()
    full = graph(np.arange(len(n)))

    def comps(idx):
        _, lab = connected_components(graph(idx), directed=False)
        return lab

    wap_idx = n.index[n.name.isin(["Wappinger Creek", "East Branch Wappinger Creek"])].to_numpy()
    lab = comps(wap_idx)
    assert len(set(lab[u[wap_idx]])) == 1, "Wappinger Creek is not one connected network"
    out = dict(wappinger_m=n.loc[wap_idx].geometry)
    skip = {"", "Hudson River", "Delaware Aqueduct", "Wappinger Creek", "East Branch Wappinger Creek", "Little Wappinger Creek"}
    tot = n[~n.name.isin(skip)].groupby("name").apply(lambda d: d.length.sum()).sort_values(ascending=False)
    keep = []
    for name in tot.index[:14]:
        idx = n.index[n.name == name].to_numpy()
        lab = comps(idx)
        cl = lab[u[idx]]
        sizes = {c: L[idx][cl == c].sum() for c in set(cl)}
        main = max(sizes, key=sizes.get)
        use = list(idx[cl == main])
        nodes_main = np.unique(np.r_[u[use], v[use]])
        for c in sizes:
            if c == main:
                continue
            nodes_c = np.unique(np.r_[u[idx[cl == c]], v[idx[cl == c]]])
            dist, pred = dijkstra(full, indices=nodes_c, return_predecessors=True)
            best = nodes_main[np.argmin(dist[:, nodes_main].min(axis=0))]
            row = np.argmin(dist[:, best])
            if dist[row, best] <= 3000:
                use += list(idx[cl == c])
                # bridge: edges on the shortest path
                x = best
                while x != nodes_c[row]:
                    p = pred[row, x]
                    e = np.where(((u == x) & (v == p)) | ((u == p) & (v == x)))[0]
                    if len(e):
                        use.append(e[0])
                    x = p
        sub = n.loc[sorted(set(use))]
        keep.append((name, sub.length.sum(), sub.geometry))
    keep.sort(key=lambda t: -t[1])
    out["others_m"] = [(nm, ln, g) for nm, ln, g in keep[:6]]
    out["all_m"] = n.geometry
    return out


_NET = {}


def net():
    if not _NET:
        _NET.update(nhd_network())
    return _NET


def m2web(gs):
    return gpd.GeoSeries(list(gs), crs=METRIC_CRS).to_crs(WEB)


def tiger_roads():
    return gpd.read_file(DATA / "tiger" / "tl_2024_36027_roads.shp")


def mkc(lat):
    """Web-Mercator metre stretch at a latitude (ground m = web m * cos(lat))."""
    return 1.0 / math.cos(math.radians(lat))


def draw_lines(ax, gs, **kw):
    for geom in gs:
        parts = getattr(geom, "geoms", [geom])
        for p in parts:
            x, y = p.xy
            ax.plot(x, y, **kw)


def draw_polys(ax, gs, **kw):
    from matplotlib.patches import PathPatch
    from matplotlib.path import Path as MP
    for geom in gs:
        for poly in getattr(geom, "geoms", [geom]):
            verts, codes = [], []
            for ring in [poly.exterior, *poly.interiors]:
                c = np.asarray(ring.coords)
                verts += list(c)
                codes += [MP.MOVETO] + [MP.LINETO] * (len(c) - 2) + [MP.CLOSEPOLY]
            ax.add_patch(PathPatch(MP(verts, codes), **kw))


def halo(w, c="white"):
    return [pe.withStroke(linewidth=w, foreground=c)]


# ------------------------------------------------------------------ site maps
def zone_stats(t):
    g = t.dropna(subset=["zone"]).groupby(["zone", "date"]).EC
    s = g.agg(["size", "mean", "std"]).reset_index()
    return {(r.zone, r.date): (int(r["size"]), r["mean"], r["std"]) for _, r in s.iterrows()}


def boundary_tick(g, zup, zdn):
    """Midpoint (web m) and unit tangent between the last zup and first zdn point of
    a single-day transect g (sorted upstream->downstream)."""
    g = g.sort_values("dist_m").reset_index(drop=True)
    z = g.zone.to_numpy()
    xy = pts_web(g.lat, g.lon)
    for i in range(len(g) - 1):
        if z[i] == zup and z[i + 1] == zdn:
            m = 0.5 * (xy[i] + xy[i + 1])
            d = xy[i + 1] - xy[i]
            return m, d / np.linalg.norm(d)
    return None


def draw_contrast(ax, mid, tan, label, kind, lat, sub, ground_half=170, lab_pts=(0, 40), lab_dir=1):
    """Boundary tick across the channel + boxed contrast label with a leader line."""
    nrm = np.array([-tan[1], tan[0]])
    L = ground_half * mkc(lat)
    p0, p1 = mid - nrm * L, mid + nrm * L
    ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color="black", lw=2.4, zorder=8, solid_capstyle="butt",
            path_effects=halo(4.6))
    end = mid + nrm * lab_dir * L
    ax.annotate(f"Contrast {label}{':' if label == 'B' else ''}\n{kind}{sub}", end, xytext=lab_pts, textcoords="offset points", ha="center",
                va="center", fontsize=7.5, fontweight="bold", zorder=11,
                bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="black", lw=0.9),
                arrowprops=dict(arrowstyle="-", color="black", lw=0.9, shrinkA=0, shrinkB=0))


def flow_arrow(ax, g, frac0, frac1, lat, side_m=0.0, label_off=(0, 0), width=2.2):
    """Downstream arrow parallel to the surveyed channel between two fractions of its
    length, shifted ``side_m`` ground-metres to the left of the flow direction."""
    g = g.sort_values("dist_m")
    xy = pts_web(g.lat, g.lon)
    d = g.dist_m.to_numpy()
    xs = np.interp([frac0 * d.max(), frac1 * d.max()], d, xy[:, 0])
    ys = np.interp([frac0 * d.max(), frac1 * d.max()], d, xy[:, 1])
    v = np.array([xs[1] - xs[0], ys[1] - ys[0]]); v /= np.linalg.norm(v)
    n = np.array([-v[1], v[0]]) * side_m * mkc(lat)
    xs, ys = xs + n[0], ys + n[1]
    ax.add_patch(FancyArrowPatch((xs[0], ys[0]), (xs[1], ys[1]), arrowstyle="-|>,head_width=0.32,head_length=0.7",
                                 mutation_scale=16, color="black", lw=width, zorder=9,
                                 path_effects=halo(width + 2.4)))
    ax.annotate("flow", (0.5 * (xs[0] + xs[1]), 0.5 * (ys[0] + ys[1])), xytext=label_off, textcoords="offset points",
                fontsize=8, fontstyle="italic", fontweight="bold", ha="center", va="center", zorder=11,
                path_effects=halo(3.0))


def base_axes(ax, xy, pad_frac=0.28, min_half=None, aspect_w_over_h=1.0):
    cx0, cx1 = xy[:, 0].min(), xy[:, 0].max()
    cy0, cy1 = xy[:, 1].min(), xy[:, 1].max()
    mx, my = (cx0 + cx1) / 2, (cy0 + cy1) / 2
    hw = (cx1 - cx0) / 2 * (1 + pad_frac) + 150
    hh = (cy1 - cy0) / 2 * (1 + pad_frac) + 150
    if min_half:
        hw, hh = max(hw, min_half), max(hh, min_half)
    # fit to requested aspect
    if hw / hh > aspect_w_over_h:
        hh = hw / aspect_w_over_h
    else:
        hw = hh * aspect_w_over_h
    ax.set_xlim(mx - hw, mx + hw)
    ax.set_ylim(my - hh, my + hh)
    ax.set_aspect("equal")
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_linewidth(0.6)
    return (mx - hw, mx + hw, my - hh, my + hh)


from matplotlib.path import Path as _MP

_SHIELD = _MP([(-0.9, 0.9), (0.9, 0.9), (0.97, 0.25), (0.7, -0.35), (0, -1.0), (-0.7, -0.35), (-0.97, 0.25),
               (-0.9, 0.9)], [_MP.MOVETO] + [_MP.LINETO] * 6 + [_MP.CLOSEPOLY])
_IBAND = _MP([(-0.9, 0.9), (0.9, 0.9), (0.93, 0.5), (-0.93, 0.5), (-0.9, 0.9)],
             [_MP.MOVETO] + [_MP.LINETO] * 3 + [_MP.CLOSEPOLY])
_NYBOX = _MP([(-1.3, 0.8), (1.3, 0.8), (1.3, -0.8), (-1.3, -0.8), (-1.3, 0.8)],
             [_MP.MOVETO] + [_MP.LINETO] * 3 + [_MP.CLOSEPOLY])


def route_shield(ax, x, y, kind, num, ms=15, zorder=11):
    """Route marker drawn from matplotlib paths (MUTCD-style approximations).
    kind: 'I' interstate (blue body, red band, white number), 'US' (white shield, black outline),
    'NY' (white rounded box, black outline)."""
    if kind == "I":
        ax.plot(x, y, marker=_SHIELD, ms=ms + 2.5, mfc="white", mec="white", ls="", zorder=zorder)
        ax.plot(x, y, marker=_SHIELD, ms=ms, mfc="#1F4E9A", mec="#1F4E9A", ls="", zorder=zorder + 0.1)
        ax.plot(x, y, marker=_IBAND, ms=ms, mfc="#C8102E", mec="#C8102E", ls="", zorder=zorder + 0.2)
        ax.annotate(num, (x, y), xytext=(0, -1.2), textcoords="offset points", ha="center", va="center", fontsize=6.3,
                    fontweight="bold", color="white", zorder=zorder + 0.3)
    elif kind == "US":
        ax.plot(x, y, marker=_SHIELD, ms=ms, mfc="white", mec="black", mew=1.3, ls="", zorder=zorder)
        ax.annotate(num, (x, y), xytext=(0, 0.8), textcoords="offset points", ha="center", va="center", fontsize=6.5,
                    fontweight="bold", color="black", zorder=zorder + 0.3)
    else:
        ax.plot(x, y, marker=_NYBOX, ms=ms * 1.05, mfc="white", mec="black", mew=1.2, ls="", zorder=zorder)
        ax.annotate(num, (x, y), xytext=(0, 0), textcoords="offset points", ha="center", va="center", fontsize=6.5,
                    fontweight="bold", color="black", zorder=zorder + 0.3)


SHIELDS = {"I-84": ("I", "84"), "US 9": ("US", "9"), "US 44": ("US", "44"), "NY 82": ("NY", "82"),
           "NY 22": ("NY", "22")}


def route_label(ax, x, y, short, ms=15):
    if short in SHIELDS:
        route_shield(ax, x, y, *SHIELDS[short], ms=ms)
    else:
        ax.annotate(short, (x, y), fontsize=4.8, color="#333333", ha="center", va="center", zorder=11,
                    bbox=dict(boxstyle="round,pad=0.12", fc="white", ec="none", alpha=0.75))


from matplotlib.legend_handler import HandlerBase
from matplotlib.patches import PathPatch as _PP


class RouteKey:
    """Legend handle for a route-shield type: 'I', 'US' or 'NY' (shape only, no number)."""
    def __init__(self, kind):
        self.kind = kind


class HandlerRoute(HandlerBase):
    def create_artists(self, legend, orig, xdescent, ydescent, width, height, fontsize, trans):
        cx, cy = xdescent + width / 2, ydescent + height / 2
        hh = height * 0.95

        def poly(path, sx, sy, **kw):
            v = path.vertices * [sx, sy] + [cx, cy]
            return _PP(_MP(v, path.codes), transform=trans, **kw)
        if orig.kind == "I":
            return [poly(_SHIELD, hh, hh, fc="#1F4E9A", ec="#1F4E9A", lw=0.5),
                    poly(_IBAND, hh, hh, fc="#C8102E", ec="#C8102E", lw=0.5)]
        if orig.kind == "US":
            return [poly(_SHIELD, hh, hh, fc="white", ec="black", lw=1.1)]
        return [poly(_NYBOX, hh * 0.8, hh * 0.8, fc="white", ec="black", lw=1.1)]


ROUTE_KEYS = {"I": "Interstate", "US": "US route", "NY": "NY State route"}


def route_entries(kinds):
    return [(RouteKey(k), ROUTE_KEYS[k]) for k in ("I", "US", "NY") if k in kinds]


def _legend(ax_or_fig, h, lab, **kw):
    return ax_or_fig.legend(h, lab, handler_map={RouteKey: HandlerRoute()}, **kw)


def draw_context(ax, ext, F_web, band_web, streams=True, roads=True, label_roads=True, lw_scale=1.0, label_frac={}):
    """Fault traces, NHD streams, TIGER major roads, clipped to extent."""
    bbox = box(ext[0], ext[2], ext[1], ext[3])
    if streams:
        w = m2web(net()["all_m"])
        w = w[w.intersects(bbox)]
        draw_lines(ax, w.intersection(bbox), color=STREAM, lw=1.1 * lw_scale, zorder=3, alpha=0.9)
    if roads:
        r = tiger_roads()
        r = r[r.MTFCC.isin(["S1100", "S1200"])].to_crs(WEB)
        r = r[r.intersects(bbox)]
        draw_lines(ax, r.geometry.intersection(bbox), color=ROAD, lw=1.2 * lw_scale, zorder=3,
                   path_effects=halo(2.6))
        if label_roads:
            short_of = {"US Hwy 44": "US 44", "Rte 44": "US 44", "Rte 82": "NY 82", "State Rte 82": "NY 82"}
            r = r.assign(short=r.FULLNAME.map(short_of))
            for short, grp in r.dropna(subset=["short"]).groupby("short"):
                geom = grp.geometry.intersection(bbox)
                parts = [p for g in geom[~geom.is_empty] for p in getattr(g, "geoms", [g]) if p.geom_type == "LineString"]
                if not parts:
                    continue
                longest = max(parts, key=lambda p: p.length)
                pt = longest.interpolate(label_frac.get(short, 0.3), normalized=True)
                route_label(ax, pt.x, pt.y, short, ms=17)
    inb = F_web[F_web.intersects(bbox)]
    draw_lines(ax, inb.intersection(bbox), color="black", lw=1.9, zorder=4, path_effects=halo(3.6))


def sc_markers(ax, t, norm, by_day, size=48, zorder=7):
    """Scatter of points coloured by raw SC; marker by survey day when by_day."""
    marks = {"2018-10-19": ("o", "19 Oct 2018"), "2018-10-26": ("^", "26 Oct 2018")}
    for dt, g in t.groupby("date"):
        xy = pts_web(g.lat, g.lon)
        m = marks.get(dt, ("o", dt))[0] if by_day else "o"
        s = size * (1.35 if m == "^" else 1.0)
        ax.scatter(xy[:, 0], xy[:, 1], c=g.EC, cmap=CMAP, norm=norm, marker=m, s=s,
                   edgecolor="white", linewidth=0.9, zorder=zorder)
        inf = g[g.InFault == "yes"]
        if len(inf):
            xi = pts_web(inf.lat, inf.lon)
            ax.scatter(xi[:, 0], xi[:, 1], marker=m, s=s * 2.3, facecolor="none", edgecolor=OI["verm"],
                       linewidth=1.5, zorder=zorder - 0.5)


def channel_line(ax, t, zorder=6):
    for tr, g in t.groupby("transect", sort=False):
        xy = pts_web(g.sort_values("dist_m").lat, g.sort_values("dist_m").lon)
        ax.plot(xy[:, 0], xy[:, 1], color="0.15", lw=0.9, alpha=0.8, zorder=zorder)


def sc_colorbar(fig, ax, norm, label=r"Specific conductance ($\mu$S cm$^{-1}$)"):
    sm = ScalarMappable(norm=norm, cmap=CMAP)
    cb = fig.colorbar(sm, ax=ax, fraction=0.04, pad=0.02, shrink=0.88)
    cb.set_label(label, fontsize=8)
    cb.ax.tick_params(labelsize=7)
    return cb


INFAULT_LABEL = "Fault point (survey point downstream of a fault)"   # edit here


def common_legend(fig, first=(), extra=()):
    """Legend order: survey-date markers first, then fault/stream/road, extras, InFault ring last."""
    h, lab = [], []
    for hh, ll in first:
        h.append(hh); lab.append(ll)
    h += [Line2D([], [], color="black", lw=1.9, path_effects=halo(3.6)),
          Line2D([], [], color=STREAM, lw=1.3),
          Line2D([], [], color=ROAD, lw=1.3, path_effects=halo(2.6))]
    lab += [FAULT_LABEL, "Stream", "Major road"]
    for hh, ll in extra:
        h.append(hh); lab.append(ll)
    h.append(Line2D([], [], marker="o", ls="", mfc="none", mec=OI["verm"], mew=1.5, ms=8))
    lab.append(INFAULT_LABEL)
    return h, lab


WWTP_FILE = DATA / "wwtp_facilities.csv"   # EPA ECHO facility locations (not surveyed outfalls)
WWTP_LABEL = "Wastewater facility"
WWTP_COLOR = "#332288"
WWTP_SHORT = {"NY0025429": "Millbrook STP", "NY0218944": "Stratford Farms STP", "NY0218952": "Ennis MHP WWTP",
              "NY0077593": "Valley Dale STP", "NY0264989": "Titusville WWTP", "NY0099279": "NYSP Troop K"}


def wwtp_points(ext):
    """Facilities inside ext=(x0, x1, y0, y1) (web m): list of (short name, x, y)."""
    d = pd.read_csv(WWTP_FILE)
    xy = pts_web(d.lat, d.lon)
    out = []
    for (_, r), (x, y) in zip(d.iterrows(), xy):
        if ext[0] <= x <= ext[1] and ext[2] <= y <= ext[3]:
            out.append((WWTP_SHORT.get(r.permit_id, r["name"]), x, y))
    return out


def draw_wwtp(ax, pts, label_off=None, size=8.5, labels=True):
    label_off = label_off or {}
    for nm, x, y in pts:
        ax.plot(x, y, marker="s", ms=size, mfc=WWTP_COLOR, mec="white", mew=1.0, zorder=9, ls="")
        if labels and nm in label_off:
            dx, dy, ha = label_off[nm]
            ax.annotate(nm, (x, y), xytext=(dx, dy), textcoords="offset points", fontsize=7.5, ha=ha,
                        va="center", zorder=10, color=WWTP_COLOR, fontweight="bold",
                        bbox=dict(boxstyle="round,pad=0.15", fc="white", ec=WWTP_COLOR, lw=0.7))


def wwtp_entry():
    return (Line2D([], [], marker="s", ls="", mfc=WWTP_COLOR, mec="white", ms=8), WWTP_LABEL)


WWTP_OFF = {2: {"Stratford Farms STP": (-10, 0, "right"), "Ennis MHP WWTP": (-10, 0, "right"),
                "Valley Dale STP": (-10, -14, "right"), "Titusville WWTP": (11, 0, "left")}}


def survey_entry(label, marker="o"):
    return (Line2D([], [], marker=marker, ls="", mfc="0.55", mec="white", mew=0.8, ms=9 if marker == "o" else 10), label)


def finish(fig, ax, h, lab, out, ncol=2, y=-0.005):
    fig.legend(h, lab, loc="lower center", ncol=ncol, frameon=False, fontsize=7, bbox_to_anchor=(0.5, y), handler_map={RouteKey: HandlerRoute()})
    fig.savefig(out, dpi=DPI, bbox_inches="tight", pad_inches=0.05)
    plt.close(fig)
    print("wrote", out.relative_to(REPO))


def site_axes(figsize):
    fig, ax = plt.subplots(figsize=figsize)
    return fig, ax


def pos_along(g, frac):
    g = g.sort_values("dist_m")
    xy = pts_web(g.lat, g.lon)
    d = g.dist_m.to_numpy()
    return np.array([np.interp(frac * d.max(), d, xy[:, 0]), np.interp(frac * d.max(), d, xy[:, 1])])


def zone_box(ax, text, xy, off_pts, zorder=12, ha="center"):
    ax.annotate(text, xy, xytext=off_pts, textcoords="offset points", fontsize=7.5, ha=ha, va="center",
                zorder=zorder, bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="0.3", lw=0.7, alpha=0.95),
                arrowprops=dict(arrowstyle="-", color="0.25", lw=0.7, shrinkA=0, shrinkB=2))


def zone_centroid(g, zone):
    s = g[g.zone == zone]
    xy = pts_web(s.lat, s.lon)
    return xy[len(xy) // 2] if len(xy) else None


def fig_site(site):
    t = tidy_salinity()
    ts = t[t.paper_site == site]
    stats = zone_stats(ts)
    F_web, band_web, F_m = faults_web()
    xy_all = pts_web(ts.lat, ts.lon)
    lat0 = ts.lat.mean()
    norm = Normalize(ts.EC.min() - 0.3, ts.EC.max() + 0.3)
    if site == 3:
        return _site3(ts, stats, norm, F_web, band_web, F_m, lat0)
    figsize = {1: (6.6, 5.6), 2: (6.6, 6.3)}[site]
    fig, ax = site_axes(figsize)
    aspect = {1: 1.15, 2: 0.82}[site]
    ext = base_axes(ax, xy_all, pad_frac={1: 0.9, 2: 0.2}[site], aspect_w_over_h=aspect)
    add_basemap_safe(ax, source=BASE)
    ax.set_xlim(ext[0], ext[1]); ax.set_ylim(ext[2], ext[3])
    draw_context(ax, ext, F_web, band_web)
    channel_line(ax, ts)
    sc_markers(ax, ts, norm, by_day=False)
    wp_all = wwtp_points(ext)
    off_map = [w for w in wp_all if w[0] == "Valley Dale STP"]   # discharges to a tributary ~2 km away
    wp = [w for w in wp_all if w[0] != "Valley Dale STP"]
    print('  site', site, 'facilities in frame:', [w[0] for w in wp], '| off-map note:', [w[0] for w in off_map])
    draw_wwtp(ax, wp, WWTP_OFF.get(site, {}))
    for nm, x, y in off_map:
        ax.annotate(nm + " \u2192", (ext[1], y), xytext=(-4, 0), textcoords="offset points", ha="right",
                    va="center", fontsize=7.5, color=WWTP_COLOR, fontweight="bold", zorder=10,
                    bbox=dict(boxstyle="round,pad=0.12", fc="white", ec="none", alpha=0.85))
    g = ts[ts.transect == f"S{site}"]
    bt = {1: ("A", "1-1", "1-2", "28 Sep"), 2: ("B", "2-1", "2-2", "5 Oct")}[site]
    mid, tan = boundary_tick(g, bt[1], bt[2])
    if site == 1:
        draw_contrast(ax, mid, tan, "A", "tributary junction", lat0, "", ground_half=80, lab_pts=(-55, 55), lab_dir=-1)
        flow_arrow(ax, g, 0.78, 0.97, lat0, side_m=-60, label_off=(-24, 0))
        zone_box(ax, f"Zone 1-1 (n={stats[('1-1','2018-09-28')][0]})\n{stats[('1-1','2018-09-28')][1]:.1f} ± {stats[('1-1','2018-09-28')][2]:.1f}",
                 zone_centroid(g, '1-1'), (70, -85))
        zone_box(ax, f"Zone 1-2 (n={stats[('1-2','2018-09-28')][0]})\n{stats[('1-2','2018-09-28')][1]:.1f} ± {stats[('1-2','2018-09-28')][2]:.1f}",
                 zone_centroid(g, '1-2'), (-40, -95))
        ax.text(0.015, 0.985, "28 Sep 2018; values: within-zone mean ± SD, µS/cm",
                transform=ax.transAxes, fontsize=7, va="top", bbox=dict(fc="white", ec="none", alpha=0.85, pad=1.5), zorder=12)
    if site == 2:
        draw_contrast(ax, mid, tan, "B", "fault position interpreted\nin the field (90\u00b0 bend)", lat0, "", ground_half=300, lab_pts=(95, 0), lab_dir=-1)
        flow_arrow(ax, g, 0.24, 0.36, lat0, side_m=-170, label_off=(-22, 0))
        for z, (fr, off) in {"2-1": (0.12, (-95, 30)), "2-2": (0.94, (105, 10))}.items():
            n, m, s = stats[(z, "2018-10-05")]
            zone_box(ax, f"Zone {z} (n={n})\n{m:.1f} ± {s:.1f}", pos_along(g, fr), off)
        ax.text(0.015, 0.985, "5 Oct 2018; values: within-zone mean ± SD, µS/cm",
                transform=ax.transAxes, fontsize=7, va="top", bbox=dict(fc="white", ec="none", alpha=0.85, pad=1.5), zorder=12)
    add_scalebar(ax, _round_scale((ext[1] - ext[0]) / 2 * math.cos(math.radians(lat0))), lat0)
    north_arrow(ax)
    sc_colorbar(fig, ax, norm)
    extra = ([wwtp_entry()] if wp else []) + route_entries({1: set(), 2: {'US'}}[site])
    date = {1: "28 Sep 2018", 2: "5 Oct 2018"}[site]
    h, lab = common_legend(fig, [survey_entry(f"Survey point ({date})")], extra)
    finish(fig, ax, h, lab, FIG / f"rev_site{site}.png", ncol={1: 2, 2: 1}[site], y={1: -0.005, 2: -0.12}[site])


def site2_note(g):
    d = nearest_dist_m(g.lat, g.lon, load_faults_metric())
    return f"Survey points are {d.min():.0f}\u2013{d.max():.0f} m from the digitized trace"


def _site2_marks(ax, g, F_m, lat0):
    """Mark every place the digitized trace meets the surveyed channel, and number them."""
    gm = g.sort_values("dist_m")
    pm = points_metric(gm.lat, gm.lon)
    line = LineString([(p.x, p.y) for p in pm])
    d_tot = gm.dist_m.max()
    u = F_m.geometry.union_all()
    inter = line.intersection(u)
    pts = [p for p in getattr(inter, "geoms", [inter]) if p.geom_type == "Point"]
    pts = sorted(pts, key=lambda p: line.project(p))
    res = []
    for k, p in enumerate(pts, 1):
        w = gpd.GeoSeries([p], crs=METRIC_CRS).to_crs(WEB).iloc[0]
        km = line.project(p) * d_tot / line.length / 1000
        ax.plot(w.x, w.y, marker="X", ms=11, mfc="white", mec="black", mew=1.3, zorder=10)
        ax.annotate(f"crossing {k}\n({km:.1f} km along survey)", (w.x, w.y), xytext=(48 if k == 1 else -48, 4 if k == 1 else 24),
                    textcoords="offset points", fontsize=7, ha="center", va="center", zorder=12,
                    bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="0.3", lw=0.7),
                    arrowprops=dict(arrowstyle="-", color="0.25", lw=0.7))
        res.append((k, km))
    print("  site 2 survey-line/trace crossings (km along survey):", res)


# ------------------------------------------------------------------ site 3
def _site3(ts, stats, norm, F_web, band_web, F_m, lat0):
    W, MAPH, H = 7.2, 5.3, 8.8
    fig = plt.figure(figsize=(W, H))
    ax = fig.add_axes([0.01, 1 - MAPH / H - 0.003, 0.86, MAPH / H])
    xy_all = pts_web(ts.lat, ts.lon)
    aspect = 0.86 * W / MAPH
    ext = base_axes(ax, xy_all, pad_frac=0.25, aspect_w_over_h=aspect)
    add_basemap_safe(ax, source=BASE)
    ax.set_xlim(ext[0], ext[1]); ax.set_ylim(ext[2], ext[3])
    draw_context(ax, ext, F_web, band_web, label_frac={"US 44": 0.55})
    channel_line(ax, ts)
    print('  site 3 facilities in frame:', [w[0] for w in wwtp_points(ext)])
    draw_wwtp(ax, wwtp_points(ext), {})
    c = chloride_transect()
    cxy = pts_web(c.lat, c.lon)
    ax.plot(cxy[:, 0], cxy[:, 1], color=OI["orange"], lw=5.5, alpha=0.65, zorder=5.2, solid_capstyle="round")
    star = int(c.Notes.fillna("").str.contains("long-term").idxmax())
    ax.plot(*cxy[star], marker="*", ms=15, mfc="red", mec="black", mew=0.9, zorder=11)
    for lab, i, off in (("Z", 0, (-12, 12)), ("Z\u2032", len(c) - 1, (-6, -16))):
        ax.annotate(lab, cxy[i], xytext=off, textcoords="offset points", fontsize=11, fontweight="bold",
                    zorder=12, ha="center", va="center", path_effects=halo(3.5))
    sc_markers(ax, ts, norm, by_day=True, size=44)
    t19 = ts[ts.transect == "S3-19Oct"]
    t26l = ts[ts.transect == "S3-26Oct-lower"]
    t26u = ts[ts.transect == "S3-26Oct-upper"]
    mC, tC = boundary_tick(t19, "3-1", "3-2")
    mD, tD = boundary_tick(t19, "3-2", "3-3")
    mE, tE = boundary_tick(t26l, "3-3", "3-4")
    mC2, tC2 = boundary_tick(t26u, "3-1", "3-2")
    draw_contrast(ax, mC, tC, "C", "tributary", lat0, "\n(19 & 26 Oct)", ground_half=130, lab_dir=1, lab_pts=(10, 50))
    draw_contrast(ax, mD, tD, "D", "fault zone", lat0, "\n(19 Oct only)", ground_half=130, lab_dir=1, lab_pts=(-95, 20))
    draw_contrast(ax, mE, tE, "E", "fault zone", lat0, "\n(26 Oct only)", ground_half=130, lab_dir=-1, lab_pts=(-25, 55))
    flow_arrow(ax, t19, 0.63, 0.74, lat0, side_m=90, label_off=(0, -14))
    # zone ids with leaders
    zone_box(ax, "Zone 3-3", zone_centroid(t19, "3-3"), (-70, 18))
    zone_box(ax, "Zone 3-4", zone_centroid(t26l, "3-4"), (-20, -42))
    # inset extent: overlapping reach of zones 3-1/3-2 (both days)
    ov = ts[ts.zone.isin(["3-1", "3-2"])]
    oxy = pts_web(ov.lat, ov.lon)
    ix0, ix1 = oxy[:, 0].min() - 60, oxy[:, 0].max() + 60
    iy0, iy1 = oxy[:, 1].min() - 60, oxy[:, 1].max() + 60
    IW, IH = 4.15, 1.95
    r = IW / IH
    if (ix1 - ix0) / (iy1 - iy0) > r:
        m = (iy0 + iy1) / 2; hh = (ix1 - ix0) / r / 2; iy0, iy1 = m - hh, m + hh
    else:
        m = (ix0 + ix1) / 2; hw = (iy1 - iy0) * r / 2; ix0, ix1 = m - hw, m + hw
    ax.add_patch(plt.Rectangle((ix0, iy0), ix1 - ix0, iy1 - iy0, fill=False, ec="black", lw=1.3, ls="--", zorder=13))
    ax.annotate("Zones 3-1, 3-2\n(inset below)", (ix0 + (ix1 - ix0) / 2, iy0), xytext=(40, -8), textcoords="offset points",
                ha="center", va="top", fontsize=7.5, zorder=13,
                bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="0.3", lw=0.7))
    ia = fig.add_axes([0.03, 1.15 / H, IW / W, IH / H])
    ia.set_xlim(ix0, ix1); ia.set_ylim(iy0, iy1)
    ia.set_aspect("equal")
    ia.set_xticks([]); ia.set_yticks([])
    add_basemap_safe(ia, source=BASE)
    ia.set_xlim(ix0, ix1); ia.set_ylim(iy0, iy1)
    ibox = box(ix0, iy0, ix1, iy1)
    w = m2web(net()["all_m"])
    draw_lines(ia, w[w.intersects(ibox)].intersection(ibox), color=STREAM, lw=1.1, zorder=3)
    draw_lines(ia, F_web[F_web.intersects(ibox)].intersection(ibox), color="black", lw=1.9, zorder=4,
               path_effects=halo(3.6))
    ia.plot(cxy[:, 0], cxy[:, 1], color=OI["orange"], lw=5.5, alpha=0.65, zorder=5.2)
    sc_markers(ia, ts, norm, by_day=True, size=70)
    for (m_, t_), lab, mk in ((((mC, tC)), "C \u25cf", 1), (((mC2, tC2)), "C \u25b2", -1)):
        nrm = np.array([-t_[1], t_[0]]) * 75 * mkc(lat0)
        ia.plot(*zip(m_ - nrm, m_ + nrm), color="black", lw=2.4, zorder=8, path_effects=halo(4.6))
        ia.annotate(lab, m_ + nrm * (1 if mk == 1 else -1), xytext=(0, 9 * mk), textcoords="offset points",
                    ha="center", va="center", fontsize=8, fontweight="bold", zorder=12,
                    bbox=dict(boxstyle="round,pad=0.12", fc="white", ec="black", lw=0.7))
    for z, tt, off in (("3-1", t26u, (0, 22)), ("3-2", t26u, (0, 22))):
        sub = tt[tt.zone == z]
        p = pts_web(sub.lat, sub.lon)[len(sub) // 2]
        ia.annotate(f"Zone {z}", p, xytext=off, textcoords="offset points", fontsize=7.5, fontweight="bold",
                    ha="center", va="center", zorder=12,
                    bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="0.3", lw=0.7))
    for sp in ia.spines.values():
        sp.set_linewidth(1.5)
    ia.set_title("Inset: reach surveyed on both days (zones 3-1 and 3-2)", fontsize=7.5, loc="left", pad=3)
    add_scalebar(ia, 200, lat0)
    add_scalebar(ax, _round_scale((ext[1] - ext[0]) / 2 * math.cos(math.radians(lat0))), lat0)
    north_arrow(ax)
    # colour bar
    cax = fig.add_axes([0.905, 1 - MAPH / H + 0.03, 0.022, MAPH / H - 0.08])
    cb = fig.colorbar(ScalarMappable(norm=norm, cmap=CMAP), cax=cax)
    cb.set_label(r"Specific conductance ($\mu$S cm$^{-1}$)", fontsize=8)
    cb.ax.tick_params(labelsize=7)
    # table of within-day stats (right of inset)
    rows = [("3-1", "2018-10-19"), ("3-1", "2018-10-26"), ("3-2", "2018-10-19"), ("3-2", "2018-10-26"),
            ("3-3", "2018-10-19"), ("3-3", "2018-10-26"), ("3-4", "2018-10-26")]
    lines = ["Within-day SC, mean \u00b1 SD (n), \u00b5S/cm"]
    for z, d in rows:
        n, m_, s_ = stats[(z, d)]
        mk = "\u25cf" if d.endswith("19") else "\u25b2"
        lines.append(f"{mk} Zone {z}, {d[-2:]} Oct: {m_:6.1f} \u00b1 {s_:.1f} ({n})")
    fig.text(0.625, (1.15 + IH) / H, "\n".join(lines), fontsize=6.6, va="top", ha="left",
             family="DejaVu Sans Mono", linespacing=1.4,
             bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="0.3", lw=0.7))
    h, lab = common_legend(fig, [survey_entry("Survey point, 19 Oct 2018 (circle)"),
                                 survey_entry("Survey point, 26 Oct 2018 (triangle)", "^")], [
        (Line2D([], [], color=OI["orange"], lw=5.5, alpha=0.65), "Chloride transect Z\u2013Z\u2032 (20 Jul 2020)"),
        (Line2D([], [], marker="*", ls="", mfc="red", mec="black", ms=12), "Kelly et al. (2019) long-term site")]
        + route_entries({"US", "NY"}))
    fig.legend(h, lab, loc="lower center", ncol=2, frameon=False, fontsize=7, bbox_to_anchor=(0.5, 0.0), handler_map={RouteKey: HandlerRoute()})
    out = FIG / "rev_site3.png"
    fig.savefig(out, dpi=DPI)
    plt.close(fig)
    print("wrote", out.relative_to(REPO))


# ------------------------------------------------------------------ overview
HWY = {  # short label -> FULLNAMEs in TIGER (Taconic is S1400 in TIGER, added by name)
    "I-84": ["I- 84"], "US 9": ["US Hwy 9", "Rte 9"], "US 44": ["US Hwy 44", "Rte 44"],
    "NY 82": ["Rte 82", "State Rte 82"], "NY 22": ["Rte 22", "State Rte 22"],
    "Taconic State Pkwy": ["Taconic State Pkwy"]}


def hudson_polygons():
    """Filled water polygons for the Hudson River (USGS NHD): NHDArea StreamRiver (FTYPE 460)
    plus the NHDWaterbody Estuary (FTYPE 493), in EPSG:3857.  Files in data/nhd/ (see README)."""
    a = gpd.read_file(DATA / "nhd" / "nhd_area_hudson.geojson")
    a = a[a.FTYPE == 460]
    w = gpd.read_file(DATA / "nhd" / "nhd_waterbody_dutchess.geojson")
    w = w[w.FTYPE == 493]
    g = pd.concat([a.geometry, w.geometry]).to_crs(WEB)
    return g.drop_duplicates(ignore_index=True)


def acceptance_check(wap_m):
    """Every SC survey point and chloride point must lie within ~150 m of the Wappinger line."""
    u = wap_m.union_all()
    t = tidy_salinity()
    res = {}
    for site, g in t.groupby("paper_site"):
        res[f"Site {site}"] = max(p.distance(u) for p in points_metric(g.lat, g.lon))
    c = chloride_transect()
    res["Chloride"] = max(p.distance(u) for p in points_metric(c.lat, c.lon))
    print("Wappinger Creek line, max distance of survey points (m):", {k: round(v) for k, v in res.items()})
    assert all(v <= 150 for v in res.values()), res
    return res


def fig_overview():
    from maps import _budnik_extent
    ext = _budnik_extent()
    left, right, bottom, top = ext
    t = tidy_salinity()
    F_web, _, _ = faults_web()
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(8.3, 6.4), gridspec_kw={"width_ratios": [0.69, 0.60]})
    img = plt.imread(FIG / "budnik_faultmap.png")
    axL.imshow(img)
    ih_, iw_ = img.shape[:2]
    # single north arrow for the whole figure, directly under panel (a)'s legend box
    axL.annotate("N", xy=(0.107 * iw_, 0.095 * ih_), xytext=(0.107 * iw_, 0.095 * ih_ + 0.11 * ih_),
                 arrowprops=dict(arrowstyle="-|>,head_width=0.5,head_length=0.9", color="black", lw=3),
                 ha="center", va="top", fontsize=15, fontweight="bold", annotation_clip=False)
    axL.set_axis_off()
    axL.set_title("(a) Budnik et al. (2010) fault map", fontsize=10)
    axL.text(0.5, -0.02, "Taken directly from Budnik, Walker & Menking (2010), Fig. 3.10,\n"
             "Natural Resource Inventory of Dutchess County, NY.", transform=axL.transAxes, ha="center",
             va="top", fontsize=7, color="0.3")
    ax = axR
    ax.set_xlim(left, right); ax.set_ylim(bottom, top); ax.set_aspect("equal")
    ax.set_xticks([]); ax.set_yticks([])
    add_basemap_safe(ax, source=BASE)
    ax.set_xlim(left, right); ax.set_ylim(bottom, top)
    bbox = box(left, bottom, right, top)
    lat0 = cy = 41.75
    # streams (USGS NHD): Wappinger Creek + East Branch highlighted; six longest other named streams
    hud = hudson_polygons()
    draw_polys(ax, hud.intersection(bbox).loc[lambda q: ~q.is_empty], fc=WATER, ec="none", zorder=2.2)
    lp = hud.intersection(box(left, (bottom + top) / 2 + 0.07 * (top - bottom), right, (bottom + top) / 2 + 0.17 * (top - bottom)))
    lp = lp[~lp.is_empty].union_all()
    ax.text(lp.representative_point().x - 1500, lp.representative_point().y, "Hudson River", rotation=80, fontsize=8,
            fontstyle="italic", color="#1f5f8b", ha="center", va="center", zorder=11)
    N_ = net()
    wap = m2web(N_["wappinger_m"])
    for nm, ln, g in N_["others_m"]:
        draw_lines(ax, m2web(g), color=OI["sky"], lw=1.2, zorder=3)
    draw_lines(ax, wap, color=OI["blue"], lw=2.6, zorder=4)
    acceptance_check(N_["wappinger_m"])
    # highways
    r = tiger_roads().to_crs(WEB)
    for short, names in HWY.items():
        sub = r[r.FULLNAME.isin(names)]
        sub = sub[sub.intersects(bbox)]
        if not len(sub):
            continue
        draw_lines(ax, sub.geometry, color="#6b6b6b", lw=1.5, zorder=5, path_effects=halo(2.8))
    # faults
    draw_lines(ax, F_web[F_web.intersects(bbox)], color="black", lw=1.2, zorder=6, path_effects=halo(2.4))
    # site boxes
    for site in (1, 2, 3):
        ts = t[t.paper_site == site]
        xy = pts_web(ts.lat, ts.lon)
        pad = (top - bottom) * 0.012
        x0, y0 = xy[:, 0].min() - pad, xy[:, 1].min() - pad
        wd, ht = np.ptp(xy[:, 0]) + 2 * pad, np.ptp(xy[:, 1]) + 2 * pad
        ax.add_patch(plt.Rectangle((x0, y0), wd, ht, fill=False, ec=OI["verm"], lw=2.2, zorder=9))
    off = {1: (-4, 12, "right"), 2: (-8, 4, "right"), 3: (10, 14, "left")}
    for site in (1, 2, 3):
        ts = t[t.paper_site == site]
        xy = pts_web(ts.lat, ts.lon)
        dx, dy, ha = off[site]
        ax.annotate(f"Site {site}", (xy[:, 0].mean(), xy[:, 1].max()), xytext=(dx, dy), textcoords="offset points",
                    ha=ha, va="bottom", fontsize=9.5, fontweight="bold", zorder=10,
                    bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=OI["verm"], lw=1.2))
    # labels: Wappinger Creek, highways (placed on the longest in-extent piece)
    anchor = gpd.GeoSeries([Point(-73.885, 41.655)], crs="EPSG:4326").to_crs(WEB).iloc[0]
    wu = wap.union_all()
    from shapely.ops import nearest_points
    pt = nearest_points(wu, anchor)[0]
    ax.annotate("Wappinger Creek", (pt.x, pt.y), xytext=(75, -10), textcoords="offset points", fontsize=8.5,
                fontweight="bold", color=OI["blue"], zorder=10, ha="left",
                bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=OI["blue"], lw=0.9),
                arrowprops=dict(arrowstyle="-", color=OI["blue"], lw=1.0))
    frac = {"I-84": 0.45, "US 9": 0.5, "US 44": 0.6, "NY 82": 0.85, "NY 22": 0.5, "Taconic State Pkwy": 0.9}
    for short, names in HWY.items():
        sub = r[r.FULLNAME.isin(names)]
        sub = sub[sub.intersects(bbox)]
        if not len(sub):
            continue
        g = sub.geometry.intersection(bbox)
        parts = [p for q in g[~g.is_empty] for p in getattr(q, "geoms", [q]) if p.geom_type == "LineString"]
        lg = max(parts, key=lambda p: p.length)
        pt = lg.interpolate(frac[short], normalized=True)
        route_label(ax, pt.x, pt.y, short, ms=14)
    wp = wwtp_points((left, right, bottom, top))
    draw_wwtp(ax, wp, {"Millbrook STP": (9, -2, "left")}, size=6)
    add_scalebar(ax, 10000, lat0)
    h = [Line2D([], [], color="black", lw=1.4, path_effects=halo(2.4)),
         Line2D([], [], color=OI["blue"], lw=2.6), Line2D([], [], color=OI["sky"], lw=1.1),
         Line2D([], [], color="#6b6b6b", lw=1.5, path_effects=halo(2.8)),
         Patch(fc="none", ec=OI["verm"], lw=2.2), wwtp_entry()[0]] + [e[0] for e in route_entries({"I", "US", "NY"})]
    lab = ["High-angle fault (Budnik et al. 2010)", "Wappinger Creek", "Other major streams",
           "Major highway", "Study site", WWTP_LABEL] + [e[1] for e in route_entries({"I", "US", "NY"})]
    ax.legend(h, lab, loc="upper center", bbox_to_anchor=(0.5, -0.012), ncol=3, fontsize=6.5, frameon=False, columnspacing=1.0, handlelength=1.6, handler_map={RouteKey: HandlerRoute()})
    ax.set_title("(b) Study area: faults, highways and streams", fontsize=10)
    fig.subplots_adjust(left=0.0, right=0.995, top=0.95, bottom=0.07, wspace=0.01)
    out = FIG / "rev_overview.png"
    fig.savefig(out, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print("wrote", out.relative_to(REPO))


# ------------------------------------------------------------------ chloride (Fig 5)
def fig_chloride():
    import changepoint as cp
    c = chloride_transect()
    faults = load_faults_metric()
    d, y = c.distance_m.to_numpy(), c.Cl.to_numpy()
    summ = pd.read_csv(REPO / "docs" / "logs" / "changepoint_summary.csv")
    row = summ[summ.transect == "Chloride"].iloc[0]
    bp, blo, bhi = float(row.bp), float(row.boot_lo), float(row.boot_hi)
    beta = cp.fit(d, y, (bp,))[0]
    t = tidy_salinity()
    line, _ = cp.line_of(c.lat, c.lon)
    dtot = d.max()
    inf = t[t.InFault == "yes"]
    pos = {}
    for k, tr in (("D", "S3-19Oct"), ("E", "S3-26Oct-lower")):
        sub = inf[inf.transect == tr]
        pos[k] = [cp.along_from_proj(line, p, dtot) for p in points_metric(sub.lat, sub.lon)]
    cross = cp.trace_crossings(line, faults, dtot)
    star = int(c.Notes.fillna("").str.contains("long-term").idxmax())
    fig, ax = plt.subplots(figsize=(7.0, 4.1))
    ymax = y.max() * 1.3
    ax.set_ylim(0, ymax); ax.set_xlim(-60, dtot + 80)
    ax.axvspan(blo, bhi, color=OI["orange"], alpha=0.30, lw=0, zorder=1)
    xs = np.linspace(d.min(), d.max(), 300)
    ax.plot(xs, cp.design(xs, (bp,)) @ beta, color=OI["verm"], lw=2.2, zorder=3)
    ax.axvline(bp, color=OI["verm"], lw=1.0, ls="--", zorder=2)
    ax.plot(d, y, color="0.45", lw=0.8, zorder=3)
    ax.scatter(d, y, s=30, c="black", edgecolor="white", linewidth=0.6, zorder=4)
    ax.plot(d[star], y[star], marker="*", ms=17, mfc="none", mec="red", mew=1.6, zorder=6)
    for k, col in (("D", OI["purple"]), ("E", OI["purple"])):
        for x in pos[k]:
            ax.plot([x, x], [0, ymax * 0.07], color=col, lw=2.4, zorder=5, solid_capstyle="butt")
        ax.annotate(f"{k} fault\npoints", (np.mean(pos[k]), ymax * 0.075), xytext=(0, 5), textcoords="offset points",
                    ha="center", va="bottom", fontsize=7.5, color="#8a3f6d", fontweight="bold", zorder=6)
    for x in cross:
        ax.plot([x], [0], marker="X", ms=7, mfc="#bbbbbb", mec="#666666", mew=0.6, clip_on=False, zorder=7)
        ax.axvline(x, color="#bbbbbb", lw=0.9, ls=":", zorder=2)
        ax.annotate("county-map trace\ncrosses path\n(approximate)", (x, ymax * 0.62), ha="center", fontsize=7, color="#666666",
                    bbox=dict(fc="white", ec="none", alpha=0.85, pad=1))
    ax.annotate("Z", (d[0], y[0]), xytext=(-10, 8), textcoords="offset points", fontsize=11, fontweight="bold")
    ax.annotate("Z\u2032", (d[-1], y[-1]), xytext=(4, 10), textcoords="offset points", fontsize=11, fontweight="bold")
    ax.annotate("Kelly et al. (2019)\nlong-term site", (d[star], y[star]), xytext=(12, 22), textcoords="offset points",
                fontsize=7.5, color="red", ha="left", arrowprops=dict(arrowstyle="-", color="red", lw=0.8))
    ax.set_xlabel("Distance along transect from Z (m)")
    ax.set_ylabel(r"Chloride (mg L$^{-1}$)")
    ax.grid(True, ls=":", alpha=0.4)
    h = [Line2D([], [], marker="o", ls="", color="k", label="Chloride sample (20 Jul 2020)"),
         Line2D([], [], color=OI["verm"], lw=2.2, label=f"Segmented regression (1 breakpoint, BIC), at {bp:.0f} m"),
         Patch(fc=OI["orange"], alpha=0.30, label=f"Breakpoint 95% bootstrap interval ({blo:.0f}\u2013{bhi:.0f} m)"),
         Line2D([], [], color=OI["purple"], lw=2.4, label="Fault points at Contrasts D and E (survey points downstream of a fault), projected onto path"),
         Line2D([], [], marker="X", ls="", mfc="#bbbbbb", mec="#666666", ms=7, label="Digitized county-map fault trace crosses survey line (approximate)")]
    ax.legend(handles=h, loc="upper center", fontsize=7, frameon=False, ncol=2, bbox_to_anchor=(0.5, -0.17))
    fig.tight_layout()
    out = FIG / "rev_chloride.png"
    fig.savefig(out, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print("wrote", out.relative_to(REPO), " D:", [round(x) for x in pos["D"]], "E:", [round(x) for x in pos["E"]],
          "cross:", [round(x) for x in cross], "bp", bp, blo, bhi)


def main(args):
    which = args or ["overview", "1", "2", "3", "chloride"]
    for w in which:
        if w == "overview":
            fig_overview()
        elif w == "chloride":
            fig_chloride()
        else:
            fig_site(int(w))


if __name__ == "__main__":
    main(sys.argv[1:])
