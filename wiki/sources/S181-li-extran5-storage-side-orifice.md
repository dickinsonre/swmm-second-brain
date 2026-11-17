---
title: "S181: Extran 5, Storage Facility with Side Outlet Orifice (LinkedIn, 2025)"
type: source
raw: raw/linkedin/2025-04-06-extran-5-storage-facility-side-outlet-orifice-ai-github-dickinson-jh2ne.md
kind: linkedin-article
author: Robert Dickinson
published: 2025-04-06
ingested: 2026-11-16
tags: [extran, test-models, orifices, storage, swmm5, icm]
drafted_by: Robert Dickinson, with an input-file summary created with AI help and passages that read as AI-written
reviewed: no
---
**What it is.** The article on Example 5 of the 1981 EXTRAN manual: a storage unit drained by a side outlet orifice. Raw file: [raw/linkedin/2025-04-06-extran-5-storage-facility-side-outlet-orifice-ai-github-dickinson-jh2ne.md](../../raw/linkedin/2025-04-06-extran-5-storage-facility-side-outlet-orifice-ai-github-dickinson-jh2ne.md). Created 19 January 2025, published 6 April 2025, the first of the four.

**How it was written.** The four articles share one frame, word for word in most paragraphs: where the file came from, why it was a good test in the 1980s, where it is used now, a summary of the SWMM5 input file "created with AI Help", and the model in ICM. The history and "why it is good" paragraphs read as AI-polished. The .inp summary is an AI-written passage, not checked against the .inp. The siblings are [S180](S180-li-extran1-extran2-test-files.md), [S182](S182-li-extran-example-6-type-1-pump.md) and [S183](S183-li-extran-example-7-type-2-pump.md).

**Claims worth keeping**
- A side outlet orifice, in Bob's words: "a link using an orifice equation for a circular or rectangular shape with an offset from the bottom of the sewer or storm link. Often used for diverting flows to another link."
- The prose dates the file's uses: 1981, with the EXTRAN 3 manual on mainframes; 1988, the SWMM3 to SWMM4 transition; 2006, SWMM5 compared with SWMM4. The bullet list of the same article says "SWMM3 → SWMM4 transition validation, 1981" and "SWMM4 → SWMM5 algorithm verification, 1988" (Q93).
- It is among the test files of EPA's 2006 quality assurance report by Lewis Rossman ([S185](S185-epa-swmm5-qa-report-dynamic-wave-2006.md)), in the ZIP files of the SWMM5 download archived in 2006, and in EPA's GitHub test suite.
- Bob: it is used in InfoWorks ICM SWMM network daily build validation and in Autodesk Water InfoDrainage.
- The .inp imports into ICM SWMM and ICM InfoWorks networks, and an imported ICM SWMM network can be converted inside ICM to an InfoWorks network.
- The 1981 manual printed both the input files and the model output; the input was in fixed format. A caption calls the set "Seven Classic SWMM5 Hydraulics Test Files from Extran3 in 1981 later used in SWMM4 and SWMM5 Testing".
- AI-written passage, not checked against the .inp: storage unit 82309, 40.5 ft deep; side orifice 90010 from 82309 to junction 82308, 2 ft in diameter, discharge coefficient 0.85; 9 junctions, 1 outfall, 1 storage unit, 9 conduits; dynamic wave with a 20-second routing step; 8 hours on 1 January 2002.

**Checked at ingest.** The QA report gives the same storage unit, 40.5 ft high with a constant 800 sq ft of surface area, and the new node 82308 [S185](S185-epa-swmm5-qa-report-dynamic-wave-2006.md); the Rosetta Stone's conversion uses a circular side orifice of 2.0 ft with a coefficient of 0.85 [S186](S186-st-venant-rosetta-stone-app-md-v2-6-2.md). The AI summary agrees with both.

**Feeds:** [The EXTRAN manual test models](../concepts/extran-manual-test-models.md), [Orifices](../concepts/orifices.md), [EXTRAN](../entities/extran.md).
