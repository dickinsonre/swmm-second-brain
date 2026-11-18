---
title: "SWMM5+ (CIMM finite-volume engine)"
type: entity
updated: 2026-11-18
sources: [S222, S223, S82, S309, S310, S311]
tags: [swmm5plus, finite-volume, fortran, engines]
reviewed: no
---
SWMM5+ is a finite-volume dynamic-wave engine written in Fortran 2008 by Ben Hodges and his students at the University of Texas at Austin for CIMM, kept as CIMM-ORG/SWMM5plus [S223](../sources/S223-swmm5plus-branch-atlas-summary.md). It keeps EPA SWMM 5.1.13, in C, as its front end for reading the .inp [S223](../sources/S223-swmm5plus-branch-atlas-summary.md). It is about 88,000 lines of modern Fortran built around coarrays and HDF5, usually run in a container; version 1.0.3 is public domain (Unlicense) [S222](../sources/S222-swmm5plus-bench-summary.md).

**Branches.** Nine branches date from 2019 to 2024. From BIPquick-Dev on every branch used Intel Fortran, and the newer CMake file refuses any other compiler. With a portability layer and a single-image coarray transform written with Claude, 8 of the 9 build with gfortran and flang [S223](../sources/S223-swmm5plus-branch-atlas-summary.md).

**As a shared library.** Ehsan Madadi's swmm5plus-capi builds it as an ordinary library for Windows, macOS and Linux, which his desktop program Mirab uses [S222](../sources/S222-swmm5plus-bench-summary.md) [S82](../sources/S82-mirab-test-bench-summary.md).

**Measured beside EPA SWMM 5.2.4** [S222](../sources/S222-swmm5plus-bench-summary.md)
- It is explicit: on EXTRAN4 a mean step of 0.119 s and 241,021 steps for eight hours.
- An upstream end and a node with two links are faces that cannot flood; on EXTRAN4 EPA floods 178 ac-ft, 15.0 % of the inflow, at two such nodes.
- With a weir's Surcharge flag set to YES both engines use the same equivalent-orifice formula above the crown, and the weir peaks agree within 1.9 %.

**What has not been done.** No branch was compared with an Intel Fortran build; every build ran one image, so the parallel partitioning was never exercised; no WebAssembly engine has been built [S223](../sources/S223-swmm5plus-branch-atlas-summary.md). Neither engine was checked against field data [S222](../sources/S222-swmm5plus-bench-summary.md).

**Added 18 November 2026.** Three app pages read the SWMM5+ source. Upstream has 88,020 lines of Fortran in 72 files; no .f90 file makes an MPI call, since SWMM5+ uses coarrays with 111 sync all [S309](../sources/S309-swmm5plus-explorer-summary.md). SWMM5+ downloads EPA SWMM v5.1.13 (CMakeLists.txt lines 82 to 85), whose engine sits in src/ [S310](../sources/S310-swmm5plus-repo-explorer-summary.md). A module extraction matches 71 of 71 module declarations and 534 of 534 edges, while 27 of the curated dependency edges have no use statement behind them [S311](../sources/S311-swmm-insight-lab-summary.md) [S310](../sources/S310-swmm5plus-repo-explorer-summary.md).

See [SWMM5+ Bench (app)](swmm5plus-bench.md), [SWMM5+ Branch Atlas (app)](swmm5plus-branch-atlas.md), [Mirab Test Bench (app)](mirab-test-bench.md).
