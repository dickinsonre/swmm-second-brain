---
title: EXTRAN III Workbench (app)
type: entity
updated: 2026-11-15
sources: [S05, S74, S81]
tags: [apps, swmm-history, extran, verification, hydraulics]
reviewed: no
---
Bob's browser app that runs EXTRAN III, the 1981 Extended Transport block of SWMM 3, from the FORTRAN listing printed in its user's manual, beside EPA SWMM 5.2.4. Version 1.6.0, 11 November 2026 [S74](../sources/S74-extran3-workbench-app-md.md). The program itself is on [EXTRAN](extran.md).

**It answers three questions** [S74](../sources/S74-extran3-workbench-app-md.md)
1. Does the rebuilt program reproduce Camp Dresser & McKee's printed 1981 runs?
2. What does the 1981 method give on a modern SWMM 5 model, next to SWMM 5?
3. What does SWMM 5 give on a 1981 deck?

**What is in the file** [S74](../sources/S74-extran3-workbench-app-md.md)
- Four EXTRAN III engines: as printed, and with ten 1981 bugs fixed, each at the 1981 array sizes and with enlarged arrays.
- EPA SWMM 5.2.4.
- The seven manual example decks with their printed results, 164 SWMM 4 EXTRAN decks from January 2003, and ten SWMM 5 sample models.

**Against the 1981 printout.** Of 2,424 printed values in the seven examples, the browser engine matches 2,253 exactly (92.9 %), and 98.4 % counting last-digit and OCR-confusion differences [S74](../sources/S74-extran3-workbench-app-md.md). The method is on [Verification against printed runs](../concepts/verification-against-printed-runs.md).

**The ten fixes.** The "bugs fixed" engines change ten places and nothing else [S74](../sources/S74-extran3-workbench-app-md.md):

| Card | As printed |
|---|---|
| DEPTHX 95 | A hydraulic radius uses `DTEMP`, which is never set |
| DEPTHX 96-97 | `HRAD**0.677` where 0.6667 is meant |
| DEPTHX 56 | A rectangle's "radius" was its wetted perimeter |
| HEAD 86 | `CALL HYDRAD(...,AMID,RMID)` where `BMID` is meant |
| HYDRAD 45 | A closed rectangle never ran full |
| TRANSX 340 | The iteration limit is fixed at 30 |
| TRANSX 459 | `ASTORE(J)` where `ASTORE(I)` is meant |
| BOUND 229 | Pumped outflow not limited to the pump rate |
| BOUND 234 | `YDEP(J2)` where `YDEP(J1)` is meant |
| OUTPUT 62 | The continuity figure leaves out the starting volume |

The HYDRAD 45 fault is the one the [Bellinge (app)](bellinge-app.md) essay blames for EXTRAN III as printed diverging on a branch with closed rectangles [S81](../sources/S81-bellinge-summary.md).

**A run-length finding.** TRANSX runs whole passes of (NTCYC+99)/100 steps, so a deck asking for 1,080 steps runs 1,089 [S74](../sources/S74-extran3-workbench-app-md.md).

**On modern models.** Of 257 corpus models at 1981 sizes, 207 run through both engines. Enlarged arrays (5,000 junctions and links) let 16 of the 34 too-big models run, the largest with 2,055 nodes. Of those 16, EXTRAN III's continuity is within 5 % in 2 and prints asterisks in 5: "larger arrays do not make the 1981 explicit method stable on large models" [S74](../sources/S74-extran3-workbench-app-md.md). The converters are on [Converting SWMM 5 models for older engines](../concepts/converting-swmm5-models-for-older-engines.md).

**What no person has checked.** 139 doubtful listing lines against images of the manual pages, as [S05](../sources/S05-swmm5org-article-facts.md) also recorded in October; and every statement of the essay against the code [S74](../sources/S74-extran3-workbench-app-md.md).

**Open.** [S05](../sources/S05-swmm5org-article-facts.md) says the converter ran on 259 models; [S74](../sources/S74-extran3-workbench-app-md.md) says 257 (Q51). Its summary records no Netlify address and no repository. See [Open questions](../open-questions.md).
