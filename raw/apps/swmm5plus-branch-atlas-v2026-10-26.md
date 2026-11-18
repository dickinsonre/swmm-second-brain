---
name: SWMM5+ Branch Atlas
file: swmm5plus-branch-atlas.html
version: 2026-10-26
date: 2026-10-26
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/H95HGFeDKt4wRocY8BtiHe", repo: "measures CIMM-ORG/SWMM5plus"}
engines:
  - {name: SWMM5+ (nine branches), source: "CIMM-ORG/SWMM5plus, measured 2026-10-26", note: "8 of 9 branches built as native engines with gfortran and flang; no WebAssembly engine has been built yet"}
units: US customary with a US/SI switch
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says the atlas was built with Claude (Opus 5.5) under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/H95HGFeDKt4wRocY8BtiHe, version 1793055476-10c8 (index.html, 1,185,382 bytes, SHA-256 21afd3daa88123cb80419724ba63b2b89f0d793aeecec3b15e755f1e86b83466), its About and Doc sheets read in headless Chromium on 2026-11-17. Nothing was run to write this file."
---

# SWMM5+ Branch Atlas: the nine branches of CIMM-ORG/SWMM5plus, measured, built and compared

## In three points
- **What:** Measures all nine branches of CIMM-ORG/SWMM5plus (2019 to 2024), the Fortran 2008 finite-volume engine by Ben Hodges and his students for CIMM, and tries to build and run each one outside Intel Fortran.
- **So what:** With a portability layer and a single-image coarray transform, 8 of the 9 branches build as native engines with gfortran and flang, and on three branches the two builds printed equal values on all three bench models.
- **Now what:** Use it to see how the branches differ before choosing one to build on. The WebAssembly stage has not been run, no branch was compared with an Intel Fortran build, and three small models are not a test suite.

This summary was written after the fact. The page ships no technical summary and no version of its own, so the version above is its measurement date ("measured 2026-10-26"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

SWMM5+ is written in Fortran 2008; its nine branches date from 2019 to 2024. It keeps EPA SWMM 5.1.13 (C) as its front end and routes with a finite-volume solver. Nine branches mean nine engines that differ in undocumented ways; the atlas measures each with git and compilers. Sheets: Branches, Differences (a distance matrix of Fortran lines added plus removed between branch heads), Engines, Build ledger, Doc, About. The SWMMengine pair was built originally with gfortran 9, AlphaRelease0001a with gfortran plus OpenCoarrays; from BIPquick-Dev on every branch used Intel Fortran, and the newer CMake file refuses anything else.

## Checks (as stated on the page)

- Every rewrite is logged with the line as committed and the line as compiled.
- Three branches (development, archived_development_20230607 and cmake) were each built twice, from the unmodified coarray source with gfortran and from the single-image source with flang; every printed value both builds produced is equal, and where cmake stops, both stop at the same check.
- AlphaRelease0001a's single-image output matched its coarray output byte for byte.
- Every number comes from git, a compiler, or the engine's own output files.

## What this does not show

- No comparison with an Intel Fortran build.
- Every engine runs one image; the parallel partitioning (BIPquick and successors) is compiled in but never exercised with more than one processor.
- Three small bench models do not rank the branches or say which is right.
- HDF5 output is stubbed out.
- The two SWMMengine branches ran only on built-in cases (the C library they need to read an .inp was never committed).
- BIPquick-Dev does not build; its 89 unique commits are measured but never run.
- No WebAssembly engine has been built: the Emscripten stage was stopped by the build session's safety check pending Bob's go-ahead, so the browser runner on the Engines sheet is off.

## How to reproduce

The Build ledger names the method behind each number and how to rerun it.

## Credits and licenses

SWMM5+ by Ben Hodges and his students at the University of Texas at Austin for CIMM (CIMM-ORG/SWMM5plus). EPA SWMM 5.1.13 front end (public domain). LLVM flang 20, gfortran, OpenCoarrays. No license is stated for the page.

## AI use

The page says the atlas was built with Claude (Opus 5.5), Anthropic's AI model, in a Claude session on 26 October 2026, at the request and under the direction of Robert (Bob) Dickinson, who chose the subject. Claude cloned the repository and measured every branch, wrote the portability layer (IFPORT, HDF5, dlopen and shell replacements), the single-image coarray transform, the build scripts for gfortran and flang, the three bench models and the comparison scripts, found and documented the defects in the Build ledger, and wrote the page, the essay and the .docx. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 2026-10-26: the version read.
