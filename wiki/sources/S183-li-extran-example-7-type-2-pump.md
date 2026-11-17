---
title: "S183: Example 7 of the Extran Manual, Type 2 Pump (LinkedIn, 2025)"
type: source
raw: raw/linkedin/2025-04-07-example-7-extran-manual-type-2-pump-ai-github-swmm5-dickinson-pj38e.md
kind: linkedin-article
author: Robert Dickinson
published: 2025-04-07
ingested: 2026-11-16
tags: [extran, test-models, pumps, swmm5, icm]
drafted_by: Robert Dickinson, with an input-file summary created with AI help and passages that read as AI-written
reviewed: no
---
**What it is.** The article on Example 7 of the 1981 EXTRAN manual, an in-line pump. Raw file: [raw/linkedin/2025-04-07-example-7-extran-manual-type-2-pump-ai-github-swmm5-dickinson-pj38e.md](../../raw/linkedin/2025-04-07-example-7-extran-manual-type-2-pump-ai-github-swmm5-dickinson-pj38e.md).

**How it was written.** The four articles share one frame, word for word in most paragraphs: where the file came from, why it was a good test in the 1980s, where it is used now, a summary of the SWMM5 input file "created with AI Help", and the model in ICM. The history and "why it is good" paragraphs read as AI-polished. The .inp summary is an AI-written passage, not checked against the .inp. Template slips: the AI summary is headed "Summary of the Extran6.inp" though it describes Example 7, the ICM caption says "Extran 6 Model", and the reader is told to import "the Extran5.inp file".

**Claims worth keeping**
- A Type 2 pump, in Bob's words: "An in-line pump where flow increases incrementally with inlet node depth."
- The prose dates the file's uses: 1981, with the EXTRAN 3 manual on mainframes; 1988, the SWMM3 to SWMM4 transition; 2006, SWMM5 compared with SWMM4. The bullet list of the same article says "SWMM3 → SWMM4 transition validation, 1981" and "SWMM4 → SWMM5 algorithm verification, 1988" (Q93).
- It is among the test files of EPA's 2006 quality assurance report by Lewis Rossman ([S185](S185-epa-swmm5-qa-report-dynamic-wave-2006.md)), in the ZIP files of the SWMM5 download archived in 2006, and in EPA's GitHub test suite.
- Bob: it is used in InfoWorks ICM SWMM network daily build validation and in Autodesk Water InfoDrainage.
- The .inp imports into ICM SWMM and ICM InfoWorks networks, and an imported ICM SWMM network can be converted inside ICM to an InfoWorks network.
- The 1981 manual printed both the input files and the model output; the input was in fixed format. A caption calls the set "Seven Classic SWMM5 Hydraulics Test Files from Extran3 in 1981 later used in SWMM4 and SWMM5 Testing".
- AI-written passage, not checked against the .inp: 9 junctions, 1 free outfall, 9 conduits; pump 90010 from 82309 to 15009 on a curve of 5 cfs at 8 ft, 10 cfs at 25 ft and 20 cfs at 100 ft; no control rules; dynamic wave with a 20-second step.

**Checked at ingest.** The deck says 5, 10 and 20 cfs below 8 ft, below 25 ft and above 25 ft of depth; the Rosetta Stone wrote the last point at 42.7 ft in its own conversion [S186](S186-st-venant-rosetta-stone-app-md-v2-6-2.md). Both are ways of writing "above 25 ft".

**Feeds:** [The EXTRAN manual test models](../concepts/extran-manual-test-models.md), [Pumps and pump curves](../concepts/pumps-and-pump-curves.md).
