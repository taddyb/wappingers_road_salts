"""Regenerate the data-driven figures from source data.

  * Figure 5 -- longitudinal chloride transect (Z -> Z'), with the Kelly et al.
    2019 long-term sampling point marked.
  * Zone EC figure -- box/strip plot of specific conductance by zone with the
    fault vs tributary boundaries and Welch significance, a new figure that
    makes the corrected Table 1 visual.

Run:  .venv/bin/python src/figures.py
"""

from pathlib import Path
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from wappingers import load_salinity, load_chloride, zones, CONTRASTS
from stats import analyze

FIG = Path(__file__).resolve().parent.parent / "figures"


def chloride_figure():
    d = load_chloride()
    notes = d["Notes"].astype(str).str.lower()
    # The final "side tributary" sample is off the Z->Z' main-stem transect;
    # the original Figure 5 excludes it. Keep only the main transect.
    d = d[~notes.str.contains("tributary")].reset_index(drop=True)
    notes = d["Notes"].astype(str).str.lower()
    # The red star is the Kelly et al. 2019 long-term monitoring point, flagged
    # in the data's own Notes column.
    star_i = int(notes.str.contains("long-term").idxmax())

    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    ax.plot(d["distance_m"], d["Cl"], color="black", lw=1.6)
    ax.plot(d["distance_m"].iloc[star_i], d["Cl"].iloc[star_i],
            marker="*", markersize=18, markerfacecolor="none",
            markeredgecolor="red", markeredgewidth=1.6, zorder=5)
    ax.annotate("Z", (d["distance_m"].iloc[0], d["Cl"].iloc[0]),
                textcoords="offset points", xytext=(-4, 6), fontsize=12)
    ax.annotate("Z'", (d["distance_m"].iloc[-1], d["Cl"].iloc[-1]),
                textcoords="offset points", xytext=(2, -10), fontsize=12)
    ax.set_xlabel("Distance (m)")
    ax.set_ylabel(r"Cl (mg L$^{-1}$)")
    ax.grid(True, ls="--", alpha=0.4)
    ax.margins(x=0.02)
    fig.tight_layout()
    out = FIG / "chloride.png"
    fig.savefig(out, dpi=200)
    plt.close(fig)
    print(f"wrote {out.relative_to(FIG.parent)}")


def zone_ec_figure():
    df = load_salinity()
    z = zones(df)
    order = ["1-1", "1-2", "2-1", "2-2", "3-1", "3-2", "3-3", "3-4"]
    rows = {r["contrast"]: r for r in analyze()}

    fig, ax = plt.subplots(figsize=(7.2, 4.0))
    for i, zl in enumerate(order):
        vals = z[zl]
        ax.scatter(np.full_like(vals, i, dtype=float)
                   + np.random.default_rng(i).uniform(-0.08, 0.08, len(vals)),
                   vals, s=18, color="0.35", zorder=3)
        ax.hlines(vals.mean(), i - 0.25, i + 0.25, color="black", lw=2, zorder=4)
    ax.set_xticks(range(len(order)))
    ax.set_xticklabels([f"Zone {z}" for z in order], rotation=30, ha="right")
    ax.set_ylabel(r"Specific conductance ($\mu$S cm$^{-1}$)")

    # Bracket each contrast between its two zones, annotate boundary + p.
    ymax = max(z[zl].max() for zl in order)
    for name, a, b, kind in CONTRASTS:
        r = rows[name]
        i, j = order.index(a), order.index(b)
        y = ymax + 6 + 10 * (kind == "fault")
        color = "firebrick" if kind == "fault" else "steelblue"
        ax.plot([i, i, j, j], [y - 2, y, y, y - 2], color=color, lw=1.3)
        sig = "*" if r["welch_p"] < 0.05 else "n.s."
        ax.text((i + j) / 2, y + 1,
                f"{name} ({kind}) {sig}", ha="center", va="bottom",
                fontsize=8, color=color)
    ax.grid(True, axis="y", ls="--", alpha=0.3)
    fig.tight_layout()
    out = FIG / "zone_ec.png"
    fig.savefig(out, dpi=200)
    plt.close(fig)
    print(f"wrote {out.relative_to(FIG.parent)}")


if __name__ == "__main__":
    chloride_figure()
    zone_ec_figure()
