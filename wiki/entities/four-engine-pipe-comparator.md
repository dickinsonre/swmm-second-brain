---
title: "Four-Engine Pipe Comparator (app)"
type: entity
updated: 2026-11-19
sources: [S378]
tags: [apps, hec-ras, icm, swmm5, swmm6, pressurization]
reviewed: no
---
Bob's app Four-Engine Pipe Comparator compares how [HEC-RAS](hec-ras.md) Pipe Networks, [InfoWorks ICM](infoworks-icm.md), EPA SWMM5 and OpenSWMM 6 route unsteady flow through closed conduits, and what pressurization costs each in stable timestep. Version 1.5.0, 2026-11-18 [S378](../sources/S378-four-engine-pipe-comparator-app-md.md). No engine runs inside the page; its 128 capability cells are a reading of documentation, release notes, source and upstream measurements [S378](../sources/S378-four-engine-pipe-comparator-app-md.md). It generates a surcharge benchmark as a SWMM5 .inp, the one format all four read [S378](../sources/S378-four-engine-pipe-comparator-app-md.md). Its `links:` line names no Netlify or artifact address [S378](../sources/S378-four-engine-pipe-comparator-app-md.md).

**What it computes** [S378](../sources/S378-four-engine-pipe-comparator-app-md.md). On a 3 ft pipe, 330 ft long, at 3 ft/s and Cr 0.75: SWMM5 SLOT 2.75 s, SWMM5 EXTRAN 14.72 s, ICM 5 to 60 s (accuracy choice), HEC-RAS 82.5 s, and a SWMM6 FV substep of 0.400 s on an 82.5 ft cell. Half-full celerity 6.16 ft/s; a 1 percent slot 87.07 ft/s. 204 checks in four suites, run against functions extracted from the shipped HTML.

**A trap it names** [S378](../sources/S378-four-engine-pipe-comparator-app-md.md). SWMM6 reports conduit flow as the mean face mass flux over the reporting step, not the end-of-step momentum state; upstream found a force main delivering 25 cfs whose cell momentum state held 18.4. Record which quantity was pulled before calling a difference physical.

**What it does not show** [S378](../sources/S378-four-engine-pipe-comparator-app-md.md). The FV cost figures are quoted from upstream, not measured. The benchmark scoreboard ships empty, because filling it would mean publishing runs that were never made.

See [OpenSWMM 6 solvers, measured](../concepts/openswmm6-solvers-measured.md), [Preissmann slot and surcharge](../concepts/preissmann-slot-and-surcharge.md).
