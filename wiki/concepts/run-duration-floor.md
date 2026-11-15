---
title: Run duration floored to whole seconds
type: concept
updated: 2026-11-15
sources: [S76, S79]
tags: [swmm5, findings, time, verification]
reviewed: no
---
EPA SWMM 5.2.4 computes the length of a run by flooring a floating-point product to whole seconds. For some start dates and end times the product falls just under a whole number, and the run comes out one second short. Two of Bob's apps met this independently, eighteen days apart [S79](../sources/S79-teacher-forced-swmm-summary.md), [S76](../sources/S76-inside-the-network-cfd-app-md.md).

**The line.** In `project.c`: `TotalDuration = floor((EndDateTime - StartDateTime) * SECperDAY);` [S76](../sources/S76-inside-the-network-cfd-app-md.md). The Teacher-Forced SWMM page cites it as `project.c:165` [S79](../sources/S79-teacher-forced-swmm-summary.md).

**Two sightings**

| App | Date | Case | Effect |
|---|---|---|---|
| [Teacher-Forced SWMM (app)](../entities/teacher-forced-swmm.md) | 25 October 2026 | A run from midnight to 00:50 | Duration 2999 seconds. The last routing step is 19 seconds, not 20, and the hot start is written one second before the stated end. Measured: the final step ends at 2,999,000 ms instead of 3,000,000 [S79](../sources/S79-teacher-forced-swmm-summary.md) |
| [Inside the Network (app)](../entities/inside-the-network-cfd.md) | 12 November 2026 | Three EXTRAN example files that start 01/01/1988 and end at 08:00 | The product is 28799.999999895, so the duration is 28799 s and the run stops one report short: 479 records where another engine writes 480 [S76](../sources/S76-inside-the-network-cfd-app-md.md) |

A fourth file in the second case ends at 06:00, which is exact in binary, and is byte-identical between the two engines [S76](../sources/S76-inside-the-network-cfd-app-md.md).

**An engine that does not do it.** The native reference in the second case is the OWA fork inside swmm-toolkit 0.17.0, which "subtracts dates and times separately and gets 28800" [S76](../sources/S76-inside-the-network-cfd-app-md.md).

**What each app did about it**
- Teacher-Forced SWMM calls it defect D-1 and, under its precise-restart flag, rounds to the nearest millisecond before flooring, so the hot start is written at the stated end [S79](../sources/S79-teacher-forced-swmm-summary.md).
- Inside the Network leaves its engine as stock EPA and notes that only the first 4 hours are used by its comparison [S76](../sources/S76-inside-the-network-cfd-app-md.md).

**Why it matters for comparisons.** Two engines that agree on every record they both wrote can still differ by one record in file length. A byte comparison of whole `.out` files reports that as a mismatch; the second app's check reads "identical over the 479 records both wrote" [S76](../sources/S76-inside-the-network-cfd-app-md.md). See [Byte-for-byte gate](byte-for-byte-gate.md) and [Reading SWMM output](reading-swmm-output.md).

**Status.** Called "a genuine defect, though a small one" by the first app's essay [S79](../sources/S79-teacher-forced-swmm-summary.md). Read and measured by Claude in both apps; no person has reviewed either. The line number comes from one source only. It has no ID in [The SWMM findings register](findings-register.md) (Q47), and the label D-1 is also used for unrelated findings in two other apps.

**Not in the sources.** Whether this has been reported to EPA.
