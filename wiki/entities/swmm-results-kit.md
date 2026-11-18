---
title: SWMM Results Kit
type: entity
updated: 2026-11-17
sources: [S199, S200, S225, S240]
tags: [swmm5, swmm6, results-reading, library, verification]
reviewed: no
---
The shared library that reads every .rpt and .out file in Bob's engine apps into one run record, so that every view in an app sees the same numbers. Version 1.0.0 went into [Seven SWMM Engines (app)](seven-swmm-engines.md) on 28 October 2026 [S199](../sources/S199-seven-swmm-engines-summary.md); [One SWMM (app)](one-swmm.md) uses 1.0.1 [S200](../sources/S200-one-swmm-summary.md).

**How it was checked** [S199](../sources/S199-seven-swmm-engines-summary.md)
- Its .out reader matched EPA's own swmm-output library on 96 corpus runs, 11,738,268 values with 0 wrong, and on the 7 .out files that Seven SWMM Engines' engines write.
- Its .rpt reader passed 16,533 cross-checks against the same runs' .out files on 103 reports (7,037 table rows).
- Proved on SWMM 5.2.4 files and OpenSWMM 6 alphas 1 to 4. Its SWMM 5.0 and 5.1 report layouts are coded, not proved.

**What it fixed** [S199](../sources/S199-seven-swmm-engines-summary.md) [S200](../sources/S200-one-swmm-summary.md)
- The earlier report reader of Seven SWMM Engines dropped 7 DUMMY rows of Bellinge's 1,044 links and lost fields on weir, pump and orifice rows. The kit reads them all.
- 1.0.1: a hydrograph with a 06:00 report start now reads hour 6.00.
- A difference exactly equal to a tolerance now passes; floating-point subtraction had made a 0.01 ft difference fail a 0.01 ft test.

**Added 17 November 2026, second batch.** Two more apps read their results through the Results Kit 1.0.0: [Four Ways to K (app)](four-ways-to-k.md) [S225](../sources/S225-four-ways-to-k-summary.md) and [Non-Prismatic Channel Lab (app)](non-prismatic-channel-lab.md) [S240](../sources/S240-non-prismatic-channel-lab-summary.md).

**Related.** [Reading SWMM output](../concepts/reading-swmm-output.md).
