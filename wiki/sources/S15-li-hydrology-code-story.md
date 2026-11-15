---
title: "S15: A Story about the C-Code Hydrology of SWMM5 (LinkedIn newsletter edition 12, 2024)"
type: source
raw: raw/linkedin/2024-02-10-story-c-code-hydrology-swmm5-robert-dickinson-2x0we.md
kind: linkedin-article
author: Robert Dickinson
published: 2024-02-10
ingested: 2026-11-14
tags: [hydrology, swmm5, source-code]
reviewed: 2026-11-15
---
**What it is.** Eight narrated sections on SWMM5's hydrology code: runoff, the runoff numerical solution, Curve Number, Horton, Green-Ampt and groundwater. Raw file: [raw/linkedin/2024-02-10-story-c-code-hydrology-swmm5-robert-dickinson-2x0we.md](../../raw/linkedin/2024-02-10-story-c-code-hydrology-swmm5-robert-dickinson-2x0we.md).

**How it was written.** The text is AI-written storytelling laid over the C source (a companion article of the same month is titled "Using ChatGPT to understand what I programmed in 1988"); this one does not name the tool. Its use to the wiki is the list of functions and variables it names, not the prose. None of it was checked against the code here.

**Claims worth keeping**
- Subcatchment results are indexed by `SubcatchResultType`: rainfall, snow depth, evaporation, infiltration, runoff, groundwater flow, groundwater elevation, soil moisture, washoff.
- Subarea runoff is computed by `getSubareaRunoff`, `getSubareaInfil`, `findSubareaRunoff`, `updatePondedDepth` and `adjustSubareaParams`.
- The runoff equation is integrated by `odesolve_integrate`, which uses Runge-Kutta steps with adaptive step size (`rkqs`, and `rkck` for the Cash-Karp formula).
- Infiltration entry points: `curvenum_getInfil`, `horton_getInfil`, `modHorton_getInfil`, `grnampt_getInfil` with `grnampt_getUnsatInfil` and `grnampt_getSatInfil`.
- Groundwater: `gwater_getVolume`, `gwater_getGroundwater` and `getFluxes`, over an upper and a lower zone.

**Feeds:** [Infiltration methods](../concepts/infiltration-methods.md), [Runoff surfaces and subarea routing](../concepts/runoff-surfaces-and-subarea-routing.md), [EPA SWMM 5](../entities/swmm-5.md).
