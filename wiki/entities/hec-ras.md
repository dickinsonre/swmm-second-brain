---
title: "HEC-RAS"
type: entity
updated: 2026-11-19
sources: [S378, S196]
tags: [program, hec-ras, pipes, pressurization]
reviewed: no
---
HEC-RAS is the US Army Corps of Engineers' Hydrologic Engineering Center program [S378](../sources/S378-four-engine-pipe-comparator-app-md.md). Its Pipe Networks, at version 7.0.1, is one of the four engines the [Four-Engine Pipe Comparator](four-engine-pipe-comparator.md) compares for pressurized flow in closed conduits [S378](../sources/S378-four-engine-pipe-comparator-app-md.md). The comparator never runs HEC-RAS; what it says of it is a reading of HEC-RAS 7.0 release notes and documentation [S378](../sources/S378-four-engine-pipe-comparator-app-md.md).

**In the comparator's numerics lab** [S378](../sources/S378-four-engine-pipe-comparator-app-md.md). On a 3 ft pipe, 330 ft long, at 3 ft/s and Cr 0.75, the HEC-RAS step is 82.5 s, against 2.75 s for SWMM5 SLOT and 14.72 s for SWMM5 EXTRAN.

**Bob's own engine from its manuals.** [SWMM5 RASPIPE](swmm5-raspipe.md) is EPA SWMM 5.2.4 with a semi-implicit finite-volume pipe solver written from HEC's public manuals; its summary says it contains no HEC-RAS code and has not been compared with a run of HEC-RAS [S196](../sources/S196-swmm5-raspipe-summary.md).
