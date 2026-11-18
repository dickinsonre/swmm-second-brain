---
title: "SWMM5+ Branch Atlas (app)"
type: entity
updated: 2026-11-17
sources: [S205, S222, S223]
tags: [apps, swmm5plus, fortran, branches, builds]
reviewed: no
---
Bob's app SWMM5+ Branch Atlas: a measurement of all nine branches of CIMM-ORG/SWMM5plus (2019 to 2024), the Fortran 2008 finite-volume engine by Ben Hodges and his students for CIMM, with an attempt to build and run each one outside Intel Fortran. Version and date 2026-10-26 [S223](../sources/S223-swmm5plus-branch-atlas-summary.md). Netlify address: https://swmm5plus-branch-atlas.netlify.app [S205](../sources/S205-note-netlify-addresses.md).

**A caution about its source.** The page ships no technical summary. [S223](../sources/S223-swmm5plus-branch-atlas-summary.md) was written by Claude on 17 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q108).

**What the summary says** [S223](../sources/S223-swmm5plus-branch-atlas-summary.md)
- SWMM5+ keeps EPA SWMM 5.1.13 (C) as its front end and routes with a finite-volume solver.
- The SWMMengine pair was built originally with gfortran 9 and AlphaRelease0001a with gfortran plus OpenCoarrays; from BIPquick-Dev on every branch used Intel Fortran, and the newer CMake file refuses anything else.
- With a portability layer and a single-image coarray transform, 8 of the 9 branches build as native engines with gfortran and flang.
- Three branches (development, archived_development_20230607 and cmake) were each built twice, from the unmodified coarray source with gfortran and from the single-image source with flang; every printed value both builds produced is equal on all three bench models.
- AlphaRelease0001a's single-image output matched its coarray output byte for byte.
- BIPquick-Dev does not build; its 89 unique commits are measured but never run.

**What it does not show.** No comparison with an Intel Fortran build. Every engine runs one image, so the parallel partitioning is compiled in but never exercised. Three small bench models do not rank the branches. HDF5 output is stubbed out. The two SWMMengine branches ran only on built-in cases. No WebAssembly engine has been built: the Emscripten stage was stopped by the build session's safety check pending Bob's go-ahead. [S223](../sources/S223-swmm5plus-branch-atlas-summary.md)

**Noted at ingest.** [SWMM5+ Bench (app)](swmm5plus-bench.md) reaches SWMM5+ by a different route, Ehsan Madadi's shared library built from one commit, afd44de of 25 November 2024 [S222](../sources/S222-swmm5plus-bench-summary.md).

See [Apps summarized on 17 November 2026: SWMM history and the insides of SWMM5](../concepts/apps-from-pages-history-and-swmm5.md), [SWMM5+ (CIMM finite-volume engine)](swmm5plus.md), [SWMM5+ Bench (app)](swmm5plus-bench.md).
