# Coherence review of `revisions.tex` (2026-11-09)

Read-only review of `revisions.tex`, the three `\input` tables, and the rendered figures
`figures/rev_*.png`. Line numbers refer to the current `revisions.tex`. Items are ranked
with the most important first. Deliberate choices in `docs/revision_plan.md` (D0 within-day only,
no fault band, "fault points" wording, inconclusive framing) are not flagged.

---

## A. Orphans, contradictions and framing leftovers (fix before resubmission)

### 1. L213: reference to a withdrawn earlier argument (submission-history orphan)
> "The earlier argument that sampling within conserved land lets us discount such inputs does not hold, ... and we withdraw it."

No such argument appears in the current paper. It survives only in `original.tex`, so this is
a self-reference to the submission history, which the editor-style review ruled out.
**Fix:** replace it with: "Sampling within conserved land does not let us discount such inputs, because the sources lie in the contributing area and not only along the survey line."

### 2. L110 vs L153: "consistent offset" contradicts "not constant"
L110: "the two survey days differ by a consistent offset"; L153: "The offset is therefore not
constant, and its range of about 6 µS/cm exceeds Contrasts B and E".
**Fix (L110):** "consistent offset" → "large offset".

### 3. L232, L238 (and L244, L246): "without tie points" contradicts the repeated reach; "tie points" is never defined
L232: "At Site 3 we surveyed on two days without tie points". L238: "pooling the two survey days, which had no tie points". But L153 (and the Fig. 4 inset) report that Zones 3-1 and 3-2 *were* resurveyed on both days, giving 11 point pairs. The real problem is that the repeated reach gives an offset that varies by about 6 µS/cm and lies upstream of the 26 Oct seam, so it cannot tie the days. "Tie points"/"tie-pointed" (L232, L238, L244, L246) is also used without being defined.
**Fix (L232):** "At Site 3 we surveyed on two days; the reach repeated on both days gave an offset that varied by about 6~µS/cm (Section~3.1), too much to tie the days together, which limited us to within-day comparisons ..."
**Fix (L238):** "...or tied across days by repeated points at a steady offset: pooling the two survey days produces ...". Delete ", which had no tie points,".

### 4. L93 (+ Fig. 6 legend, L272): the zone-boundary rule and the fault-point definition don't match the data
- L93 says zones are bounded "where the creek crosses a mapped fault trace (at Site 2, the fault position interpreted in the field)". But at Site 3 the D and E boundaries are not at the digitized crossings. Fig. 6 puts the trace crossings at about 750 m (19 Oct) and 523 m (lower 26 Oct), while the boundaries sit at about 920 m and 716 m. In every site the boundary falls between the last unflagged point and the first fault point (Appendix: 1-1/1-2 pt 4/5; 2-1/2-2 pt 10/11; 3-2/3-3 pt 9/10; 3-3/3-4 pt 6/7). The Fig. 6 legend says "Zone boundary (field-interpreted fault; contrasts B, D, E)", which contradicts the text's claim that only Site 2 is field-interpreted. L168 itself shows the E boundary is 193 m from the trace crossing.
- L93 says "We marked the survey points located just downstream of a mapped fault", which reads as map-based fact. L272 (Appendix) says "The flag records what we believed at the time of sampling". The Site 2 flags also don't fit "just downstream": pts 1–3 at the upstream end of Zone 2-1, and pts 16 and 18 but not 17.
**Fix:** decide how the D/E boundaries were placed and state it once in L93. For example, "Zone boundaries at fault crossings were placed immediately upstream of the fault points (at Site 2, at the field-interpreted bend), so they lie within a few hundred meters of, but not exactly at, the digitized trace crossings". Reword the fault-point sentence to match L272: "During sampling we flagged the survey points we believed lay just downstream of a fault; we call these fault points". Make the Fig. 6 legend agree (in `src/rev_figures.py`).

### 5. L93, L110: contrast letters are used before they are defined
"(Contrast B)" (L93) and "Contrast D ... Contrast E" (L110) appear in Methods, but Methods never says what Contrasts A–E are. The definition now exists only in Table 1 and in the Results headings. In the Results the Site 3 paragraph (L142) never gives the zones for C, D and E.
**Fix:** add to L93 after the zone-numbering sentence: "This gives five upstream/downstream contrasts (Table~\ref{tab:ttest}): A (Zones 1-1/1-2, tributary), B (2-1/2-2, fault), C (3-1/3-2, tributary), D (3-2/3-3, first fault) and E (3-3/3-4, second fault)."

### 6. L69/L71: the three predictions are never closed out
L71: "We test these predictions". Prediction 1 (abrupt step) is answered by the change-point results. Prediction 2 (persistence at summer/early-autumn baseflow) is never evaluated. Sites 1 and 2 were at very high flow (L124, L133), so the survey cannot test it. Prediction 3 (chloride and Cl/Br) is only partly addressed: one chloride transect and no bromide. The Discussion never refers back to the predictions.
**Fix:** add one sentence at the end of the first paragraph of §4.1 (after L199): "Of the three predictions in the Introduction, the first, an abrupt step at a fault, is not met at any crossing; the second could not be tested, because Sites 1 and 2 were surveyed at high flow; and the third was examined only with a single chloride transect and no bromide." Optionally soften L71: "We test these predictions" → "We examine these predictions".

### 7. L142, L203: "lower-conductance water enters" has no supporting number
L142: "a decrease where lower-conductance water enters". L203: "when lower-conductance water joins the main stem". The tributary's conductance is not reported anywhere in the revised paper. The original's "the active tributary measured nearly 150 µS/cm lower" (original.tex L168) was cut, and the Appendix lists no tributary reading.
**Fix:** either restore the docx sentence once (Results, L142): "the tributary measured nearly 150~µS/cm lower than Zones 3-1 and 3-2". Or hedge both: "consistent with dilution by lower-conductance tributary water".

### 8. Abstract L52: "tributary junctions lowered conductance" (plural) overstates
Only Contrast C supports this, and only robustly on 26 Oct. Contrast A is −0.5 µS/cm, not significant, and confounded (L124). The body (L142, L203, L242) correctly speaks of the tributary contrast (C).
**Fix:** "while the tributary junction at Site 3 lowered conductance as mixing predicts".

### 9. L199, L242: "contrasts at mapped faults" / "three mapped faults" includes B, which is not at a mapped fault
The Methods (L93) and Results (L133) say the B boundary is a field interpretation, not a mapped-trace position.
**Fix:** L199 "Of the three contrasts at mapped faults" → "Of the three fault contrasts". L242 "at one of three mapped faults (Site 2)" → "at one of three fault contrasts (Site 2)".

### 10. Fig. 5 and Fig. 6 captions (L162, L173): "blue cross(es)" don't exist
Both figures draw the digitized trace crossing as a **gray** X. In Fig. 6 the blue triangles are the PELT shifts. Fig. 5 shows only one crossing, at about 1,800 m.
**Fix:** L162 "the blue cross the mapped fault crossing" → "the gray cross where the digitized fault trace crosses the transect". L173 "blue crosses are mapped fault crossings" → "gray crosses are digitized fault-trace crossings".

### 11. L122 vs L151: within-day SD range differs
L122: "Within a single day the zone standard deviations are 0.1–2.6 µS/cm" (matches Table 1). L151: "against 0.4–2.6 µS/cm within a day". The second figure is the Site 3 range only.
**Fix (L151):** "against 0.4–2.6~µS/cm within a day at Site 3".

### 12. L205 vs L232: "real but small" contradicts the Limitations
L205: "which is why we report it as a real but small difference". L232: "we cannot rule out that reading error accounts for part of Contrast B". "Real" is also stronger than the framing allows.
**Fix (L205):** "real but small difference" → "statistically significant but small difference".

### 13. L228: §4.4 title doesn't match its content
"Limitations and alternative hypotheses". The alternative hypotheses are in §4.2. §4.4 contains limitations plus the test design (L238).
**Fix:** retitle to "Limitations and a test of the hypothesis" (or "Limitations and test design"). The `sec:limits` label and the L225 reference still work.

### 14. L65: stranded salinization-syndrome paragraph
A two-sentence paragraph, "This motivates a search for the specific structures ...", sits *after* the fault paragraph (L63), which already introduced faults as "one candidate control". It is a leftover from the cut syndrome discussion and reads backwards.
**Fix:** move L65 to the end of L61, before "This raises the question of what controls where that stored salt re-emerges", and drop its "This motivates..." sentence. Or cut L65 entirely; kaushal2018/2023 are recent citations, so check the ≥30% budget first.

### 15. L90: field sites 4 and 5 do not "together repeat part of the 19 October reach"
From the Appendix, only field site 5 (the upper 26 Oct survey, Zones 3-1/3-2) repeats the 19 Oct reach. Field site 4 (the lower survey) starts at the 19 Oct end point (the "seam", L153) and continues downstream. "Upper" and "lower 26 October surveys" (L114, L168) are never tied to field-site numbers, although Fig. 6 panel titles use both.
**Fix:** "...and two on 26 October: an upper survey (field site 5) that repeats Zones 3-1 and 3-2, and a lower survey (field site 4) that continues downstream from the end of the 19 October survey."

### 16. L116 vs Table 2 caption (L188): Taconic exclusion appears only in the caption
The Methods define major roads as TIGER S1100/S1200. The caption adds "(excluding the Taconic State Parkway)", unexplained. In TIGER the Parkway is S1400, so it is excluded by the definition.
**Fix:** add to L116: "(the Taconic State Parkway is coded as a local road, S1400, and is therefore excluded)". Or drop the parenthetical from the caption.

### 17. L97: forward reference to a method not yet described, duplicated at L114
"we describe it and apply the same change-point method used for conductance". Change-point analysis is introduced only at L114, which ends "The same procedure was applied to the chloride transect."
**Fix:** cut ", and apply the same change-point method used for conductance" → "...cannot confirm the conductivity pattern, and we treat it as descriptive."

### 18. L246: "untested here" conflicts with the paper testing it
"We therefore regard the fault-conduit hypothesis as plausible but untested here." L71 says "We test these predictions", and the paper does test them, with an inconclusive result.
**Fix:** "plausible but unresolved by this survey".

---

## B. Redundancy (cut one copy)

19. **L221 repeats L63 and L79 almost word for word.** It restates the conduit–barrier description (caine1996, bense2013), manda2008 and kim2014, and its conclusion repeats L63 ("These studies leave open...") and L246. **Fix:** delete the first paragraph of §4.3 (L221) and let §4.3 open at L223. That is about 70 words; the strict count of 5,992 stays well above 5,500.
20. **Tributary masking, L67 vs L203.** "Dilution by a tributary could also partly mask a groundwater input ... without discharge measurements" appears in both. **Fix:** cut the L67 sentence (`L:intro-mask`); keep L203, where it is used. Check the letter's `\Ln{intro-mask}` reference first.
21. **Instrument accuracy and the calibration-offset argument appear three times** (L90, L205, L232), and "about 2.5 times" four times (L133, L205, L232, L242). **Fix:** in L232 cut from "its stated accuracy is about ±1.7..." through "...accounts for part of Contrast B" and replace with "Contrasts B and E are close to the instrument's stated accuracy (Section~4.1)". Or trim L205's version and keep L232.
22. **Day-offset numbers, L110 vs L153.** "eleven pairs ... within 120 m ... 23.5 to 29.7 (mean 27.8)" appears in both. **Fix (L110):** "At Site 3 the two survey days differ by a large offset (about 28~µS/cm; Section~3.1), larger than any of the contrasts we test."
23. **Adjusted p-values as a "sensitivity check rather than a correction"** appear at L112, L236 and in the Table 2 caption. **Fix:** cut from L236 "the autocorrelation of residuals is poorly determined ... rather than a correction" → "Statistically, our zones contain only three to eleven points."
24. **Budnik "largely conjectural" appears four times** (L77 quote, L93 twice, L236). **Fix:** in L93 cut "and are largely conjectural \citep{budnik2010}" and ", whose locations are largely conjectural \citep{budnik2010}". Keep L77 and L236.
25. **Test-design list, L238 vs L246 (and Abstract).** L246 repeats the full list. **Fix (L246):** "A conclusive test would follow the design in Section~\ref{sec:limits}." Optionally keep "single-day surveys, discharge and tracers" as a short gloss.
26. **L102 first sentence repeats L93's zone definition**, with different terms ("geologic interactions", "side-stream"). **Fix:** cut it and start: "For each contrast we applied a two-sample Welch $t$-test ...".
27. **L90 vs L93 spacing.** "approximately every 100 m ... about every 400 m" is followed two sentences later by the exact means. Optional: drop the approximate spacing from L90.

---

## C. Minor reference and terminology fixes

28. **L142: Figure 4 is not cited in the Site 3 Results paragraph.** Its first citation is at L153. Add "(Figure~\ref{fig:site3})" after "Contrasts C, D and E (19 and 26 October)." The **Fig. 4 caption (L147)** also doesn't mention the orange fault-point rings shown on the map. Add "Orange rings mark fault points."
29. **Hard-coded cross-references:** "Figures 2--6" (L93), "Section~2.2" (L133), "Section~3.1" (L232). The numbers are correct now but will break if sections move. Use `\ref`.
30. **L217 "stream chloride in this reach":** the paragraph is about Site 2, but Kelly 2008 is the East Branch (Site 3). Use "in the East Branch".
31. **"East Branch" (L215, L217) vs "east fork" (L77, L95, L251):** pick one.
32. **"side-stream" (L102) vs "tributary"** everywhere else.
33. **L168 "minimum segment length the method allows":** Methods (L114) defines the minimum as three points, not a length. Use "at the three-point minimum segment the method allows".
34. **L67/L69:** consecutive paragraphs end and start with "We therefore". At L69 "We therefore ask" doesn't follow from the tributary paragraph. Use "We ask".
35. **L215 "just upstream of the 2.36 km breakpoint":** this covers the plant at 0.9 km, which is about 1.5 km upstream. Use "upstream of".
36. **L91:** "We inferred changes in the salt input ... from changes in specific conductance." is stranded after the accuracy sentences. Move it to the start of the L90 paragraph or after "reported as specific conductance".
37. **Appendix caption (`figures/appendix_data.tex` L4):** "from the upstream end of each single-day transect". 26 Oct has two transects, each starting at 0 m. Use "of each survey (field site)". This is an auto-generated file, so edit `src/within_day.py`.
