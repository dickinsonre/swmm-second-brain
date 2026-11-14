---
title: Engine speed, 1988 to 2024
type: concept
updated: 2026-11-14
sources: [S19]
tags: [swmm-history, performance]
reviewed: no
---
One test model, timed 36 years apart, on the hardware of each day [S19](../sources/S19-li-edition-29-engine-speed.md).

| | 1987 to 1988 | 2024 |
|---|---|---|
| Program | SWMM 4, Fortran | SWMM 5.2 or later, C |
| Machine | PC AT with internal hard drive | PC with 32 cores |
| Model | The EXTRAN 3 test model of 1981 | The same model with a repeating daily baseline pattern |
| Simulated time | 6 hours | 1 January 1988 to 1 January 2024 |
| Wall-clock time | 5 minutes (after a 5 minute compile) | 5 minutes |

All rows from [S19](../sources/S19-li-edition-29-engine-speed.md). The article gives the 2024 span as 324,360 hours and the speed ratio as 54,060.

**What the ratio measures.** Hardware and software together. The article credits mostly Moore's Law, and names a more efficient engine, optimized C and the use of several cores as the software share [S19](../sources/S19-li-edition-29-engine-speed.md). The two runs are not the same input: the 2024 model swaps a flow time series for a repeating baseline pattern so the same flow recurs every day [S19](../sources/S19-li-edition-29-engine-speed.md).

**Check of the arithmetic (ours).** From 1 January 1988 to 1 January 2024 is 13,149 days, or 315,576 hours. Divided by 6 hours that is 52,596, not 54,060. The article's 324,360 hours equals 37 years of 8,760 hours plus 240 hours. Open question Q03 in [Open questions](../open-questions.md).

**The model.** It is Extran1.INP in the OWA-Extran set, and Example 1 of the 1981 manual [S19](../sources/S19-li-edition-29-engine-speed.md). See [EXTRAN](../entities/extran.md).
