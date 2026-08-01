"""Regenerate the data-driven figures from source data.

  * Figure 5 -- longitudinal chloride transect (Z -> Z'), with the Kelly et al.
    2019 long-term sampling point marked.

Run:  .venv/bin/python src/figures.py
"""

from pathlib import Path
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from wappingers import load_chloride

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


if __name__ == "__main__":
    chloride_figure()
