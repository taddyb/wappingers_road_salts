# Analysis results for the revision (WP0)

All numbers below were produced by the scripts in `src/` (console logs saved in `docs/logs/`).
Decision D0(a): zones are compared only within a single survey day. SC = specific conductance (µS/cm).
Δ = downstream − upstream. CI = Welch 95% CI of Δ. "n_eff" = autocorrelation-adjusted n (rule in `src/within_day.py` docstring).

Scripts: `src/within_day.py` (W), `src/changepoint.py` (C), `src/geo_context.py` (G). Log files: `docs/logs/{within_day,changepoint,geo_context}.txt`, `docs/logs/changepoint_summary.csv`.

## Survey structure (verified)

| Transect | Field site | Date | n | Length (m) | Orientation rule |
|---|---|---|---|---|---|
| S1 | 1 | 28 Sep 2018 | 9 | 677 | field order = downstream (zone 1-1 before 1-2) |
| S2 | 2 | 5 Oct 2018 | 18 | 7066 | field order = downstream (zone 2-1 before 2-2) |
| S3-19Oct | 3 | 19 Oct 2018 | 20 | 2130 | field order = downstream; last point is 17.6 m from site 4 row 1 |
| S3-26Oct-upper | 5 | 26 Oct 2018 | 14 | 1077 | **reversed** (site-5 row 1 sits beside site-3 gps 8, row 11 beside gps 1, i.e. site 5 was walked upstream) |
| S3-26Oct-lower | 4 | 26 Oct 2018 | 12 | 1299 | field order = downstream (continues the site-3 end) |

Field sites 4 and 5 are 1139 m apart (site-5 downstream end to site-4 start), so they are two separate transects, not one.
Zone membership is as in `wappingers.zones()`; every one of the 73 points falls in a zone (site 4 row 12 is in zone 3-4; the plan's "row 46" is the same point). Distances are haversine sums between consecutive GPS fixes (W, `wappingers.tidy_salinity`). Site 1 GPS points 1 and 2 are 13 m apart (field note: GPS did not find point 2 correctly); S1 distances in that stretch are unreliable.

## What changed vs. the submitted Table 1

| Contrast | Submitted (pooled days) | Within-day (this analysis) |
|---|---|---|
| A tributary | Δ −0.45, t −1.35, p 0.264 | unchanged (single day, 28 Sep): same numbers |
| B fault | +4.3, t 5.63, p<0.001 | unchanged (single day, 5 Oct) |
| C tributary | x̄ 359.8→350.6 (Δ −9.2), p 0.248 | 19 Oct: Δ −3.8, p 0.093; 26 Oct: Δ −5.6, p<0.001 |
| D fault | x̄ 350.6→342.4 (Δ −8.2), p 0.286 | 19 Oct: Δ −2.8, p 0.140 (26 Oct not testable: zones 3-2 and 3-3 are on different transects) |
| E fault | x̄ 342.4→360.4 (Δ +18.0), t 5.83, p<0.001 | 26 Oct: **Δ +1.6**, t 1.96, p 0.090 (not significant) |

The submitted E "step" was the 19→26 Oct day offset (see below).

## Within-zone, within-day SC statistics (R1.6, R1.7, R1.11, R2.2b/R2.3) — W

| Zone | Date | n | mean | SD | min–max |
|---|---|---|---|---|---|
| 1-1 | 28 Sep | 4 | 259.85 | 0.66 | 258.9–260.4 |
| 1-2 | 28 Sep | 5 | 259.40 | 0.12 | 259.2–259.5 |
| 2-1 | 5 Oct | 10 | 308.79 | 1.13 | 307.3–311.1 |
| 2-2 | 5 Oct | 8 | 313.08 | 1.90 | 310.8–316.0 |
| 3-1 | 19 Oct | 6 | 340.08 | 0.43 | 339.4–340.5 |
| 3-1 | 26 Oct | 11 | 370.54 | 2.64 | 367.4–375.2 |
| 3-2 | 19 Oct | 3 | 336.27 | 2.20 | 334.8–338.8 |
| 3-2 | 26 Oct | 3 | 364.93 | 1.11 | 363.9–366.1 |
| 3-3 | 19 Oct | 11 | 333.45 | 1.93 | 331.4–336.9 |
| 3-3 | 26 Oct | 6 | 358.82 | 1.76 | 355.5–360.2 |
| 3-4 | 26 Oct | 6 | 360.37 | 0.80 | 359.3–361.5 |

R1.7: the submitted Zone 3-2 SD (12.6–15.8 across Site 3 zones) is the day mixing; the within-day SDs are 0.4–2.6 µS/cm. **R1.11 (Site 2):** within-zone SD 1.13 (2-1) and 1.90 (2-2) µS/cm, vs. Δ = +4.3. Temperature is not different between the two zone means by more than 0.4 °C on 5 Oct (15.4–15.8 °C) — note SC along S2 drifts gradually (see change-point).

## Within-day contrasts (R1.6, R1.5(3), R1.10, R2.5, R2.6, R2.15) — W, files `figures/table1_revised.tex`, `figures/table1_revised_support.tex`

| C | Boundary | Date | n1,n2 | mean±SD up | mean±SD down | Δ [95% CI] | Welch t (df) | p | MW U | MW p |
|---|---|---|---|---|---|---|---|---|---|---|
| A | tributary | 28 Sep | 4,5 | 259.85±0.66 | 259.40±0.12 | −0.45 [−1.48, +0.58] | −1.35 (3.2) | 0.264 | 5 | 0.266 |
| B | fault | 5 Oct | 10,8 | 308.79±1.13 | 313.08±1.90 | +4.29 [+2.61, +5.96] | 5.63 (10.8) | 0.0002 | 79 | 0.0006 |
| C | tributary | 19 Oct | 6,3 | 340.08±0.43 | 336.27±2.20 | −3.82 [−9.15, +1.52] | −2.97 (2.1) | 0.093 | 0 | 0.028 |
| C | tributary | 26 Oct | 11,3 | 370.54±2.64 | 364.93±1.11 | −5.60 [−7.92, −3.28] | −5.48 (8.8) | 0.0004 | 0 | 0.012 |
| D | fault | 19 Oct | 3,11 | 336.27±2.20 | 333.45±1.93 | −2.82 [−7.36, +1.72] | −2.02 (2.9) | 0.140 | 6 | 0.119 |
| E | fault | 26 Oct | 6,6 | 358.82±1.76 | 360.37±0.80 | +1.55 [−0.32, +3.42] | 1.96 (7.0) | 0.090 | 29.5 | 0.076 |

(U is for the downstream sample; n = 3 or 4 in one zone for A, C, D: tests there have very little power — the minimum attainable exact Mann–Whitney p for 6 vs 3 is ≈0.024, and scipy's reported 0.028 uses the asymptotic approximation because of ties.) A Welch p of 0.093 with n=3 should not be called a trend.
Within-day reproduction of the plan's §0 table: all four rows (C 19/26 Oct, D 19 Oct, E 26 Oct) match to the printed precision.

### Autocorrelation and n_eff (R1.8) — W

Lag-1 autocorrelation of SC along each transect (raw series, trend included): S1 0.03, S2 0.78, S3-19Oct 0.83, S3-26Oct-upper 0.69, S3-26Oct-lower 0.30. These high raw values mostly reflect smooth along-channel trends, i.e. the SC fields are strongly spatially structured.
For the zone contrasts, ρ is the lag-1 autocorrelation of residuals from the two zone means (pooled along the transect); negative ρ is set to 0.

| C | Date | ρ (resid.) | n_eff up / down | Welch p | p with n_eff |
|---|---|---|---|---|---|
| A | 28 Sep | −0.27 | 4.0 / 5.0 | 0.264 | 0.264 |
| B | 5 Oct | 0.37 | 4.6 / 3.7 | 0.0002 | 0.017 |
| C | 19 Oct | −0.35 | 6.0 / 3.0 | 0.093 | 0.093 |
| C | 26 Oct | 0.54 | 3.2 / 2.0 | 0.0004 | 0.041 |
| D | 19 Oct | 0.35 | 2.0 / 5.3 | 0.140 | 0.279 |
| E | 26 Oct | 0.30 | 3.2 / 3.2 | 0.090 | 0.243 |

Take-away: B remains significant after adjustment (p 0.017), but by orders of magnitude less than the nominal p. ρ from 6–14 residuals (and 3 for some zones) is poorly determined; treat n_eff as a sensitivity check.

## Change-point / segmented regression (R1.5(3), R2.6) — C

Method: continuous piecewise-linear regression, 0/1/2 breakpoints, ≥3 points per segment, BIC (k = 2+2·nbp), RSS/n floored at resolution²/12 (0.1 µS/cm; 1.25 mg/L for Cl); breakpoint intervals: profile-RSS (Δχ²₁ = 3.84) and 500-rep residual bootstrap, both restricted to the grid (breakpoints can't lie within 3 points of an end). PELT: l2 cost, min_size 3, penalty 2σ̂²ln n with σ̂² from first differences.

| Transect (n) | BIC (0 / 1 / 2 bp) | Selected | Breakpoint (m) [bootstrap 95%; profile 95%] | Slope change | PELT change-in-mean (m; step) |
|---|---|---|---|---|---|
| S1 (9) | −11.5 / −9.6 / −5.4 | **0** (best 1-bp at 226 m not supported) | 226 [202, 591; same] | −4.1 µS/cm/km | none |
| S2 (18) | 0.5 / **−12.6** / −9.9 | **1** | 2355 [1327, 3384; 2004, 3207] | +1.5 µS/cm/km (slope 0.1 → 1.6) | 2617 (+1.5), 3588 (+2.3), 5948 (+3.3) |
| S3-19Oct (20) | **2.6** / 2.6 / 7.0 | **0** (1-bp tie, ΔBIC 0.03) | best 1-bp 1707 [227, 1873; 619, 1873] | +5.1 | 630 (−4.1), 1249 (−3.4) |
| S3-26Oct-upper (14) | 0.6 / −3.8 / **−4.1** | **2** (ΔBIC vs 1-bp only 0.3) | 300 [177, 335; 247, 353]; 459 [406, 830; 406, 794] | +21.2; −10.9 | 204 (−4.8), 545 (−1.6), 773 (−3.2) |
| S3-26Oct-lower (12) | 8.5 / **−1.7** / 0.5 | **1** | 194 [194, 300; 194, 304] (pinned at the min-segment limit: 3rd point at 188 m) | −21.7 (slope +21.9 → +0.2 µS/cm/km) | 266 (+2.4) |
| Chloride (18) | 82.6 / **66.5** / 68.5 | **1** | 467 [308, 800; 400, 567] | −68.2 mg/L/km (slope +53 → −15) | 384 (+16.6), 1021 (−18.6) mg/L |

Distances (along-channel unless noted) from each reported breakpoint to features:

| Transect | Breakpoint (m) | Nearest InFault pt | Polyline×trace crossing | Straight-line to nearest trace | Junction / boundary |
|---|---|---|---|---|---|
| S1 (not selected) | 226 | 203 m (InFault 428–677 m) | 153 m (crossing at 379) | 137 m | tributary A (363 m): 138 m |
| S2 | 2355 | 1477 m (at 878) | 1310 m (crossings at 1046, 5763) | 389 m | fault B boundary (3993 m): 1638 m |
| S3-19Oct (not selected) | 1707 | 532 m (at 1175) | 948 m (crossing at 759) | 237 m | tributary C (419): 1288; fault D (922): 785 |
| S3-26Oct-upper bp1 | 300 | no InFault pts | none (path does not cross a trace) | 562 m | tributary C (773): 473 |
| S3-26Oct-upper bp2 | 459 | – | – | 453 m | tributary C: 314 |
| S3-26Oct-lower | 194 | 611 m (at 804) | 330 m (crossing at 523) | 123 m | fault E boundary (716): 522 |
| Chloride | 467 | 125 m (D pts projected at 126, 222, 342 m) | 1342 m (crossing at 1809 m) | 303 m | – |

Reading: no SC breakpoint coincides with a mapped fault crossing or an InFault point on any transect; the only well-supported SC breakpoints (S3-26Oct-lower at 194 m, S2 at 2355 m) are 500–1600 m from the E and B boundaries. The S3-26Oct-lower rise (355.5→359.7 µS/cm over the first 190 m) is the same feature as §0b item 2 (onset ~600 m upstream of the trace and InFault points at 804/930 m). The breakpoints on S3-26Oct-upper (300, 459 m) are near neither a tributary nor a fault; the tributary-C decrease is a gradual downward drift (≈ −10 to −20 µS/cm/km upstream, ≈ −10 downstream), not a step. S1 and S3-19Oct are best described as no breakpoint (S1 with n = 9, 0 bp is selected; 3 points per segment leaves almost no resolving power).
Chloride: breakpoint at 467 m [bootstrap 308–800 m], i.e. at the 50 mg/L peak (474 m), 125 m from the nearest D InFault point and ~300 m from the nearest mapped trace. PELT puts mean shifts at 384 (+16.6 mg/L) and 1021 m (−18.6 mg/L). The bootstrap interval covers the D InFault points' range only at its lower end.
The InFault-vs-breakpoint comparison for the "polyline×trace crossing" uses straight chords between GPS fixes; for sparse fixes (e.g. 318 m between S3-19Oct points 7 and 8) this is a coarse position.

## Day offset (R1.7, R2.3e, Fig. 4) — W

Each 19 Oct point → nearest 26 Oct point within 120 m (n = 11): offsets 23.5–29.7 µS/cm (mean 27.8, SD 2.2), pair distances 15–108 m, temperature 0.6–1.9 °C lower on 26 Oct.
Site-3 vs site-5 pairs (19 Oct gps 1–8 → site-5 nearest, ≤50 m, n = 8): +27.3 to +29.7 µS/cm (mean 28.8). Reverse direction (each site-5 point → nearest 19 Oct point; 10 pairs ≤50 m): +27.3 to +29.7. Seam (site 3 last vs site 4 first): 17.6 m apart, 332.0 vs 355.5, **+23.5**. Site-5 end to site-4 start: 1139 m.
§0b item 1 reproduced; see Discrepancies. The offset varies between 23.5 and 29.7 µS/cm (≈6 µS/cm), larger than B (+4.3) and E (+1.6).

## Chloride transect specifics (R2.7) — C

- 18 transect points (side-tributary sample excluded), 0–2351 m from Z.
- Projected onto the Cl path, the D InFault points (S3-19Oct gps 10–12) fall at 126, 222, 342 m (perpendicular offsets 4–15 m); the E InFault points (S3-26Oct-lower gps 7–8) at 2087 and 2205 m (17–23 m offsets).
- Points downstream of the first E InFault point (2087 m): **2 of 18** (2238 m: 13.75, 2351 m: 15.0 mg/L). Points downstream of the E trace crossing (path crosses a digitized trace at 1809 m): **4 of 18** (1960–2351 m). The trace crosses the path ~280 m upstream of the InFault points.
- Cl peaks (mg/L, position, nearest D InFault point by straight line, nearest mapped trace): 50.0 at 474 m, 133 m (farthest D pt 333 m), 307 m; 36.25 at 690 m, 315 m, 391 m; 40.0 at 959 m, 468 m (farthest 664 m), 293 m. Last five Cl values: 15.0, 17.5, 15.0, 13.75, 15.0. No two-sample test attempted (≤4 points downstream of E).

## Road distance (R1.12, R2.9) — G (also W)

Definition: "major road" = TIGER MTFCC S1100 (primary; 3 segments: I-84 and Newburgh-Beacon Bridge) + S1200 (secondary; 259 segments: US 9, US 44, NY 82, NY 55, NY 376 …), 262 segments total. US 44 and NY 82 are in S1200. **Taconic State Parkway is coded S1400 (local road) in TIGER and is therefore excluded**; adding it by name changes no transect median (nearest roads are already closer).
Median distance to nearest major road, per zone and day (m; [min–max]):

| Zone | Date | n | median | range |
|---|---|---|---|---|
| 1-1 | 28 Sep | 4 | 927 | 852–949 |
| 1-2 | 28 Sep | 5 | 751 | 735–762 |
| 2-1 | 5 Oct | 10 | 335 | 39–711 |
| 2-2 | 5 Oct | 8 | 726 | 466–927 |
| 3-1 | 19 Oct | 6 | 304 | 248–432 |
| 3-1 | 26 Oct | 11 | 245 | 177–439 |
| 3-2 | 19 Oct | 3 | 425 | 370–443 |
| 3-2 | 26 Oct | 3 | 414 | 391–445 |
| 3-3 | 19 Oct | 11 | 409 | 316–535 |
| 3-3 | 26 Oct | 6 | 312 | 283–350 |
| 3-4 | 26 Oct | 6 | 368 | 286–390 |

Per-transect medians: S1 762, S2 571, S3-19Oct 397, S3-26Oct-upper 296, S3-26Oct-lower 338. Nearest major road: S1 Covey Ln (all 9 points; an S1200 road, minor name), S2 US 44 (16 of 18) and Manchester Rd (2), S3 US 44 (all 19 Oct, all 26 Oct upper, 7 of 12 lower) and NY 82 (5 of 12 lower). InFault points: median 751 (S1), 291 (S2), 409 (S3-19Oct), 326 (S3-26Oct-lower).
Descriptive observations (no inference): the B contrast goes from closer to farther from a major road (335 → 726 m), i.e. SC rises while distance from the nearest major road increases; at Site 3 the zones lie 245–425 m from US 44 with no monotone relation to the zone SC pattern. Zone 2-1 contains a point 39 m from a major road.

## Fault band basis (R2.6, R2.13) — G

Distance from each of the 16 InFault points to the nearest digitized Budnik et al. (2010) trace: min 5 m, **median 75 m**, max 279.5 m. By transect: S1 (5 pts) median 50, max 64; S2 (6) median 68, max 170; S3-19Oct (3) median 172, max 240; S3-26Oct-lower (2) median 223, max 279. By paper site: Site 1 40–64 (median 50); Site 2 5–170 (68); Site 3 111–279 (172). **A ±300 m band is confirmed** (max 280 m leaves ≈20 m of margin; the largest offsets are all on Site 3). The plan's "median ~90 m" is not reproduced (75 m).

## Raw data appendix (D5, R2.2c) — W

`figures/appendix_data.tex` (73 rows, longtable; needs `\usepackage{longtable}` and booktabs) and `data/salinity_tidy.csv` (columns paper_site, field_site, field_row, date, transect, dist_m, lat, lon, EC, Temp, zone, InFault). `data/salinity_tidy_with_roads.csv` adds road_m.

## Discrepancies vs `docs/revision_plan.md` §0/§0b

1. §0 within-day table: reproduced exactly.
2. §0b(1) "Nine point pairs 15–50 m apart differ by +27.3 to +29.7": I get 8 forward pairs (19 Oct → nearest site-5 point, ≤50 m; +27.3 to +29.7) or 10 reverse pairs (site-5 → nearest 19 Oct, ≤50 m; +27.3 to +29.7); the range matches, "nine" does not. Including the two seam-side pairs (offsets +23.5/+23.7 to site 4) the overall range is 23.5–29.7. Seam 18 m / +23.5 reproduced.
3. §0b(2) reproduced: S3-26Oct-lower rises 355.5→359.7 over the first 188 m then ~360 through InFault points at 804–930 m. The "~600 m upstream of the trace" is the distance to the InFault points (611 m); the digitized trace crosses the transect chord at 523 m, only 330 m from the breakpoint (194 m), and the nearest-trace distance from the breakpoint is 123 m.
4. §0b(3) reproduced: Cl peaks 50 (474 m), 40 (959 m); nearest trace 307/293 m; ~133–468 m from D InFault points (to nearest D point: 133 and 468 m); "side tributary" 6.25 excluded; Cl near E 13.75–17.5 and falling.
5. InFault–trace median 75 m, not ~90 m (range 5–280 confirmed).
6. Row labels in the plan ("rows 14–33") are the 0-based indices in the concatenated Site-3 frame, not field row numbers.

## Surprises / things the author should know

- **No SC breakpoint lies at a mapped fault crossing or InFault point on any transect.** Within-day, only B is a clear fault-associated SC rise; D is a small non-significant decrease (19 Oct) and E a small non-significant rise.
- **S2 SC increases mostly as a gradual downstream ramp** (slope 0.1 → 1.6 µS/cm/km, bp at 2355 m ±1000 m) and the B zone boundary is at 3993 m — the B step is partly a trend. A single-breakpoint model is selected; the B contrast is thus consistent with a diffuse increase, not an abrupt fault step. PELT puts three small mean shifts (+1.5, +2.3, +3.3) between 2.6 and 5.9 km.
- **Zone 3-2 on 26 Oct and D:** zones 3-2 (upper transect) and 3-3 (lower transect) are on different 26 Oct transects 1.1 km apart, so D cannot be tested on 26 Oct. The 26 Oct "D" difference (−6.1) would be an artefact of that gap.
- **Contrast C is significant on 26 Oct (Δ −5.6) but its n = 3 downstream zone, and S3-26Oct-upper shows a 2-breakpoint solution only marginally preferred (ΔBIC 0.3)**; the breakpoints are not at the tributary (474 and 314 m away).
- **Chloride breakpoint (467 m) is near the 50 mg/L peak**: it is a one-point-driven result (the peak and the preceding rise); bootstrap interval 308–800 m. Also the Cl path does not cross a digitized trace until 1809 m (near E), and then Cl is low (15 mg/L); the peaks are ~300 m from the traces.
- **The 280 m InFault offsets are all at Site 3** where the field-flagged crossing and the digitized trace disagree by 110–280 m; S1's InFault points are 40–64 m from the trace. This supports ±300 m as an empirical, not a nominal, band.
- **Site 1 is weak evidence either way**: n = 9, SD 0.1–0.7, A is non-significant; 0 breakpoints are selected.
- Taconic State Parkway is not "major" in TIGER's coding (S1400), so any statement about proximity to it needs a manual step.
- Site 2 InFault: 6 InFault points, including gps 1–3 at the transect's start and 16, 18 at the end; the B boundary lies between gps 10 and 11 (3993 m), with InFault flagged at gps 11 (4166 m). Zone boundary vs trace crossings (1046 and 5763 m by chord) differ from the zone boundary (3993 m), which relates to R2.3a (multiple crossings).
- The revised table `figures/table1_revised.tex` has 12 columns; it needs `\scriptsize`/`\resizebox` or a landscape page. `\dagger` flags zones with n < 5 (add to the caption).
