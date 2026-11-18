---
title: "Agent Relay (app)"
type: entity
updated: 2026-11-18
sources: [S289]
tags: [apps, ai-agents, digital-delivery, gis, swmm5, calibration]
reviewed: no
---
Bob's app Agent Relay: the seven-box AI-enabled digital-delivery workflow from Ranjeet Bandiwadekar's LinkedIn diagram, run once on an invented town: five rule-based agents read and write one versioned GIS layer, EPA SWMM 5.2.2 runs in the browser, and a person approves every write. Version 1.0.0, 2026-11-17 [S289](../sources/S289-agent-relay-app-md.md). Its `links:` line names no live Netlify address [S289](../sources/S289-agent-relay-app-md.md).

**Its source.** [S289](../sources/S289-agent-relay-app-md.md) is the technical summary the app ships with. Bob has not read this page.

**What the summary says** [S289](../sources/S289-agent-relay-app-md.md)
- The relay finds all four planted faults in 33 engine runs and moves the layer from v1 to v13.
- Calibration recovers the planted multiplier, 1.257 against 1.25, raising NSE from 0.939 to 0.998; the validation event scores 0.998.
- The step API and swmm_run give the same .out series (180 flow values at P6 identical); the reader matches the .rpt tables on 2,880 values to 0.0005; design-storm continuity: runoff -0.022%, routing -0.091%.
- 21 of 21 build checks pass.

**What it does not show.** No language model runs; the faults are planted and the sensor records come from the same engine, so recovery is expected; nothing was run in ICM, ArcGIS, QGIS, AutoCAD or Civil 3D; one parameter, meter and event; eleven nodes; costs and thresholds illustrative; the reader is a new minimal one, not the shared parser. [S289](../sources/S289-agent-relay-app-md.md)

**Noted at ingest.** The engine is EPA SWMM 5.2.2, not 5.2.4, as the file states.

See [Apps summarized on 17 and 18 November 2026: AI workflows, tools and puzzles](../concepts/apps-from-pages-tools-and-puzzles.md), [Socratic Engine Chat (app)](socratic-engine-chat.md), [Calibration, validation and uncertainty](../concepts/calibration-validation-uncertainty.md), [App build contract (four working principles)](../concepts/app-build-contract.md).
