---
title: Block architecture and interface files
type: concept
updated: 2026-11-17
sources: [S01, S09, S21, S22, S193, S194, S199]
tags: [swmm-history, architecture]
reviewed: 2026-11-15
changed_after_review: "2026-11-17 (S192 to S202 ingest): one paragraph added at the end on interface files in three apps (S193, S194, S199)"
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

**Added 17 November 2026: the interface files, run again.**
- [SWMM 3 Runoff & Transport](../entities/swmm3-runoff-transport-app.md) passes the 1981 interface file from Runoff to Transport. It reads back with the record lengths the 1981 manual's Figure 2-3 implies, and a Transport file read by a second Transport run routes on [S193](../sources/S193-swmm3-runoff-transport-summary.md).
- [SWMM 4 Twin Engines](../entities/swmm4-twin-engines.md): the Runoff interface file from the WebAssembly engine is byte-identical to the native build's [S194](../sources/S194-swmm4-twin-engines-summary.md).
- [Seven SWMM Engines](../entities/seven-swmm-engines.md) runs SWMM 4.4H as Runoff feeding Extran through an interface file, and feeds EXTRAN III the 4.4H Runoff file as a SWMM III tape [S199](../sources/S199-seven-swmm-engines-summary.md).
