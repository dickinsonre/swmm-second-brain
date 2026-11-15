---
title: Inside the Network (app)
type: entity
updated: 2026-11-15
sources: [S76]
tags: [apps, cfd, hydraulics, swmm5, extran]
reviewed: no
---
Bob's app that runs two models of one sewer in the browser and shows where they differ: a free-surface CFD solver that moves particles of water through chambers and box conduits, and EPA SWMM 5.2.4. Version 1.1.0, 12 November 2026. "It is a demonstration, not a design tool" [S76](../sources/S76-inside-the-network-cfd-app-md.md).

**Two kinds of model** [S76](../sources/S76-inside-the-network-cfd-app-md.md)
- Four [EXTRAN](extran.md) manual examples (1, 2, 7 and 80) as SWMM 5 files. SWMM 5 runs each whole file. The CFD follows one path of conduits to the outfall with lengths compressed 100, 50 or 25 to 1.
- A 150 ft section built for the app, run at true scale, with a SWMM 5 twin `.inp` written from the same table.

**The CFD solver.** netcfd 1.1, written for the app: a 2D vertical slice, PIC/FLIP particles on a staggered grid, cut-cell walls, a ghost-fluid free surface, and at true scale a rough-wall log law tuned to carry Manning's velocity at full flow [S76](../sources/S76-inside-the-network-cfd-app-md.md).

**How a long sewer fits.** Length and time are divided by the compression factor and bed slope multiplied by it; depths, velocities and flows are unscaled. The summary's argument: the Saint-Venant momentum equation is unchanged if bed slope and friction slope are both multiplied by the factor. It cites distorted-scale laboratory practice, such as the Mississippi Basin Model. Flows entering or leaving the path come from the SWMM 5 results [S76](../sources/S76-inside-the-network-cfd-app-md.md).

**Gates the solver passed at true scale** [S76](../sources/S76-inside-the-network-cfd-app-md.md)

| Gate | Reference | CFD |
|---|---|---|
| Dam break, 0.1 ft cells | Ritter depth at the dam 0.889 ft | 0.900 ft |
| Uniform flow, 40 cfs, S 0.02, n 0.013 | Manning normal depth 0.866 ft | 0.882 ft |
| Hydraulic jump, 40 cfs | Belanger sequent depth 2.267 ft | 2.181 ft |
| Still water, 20 s | zero motion | rms speed 0.012 ft/s |

**Against SWMM 5, plateau means at 50 to 1.** No pass mark was set [S76](../sources/S76-inside-the-network-cfd-app-md.md).

| Case | Node depth, CFD minus SWMM 5 | Water over the rim, CFD and SWMM 5 |
|---|---|---|
| Example 1, north branch | -0.27 to +0.61 ft | 102,622 and 114,210 ft³ |
| Example 7, north branch | -0.25 to +0.63 ft | 100,904 and 148,270 ft³ |
| Example 80, constricting pipes | -1.51 to -0.24 ft | 0 and 0 |

On the short true-scale section the CFD stands 1.29 ft above SWMM 5 at the first manhole (2.35 against 1.06 ft); with entry and exit losses of 0.5 and 1.0 SWMM 5 gives 1.92 ft there [S76](../sources/S76-inside-the-network-cfd-app-md.md).

**A finding on the way.** On three example files the page's SWMM engine writes 479 records where a native OWA-based engine writes 480. See [Run duration floored to whole seconds](../concepts/run-duration-floor.md).

**What it does not show.** Eighteen numbered limits, L-1 to L-18. Among them: two dimensions, so circular pipes are boxes; air has no pressure; inflows carry no momentum; chambers are not compressed, so a riser stores far more than a SWMM 5 junction; no measured data anywhere. No person has reviewed the solver code [S76](../sources/S76-inside-the-network-cfd-app-md.md).

**Engine.** EPA SWMM 5.2.4 with Bob's KW/SF patch, extension off; see [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md).
