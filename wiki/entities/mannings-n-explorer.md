---
title: "Manning's n Explorer (app)"
type: entity
updated: 2026-11-18
sources: [S320]
tags: [apps, mannings-n, solvers, routing, audits]
reviewed: no
---
Bob's app Manning's n Explorer: how Manning's n travels between solvers. Version 3.1, 2026-10-24 [S320](../sources/S320-mannings-n-explorer-summary.md). Its `links:` line names no live Netlify address [S320](../sources/S320-mannings-n-explorer-summary.md).

**A caution about its source.** The page ships no technical summary. [S320](../sources/S320-mannings-n-explorer-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q116).

**What the summary says** [S320](../sources/S320-mannings-n-explorer-summary.md)
- A workbench for one idea: a calibrated Manning's n is the number that made one program, grid and time step reproduce one set of high-water marks, so copying it into another solver can count some losses twice. It lines up thirty solvers by what they resolve (turbulence, sub-grid topography, numerical diffusion), gives a starting-point estimate for transferring n without calibration data, routes a flood wave, and walks through calibration. Single-file edition of Bob's Lovable app.
- Reading all 5,559 source lines turned up thirteen code defects, four of which changed what the app teaches. The Flood Wave tab routed through a single sub-reach, so all three curves peaked at 8.0 hours with 0.08%, 0.04% and 0.02% attenuation and there was nothing to watch; the Muskingum-Cunge routine used half the diffusion it printed; and both stage models ran backwards (raise n and the water surface went down).
- All 5,559 lines of the source read and every formula pulled into a Node test: thirteen code defects, listed on the Audit tab.
- Muskingum-Cunge diffusion checked against Ponce's form, D = q/(S0·c·Δx) = 2ν/(c·Δx).
- SWMM5 statements checked against the EPA SWMM 5.2.4 source files, and vendor statements against their documentation.

**How to use it, as the summary puts it.** Use it to think before you copy an n between models. No solver was run; the grades and purity percentages are judgements carried over from the original app, and the routing is Muskingum-Cunge on a prismatic wide channel at fixed depth. [S320](../sources/S320-mannings-n-explorer-summary.md)

**What it does not show.** As the page lists it: no solver was run (not TUFLOW, ICM, HEC-RAS or SWMM5); the grades and purity percentages are judgements from the original app, five of them justified by scheme descriptions this edition had to correct; the routing has no floodplain storage, lateral spreading or backwater; kinematic routing has nothing to say above the depth where the pipe's discharge curve peaks; the transfer tools give starting points, not answers. [S320](../sources/S320-mannings-n-explorer-summary.md)

See [Apps summarized on 18 November 2026: EPANET, converters and SWMM5 tools](../concepts/apps-from-pages-epanet-converters-and-swmm5-tools.md), [Force main friction](../concepts/force-main-friction.md), [SWMM 5 versus ICM InfoWorks](../concepts/swmm5-versus-icm-infoworks.md).
