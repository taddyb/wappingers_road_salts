# Citation audit: revisions.tex, references_revised.bib, response_to_reviewers.tex

Audit date: 2026-11-09. This audit is read-only: no manuscript, bib or letter file was edited.

Line numbers refer to `revisions.tex` as of commit fc6952a, which removed the Introduction karst sentence. With that commit, `ferrill2025` is cited only at L224.

## Method

- Every DOI was resolved with the Crossref API, and authors, title, journal, volume, issue, pages and year were compared field by field with the bib entry.
- USGS reports were checked against the USGS Pubs Warehouse API (`pubs-services/publication/<id>`).
- Abstracts came from Crossref, OpenAlex, Semantic Scholar, USGS, AGRIS, the UMass bibliography or repository records.
- The full text was read for these works:
  - Schalk & Stasulis 2012 (USGS SIR PDF)
  - Budnik et al. 2010 (Dutchess County PDF, including a render of Fig. 3.10)
  - Kelly et al. 2008 (Cary reprint)
  - Kelly et al. 2019 (Cary report PDF; all 16 pages rendered)
  - Nimiroski & Waldron 2002 (USGS PDF)
  - Kelting & Laxson 2010 (84-page PDF)
  - Adirondack Task Force 2023 (DEC PDF)
  - Jackson & Jobbágy 2005 (PMC)
  - Ruxton 2006 (OpenAlex full-text index)

The verdicts are:

- **SUPPORTED** means the claim matches the source.
- **PARTLY** means the claim overstates or blurs what the source says.
- **NOT SUPPORTED** means the source does not say it, or says the opposite.
- **COULD NOT VERIFY** means the abstract was not enough and the full text could not be reached.

## Summary table (41 cited keys)

| key | real? | bib correct? | claim verdict | one-line issue |
|---|---|---|---|---|
| tiwari2018 | yes | yes (issue 1 missing, minor) | PARTLY | Jackson 2005 shows US use since 1940 only; "Europe" and "since early 1940s" not confirmed from Tiwari (full text not reached) |
| jackson2005 | yes | yes (issue 41 missing, minor) | SUPPORTED (L59 ×2) | US salt sales 1940-2004 rising ~100x; groundwater/stream salinization |
| kaushal2005 | yes | yes (issue 38 missing) | SUPPORTED / PARTLY at L61 | NE US only; L61 "documented globally" overstates |
| dugan2023 | yes | **NO: authors** | SUPPORTED | Crossref lists only 2 authors (Dugan & Arnott); "and others" is wrong |
| jamshidi2020 | yes | yes | COULD NOT VERIFY (abstract does not support) | Abstract is about groundwater in Hamedan/Malayer, Iran; it doesn't say salt is applied beyond need |
| kelting2010 | yes | yes (AWI2010-01 confirmed on title page, Feb 2010) | SUPPORTED (L59, L240) | Letter calls it "Kelting et al." (2 authors) |
| williams1999 | yes | yes (year 2000 correct; key says 1999) | SUPPORTED L59 / PARTLY L61 | Toronto groundwater, not "global" trends |
| findlay2011 | yes | yes | SUPPORTED | |
| hintz2022 | yes | yes | SUPPORTED | These were mesocosm experiments at lake sites, so "in lakes" is loose but acceptable |
| shattuck2023 | yes | yes | SUPPORTED | |
| corsi2015 | yes | yes | SUPPORTED | Abstract: "maximum concentrations occurred during winter" |
| kelly2008 | yes | yes (issue 2 missing) | SUPPORTED (L61, L216) | All percentages and the 1905 weathering estimate checked against full text |
| rivett2016 | yes | yes | PARTLY | Covers two severe UK winters of infiltration, not "recent decades" |
| vanmeter2024 | yes | yes | SUPPORTED | Groundwater accumulation ~480 kt/yr; baseflow release |
| caine1996 | yes | yes | SUPPORTED | |
| bense2013 | yes | yes | SUPPORTED | Abstract (via mirror): along-fault flow favoured over across-fault; context-dependent |
| **schalk2012** | yes | yes | **NOT SUPPORTED** | **No fault zone in the report: the 4 wells are in 3 towns in different rock units. Also affects the abstract, L63 and L224** |
| manda2008 | yes | yes | SUPPORTED (ms) / PARTLY (letter) | Foliation-parallel fractures, not faults; the letter calls it "fault-controlled flow" |
| kim2014 | yes | yes | SUPPORTED | Hinesburg thrust; well yield and chemistry |
| kaushal2018 | yes | yes | SUPPORTED | Source of the term "freshwater salinization syndrome" |
| kaushal2023saltcycle | yes | yes (issue 11 missing) | SUPPORTED | Term is the title |
| kaushal2023factors | yes | yes | PARTLY | A hypothesis framework of five "state factors"; "first-order controls on where salt reaches streams" overstates |
| genereux1998 | yes | yes | SUPPORTED | Cited for the mixing principle only, which is how the text uses it |
| harte2010 | yes | yes | SUPPORTED | |
| hodgins2024 | yes | yes | SUPPORTED | "<100 to >5000 mg/L over ≤10 m" is exact |
| hodgins2026 | yes | yes (print 2026; online 2025) | SUPPORTED | |
| miller2014 | yes | yes | PARTLY | Upper Colorado snowmelt basins, baseflow 40-86% at low flow; "direct runoff is absent" is not from the source |
| mullaney2009 | yes | yes | PARTLY (L69, L236) | "the standard fingerprint" overstates; "sewage mixtures common at lower ratios" misreads the source |
| budnik2010 | yes | minor (booktitle) | SUPPORTED | Quote and p. 18 exact; Fig. 3.10 legend and 1:340,000 scale confirmed |
| kelly2019 | yes | yes | **NOT SUPPORTED at L218**; PARTLY for site location | Report has no 1980s-2010s chloride time series; ~15 to >40 mg/L is from kelly2008 (1986-2005) |
| ruxton2006 | yes | yes | SUPPORTED | |
| runkel2013 | yes | yes | SUPPORTED | Temporal variation is a named uncertainty source in synoptic profiles |
| nimiroski2002 | yes | report number missing | SUPPORTED | Deicing was >90% of chloride input, Scituate basin, RI |
| marti2025 | yes | article no. missing | SUPPORTED | K contrast controls recharge partitioning; faults shape seepage areas |
| cook2022 | yes | yes | SUPPORTED | Head/14C transects across 3 faults; barrier tests |
| greco2023 | yes | yes | SUPPORTED | Online 2021, print 2023 |
| **mcclymont2023** | yes | yes | **NOT SUPPORTED** | Abstract: "warming elicited little response". It does not show warming compounding chloride |
| ferrill2025 | yes | OK (number "Special 15" missing) | SUPPORTED | Uranine moved along the fault at up to 1993 m/d; K anisotropy >7x |
| orr2026 | yes | yes | SUPPORTED | Spring Creek PA karst; Cl highest in summer baseflow |
| perera2013 | yes | yes | PARTLY | Shows accumulation under continued application, not persistence after application stops |
| adirondack2023 | yes | yes | PARTLY | Calibration, anti-icing brine, application rates and training are in the report; "pre-wetting" is not |

**Counts (41 keys):**

| Verdict | Count |
|---|---|
| Real | 41 of 41 |
| Bib entries with a substantive error | 1 (dugan2023 authors) |
| Bib entries with minor omissions | ~8 (missing issue, article or report number; budnik booktitle) |
| SUPPORTED | 26 |
| PARTLY | 11 (tiwari2018, rivett2016, kaushal2023factors, miller2014, mullaney2009, perera2013, adirondack2023, kaushal2005/williams1999 at L61, manda2008 in the letter only, kelly2019 site location) |
| NOT SUPPORTED | 3 (schalk2012, kelly2019 at L218, mcclymont2023) |
| COULD NOT VERIFY | 1 (jamshidi2020) |

Some keys are counted under both their main verdict and a secondary PARTLY use.

## Per-key detail (keys with problems), most serious first

### 1. schalk2012: NOT SUPPORTED (abstract L52, Introduction L63, Discussion L224)

**Manuscript text:**

- L63: "in Maine, \citet{schalk2012} documented four road-salt-contaminated bedrock wells along a fault zone, traced to a roadway running along the fault's trace, with elevated specific conductance in both summer and winter, so salt-laden water persisted in the fault zone year-round."
- L224: "contaminated bedrock wells lay along a fault zone beside a road that followed the fault trace ... with a road directly above the structure".
- L52 (abstract, uncited): "road-salt-contaminated wells have been found along a fault zone beside a highway".

**What the source says (full SIR 2012-5205 PDF read):**

- The four wells are in three towns:
  - Gray, in muscovite-biotite granite, 40 ft from Routes 26/100.
  - West Gardiner, in Waterville Formation slate/schist, near an I-95 tollbooth and a MaineDOT salt-pile yard.
  - North and South Sullivan, in Ellsworth Formation quartz granofels, 25 and 150 ft from US Route 1.
- Wells were selected for open-hole bedrock completion, known salt contamination, owner permission and location along a state road (p. 4, Table 1).
- The word "fault" appears once in the report, in general background: "Zones of highest-yielding bedrock wells in the State coincide with locations of faults and other geologic structures" (p. 4).
- No well is described as lying along a fault zone. No road is described as following a fault trace.
- What the report does show:
  - Salt is transported through *active bedrock fractures*.
  - Specific conductance was elevated throughout the year, including after summer recharge.
  - The well nearest the road responded most to thaws.

The error was carried over from the docx (`original.tex` L62 has the same wording). This is the paper's stated "most direct evidence that faults carry road salt," so the framing needs an author decision.

**Proposed fix (minimal):**

- **L63:** "in Maine, \citet{schalk2012} showed that road salt reached four bedrock wells beside state roads through active bedrock fractures, with specific conductance elevated throughout the year, including after summer recharge." Then drop "so salt-laden water persisted in the fault zone year-round". Change "The most direct evidence that faults carry road salt" to something like "Evidence that fractured bedrock carries road salt".
- **L224:** Rewrite to say the closest evidence is fracture-borne road salt in bedrock wells near roads, without a fault.
- **Abstract:** Change to "road-salt-contaminated bedrock wells have been linked to transmissive fractures beside highways".
- The letter has no Schalk statement, but if R1.4 or R1.13 is ever expanded to say faults "carry road salt," correct it there too.

### 2. mcclymont2023: NOT SUPPORTED (L222)

**Manuscript text:** "...toward levels that restructure plankton communities \citep{greco2023} and act with warming to compound those effects \citep{mcclymont2023}."

**What the source says (abstract):** "Although warming elicited little response, increasing chloride concentrations led to reduced zooplankton biomass and richness, even at concentrations below the CWQG, and an increase in cyanobacteria abundance". The paper tested interaction with +2.7 °C warming and found little.

**Fix:** "...restructure plankton communities, reducing zooplankton biomass and richness below current Canadian guidelines \citep{greco2023,mcclymont2023}." Drop "act with warming to compound those effects."

### 3. kelly2019: NOT SUPPORTED at L218; PARTLY for the monitoring location (L95, L148, L163)

**Manuscript text (L218):** "Long-term records show that stream chloride in this reach has risen from annual means of roughly 15 mg/L in the 1980s to over 40 mg/L by the 2010s \citep{kelly2019}".

**What the source says:**

- Kelly, Findlay & Weathers 2019 (16-page Cary report, every page rendered) contains:
  - a US road-salt-use bar chart;
  - a *monthly-average* sodium and chloride chart for the East Branch at Cary (1986-2017 pooled), with chloride ~27-35 mg/L;
  - a pie diagram (90% road salt, 3% softeners, 3% sewage).
- It has no annual time series and no 1980s or 2010s values.
- Kelly et al. 2008 does have the trend: 1.5 mg/L/yr from 1986 to 2005, with concentrations "about three times higher in 2005 than ... 1986" (≈14 → ≈43 mg/L). It stops at 2005.

**Fix:** "...risen from roughly 15 mg/L in the mid-1980s to over 40 mg/L by the mid-2000s \citep{kelly2008}". Keep kelly2019 only if a 2010s value is actually taken from another source.

**Monitoring location:** Kelly 2019 names the site only as "Wappinger Creek at Cary Institute". Kelly 2008 gives coordinates (N41.786 W073.741, Cary Arboretum). Consider citing kelly2008 alongside kelly2019 at L95 for the site position.

### 4. dugan2023: bib author list wrong

Crossref lists two authors: Dugan, Hilary A. and Arnott, Shelley E. The bib has `Dugan, H. A. and others`, which renders as "et al." for a two-author paper. The project's "and others" convention does not apply here.

**Fix:** `author = {Dugan, H. A. and Arnott, S. E.}`.

The claim at L59 (salinization threat across cold-climate fresh waters) is SUPPORTED.

### 5. jamshidi2020: COULD NOT VERIFY (L59)

**Manuscript text:** "It is often applied in amounts beyond what de-icing requires \citep{jamshidi2020}."

**What the source says:** The abstract (AGRIS) covers groundwater contamination in Malayer and Hamedan, Iran. Hamedan uses ~10× more salt, and Hamedan wells show rising contamination. It recommends new winter-maintenance approaches. It does not state that salt exceeds de-icing requirements. The full text (Springer) was not reachable.

**Fix:** Either confirm a specific sentence in the full text, or attribute the claim to a source that says it. Kelting & Laxson 2010 recommend tailoring application rates; Kelly et al. 2019 (p. 11) say adding too much salt is a waste. Otherwise soften to "Application rates vary widely between jurisdictions \citep{jamshidi2020}."

### 6. mullaney2009: PARTLY (L69, L236; also quoted in the letter at R1.3)

**L69:** "chloride-to-bromide ratios, which are the standard fingerprint of deicing salt".

- Mullaney uses Cl:Br versus Cl against binary mixing curves for several sources. That supports "a widely used tracer", not "the standard fingerprint".
- **Fix:** "...chloride-to-bromide ratios, which are widely used to distinguish deicing salt from other chloride sources \citep{mullaney2009}." The R1.3 quotation in the letter must change to match.

**L236:** The cited part ("ratios above 1,000 at chloride above 100 mg/L marked halite-dominated waters in the northern glacial-aquifer system") is SUPPORTED. Note that these were groundwater samples from shallow monitoring wells.

- The follow-on clause "since sewage mixtures are common at lower ratios" misreads the abstract. The abstract says the halite-dominated samples "commonly contained mixtures that indicated input from sewage or animal waste".
- **Fix:** "...and a different ratio, although even halite-dominated samples commonly contain sewage or animal-waste mixtures \citep{mullaney2009}."

### 7. kaushal2023factors: PARTLY (L65, L222)

**Manuscript text:** "geology and hydrologic flowpaths are first-order controls on where salt reaches streams".

**What the source says:** The paper *hypothesizes* five interacting "state factors" (human activities, geology, flowpaths, climate, time) that drive the spread and stages of freshwater salinization syndrome. Geology there mainly drives weathering, ion exchange and alkalinization.

**Fix:** "...in which geology and hydrologic flowpaths are among five proposed state factors driving salinization \citep{kaushal2023factors}" (L65). Make the same change at L222.

### 8. miller2014: PARTLY (L69, pred2; quoted in the letter at R1.3)

**Manuscript text:** "when direct runoff is absent and groundwater supplies much of the streamflow at low flow".

**What the source says:** In 14 Upper Colorado River Basin rivers (>1000 km², snowmelt-dominated), baseflow was 40-86% of discharge in low-flow conditions. It says nothing about direct runoff being absent, and the setting is not the Northeast.

**Fix:** "...when groundwater-fed baseflow supplies much of the streamflow at low flow \citep{miller2014}". Optionally add "in other settings". Update the letter quote to match.

### 9. perera2013: PARTLY (L240)

**Manuscript text:** "Salt entering streams through groundwater will continue for years after application ceases, because of long groundwater transit times \citep{perera2013}."

**What the source says:** Perera et al. show up to 40% of applied chloride entering the shallow aquifer and baseflow chloride rising toward ~505 mg/L *if current application continues*. Persistence after salting stops is not in the abstract.

Jackson & Jobbágy 2005 states it directly: "it typically will take decades to centuries for the salts to disappear, even when road salt use ends."

**Fix:** Cite `\citep{perera2013,jackson2005}`, or rephrase the Perera part as "...because salt accumulates in shallow aquifers \citep{perera2013}".

### 10. kaushal2005 and williams1999 at L61: PARTLY

**Manuscript text:** "...with long-term increases documented globally \citep{williams1999,kaushal2005}". Kaushal covers the NE US; Williams covers Toronto groundwater.

**Fix:** "...documented in the northeastern United States and Canada".

### 11. tiwari2018 and jackson2005 at L59: PARTLY

**Manuscript text:** "used as a de-icing agent in North America and Europe since the early 1940s, and its use has climbed steadily decade over decade".

**What the sources say:** Jackson 2005 gives US highway salt sales from 1940 (149,000 Mg) to ~18 million Mg, a hundredfold rise. The Tiwari & Rachlin abstract is general; the full text was not reached, so "Europe" is unconfirmed.

**Fix:** Either verify that Tiwari mentions Europe, or say "in the United States since the 1940s".

### 12. rivett2016: PARTLY (L61)

**Manuscript text:** "As road salt has infiltrated groundwater over recent decades \citep{rivett2016}".

**What the source says:** Rivett et al. quantify stream leakage of highway salt to groundwater over two severe UK winters (21-54% of increased chloride). That supports infiltration, not a multi-decade trend.

**Fix:** "As road salt infiltrates groundwater \citep{rivett2016}" (drop "over recent decades"). Alternatively add vanmeter2024, which has a 30-year record.

### 13. adirondack2023: PARTLY (L240)

**Manuscript text:** "lower application rates, calibrated equipment, pre-wetting, brine-based anti-icing and staff training".

**What the source says:** The report (30 pp., 2023) covers calibration, brine anti-icing, Direct Liquid Application, training and application rates. A full-text search finds no "pre-wet" or "pre-treat".

**Fix:** Drop "pre-wetting", or add \citep{kelly2019} (p. 8 lists pre-wetting).

### 14. manda2008: OK in the manuscript; PARTLY in the letter

The manuscript (L63, L222) correctly describes foliation-parallel fractures. Letter R1.4 lists it among "studies of fault-controlled flow in fractured metamorphic bedrock".

**Fix (letter):** "studies of structurally controlled flow in fractured metamorphic bedrock (Manda et al., 2008; Kim et al., 2014)".

### 15. Minor bib completeness (no wrong values)

| key | missing or minor |
|---|---|
| nimiroski2002 | `number = {2002-4149}` (USGS WRIR 2002-4149; authors Mark Nimiroski and Marcus Waldron confirmed) |
| marti2025 | `pages = {e2024WR037474}` |
| ferrill2025 | `number = {Special 15}`, `pages = {lithosphere_2024_178}` (Crossref: vol. "2024", issue "Special 15", issued 2025) |
| kaushal2023saltcycle | `number = {11}` |
| jackson2005 | `number = {41}` |
| kaushal2005 | `number = {38}` |
| kelly2008 | `number = {2}` |
| tiwari2018 | `number = {1}` |
| budnik2010 | booktitle "Natural Resources Inventory" vs. the chapter header "Natural Resource Inventory of Dutchess County, NY"; use the singular |
| kelly2008 author list | Crossref has 7 authors, the 7th being Likens; "and others" after Burns is fine |
| budnik2010 publisher | "Cornell Cooperative Extension Dutchess County" is not stated in the chapter PDF; plausible but unverified |

## Claims checked and SUPPORTED (brief notes)

- **budnik2010:**
  - L77 quote: "The location of and sense of motion on the faults is largely conjectural since the faults themselves are rarely exposed at the surface." This is p. 18, and the quoted fragment is exact. Context: the sentence closes a paragraph about the Fig. 3.11 cross-section faults, but it is phrased generally ("the faults").
  - Fig. 3.10 "Map of faults within Dutchess County" is p. 16. Its legend reads "High Angle Fault", "Thrust Fault Area", and the scale is labelled "1:340,000".
  - L79 (low-angle thrusts plus high-angle reverse faults, Taconic Orogeny, metamorphosed shale/sandstone) is supported by pp. 13-18.
- **kelly2008 (L216):** All figures are exact:
  - road salt 83%, parking 8%, sewage 4%, softeners 3%;
  - weathering 1%, estimated from a single 0.6 mg/L chloride value from 1905;
  - Millbrook STP "approximately 3 km upstream from the sampling site".
- **kelly2008 (L61):** "summertime concentrations were high and increasing, suggesting a slow release ... from groundwater". SUPPORTED.
- **nimiroski2002:** "Deicing of State and local roads was the largest source"; >90% of chloride. SUPPORTED.
- **kelting2010 (L240):** "Identify Salt Sensitive Areas: groundwater recharge areas, wetlands, shallow water tables, drinking water sources" is near-verbatim. Corrosion of vehicles and infrastructure is covered in §7. SUPPORTED.
- **ruxton2006:** Recommends the unequal-variance test "always" in preference to Student's or Mann-Whitney, including with unequal n. SUPPORTED.
- **ferrill2025 (L224):** Glen Rose Formation (Trinity Aquifer) carbonates; dye moved along the fault zone at up to 1993-2596 m/d. SUPPORTED.
- **orr2026 (L226):** Spring Creek watershed, PA; 15 streams and 8 springs; Cl highest in summer baseflow. SUPPORTED.

## Letter-specific issues (response_to_reviewers.tex)

1. **R1.14 (L392-393):** "Kelting et al., 2010" should be "Kelting & Laxson, 2010" (two authors).
2. **R1.3 (L150-155):** The letter quotes two manuscript phrases that this audit asks to reword: "are the standard fingerprint of deicing salt" (mullaney2009) and "when direct runoff is absent ..." (miller2014). Update the quotes after the manuscript changes.
3. **R1.4 (L163-164):** "studies of fault-controlled flow in fractured metamorphic bedrock (Manda et al., 2008 ...)" overstates Manda (foliation-parallel fractures). See item 14.
4. **R1.4 (L166-168):** "We also removed the karst example from the Introduction ... the Discussion mentions it once". This is now consistent with revisions.tex after commit fc6952a (ferrill2025 only at L224, `L:disc-karst`).
5. **Budnik quote (L474-476):** The wording and p. 18 are exact. "printed at about 1:340,000" matches the Fig. 3.10 scale label.
6. **R1.12 (L352-354):** "about 4% of the sodium chloride input to sewage (septic systems and the plant together)" is SUPPORTED by Kelly et al. 2008 ("sewage (septic and sewage treatment plant)").
7. **Other author-year citations:** These are consistent with the bib: Caine et al. 1996; Bense et al. 2013; Genereux 1998; Orr & Boyer 2026; Harte & Trowbridge 2010; Hodgins et al. 2024, 2026; Miller et al. 2014; Mullaney et al. 2009; Kim et al. 2014; Kelly et al. 2008, 2019.
8. **Bense et al. 2008:** Still named in the letter as removed. It is correctly uncited in revisions.tex.

## Year mismatches

- **williams1999:** The key says 1999, but the bib year is 2000, which is correct per Crossref (Water Research 34(1), 2000). Numeric citations show no year, so readers see no mismatch. The key name is only cosmetic.
- **Print vs. online years:** The bib uses the print year where Crossref's online year is earlier:
  - kelly2008 (online 2007)
  - kaushal2023factors (online 2022)
  - dugan2023 (online 2022)
  - mcclymont2023 (online 2022)
  - greco2023 (online 2021)
  - hodgins2026 (online 2025)

  This is consistent and acceptable.
- No in-text year disagrees with the bib.

## Share of cited references from 2022-2026

The 41 cited keys include these 15 dated 2022-2026 (bib/print year): adirondack2023, cook2022, dugan2023, ferrill2025, greco2023, hintz2022, hodgins2024, hodgins2026, kaushal2023factors, kaushal2023saltcycle, marti2025, mcclymont2023, orr2026, shattuck2023, vanmeter2024.

**15 / 41 = 36.6% (confirmed).**

- If the editor counted Crossref first-online year instead, greco2023 (2021) would drop out: 14/41 = 34.1%, still ≥30%.
- If mcclymont2023 were removed instead of reworded, the share would be 14/40 = 35.0%.

## Uncited entries in references_revised.bib (19)

bubeck1971, robinson2017, forman1998, richburg2001, ramakrishna2005, foos2003, bredehoeft1992, gudmundsson2000, bense2008, willmert2018, ledford2016, mabee2002, kimball2002, selker2006, panno2006, kronholm2015, cook2006, granato2015, waltonday2021.

`unsrtnat` prints only cited entries, so these do not appear in the reference list. Their metadata was not audited.
