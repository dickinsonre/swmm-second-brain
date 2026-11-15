---
title: SWMM5 Topology Sandbox (app)
type: entity
updated: 2026-11-15
sources: [S78, S106, S136]
tags: [apps, replit, swmm5, generators, teaching]
reviewed: no
---
Bob's Replit app SWMM5 Topology Sandbox: an educational app that generates a drainage network from a chosen pattern, draws it, shows estimated hydrographs and exports a SWMM5-format INP file. Version 1.0.0, at `fractal-swmm-gen--robertdickinson.replit.app` [S106](../sources/S106-swmm5-topology-sandbox-replit-summary.md).

**A caution about its source.** Everything on this page rests on [S106](../sources/S106-swmm5-topology-sandbox-replit-summary.md), which Replit Agent wrote on 15 November 2026 from the project's source. Nothing here has been read by Bob (Q67).

**What the summary says** [S106](../sources/S106-swmm5-topology-sandbox-replit-summary.md)
- 22 network pattern choices, 5 link types and 8 API route handlers.
- Imperviousness, slope and area get random variation around the configured values.
- The hydrograph charts are estimates formed from topology-specific parameters. The client and server "simulation" routes return random result values. Neither calls a hydraulic engine.
- It exports an INP file and a CSV of network statistics. No SWMM engine was run against an exported INP.
- `npm run check` and `npm run build` passed; the build reported a client bundle larger than 500 kB. No test script.
- Server-side records are held in memory, not in PostgreSQL.
- The date 2026-01-19 is when Git first recorded `package.json`.

**What it does not show.** Only the home page and the not-found route were loaded. Compatibility of the exported INP with a SWMM run was not checked. [S106](../sources/S106-swmm5-topology-sandbox-replit-summary.md)

**Noted at ingest.** [S78](../sources/S78-fractal-swmm-generator-app-md.md) also counts 22 patterns in the Fractal SWMM5/SWMM6 Network Generator. Neither file says how the two generators are related (Q73).

**Added 15 November 2026: another generator built on topology.** [SWMM5 Topo Network Wizard (app)](swmm5-topo-network-wizard.md) defines 49 topology methods, lays the nodes out with a particle simulation and exports SWMM5 input files; it runs no SWMM engine [S136](../sources/S136-swmm5-topo-network-wizard-replit-summary.md). Neither summary says how the two apps are related (Q73).

See [Replit apps and the summaries Replit Agent wrote](../concepts/replit-app-summaries.md), [Fractal SWMM5/SWMM6 Network Generator (app)](fractal-swmm-generator.md), [SWMM5 INP MAKER (app)](swmm5-inp-maker.md).
