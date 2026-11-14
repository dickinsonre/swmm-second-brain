---
title: Two-layer soil infiltration (SOIL2)
type: concept
updated: 2026-11-14
sources: [S08, S55]
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

**Related work of Bob's.** `SWMMBobSWMM6/swmm524-perched` is described as SWMM 5.2.4 with a perched two-layer soil, and the Topsoil Recovery Check app compares Horton with the LID two-layer soil for decompacted topsoil [S08](../sources/S08-swmm5org-topic-inside-swmm5.md).

**Open**
- Q30. The README lists `lid_twolayer.h`, `lid_twolayer.c`, example files and an integration guide. None is in the old repository or in `raw/`. Whether `swmm524-perched` is this design under another name is not stated. See [Open questions](../open-questions.md).

See [Infiltration methods](infiltration-methods.md).
