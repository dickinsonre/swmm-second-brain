---
title: Green-Ampt Newton test order
type: concept
updated: 2026-11-14
sources: [S59, S67]
tags: [swmm5, infiltration, green-ampt, findings, verification]
reviewed: 2026-11-15
---
A candidate finding in [EPA SWMM 5](../entities/swmm-5.md) 5.2.4: the Green-Ampt solver checks whether its Newton correction is small before it applies the correction, so some wet steps infiltrate at the saturated conductivity alone [S67](../sources/S67-note-green-ampt-newton-test-order.md).

**Status.** The note's own status is "working". The runs were made once by Claude and have not been rerun by Bob. It has no register ID [S67](../sources/S67-note-green-ampt-newton-test-order.md). Treat every run number below as unconfirmed until a rerun.

**The code** [S67](../sources/S67-note-green-ampt-newton-test-order.md)

`grnampt_getF2` in `src/solver/infil.c`, lines 847 to 856. `f2` starts equal to `f1`.

```c
    for ( i = 1; i <= 20; i++ )
    {
        df2 = (f2 - f1 - c1 * log(f2 + c1) + c2) / (1.0 - c1 / (f2 + c1) );
        if ( fabs(df2) < 0.00001 )
        {
            return MAX(f2, f2min);
        }
        f2 -= df2;
    }
    return f2min;
```

At the `return`, `df2` has not been applied. If the first correction is under 0.00001 ft, `f2` is still `f1`, and the function returns the minimum volume: Ksat times the step, with no suction term. These ten lines were compared with EPA's file at tag v5.2.4 when the note was ingested, and they match [S67](../sources/S67-note-green-ampt-newton-test-order.md).

**When it happens** [S67](../sources/S67-note-green-ampt-newton-test-order.md)
- The wet step is 10 s or more.
- Ks (in/hr) times wet step (s) times (1 + c1/F) is below 0.432. c1 is (suction head + ponded depth) times moisture deficit; F is cumulative infiltration.
- So it favors low conductivity, short wet steps and a soil already partly wetted.

**One test, as reported** [S67](../sources/S67-note-green-ampt-newton-test-order.md)

One 10 ac pervious subcatchment, suction 12.6 in, Ksat 0.01 in/hr, deficit 0.10, 6.137 in of rain in 24 hours.

| Run | Infiltration, in | Peak runoff, cfs |
|---|---|---|
| Stock, wet step 5, 30, 60 or 300 s | 1.096 to 1.097 | 3.3109 |
| Stock, wet step 15 s | 0.868 | 3.4858 |
| One line moved, wet step 15 s | 1.096 | 3.3109 |
| Four independent solvers, wet step 15 s | 1.096 | 3.3109 |

The 15 s run lost 21 % of its infiltration while the continuity error stayed at -0.001 % [S67](../sources/S67-note-green-ampt-newton-test-order.md). See [Continuity is not validation](continuity-is-not-validation.md).

**The proposed fix.** Move `f2 -= df2;` above the test. One line [S67](../sources/S67-note-green-ampt-newton-test-order.md).

**A second, smaller effect.** In every run the value returned lacks its last correction, so stock is high by up to 0.00001 ft per call: 1.287 in against 1.286 in on a silt loam test [S67](../sources/S67-note-green-ampt-newton-test-order.md).

**What it does not show.** No real model, LID, snowmelt or storage seepage [S67](../sources/S67-note-green-ampt-newton-test-order.md).

**The second candidate in the same file.** Defect D1 of the [Topsoil Recovery Check (app)](../entities/topsoil-recovery-check.md) is at line 545 of `infil.c`, in Modified Horton [S59](../sources/S59-topsoil-recovery-check-app-md.md). Both are on [Infiltration methods](infiltration-methods.md).

**Open.** A register ID, a rerun, and the three files the note points to that are not in the repository: the test `.inp`, the patch, and the full write-up (Q44 in [Open questions](../open-questions.md)).
