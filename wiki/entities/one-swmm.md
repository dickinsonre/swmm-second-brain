---
title: One SWMM (app)
type: entity
updated: 2026-11-17
sources: [S200, S188]
tags: [apps, swmm5, swmm6, icm, comparison]
reviewed: no
---
Bob's app that puts his SWMM5, SWMM6 and ICM tools behind one page with two faces. Version 0.2.0, 9 November 2026 [S200](../sources/S200-one-swmm-summary.md).

**A caution about its source.** The page ships no technical summary. [S200](../sources/S200-one-swmm-summary.md) was written by Claude on 16 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q99).

**Two faces** [S200](../sources/S200-one-swmm-summary.md)
- Simple: four doors. Run my model; compare engines; is it stable; explain this number.
- Expert: every engine, the map, results tables, reports, and an Agent view with verbs (run, diagnose, explain, series, diff, certify, verify), a ledger and certificates.
- The rule between them: "the simple view may hide machinery, never a caveat."

**What it joins** [S200](../sources/S200-one-swmm-summary.md): the engines of [Seven SWMM Engines (app)](seven-swmm-engines.md), the [SWMM Results Kit](swmm-results-kit.md), and the verb contract of Bob's SWMM Agent Engine. That app's expected-difference register and its 778 tests were not in the build session, so every difference counts.

**Certificates.** One covers peak depth, HGL, flow, runoff and flooding under one tolerance, on one model, in one browser session. A floating-point slip had withheld the SWMM6 alpha.4 certificate on Example1: 4971.72 - 4971.71 came out as 0.010000000000218 ft against a 0.01 ft tolerance, at four nodes. A difference equal to the tolerance now passes [S200](../sources/S200-one-swmm-summary.md).

**ICM is read, never run.** Its peaks come in as a CSV and are compared, not certified [S200](../sources/S200-one-swmm-summary.md).

**Version 0.2.0** answers an outside review of 0.1.0 that found six faults, among them a storm swap that left 73.90 cfs standing after the rain file was replaced by a dry one, and a partial result (4 of 42 peaks) that had certified [S200](../sources/S200-one-swmm-summary.md).

**What it does not show.** Agreement is not proof that any engine is right. No person has yet used the front door on their own model [S200](../sources/S200-one-swmm-summary.md).

**Not the same One SWMM.** In Bob's 2021 webinar, the One SWMM engine is Innovyze's build of SWMM 5, used by ICM SWMM networks, InfoSWMM and InfoDrainage [S188](../sources/S188-talk-water-talks-icm-sim-vs-icm-swmm-2021.md). This app shares the name; neither source connects the two.
