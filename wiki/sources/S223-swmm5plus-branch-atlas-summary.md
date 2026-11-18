---
title: "S223: SWMM5+ Branch Atlas, summary written from the page (v2026-10-26)"
type: source
raw: raw/apps/swmm5plus-branch-atlas-v2026-10-26.md
kind: app-md
author: Robert Dickinson
published: 2026-10-26
ingested: 2026-11-17
tags: [apps, swmm5plus, fortran, branches, builds]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app SWMM5+ Branch Atlas, version 2026-10-26: a measurement of all nine branches of CIMM-ORG/SWMM5plus (2019 to 2024), the Fortran 2008 finite-volume engine by Ben Hodges and his students for CIMM, with an attempt to build and run each one outside Intel Fortran. Raw file: [raw/apps/swmm5plus-branch-atlas-v2026-10-26.md](../../raw/apps/swmm5plus-branch-atlas-v2026-10-26.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 17 November 2026, at Bob's request, from the published Claude artifact, version 1793055476-10c8, reading its About and Doc sheets in a headless browser; nothing was run to write it. Bob has not read it (Q108). The page says the atlas was built with Claude (Opus 5.5) in a session on 26 October 2026 under Bob's direction: Claude cloned the repository and measured every branch, wrote the portability layer (IFPORT, HDF5, dlopen and shell replacements) and the single-image coarray transform, wrote the bench models and documented the defects in the Build ledger.

**Claims worth keeping** (all copied from the file)
- SWMM5+ keeps EPA SWMM 5.1.13 (C) as its front end and routes with a finite-volume solver.
- The SWMMengine pair was built originally with gfortran 9 and AlphaRelease0001a with gfortran plus OpenCoarrays; from BIPquick-Dev on every branch used Intel Fortran, and the newer CMake file refuses anything else.
- With a portability layer and a single-image coarray transform, 8 of the 9 branches build as native engines with gfortran and flang.
- Three branches (development, archived_development_20230607 and cmake) were each built twice, from the unmodified coarray source with gfortran and from the single-image source with flang; every printed value both builds produced is equal on all three bench models.
- AlphaRelease0001a's single-image output matched its coarray output byte for byte.
- BIPquick-Dev does not build; its 89 unique commits are measured but never run.

**Limits it states.** No comparison with an Intel Fortran build. Every engine runs one image, so the parallel partitioning is compiled in but never exercised. Three small bench models do not rank the branches. HDF5 output is stubbed out. The two SWMMengine branches ran only on built-in cases. No WebAssembly engine has been built: the Emscripten stage was stopped by the build session's safety check pending Bob's go-ahead.

**Checked at ingest.** [SWMM5+ Bench (app)](../entities/swmm5plus-bench.md) reaches SWMM5+ by a different route, Ehsan Madadi's shared library built from one commit, afd44de of 25 November 2024 [S222](S222-swmm5plus-bench-summary.md). The `links:` line gives Netlify as "not yet deployed"; Netlify reported a finished deploy at https://swmm5plus-branch-atlas.netlify.app on 17 November 2026 [S205](S205-note-netlify-addresses.md).

**Feeds:** [SWMM5+ Branch Atlas (app)](../entities/swmm5plus-branch-atlas.md), [Apps summarized on 17 November 2026: SWMM history and the insides of SWMM5](../concepts/apps-from-pages-history-and-swmm5.md), [SWMM5+ (CIMM finite-volume engine)](../entities/swmm5plus.md), [SWMM5+ Bench (app)](../entities/swmm5plus-bench.md).
