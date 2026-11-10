# Cover letter revision plan (JHEWS-101225, round 1)

Scope: the cover letter is everything before `\editor` in `response_to_reviewers.tex`.
This is a plan only; the cover letter has not been edited. All facts below were
checked against `revisions.tex`, `original.tex` and the editor's comments docx on
2026-11-09.

## 1. What the editor asked for, and whether the cover letter says it is done

| Editor request (NOTES in the comments docx) | Status in the current cover letter | Proposed sentence |
|---|---|---|
| 1. A revised manuscript with the changes highlighted | Only implied, in the conventions paragraph ("line number in the highlighted-changes manuscript"). Never stated as a submitted item. | "We submit the revised manuscript, a version with all changes highlighted, and this point-by-point reply as separate files." |
| 2. A separate point-by-point reply to the reviewers | Not stated; the letter simply is one. | Covered by the sentence above. |
| 3a. Do not add, remove or alter any author | Not mentioned. True in the revision: same two authors, same order, same emails. | "The author list and order are unchanged." |
| 3b. Complete missing names, emails, affiliations | Not in the cover letter. Response E.1 mentions only the first author's affiliation. The revision also adds ORCIDs for both authors. | "We completed the author information: the first author's affiliation (Marist University, where the work was done) and both ORCIDs are now given." Also enter the same details in the OIS form (see the `\plan` note under E.1). |
| Editor's comment: publication provided the reviewers' points are addressed | Answered in E.1, not in the cover letter. | "We have responded to every point raised by Reviewers 1 and 2; Reviewer 3 recommended minor revisions without specific comments." |

## 2. Main changes the cover letter should summarize, tied to comments

1. **Reframing and new title** (R1 general, R1.13, R2 general). The paper is now a
   hypothesis-generating case study; the title is a question. The current draft
   covers this ("toned down the conclusions, and scope") and gives the title
   correctly. Keep, tighten.
2. **Within-day comparisons after the Site 3 day-pooling issue** (R1.7, R2.6, R2.8).
   The current draft calls this "small changes to the presentation of the results".
   That understates it. State plainly: Site 3 was surveyed on two days whose
   conductance differed by about 28 µS/cm; the submitted analysis pooled them;
   compared within a single day, Contrast E falls from +18.0 to +1.6 µS/cm and is
   no longer significant; one of three fault contrasts (not two) now shows a
   significant increase; the Discussion now says the survey offers little support
   for the hypothesis.
3. **Change-point analysis and autocorrelation** (R1.5(3), R1.8). Segmented
   regression and a change-in-mean check on each single-day transect (new Figure 5)
   find no breakpoint at a fault contrast boundary; the Site 2 increase is a gradual
   rise beginning about 1.6 km upstream of the boundary. Effective-sample-size
   adjusted p-values are reported as a sensitivity check (new Table 2).
4. **Statistics reporting and data** (R1.6, R1.9, R2.2, R2.3, R2.15). Normalization
   removed; Table 1 rebuilt with SD, CI, df and Mann-Whitney; all measurements in
   Appendix A.
5. **Alternative sources and limitations** (R1.5(1), R1.5(2), R1.12, R2.5, R2.9).
   New Section 4.2 (roads, developed land, wastewater plants, diffuse groundwater)
   and Section 4.4 (limitations and a test of the hypothesis).
6. **Introduction and literature** (R1.1 to R1.4, R2.1). Fault hydrogeology now
   rests on Caine et al. (1996), Bense et al. (2013) and metamorphic-bedrock
   studies; predictions are referenced; tributary-mixing paragraph added.
7. **Figures** (R2.4, R2.10 to R2.14). All maps redrawn: single-panel Figure 1,
   contrasts labeled, flow arrows, survey days distinguished and inset at Site 3,
   Z–Z' drawn on Figure 4; Figure 6 is the chloride transect.
8. **What could not be done** (R1.5(1), R2.5, R2.6). No new field data: discharge,
   tracers, repeated cross-channel readings and field location of faults are
   handled as limitations and future work. The current draft says this; keep.

## 3. Specific problems in the current draft

| Problem | Where | Suggested fix |
|---|---|---|
| Date "8 November 2026" | line 53 | Set to the actual submission date. |
| "Thank you, and thank the three Reviewers, for thoughtful review" (grammar) | para 1 | "Thank you and the three Reviewers for the thoughtful review of our manuscript (JHEWS-101225)." Add the manuscript ID. |
| "toned down the conclusions, and scope, of the paper to better indicate that we conducted a case study" (stray commas, vague) | para 1 | "We have narrowed the scope and conclusions and now present the paper as a hypothesis-generating case study." |
| "There were small changes to the presentation of the results." (understates; the main result changed) | para 2 | Replace with the plain statement in item 2 above. |
| "To better address/resolve reviewer comments on site three" (slash, "site three") | para 2 | "In answering the Reviewers' comments on Site 3 (R1.7, R2.6, R2.8) ..." |
| "This provides more confindence in our responses.We could not" (typo, missing space, vague) | para 2 | Delete the sentence; the consequence of the split is stated instead. Start "We could not collect ..." as a new sentence. |
| "Table 1, Table 2 and the Appendix A table are new or replaced, with captions marked." | conventions para | In `revisions_diff.pdf` the Table 1 and Table 2 captions are marked, but the Table A1 caption is not (it lives in the `\input` file). Either say "the Table 1 and Table 2 captions are marked" or mark the appendix caption. |
| No mention of the change-point analysis, alternative sources, limitations, new figures/tables | whole letter | Add one sentence each (see draft). |
| No statement on the editor's notes 1 to 3 | whole letter | Add the sentences from section 1. |
| The highlighted PDF prints "Equation ??" in struck-out text (diff line 258), because the removed normalization equation label no longer exists | not the letter, but the reader of the letter sees it | Mention nothing in the letter; consider fixing in the diff build. |

## 4. Proposed cover letter (about 330 words)

> [submission date]
>
> Dear Editor,
>
> Thank you and the three Reviewers for the thoughtful review of our manuscript
> (JHEWS-101225). We appreciate the feedback. We have narrowed the scope and
> conclusions and now present the paper as a hypothesis-generating case study. The
> title is now "Do fault zones route road-salt-contaminated groundwater to streams?
> A Hudson Valley, NY Case Study".
>
> The main result has changed. In answering the Reviewers' comments on Site 3
> (R1.7, R2.6, R2.8) we found that the submitted analysis pooled two survey days
> whose conductance differed by about 28 µS/cm. We now compare zones only within a
> single survey day. This removes the large increase at Contrast E (+18.0 becomes
> +1.6 µS/cm, not significant), so one of three fault contrasts, not two, shows a
> significant increase, and we now state that the survey offers little support for
> the hypothesis. As Reviewer 1 suggested (R1.5(3)), we added a change-point
> analysis; it finds no conductance breakpoint at a fault contrast boundary and
> shows the Site 2 increase to be a gradual rise. We also added an autocorrelation
> check (R1.8), a section on alternative sources (R1.12, R2.9), a limitations
> section, the full data in Appendix A (R2.3), and revised every figure as
> Reviewer 2 requested.
>
> We could not collect new field data for this revision, so requests that need new
> measurements (discharge, tracers, repeated cross-channel sampling) are handled as
> limitations and future work.
>
> We submit the revised manuscript, a version with all changes highlighted, and
> this point-by-point reply as separate files. The author list and order are
> unchanged; we completed the author information by adding the first author's
> affiliation and both ORCIDs.
>
> Reviewer comments are in gray italics; our responses are in black. A reference
> such as {L135} is a line number in the highlighted-changes manuscript. latexdiff
> does not highlight tables read from separate files; Table 1, Table 2 and the
> Appendix A table are new or replaced, with the Table 1 and Table 2 captions
> marked.
>
> Sincerely,
> Tadd Bindas and Zion Klos

Notes on the draft:
- In the `.tex`, keep `\textcolor{commentcolor}{\textit{gray italics}}` and
  `\Ln{intro-framing}` in the conventions paragraph rather than the literal
  "{L135}" shown here.
- Every number is already in `revisions.tex` (28, +18.0, +1.6 µS/cm; one of three
  contrasts); no new claims are introduced.
- Sentences kept from the author's draft: the thanks, the title sentence, the
  "could not collect new field data" sentence, and the conventions paragraph.
