---
title: Block architecture and interface files
type: concept
updated: 2026-11-14
sources: [S01, S09, S21, S22]
tags: [swmm-history, architecture]
reviewed: no
---
SWMM 1 to 4 ran as separate blocks joined by interface files. SWMM 5 is one engine reading one input file [S22](../sources/S22-li-ten-problems.md).

**The 1971 blocks** [S01](../sources/S01-swmm1-engine-app-md.md)

| Block | Program units | Cards |
|---|---|---|
| Executive (MAIN, GRAPH, CURVE, PINE, PPLOT) | 5 | 389 |
| Runoff | 7 | 1,311 |
| Transport | 25 | 4,114 |
| Storage | 17 | 3,918 |
| Receiving Water | 11 | 2,468 |

The Executive Block reads block names from cards (`WATERSHED`, `TRANSPORT`, `STORAGE`, `RECEIVING`, `ENDPROGRAM`) and the blocks pass hydrographs to each other on tape [S01](../sources/S01-swmm1-engine-app-md.md). [S21](../sources/S21-li-edition-56-swmm-history.md) counts four blocks for SWMM 1, leaving out the Executive.

**The interface tape, 1971.** Unformatted, with 4-byte record markers: a 40-word title; `NSTEP, NPOINTS, NQUAL, DT, TZERO, TAREA`; the element numbers; then for each step the time, a flow per point and `NQUAL` loads per point. Storage always reads unit 10 and writes unit 11 [S01](../sources/S01-swmm1-engine-app-md.md).

**An interface fault from 1971.** Transport writes pollutants to the tape in one loop order (`TRAN497T` to `498`) and Storage reads them in another (`STOR103` to `104`), so with two or more outfalls on the tape Storage takes coliforms as suspended solids [S01](../sources/S01-swmm1-engine-app-md.md).

**Why it became a problem.** Each block had its own input conventions and its own manual chapter. That suited 1970s hardware and confused everyone afterward. SWMM 4 decks never converted cleanly to SWMM 5, and some features did not make the trip [S22](../sources/S22-li-ten-problems.md). [S22](../sources/S22-li-ten-problems.md) lists the blocks of SWMM 1 to 4 as Runoff, Transport, EXTRAN, Storage/Treatment and Receiving; the 1971 listing has no EXTRAN block [S01](../sources/S01-swmm1-engine-app-md.md).

**A small confirmation.** The oldest thread in Bob's OpenSWMM list, 15 February 1995, started by [William (Bill) James](../entities/william-james.md), is titled "Interface files" [S09](../sources/S09-openswmm-thread-list.md).

See [SWMM 1 (1971)](../entities/swmm-1.md), [SWMM version history, 1969 to 2026](swmm-version-history.md).
