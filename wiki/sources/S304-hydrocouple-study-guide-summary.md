---
title: "S304: HydroCouple Study Guide, summary written from the page (v1.0)"
type: source
raw: raw/apps/hydrocouple-study-guide-v1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-25
ingested: 2026-11-18
tags: [apps, hydrocouple, cpp, api, documentation]
drafted_by: Claude (Anthropic), from the published page
reviewed: 2026-11-18
---
**What it is.** A technical summary of the app HydroCouple Study Guide, version 1.0: the guide, checked against the headers it describes. Raw file: [raw/apps/hydrocouple-study-guide-v1.0.md](../../raw/apps/hydrocouple-study-guide-v1.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/BdkdNWB8EBKDXu8i5LqFgz, version 1792946561-c5fe (index.html, 1,407,762 bytes, SHA-256 bddec357eb68021e1e02a15df856793779b8d8ba8f44c26c3420b352e926ae1f), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file." Its AI-use section: "The page says: built with Claude, Anthropic's AI model, in a Claude session on 25 October 2026 at the direction of Robert (Bob) Dickinson, who supplied the guide and is responsible for the work. Claude cloned HydroCouple (v1.0.0 and b1722c4) and HydroCoupleSDK, wrote the header parser, the 27 compile probes and the corrected C++ files, compiled the lifecycle table, wrote the simulator and its 26 tests, and built the page, its figures and text, including the Doc essay."

**Claims worth keeping** (all copied from the file)
- A study guide to HydroCouple, Caleb Buahin's C++ interface standard for coupling environmental models, arrived as a zip (five chapters, two C++ files, one Graphviz drawing) whose README asks the reader to check the real headers. This app does, claim by claim, against the 2017 v1.0.0 release and the 2026 2.0 code, and runs the guide's own coupling example in a JavaScript simulator so the pull can be watched.
- The architecture in the guide is right, and much of the API it shows is the 2017 Qt interface or never existed: 19 of 27 code lines compile against v1.0.0 and 13 against 2.0. The page lists twenty findings, and its corrected C++ files compile with -Wall.
- Checked by a machine: 27 guide lines, each compiled twice (against v1.0.0 and b1722c4); the corrected .cpp compiles with -Wall; the lifecycle transition table dumped from C++; 26 simulator tests in node; 95 interfaces parsed from the headers; a browser test of every tab in both themes. Checked by reading: verdicts on header comments rest on Claude's reading of the cited lines.

**Limits it states.** As the page lists it: the simulator is a JavaScript model of the pull using the standard's names and compiled transition table; it is not HydroCoupleSDK, loads no component library, and nothing was run through a HydroCouple build. The runoff model is not SWMM (no Horton or Green-Ampt infiltration, no routing, no report-step averaging). No person has yet reviewed the twenty findings against the headers.

**Checked at ingest.** Read in full; nothing was rerun at ingest. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [HydroCouple Study Guide (app)](../entities/hydrocouple-study-guide.md), [Apps summarized on 18 November 2026: SWMM6, SWMM5+ and solvers](../concepts/apps-from-pages-swmm6-solvers-and-swmm5plus.md), [Inside hydrocouple.platform (app)](../entities/inside-hydrocouple-platform.md), [OpenSWMM 6 and HydroCouple](../entities/openswmm-6-and-hydrocouple.md).
