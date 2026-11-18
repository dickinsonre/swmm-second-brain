---
title: "Exam-First SWMM Harness (app)"
type: entity
updated: 2026-11-18
sources: [S69, S72, S286]
tags: [apps, calibration, testing, swmm5, swmm6, held-out, defects]
reviewed: no
---
Bob's app Exam-First SWMM Harness: a calibration and testing harness built on "write the exam before the code": a frozen exam, a loop that rewrites the settings block of harness.py keeping an edit only when held-out scores improve, and a sealed set opened once, around EPA SWMM 5.2.4 and OpenSWMM 6.0.0-alpha.4 pinned by SHA-256. Version and date 2026-10-19 [S286](../sources/S286-exam-first-swmm-harness-summary.md). Netlify address, from its `links:` line: https://swmm5-swmm6-loop-harness.netlify.app [S286](../sources/S286-exam-first-swmm-harness-summary.md).

**A caution about its source.** The page ships no technical summary. [S286](../sources/S286-exam-first-swmm-harness-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q111).

**What the summary says** [S286](../sources/S286-exam-first-swmm-harness-summary.md)
- 41 rounds of 8 edits (2,148 question gradings, 8 rewrites kept): held-out score 0.496 to 0.807, sealed score 0.637 to 0.715; detector 9 of 12 to 12 of 12 on sealed pairs; sealed calibration fell 0.524 to 0.430 while its held-out score rose 0.408 to 0.613.
- DR-1: OpenSWMM 6 (swmm6_rel 3c30f1e6) writes its internal node type straight into the .out, where 2 means storage and 3 divider, but its internal enum has DIVIDER = 2 and STORAGE = 3; the engine already has internal_to_c_node_type() for the conversion. A one-line fix was built and checked.
- DR-2: on network P17 (five junctions SWMM 5.2.4 never surcharges), FLOW_ROUTING FV reports 79.2 ft at J2 and 103.4 ft at J3, which are 11.50 and 12.75 ft deep, with routing continuity 0.0%; the spike disappears only at a 0.5 s step; cause undiagnosed.
- Every score is an engine run graded by the frozen grader; the engines give byte-identical .out files run to run.

**What it does not show.** No field data (a twin experiment); small generated networks, not the corpus; six whole-model parameters; one proposer, one loop seed, one machine; no person has reviewed the exam, key or defect register. [S286](../sources/S286-exam-first-swmm-harness-summary.md)

**Noted at ingest.** DR-1 agrees with what [S69](../sources/S69-swmm6-code-house-app-md.md) found reading the same output plugin (DIVIDER stored as 2 and STORAGE as 3) and [S72](../sources/S72-li-swmm6-code-house-article.md) saw in a real file.

See [Apps summarized on 17 and 18 November 2026: SWMM6, benchmarks and ICM results](../concepts/apps-from-pages-swmm6-and-benchmarks.md), [Calibration, validation and uncertainty](../concepts/calibration-validation-uncertainty.md), [Reading SWMM output](../concepts/reading-swmm-output.md), [OpenSWMM 6 and HydroCouple](openswmm-6-and-hydrocouple.md), [OpenSWMM 6 solvers, measured](../concepts/openswmm6-solvers-measured.md), [The SWMM findings register](../concepts/findings-register.md).
