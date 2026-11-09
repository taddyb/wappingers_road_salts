# Positional accuracy of the Budnik et al. (2010) Fig. 3.10 fault traces

Research notes. Everything below was read on the opened PDFs/pages listed under "URLs opened". Page numbers are the printed page numbers of the chapter PDF (printed page = PDF page for this document, 1-35) unless stated.

## 1. Does the chapter state positional accuracy, uncertainty, or mapping scale?

**No accuracy or uncertainty statement exists** anywhere in the 35-page chapter (searched full text for "accura", "uncertain", "scale", "approximate", "source", "compiled", "digital", "data").

Scale information that does exist:
- Fig. 3.10 (p. 16) carries only a graphic scale bar plus the label "1:340,000" (read from the rendered page image). Its legend has two entries, "High Angle Fault" and "Thrust Fault Area". The caption is just "Figure 3.10: Map of faults within Dutchess County". There is no credit line, no source note, and no accuracy note on the page.
- Map 3.1, Bedrock Geology (p. 32): "Prepared by: CCEDC GIS Lab, 2010 ... 1:225,000". The other Maps (3.2-3.4) are also credited "CCEDC GIS Lab, 2010". Fig. 3.10 itself is not credited to the GIS Lab.
- Text on Map 3.1 (p. 15): "A simplified view of the bedrock types found in Dutchess County is shown in Map 3.1" (p. 9) and "Areas of similar bedrock types are inferred to be bounded by faults that separate them from areas of differing bedrock types." (p. 15).

So 1:340,000 is the *display* scale of Fig. 3.10, not a stated compilation scale.

## 2. Source of the faults in Fig. 3.10

**The chapter does not name a source for Fig. 3.10.** Checked: caption (p. 16), the text that cites it (pp. 5, 15), the references list (pp. 31-32), the credits, the footnote on p. 1, and the Map pages. Findings:
- Fig. 3.10 is cited in the text only for the thrust faults: "The thrust faults that bound the allochthon are shown in Figure 3.10." (p. 5). The high-angle faults are not discussed in connection with the figure.
- The references list has no geologic map. Geologic references are Isachsen et al. (1991) "Geology of New York, a Simplified Account", NYS Museum/Geological Survey Educational Leaflet No. 28 (a text/educational leaflet), and Knopf (1962) "Stratigraphy and Structure of the Stissing Mountain area". Fisher, Isachsen & Rickard (1970) is **not** cited anywhere in the chapter.
- Other chapter figures with stated provenance: Fig. 3.4 "(from Isachsen et al., 1991)"; Fig. 3.11 "(interpreted by Jeff Walker; drafted by John DeGilio)" (p. 17). Fig. 3.10 has no such line.

Candidate source (NOT confirmed by the chapter): New York State Museum record that I opened, https://nysm.nysed.gov/bibcite/reference/28461:
- Title: "Geologic Map of New York; Lower Hudson Sheet, 1:250,000"
- Authors as printed on that page: "Fisher, D., Isachsen, Y., Richard, L." (the page spells it "Richard"; the usual spelling is Rickard)
- Year: 1970; Series: "New York State Museum and Science Service Map and Chart Series", Issue Number 15
- Publisher: "The University of the State of New York", Albany, New York
- Scale: 1:250,000 (in the title)
- No DOI on the page.
- The NGMDB product pages (ngmdb.usgs.gov/Prodesc/proddesc_98670.htm and proddesc_19466.htm) returned HTTP 403, so I could not confirm the record from USGS NGMDB. A web-search snippet mentioned them but I did not read them.

Whether Fig. 3.10 was compiled from this map is an inference (it is the standard bedrock/fault compilation covering Dutchess County, and the chapter's own authors cite Isachsen's group), not something I could verify. Say "likely derived from" at most; better to ask the authors (Walker/Menking, Vassar) or the Dutchess County Planning Dept. what the Fig. 3.10 layer was.

## 3. Approximate / inferred / concealed / high-angle wording

No fault is called approximate or concealed, and no line style distinguishes location quality (Fig. 3.10 uses one solid line style for "High Angle Fault"). Relevant wording:
- p. 15: "Although the contacts between these contrasting rock types are only exposed in a few places, they are inferred to be low-angle thrust faults" (thrust faults only).
- p. 15: "No doubt there are many faults within the blocks of similar rock types, but it is difficult to identify them because of the soil and vegetative cover."
- p. 18: "Also shown are relatively high-angle reverse faults, another type of faulting typical of the compressional forces active during mountain building events." (about the cross-section, Fig. 3.11)
- p. 18, the key sentence: **"The location of and sense of motion on the faults is largely conjectural since the faults themselves are rarely exposed at the surface."**
- p. 17: "The faults in the region are very old and considered to be inactive."

There is no statement of how locations were determined.

## 4. U.S. National Map Accuracy Standards (NMAS), horizontal rule

Official USGS source: USGS "Map Accuracy" fact sheet (National Cartographic Information Center, 1981), https://pubs.usgs.gov/unnumbered/70039528/report.pdf, which reprints the standards. It says: "In 1941 the U.S. Bureau of the Budget issued the 'United States National Map Accuracy Standards,' ... The standards were revised several times, and the current version was issued in 1947."

**Correction to the expected wording.** The standard's actual text is a two-tier rule keyed to "1:20,000 or smaller", not "smaller than 1:20,000":

> "1. Horizontal accuracy. For maps on publication scales larger than 1:20,000, not more than 10 percent of the points tested shall be in error by more than 1/30 inch, measured on the publication scale; for maps on publication scales of 1:20,000 or smaller, 1/50 inch. These limits of accuracy shall apply in all cases to positions of well-defined points only. Well-defined points are those that are easily visible or recoverable on the ground, such as the following: monuments or markers, such as bench marks, property boundary monuments; intersections of roads, railroads, etc.; corners of large buildings or structures (or center points of small buildings); etc."

It also says: "Similarly, features not identifiable upon the ground within close limits are not to be considered as test points within the limits quoted, even though their positions may be scaled closely upon the map. In this class would come timber lines, soil boundaries, etc."

Implied ground distance for 1/50 inch (= 0.508 mm on the map), at the 90th percentile ("not more than 10 percent ... in error by more than"):

| Map scale | Computation | Ground distance |
|---|---|---|
| 1:340,000 (Fig. 3.10 display) | 0.508 mm x 340,000 | 172.7 m |
| 1:250,000 (candidate source, Fisher et al. 1970) | 0.508 mm x 250,000 | 127.0 m |
| 1:225,000 (Map 3.1, for reference) | 0.508 mm x 225,000 | 114.3 m |

(Context: at 1:24,000 the same rule at 1/30 inch = 0.847 mm gives 20.3 m; not applicable here.)

## 5. Faults are not "well-defined points": USGS/FGDC guidance

Source: FGDC Digital Cartographic Standard for Geologic Map Symbolization (FGDC-STD-013-2006; USGS Techniques and Methods 11-A2), introductory text, https://pubs.usgs.gov/tm/2006/11A02/FGDCgeostdTM11A2_introtext.pdf (PDF pages cited), and the Preface to Appendix A, https://pubs.usgs.gov/tm/2006/11A02/FGDCgeostdTM11A2web_Preface.pdf.

(a) Geologic features were never held to plain NMAS. The standard says (p. 18-19) that Chief Geologist Bradley's 1956 memo adapted the NMAS for geologic maps: "features that ... can be located from exposures or other evidence [should be positioned] within 1/25 inch [on the map] of their true map position". It then notes these efforts "were not widely adopted by the geoscience community, likely in part because of (1) the difficulty in translating to geologic mapping a concept designed for topographic and other types of base maps".

(b) Definitions of location quality (p. 23):
- "Location accurate": "A feature is observable, and its plotted position on the map is within the declared zone of confidence."
- "Location approximate": "A feature is observable, but its plotted position on the map may not be within the declared zone of confidence."
- "Location inferred": "A feature is not directly observable between outcrops or beneath rubble or vegetation, so its location must be inferred by indirect means; by definition, its plotted position on the map may not be within the declared zone of confidence."
- "Location concealed": the feature is "completely concealed beneath an overlying map unit or body of water or ice".

(c) Zone of confidence (p. 19): "This hypothetical distance, which extends outward from a feature's position on the map, is herein defined as the zone of confidence ... for planar and linear geologic features, the zone of confidence borders the feature along both sides, forming what is described in GIS terminology as a buffer zone". It is explicitly project-specific: "a single, universally applicable value for the zone of confidence is not herein established" and depends on "the area's geology, landscape terrain, vegetation cover ... the scale of mapping; the quality and nature of the base map used". This is the direct precedent for drawing a buffer around digitized fault traces.

(d) Bradley 1956 (p. 15): "Solid lines should be used to indicate accurate locations of features that are geologically identifiable within the plottable limits of the map ... Features that are only approximately located should be shown by long dashed lines; those that are indefinite or inferred, by short dashed lines".

Not found: an official NGMDB/USGS sentence saying outright that faults "are not well-defined points under NMAS". I did not read one. The NMAS text itself excludes "features not identifiable upon the ground within close limits" (examples given: timber lines, soil boundaries), and faults that are "rarely exposed at the surface" (Budnik et al., p. 18) fall in that class by the same logic. That is an inference from the quoted texts, flagged as such.

## URLs opened (actually read)
- https://www.dutchessny.gov/Departments/Planning/Docs/nrichapthree.pdf (full text extracted, Fig. 3.10 page rendered and viewed)
- https://nysm.nysed.gov/bibcite/reference/28461 (Fisher et al. 1970 record)
- https://nysm.nysed.gov/bibcite/reference/28366 (opened; it is Cadwell 1989 Surficial Geologic Map, Lower Hudson Sheet, Map and Chart Series 40, not the bedrock map; not used)
- https://pubs.usgs.gov/unnumbered/70039528/report.pdf (USGS Map Accuracy fact sheet, NMAS text)
- https://pubs.usgs.gov/tm/2006/11A02 (index), .../FGDCgeostdTM11A2_introtext.pdf, .../FGDCgeostdTM11A2web_Preface.pdf (FGDC standard)

Could not open: ngmdb.usgs.gov product pages and ngmdb fgdc-geolsym-all.pdf (HTTP 403); the UNT web-archive copy of USGS nmas647.html returned only a wrapper page with no text.

## Implication for the band width

Because Fig. 3.10 has no stated accuracy, a band must be justified from scale-based reasoning and labelled as an assumption. Faults are not NMAS well-defined points, so the NMAS number is a floor, not a measured accuracy.

Half-widths (1/50 in = 0.508 mm on the map):
1. Floor from the figure's own printed scale: 0.508 mm x 340,000 = **173 m**.
2. Floor from the likely (unconfirmed) 1:250,000 compilation: 0.508 mm x 250,000 = **127 m**. This is smaller than (1), so (1) is the binding one when we digitized from the 1:340,000 figure. If both errors apply, in quadrature: sqrt(127^2 + 173^2) = **214 m**.
3. Geologic-map adaptation (Bradley 1956, via FGDC), 1/25 in = 1.016 mm on the map: 1.016 mm x 250,000 = **254 m** (source scale), 1.016 mm x 340,000 = **345 m** (figure scale). The FGDC standard says this adaptation was applicable to features located from exposures; Budnik et al. state the faults are "rarely exposed" with "largely conjectural" locations, so a larger value is plausible.

Defensible choices: a lower-bound band of about 175 m half-width (NMAS 1/50 in at the figure's 1:340,000), described as the minimum; and a more conservative band of about 250-350 m (1/25 in at 1:250,000-1:340,000). State the scale basis explicitly in the manuscript, cite the FGDC zone-of-confidence concept as precedent, and say the source map of Fig. 3.10 is not identified in Budnik et al. (2010). Do not assert it came from Fisher et al. (1970) without confirmation from the authors or the County.
