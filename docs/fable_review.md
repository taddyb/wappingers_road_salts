# Pre-resubmission review of `revisions.tex` (JHEWS-101225)

Reviewed 2026-11-09 against `original.tex`, the reviewer comments (docx), `response_to_reviewers.tex`, `docs/revision_plan.md`, the three `\input` tables and the six `figures/rev_*.png`. Read-only: nothing but this file was written. Line numbers are source lines of `revisions.tex` at commit 6357905.

**Status (2026-11-09):** the author approved Sections B, C and D and they have been applied to `revisions.tex`, the figure scripts and the response letter. Not applied: the title case change (B18; the cover letter quotes the title), the Figure 1b relabel (the facility is described in the text instead), the `L:cl-E` rewording in C21, and the fuller option of C14. Line numbers below refer to commit 6357905, before the edits.

**On the WRR paper (voice reference).** In the first pass I could not reach the paper online (Wiley returned HTTP 403) and wrote Section C from the brief's description. The author's PDF of Bindas et al. (2024, WRR, 10.1029/2023WR035337) was then supplied locally, and I read its Abstract, Introduction, Results openings, "Further Discussion" and Conclusions. **Section C has been rewritten against the paper itself** and opens with a voice profile. Sections A, B and D are unchanged except D16.

**Checks I ran.** Cited references: 35 keys, 11 from 2022–2026 = 31.4% (passes, but with no margin: removing one recent citation gives 10/34 = 29.4%). Main-body words (Introduction to Conclusions, no captions/tables/equations): about 5,600. All cited entries have a DOI except four reports (adirondack2023, budnik2010, kelly2019, kelting2010), which have a URL or report number. No "now / no longer / revised / withdraw / reviewer / field log / flagged" wording remains in the manuscript text (the figures are another matter; see B3).

---

## Section A. Reviewer-comment coverage

Verdicts judge the manuscript, not the letter. IDs follow `response_to_reviewers.tex`.

| ID | Comment (short) | Verdict | Where in `revisions.tex` | What is still missing |
|---|---|---|---|---|
| E.1 | Address the points raised; highlighted changes; letter; no author changes | MET | whole paper; author block L24–34 | Nothing in the manuscript. 31.4% recent references is a thin margin; recount after any citation edit. |
| R1 gen. | Reframe as hypothesis-generating; alternatives; limitations; clarify maps; temper conclusions | MET | L71, L198–204, L208–216, L229–237, L241–245 | None of substance. |
| R1.1 | Introduction reaches geology too late | MET | faults at L63 (third paragraph) | The syndrome paragraph (L65) now sits between faults and tributaries and reads as an orphan (see B9). |
| R1.2 | Soil and groundwater timescales mixed | MET | L61 | None. The soil mentions at L52 and L210 are a separate point (R2.9) and are not mixed with groundwater timescales. |
| R1.3 | Predictions lack references | MET | L69 | None. |
| R1.4 | Fault hydrogeology should rest on Caine, Bense, metamorphic rock | MET | L63, L79, L220 | L63 and L79 say the same thing twice (see D7). |
| R1.5(1) | No discharge, no tracers | MET | L67 (masking), L229, L237 | None. |
| R1.5(2) | One chloride transect, ion-selective probe | MET | L94, L96, L233 | None. |
| R1.5(3) | t-tests cannot show abruptness; use change-point analysis | MET | L113, L156, L167, Figure 6 | The text never says what the change-point analysis finds at the **tributary** (see D1). |
| R1.6 | Table 1 lacks SD, df, CI, Mann–Whitney | MET | Table 1 (L177–184) | None. Tables float after Section 3.3, far from the text that uses them (D5). |
| R1.7 | Zone 3-2 SD larger than the contrasts | MET | L121 (SD range), L150 (pooled SD 12.6–15.8), L152 | The pooling paragraph has no stated motive for a new reader (B1). |
| R1.8 | Autocorrelation not handled | MET | L111, Table 2, L132 | None. |
| R1.9 | z-score normalization has no effect | MET | removed; L101 tests µS/cm | None. |
| R1.10 | Explanation of non-significant Contrast D was wrong | MET | old explanation removed; L141, L200 | None. |
| R1.11 | 4.3 µS/cm is near the uncertainty of temperature-compensated SC | MET | L90, L132, L204, L231 | Optional: the reviewer names temperature compensation. Appendix A shows water temperature nearly constant within a survey; one clause saying so (after checking every survey in the appendix) would answer that word directly. |
| R1.12 | Alternative sources: roads, developed land, sewage/septic, non-fault groundwater | MET | L208–216, Table 2 | Septic systems appear only inside the Kelly percentages (L214); a clause that septic inputs along the reaches were not mapped would close it. Figure 1b shows a fourth wastewater facility at Site 3 that the text never mentions (B6). |
| R1.13 | Overreach; D contradicts "all three"; deicer advice premature; little comparison with other surveys or metamorphic fault hydrogeology | **PARTLY** | overreach removed; L198–200; L224; surveys L222 | The comparison with fault hydrogeology in metamorphic rock is one sentence (L220) that says only that those studies make the idea plausible. The letter claims a comparison in Section 4.3. See C12 for a rewrite that makes it a real comparison using only what L63 already states. |
| R1.14 | DOIs / report numbers; citation order | MET | `sort&compress` L16; bib | None. |
| R2 gen. | More caution; clearer figures; alternatives | MET | as R1 gen. | None. |
| R2.1 | Add tributary mixing to the Introduction; dilution may mask groundwater | MET | L67 | None. |
| R2.2 | Normalization across site or within zone? | MET | removed | None. |
| R2.3 | Show SDs; show the actual data | MET | L121, Table 1, figure labels, Appendix A | None. |
| R2.4 | Fig 3: fault crosses the stream at several places; justify zones | **PARTLY** | L92 (`site2-bend`), L132 (`site2-trace`), caption L137 | Figure 3 rings six "fault points": three at the **upstream end of Zone 2-1** (0–878 m), one just below the boundary and two more in Zone 2-2. The text defines fault points only as "downstream of a fault" (L92) and never says which fault these belong to or why they were not used as boundaries. The reviewer who asked about multiple crossings will ask about these (B2). |
| R2.5 | Contrast B is small; meter uncertainty; cross-channel variation | MET | L90, L132, L204, L231 | None. |
| R2.6 | Change occurs within Zone 3-3; fault may be mislocated; show a zone | MET (band declined by author decision) | L77, L150, L152, L235 | The manuscript explains the artifact (L150) but a reader of Figure 4 is never told in so many words that the visible color change inside Zone 3-3 is the join between the two days. One clause at L152 would do it (B1). |
| R2.7 | Test chloride above/below Contrast E | MET (declined with reason) | L156 (`cl-E`) | None. |
| R2.8 | Two overlapping data sets in Zone 3-1 | MET | L152, caption L146, Figure 4 inset | No explanation of **why** the days differ is offered, even as a hedged guess (D3). |
| R2.9 | Land use dismissed; road distance and density; salt in soil | MET | L115, L210, L212, Table 2 | L212 answers an argument the paper no longer makes (B4). Road density is acknowledged as not captured (L210). |
| R2.10 | Fig 1b hard to read | MET | Figure 1 | Unlabeled facility square at Site 3; NY 55 named in the text (L77) but not on the map. |
| R2.11 | Fig 2: label Contrast A; flow direction | MET | Figure 2 | None. |
| R2.12 | Fig 3: label Contrast B; flow direction | MET | Figure 3 | See R2.4. |
| R2.13 | Fig 4: label contrasts, flow, error margin, Z–Z′, inset | MET except error margin (declined by author decision; reason given at L77, L235) | Figure 4, caption L146 | The inset shows two separate boundary bars for Contrast C (one per day) with no explanation (B7). |
| R2.14 | Fig 5: locate Z–Z′ | MET | Figure 4 band; caption L161 | Figure 5 labels still say "flagged points" (B3). |
| R2.15 | Table 1: normalized means, variance, chloride above/below E | **PARTLY** (variance MET; the other two declined) | Table 1; L156 | By design. The manuscript gives the reason for no chloride test (L156). Nothing more is needed in the paper. |
| R3 | "Minor revisions", no comments | n/a | | |

**Summary:** no comment is NOT MET. Three are PARTLY: R1.13 (metamorphic-rock comparison is one sentence), R2.4 (unexplained fault points at Site 2), R2.15 (declined items, acceptable).

---

## Section B. Context fragments and flow breaks

**B1. L150, "Pooling days" has no motive and no method.**
Quote: "When the two survey days are pooled, Contrast E appears as a rise of $+18.0$~$\mu$S/cm". A reader who has just been told three times that days are never pooled (L109, L121, L146) has no idea why a pooled result is being reported. It is the paper's main methodological point (abstract, L237, L243), so it needs a reason that lives inside the paper, and the pooled test must appear in Methods before its result appears.
Fix: (a) add to L109 after "Contrast D is therefore tested on 19 October, and Contrast E on 26 October.": "Zone 3-3 was surveyed partly on each day, so the simplest analysis would pool the two days into one Site 3 data set. To show what that choice does, we also ran the Contrast E test on the pooled data and report it separately in Section~\ref{sec:contrasts}." (b) Use the C7 rewrite for L150. (c) At L152 add after the seam sentence: "This seam falls inside Zone 3-3, which is why Figure~\ref{fig:site3} shows a change of color partway along that zone."

**B2. L92, "fault points" are defined too thinly to be understood.**
Quote: "Survey points located downstream of a fault are called fault points". Every point below a fault is downstream of it, yet only some are ringed; at Site 2 three ringed points sit at the upstream end of Zone 2-1 (Appendix A, points 1–3) and at Site 1 all of Zone 1-2 is ringed although Contrast A is labeled a tributary contrast. The reader is not told who decided, when, on what basis, or what the points are used for (they are used only as a distance reference in L156 and L167).
Fix (keeps the "fault points" term and the author's stated meaning): "During the surveys we marked the points that we believed lay just downstream of a fault. We call these fault points (Figures~\ref{fig:site1}--\ref{fig:changepoint} and Appendix A). They record our judgment on the day and not an observed fault position, and they do not enter the statistical tests; we use them only as a reference when reporting where a change in conductance or chloride lies. At Site 2 they include three points at the head of the reach, where the creek first meets the mapped trace." The last sentence is my reading of Figure 3; the author must confirm or replace it.

**B3. Figures 5 and 6 carry wording from the working files.**
- `rev_chloride.png`: in-plot labels "D flagged points", "E flagged points"; legend "Survey points flagged as just downstream of the fault (D, E), projected onto path". The paper's term is "fault points" (caption L161).
- `rev_changepoint_sc.png`: panel titles "Site 3 upper (field site 5)" and "Site 3 lower (field site 4)"; legend "PELT change-in-mean"; legend line "Zone labels in boxes; zone ends at boundary lines".
- L90: "one on 19 October (field site 3), and two on 26 October: an upper survey (field site 5) ... a lower survey (field site 4)". "Field site" is notebook numbering. It makes Site 3 consist of field sites 3, 5 and 4, in that order, which is confusing.
Fix: name the three Site 3 surveys once in the paper's own terms ("the 19 October survey", "the upper 26 October survey", "the lower 26 October survey"), drop "field site" from L90 and the figure titles, and either rename the Appendix column "Survey" or keep "Field" with one sentence at L271 ("Field is the survey number in our records; surveys 3, 4 and 5 together make up Site 3"). Relabel Figure 5 to "D fault points" / "E fault points".

**B4. L212, answer to an argument the paper does not make.**
Quote: "Sampling within conserved land does not let us discount such inputs, because the sources lie in the contributing area and not only along the survey line." The reader has not been told that any sampling was within conserved land (the Cary Institute appears only in the Acknowledgements, L250).
Fix: either state the fact first in L77 ("Part of the Site 3 reach lies on land conserved by the Cary Institute of Ecosystem Studies.") or reword L212 to stand alone: "Parts of our reaches run through conserved, forested land, but we do not think that lets us discount such inputs, because their sources lie anywhere in the contributing area and not only along the survey line."

**B5. Flow conditions first appear in Results, and Site 3 is never described.**
Quotes: L123 "we surveyed Site 1 at very high flow after rain"; L132 "Flow was very high for the duration of the Site 2 survey, and we canoed part of it"; L198 "the second could not be tested, because Sites 1 and 2 were surveyed at high flow". Prediction 2 (L69) is about baseflow, but Methods never give the flow state of any survey, and the paper never says what flow was like at Site 3 on 19 or 26 October. L198 therefore leaves the reader asking why Site 3 did not test prediction 2.
Fix: one sentence in L90 after the dates: "Sites 1 and 2 were surveyed at very high flow following rain; [Site 3 conditions, from the author's records, or: we did not record flow conditions at Site 3]." Then L198: "the second could not be tested, because Sites 1 and 2 were surveyed at high flow and we have no discharge record to show that the Site 3 surveys were at baseflow." The bracketed part needs the author; do not guess.

**B6. Figure 1b shows a wastewater facility the text never mentions.**
There is an unlabeled square at the west edge of the Site 3 box (from `data/wwtp_facilities.csv` this is the NYSP Troop K Headquarters facility on a tributary). L214 discusses Millbrook, Stratford Farms, Ennis, Titusville and Valley Dale only, and Figure 4 shows no facility.
Fix: add one clause to L214 ("a state police facility with a discharge permit lies on a tributary about 0.8~km from the lower end of Site 3, and enters the creek downstream of our survey", using the figures in `docs/wwtp_kelly2008.md` after the author checks them), or remove the square from Figure 1b.

**B7. Figure 4 inset: two boundaries for one tributary.**
The inset draws a "C ▲" bar and a "C ●" bar about 40 m apart. The text (L141) treats Contrast C as one junction. Fix: one clause in the caption at L146: "The Contrast C boundary is drawn separately for each day because the survey points nearest the junction differ between days."

**B8. L109, a result and a list of rejected options inside Methods.**
Quote: "At Site 3 the two survey days differ by a large offset (about 28~$\mu$S/cm; Section~\ref{sec:contrasts}), larger than any of the contrasts we test. We did not pool days, add a day covariate, or correct for the offset." "Add a day covariate" and "correct for the offset" are options weighed during the revision; the reader was never offered them. See C5 for a rewrite that gives the reasoning instead.

**B9. L65, orphan paragraph.**
Quote: "Salinization is increasingly viewed as a coupled process ... This motivates a search for the specific structures that concentrate delivery of stored salt to surface water." It comes after the fault paragraph has already begun that search, and before the tributary paragraph, so it interrupts faults → tributaries → question.
Fix: fold it into the end of the second paragraph (L61), before the pivot sentence: "... rather than the most recent winter alone. Salinization is increasingly viewed as a coupled process, the ``freshwater salinization syndrome'' \citep{kaushal2018} or ``anthropogenic salt cycle'' \citep{kaushal2023saltcycle}, in which geology and hydrologic flowpaths are among five proposed state factors \citep{kaushal2023factors}. This raises the question of which geologic structures control where that stored salt re-emerges." Geology still arrives at the third paragraph (R1.1). The letter's R1.1 response quotes the position of this text ("two sentences after the fault paragraph") and must be updated.

**B10. L77, "without an error zone".**
Quote: "so the mapped traces are approximate and we draw them as lines without an error zone". A reader would not expect an error zone; this answers Reviewer 2. Fix: "so we treat the mapped traces as approximate. The map states no positional accuracy, and we therefore draw the faults as lines and do not attach a width to them." Then cut the repeat at L235 ("so we draw them as lines").

**B11. L90, "The meters used with this cell".**
Quote: "The meters used with this cell specify an accuracy of $\pm$0.5\% of reading $\pm$1 digit". This reads as if the authors do not know which meter they used (true, per the plan, but unexplained). Fix: "We did not record the meter model; the Orion meters compatible with this cell specify an accuracy of ..."

**B12. Undefined abbreviations and names.**
- PELT (L113, Figure 6 legend): never expanded and has no citation. Write "a penalized change-in-mean analysis (the PELT algorithm, pruned exact linear time, in the \texttt{ruptures} package)". No new citation is needed if the package is named, but adding one would cost reference-budget margin, so I do not recommend it.
- TIGER/Line (L115), EPA ECHO (L84, L214, L258), NHD (L84): expand at first use ("the US Census Bureau's TIGER/Line road files", "the US Environmental Protection Agency's Enforcement and Compliance History Online (ECHO) database", "National Hydrography Dataset").
- STP, WWTP, MHP: used in Figures 1 and 3 only. Define in the Figure 3 caption or spell out on the figure.
- "the long-term monitoring site of \citet{kelly2019}" (L94): say what is monitored there and why it is marked ("where stream chloride has been monitored since the 1980s", if that is what Kelly et al. 2019 report; author to confirm).
- "SC" appears in Figures 4 and 6 and the Appendix; define at L90: "reported as specific conductance (SC)".

**B13. L167, garbled parenthesis.**
Quote: "the field-interpreted fault position at the channel bend (3{,}993~m; 0.6--2.7~km given the bootstrap interval)". The two numbers measure different things. Fix: "This breakpoint lies about 1.6~km upstream of the Contrast B boundary at 3{,}993~m (between 0.6 and 2.7~km upstream, given the bootstrap interval)".

**B14. L156, "nearest digitized fault trace" is ambiguous against Figure 5.**
Quote: "293--391~m from the nearest digitized fault trace". Figure 5 marks the only trace crossing on the transect at about 1,800 m, more than 800 m from the peaks, so the reader cannot reconcile the two. The 293–391 m are straight-line distances to the trace mapped near Z. Fix: "293--391~m in straight-line distance from the fault trace mapped near Z (the transect itself crosses a mapped trace only once, at about 1.8~km)". Author to confirm the 1.8 km figure from the analysis output.

**B15. Three different values for the day offset.**
L109 and caption L146: "about 28"; L152: pairs "23.5--29.7 (mean 27.8)" then "the two days differ by about 29--30". The last comes from zone means and contradicts the first. Fix at L152: "so within each day the zones are internally consistent, and the zone means differ between days by 29--30~$\mu$S/cm, close to the paired-point offset."

**B16. L92, "such a bend" and out-of-order Site 2 material.**
Quote: "is therefore placed at such a bend, a roughly 90$^{\circ}$ turn of the channel". "Such" points back five sentences, across the definition of fault points, zone numbering and the list of contrasts. Fix: move the three Site 2 sentences (`site2-bend`, `site2-bend-caveat`) up to follow directly after "these field positions lie within a few hundred meters of, but not exactly at, the digitized trace crossings.", and write "is therefore placed at the most abrupt bend on the reach, a roughly 90$^{\circ}$ turn".

**B17. L92, restriction that Site 1 does not satisfy.**
Quote: "we restricted our fault-crossing contrasts to reaches where the creek intersects a mapped fault without a coincident tributary". Site 1 was chosen for its fault (L77) but its only contrast is a tributary contrast with all downstream points ringed as fault points. Say so here, not first at L123: add "At Site 1 a tributary enters where the channel meets the fault, so we class Contrast A as a tributary contrast and do not count it among the fault contrasts."

**B18. Small leftovers.**
- L77: "State Highways 44, 55, and 9": US 44 and US 9 are US routes (the paper says "US 44" at L210 and L212), and NY 55 is not on Figure 1b.
- L22/L43: title mixes sentence case and "Case Study". Use "case study".
- L214 "2.36~km breakpoint" versus L167 "2{,}355~m". Use one.
- L222 "over 5000~mg/L" → "5{,}000".
- L258 "Both the data, and the code, to reproduce" → "The data and code needed to reproduce".
- Figure 1a has burned-in text "Taken directly from Budnik, Walker & Menking (2010)". The caption already says "reproduced from"; remove the burned-in line and confirm permission to reproduce.

---

## Section C. Voice: passages and proposed rewrites

This section was rewritten after reading the author's WRR paper (Bindas et al., 2024, 10.1029/2023WR035337; local PDF, text extracted with PyMuPDF). I read the Abstract, Introduction, the openings of Sections 3.1–3.3, Section 3.4 "Further Discussion" and the Conclusions. All numbers in the rewrites are unchanged from `revisions.tex`. Rewrites that change a sentence quoted with `\mq{}` in `response_to_reviewers.tex` are marked **[letter quote]**.

### Voice profile (observed in the WRR paper)

Example phrases are from Bindas et al. (2024), an open-access CC BY article.

1. **First person plural, active, for every choice and inference.** Choices are owned ("We chose to parameterize channels using"), and possessives carry results ("Our synthetic experiments recovered"). The passive is kept for routine procedure.
2. **Long, chained sentences, closed now and then by a short one.** Typical sentences run 25–45 words and are joined with "while", "but", "as", "thus" and "which"; a paragraph often ends on a short decision ("Thus, in our next efforts, we focused on n.").
3. **A connective opens most sentences after the first.** "Nevertheless,", "Hence,", "Thus,", "Indeed,", "Furthermore,", "Moreover,", "In other words,", "That being said,", "On another note,", "Recall that". The reasoning is visible in the joins.
4. **A hedge is a belief verb plus a reason.** "We believe this may be because", "We hypothesize", "We theorize", "we suspect (and preliminary tests show)", "presumably because", "likely because", "potentially due to". The paper never hedges without saying why.
5. **Claims are scoped out loud.** "we do not claim that the procedure retrieved the 'true' n". Graded qualifiers do the rest: "moderate", "somewhat", "mostly", "decent", "to some extent".
6. **Limitation, then concession, then what is still worth having.** "Here, admittedly, the values of parameters obtained via inversion" is followed two sentences later by "Nevertheless, we expect these values to be highly correlated". A mixed result is weighed both ways ("has some promise but also some limitations. It is promising because ... It is simultaneously challenging because").
7. **Future work sits inside the paragraph that raises the problem**, not in a closing list: "Future work with large-DA studies can address this hypothesis."; "we leave this evaluation for future effort"; "In the future, it will be interesting to see if".
8. **Plain, slightly informal candor.** "While it is a pity that", "the deviation was not huge", "As expected,", "Interestingly,", "As a side note,".
9. **The Introduction runs stake → practice → gap → work → numbered questions.** The gap opens "Nevertheless, it was unclear if"; the work opens "In this work, we developed"; three numbered research questions follow, and one sentence of promise closes the section.
10. **Sections open with a roadmap or a topic sentence that states the finding.** "In the following, we first discuss our synthetic experiments (Section 3.1)"; "The real-world data experiment showed satisfactory streamflow routing". No run-in labels, no bullet lists outside the research questions.
11. **Conclusions restate, qualify with "but"/"yet", and end on future work.** They open "In this work, we used", give each finding with its qualification in the same sentence, and close with "future work should also consider whether".
12. **Terms are glossed in parentheses at first use**, e.g. a "parameterization scheme" is explained in a parenthesis the moment it appears.

What this means for `revisions.tex`: it is already first person and already frank, but it is **more clipped and more list-like** than the WRR paper. Its typical faults against this profile are short verdict sentences with no connective ("That value is an artifact of pooling two survey days."), slogans repeated to satisfy a rule ("an observation worth testing"), run-in bold and italic labels in place of topic sentences, limitations stated as a row of "We have no ..." sentences without the concession-and-value turn, and future work gathered into one checklist sentence. The rewrites below lengthen and join sentences, put a connective at the joins, give each hedge its reason, and attach future work to the limitation it would resolve.

### Rewrites

**C1. Abstract, L52 (middle). Result sentences are stacked without joins; the within-day point arrives before the reader knows there were several days.** *(changed)*
Current: "Comparisons were valid only within a single survey day: pooling two survey days created an apparent 18~$\mu$S/cm step at one fault that fell to a non-significant 1.6~$\mu$S/cm within a day. Of three fault crossings, only one showed a small significant increase (4.3~$\mu$S/cm), and it was a gradual rise beginning about 1.6~km upstream rather than a step at the fault. No conductance breakpoint coincided with a fault, while the tributary junction at Site 3 lowered conductance as mixing predicts. Road proximity, wastewater discharges and salt stored in soils remain plausible alternative sources. This low-cost survey therefore does not clearly show fault-routed transport. We outline a falsifiable test combining ..."
Proposed: "Of three fault crossings, only one showed a significant increase, and it was small (4.3~$\mu$S/cm) and gradual, beginning about 1.6~km upstream of the fault and not at it. No conductance breakpoint coincided with a fault, while conductance fell at the tributary junction at Site 3, in the direction mixing predicts. We also found that zones could only be compared within a single survey day: pooling two survey days created an apparent 18~$\mu$S/cm step at one fault, which fell to a non-significant 1.6~$\mu$S/cm within a day. Road proximity, wastewater discharges and salt stored in roadside soils remain plausible alternative sources. Hence, we do not claim that this low-cost survey shows fault-routed transport, but we use it to outline a falsifiable test combining ..." (rest unchanged).

**C2. L59 and L61. Two short orphan sentences with no join.** *(changed)*
Current (L59): "Application rates vary widely between jurisdictions \citep{jamshidi2020}."
Proposed: fold into the first sentence: "... and its use has climbed steadily decade over decade \citep{tiwari2018,jackson2005}, although application rates vary widely between jurisdictions \citep{jamshidi2020}."
Current (L61): "Road salt reaches groundwater, in some settings partly through leakage from salt-laden streams \citep{rivett2016}. Through exchange between groundwater and streams, summertime stream salt concentrations have continued to rise, ..."
Proposed: "Road salt also reaches groundwater, in some settings partly through leakage from salt-laden streams \citep{rivett2016}, and through this exchange between groundwater and streams, summertime stream salt concentrations have continued to rise, ..."

**C3. L63 (end). The gap is stated flatly; the WRR Introduction opens its gap with "Nevertheless, it was unclear if".** *(changed)*
Current: "These studies leave open whether faults carry road salt and deliver it to streams: the Maine evidence links salt to bedrock fractures rather than to a particular fault, and we found little direct evidence that faults route highway road salt to surface water. Resolving this matters because it would identify streams at risk through a fault even where no road runs nearby."
Proposed: "Nevertheless, it remains unclear whether faults carry road salt and deliver it to streams. The Maine evidence links salt to bedrock fractures and not to a particular fault, and we found little direct evidence that faults route highway road salt to surface water. Resolving this is important because, if faults do act in this way, a stream could be at risk through a fault even where no road runs nearby."

**C4. L69–71. The question and the framing sentence; "The study is a ... study" reads as a label.** *(changed)* **[letter quote: `L:intro-framing`, letter lines 70 and 115]**
Current (L69): "We ask whether sharp increases in stream salinity coincide spatially with mapped high-angle faults in a way consistent with ..."
Proposed: "In this work, we ask whether sharp increases in stream salinity coincide spatially with mapped high-angle faults in a way consistent with ..." (rest unchanged; the "First ... Second ... Third" predictions already match the WRR paper's numbered questions and should stay).
Current (L71): "We test these predictions with a case study of Wappinger Creek ... We focused on reaches where mapped high-angle faults cross the channel. The study is a hypothesis-generating screening case study: it can show whether the predicted pattern is visible in a low-cost survey, and what a conclusive test would require, but it cannot by itself demonstrate that faults transport road salt."
Proposed: "We examined these predictions with a case study of Wappinger Creek in Dutchess County, New York, combining dense longitudinal surveys of specific conductance, mapped fault traces, and a single chloride transect, and focusing on reaches where mapped high-angle faults cross the channel. We present this work as a hypothesis-generating case study: a low-cost survey of this kind can show whether the predicted pattern is visible, and what a conclusive test would require, but we do not claim that it can, by itself, demonstrate that faults transport road salt."

**C5. L109. A list of things not done, with no reason given.** *(changed)*
Current: "At Site 3 the two survey days differ by a large offset (about 28~$\mu$S/cm; Section~\ref{sec:contrasts}), larger than any of the contrasts we test. We did not pool days, add a day covariate, or correct for the offset. Contrast D is therefore tested on 19 October, and Contrast E on 26 October."
Proposed: "This matters at Site 3, where conductance on the two survey days differed by about 28~$\mu$S/cm (Section~\ref{sec:contrasts}), which is larger than any of the contrasts we test. We chose not to pool the two days or to subtract the offset, because the reach surveyed on both days shows that the offset is not constant along the channel. Thus, Contrast D is tested on 19 October and Contrast E on 26 October." Then add the motive sentences from B1(a).

**C6. L141. A technical aside that reads as a rebuttal, then a clipped sentence.** *(changed)*
Current: "On 19 October the two tests disagree, so by the criterion in Section~\ref{sec:stats} this contrast does not meet our robustness criterion; the Mann--Whitney $p$ is an asymptotic value computed with ties and groups of only 6 and 3 points, for which the smallest attainable exact $p$ is about 0.024. The downstream zone has only three points, so these tests have little power."
Proposed: "On 19 October the two tests disagree, and hence this contrast does not meet the robustness criterion of Section~\ref{sec:stats}. We believe the disagreement says more about the sample than about the stream, because with groups of only six and three points the Mann--Whitney test cannot return an exact $p$ below about 0.024, and the downstream zone has only three points on either day, so both tests have little power."
Also give the 26 October Mann–Whitney value that Table 1 has and the text omits: "($p < 0.001$; Mann--Whitney $p = 0.012$; adjusted $p = 0.041$)".

**C7. L150. Passive, clipped, and written as if correcting something the reader has seen.** *(changed)* **[letter quote: `L:pooling`, letter line 255]**
Current: "When the two survey days are pooled, Contrast E appears as a rise of $+18.0$~$\mu$S/cm ($p < 0.001$), larger than any other step in the survey. That value is an artifact of pooling two survey days. Zone 3-3 would then combine 11 points from 19 October (333.4~$\mu$S/cm) with 6 from 26 October (358.8~$\mu$S/cm), giving a pooled mean of 342.4~$\mu$S/cm, whereas Zone 3-4 consists only of 26 October points. The ``step'' is the difference between days, not a change along the channel;"
Proposed: "The within-day rule matters most at Contrast E. When we pooled the two survey days, as a first analysis of the Site 3 data naturally would, Contrast E appeared as a rise of $+18.0$~$\mu$S/cm ($p < 0.001$), larger than any other step in the survey. However, this value is an artifact of the pooling: Zone 3-3 then combines 11 points from 19 October (333.4~$\mu$S/cm) with 6 from 26 October (358.8~$\mu$S/cm), giving a pooled mean of 342.4~$\mu$S/cm, while Zone 3-4 consists only of 26 October points. In other words, the ``step'' is the difference between days and not a change along the channel;" (rest unchanged).

**C8. L200. A slogan in place of reasoning, used twice.** *(changed)*
Current: "Contrast B is an observation worth testing, not evidence of fault transport. It is a gradual rise that begins roughly 1.6~km upstream of the zone boundary, which marks the fault position we interpreted in the field at an abrupt channel bend, along a reach where the county-scale fault trace runs parallel to the creek and cannot show where the fault meets the channel. A rise of this kind is what diffuse groundwater input, or a fault-parallel flowpath delivering water along the reach, would both produce, and the survey cannot tell them apart."
Proposed: "Although Contrast B is statistically significant, we do not claim it as evidence of fault transport. The rise is gradual and begins roughly 1.6~km upstream of the zone boundary, which marks the fault position we interpreted in the field at an abrupt channel bend, along a reach where the county-scale fault trace runs parallel to the creek and cannot show where the fault meets the channel. A rise of this kind could be produced either by diffuse groundwater input or by a fault-parallel flowpath delivering water along the reach, and our survey cannot tell the two apart. Nevertheless, we believe Contrast B is worth testing further, because it is the one place where conductance rose along a fault-controlled reach."
Current (later in L200): "The 2020 chloride transect adds a further observation worth testing: its peak lies near the Contrast D fault points ..."
Proposed: "The 2020 chloride transect is interesting in the same limited way, as its peak lies near the Contrast D fault points ..." Keep `L:disc-D`, `L:disc-E` and `L:disc-clpeak` sentences as they are (all three are letter quotes).

**C9. L202. Over-confident (see D1), and a three-word topic sentence.** *(changed)*
Current: "The tributary contrast is an internal check. Contrast C decreases conductance on both days, as two-end-member mixing predicts when lower-conductance water joins the main stem \citep{genereux1998}, so the survey can detect a known input of the size we are discussing."
Proposed: "The tributary contrast serves as an internal check, although admittedly a weak one. Conductance was lower below the junction on both days, which is the direction two-end-member mixing predicts when lower-conductance water joins the main stem \citep{genereux1998}. However, the downstream zone has only three points, the two tests disagree on 19 October, and conductance was already falling along the reach above the junction (Figure~\ref{fig:changepoint}), so we cannot say how much of the decrease the tributary itself supplies. Hence, we take Contrast C as an indication that the survey responds to a known input, and not as a measure of how small an input it can detect."
Matching edits: L141 last sentence "thus behaves as mixing predicts" → "is thus in the direction mixing predicts"; L241 "The tributary contrast behaved as mixing predicts, which gives us some confidence that the survey can detect a known input." → "Conductance fell at the tributary junction, in the direction mixing predicts, which gives us some confidence that the survey responds to a known input."

**C10. L204. Clipped opener and aside; the screening sentence is good and should stay.** *(changed)*
Current: "The size of the differences also matters. The stated accuracy of the conductivity measurement is a bound on absolute error, and ..." and "Site 1, where a coincident tributary and very high flow after rain confound the only contrast, contributes little either way."
Proposed: "Furthermore, the differences we are discussing are small relative to what the instrument can resolve. The stated accuracy of the conductivity measurement is a bound on absolute error, and ..." and "Site 1 contributes little either way, because a coincident tributary and very high flow after rain confound its only contrast." Leave `L:disc-size` and `L:disc-screening` wording intact (letter quotes).

**C11. L208–216. Four italic run-in labels turn the subsection into a list; the WRR paper uses linked topic sentences.** *(changed)*
Proposed: delete "\emph{Road proximity.}", "\emph{Developed land.}", "\emph{Wastewater.}" and "\emph{Diffuse groundwater.}" and open the paragraphs as follows.
- L210: "We first considered the roads themselves. Per-zone median distances from survey points ..."
- L212: "Developed land is a second possible source, as stream conductance also rises near developed land from sources unrelated to faults or highways, such as residential runoff and lawn and agricultural fertilizers. Site 2 runs beside US 44 and ends near the settled area around Titusville (Figure~\ref{fig:site2}); we did not quantify land cover, and thus cannot weigh this source."
- L214: "Wastewater is a third possibility, and for Contrast B we believe it is the most specific one. \citet{kelly2008} estimated ..."
- L216: "Finally, groundwater unrelated to faults can enter the creek anywhere along a reach. Such diffuse inputs would raise conductance gradually downstream rather than in a step, and ..."
Keep the `L:alt-start`, `L:alt-road`, `L:alt-season` and `L:alt-wwtp` sentences as they are (letter quotes). `L:alt-withdraw` is dealt with in B4 **[letter quote, letter line 341]**.

**C12. L220. One flat sentence where R1.13 asked for a comparison.** *(changed: the rhetorical question is gone, since the WRR paper does not use them)*
Current: "The studies of fault-zone hydrogeology in the Introduction, including those in New England metamorphic bedrock \citep{caine1996,bense2013,manda2008,kim2014}, make fault-routed delivery plausible, but none of them involves road salt, and none tests it."
Proposed: "Our mixed result is not at odds with what is known about faults in rock like ours. The conduit--barrier model does not predict that every fault leaks, as a fault may carry water along its damage zone, block flow across its core, or do both, depending on its architecture and setting \citep{caine1996,bense2013}. In New England metamorphic bedrock, structural control has been shown at the scale of wells, through foliation-parallel fractures that raise connectivity and add anisotropy \citep{manda2008} and through a thrust fault that influences well yield and water chemistry \citep{kim2014}. Thus, a survey in which one of three faults shows a small rise and two show none does not tell us whether the other two faults act as barriers, are not connected to a source of salt, or simply discharge too little to register in the thalweg. These studies make fault-routed delivery plausible, but none of them involves road salt, and hence none of them tests it."
(Uses only claims already made at L63 and L79.)

**C13. L224. Verdict sentences.** *(changed)* **[letter quote: `L:mgmt`, letter line 372]**
Current: "The evidence here does not justify changing deicing practice on the basis of fault locations. Mapped faults are at most a candidate screening layer, to be tested with the design in Section~\ref{sec:limits} before any use in salt management."
Proposed: "We do not claim that the evidence here justifies changing deicing practice on the basis of fault locations. Mapped faults are, at most, a candidate screening layer, and future work should test them with the design in Section~\ref{sec:limits} before they are put to any use in salt management."

**C14. L229. A meta sentence, then two "We have no ..." sentences with no turn toward what would fix them.** *(changed)* **[letter quotes: `L:lim-discharge`, `L:lim-tracers`, letter lines 177 and 179]**
Current: "Several limitations constrain how far these results can be taken, and we state them plainly because they shape what the survey can and cannot say. We have no discharge measurements, so we cannot estimate the volume of any groundwater input, convert conductance to load, or separate dilution from addition. We have no source tracers, so we cannot attribute salt to roads, wastewater or other sources."
Proposed (lighter option, keeps both letter quotes verbatim): "Admittedly, several limitations constrain how far these results can be taken." followed by the two sentences unchanged.
Proposed (fuller option, in the WRR pattern of limitation plus remedy; changes both letter quotes): "Admittedly, several limitations constrain how far these results can be taken. We have no discharge measurements, and thus we cannot estimate the volume of any groundwater input, convert conductance to load, or separate dilution from addition. Similarly, we have no source tracers, so we cannot attribute salt to roads, wastewater or other sources. Future work with paired discharge and tracer measurements could address both of these gaps (see below)."

**C15. L231–235. Clipped limitation sentences.** *(changed)*
Current (L233): "The chloride data are weaker still. They come from a single transect in a different year, measured with ..."
Proposed: "The chloride data are more limited still, as they come from a single transect in a different year, measured with ..."
Current (L235): "Statistically, our zones contain only three to eleven points. Finally, three fault contrasts in one lithology cannot support a general statement about faults; testing whether any pattern holds would need many crossings in several rock types."
Proposed: "Moreover, our zones contain only three to eleven points, so the tests have little power and the autocorrelation used to discount them is itself poorly determined. Finally, three fault contrasts in one lithology cannot support a general statement about faults, and we leave it to future work with many crossings in several rock types to test whether any pattern holds."
Current (L235, earlier): "This is admittedly a weakness for a study whose hypothesis is spatial: if a mapped trace is off by a few hundred meters, a real step could fall outside the zone boundaries we tested. Field mapping of the fault zone at each crossing would remove this uncertainty."
Keep. This is already the WRR pattern (admission, reason, remedy). `L:lim-faultpos` is a letter quote; do not change "cannot say how far a real fault lies from any mapped position".

**C16. L237. Future work as one checklist sentence; the WRR paper spreads future work over linked sentences and names what each would settle.** *(changed)* **[letter quotes: `L:td`, `L:td-pitfall`; keep their first sentences]**
Current: "Paired discharge measurements would turn conductance into load and separate dilution from addition; chloride-to-bromide ratios would fingerprint deicing salt against wastewater and other sources \citep{mullaney2009}; and environmental age tracers would indicate whether water entering near a fault is older groundwater \citep{cook2022}. Repeated cross-channel and depth readings would show whether small contrasts exceed lateral variation, fault zones should be located in the field rather than from county maps, and surveys should cover several lithologies and many crossings, with change-point analysis applied to single-day transects so that gradual ramps and abrupt steps can be distinguished."
Proposed: "Future work should pair each survey with discharge measurements, which would turn conductance into load and separate dilution from addition. Furthermore, chloride-to-bromide ratios would fingerprint deicing salt against wastewater and other sources \citep{mullaney2009}, while environmental age tracers would indicate whether water entering near a fault is older groundwater \citep{cook2022}. Repeated readings across the channel and at depth would show whether contrasts as small as ours exceed lateral variation. We also believe that fault zones should be located in the field rather than from county maps, and that change-point analysis should be applied to single-day transects so that gradual ramps and abrupt steps can be distinguished. Finally, surveys covering many crossings in several lithologies would show whether any pattern holds beyond one creek. We hypothesize that, if faults do route road salt to streams, such a design would find a step at a field-located fault that carries a deicing-salt signature and an older age; if it found none, the hypothesis could be set aside for faults of this kind."
(The last sentence states the falsification criterion that the abstract promises. It adds no data; the author should check that it says what they mean.)

**C17. L241–245, Conclusions. The WRR Conclusions open "In this work, we used", qualify each finding in the same sentence, and end on future work; these open on a question, repeat one point twice, and end on a management instruction.** *(changed and extended)*
Current (L241, first sentence): "We asked whether high-angle fault zones route road-salt-contaminated groundwater to Wappinger Creek, and our survey does not answer the question clearly."
Proposed: "In this work, we used longitudinal surveys of specific conductance and a single chloride transect to ask whether high-angle fault zones route road-salt-contaminated groundwater to Wappinger Creek, and our survey does not answer the question clearly."
Current (L243, first sentence): "We believe the most transferable result is methodological."
Keep; it is already in voice.
Current (L245): "Nevertheless, we do not think the hypothesis should be set aside. Studies of fault zones in fractured and metamorphic rock make fault-routed delivery plausible, and our survey was not designed to rule it out. We therefore regard the fault-conduit hypothesis as plausible but unresolved by this survey. A conclusive test would follow the design in Section~\ref{sec:limits}, with single-day surveys, discharge measurements and tracers. Until such a test is done, we suggest that mapped faults be treated as a candidate screening layer to evaluate, not as a basis for changing deicing practice."
Proposed: "Nevertheless, we do not think the hypothesis should be set aside. Studies of fault zones in fractured and metamorphic rock make fault-routed delivery plausible, and our survey could not have ruled it out, so we regard the hypothesis as unresolved. Until it is tested, we suggest that mapped faults be treated as a candidate screening layer to evaluate, and not as a basis for changing deicing practice. Future work should follow the design in Section~\ref{sec:limits}, with single-day surveys, discharge measurements and tracers, and should extend to other creeks and rock types to see whether any pattern holds."

**C18. L79. A mechanism stated with "could in principle"; the WRR paper would mark it as a hypothesis.** *(changed)*
Current: "If the high-angle faults crossing Wappinger Creek are conduits, they could in principle route road-salt-laden groundwater from a highway to the channel even where the two are separated by a topographic divide, which motivated our focus on stream reaches that coincide with mapped fault traces. Whether they do so is the question we test."
Proposed: "We hypothesize that, if the high-angle faults crossing Wappinger Creek are conduits, they could route road-salt-laden groundwater from a highway to the channel, potentially even where the two are separated by a topographic divide. This motivated our focus on stream reaches that coincide with mapped fault traces."

**C19. L119–141, Results. Bold run-in labels and number-first sentences; the WRR results open each block with a topic sentence that states the finding.** *(new)*
Current (L121): "Zones are compared only within a single survey day, so the results are reported survey by survey."
Proposed: "In the following, we first report the zone contrasts survey by survey, then show what pooling the two Site 3 days does to them, and lastly describe the reach that was surveyed on both days."
Current (L123): "\textbf{Site 1, Contrast A (28 September).} Specific conductance fell from 259.9 $\pm$ 0.7~$\mu$S/cm ..."
Proposed: "At Site 1 (28 September), the tributary contrast showed no detectable change. Specific conductance fell from 259.9 $\pm$ 0.7~$\mu$S/cm ..."
Current (L132): "\textbf{Site 2, Contrast B (5 October).} Zone 2-1 averaged ..."
Proposed: "Site 2 (5 October) gave the only significant increase at a fault. Zone 2-1 averaged ..."
Current (L141): "\textbf{Site 3, Contrasts C, D and E (19 and 26 October).} Figure~\ref{fig:site3} shows both days. Contrast C, the tributary junction, is a decrease on both days: ..."
Proposed: "At Site 3 (19 and 26 October; Figure~\ref{fig:site3}), conductance fell at the tributary junction on both days, while neither fault contrast showed a significant increase. Contrast C, the tributary junction, was a decrease of ..."
If the bold labels are wanted for navigation, keep them and add the topic sentences after them. `L:contrastD` and `L:contrastE` wording is quoted in the letter and is not touched.

**C20. L152. The day offset is described but no reason is offered; the WRR paper always attaches one ("We believe this may be because").** *(new; needs the author)*
Current: "The offset is therefore not constant, and its range of about 6~$\mu$S/cm exceeds Contrasts B and E, which is why we neither pooled days nor corrected for it."
Proposed: "Hence, the offset is not constant, and its range of about 6~$\mu$S/cm exceeds Contrasts B and E, which is why we neither pooled days nor corrected for it. We believe the offset may be because flow changed between the two days, but without discharge measurements we cannot confirm this."
Use the second sentence only if the author does think flow is the likely cause; otherwise write "We do not know what caused the offset, and without discharge measurements we cannot test the obvious candidate, a change in flow." See D3.

**C21. L156. Short result sentences in a row.** *(new)* **[letter quote: `L:cl-E`, letter line 554. Change only if the letter is updated]**
Current: "The transect therefore shows no chloride increase at Contrast E. With so few points downstream of E we did not attempt a two-sample test."
Proposed: "Thus, the transect shows no chloride increase at Contrast E, and with so few points downstream of E we did not attempt a two-sample test."
Current (same line): "The breakpoint is about 125~m from the nearest Contrast D fault point and about 300~m from the nearest trace, but it is driven largely by the single 50~mg/L sample."
Proposed: "Interestingly, the breakpoint is about 125~m from the nearest Contrast D fault point and about 300~m from the nearest trace; however, it is driven largely by the single 50~mg/L sample, and we do not read it as more than that."

**C22. L167. The key interpretive sentence of Section 3.3 is buried mid-paragraph.** *(new)* **[`L:cp-none` and `L:cp-contrastB` are letter quotes; wording kept, only a connective added]**
Current: "Contrast B is therefore better described as part of a gradual downstream ramp than as an abrupt step at the interpreted fault position. At Site 1 and on the 19 October Site 3 transect no breakpoint is selected ..."
Proposed: keep the first sentence verbatim and start a new paragraph after it: "At the other sites, the analysis gave even less indication of a step. At Site 1 and on the 19 October Site 3 transect no breakpoint was selected ..."

**C23. L198. The Discussion opens well; the count of predictions is a semicolon list.** *(new)* **[`L:disc-answer` first sentence is a letter quote; keep it]**
Current: "Of the three predictions in the Introduction, the first, an abrupt step at a fault, is not met at any crossing; the second could not be tested, because Sites 1 and 2 were surveyed at high flow; and the third was examined only with a single chloride transect and no bromide."
Proposed: "Recall that we set out three predictions in the Introduction. The first, an abrupt step at a fault, was not met at any crossing. The second, persistence at baseflow, could not be tested because Sites 1 and 2 were surveyed at high flow, and the third was examined only with a single chloride transect and no bromide. Hence, the survey bears mainly on the first prediction."

**C24. L222 (last sentence). Good content, unhedged.** *(new)*
Current: "Compared with these approaches, a thalweg survey at roughly 100--400~m spacing integrates over the whole channel flow and is less sensitive to focused inputs that vary over 10~m, so it could miss a real fault signal as well as report a spurious one."
Proposed: "Compared with these approaches, a thalweg survey at roughly 100--400~m spacing integrates over the whole channel flow and is presumably less sensitive to focused inputs that vary over 10~m. In other words, a survey like ours could miss a real fault signal as well as report a spurious one."

**C25. L96. An unsupported "likely" with no admission.** *(new)* **[`L:cl-single` is a letter quote; not touched]**
Current: "The transect was sampled in midsummer, when streamflow is likely dominated by baseflow, so elevated chloride is more plausibly from groundwater than from runoff."
Proposed: "We sampled the transect in midsummer, when we expect streamflow to be dominated by baseflow and elevated chloride to come from groundwater more plausibly than from runoff, although we did not measure flow on that day."

**C26. L90. Procedure in the passive where the WRR paper owns its choices.** *(new, minor)*
Current: "Sampling was performed in the thalweg of each study site, which reduced variation due to incomplete lateral mixing."
Proposed: "We sampled in the thalweg at each site to reduce variation due to incomplete lateral mixing."
Current: "A calibration offset shared by all readings on one day cancels when zones are compared within that day; random reading error does not."
Proposed: "A calibration offset shared by all readings on one day cancels when zones are compared within that day, while random reading error does not."

### Passages already in the WRR voice (leave alone)

L67 (tributary mixing, ending "We therefore treat tributary and fault boundaries as distinct kinds of contrast."); L111 (autocorrelation, ending in the sensitivity-check caveat); L204 `L:disc-screening` sentence; L235 "This is admittedly a weakness ..."; L243 "We believe the most transferable result is methodological."

---

## Section D. Other improvements, ranked

**D1. (Highest.) The tributary "internal check" is asserted more strongly than the paper's own figures allow.**
L141, L202, L241 and the abstract say Contrast C "behaves as mixing predicts" and that the survey "can detect a known input". But Figure 6 shows conductance falling steadily along the whole 19 October transect, through the tributary and through the Contrast D boundary, with no breakpoint selected; on the upper 26 October transect it is already falling above the junction and the two segmented breakpoints are 314–473 m from it (L167). The paper applies the test "is there a break at the boundary?" to the faults and not to the tributary. A reviewer who asked for change-point analysis (R1.5(3)) will notice. Section 3.3 should say what the analysis finds at the junction on each day. `docs/analysis_results.md` (the change-point table) lists a change-in-mean shift at 773 m on the upper 26 October transect, which is the junction position, and none at the junction on 19 October; if the author confirms this, it can be reported as it is: partial support on one day, none on the other. Then apply C9. This also makes the screening framing stronger, not weaker.

**D2. Site 3 conductance falls downstream through both fault boundaries on 19 October, and the paper does not say so.**
The fall of roughly 8 µS/cm over about 1.7 km (Figure 6, third panel) is the opposite of what a fault input predicts and is the plainest pattern in the Site 3 data, yet the text mentions only "no breakpoint is selected" (L167). Add one or two sentences to L167 and one to L200, e.g. "On 19 October conductance fell steadily downstream along the whole reach, through both the tributary junction and the Contrast D boundary, which is the opposite of what a salt-laden fault input would produce." A hedged reason may follow only if the author has one (for example dilution of the upstream Millbrook effluent, L214, which the paper already describes as a continuous upstream source); mark it "we suspect".

**D3. The 28 µS/cm day offset is never explained, even tentatively.**
It is the central fact behind the paper's methodological lesson, and a reader will want to know whether it rained. If the author knows (weather, stage, or a nearby gauge record already in hand), say it; if not, say so in the paper's voice at L152: "We do not know what caused the offset. We suspect a change in flow between the two days, but without discharge we cannot confirm it." No new data are needed for the second form.

**D4. Reorder Results: contrasts → SC change points → chloride.**
Section 3.2 (chloride) currently separates the conductance contrasts (3.1) from the conductance change-point analysis (3.3), and 3.2 uses the segmented method before the reader has seen it applied to conductance. Swap 3.2 and 3.3. Figure numbers change (chloride becomes Figure 6); the letter's figure references must follow.

**D5. Put Tables 1 and 2 where they are used.**
L176 places both tables after Section 3.3, but every number in Section 3.1 comes from them. Move both `table` environments to follow L121. If space is tight, Table 2's "p (Welch)" column duplicates Table 1 and can go.

**D6. Figure 6 draws breakpoints that were not selected.**
The Site 1 and 19 October panels show a solid vertical line and a tan interval for a breakpoint the caption says was not selected. A reader skimming sees five panels with breakpoints. Remove the vertical line and band where BIC selects none, or say in the caption (L172): "for Site 1 and 19 October the dashed fit, its vertical line and its interval show the best one-breakpoint model, which was not selected". Also drop the legend line "Zone labels in boxes; zone ends at boundary lines".

**D7. Redundancy to trim (about 150–200 words; main body stays well above 5,000).**
- Conduit–barrier model: L63 and L79 say the same thing with the same two citations. Keep L63; cut L79 to "This structural setting is central to our hypothesis (Section 1). If the high-angle faults ..."
- Site 2 bend: explained at L92, L132, caption L137, L167 and L200. Keep the full account at L92; at L132 cut "The Zone 2-1/2-2 boundary, about 4.0~km along the survey, is the fault position we interpreted in the field from the abrupt 90$^{\circ}$ channel bend (Section~\ref{sec:sampling})." to "The boundary is the bend described in Section~\ref{sec:sampling}."
- Sampling spacing: L90 ("approximately every 100~m ... about every 400~m") and L92 ("Mean spacing ... 85~m ... 416~m ... 83--118~m"). Keep the L92 numbers; cut the clause in L90.
- "Zones are compared only within a single survey day": L109, L121, caption L146. Cut the L121 opener to "Results are reported survey by survey."
- "largely conjectural": L77 and L235. At L235 write "whose authors call the fault locations largely conjectural (Section 2.1)".
- Instrument accuracy for Contrast B: L132, L204, L231, L241. Drop the parenthesis at L132 ("($\pm$1.7~$\mu$S/cm at 310~$\mu$S/cm)"), already given at L90.

**D8. Section 4.1 title.** "Contrasts" says nothing. Use "What the contrasts show" or "Fault and tributary contrasts".

**D9. Say which predictions each analysis tests, in Methods.**
The Introduction sets up three predictions (L69) and the Discussion closes them (L198), but Methods and Results never mention them. One sentence at the start of Section 2.3: "The zone contrasts and the change-point analysis address the first prediction, an abrupt rise at a fault; the chloride transect bears on the third; we have no test of the second."

**D10. Dense distance sentences in Section 3.3.**
L167 last sentence gives three distances from one breakpoint in one clause ("330~m upstream of where the channel crosses the digitized trace (at 523~m), 123~m in straight-line distance from the nearest trace, and 522~m upstream of the Contrast E boundary"). Lead with the meaning: "This breakpoint is not at the fault by any measure we have: it lies 522~m upstream of the Contrast E boundary and 330~m upstream of where the channel crosses the digitized trace (123~m from the trace in a straight line). It also sits at the three-point minimum segment the method allows, so its position is set partly by the method."

**D11. L90, stray sentence.** "We inferred changes in the salt input to the stream along its length from changes in specific conductance." sits between the instrument and its accuracy. Move it to the start of the paragraph, or cut it (the abstract and L69 already say conductance is the proxy).

**D12. L96, unsupported "likely".** "when streamflow is likely dominated by baseflow, so elevated chloride is more plausibly from groundwater than from runoff". No flow information is given for 20 July 2020. Hedge as an assumption: "We sampled in midsummer on the assumption that streamflow would then be mostly baseflow; we did not measure flow."

**D13. L198, "Our survey offers little support".** Good opening. The following three sentences repeat numbers from Section 3.1; they could be one: "Of the three fault contrasts, only Contrast B shows a significant increase ($+4.3$~$\mu$S/cm); Contrast D is a non-significant decrease and Contrast E a non-significant increase within instrument accuracy."

**D14. Abstract length and keywords.** The abstract is about 290 words; check the journal limit. Keywords repeat "fault lines" where the paper says "fault zones"; "specific conductance" and "groundwater" would index it better.

**D15. Reference-budget margin.** 11 of 35 cited references are from 2022–2026 (31.4%). Any edit that drops a recent citation (shattuck2023, hintz2022, dugan2023, vanmeter2024, kaushal2023saltcycle, kaushal2023factors, hodgins2024, hodgins2026, orr2026, cook2022, adirondack2023) takes the paper below 30%. B9 and C12 above keep all of them.

**D16. After any of these edits.** Run `.venv/bin/python src/letter_linerefs.py`, rebuild the letter, and update every `\mq{}` quote whose sentence was reworded. Rewrites in this report that touch a quoted sentence: C4 (`L:intro-framing`), C7 (`L:pooling`), C13 (`L:mgmt`), C14 fuller option (`L:lim-discharge`, `L:lim-tracers`), C21 (`L:cl-E`), B4 (`L:alt-withdraw`), B9 (position described in the R1.1 response, `L:intro-syndrome`), B11 (`L:m-accuracy`), B14 (`L:cl-peaks`), B16 (`L:site2-bend`), D10 (`L:cp-E-min`). C8, C10, C11, C15, C16, C22, C23 and C25 were written to leave the quoted sentences intact.
