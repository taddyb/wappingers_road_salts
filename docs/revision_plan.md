# Revision plan — Manuscript 101225 (reviewer round 1)

**Status: DRAFT FOR AUTHOR REVIEW. Nothing in `revisions.tex` has been changed.**
Mark each item **Accept / Modify / Skip** in the `Decision` column (or inline) before
any subagent is dispatched. Line numbers refer to the current `revisions.tex`
(identical to `original.tex`).

### Decisions recorded (author, 2026-11-07)

- **D1 Accepted.** Reframe as a hypothesis-generating case study; scale back *every*
  claim in abstract, results, discussion and conclusions.
- **D2 Accepted (no normalization).** The current tests already use raw µS/cm, so the
  z-score in Eq. 1 is a leftover from the original R analysis. Remove Eq. 1 and its
  paragraph. The site maps also colour points by a per-site z-score (`NEC` in
  `wappingers.zone_frames`); switch them to raw µS/cm so nothing in the paper is
  normalized.
- **D3 Accepted.** Run change-point / segmented regression of SC against distance
  on each single-day transect.
- **D6 Accepted.** Do all requested figure work.
- **No new data or fieldwork.** Every response uses the existing 2018 SC survey, the
  2020 chloride transect, published literature and existing map data. Where a
  reviewer asks for something that needs new data (discharge, tracers, repeat
  cross-sections), we acknowledge it in Limitations / Future work. Instrument specs
  come from the manufacturer's documentation, not new tests.
- **D0 Locked: option (a).** Zones are compared only within a single survey day. No
  cross-day pooling, no day covariate, no offset correction. Change-point / segmented
  regression (D3) also runs only on single-day transects. See §0b for why (b) and (c)
  were rejected.
- **FRAMING DECIDED (author, 2026-11-07): "inconclusive + test design."** WP0 found
  no SC breakpoint at any mapped fault crossing; Contrast B (the only significant
  fault contrast, +4.3 µS/cm, n_eff-adjusted p = 0.017) is a gradual downstream ramp
  beginning ~1.6 km upstream of the B boundary; E is a small n.s. rise (+1.6) whose
  breakpoint (194 m, pinned at the min-segment limit) is ~610 m upstream of the
  InFault points but 123 m from the nearest trace, i.e. inside the ±300 m band; D is a n.s. decrease; the 2020 Cl
  breakpoint is ~125 m from the D crossing points but rests on one 50 mg/L sample.
  The paper answers its title question as **"not clearly, in this survey"** and makes
  its contribution:
  1. a low-cost screening approach and what it can and cannot resolve;
  2. a documented pitfall: a multi-day survey without tie points produced a spurious
     18 µS/cm "fault step" (the submitted Contrast E), and how to avoid it;
  3. a specific, falsifiable test design for the fault-conduit hypothesis (single-day
     or tie-pointed surveys, paired discharge, Cl/Br and age tracers, cross-channel
     repeats, field-located fault zones, multiple lithologies);
  4. the context case for why faults remain a plausible pathway (literature, R1.4).
  Text WPs (WP3/WP4) must write every claim to this framing. No sentence may say
  or imply that the data show fault transport. Contrast B and the Cl peak near D
  are "observations worth testing", never "support".
- **CITATION BUDGET (author, 2026-11-08): the final cited set must be ≥30% from
  2022–2026; cut unnecessary citations to get there.** Today `revisions.tex` cites
  41 references, 13 of them recent (32%). Binding for WP3/WP4:
  - **Add (11; 2 recent):** caine1996, bense2013 (R1.4, requested by name);
    manda2008, kim2014 (fault/fracture flow in metamorphic rock, New England);
    harte2010, hodgins2024, hodgins2026 (longitudinal surveys locating salt-laden
    groundwater inputs; R1.3(i), R1.13); miller2014 (baseflow dominance, R1.3(ii));
    mullaney2009 (Cl and Cl/Br as a road-salt tracer, R1.3(iii)); genereux1998
    (two-end-member mixing, R2.1); runkel2013 (synoptic surveys need same-day/steady
    conditions; test design and the two-day pitfall).
  - **Do not cite** (verified but redundant): mabee2002, kimball2002, selker2006,
    panno2006, kronholm2015, cook2006, granato2015, waltonday2021. They stay in
    `references_revised.bib`; uncited entries don't print.
  - **Remove from the text (7 older, redundant once the intro is shortened per
    R1.1/R1.2):** bubeck1971 (history; tiwari2018/jackson2005 cover it),
    robinson2017 (the soil-persistence sentence is cut per R1.2), forman1998 and
    richburg2001 (impacts paragraph trimmed; hintz2022 carries it), foos2003 (third
    example of long-term increases), bredehoeft1992 and gudmundsson2000 (superseded
    by caine1996/bense2013).
  - **Result:** 41 + 11 − 7 = 45 cited, 15 recent = **33%**. Any further addition must
    keep this ≥30%; WP6 recounts from the final `revisions.tex`.
- **Chloride transect text errors (found 2026-11-08; WP3/WP4 must fix):** Methods
  (l.91) says the transect "spanned roughly one kilometer"; the data run 2,351 m
  (Z at 0 m, Kelly site at 1,224 m, Z′ at 2,351 m; 18 samples plus 1 side-tributary
  sample). Fig. 5's caption says "along zones 3-3 and 3-4"; the transect starts near
  the D crossing and ends at the E crossing, so it lies mostly within Zone 3-3.
  Results (l.143) attributes the Cl peak to Contrast E; it lies near D (see §0b).
- **InFault meaning (author, 2026-11-08):** points were flagged `InFault` "because we
  believed these points were located downstream of the fault". They do not mark
  an observed fault position, and they were not placed from the map. Consequences
  (binding for all WPs):
  1. The 5–280 m InFault-to-trace offsets **do not measure fault-location error**
     and cannot justify the band width. Drop that argument everywhere (plan,
     analysis_results.md, letter, Methods).
  2. Never describe InFault points as "fault crossings", "observed in the field" or
     "at the fault". Use "survey points flagged in the field log as lying just
     downstream of the mapped fault". Distances reported "from InFault points"
     (e.g. Contrast E breakpoint ~610 m, Cl breakpoint ~125 m from the D points)
     must be reworded on this basis or replaced by distance to the digitized trace.
  3. Figure legend: replace "Survey point noted as at the fault (field log)" with
     wording to match (`INFAULT_LABEL` in `src/rev_figures.py`). `src/maps.py`'s
     docstring ("where the crossing was actually observed in the field") is wrong
     and must be corrected.
- **Fault band: DECIDED, no band (author, 2026-11-08).** Budnik et al. (2010) states
  no positional accuracy (p. 18: locations "largely conjectural"; see
  `docs/budnik_fault_accuracy.md`), and the FGDC/NMAS options were not judged good
  enough to cite. Faults are drawn as lines on all maps. Tell Reviewer 2 (R2.6, R2.13)
  we found no citable error zone; discuss the uncertainty in the text and in
  Limitations. Do not cite FGDC-STD-013-2006 or NMAS. Do not mention ±300 m anywhere.
  The "Defaults accepted → Fault uncertainty band" bullet below is superseded.
- **Word count (author, 2026-11-08): the ≥5,000 main-body-word minimum still
  applies.** Count runs Introduction → Conclusions, excluding the abstract, captions,
  tables, equations and references. Current: 4,830 (Intro 889, Methods 1,188, Results
  817, Discussion 1,541, Conclusions 390). Targets: Intro ~800–900 (R1.1 wants it
  tighter, but it gains the fault-hydrogeology and tributary paragraphs), Methods
  ~1,300–1,450, Results ~900–1,000, Discussion ~1,900–2,100 (adds Limitations and
  the test design), Conclusions ~350–450. **Final ≥5,300 for margin.** Each text WP
  reports its section counts with the same counting script (WP6 re-checks).
- **Site 2 reframing (author, 2026-11-08):** the Contrast B boundary (the 90° bend)
  is where the authors believe the fault IS. The digitized Budnik trace is conjectural,
  so its intersections with the survey (~1.0/5.8 km) are not reliable fault positions.
  X markers are removed from the site maps and lightened/relabelled on Figs 5–6. The
  text describes B as the field-interpreted fault position and keeps the honest ramp
  result (onset roughly 1.6 km, 0.6–2.7 km, upstream of the bend).
- **ORCIDs (author, 2026-11-08):** Tadd Bindas 0000-0003-3159-6276; Zion Klos
  0000-0002-9563-6065. Klos's department is still unknown (omitted).
- **Fable editor-style review (2026-11-08):** verdict: ready to return to the
  reviewers after presentation fixes. Must-fixes being applied: no self-reference to the
  submission history in the paper, bib hyphen glyphs (fixed), letter \showplanfalse and
  date, ORCIDs, no "A Preprint" running head, appendix table anchors, Contrast C 19 Oct
  Welch/MW disagreement stated, Titusville/Valley Dale mentioned, orphan Orr sentence
  moved, repetition trimmed.
- **Chloride sensor (author, 2026-11-08): RESOLVED.** YSI Pro Series 1005 chloride
  ISE (605105), on a YSI handheld meter (Pro Plus or ProQuatro). From the ProQuatro
  spec sheet: range 0–1,000 mg/L at 0–40 °C, resolution 0.01 mg/L, accuracy ±15% of
  reading or ±5 mg/L (whichever is greater), 1–3-point calibration. From the manual:
  2-point calibration at 10 and 1,000 mg/L recommended; freshwater only; temporary
  drift after exposure to pH buffers; working life 3–6 months. At 14–50 mg/L the
  accuracy is ±5 to ±7.5 mg/L. This is in §2.2, §4.4 and R1.5(2); no TBDs remain.
  Open curiosity, not in the paper: all recorded values are multiples of 1.25 mg/L
  although the meter resolves 0.01 mg/L (possibly rounded when transcribed). A
  NOTE(author) comment in §2.2 asks for the calibration standards if known.
- **Site 2 boundary (author, 2026-11-08): RESOLVED.** "The site 2 original comparison
  was where the river had a 90 degree sudden break indicating preferential flow along
  a fault line." This is in §2.2 and R2.4, framed as a field interpretation of channel
  geometry: the mapped crossings at ~1.0/5.8 km don't coincide with the bend, and a
  bend does not show groundwater flow along the fault. Only the chloride-method TBD
  remains.
- **Word count after WP4 (2026-11-08):** the author confirmed that the requirement is
  ≥5,000 words in the main body, excluding the abstract and references, and that
  6,000+ is comfortable. Strict count (also excluding captions, tables, equations and
  the appendix): 5,992. Including figure/table captions: 6,925. WP6 re-checks; any
  later edits must keep the strict count ≥5,500.
- **Author block (author, 2026-11-08):** Tadd Bindas has no department: the research
  was done as an undergraduate at Marist (University). He now works at FBF
  Engineering. Write it as affiliation "Marist University, Poughkeepsie, NY" with a
  footnote "Present address: FBF Engineering". Keep the email. Names and order are
  unchanged (editor rule). ORCIDs are filled in. Departments are not required by the
  editor (names, emails, affiliations only), so none are given. Tadd's Marist
  affiliation is approved by the author (the work was his Marist senior thesis).
- **Instruments (author, 2026-11-08):** SC survey used a Thermo Scientific Orion
  013010MD conductivity cell, "calibrated successfully using the standard protocols
  outlined by the manufacturer". Name the manufacturer. Author re-confirmed: Orion cell in
  2018 (SC), YSI Pro Series 1005 chloride ISE in 2020. The Orion Star meter model is
  unknown; quote the spec shared by the compatible meters (`docs/instrument_specs.md`).
  No TODO remains for this.
- **Wastewater (author, 2026-11-08; findings in `docs/wwtp_kelly2008.md`,
  `data/wwtp_facilities.csv`):** Millbrook STP (NY0025429, East Branch) is upstream
  of all sites: ~2.4 km along the channel above Site 3, 15.3 km above Site 1 and
  25.3 km above Site 2. It is a continuous upstream source and cannot alone make a
  mid-reach step. **Two private STPs sit beside Site 2's zone 2-1:** Ennis MHP
  (nearest survey point at ~0.9 km along, 369 m away) and Stratford Farms (~1.6 km
  along, 242 m away). The Site 2 breakpoint is at 2.36 km (bootstrap 1.3–3.4 km). These
  are ECHO facility locations, not outfalls; flows are not listed. WP4 must name them in
  §4.2 as a plausible, untested alternative source for the Site 2 increase. Facilities
  are being added to Figs 1b and 3. Kelly 2008 numbers to state: road 83%, parking 8%
  (deicing 91%), sewage incl. septic 4%, softeners 3%; weathering 1% was estimated
  from a single 1905 sample, not measured. Kelly 2008's sampling site
  (N41.786 W73.741) is ~0.8 km from the chloride file's "long-term" point, which cites
  Kelly **2019**, so don't conflate the two sites.
- **WP3 done (2026-11-08).** Intro and Methods were rewritten: 45 references cited,
  33% from 2022–2026; Intro 924 words, Methods 1,470. The orchestrator then added the
  instrument accuracy (±0.5% of reading via the compatible Orion Star meters) and
  neutral chloride wording. **WP4 must:** (a) move some syndrome/impacts material into
  the Discussion, because the R1.1 response says it was "partly moved to the
  Discussion"; (b) put the single-transect and measurement-precision caveat in
  Limitations (R1.5(2)); (c) note that Contrast E's +1.6 µS/cm is within instrument
  accuracy, while B's 4.3 is ~2.5×; (d) keep the chloride method neutral until it is
  confirmed (all values are multiples of 1.25 mg/L).
- **Defaults accepted (author, 2026-11-07):**
  - *Karst example (Ferrill 2025):* keep as one sentence, explicitly labelled a
    carbonate example and not a direct analogue for the metasedimentary bedrock (R1.4).
  - *Road distance:* compute the distance from each SC point to the nearest major
    road (`data/tiger`); report the per-zone median descriptively (Table 1 or the
    appendix) and discuss it in §4.2. No regression or significance claims (R1.12, R2.9).
  - *Fault uncertainty band:* empirical. The 16 `InFault` field points lie 5–280 m
    (median ~90 m) from the digitized Budnik traces, so draw ±300 m bands and state
    the basis in Methods (R2.6, R2.13). Recompute the offsets in WP1 rather than
    trusting these preliminary numbers.
  - *Confluence-mixing paragraph:* in the Introduction (R2.1).
  - *Change-point method:* segmented (piecewise-linear) regression, number of
    breakpoints chosen by BIC, checked with a change-in-mean (PELT) analysis.
  - *Change-point results:* a new figure of SC vs. distance, one panel per
    single-day transect, with fitted segments, breakpoints and the positions of
    mapped fault crossings and tributaries (R1.5(3)); chloride gets the same
    treatment in Fig. 5.
- **Still needed from the author:** conductivity meter model + accuracy/temperature
  compensation spec; YSI sonde/chloride probe model + spec; how the Site 2 zone
  boundary was chosen; what `InFault` meant in the field (judged on site vs. plotted
  from the map).
- **Comment IDs:** the labels in `response_to_reviewers.tex` are canonical. Reviewer 1
  uses their own numbers (R1.1–R1.14, with R1.5(1)–(3)); Reviewer 2's unnumbered
  comments are R2.1 (intro), R2.2 (normalization), R2.3 (SD/raw data), R2.4 (Fig 3
  zones), R2.5 (Contrast B), R2.6 (Contrast E), R2.7 (chloride test), R2.8 (Zone 3-1
  overlap), R2.9 (land use), R2.10–R2.14 (Figs 1–5), R2.15 (Table 1). The R2 IDs in
  the tables below (R2.2a, R2.3c, …) predate this numbering.
- **Comments doc first:** `response_to_reviewers.tex` holds every comment verbatim
  with a planned response; review it before any work package runs.

Editor requirements for resubmission: (1) revised manuscript with changes highlighted
→ `latexdiff original.tex revisions.tex`; (2) separate point-by-point letter →
`response_to_reviewers.tex`; (3) **do not add, remove, or alter authors** (filling in
missing affiliations/emails for the existing two authors is allowed and requested).

---

## 0. Finding that should be decided first (affects R1.5, R1.7, R1.10, R2.3, Fig 4, Table 1)

While checking the reviewers' statistical points against `data/salinity-dataset.xlsx`,
I found that **the Site 3 zones mix two survey days**, and the day-to-day offset is
larger than the contrasts being tested.

| Site 3 sub-survey | Date | EC level |
|---|---|---|
| field site 3 (rows 14–33) | 19 Oct 2018 | ~332–340 µS/cm |
| field sites 4 and 5 (rows 0–13, 34–45) | 26 Oct 2018 | ~355–375 µS/cm |

- The end of the 19 Oct survey and the start of the 26 Oct survey are **18 m apart**,
  yet EC jumps from 332.0 to 355.5 µS/cm there: a ~23 µS/cm **day offset at the
  same place**.
- Zones 3-1, 3-2 and 3-3 each contain points from both days, which explains their
  large SDs (12.6–15.8 µS/cm vs. ≤2.6 within any single day). That is exactly what
  R1.7 inferred, and it is the "two overlapping sets of data (~370 and ~340)" in
  Zone 3-1 that R2 noticed.
- The manuscript says (l.110, l.134) that "every zone-to-zone comparison was computed
  within a single day's data". **That is not true for the current zone definitions.**
- Recomputed **within a single day** (Welch, raw µS/cm):

| Contrast | Day | n₁,n₂ | Δ (µS/cm) | Welch p | M-W p | Current table |
|---|---|---|---|---|---|---|
| C (tributary) | 19 Oct | 6,3 | −3.8 | 0.093 | 0.028 | −9.2, p=0.248 |
| C (tributary) | 26 Oct | 11,3 | −5.6 | <0.001 | 0.012 | |
| D (fault) | 19 Oct | 3,11 | −2.8 | 0.140 | 0.119 | −8.2, p=0.286 |
| **E (fault)** | 26 Oct | 6,6 | **+1.6** | **0.090** | 0.076 | **+18.0, p<0.001** |

**Implication:** the "largest step of the entire study" at Contrast E (+18.0 µS/cm,
p<0.001) is almost entirely the day offset. Within one day, E is a +1.6 µS/cm rise
that is not significant. The surviving SC evidence is Contrast B (+4.3 µS/cm,
single day, p<0.001, but close to instrument uncertainty per R1.11/R2) plus the 2020
chloride transect (single day, not yet tested statistically).

Also: Site 1 was surveyed on **28 Sep 2018**, not in October (l.85 says "October
2018"); Sites 1–3 span 28 Sep–26 Oct with water temperatures from 15 °C to 8 °C.

Side note: the *original* R analysis z-scored each field sub-survey separately
(`zones_as_published`), which incidentally removed the day offset. The later
"correction" to raw µS/cm reintroduced it.

**Decision D0: how to handle this** (pick one):
- **(a) Recommended:** Make within-day contrasts the primary analysis. Report Site 3
  per day, say plainly that E is a small, non-significant rise once the day offset is
  removed, and move the Site 3 weight onto the chloride transect (D4). This fits
  R1's request to reframe the paper as a hypothesis-generating case study, and
  disclosing it ourselves is far better than a reviewer finding it later.
- (b) Fit `SC ~ zone + survey_day` (day as a fixed effect). This is similar to (a)
  but still pools across days.
- (c) Keep the zones and only acknowledge the confound. **Not recommended:**
  reviewers 1 and 2 already see its symptoms.

Decision: **(a), locked 2026-11-07.**

### 0b. Follow-up checks behind the D0 decision (preliminary; WP0 to reproduce)

1. **The day offset is not constant.** Field site 5 (26 Oct) re-surveyed the reach of
   site 3 rows 14–22 (19 Oct). Nine point pairs 15–50 m apart differ by +27.3 to
   +29.7 µS/cm. At the 19 Oct / 26 Oct seam (rows 33/34, 18 m apart) the difference
   is +23.5 µS/cm. That ~5 µS/cm spread is larger than Contrasts B and E, so a day
   covariate (b) or an offset correction (c) rests on an assumption the data
   contradict.
2. **The E rise on 26 Oct is not at the mapped crossing.** Along site 4, SC rises
   355.5 → 359.7 µS/cm over the first ~190 m, then stays flat (~360) through the
   `InFault` points at 804–929 m. The onset is ~600 m upstream of the mapped trace,
   beyond the "few hundred metres" uncertainty stated in the Methods (l.89). This
   bears on R2.6.
3. **The chloride transect does not support Contrast E.** The transect Z→Z′ starts
   near the D crossing and ends at the E crossing. The Cl peaks (50 mg/L at 474 m,
   40 mg/L at 959 m, both field-noted "possible fault?") lie ~130–470 m from the D
   `InFault` points and ~300 m from the nearest digitized fault line. Near E, Cl is
   low (14–15 mg/L) and falling. The 6.2 mg/L "side tributary" sample is ~40 m from
   the D crossing. **The manuscript's claim that the chloride peak corroborates
   Contrast E (l.143, l.170, Fig. 5 caption, abstract, conclusions) is wrong** and must
   be rewritten. The Fig. 5 caption's "zones 3-3 and 3-4" also needs checking: the
   transect lies mostly within Zone 3-3.
4. **What the evidence says under (a):** B is a small significant rise (+4.3); E is a
   small non-significant rise whose onset is ~600 m upstream of the trace (+1.6,
   p=0.09); D shows no SC rise on 19 Oct (−2.8, n.s.), but the 2020 Cl peaks are
   nearest the D fault; C (tributary) decreases on both days, an internal check that
   the survey detects a known input.

**Consequences:**
- **D4 changes.** Reviewer 2 asked for a chloride test above/below E, but only ~2–3
  transect points lie downstream of E, so a two-sample test there is not meaningful.
  Instead: report that Cl near E is low and flat (answering R2.7 directly), and run
  the same change-point / segmented regression on the Cl transect to locate its
  breakpoints relative to the D crossing and the mapped fault lines. Describe it, with
  no significance claim beyond what the method supports.
- **Title. DECIDED and applied** in `revisions.tex` (title, running head, PDF
  metadata): "Do fault zones route road-salt-contaminated groundwater to streams? A
  Hudson Valley, NY Case Study".

---

## 1. Global decisions

| ID | Decision | Recommendation | Decision |
|---|---|---|---|
| D1 | Reframe the paper as a **hypothesis-generating case study** (R1 summary, R2 summary): title stays; abstract, intro last paragraph, discussion and conclusions use "consistent with", "suggests", "warrants testing". | Accept. Both reviewers ask for it, and D0 makes it necessary. | |
| D2 | **Drop the z-score normalization** (Eq. 1, l.95–100) from the Methods; tests are on raw µS/cm. Keep it only as map-colour scaling, if at all. Answers R1.9 and R2's "clarify normalization" and "show normalized means". | Accept (normalization isn't used by any test now). | |
| D3 | Add **change-point / segmented regression** of SC vs. distance on each single-day transect (R1.5(3)), and an **autocorrelation-adjusted** effective n (R1.8). | Accept as a secondary analysis; mention it as a recommended future approach if you'd rather keep the analysis minimal. | |
| D4 | **SUPERSEDED by §0b:** chloride gets change-point analysis, not an E two-sample test. Original idea: **Test chloride above vs. below Contrast E** (R2, Table 1 comment). The data (`chloride-dataset.xlsx`, 19 pts) have lat/lon, so the fault position on the transect can be located. | Accept. This becomes the key Site 3 evidence under D0(a). Numbers are unknown until it's run. | |
| D5 | Where to show **raw data** (R2): appendix table (~73 rows: point, date, distance, EC, temp, zone) vs. supplementary CSV + Data Availability. | Appendix table generated by `stats.py`. | |
| D6 | **Figure work scope** (R2 §5): all requested items vs. a subset. | All of them: each is small in `maps.py`, and Z–Z′ / fault band / day markers are needed anyway. | |
| D7 | **Word count / recent-reference targets** from the original editor screen (≥5,000 words, ≥30% refs 2022–26, per CLAUDE.md; `~/papers/revision_outline.md` no longer exists). R1.1 asks to *shorten* the impacts/syndrome intro. | Move rather than delete: shorten §1 P2–P4 and put the syndrome framing in Discussion §4.3 (where it already partly lives). Confirm whether the ≥5,000-word target still applies. | |

---

## 2. Reviewer 1 — point by point

| # | Comment (short) | Assessment | Proposed change | Where | Type | Decision |
|---|---|---|---|---|---|---|
| R1.0 | Data don't show faults *cause* steps, that faults connect to a highway, or that road salt is the source. Reframe, discuss alternatives/limitations, clarify maps, temper conclusions. | Agree | D1 + a new **Limitations** subsection (§4.x) that names each gap: no discharge, no tracers, single Cl transect, county-scale fault traces, unverified fault–highway connectivity, day offset (D0). | Abstract, §1 last para, new §4.x, §5 | text | |
| R1.1 | Intro reaches geology late. | Agree | Restructure §1: P1 road salt + legacy groundwater (condensed P1–P3), P2 **fault hydrogeology** (moved up), P3 syndrome framing condensed to 2–3 sentences, P4 hypothesis/predictions. Impact detail (Hintz 2022, etc.) trimmed and partly moved to §4.3/§4.5. | l.54–66 | text | |
| R1.2 | Soil and groundwater timescales mixed. | Agree | Drop or separate the soil-persistence sentence (`robinson2017`, 2.5–5 months, l.58); keep the groundwater residence argument (`rivett2016`, `vanmeter2024`, `perera2013`). Also fixes R2.4's "salt can persist in soil" link, see R2.4. | l.58 | text | |
| R1.3 | Testable predictions have no references. | Agree | Cite literature for each: (i) longitudinal SC/temperature surveys to locate point groundwater inputs; (ii) baseflow = groundwater-dominated; (iii) Cl as deicer fingerprint. **New refs need verification (WP2).** | l.64 | text + bib | |
| R1.4 | Fault hydrogeology rests on karst (`ferrill2025`) and unconsolidated aquifers (`bense2008`), not metamorphic bedrock; suggests Caine et al. 1996, Bense et al. 2013. | Agree | Add Caine, Evans & Forster 1996 (Geology 24:1025) and Bense et al. 2013 (Earth-Sci. Rev. 127:171) + 1–2 fractured crystalline/metamorphic-bedrock fault-flow studies (WP2 to find and **verify**). Keep Ferrill as an explicitly labelled carbonate example, or cut it. | l.62, l.74, §4.3 | text + bib | |
| R1.5(1) | No discharge, no source tracers. | Agree | State in Limitations; future work already mentions Cl/Br and age tracers (l.184). Add discharge/mass-balance. | new §4.x, §4.4 | text | |
| R1.5(2) | One Cl transect, ion-selective probe. | Agree | Methods: name the probe/ISE and its stated accuracy (**need spec — author to supply**); Limitations. | l.91, §4.x | text | |
| R1.5(3) | t-tests can't show abruptness; suggest change-point / segmented regression. | Agree | D3. | §2.3, §3, Table/Fig | analysis + text | |
| R1.6 | Table 1 lacks SD, df, CIs, Mann–Whitney. | Agree | Regenerate Table 1 with: n, mean ± SD per zone, Δ, 95% CI of Δ, Welch t, df, p, M–W U, p, survey date. (Normalized means not added; see D2.) | `src/stats.py`, l.157–162 | analysis | |
| R1.7 | t values imply Zone 3-2 SD larger than the contrasts. | **Correct**, and explained by D0 (day mixing). | Answered by D0 and the new table. | — | — | |
| R1.8 | Spatial autocorrelation not handled; p-values too small. | Agree | D3: lag-1 autocorrelation → effective n; report adjusted p or state p as upper-bound significance. Rewrite l.110's "within-zone scatter is small" justification. | §2.3 | analysis + text | |
| R1.9 | z-score normalization has no effect on within-site tests. | Correct | D2. | l.95–100 | text | |
| R1.10 | Contrast D explanation wrong: C and E have the same 17/6 split. | Correct | Delete the "most unequal sample sizes / least power" reasoning (l.134, l.170, l.194). Replace with within-day result (D0). | l.134, 170, 194 | text | |
| R1.11 | 4.3 µS/cm at B near uncertainty of temperature-compensated SC. | Fair | Report the Orion cell/meter accuracy and temperature-compensation uncertainty (**author to supply the spec / meter model**; don't invent). Note B's within-zone SD (1.1–1.9) and same-day sampling; describe B as small. | §2.2, §3.1, §4.1 | text | |
| R1.12 | Alternative sources: US 44/NY 82 next to high-SC zones, developed land at Site 2, WWTP + septic upstream (Kelly 2008), diffuse groundwater. | Agree | Expand §4.2: road proximity (see R2.4, optional quantitative road-distance per zone from `data/tiger`), Site 2 land use, WWTP/septic upstream (**verify from Kelly 2008**), diffuse groundwater. Remove the "conserved forest ⇒ discount" overstatement. | l.176 | text (+ optional analysis) | |
| R1.13 | Overreach: "strong initial evidence", "this newly observed process"; §4.4 says all three crossings point to a link though D decreases; fault-based deicer switching premature; little comparison with other longitudinal surveys / metamorphic fault hydrogeology. | Agree | Tone pass (list below). Fix l.184 "all three point to". Management §4.5 becomes "a candidate screening layer to evaluate" rather than "use a different deicer". Add a comparison paragraph to §4.1/4.3 (orr2026 + WP2 refs). | l.172, 184, 188–196 | text | |
| R1.14 | Missing DOIs/report numbers; grouped citations out of order. | Agree | `\usepackage[numbers,sort&compress]{natbib}`; add DOI/report no. to: jamshidi2020, richburg2001, shattuck2023, kaushal2005, schalk2012, bredehoeft1992, budnik2010, kelly2019, kelting2010, willmert2018, adirondack2023 (**verify each**). | preamble, `references.bib` | bib | |

Overreach phrases to soften (R1.13): "strong initial evidence" (l.172), "much stronger link" (l.172), "this newly observed process" (l.184), "all three point to" (l.184), "core observation the statistics support" / "largest step of the entire study" (l.134), "corroborates … independent ion" (l.143), "establishes both the pattern" (l.196), "concentrates significance at the unconfounded fault crossings" (l.196), abstract "reproduced the strongest of these steps".

## 3. Reviewer 2 — point by point

| # | Comment (short) | Assessment | Proposed change | Where | Type | Decision |
|---|---|---|---|---|---|---|
| R2.1 | Intro: add how tributaries typically affect downstream conductance; tributary dilution might be larger without salty groundwater. | Agree | One paragraph in §1 (or §2.1) on mixing at confluences (two-end-member mixing; needs refs, WP2). Pick up the "dilution damped" idea in §4.1 only as a hypothesis. | §1, §4.1 | text + bib | |
| R2.2a | Clarify whether normalization was by site or zone. | — | D2 (removed). Response explains. | l.95 | text | |
| R2.2b | Show SDs for "within-zone scatter is small"; means ± SD/SE everywhere. | Agree | New Table 1; text gives mean ± SD; figure zone labels show mean ± SD. | §3, figs | analysis + fig | |
| R2.2c | Show actual data (Table 2 or appendix). | Agree | D5. | appendix | analysis | |
| R2.3a | Fig 3: the fault crosses the stream several times; justify zone choice. | Needs map check | Explain zone boundary rule in Methods + caption; if multiple crossings are real, show them and say why one boundary was used. **Author to confirm how Site 2 zones were chosen.** | §2.2, Fig 3 | text + fig | |
| R2.3b | Contrast B is small: meter uncertainty? within-zone variability? lateral/depth variability >5 µS/cm. | Fair | Same as R1.11 + report SDs; acknowledge thalweg-only sampling and no cross-section repeats in Limitations. | §2.2, §4.x | text | |
| R2.3c | Contrast E: the change seems to occur within Zone 3-3; fault trace may be offset east; show a fault zone. | Partly explained by D0: the visible jump in Fig 4 is the **19→26 Oct seam**. | Under D0(a) say so. Draw the fault as a band with the mapping uncertainty (D6). Discuss trace-position uncertainty (already l.89). | §3, Fig 4 | text + fig | |
| R2.3d | Test chloride above/below E. | Agree | D4. | §3, Table 1 | analysis | |
| R2.3e | Zone 3-1 has two overlapping sets (~370 and ~340). | Correct: two survey days (D0) | Caption + text; Fig 4 markers by survey date. | Fig 4, §3 | fig + text | |
| R2.4 | Land-use dismissal too strong; road distance/density varies by zone; soil salt persists 5 months. | Agree | §4.2: discuss road proximity/density per zone (optional: distance to nearest salted road per point from `data/tiger`, reported descriptively); drop "conserved forest ⇒ discount" logic; tie to R1.2 (the soil 5-month sentence is removed or reframed, so late-summer/fall soil flushing is an acknowledged alternative). | l.176 | text (+ optional analysis) | |
| R2.5 Fig 1 | (b) too busy: simplify to major streams + faults, highlight study streams. | Agree | `maps.py` overview panel b. | Fig 1 | fig | |
| R2.5 Fig 2 | Label contrast A; flow direction. | Agree | `maps.py` | Fig 2 | fig | |
| R2.5 Fig 3 | Label contrast B; flow direction. | Agree | `maps.py` | Fig 3 | fig | |
| R2.5 Fig 4 | Label C, D, E; flow direction; fault location error; Z–Z′ line; inset/offset for overlapping points in 3-1/3-2. | Agree | `maps.py`; overlap handled by date-coded markers + inset. Z–Z′ from chloride lat/lon. | Fig 4 | fig | |
| R2.5 Fig 5 | Show Z–Z′ in Fig 4 or add a location inset. | Agree | Z–Z′ in Fig 4 + mark fault position (and E) on Fig 5's x-axis. | Fig 5 | fig | |
| R2.5 Table 1 | Normalized means; variance; chloride above/below E. | Mostly agree | Variance + chloride (D4) yes; normalized means no (D2), explained in response. | Table 1 | analysis | |

## 4. Reviewer 3 / Editor

Reviewer 3 says only "Minor Revisions" with no comments, and the Editor recommends
publication once the points are addressed. Both get a short thank-you in the letter.

## 5. Items that need the author (cannot be done by subagents)

1. Decisions D0–D7 and per-item Accept/Modify/Skip.
2. Conductivity meter model + stated accuracy and temperature-compensation spec (R1.11, R2.3b); YSI chloride probe model + ISE accuracy (R1.5(2)). These come from the manufacturer's manuals, not new testing. Which meter body was used with the Orion 013010MD cell? (Reviewer 2 assumes a YSI.)
3. How Site 2 zones were chosen relative to multiple fault crossings (R2.3a).
4. Whether the ≥5,000-word / ≥30%-recent-refs targets still apply (D7).
5. Affiliation/email details for the author block (allowed by the editor; no author changes).
6. WWTP / septic facts: confirm from Kelly et al. 2008 (subagent can read it if accessible).

## 6. Work packages for Sonnet subagents (after approval)

Run in this order; WP1 and WP2 can run in parallel with each other. Text WPs edit
**disjoint sections** of `revisions.tex` and run one at a time to avoid edit
collisions. Every subagent gets: CLAUDE.md, this plan with decisions filled in, and
the rule "don't invent numbers; every new number comes from `src/` output; every
new reference verified by opening the DOI."

**Standing rules for every subagent (author request, 2026-11-07):**
- **Show the author every figure after it changes.** Any WP that creates or
  regenerates a figure must end by listing each new or changed PNG with its path
  and a one-line description of what changed. The orchestrator then sends the
  images to the author (`SendUserFile`, render) for review before any text WP
  cites them.
- **Never overwrite files that `original.tex` uses** (`figures/overview.png`,
  `site1-3.png`, `chloride.png`, `table1_corrected.tex`). `original.tex` is the
  frozen latexdiff baseline, and `original.pdf` must keep rendering the submitted
  version. Write revised outputs to new names (`figures/rev_*.png`,
  `figures/table1_revised.tex`, …); `revisions.tex` will point at those.
- **Bibliography:** `original.tex` also reads `references.bib`, so leave it unchanged.
  WP2 writes `references_revised.bib` (a copy with DOIs added and new entries), and
  `revisions.tex` will switch to `\bibliography{references_revised}`.
- **Report unfavourable results as they are.** The paper is now
  hypothesis-generating; a null or contradicting result is a finding, not a
  problem to fix.

| WP | Scope | Files owned | Depends on | Output |
|---|---|---|---|---|
| WP0 Analysis | D0 day-aware contrasts, new Table 1 (R1.6), autocorrelation n_eff (R1.8), change-point/segmented regression (D3), chloride test (D4), raw-data appendix table (D5), optional road-distance per zone | `src/stats.py`, `src/wappingers.py`, new `src/changepoint.py`, `figures/*.tex` | D0, D3–D5 | regenerated `.tex` tables + a `docs/analysis_results.md` with every number the text will quote |
| WP1 Figures | All R2.5 items, date-coded markers, fault band, Z–Z′ | `src/maps.py`, `src/figures.py`, `figures/*.png` | D0, D6 (and WP0 for zone defs) | regenerated PNGs + rendered previews for author check |
| WP2 Literature | Verify Caine 1996, Bense 2013; find + verify metamorphic/crystalline fault-flow refs, longitudinal-SC-survey refs (R1.3, R1.13), confluence-mixing refs (R2.1); DOIs for 11 entries (R1.14) | `references.bib`, `docs/new_refs_verified.md` | — | bib entries + a 1–2 line summary per paper of what it supports |
| WP3 Intro + Methods | R1.1–R1.4, R2.1, D2, R1.5(2), R1.11, R2.3a, dates fix, natbib option | `revisions.tex` preamble, §1, §2 | WP0, WP2 | edits |
| WP4 Results + Discussion + Conclusions + Abstract | D0, D1, R1.0, R1.5, R1.7–R1.13, R2.2–R2.4, captions, Limitations subsection | `revisions.tex` abstract, §3–§5 | WP0, WP1, WP2, WP3 | edits |
| WP5 Response letter | Verbatim comments + responses + quoted changes | `response_to_reviewers.tex` | WP3, WP4 | letter |
| WP6 Verify | Build all 3 docs + `latexdiff`, check every number in the text against `docs/analysis_results.md`, check every new citation exists in the bib | — | all | report |
