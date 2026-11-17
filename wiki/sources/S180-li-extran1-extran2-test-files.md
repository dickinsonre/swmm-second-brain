---
title: "S180: Extran1 and Extran2 from the Extran Manual (LinkedIn, 2025)"
type: source
raw: raw/linkedin/2025-04-07-extran1-extran2-from-extran-manual-ai-github-swmm5-used-dickinson-ds25e.md
kind: linkedin-article
author: Robert Dickinson
published: 2025-04-07
ingested: 2026-11-16
tags: [extran, test-models, swmm-history, swmm5, icm]
drafted_by: Robert Dickinson, with an input-file summary created with AI help and passages that read as AI-written
reviewed: no
---
**What it is.** One of four articles of April 2025 on the test models of the 1981 EXTRAN manual; this one covers Extran1 (free outfall) and Extran2 (fixed backwater with a tide gate). Raw file: [raw/linkedin/2025-04-07-extran1-extran2-from-extran-manual-ai-github-swmm5-used-dickinson-ds25e.md](../../raw/linkedin/2025-04-07-extran1-extran2-from-extran-manual-ai-github-swmm5-used-dickinson-ds25e.md).

**How it was written.** The four articles share one frame, word for word in most paragraphs: where the file came from, why it was a good test in the 1980s, where it is used now, a summary of the SWMM5 input file "created with AI Help", and the model in ICM. The history and "why it is good" paragraphs read as AI-polished. The .inp summary is an AI-written passage, not checked against the .inp. The siblings are [S181](S181-li-extran5-storage-side-orifice.md), [S182](S182-li-extran-example-6-type-1-pump.md) and [S183](S183-li-extran-example-7-type-2-pump.md). Template slips: this article says the file's "primary function was validating side outlet orifice hydraulics", which is Extran5's subject, and tells the reader to import "the Extran5.inp file".

**Claims worth keeping**
- Extran1 has a free outfall; Extran2 has "fixed backwater with a tide gate". Both come from the 1981 EXTRAN 3 manual (CDM).
- Bob: "I alone have run it hundreds of times for decades."
- The prose dates the file's uses: 1981, with the EXTRAN 3 manual on mainframes; 1988, the SWMM3 to SWMM4 transition; 2006, SWMM5 compared with SWMM4. The bullet list of the same article says "SWMM3 → SWMM4 transition validation, 1981" and "SWMM4 → SWMM5 algorithm verification, 1988" (Q93).
- It is among the test files of EPA's 2006 quality assurance report by Lewis Rossman ([S185](S185-epa-swmm5-qa-report-dynamic-wave-2006.md)), in the ZIP files of the SWMM5 download archived in 2006, and in EPA's GitHub test suite.
- Bob: it is used in InfoWorks ICM SWMM network daily build validation and in Autodesk Water InfoDrainage.
- The .inp imports into ICM SWMM and ICM InfoWorks networks, and an imported ICM SWMM network can be converted inside ICM to an InfoWorks network.
- The 1981 manual printed both the input files and the model output; the input was in fixed format. A caption calls the set "Seven Classic SWMM5 Hydraulics Test Files from Extran3 in 1981 later used in SWMM4 and SWMM5 Testing".
- AI-written passage, not checked against the .inp: Extran2's outfall 10208 has a fixed stage of 94.4 ft with a flap gate and an invert of 89.9 ft; 9 junctions and 9 conduits; three triangular inflows peaking at 45, 50 and 40 cfs at nodes 80408, 81009 and 82309; dynamic wave, 15-minute reporting, 8 hours on 1 January 2002.

**Checked at ingest.** The stage of 94.4 ft agrees with the Rosetta Stone's conversion of Example 2, and the three peaks with its Example 1 deck [S186](S186-st-venant-rosetta-stone-app-md-v2-6-2.md). The QA report describes Example 2 the same way: Example 1 with a fixed-elevation outfall at node 10208 and a tide gate [S185](S185-epa-swmm5-qa-report-dynamic-wave-2006.md).

**Feeds:** [The EXTRAN manual test models](../concepts/extran-manual-test-models.md), [EXTRAN](../entities/extran.md).
