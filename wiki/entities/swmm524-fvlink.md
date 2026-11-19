---
title: "swmm524-fvlink"
type: entity
updated: 2026-11-19
sources: [S377, S308]
tags: [swmm5, engine, finite-volume, dynamic-wave]
reviewed: no
---
One of Bob's variants of [EPA SWMM 5](swmm-5.md): EPA SWMM 5.2.4 with a new `[FV_LINKS]` input section. Conduits listed there are solved by an explicit finite-volume scheme on their own cells; every other link and node stays stock dynamic wave [S377](../sources/S377-fv-link-lab-app-md.md). Branch `swmm524-fvlink` of SWMMBobSWMM6/Stormwater-Management-Model, base commit 7952ca8 (tag v5.2.4); its `fvlink` folder at the branch head of 19 November 2026: https://github.com/SWMMBobSWMM6/Stormwater-Management-Model/tree/6d64881ef29dfffb0d8031bcad5d34e86ff1f613/fvlink [S377](../sources/S377-fv-link-lab-app-md.md). The app that runs it is [FV Link Lab](fv-link-lab.md).

**How it works** [S377](../sources/S377-fv-link-lab-app-md.md)
- `src/solver/fvlink.c`, 1,403 lines: HLL flux with Davis wave speeds, hydrostatic reconstruction (Audusse et al. 2004), a static Preissmann slot at 100 ft/s capped at 5 % of the maximum width, semi-implicit Manning friction on the real section area, positivity limiting.
- Default cell about 25 ft, at least 4 cells; substep `dt <= 0.5 * dx / max(|u| + c)` with a floor of 0.001 s.
- FV links are subcycled inside every Picard iteration of the dynamic wave step, and the volume crossing each end face is booked into node continuity exactly, except at a node surcharged under EXTRAN. Reported link flow is the time-averaged delivered flow.

**What it measured** [S377](../sources/S377-fv-link-lab-app-md.md)
- Without `[FV_LINKS]`: 72 of 73 EPA regression models byte-identical to stock, and 1 stopping with the same error in both.
- FV link volume balance at most 2.7e-12 % over 37 EPA models and 14 synthetic cases.
- With the 10-ft trunk pipe of a 400-pipe tree FV: 0.19x stock wall time, every conduit peak within 0.53 % and every node peak within 0.80 % of stock.

**Open defect FVL-15** [S377](../sources/S377-fv-link-lab-app-md.md). At the inflow end the ghost state pairs the node's level with the link's velocity, so a link fed from a still pool can run water uphill: in the Company lock model of the Thoth canal, 300 cfs flows from the lock into a basin whose water surface is 7.7 ft higher. Five prototype fixes were tried and none adopted. The source's advice: do not put an FV link at the outlet of a pool. [Thaw on the Thoth](thaw-on-the-thoth.md) is where the defect was found [S308](../sources/S308-thaw-on-the-thoth-summary.md).

**Limits** [S377](../sources/S377-fv-link-lab-app-md.md). Stock dynamic wave is the reference, not the truth. Not in FV links: evaporation, seepage, conduit lengthening and hot-start cell state. Not compared against OpenSWMM's FV engine. Built and run on native Linux gcc 13.3 and WebAssembly only.

See [The byte-for-byte gate](../concepts/byte-for-byte-gate.md), [Preissmann slot and surcharge](../concepts/preissmann-slot-and-surcharge.md), [OpenSWMM 6 solvers, measured](../concepts/openswmm6-solvers-measured.md).
