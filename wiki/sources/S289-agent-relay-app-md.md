---
title: "S289: Agent Relay, app .md (v1.0.0)"
type: source
raw: raw/apps/agent-relay-v1.0.0.md
kind: app-md
author: Robert Dickinson
published: 2026-11-17
ingested: 2026-11-18
tags: [apps, ai-agents, digital-delivery, gis, swmm5, calibration]
drafted_by: Claude (Anthropic), with the app
reviewed: no
---
**What it is.** A technical summary of the app Agent Relay, version 1.0.0: the seven-box AI-enabled digital-delivery workflow from Ranjeet Bandiwadekar's LinkedIn diagram, run once on an invented town: five rule-based agents read and write one versioned GIS layer, EPA SWMM 5.2.2 runs in the browser, and a person approves every write. Raw file: [raw/apps/agent-relay-v1.0.0.md](../../raw/apps/agent-relay-v1.0.0.md).

**How it was written.** The app ships this file. The file says it was built with Claude (Anthropic) at Bob's request; no language model runs inside it.

**Claims worth keeping** (all copied from the file)
- The relay finds all four planted faults in 33 engine runs and moves the layer from v1 to v13.
- Calibration recovers the planted multiplier, 1.257 against 1.25, raising NSE from 0.939 to 0.998; the validation event scores 0.998.
- The step API and swmm_run give the same .out series (180 flow values at P6 identical); the reader matches the .rpt tables on 2,880 values to 0.0005; design-storm continuity: runoff -0.022%, routing -0.091%.
- 21 of 21 build checks pass.

**Limits it states.** No language model runs; the faults are planted and the sensor records come from the same engine, so recovery is expected; nothing was run in ICM, ArcGIS, QGIS, AutoCAD or Civil 3D; one parameter, meter and event; eleven nodes; costs and thresholds illustrative; the reader is a new minimal one, not the shared parser.

**Checked at ingest.** The engine is EPA SWMM 5.2.2, not 5.2.4, as the file states. The `links:` line gives Netlify as "none yet".

**Feeds:** [Agent Relay (app)](../entities/agent-relay.md), [Apps summarized on 17 and 18 November 2026: AI workflows, tools and puzzles](../concepts/apps-from-pages-tools-and-puzzles.md), [Socratic Engine Chat (app)](../entities/socratic-engine-chat.md), [Calibration, validation and uncertainty](../concepts/calibration-validation-uncertainty.md), [App build contract (four working principles)](../concepts/app-build-contract.md).
