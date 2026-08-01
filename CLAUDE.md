# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

The LaTeX manuscript for **"Evidence of fault zone transport of road-salt contaminated groundwater from highways to streams"** — a study of Wappingers Creek (Dutchess County, NY) showing that mapped high-angle geologic fault zones spatially coincide with statistically significant increases in stream specific conductance, implicating faults as preferential conduits for road-salt-contaminated groundwater.

This is an Overleaf-synced git repo based on the kourgeorge/arxiv-style template. The author has LibreOffice only (no MS Word), so **LaTeX/Overleaf is the sole collaboration format**. The manuscript has been converted from the Word source into `main.tex` (+ `references.bib`, `figures/`); the next phase is revising it per editor requirements.

## Source-of-truth documents (outside this repo)

- `~/papers/pollution_study_manuscript_bindas_updates.docx` — the canonical manuscript content (title, abstract, 4 sections, 5 figures, Table 1, 27 numbered references). Read it via `pandoc <file>.docx -t markdown --extract-media=<dir>`. Treat as read-only input.
- `~/papers/revision_outline.md` — the working revision plan for journal submission (ID: 101225). Editor requires **≥5,000 main-body words** (currently ~2,630) and **≥30% references from 2022–2026** (currently 1/27). Contains per-section word budgets, an 11-item recent-citation ledger with DOIs, and a quick-fixes checklist (empty Equations 1–2, corrupted sentence in §3.1, duplicated "[27] [27]"). Consult it before any content edits.
- `~/papers/manuscript_tex/main.tex` + `media/` — a raw, unstyled pandoc dump of the docx (pandoc preamble, no bibliography markup). Useful as a text/equation reference; do not build on it. The extracted `media/image1-5.png` are the docx-embedded (lower-quality) figures.
- `~/papers/academic-research-skills/` — the ARS skill suite (academic-paper, academic-paper-reviewer, deep-research, academic-pipeline). Most relevant modes for this project: `format-convert` (docx→LaTeX), `revision`, `citation-check`, `lit-review`. Invoke via the installed `academic-paper` skill or `/ars-*` commands.

## Analysis pipeline (`src/`, this repo)

The statistics and figures are regenerated from source data by a Python
pipeline in `src/` (see `src/README.md`). Set up with a venv at `.venv/`
(gitignored) and the packages listed in `src/README.md`, then:

- `.venv/bin/python src/stats.py` → corrected Table 1 (`figures/table1_corrected.tex`, `\input` by main.tex)
- `.venv/bin/python src/figures.py` → `figures/chloride.png` (Fig 5) + `figures/zone_ec.png` (a stats figure, not yet used in the paper)
- `.venv/bin/python src/maps.py` → `figures/overview.png` + `figures/site{1,2,3}.png` (Figs 1–4; fetches OSM basemap tiles, needs internet)

Data lives in `data/` (`salinity-dataset.xlsx`, `chloride-dataset.xlsx`), copied
from the WappingersCreekResearch repo. `src/wappingers.py` is the shared loader
and defines the zone row-slices and the five upstream/downstream contrasts.

**Key correction:** the original R `statistics.R` used `t = (x̄₂−x̄₁)/(s₂/√n₂)`,
a one-sample-style statistic that inflated t. `src/stats.py` replaces it with a
two-sample **Welch** t-test on raw µS/cm (matching what the Methods prose
claims), plus a Mann-Whitney check, and fixes a row-40 double-count between
Zones 3-3/3-4. Corrected result: only the two clean fault crossings (Contrasts
B, E) are significant (p<0.001); D, A, C are not. This matches the abstract's
"two of three" framing; the paper's conclusion is unchanged. `stats.py` prints
a `pub. t` column that exactly reproduces the original published Table 1 for
an auditable before/after.

**Site-map caveat:** points, colors, zone boxes, and contrast arrows are
data-derived, but the fault-trace band is approximated from the `InFault`
points and is schematic — the real traces came from the Budnik et al. 2010
geologic map and should be digitized before final submission.

## Research code, data, and figures

https://github.com/taddyb/WappingersCreekResearch (clone as needed) holds everything behind the figures/statistics, and is cited in the paper's Data Availability statement:

- `data/salinity.csv`, `data/salinity-dataset.xlsx` — Oct 2018 EC survey (Date, Site, GPS, Lat/Lon, EC µS/cm, Temp, field notes), split by site number.
- `scripts/statistics.R` — per-site mean/sd normalization (`scale()`) of EC, then t/z-tests across zone contrasts → Table 1.
- `scripts/makeGraphs.R` — ggmap/ggplot2 site maps and plots; requires a Google Maps API key read from `config.yml`.
- `manuscriptFigures/` — earlier figure variants (`BindasFigure1-4.png`, site/zone layouts). **Note:** the docx-embedded images are the *final annotated versions* (updated labels, red star + Z/Z′ on the chloride plot) and were extracted losslessly into this repo's `figures/`; the GitHub PNGs are older drafts. The final annotation step was done in the `*Template.pptx` files.
- (A Google Maps API key once committed in that repo's `config.yml` was revoked and removed in Aug 2026; `makeGraphs.R` needs a user-supplied key to re-render maps.)

Paper structure facts needed to interpret code and figures together: 3 study sites on Wappingers Creek; each site is divided into zones (1-1/1-2; 2-1/2-2; 3-1…3-4); zone boundaries are fault crossings or tributary junctions; "Contrasts" A–E are upstream/downstream zone comparisons tested with Student's t-tests on normalized EC (Table 1). Figures: 1 = regional overview, 2–4 = Sites 1–3 maps, 5 = chloride transect (Z→Z′, Site 3).

## Building the LaTeX

- Local toolchain: **tectonic only** (`~/.cargo/bin/tectonic`); no pdflatex/latexmk/bibtex installed. Build with `tectonic main.tex` (tectonic runs the bibliography passes automatically and fetches packages on demand).
- Overleaf compiles the repo directly; keep the repo self-contained (all `.sty`, figures, and `.bib` committed) so both toolchains work.
- Template usage (from the arxiv-style README): `\documentclass{article}` + `\usepackage{arxiv}`; the style already loads `geometry` and `fancyhdr` — do not re-import them. Citations via `natbib` with `\bibliographystyle{unsrtnat}` and `references.bib`; the paper's existing references use numeric `[n]` order-of-appearance style, which `unsrtnat` matches.
- For an eventual arXiv submission, the generated `.bbl` must be inlined into the `.tex` (arXiv doesn't run bibtex); see README.md steps.

## Conventions

- `main.tex` is the working document; `template.tex` is the untouched style example (its sample bib entries were replaced, so it no longer builds standalone — that's fine).
- Citations are numeric via `\usepackage[numbers]{natbib}` + `unsrtnat`; `references.bib` is ordered so numbering matches the docx's [1]–[27]. Author names in the bib are kept exactly as the docx prints them (initials, `and others` for "et al.") — don't expand names without verifying against the actual paper.
- Known source-document defects (garbled Introduction opening, corrupted §3.1 sentence, duplicated [27] citation, terse equations) are marked with `% TODO (revision outline)` comments in `main.tex` — they are deliberate faithful-conversion artifacts to be fixed in the revision phase, not conversion bugs.
- The author block in `main.tex` is a placeholder (docx had none): second-author email, departments, and ORCIDs still need filling in.
- All 27 existing references must land in `references.bib`; new citations from the revision outline's ledger must be **verified against the actual paper (open the DOI, read it) before insertion** — the outline explicitly warns these were surfaced by web search.
- Content changes should trace to either the docx or the revision outline; don't invent new data, results, or numbers — the expansion is context/framing/synthesis only.
