---
title: "SWMM6 2D Flood Lab (app)"
type: entity
updated: 2026-11-18
sources: [S300]
tags: [apps, swmm6, openswmm, 2d-surface, verification, webgpu]
reviewed: no
---
Bob's app SWMM6 2D Flood Lab: an unofficial browser port of the OpenSWMM 6.0.0-alpha.4 local-inertial surface solver. Version 0.2.0, 2026-10-10 [S300](../sources/S300-swmm6-2d-flood-lab-summary.md). Its `links:` line names no live Netlify address [S300](../sources/S300-swmm6-2d-flood-lab-summary.md).

**A caution about its source.** The page ships no technical summary. [S300](../sources/S300-swmm6-2d-flood-lab-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q116).

**What the summary says** [S300](../sources/S300-swmm6-2d-flood-lab-summary.md)
- A 2D flood model that runs in your browser, on the GPU (float32, WebGPU) or the CPU (float64), using a translation of Caleb Buahin's explicit local-inertial marcher from the OpenSWMM Engine. Six scenes: three surveyed terrains (Merewether NSW, Alexandria VA, Autzen Stadium flats in Eugene OR), three synthetic ones, or your own DEM.
- It is checked two ways. Against the compiled engine, the double-precision kernel matches to rounding on four cases (largest depth difference 7.7e-16 to 5.9e-13 ft) and on Merewether at 13 ft squares (3.4e-12 ft, both 6,621 substeps). Against a real flood, Merewether, June 2007, five surveyed peak levels: RMS difference 0.48 to 0.53 ft across four mesh sizes, against 0.48 ft for TUFLOW as reported. Building it found five engine observations, among them that LTS_TIERS changes how fast a dry-bed front moves (S6-1).
- In the page: "Run the checks" runs checks on small meshes and on the embedded terrain; the double-precision kernel always runs, the GPU rows need WebGPU.
- Against the survey (Merewether, steady 696 cfs, 6.6 ft squares, read at 1,000 s): differences from the surveyed levels +0.09, −0.16, +0.63, −0.31 and −0.86 ft at S0 to S4; from TUFLOW −0.24, −0.09, −0.03, −0.21 and −0.07 ft.
- Against the compiled engine (OpenSWMM 6.0.0-alpha.4, swmm6_rel at c23ecd53, GCC 13.3.0, LTS_TIERS 1, float64): rain on a tilted plane 7.7e-16 ft; rain on rolling ground 7.3e-16 and 1.1e-15 ft; channel dam break 5.9e-13 ft; pond over bumps 1.4e-5 ft (chaotic; a float32-sized nudge to the bed moves the answer 1.3 ft at 60 s). Alexandria 5.7e-12 ft and Autzen 6.7e-12 ft.
- The engine's default tiers on Merewether: with LTS_TIERS 4 the flood reaches S1 between 400 and 500 s instead of 200 and 300 s, and stores 15% more water at 1,000 s, with every run closing its volume balance.

**How to use it, as the summary puts it.** Use it to see how the OpenSWMM 6 surface solver behaves on real terrain and to export a SWMM6 input file for the engine. There are no pipes, inlets, culverts or 1D coupling, no infiltration and no convective acceleration; it runs one tier where the engine defaults to four, and only one site has observed flooding to compare with. [S300](../sources/S300-swmm6-2d-flood-lab-summary.md)

**What it does not show.** As the page lists it: one comparison with observed flooding (five levels, one site, one storm, a steady inflow); bare ground with building holes and no drains, culverts, inlets, fences or infiltration, so ponding is an upper bound; the Eugene grid takes the lidar water surface as ground; one engine configuration (LOCAL_INERTIAL, first order, one tier, FLAT, MEAN, triangles); regular union-jack meshes only; GPU rows from a software adapter; no speed ratio, because none was measured with a control; point inflows are a rate added to one cell, not the engine's orifice-law coupling. [S300](../sources/S300-swmm6-2d-flood-lab-summary.md)

**Noted at ingest.** The page reproduces OpenSWMM's NOTICE and the full Apache License 2.0 on its Credits tab and names the engine files it translated, so the Netlify package added no license files. Its five engine observations (S6-1 to S6-5) are the page's own findings, not checked against the engine here.

See [Apps summarized on 18 November 2026: SWMM6, SWMM5+ and solvers](../concepts/apps-from-pages-swmm6-solvers-and-swmm5plus.md), [OpenSWMM 6 and HydroCouple](openswmm-6-and-hydrocouple.md), [Sandbox Companion (app)](sandbox-companion.md), [The SWMM findings register](../concepts/findings-register.md), [OpenSWMM 6 solvers, measured](../concepts/openswmm6-solvers-measured.md).
