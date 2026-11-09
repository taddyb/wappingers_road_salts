"""Change-point / segmented-regression analysis (revision round, WP0, task 3).

For each single-day SC transect (and the 2020 chloride transect):
  * continuous piecewise-linear regression of concentration vs along-channel
    distance with 0, 1, 2 breakpoints; breakpoints on a grid, >=3 data points in
    every segment; model chosen by BIC = n ln(RSS/n) + k ln(n), k = 2 + 2*nbp
    (intercept, slope, and per breakpoint: slope change + location). RSS/n is
    floored at the instrument resolution^2/12 so exact fits cannot give -inf BIC.
  * breakpoint uncertainty: (i) profile-RSS interval (positions whose
    n ln(RSS/RSS_min) <= 3.84, other breakpoint re-optimised) and (ii) residual
    bootstrap (500 reps, seed 1) of the BIC-selected model (or, if 0 breakpoints
    are selected, of the best 1-breakpoint model, flagged "not selected").
  * cross-check: ruptures PELT change-in-mean (l2 cost, min_size 3, penalty
    2 * sigma2 * ln(n), sigma2 = var(first differences)/2 floored at res^2/12).
  * distances from each breakpoint to InFault points, digitized fault traces
    and tributary junctions.
Run:  .venv/bin/python src/changepoint.py   (writes figures/rev_changepoint_*.png
and docs/logs/changepoint_summary.csv)
"""
import itertools
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from shapely.geometry import LineString, Point
import ruptures as rpt

from wappingers import (tidy_salinity, chloride_transect, load_faults_metric,
                        points_metric, REPO, METRIC_CRS)

MINSEG = 3
B = 500
CHI2_1 = 3.841
FIG = REPO / "figures"
LOG = REPO / "docs" / "logs"


# ------------------------------------------------------------------ fitting
def design(d, bps):
    cols = [np.ones_like(d), d] + [np.clip(d - b, 0, None) for b in bps]
    return np.column_stack(cols)


def fit(d, y, bps):
    X = design(d, bps)
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    r = y - X @ beta
    return beta, float((r ** 2).sum()), r


def ok_bps(d, bps, lo, hi):
    edges = [lo - 1] + list(bps) + [hi + 1]
    return all(((d > edges[i]) & (d <= edges[i + 1])).sum() >= MINSEG for i in range(len(edges) - 1))


def bic(rss, n, k, floor):
    return n * np.log(max(rss / n, floor)) + k * np.log(n)


def grid_for(d, nbp):
    lo, hi = d.min(), d.max()
    m = 140 if nbp == 1 else 60
    return np.linspace(lo, hi, m + 2)[1:-1]


def best_fit(d, y, nbp, floor):
    """Exhaustive grid search; returns (bps, rss, profile) where profile is a list
    of (bp-tuple, rss) over all feasible combos."""
    if nbp == 0:
        return (), fit(d, y, ())[1], [((), fit(d, y, ())[1])]
    G = grid_for(d, nbp)
    prof = []
    for bps in itertools.combinations(G, nbp):
        if not ok_bps(d, bps, d.min(), d.max()):
            continue
        prof.append((bps, fit(d, y, bps)[1]))
    if not prof:
        return None, np.inf, []
    bps, rss = min(prof, key=lambda t: t[1])
    return bps, rss, prof


def analyse(d, y, floor, label, rng):
    n = len(d)
    res = {}
    for nbp in (0, 1, 2):
        if n < MINSEG * (nbp + 1):
            continue
        bps, rss, prof = best_fit(d, y, nbp, floor)
        if bps is None:
            continue
        res[nbp] = dict(bps=bps, rss=rss, bic=bic(rss, n, 2 + 2 * nbp, floor), prof=prof)
    sel = min(res, key=lambda k: res[k]["bic"])
    out = dict(label=label, n=n, res=res, sel=sel)
    # intervals for the reported model
    rep = sel if sel > 0 else (1 if 1 in res else None)
    out["rep"] = rep
    if rep:
        r = res[rep]
        bps0 = np.array(r["bps"])
        prof_int = []
        for j in range(rep):
            vals = [(p[0][j], p[1]) for p in r["prof"]]
            ok = [v for v, s in vals if n * np.log(s / r["rss"]) <= CHI2_1]
            prof_int.append((min(ok), max(ok)))
        beta, _, resid = fit(d, y, tuple(bps0))
        yhat = y - resid
        boot = []
        for _ in range(B):
            yb = yhat + rng.choice(resid, size=n, replace=True)
            bb, _, _ = best_fit(d, yb, rep, floor)
            if bb is not None:
                boot.append(bb)
        boot = np.array(boot)
        out["prof_int"] = prof_int
        out["boot_int"] = [(np.percentile(boot[:, j], 2.5), np.percentile(boot[:, j], 97.5)) for j in range(rep)]
        out["beta"] = beta
        out["fit_bps"] = tuple(bps0)
    # PELT
    diff = np.diff(y)
    s2 = max(np.var(diff, ddof=1) / 2 if len(diff) > 1 else 0, floor)
    pen = 2 * s2 * np.log(n)
    algo = rpt.Pelt(model="l2", min_size=MINSEG, jump=1).fit(y.reshape(-1, 1))
    cps = [c for c in algo.predict(pen=pen) if c < n]
    out["pelt_idx"] = cps
    out["pelt_pos"] = [0.5 * (d[c - 1] + d[c]) for c in cps]
    out["pelt_steps"] = []
    edges = [0] + cps + [n]
    for i in range(1, len(edges) - 1):
        out["pelt_steps"].append(y[edges[i]:edges[i + 1]].mean() - y[edges[i - 1]:edges[i]].mean())
    out["pelt_pen"] = pen
    return out


def seg_stats(d, beta, bps):
    """slopes (units per km) of each segment and slope change at each bp, plus
    fitted change over +/-100 m around each bp."""
    bps = list(bps)
    slopes = [beta[1]]
    for j in range(len(bps)):
        slopes.append(slopes[-1] + beta[2 + j])
    f = lambda x: float((design(np.array([x]), bps) @ beta)[0])
    jump = [f(min(b + 100, d.max())) - f(max(b - 100, d.min())) for b in bps]
    return [1000 * s for s in slopes], [1000 * beta[2 + j] for j in range(len(bps))], jump


# ----------------------------------------------------------- geometry helpers
def line_of(lat, lon):
    p = points_metric(lat, lon)
    return LineString([(g.x, g.y) for g in p]), p


def along_from_proj(line, pt, dist_vec_total):
    """Projected position of pt on line, rescaled to haversine along-channel metres."""
    return line.project(pt) * dist_vec_total / line.length


def interp_point(line, d, dtot, x):
    return line.interpolate(x / dtot * line.length)


def trace_crossings(line, faults, dtot):
    """Along-channel positions where the straight-chord transect polyline crosses a trace."""
    out = []
    u = faults.geometry.union_all()
    inter = line.intersection(u)
    if inter.is_empty:
        return out
    geoms = getattr(inter, "geoms", [inter])
    for g in geoms:
        if g.geom_type == "Point":
            out.append(line.project(g) * dtot / line.length)
    return sorted(out)


def features(g, faults, is_chl=False):
    """Dict of positions (along-channel m) for one transect dataframe g (sorted)."""
    g = g.sort_values("dist_m")
    d = g.dist_m.to_numpy()
    line, pts = line_of(g.lat, g.lon)
    dtot = d.max()
    feat = dict(line=line, dtot=dtot)
    feat["infault"] = d[(g.InFault == "yes").to_numpy()] if "InFault" in g else np.array([])
    feat["trace_cross"] = trace_crossings(line, faults, dtot)
    # nearest approach of each trace to the polyline: location on the polyline
    u = faults.geometry.union_all()
    from shapely.ops import nearest_points
    p_line, p_tr = nearest_points(line, u)
    feat["closest_trace_pos"] = line.project(p_line) * dtot / line.length
    feat["closest_trace_dist"] = p_line.distance(p_tr)
    # junctions (zone boundaries) from zone labels
    junc = {}
    if "zone" in g:
        z = g.zone.to_numpy()
        for i in range(len(z) - 1):
            if isinstance(z[i], str) and isinstance(z[i + 1], str) and z[i] != z[i + 1]:
                junc[f"{z[i]}|{z[i+1]}"] = (0.5 * (d[i] + d[i + 1]), 0.5 * (d[i + 1] - d[i]))
    feat["boundaries"] = junc
    return feat


def dist_to_trace_at(feat, faults, x):
    p = interp_point(feat["line"], None, feat["dtot"], x)
    return p.distance(faults.geometry.union_all())


# ------------------------------------------------------------------ main
BOUNDARY_KIND = {"1-1|1-2": "tributary A", "2-1|2-2": "fault B", "3-1|3-2": "tributary C",
                 "3-2|3-3": "fault D", "3-3|3-4": "fault E"}


def report_transect(name, d, y, floor, g, faults, rng, unit, log, infault=None):
    a = analyse(d, y, floor, name, rng)
    feat = features(g, faults)
    if infault is not None:
        feat["infault"] = np.array(sorted(infault))
    log.append(f"\n=== {name}  (n={len(d)}, length {d.max():.0f} m) ===")
    for k, r in sorted(a["res"].items()):
        log.append(f"  {k} bp: RSS={r['rss']:.3f}  BIC={r['bic']:.2f}  bps={[round(b) for b in r['bps']]}")
    log.append(f"  BIC-selected breakpoints: {a['sel']}")
    log.append("  Ref. features (along-channel m): InFault pts=%s; polyline x trace=%s; closest approach to any trace=%.0f m (at %.0f m); boundaries=%s"
               % ([round(x) for x in feat["infault"]], [round(x) for x in feat["trace_cross"]],
                  feat["closest_trace_dist"], feat["closest_trace_pos"],
                  {k: round(v[0]) for k, v in feat["boundaries"].items()}))
    rows = []
    if a["rep"]:
        beta = a["beta"]
        slopes, dslope, jump = seg_stats(d, beta, a["fit_bps"])
        tag = "" if a["sel"] > 0 else " [NOT BIC-selected; best 1-bp fit shown]"
        log.append(f"  Reported model: {a['rep']} bp{tag}; segment slopes ({unit}/km): {[round(float(s),1) for s in slopes]}")
        for j, b in enumerate(a["fit_bps"]):
            pi, bi = a["prof_int"][j], a["boot_int"][j]
            inf = feat["infault"]
            dn = (np.abs(inf - b).min(), inf[np.abs(inf - b).argmin()]) if len(inf) else (np.nan, np.nan)
            tc = feat["trace_cross"]
            dtc = (np.abs(np.array(tc) - b).min() if len(tc) else np.nan)
            dtr = dist_to_trace_at(feat, faults, b)
            bnd = {k: abs(v[0] - b) for k, v in feat["boundaries"].items()}
            log.append(f"  bp{j+1} = {b:.0f} m  profile95 [{pi[0]:.0f}, {pi[1]:.0f}]  boot95 [{bi[0]:.0f}, {bi[1]:.0f}]  "
                       f"slope change {dslope[j]:+.2f} {unit}/km; fitted change over +/-100 m {jump[j]:+.2f} {unit}")
            log.append(f"      nearest InFault pt {dn[0]:.0f} m (at {dn[1]:.0f}); along-channel to polyline-trace crossing {dtc:.0f} m; "
                       f"straight-line to nearest trace {dtr:.0f} m; to zone boundaries {{{', '.join(f'{BOUNDARY_KIND.get(k,k)}: {v:.0f}' for k, v in bnd.items())}}}")
            rows.append(dict(transect=name, n=len(d), selected_nbp=a["sel"], reported_nbp=a["rep"], bp=b, bp_idx=j + 1,
                             prof_lo=pi[0], prof_hi=pi[1], boot_lo=bi[0], boot_hi=bi[1],
                             slope_change_per_km=dslope[j], fitted_change_pm100=jump[j],
                             dist_nearest_infault=dn[0], dist_trace_crossing=dtc, dist_nearest_trace_m=dtr,
                             **{f"dist_{BOUNDARY_KIND.get(k,k).replace(' ','_')}": v for k, v in bnd.items()},
                             pelt_pos=";".join(f"{x:.0f}" for x in a["pelt_pos"])))
    log.append(f"  PELT (pen={a['pelt_pen']:.3f}) change-in-mean at {[round(x) for x in a['pelt_pos']]} m, steps {[round(float(s),2) for s in a['pelt_steps']]} {unit}")
    return a, feat, rows


def main():
    LOG.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(1)
    t = tidy_salinity()
    faults = load_faults_metric()
    log, allrows, store = [], [], {}
    for name, g in t.groupby("transect", sort=False):
        g = g.sort_values("dist_m")
        a, feat, rows = report_transect(name, g.dist_m.to_numpy(), g.EC.to_numpy(), 0.1 ** 2 / 12, g, faults, rng, "uS/cm", log)
        store[name] = (g, a, feat); allrows += rows
    # chloride
    c = chloride_transect()
    c["InFault"] = "no"; c["zone"] = np.nan
    cl_line, _ = line_of(c.lat, c.lon)
    tt = t[t.InFault == "yes"]
    ck = []
    for nm, tr in (("D (S3-19Oct InFault)", "S3-19Oct"), ("E (S3-26Oct-lower InFault)", "S3-26Oct-lower")):
        sub = tt[tt.transect == tr]
        pts = points_metric(sub.lat, sub.lon)
        pos = [along_from_proj(cl_line, p, c.distance_m.max()) for p in pts]
        off = [cl_line.distance(p) for p in pts]
        ck.append((nm, pos, off))
    ac, fc, rows = report_transect("Chloride", c.distance_m.to_numpy(), c.Cl.to_numpy(), 1.25 ** 2 / 12,
                                   c.rename(columns={"distance_m": "dist_m"}), faults, rng, "mg/L", log,
                                   infault=ck[0][1] + ck[1][1])
    allrows += rows
    # Cl relative to the D / E flagged survey points
    for nm, pos, off in ck:
        log.append(f"\n{nm}: projected onto Cl path at {[round(x) for x in pos]} m along Cl transect (perpendicular offsets {[round(x) for x in off]} m)")
    cpos = pd.Series(c.distance_m.to_numpy())
    Epos = ck[1][1]
    log.append(f"Cl points downstream of first E InFault point ({min(Epos):.0f} m): {(cpos > min(Epos)).sum()} of {len(c)}; "
               f"downstream of last E InFault pt ({max(Epos):.0f} m): {(cpos > max(Epos)).sum()}; Cl transect ends at {cpos.max():.0f} m")
    for x in fc["trace_cross"]:
        log.append(f"Cl path crosses a digitized trace at {x:.0f} m; points downstream of it: {(cpos > x).sum()} of {len(c)}")
    cm = points_metric(c.lat, c.lon)
    Dpts = points_metric(tt[tt.transect == 'S3-19Oct'].lat, tt[tt.transect == 'S3-19Oct'].lon)
    u = faults.geometry.union_all()
    for i in c.index:
        if c.Cl[i] >= 36:
            dD = [cm[i].distance(p) for p in Dpts]
            log.append(f"Cl peak {c.Cl[i]} mg/L at {c.distance_m[i]:.0f} m ({c.Notes[i]}): nearest D InFault pt {min(dD):.0f} m (Euclid.), "
                       f"farthest {max(dD):.0f} m; nearest mapped trace {cm[i].distance(u):.0f} m")
    # E-end Cl
    log.append("Cl last 5 points: " + ", ".join(f"{x:.0f}m:{y}" for x, y in zip(c.distance_m[-5:], c.Cl[-5:])))
    (LOG / "changepoint.txt").write_text("\n".join(log) + "\n")
    print("\n".join(log))
    pd.DataFrame(allrows).to_csv(LOG / "changepoint_summary.csv", index=False)
    figure_sc(store)
    figure_cl(c, ac, fc, ck, faults)


# ------------------------------------------------------------------ figures
OI = dict(black="#000000", orange="#E69F00", sky="#56B4E9", green="#009E73", yellow="#F0E442",
          blue="#0072B2", verm="#D55E00", purple="#CC79A7")
TITLES = {"S1": "Site 1, 28 Sep 2018", "S2": "Site 2, 5 Oct 2018", "S3-19Oct": "Site 3, 19 Oct 2018",
          "S3-26Oct-upper": "Site 3 upper (field site 5), 26 Oct 2018", "S3-26Oct-lower": "Site 3 lower (field site 4), 26 Oct 2018"}


def draw_fit(ax, d, y, a, color=OI["verm"]):
    xs = np.linspace(d.min(), d.max(), 400)
    if a["rep"]:
        ax.plot(xs, design(xs, a["fit_bps"]) @ a["beta"], color=color, lw=2,
                ls="-" if a["sel"] > 0 else "--", zorder=3)
        for j, b in enumerate(a["fit_bps"]):
            lo, hi = a["boot_int"][j]
            ax.axvspan(lo, hi, color=OI["orange"], alpha=0.25, lw=0, zorder=1)
            ax.axvline(b, color=color, lw=1.2, zorder=2)
    else:
        ax.plot(xs, design(xs, ()) @ fit(d, y, ())[0], color=color, lw=2)
    for p in a["pelt_pos"]:
        ax.plot([p], [ax.get_ylim()[0]], marker="^", color=OI["blue"], ms=7, clip_on=False, zorder=5)


def figure_sc(store):
    plt.rcParams.update({"font.size": 9, "axes.titlesize": 10, "axes.labelsize": 9})
    fig, axes = plt.subplots(3, 2, figsize=(10, 11))
    axes = axes.ravel()
    zcol = ["#f0f0f0", "#ffffff"]
    for ax, (name, (g, a, feat)) in zip(axes, store.items()):
        d, y = g.dist_m.to_numpy(), g.EC.to_numpy()
        pad = 0.15 * (y.max() - y.min() + 1)
        ax.set_ylim(y.min() - pad, y.max() + pad * 1.6)
        ax.set_xlim(d.min() - 0.02 * d.max(), d.max() * 1.02)
        # zone shading
        z = g.zone.to_numpy()
        starts = [0] + [i + 1 for i in range(len(z) - 1) if z[i] != z[i + 1]] 
        for k, s in enumerate(starts):
            e = starts[k + 1] if k + 1 < len(starts) else len(z)
            x0 = d[s] if k == 0 else 0.5 * (d[s - 1] + d[s])
            x1 = d[e - 1] if k + 1 == len(starts) else 0.5 * (d[e - 1] + d[e])
            # zone identity: text label only (no shading), so it cannot be confused with the
            # tan breakpoint-bootstrap band; boundaries are the dashed/dotted lines below
            if isinstance(z[s], str):
                ax.text(0.5 * (x0 + x1), 0.975, f"Zone {z[s]}", transform=ax.get_xaxis_transform(), ha="center",
                        va="top", fontsize=8, color="#333333", fontweight="bold",
                        bbox=dict(fc="white", ec="0.6", lw=0.6, boxstyle="round,pad=0.2"))
        ax.scatter(d, y, s=26, c=np.where(g.InFault == "yes", OI["purple"], OI["black"]), zorder=4,
                   edgecolor="white", linewidth=0.5)
        draw_fit(ax, d, y, a)
        for k, (pos, _) in feat["boundaries"].items():
            kind = BOUNDARY_KIND.get(k, "")
            if "tributary" in kind:
                ax.axvline(pos, color=OI["green"], ls="--", lw=1.6, zorder=2)
            else:
                ax.axvline(pos, color="#888888", ls=":", lw=1.2, zorder=2)
            ax.text(pos, 0.86, kind.split()[-1], transform=ax.get_xaxis_transform(), fontsize=8, ha="center",
                    color=OI["green"] if "tributary" in kind else "#555555", fontweight="bold",
                    bbox=dict(fc="white", ec="none", pad=0.5, alpha=0.8))
        for x in feat["trace_cross"]:
            ax.plot([x], [ax.get_ylim()[0]], marker="X", color="#bbbbbb", mec="#666666", mew=0.5, ms=6, clip_on=False, zorder=6)
        ax.set_title(TITLES[name] + f"  (n={len(d)}; BIC: {a['sel']} bp)", loc="left")
        ax.set_xlabel("Distance downstream along channel (m)")
        ax.set_ylabel("Specific conductance (µS/cm)")
    ax = axes[-1]; ax.axis("off")
    from matplotlib.lines import Line2D
    from matplotlib.patches import Patch
    h = [Line2D([], [], marker="o", ls="", color=OI["black"], label="SC measurement"),
         Line2D([], [], marker="o", ls="", color=OI["purple"], label="Survey point just downstream of a mapped fault"),
         Line2D([], [], color=OI["verm"], lw=2, label="Segmented fit (BIC-selected)"),
         Line2D([], [], color=OI["verm"], lw=2, ls="--", label="Best 1-breakpoint fit (not BIC-selected)"),
         Patch(color=OI["orange"], alpha=0.35, label="Breakpoint 95% bootstrap interval (tan band)"),
         Line2D([], [], color="none", label="Zone labels in boxes; zone ends at boundary lines"),
         Line2D([], [], marker="^", ls="", color=OI["blue"], label="PELT change-in-mean"),
         Line2D([], [], color=OI["green"], ls="--", lw=1.6, label="Tributary junction (zone boundary)"),
         Line2D([], [], color="#888888", ls=":", lw=1.2, label="Zone boundary (field-interpreted fault; contrasts B, D, E)"),
         Line2D([], [], marker="X", ls="", color="#bbbbbb", mec="#666666", ms=6, label="Digitized county-map fault trace crosses survey line (approximate)")]
    ax.legend(handles=h, loc="center left", frameon=False, fontsize=9)
    fig.tight_layout()
    fig.savefig(FIG / "rev_changepoint_sc.png", dpi=300)
    plt.close(fig)


def figure_cl(c, a, fc, ck, faults):
    fig, ax = plt.subplots(figsize=(9, 5.0))
    d, y = c.distance_m.to_numpy(), c.Cl.to_numpy()
    ax.set_ylim(0, y.max() * 1.25); ax.set_xlim(-40, d.max() + 60)
    ax.scatter(d, y, s=34, c=OI["black"], zorder=4, edgecolor="white", linewidth=0.5)
    draw_fit(ax, d, y, a)
    ax.set_ylim(0, y.max() * 1.25)
    # positions of the D / E flagged survey points projected onto the Cl path
    for (nm, pos, off), col, lab in zip(ck, (OI["purple"], OI["purple"]), ("D", "E")):
        for i, x in enumerate(pos):
            ax.axvline(x, color=col, lw=1.2, ls="-", alpha=0.7, zorder=2)
        ax.text(np.mean(pos), 0.95, f"Contrast {lab}\nflagged points", transform=ax.get_xaxis_transform(), ha="center", va="top",
                fontsize=8, color=col, bbox=dict(fc="white", ec="none", alpha=0.8, pad=1))
    for x in fc["trace_cross"]:
        ax.plot([x], [0], marker="X", color="#bbbbbb", mec="#666666", mew=0.5, ms=7, clip_on=False, zorder=6)
    for x in fc["trace_cross"]:
        ax.annotate("County-map trace\ncrosses path (approx.)", (x, 0), xytext=(x - 120, 8.5), fontsize=8, ha="right",
                    color="#666666", arrowprops=dict(arrowstyle="-", color="#999999", lw=0.8))
    u = faults.geometry.union_all()
    cm = points_metric(c.lat, c.lon)
    for i in (4, 8):  # the two "possible fault?" peaks
        ax.annotate(f"{y[i]:.0f} mg/L\n{cm[i].distance(u):.0f} m from\nnearest trace", (d[i], y[i]), xytext=(d[i] + 60, y[i] + 4),
                    fontsize=8, color="#333333")
    ax.set_xlabel("Distance along transect from Z (m)"); ax.set_ylabel("Chloride (mg/L)")
    ax.set_title("Chloride transect, 20 Jul 2020 (n=%d; BIC: %d bp)" % (len(d), a["sel"]), loc="left")
    from matplotlib.lines import Line2D
    from matplotlib.patches import Patch
    h = [Line2D([], [], marker="o", ls="", color="k", label="Chloride sample"),
         Line2D([], [], color=OI["verm"], lw=2, ls="-" if a["sel"] else "--", label="Segmented fit" if a["sel"] else "Best 1-bp fit (not BIC-selected)"),
         Patch(color=OI["orange"], alpha=0.35, label="Breakpoint 95% bootstrap"),
         Line2D([], [], marker="^", ls="", color=OI["blue"], label="PELT change-in-mean"),
         Line2D([], [], color=OI["purple"], lw=1.2, label="Survey points flagged as just downstream of the fault (SC survey), projected on path"),
         ]
    if fc["trace_cross"]:
        h.append(Line2D([], [], marker="X", ls="", color="#bbbbbb", mec="#666666", ms=7, label="Digitized county-map fault trace crosses survey line (approximate)"))
    ax.legend(handles=h, loc="upper center", fontsize=8, frameon=False, ncol=3, bbox_to_anchor=(0.5, -0.17))
    fig.tight_layout(); fig.savefig(FIG / "rev_changepoint_cl.png", dpi=300); plt.close(fig)


if __name__ == "__main__":
    main()
