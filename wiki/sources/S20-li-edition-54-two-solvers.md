---
title: "S20: Edition 54, Two Solvers, One Equation (LinkedIn, 2026)"
type: source
raw: raw/linkedin/2026-02-23-edition-54-two-solvers-one-equation-argument-has-lasted-dickinson-3dbte.md
kind: linkedin-article
author: Robert Dickinson
published: 2026-02-23
ingested: 2026-11-14
tags: [hydraulics, swmm5, icm, comparison]
reviewed: no
---
**What it is.** An essay on how SWMM 5 and InfoWorks ICM each solve the St. Venant equations, written around Bob's Replit comparison app. Raw file: [raw/linkedin/2026-02-23-edition-54-two-solvers-one-equation-argument-has-lasted-dickinson-3dbte.md](../../raw/linkedin/2026-02-23-edition-54-two-solvers-one-equation-argument-has-lasted-dickinson-3dbte.md).

**How it was written.** In the Heinlein-explains-engineering voice Bob's apps use, which points to AI drafting; the article carries no AI-use note. The numbers come from the app's calculators. No engine run is cited. The wave speeds are given in metric.

**Claims worth keeping**
- SWMM 5 treats each conduit as one computational element: head at the nodes, flow in the link, nothing between.
- ICM divides each conduit into segments, typically one every 150 to 200 ft, and computes head and flow at each boundary.
- The EXTRAN lineage is described as a node-link formulation with implicit backward Euler time integration and successive relaxation; ICM as a Preissmann four-point implicit scheme with Newton-Raphson iterations and adaptive time stepping.
- ICM has used the Preissmann slot from the beginning. The article says SWMM 5 added it in 5.1.013, "released around 2012".
- Force main, 12 in pipe, 5 ft of head above the crown: Manning 2.53 cfs, Hazen-Williams 3.21 cfs, Darcy-Weisbach 1.58 cfs.
- On a five-node test network in a moderate storm the two peaks differ by 2 to 3 %. Typical continuity errors: SWMM 5 0.1 to 0.5 %, ICM 0.01 to 0.1 %.
- Partly full circular pipe geometry is approximated differently in the two programs; the flow difference is typically under 1 %.

**Feeds:** [Dynamic wave routing](../concepts/dynamic-wave-routing.md), [Preissmann slot and surcharge](../concepts/preissmann-slot-and-surcharge.md), [Force main friction](../concepts/force-main-friction.md), [SWMM 5 versus ICM InfoWorks](../concepts/swmm5-versus-icm-infoworks.md), [InfoWorks ICM](../entities/infoworks-icm.md), [SWMM and ICM St. Venant comparison (app)](../entities/swmm-icm-st-venant-app.md), [EXTRAN](../entities/extran.md).
