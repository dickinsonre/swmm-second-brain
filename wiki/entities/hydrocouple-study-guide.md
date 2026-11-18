---
title: "HydroCouple Study Guide (app)"
type: entity
updated: 2026-11-18
sources: [S304]
tags: [apps, hydrocouple, cpp, api, documentation]
reviewed: no
---
Bob's app HydroCouple Study Guide: the guide, checked against the headers it describes. Version 1.0, 2026-10-25 [S304](../sources/S304-hydrocouple-study-guide-summary.md). Its `links:` line names no live Netlify address [S304](../sources/S304-hydrocouple-study-guide-summary.md).

**A caution about its source.** The page ships no technical summary. [S304](../sources/S304-hydrocouple-study-guide-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob marked it reviewed on 18 November 2026 (Q116, settled).

**What the summary says** [S304](../sources/S304-hydrocouple-study-guide-summary.md)
- A study guide to HydroCouple, Caleb Buahin's C++ interface standard for coupling environmental models, arrived as a zip (five chapters, two C++ files, one Graphviz drawing) whose README asks the reader to check the real headers. This app does, claim by claim, against the 2017 v1.0.0 release and the 2026 2.0 code, and runs the guide's own coupling example in a JavaScript simulator so the pull can be watched.
- The architecture in the guide is right, and much of the API it shows is the 2017 Qt interface or never existed: 19 of 27 code lines compile against v1.0.0 and 13 against 2.0. The page lists twenty findings, and its corrected C++ files compile with -Wall.
- Checked by a machine: 27 guide lines, each compiled twice (against v1.0.0 and b1722c4); the corrected .cpp compiles with -Wall; the lifecycle transition table dumped from C++; 26 simulator tests in node; 95 interfaces parsed from the headers; a browser test of every tab in both themes. Checked by reading: verdicts on header comments rest on Claude's reading of the cited lines.

**How to use it, as the summary puts it.** Use it to learn HydroCouple's pull-driven coupling and to know which guide code to trust. The simulator is not HydroCoupleSDK, loads no component library, and its runoff model is a SWMM-style nonlinear reservoir, not SWMM. No person has reviewed the twenty findings against the headers. [S304](../sources/S304-hydrocouple-study-guide-summary.md)

**What it does not show.** As the page lists it: the simulator is a JavaScript model of the pull using the standard's names and compiled transition table; it is not HydroCoupleSDK, loads no component library, and nothing was run through a HydroCouple build. The runoff model is not SWMM (no Horton or Green-Ampt infiltration, no routing, no report-step averaging). No person has yet reviewed the twenty findings against the headers. [S304](../sources/S304-hydrocouple-study-guide-summary.md)

See [Apps summarized on 18 November 2026: SWMM6, SWMM5+ and solvers](../concepts/apps-from-pages-swmm6-solvers-and-swmm5plus.md), [Inside hydrocouple.platform (app)](inside-hydrocouple-platform.md), [OpenSWMM 6 and HydroCouple](openswmm-6-and-hydrocouple.md).
