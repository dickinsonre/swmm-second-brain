---
title: SWMM5 Topo Network Wizard (app)
type: entity
updated: 2026-11-15
sources: [S106, S128, S136]
tags: [apps, replit, swmm5, model-generation, topology]
reviewed: no
---
Bob's Replit app SWMM5 Topo Network Wizard: an app that generates stormwater network layouts from topology methods and a particle simulation, assigns elevations and catchments, estimates flows, and exports SWMM5 input files. Version 1.0.0, at `topo-network-wizard.replit.app` [S136](../sources/S136-swmm5-topo-network-wizard-replit-summary.md).

**A caution about its source.** Everything on this page rests on [S136](../sources/S136-swmm5-topo-network-wizard-replit-summary.md), which Replit Agent wrote on 15 November 2026 from the project's source. Nothing here has been read by Bob (Q74).

**What the summary says** [S136](../sources/S136-swmm5-topo-network-wizard-replit-summary.md)
- The source shows no external EPA SWMM executable or service being run. Its three `engines:` entries are the app's own code: a topology network generator, a Lenia particle simulator and a hydraulic analysis calculator, none separately versioned.
- The source defines 49 topology method identifiers and 8 categories, and 10 scenario presets.
- An optional seed makes generation repeatable. The node slider accepts 3 to 1,000 nodes.
- The particle engine evaluates pairwise distance, a Gaussian interaction kernel, a growth function, and short-range repulsion.
- Link generation selects up to three neighbors per particle within the configured connection radius. Link direction follows elevation, and duplicate links are discarded.
- Elevations are assigned by traversing link distances from an outfall. Delaunay triangulation creates clipped Voronoi cells for subcatchments.
- The hydraulic calculator estimates runoff as runoff coefficient times rainfall intensity times catchment area, accumulates flow along a shortest-distance tree, and estimates conduit capacity from area, hydraulic radius, roughness, and slope.
- Downloads are SWMM `.inp`, GeoJSON, DXF, SVG, and PNG. The files are made in the browser; the app does not run them through SWMM.
- USA mode uses feet, square feet, cubic feet per second, and feet per second. SI mode uses meters.
- Saved projects are stored in PostgreSQL. Five project API operations are registered.
- `npm run build` passed. `npm run check` failed with 4 TypeScript errors in 2 files. No test script is configured.
- The project package metadata declares MIT. No AI tools used to build the app are recorded in the project files.

**What it does not show.** The generated INP was not opened or run in EPA SWMM. Hydraulic estimates, unit conversions and exported values were not compared with an authoritative model or hand calculation. The API, the database and the published page were not tested. [S136](../sources/S136-swmm5-topo-network-wizard-replit-summary.md)

**Noted at ingest.** The `date:` is the day of the summary; the change list runs from 7 February 2026 to 16 March 2026 (Q75). It is a fourth generator of test networks here, after the [Fractal SWMM5/SWMM6 Network Generator (app)](fractal-swmm-generator.md), the [SWMM5 Topology Sandbox (app)](swmm5-topology-sandbox.md) [S106](../sources/S106-swmm5-topology-sandbox-replit-summary.md) and the [EPANET 2.3 Generator (app)](epanet-23-generator.md) [S128](../sources/S128-epanet-23-generator-replit-summary.md). The summaries do not say how these apps are related (Q73). It was brought over after the seventeen on the concept page and is added there as a twenty-first row.

See [Replit apps: the second seventeen summaries](../concepts/replit-app-summaries-second-batch.md), [Fractal SWMM5/SWMM6 Network Generator (app)](fractal-swmm-generator.md), [SWMM5 Topology Sandbox (app)](swmm5-topology-sandbox.md), [EPANET 2.3 Generator (app)](epanet-23-generator.md).
