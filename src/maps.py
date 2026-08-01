"""Regenerate the site maps (Figures 1-4) from source data.

Each map places the surveyed points on an OpenStreetMap basemap, coloured by
per-site normalized specific conductance (the original light-blue -> blue ->
black -> orange -> yellow ramp), and overlays the zone boxes, contrast arrows,
a fault-trace band, a north arrow, and a scale bar.

Reproducibility note: the point locations, colours, zone membership, and
contrast arrows are all derived from the data. The *fault trace* is not stored
as coordinates anywhere -- in the original figures it was drawn by hand from
the Dutchess County geologic map (Budnik et al. 2010). Here it is approximated
as the band through the points flagged ``InFault == yes`` in the dataset and
should be treated as schematic; refine with digitized fault coordinates before
final submission.

Run:  .venv/bin/python src/maps.py
"""

from pathlib import Path
import math
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import FancyArrowPatch, Rectangle
import contextily as cx

from wappingers import load_salinity, zone_frames, SITE_ZONES, CONTRASTS

FIG = Path(__file__).resolve().parent.parent / "figures"

EC_CMAP = LinearSegmentedColormap.from_list(
    "ec", ["lightblue", "blue", "black", "orange", "yellow"]
)

# Per-site view: (center lat, lon, half-width in metres). Tuned to frame each
# site's points with context, echoing the zoom levels in the original script.
SITE_VIEW = {
    1: (41.8033, -73.7845, 900),
    2: (41.7150, -73.8500, 5200),
    3: (41.7895, -73.7285, 1500),
}


def merc(lon, lat):
    r = 6378137.0
    x = r * math.radians(lon)
    y = r * math.log(math.tan(math.pi / 4 + math.radians(lat) / 2))
    return x, y


def add_scalebar(ax, x0, y0, length_m, lat):
    """Draw a simple scale bar; correct for Mercator stretch at this latitude."""
    stretch = 1.0 / math.cos(math.radians(lat))
    w = length_m * stretch
    ax.add_patch(Rectangle((x0, y0), w, w * 0.03, color="black", zorder=6))
    ax.text(x0 + w / 2, y0 + w * 0.05, f"{length_m/1000:g} km",
            ha="center", va="bottom", fontsize=8, zorder=6)


def north_arrow(ax, x, y, size):
    ax.annotate("N", xy=(x, y), xytext=(x, y - size),
                arrowprops=dict(arrowstyle="-|>", color="black", lw=1.5),
                ha="center", va="center", fontsize=11, fontweight="bold", zorder=6)


def draw_site(site, df, zframes):
    clat, clon, half = SITE_VIEW[site]
    cx0, cy0 = merc(clon, clat)
    stretch = 1.0 / math.cos(math.radians(clat))
    half_x = half * stretch

    fig, ax = plt.subplots(figsize=(5.2, 5.0))
    ax.set_xlim(cx0 - half_x, cx0 + half_x)
    ax.set_ylim(cy0 - half_x, cy0 + half_x)

    zones = SITE_ZONES[site]
    all_nec = np.concatenate([zframes[z]["NEC"].to_numpy() for z in zones])
    vlim = np.abs(all_nec).max()

    centroids = {}
    for z in zones:
        fr = zframes[z]
        xs, ys = zip(*[merc(lo, la) for lo, la in zip(fr["lon"], fr["lat"])])
        xs, ys = np.array(xs), np.array(ys)
        ax.scatter(xs, ys, c=fr["NEC"], cmap=EC_CMAP, vmin=-vlim, vmax=vlim,
                   s=45, edgecolor="white", linewidth=0.5, zorder=5)
        # Draw a tight box around each contiguous cluster of the zone's points
        # (a zone such as 3-2 is split into two clusters along the reach).
        pad = half_x * 0.05
        for cx_, cy_ in _clusters(xs, ys, gap=half_x * 0.4):
            ax.add_patch(Rectangle(
                (cx_.min() - pad, cy_.min() - pad),
                np.ptp(cx_) + 2 * pad, np.ptp(cy_) + 2 * pad,
                fill=False, edgecolor="black", lw=1.5, zorder=4))
        # label near the zone's largest cluster, offset to reduce collisions
        ax.annotate(f"Zone {z}", (xs.mean(), ys.max()),
                    textcoords="offset points", xytext=(0, 6),
                    fontsize=9.5, fontweight="bold", zorder=6, ha="center")
        centroids[z] = (xs.mean(), ys.mean())

    add_basemap_safe(ax)

    # fault-trace band: line of best fit through THIS site's InFault points
    # (schematic; over the basemap, under the survey points).
    import pandas as pd
    site_pts = pd.concat([zframes[z] for z in zones])
    fault_pts = site_pts[site_pts["InFault"] == "yes"]
    if len(fault_pts) >= 2:
        fx, fy = zip(*[merc(lo, la) for lo, la in zip(fault_pts["lon"], fault_pts["lat"])])
        fx, fy = np.array(fx), np.array(fy)
        if np.ptp(fx) > np.ptp(fy):
            m, b = np.polyfit(fx, fy, 1)
            xline = np.array([cx0 - half_x, cx0 + half_x])
            yline = m * xline + b
        else:
            m, b = np.polyfit(fy, fx, 1)
            yline = np.array([cy0 - half_x, cy0 + half_x])
            xline = m * yline + b
        ax.plot(xline, yline, color="0.45", lw=16, alpha=0.5, zorder=3,
                solid_capstyle="round")

    # contrast arrows between zone centroids (fault = red, tributary = blue)
    for name, a, b, kind in CONTRASTS:
        if a in centroids and b in centroids:
            (xa, ya), (xb, yb) = centroids[a], centroids[b]
            color = "firebrick" if kind == "fault" else "steelblue"
            ax.add_patch(FancyArrowPatch(
                (xa, ya), (xb, yb), arrowstyle="-|>", mutation_scale=16,
                color=color, lw=2, zorder=7,
                shrinkA=12, shrinkB=12))
            ax.text((xa + xb) / 2, (ya + yb) / 2, name, color=color,
                    fontsize=12, fontweight="bold", zorder=8,
                    ha="center", va="center",
                    bbox=dict(boxstyle="circle,pad=0.15", fc="white", ec=color))

    add_scalebar(ax, cx0 - half_x * 0.9, cy0 - half_x * 0.9, _round_scale(half), clat)
    north_arrow(ax, cx0 + half_x * 0.85, cy0 + half_x * 0.9, half_x * 0.12)
    ax.set_axis_off()
    fig.tight_layout(pad=0.3)
    out = FIG / f"site{site}.png"
    fig.savefig(out, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"wrote {out.relative_to(FIG.parent)}")
    return centroids


def _clusters(xs, ys, gap):
    """Split a zone's points into contiguous clusters by nearest-neighbour gap.

    Points are visited in survey order; a jump larger than ``gap`` starts a new
    cluster. Yields (x-array, y-array) per cluster.
    """
    order = np.arange(len(xs))
    breaks = [0]
    for i in range(1, len(xs)):
        if math.hypot(xs[i] - xs[i - 1], ys[i] - ys[i - 1]) > gap:
            breaks.append(i)
    breaks.append(len(xs))
    for s, e in zip(breaks[:-1], breaks[1:]):
        yield xs[order[s:e]], ys[order[s:e]]


def _round_scale(half):
    # pick a tidy scale-bar length ~ 40% of half-width
    target = half * 0.8
    for v in (100, 200, 500, 1000, 2000, 5000):
        if v >= target:
            return v
    return 5000


def add_basemap_safe(ax):
    try:
        cx.add_basemap(ax, source=cx.providers.CartoDB.Positron)
    except Exception as e:  # noqa: BLE001
        print(f"  basemap fetch failed ({e!r}); leaving blank background")


def draw_overview(df, zframes):
    """Regional overview (Figure 1): all three sites, each in a dashed box."""
    pts = df.dropna(subset=["lat", "lon"])
    xs, ys = zip(*[merc(lo, la) for lo, la in zip(pts["lon"], pts["lat"])])
    xs, ys = np.array(xs), np.array(ys)
    cx0, cy0 = xs.mean(), ys.mean()
    half = max(np.ptp(xs), np.ptp(ys)) * 0.62

    fig, ax = plt.subplots(figsize=(5.4, 5.2))
    ax.set_xlim(cx0 - half, cx0 + half)
    ax.set_ylim(cy0 - half, cy0 + half)

    nec_all = np.concatenate([zframes[z]["NEC"].to_numpy() for z in zframes])
    vlim = np.abs(nec_all).max()
    for site, zs in SITE_ZONES.items():
        import pandas as pd
        sp = pd.concat([zframes[z] for z in zs])
        sx, sy = zip(*[merc(lo, la) for lo, la in zip(sp["lon"], sp["lat"])])
        sx, sy = np.array(sx), np.array(sy)
        ax.scatter(sx, sy, c=sp["NEC"], cmap=EC_CMAP, vmin=-vlim, vmax=vlim,
                   s=22, edgecolor="white", linewidth=0.3, zorder=5)
        pad = half * 0.05
        ax.add_patch(Rectangle((sx.min() - pad, sy.min() - pad),
                               np.ptp(sx) + 2 * pad, np.ptp(sy) + 2 * pad,
                               fill=False, edgecolor="black", lw=1.4,
                               linestyle=(0, (5, 4)), zorder=6))
        ax.annotate(f"Site {site}", (sx.mean(), sy.max() + pad),
                    textcoords="offset points", xytext=(0, 5), ha="center",
                    fontsize=11, fontweight="bold", zorder=7)
    add_basemap_safe(ax)
    add_scalebar(ax, cx0 - half * 0.9, cy0 - half * 0.92, 5000, cy_to_lat(cy0))
    north_arrow(ax, cx0 + half * 0.85, cy0 + half * 0.9, half * 0.1)
    ax.set_axis_off()
    fig.tight_layout(pad=0.3)
    out = FIG / "overview.png"
    fig.savefig(out, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"wrote {out.relative_to(FIG.parent)}")


def cy_to_lat(y):
    r = 6378137.0
    return math.degrees(2 * math.atan(math.exp(y / r)) - math.pi / 2)


if __name__ == "__main__":
    df = load_salinity()
    zframes = zone_frames(df)
    draw_overview(df, zframes)
    for site in (1, 2, 3):
        draw_site(site, df, zframes)
