# WP2 literature verification (2026-11-07)

Output bib: `references_revised.bib` (41 original entries + 19 new = 60). `references.bib` is unchanged.

Method: every DOI was resolved against the Crossref record (authors, year, title, journal, volume, pages, DOI) or the USGS Publications Warehouse page, and the abstract was read from a publisher, USGS, OpenAlex or repository copy. Entries whose abstract was not fully readable are flagged. Publisher sites (ScienceDirect, USGS via WebFetch, ADS) block automated access, so some abstracts came from OpenAlex or USGS HTML fetched with curl.

## 1. New references, by task

### R1.4 Fault hydrogeology in crystalline and metamorphic bedrock (Intro P-fault paragraph, Discussion 4.3)

| Key | Citation | Opened | Supports |
|---|---|---|---|
| caine1996 | Caine, Evans & Forster 1996. Fault zone architecture and permeability structure. Geology 24(11):1025. | doi 10.1130/0091-7613(1996)024<1025:FZAAPS>2.3.CO;2 (Crossref + abstract via OpenAlex) | Fault zones act as conduits, barriers or combined systems depending on the share of fault core vs damage zone; a framework, not a site result. Use for "faults can be conduits" with that caveat. |
| bense2013 | Bense, Gleeson, Loveless, Bour & Scibek 2013. Fault zone hydrogeology. Earth-Sci. Rev. 127:171-192. | doi 10.1016/j.earscirev.2013.09.008 (Crossref + UEA repository record). **Abstract read only through search-engine excerpts of the ADS abstract; ScienceDirect and ADS blocked automated access.** | Fault zones are conduit-barrier systems (along-fault flow favoured, across-fault flow hindered); review covers clastic, carbonate, crystalline and volcanic rocks; the effect of a given fault needs its hydrogeological context. |
| kim2014 | Kim, Ryan, Klepeis, Gleeson, North, Bean, Davis & Filoon 2014. Tectonic evolution of a Paleozoic thrust fault influences the hydrogeology of a fractured rock aquifer, northeastern Appalachian foreland. Geofluids 14(3):266-290. | doi 10.1111/gfl.12076 (Crossref + abstract) | In Vermont, the Hinesburg thrust (metamorphic hanging wall over sedimentary footwall) affects well yield and chemistry; wells drilled closest to the thrust have the highest median yields. Closest regional analogue: Appalachian foreland, metamorphosed clastic rock. Not about road salt. |
| manda2008 | Manda, Mabee & Wise 2008. Influence of rock fabric on fracture attribute distribution and implications for groundwater flow in the Nashoba Terrane, eastern Massachusetts. J. Struct. Geol. 30(4):464-477. | doi 10.1016/j.jsg.2007.12.006 (Crossref; abstract via UMass Geological Survey listing) | In New England metamorphic and igneous rock, foliation-parallel fractures can raise connectivity and add flow anisotropy. Supports fracture-controlled flow in metamorphic bedrock. |
| mabee2002 | Mabee, Curry & Hardcastle 2002. Correlation of lineaments to ground water inflows in a bedrock tunnel. Ground Water 40(1):37-43. | doi 10.1111/j.1745-6584.2002.tb02489.x (Crossref + abstract) | In foliated metamorphic bedrock in eastern Massachusetts, 13 of 19 tunnel flow zones (68%) correlate with coincident lineaments; the authors caution that predicting which lineaments transmit water is difficult. Use as evidence both for and against mapped structures as flow paths. |

No verified 2022-2026 fault-flow study in northeastern metamorphic rock was found. `cook2022` (age tracers, below) and the existing `marti2025` are the recent fault-hydrology references.

### R1.3 Support for the three predictions (Intro, Methods 2.x)

| Key | Citation | Opened | Supports |
|---|---|---|---|
| kimball2002 | Kimball, Runkel, Walton-Day & Bencala 2002. Assessment of metal loads in watersheds affected by acid mine drainage by using tracer injection and synoptic sampling: Cement Creek, Colorado. Appl. Geochem. 17(9):1183-1207. | doi 10.1016/S0883-2927(02)00017-3; USGS page 70024356 (abstract read) | (i) Spatially detailed synoptic profiles locate inflows; dispersed subsurface inflow occurred mostly where bedrock was heavily fractured. Mine-drainage context, not salt. |
| harte2010 | Harte & Trowbridge 2010. Mapping of road-salt-contaminated groundwater discharge and estimation of chloride load to a small stream in southern New Hampshire, USA. Hydrol. Process. 24(17):2349-2368. | doi 10.1002/hyp.7645 (Crossref + abstract) | (i), (iii) and R1.13. Electromagnetic mapping of the streambed during base flow found reaches where high-conductivity groundwater discharged, matching high shallow-groundwater specific conductance. Also a direct precedent for locating road-salt groundwater inputs along a stream. |
| hodgins2026 | Hodgins, Roy & Robinson. Influence of groundwater discharge on stream chloride concentrations in mixed urban land use sub-watersheds receiving road salt applications. J. Hydrol. 665:134757. | doi 10.1016/j.jhydrol.2025.134757 (Crossref + abstract). **Year: Crossref issue/print year 2026 is used in the bib; OpenAlex lists 2025 (online).** | (i), (ii), R1.13, R2.1. Negative concentration-discharge slopes in summer indicate groundwater is likely the dominant chloride source; longitudinal chloride and radon-222 show local groundwater inputs and land use drive spatial variation; dilution in larger streams lessened the groundwater effect. |
| hodgins2024 | Hodgins, Robinson, Power & Roy 2024. Road salt chloride exposure in urban streambeds and links to groundwater-surface water interactions and salt sources. Sci. Total Environ. 957:177488. | doi 10.1016/j.scitotenv.2024.177488 (Crossref; abstract via Semantic Scholar) | R1.13 and (i). Streambed conductivity mapping and temperature mapping on 100-m reaches show chloride in porewater varying from under 100 to over 5000 mg/L over 10 m or less. Supports small-scale spatial variability of salt-laden discharge. |
| selker2006 | Selker et al. 2006. Distributed fiber-optic temperature sensing for hydrologic systems. Water Resour. Res. 42(12), article id 2006WR005326 (Crossref); the bib omits pages. | doi 10.1029/2006WR005326 (Crossref + abstract) | (i) Distributed temperature sensing is a tool with 1-m spatial resolution along a stream; supports the "dense longitudinal temperature survey" part of prediction (i) and the test design. |
| miller2014 | Miller, Susong, Shope, Heilweil & Stolp 2014. Continuous estimation of baseflow in snowmelt-dominated streams and rivers in the Upper Colorado River Basin: a chemical hydrograph separation approach. Water Resour. Res. 50(8):6986-6999. | doi 10.1002/2013WR014939 (Crossref + abstract) | (ii) Specific conductance is used to separate baseflow; baseflow was 40-86% of discharge in low-flow conditions in Upper Colorado streams. Indirect support for late-season baseflow being groundwater-dominated, in a different climate. |
| panno2006 | Panno, Hackley, Hwang, Greenberg, Krapac, Landsberger et al. (7 authors on Crossref; full list in bib). Year in bib: 2006. Characterization and identification of Na-Cl sources in ground water. Ground Water 44(2):176-187. | doi 10.1111/j.1745-6584.2005.00127.x (Crossref + abstract). Crossref online year 2005; print volume year 2006 used. | (iii) Cl/Br ratios (against Cl) separate Na-Cl sources, with overlapping groups. |
| mullaney2009 | Mullaney, Lorenz & Arntson 2009. Chloride in groundwater and surface water in areas underlain by the glacial aquifer system, northern United States. USGS SIR 2009-5086. | doi 10.3133/sir20095086; USGS page (full abstract read) | (iii) Cl:Br above 1,000 with Cl above 100 mg/L was dominated by halite, with sewage and animal-waste mixtures common. Base-flow chloride predicted maximum measured chloride. |
| granato2015 | Granato, DeSimone, Barbaro & Jeznach 2015. Methods for evaluating potential sources of chloride in surface waters and groundwaters of the conterminous United States. USGS OFR 2015-1080. | doi 10.3133/ofr20151080; USGS page (abstract read) | R1.12 and test design. Non-deicing chloride sources (wastewater, fertilizer, etc.) and how to use water and solute budgets to identify sources. |

### R2.1 Tributary confluence mixing (Intro)

| Key | Citation | Opened | Supports |
|---|---|---|---|
| genereux1998 | Genereux 1998. Quantifying uncertainty in tracer-based hydrograph separations. Water Resour. Res. 34(4):915-919. | doi 10.1029/98WR00010 (Crossref + abstract) | Two-component mixing: the mixing fraction follows from tracer concentrations in the end members. Supports the mixing principle only; the paper is about hydrograph separation, not confluences. |
| kronholm2015 | Kronholm & Capel 2015. A comparison of high-resolution specific conductance-based end-member mixing analysis and a graphical method for baseflow separation of four streams in hydrologically challenging agricultural watersheds. Hydrol. Process. 29(11):2521-2533. | doi 10.1002/hyp.10378 (Crossref + abstract). Crossref online year 2014; print year 2015 used. | Specific conductance end-member mixing works only when end members differ in conductance and relate monotonically to flow; limits of the approach. |

Neither is confluence-specific. `hodgins2026` (dilution in larger streams) and `kimball2002` (tributary inflows in a synoptic mass balance) are the closest to a salinization or synoptic context. The mixing equation itself is textbook (flow-weighted average), so cite these for the principle, not for a confluence result.

### R1.13 Comparison with other longitudinal surveys

orr2026, harte2010, hodgins2026, hodgins2024 (above). `orr2026` metadata verified: Orr & Boyer, Environ. Res. Commun. 8(5):055036, doi 10.1088/2515-7620/ae6035. It analyses 1999-2020 Cl and Na from 15 streams and 8 springs in the Spring Creek watershed, Pennsylvania; summer baseflow chloride was highest and long-term increases scaled with baseflow index; it is a karst watershed.

### Test design (survey timing and age tracers)

| Key | Citation | Opened | Supports |
|---|---|---|---|
| cook2022 (existing, corrected) | Cook, Banks, Marshall, Harrington, Batlle-Aguilar, Dogramaci & Turnadge 2022. Inferring fault hydrology using groundwater age tracers. J. Hydrol. 610:127905. | doi 10.1016/j.jhydrol.2022.127905 (Crossref; abstract summary via AGRIS record; full text not read) | Head and 14C age transects across three faults tested whether faults block or channel flow; dense sampling is required. Supports the age-tracer element of the test design. |
| runkel2013 | Runkel, Walton-Day, Kimball, Verplanck & Nimick 2013. Estimating instream constituent loads using replicate synoptic sampling, Peru Creek, Colorado. J. Hydrol. 489:26-41. | doi 10.1016/j.jhydrol.2013.02.031; USGS page 70044991 (abstract read) | Temporal variation in concentration (diel cycles or source change) is a source of uncertainty in synoptic profiles; replicate synoptic runs are used to put error bars on them. Supports the two-day-offset pitfall. |
| waltonday2021 | Walton-Day, Runkel, Smith & Kimball 2021. Quantification of metal loading using tracer dilution and instantaneous synoptic sampling and importance of diel cycling in Leavenworth Creek, Colorado, 2012. USGS OFR 2021-1078. | doi 10.3133/ofr20211078; USGS page (abstract read) | Diel concentration cycles of 26-33% for zinc led the authors to sample all stream sites at 1200 h on one day. Supports same-day sampling. |
| cook2006 | Cook, Lamontagne, Berhane & Clark 2006. Quantifying groundwater discharge to Cockburn River, southeastern Australia, using dissolved gas tracers 222Rn and SF6. Water Resour. Res. 42(10), article id 2006WR004921. | doi 10.1029/2006WR004921 (Crossref + abstract) | Radon-222 along a river estimates groundwater inflow; ignoring hyporheic exchange would overestimate inflow by about 70%. Supports radon as a test-design tracer. |

Pitfall nature: all three synoptic papers come from mine-drainage studies, so they support the sampling principle, not salinity results.

## 2. DOI and report-number fixes (R1.14)

Added to `references_revised.bib` (each checked against its record):

| Key | Added |
|---|---|
| jamshidi2020 | doi 10.1007/s11356-020-09261-7 |
| shattuck2023 | doi 10.1002/lol2.10306 |
| kaushal2005 | doi 10.1073/pnas.0506414102 |
| richburg2001 | doi 10.1672/0277-5212(2001)021[0247:EORSAP]2.0.CO;2 |
| willmert2018 | doi 10.1016/j.jenvman.2018.07.085 |
| bredehoeft1992 | doi 10.1306/BDFF8862-1718-11D7-8645000102C1865D |
| schalk2012 | USGS SIR 2012-5205, doi 10.3133/sir20125205 (USGS page opened) |
| budnik2010 | No DOI. Chapter 3 of the Natural Resource Inventory of Dutchess County (Budnik, Walker & Menking, May 2010), URL https://www.dutchessny.gov/Departments/Planning/Docs/nrichapthree.pdf (PDF opened, authors confirmed) |
| kelly2019 | No DOI. URL https://www.caryinstitute.org/sites/default/files/downloads/report_road_salt.pdf (PDF opened: 16 pages, authors Kelly, Findlay, Weathers) |
| kelting2010 | No DOI. Report AWI2010-01 (per search results; the report PDF itself was not opened), URL on adkwatershed.org |
| adirondack2023 | No DOI. URL https://extapps.dec.ny.gov/docs/administration_pdf/adirondackroadsaltreport.pdf (PDF opened: 30 pages, "2023") |

Not independently confirmed: the AWI2010-01 report number (from search results only) and the Bredehoeft DOI suffix (from Crossref only; the AAPG page was not opened).

## 3. Metadata problems in existing entries

- **cook2022**: DOI 10.1016/j.jhydrol.2022.127959 and article 127959 belong to a different paper (a tile-drainage rainfall-runoff study). Corrected to 127905. The bib already lists all seven authors, including Turnadge, matching Crossref order.
- **dugan2023**: issue was 4; Crossref gives issue 2.
- All other entries with DOIs matched Crossref on volume, pages and year (checked programmatically). Notes: `williams1999` has key year 1999 but year field 2000, correct per Crossref (print 2000). `kelly2008`: Crossref online year 2007, print year 2008 (bib 2008, correct). `kaushal2023factors`, `dugan2023`, `mcclymont2023`, `greco2023` have online years 2021-2022 and print year 2023 in Crossref; the bib uses 2023.
- `nimiroski2002`: USGS WRIR 2002-4149, doi 10.3133/wri024149 confirmed on the USGS page.
- `schalk2012` title: the bib adds "in Maine" and "Maine"; the USGS title is "...in four road-salt-contaminated wells in Maine, 2007-9" (bib text matches).
- Not checked beyond Crossref resolution: contents of the existing reviews and ecology papers.

## 4. Unverified candidates (not added)

- Cook, Love, Robinson & Simmons 2005, Groundwater ages in fractured rock aquifers, J. Hydrol. 308:284-301, doi 10.1016/j.jhydrol.2004.11.005: metadata matched on Crossref, but no abstract found.
- Roques et al. 2014, Hydrological behavior of a deep sub-vertical fault in crystalline basement, J. Hydrol. 509:42-54, doi 10.1016/j.jhydrol.2013.11.023: no abstract found.
- Gleeson & Novakowski 2009 (GSA Bull. 121:333): Canadian Shield lineaments; not northeastern US and the abstract was not cleanly read.
- Boutt, Diggins & Mabee 2010 (Hydrogeol. J. 18:1839): Massachusetts crystalline rock flow depth; no abstract obtained.
- Mabee 1999 (Ground Water 37:88): abstract read, but well productivity rather than fault flow; left out.
- Kimball & Runkel 2009 and Kimball 2010 synoptic papers: not opened.
- Kobayashi 1986 (conductance hydrograph separation): not opened.
- A Merced-San Joaquin confluence salinity mass-balance paper and Los Angeles River mixing paper surfaced in search; neither was located in Crossref or opened.
- No reference found for "late-season baseflow in the Hudson Valley is groundwater-dominated" specifically.
- `bense2013` abstract: see section 1.

## 5. Kelly et al. 2008 (Environ. Sci. Technol. 42(2):410-415, doi 10.1021/es071391l)

Read from the Cary Institute reprint PDF (https://www.caryinstitute.org/sites/default/files/public/reprints/Kelly_et_al_EST_2008.pdf).

- Abstract: "salt used for deicing accounted for 91% of the sodium chloride input to the watershed, while sewage and water softeners accounted for less than 10% of the input."
- Results text: "municipal roadway anti-icing salt contributed 83% and parking area anti-icing salt contributed 8%"; "Sewage contributed 4% and water softeners contributed 3%"; "Only 2% of sodium and chloride was from atmospheric deposition and rock weathering. Thus 98% ... was anthropogenic."
- Table 1 (kg/yr, 1986-2005 average): road salt 1,180,231 (83%); parking area salt 113,094 (8%); sewage 52,414 (4%); water softeners 43,594 (3%); wet deposition 18,319 (1%); rock weathering 13,717 (1%); dry deposition 442 (<1%); total 1,421,811.
- Site: East Branch of Wappinger Creek, 6243 ha, sampled monthly at the Cary Arboretum (Millbrook); 91% forested or open field, 9% residential and commercial; 136 km of road. "The Millbrook sewage treatment plant is approximately 3 km upstream from the sampling site." About 44% of residents use private wells and septic systems; the rest use the village water supply and sewer.
- Weathering method: not measured; derived from a single chloride value of 0.6 mg/L from 1905, with wet and dry deposition subtracted.
- Main conclusion: increases in concentration and export are attributed to a storage (lag) effect of long-term road salt use; sewage and softener increases explain only about 1% of the export increase.

Mismatches with the current text in `revisions.tex` (section "Addressing possible alternative sources", about line 176):

1. "Road salt contributes to 83%" is the municipal roadway share only. Total deicing salt is 91% (roadway 83% plus parking-area 8%); the text should say which it means.
2. The text does not mention the wastewater treatment plant. The paper places it about 3 km upstream of its sampling site, and sewage (plant plus septic) is 4%.
3. "Rock weathering accounts for only 1%" is an estimate from one 1905 chloride value, and atmospheric deposition adds another 1% (2% together); it was not measured. The text also says bedrock is "known to have minimal influence"; the paper does not make that claim about the bedrock.
4. The study area is the East Branch watershed at the Cary Arboretum. The revisions text calls it "a portion of our study site"; the author should check that the surveyed reaches lie in or downstream of the East Branch, and whether any are below the treatment plant, before using the 83%/1% figures as local numbers.

## 6. Recent-reference share (2022-2026)

- Bib as it would stand if every entry were cited: 60 entries, 15 dated 2022-2026 = **25.0%**. The 15 are adirondack2023, cook2022, dugan2023, ferrill2025, greco2023, hintz2022, hodgins2024, hodgins2026, kaushal2023factors, kaushal2023saltcycle, marti2025, mcclymont2023, orr2026, shattuck2023, vanmeter2024.
- References currently cited in `revisions.tex` (all 41 original entries) plus the 19 new ones: the same 60, so also **25.0%** (15 of 60).
- The new references add only two 2022-2026 entries (hodgins2024, hodgins2026). To reach 30% (18 of 60) three more verified 2022-2026 references would be needed, or fewer older ones cited. None is in this file because none was verified.
