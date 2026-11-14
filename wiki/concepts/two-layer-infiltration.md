---
title: Two-layer soil infiltration (SOIL2)
type: concept
updated: 2026-11-14
sources: [S08, S55, S59]
tags: [hydrology, infiltration, swmm5, enhancement]
reviewed: no
---
Bob's proposed enhancement to SWMM 5: let an ordinary subcatchment infiltrate through two soil layers by reusing the LID control's soil layer [S55](../sources/S55-swmm-brain-readme.md).

**The problem it answers.** Horton, Green-Ampt and Curve Number all treat the soil as one uniform layer, while real profiles have horizons (sandy loam over clay, topsoil over hardpan) and the interface controls how fast water moves down [S55](../sources/S55-swmm-brain-readme.md).

**The change** [S55](../sources/S55-swmm-brain-readme.md)
- One new keyword, `SOIL2`, for the lower layer of a LID control.
- One new flag, `UseAsInfil`, at the end of a `[LID_USAGE]` line.
- About 39 lines touched in existing code. Every existing input file is meant to run identically.

```ini
SandyLoamClay    SOIL   12.0  0.453  0.190  0.085  0.43  4.33  0.30    ;; Upper layer
SandyLoamClay    SOIL2  24.0  0.464  0.310  0.187  0.04  8.22  0.15    ;; Lower layer

[LID_USAGE]
S1  SandyLoamClay  0  0  0  0  0  0  *  *  0  1    ;; UseAsInfil = 1
```

The example is copied from [S55](../sources/S55-swmm-brain-readme.md), which does not give the units of the seven numbers.

**The equation.** `perc = Ksat × exp(-15.0 × (1.0 − θ/porosity))`, taken from `lid_proc.c :: soilFluxRates()`. Percolation from the upper layer is the inflow to the lower layer. If the lower layer saturates, it throttles the upper one [S55](../sources/S55-swmm-brain-readme.md).

**Evidence.** None in the source. The README's argument is that the percolation equation is "already validated by every LID simulation ever run in SWMM5"; it reports no test of the two-layer code [S55](../sources/S55-swmm-brain-readme.md).

**A SOIL2 layer that exists and runs.** [swmm524-perched](../entities/swmm524-perched.md), Bob's variant of EPA SWMM 5.2.4 (branch van-genuchten, commit 548e5fbf), adds a `SOIL2` layer under the bio-retention soil [S59](../sources/S59-topsoil-recovery-check-app-md.md). Its rule is not the README's: flow from the topsoil into SOIL2 is capped by SOIL2's Green-Ampt capacity with the perched head added, and optional `VG` lines take the head from van Genuchten curves [S59](../sources/S59-topsoil-recovery-check-app-md.md). The source does not mention a `UseAsInfil` flag.

**Evidence for that engine** [S59](../sources/S59-topsoil-recovery-check-app-md.md)
- With no SOIL2, VG or STRUCT line it writes the same `.out` and LID report as EPA 5.2.4, byte for byte, on 930 of 930 inputs.
- On one soil pair (4 in of topsoil over 24 in of compacted sandy clay) it captures 83.0 % of big winter storms, and 67.1 % with van Genuchten. See [Topsoil over compacted clay](topsoil-over-compacted-clay.md).
- OpenSWMM 6.0.0-alpha.4 ignores the unknown `SOIL2` keyword without reporting it, so a SOIL2 model runs there as a one-layer model.

**Other related work.** The Topsoil Recovery Check app is described on the swmm5.org topic page as comparing Horton with the LID two-layer soil for decompacted topsoil [S08](../sources/S08-swmm5org-topic-inside-swmm5.md).

**Open**
- Q30, partly answered. A SOIL2 engine exists as swmm524-perched [S59](../sources/S59-topsoil-recovery-check-app-md.md), with a different flow rule from the one in the README [S55](../sources/S55-swmm-brain-readme.md). Still open: where the README's `lid_twolayer.h` and `lid_twolayer.c` are, and whether the `UseAsInfil` design was ever built. See [Open questions](../open-questions.md).

See [Infiltration methods](infiltration-methods.md).
