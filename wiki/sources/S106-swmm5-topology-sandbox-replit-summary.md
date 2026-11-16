---
title: "S106: SWMM5 Topology Sandbox, summary written by Replit Agent (v1.0.0)"
type: source
raw: raw/apps/fractal-swmm-gen--robertdickinson-v1.0.0.md
kind: app-md
author: Robert Dickinson
published: 2026-01-19
ingested: 2026-11-15
tags: [apps, replit, swmm5, generators, teaching]
reviewed: 11/16/2026
---
**What it is.** A technical summary of SWMM5 Topology Sandbox, version 1.0.0: an educational app that generates a drainage network from a chosen pattern, draws it, shows estimated hydrographs and exports a SWMM5-format INP file. It is one of Bob's Replit apps, at `fractal-swmm-gen--robertdickinson.replit.app`. Raw file: [raw/apps/fractal-swmm-gen--robertdickinson-v1.0.0.md](../../raw/apps/fractal-swmm-gen--robertdickinson-v1.0.0.md).

**How it was written. This one is different.** The app ships no summary of its own making. Replit Agent wrote the file on 15 November 2026 from the project's source, and the file says Bob has not yet reviewed it (Q67). Of the app itself it says the reviewed files and Git history do not identify the AI tools used to build it. The copy here was read out of the editor of the Replit project named Fractal SWMMGen on 15 November 2026 and matched a SHA-256 computed there (see the log).

**Claims worth keeping** (all copied from the file)
- 22 network pattern choices, 5 link types and 8 API route handlers.
- Imperviousness, slope and area get random variation around the configured values.
- The hydrograph charts are estimates formed from topology-specific parameters. The client and server "simulation" routes return random result values. Neither calls a hydraulic engine.
- It exports an INP file and a CSV of network statistics. No SWMM engine was run against an exported INP.
- `npm run check` and `npm run build` passed; the build reported a client bundle larger than 500 kB. No test script.
- Server-side records are held in memory, not in PostgreSQL.
- The date 2026-01-19 is when Git first recorded `package.json`.

**Limits it states.** Only the home page and the not-found route were loaded. Compatibility of the exported INP with a SWMM run was not checked.

**Checked at ingest.** [S78](S78-fractal-swmm-generator-app-md.md) also counts 22 patterns in the Fractal SWMM5/SWMM6 Network Generator. Neither file says how the two generators are related (Q73).

**Feeds:** [SWMM5 Topology Sandbox (app)](../entities/swmm5-topology-sandbox.md), [Replit apps and the summaries Replit Agent wrote](../concepts/replit-app-summaries.md), [Fractal SWMM5/SWMM6 Network Generator (app)](../entities/fractal-swmm-generator.md), [SWMM5 INP MAKER (app)](../entities/swmm5-inp-maker.md).
