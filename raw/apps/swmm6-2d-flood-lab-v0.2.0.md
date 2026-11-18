---
name: SWMM6 2D Flood Lab
file: swmm6-2d-flood-lab.html
version: 0.2.0
date: 2026-10-10
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/NkSm7Co3mDmvkSsJcJk7Eb", repo: none}
engines:
  - {name: OpenSWMM Engine, version: 6.0.0-alpha.4, branch: swmm6_rel, commit: c23ecd53, note: "the explicit local-inertial 2D surface solver translated to JavaScript and WGSL and reduced to one configuration; no engine binary in the page", license: Apache-2.0}
units: US customary on screen with an SI switch; the cases are defined in metres
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page shows no AI-use note; a comment in its code says the solver was translated by Claude for Robert Dickinson on 2026-10-08. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/NkSm7Co3mDmvkSsJcJk7Eb, version 1791620586-3d3b (index.html, 690,547 bytes, SHA-256 0b6875b662fc42559aedd4062f3f5259e2880405e8576f158f5d173b9151e155), its Flood, Verify, Scheme and Credits tabs read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# SWMM6 2D Flood Lab: an unofficial browser port of the OpenSWMM 6.0.0-alpha.4 local-inertial surface solver

## In three points
- **What:** A 2D flood model that runs in your browser, on the GPU (float32, WebGPU) or the CPU (float64), using a translation of Caleb Buahin's explicit local-inertial marcher from the OpenSWMM Engine. Six scenes: three surveyed terrains (Merewether NSW, Alexandria VA, Autzen Stadium flats in Eugene OR), three synthetic ones, or your own DEM.
- **So what:** It is checked two ways. Against the compiled engine, the double-precision kernel matches to rounding on four cases (largest depth difference 7.7e-16 to 5.9e-13 ft) and on Merewether at 13 ft squares (3.4e-12 ft, both 6,621 substeps). Against a real flood, Merewether, June 2007, five surveyed peak levels: RMS difference 0.48 to 0.53 ft across four mesh sizes, against 0.48 ft for TUFLOW as reported. Building it found five engine observations, among them that LTS_TIERS changes how fast a dry-bed front moves (S6-1).
- **Now what:** Use it to see how the OpenSWMM 6 surface solver behaves on real terrain and to export a SWMM6 input file for the engine. There are no pipes, inlets, culverts or 1D coupling, no infiltration and no convective acceleration; it runs one tier where the engine defaults to four, and only one site has observed flooding to compare with.

This summary was written after the fact. The app ships no technical summary of its own. Its version and date are the page's own ("SWMM6 2D Flood Lab 0.2.0 · 2026-10-10"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Flood, Verify, Scheme, Credits. Pick a scene and a mesh (Merewether: 13, 9.8, 6.6 or 3.3 ft squares, up to 252,822 triangles), set rain, boundary inflow (Merewether: 696 cfs across 78.7 ft of road edge), point inflows, Manning n and edges, then run at 60, 240 or 1,000 times real time or as fast as it goes. The panel shows simulated time, deepest cell, fastest velocity, flooded area, water on the surface and volume error, and explains what sets the current time step (Δt = α · Lchar / (√(g·h) + |u|)). Probes, a GIF recorder and Export (including a SWMM6 input file with LTS_TIERS 1 and ROUTING_STEP 0:00:10) are in the header.

## Checks (as stated on the page)

- In the page: "Run the checks" runs checks on small meshes and on the embedded terrain; the double-precision kernel always runs, the GPU rows need WebGPU.
- Against the survey (Merewether, steady 696 cfs, 6.6 ft squares, read at 1,000 s): differences from the surveyed levels +0.09, −0.16, +0.63, −0.31 and −0.86 ft at S0 to S4; from TUFLOW −0.24, −0.09, −0.03, −0.21 and −0.07 ft.
- Against the compiled engine (OpenSWMM 6.0.0-alpha.4, swmm6_rel at c23ecd53, GCC 13.3.0, LTS_TIERS 1, float64): rain on a tilted plane 7.7e-16 ft; rain on rolling ground 7.3e-16 and 1.1e-15 ft; channel dam break 5.9e-13 ft; pond over bumps 1.4e-5 ft (chaotic; a float32-sized nudge to the bed moves the answer 1.3 ft at 60 s). Alexandria 5.7e-12 ft and Autzen 6.7e-12 ft. At 6.6 ft squares on Merewether the two drift up to 1.4 in while the front moves and end 0.076 in apart at one cell; moving the engine's own bed by one part in 10^12 changes its depths by up to 3.3 in.
- The engine's default tiers on Merewether: with LTS_TIERS 4 the flood reaches S1 between 400 and 500 s instead of 200 and 300 s, and stores 15% more water at 1,000 s, with every run closing its volume balance.
- The GPU path against the kernel on a software WebGPU adapter: differences at or near each case's noise floor.

## What this does not show

As the page lists it: one comparison with observed flooding (five levels, one site, one storm, a steady inflow); bare ground with building holes and no drains, culverts, inlets, fences or infiltration, so ponding is an upper bound; the Eugene grid takes the lidar water surface as ground; one engine configuration (LOCAL_INERTIAL, first order, one tier, FLAT, MEAN, triangles); regular union-jack meshes only; GPU rows from a software adapter; no speed ratio, because none was measured with a control; point inflows are a rate added to one cell, not the engine's orifice-law coupling.

## Engine findings (as the page records them)

- S6-1: LTS_TIERS changes how fast a dry-bed front moves under LOCAL_INERTIAL (wet front at 20 s: 389 ft with one tier, 240 ft with four, 175 ft with eight). Open.
- S6-2: an inactive cell keeps its last discharge vector. Observation; small.
- S6-3: rain on a dry mesh with no boundary never moved (alpha.3 on develop only). Fixed in alpha.4.
- S6-4: the shipped 2D example labels an outflow as its upstream inflow (examples/2d_complete_example.inp, line 219). A sign in the example file.
- S6-5: a SPECIFIED_FLOW edge is per metre in every unit system, and a dry bed gives it the whole first step. Observation.

## Credits and licenses

The solver is a translation of the explicit local-inertial marcher written by Caleb Buahin for the OpenSWMM Engine, with documentation by Corinne Wiesner-Friedman and the HydroCouple developers (HydroCouple/openswmm.engine, swmm6_rel, commit c23ecd53, Apache License 2.0). The page names the files translated and their dates, says it is not an EPA, HydroCouple or OpenSWMM release, and reproduces the upstream NOTICE and the full Apache License 2.0 text on its Credits tab. Terrain: UNSW Water Research Laboratory via ANUGA (Apache-2.0; marked publishable); opengeos/data (MIT, Qiusheng Wu); PDAL/data Autzen lidar (CC BY 4.0; Watershed Sciences, Inc. and Hobu, Inc.). Method references: Bates, Horritt and Fewtrell (2010); de Almeida et al. (2012, 2013); Perot (2000); ARR Project 15. The idea of a flood model on the visitor's GPU came from the Iterating team's 2D SWMM experiment that Robert Dickinson shared; the page was built independently.

## AI use

The page shows no AI-use note. A comment in its code says the engine files were "translated to JavaScript and reduced to one configuration by Claude for Robert Dickinson, 2026-10-08". This summary was written by Claude (Anthropic) on 18 November 2026 from the published page.

## Changes

- 0.2.0 (2026-10-10): three surveyed terrains built in; constant SPECIFIED_FLOW boundary inflow; a fix for a point inflow on a dry mesh taking the whole first 10 s window as one substep; rectangular meshes; the survey comparison and findings S6-4 and S6-5 (the version read).
- Earlier: the Credits tab dates the translation of the engine files 2026-10-08. The page does not list the earlier version numbers.
