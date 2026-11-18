---
title: "SWMM5+ Explorer (app)"
type: entity
updated: 2026-11-18
sources: [S309]
tags: [apps, swmm5plus, fortran, c-port, audits]
reviewed: no
---
Bob's app SWMM5+ Explorer: the Fortran source, the Lovable sketch, and a proposed C port, checked against upstream. Version 1.0.1, 2026-10-24 [S309](../sources/S309-swmm5plus-explorer-summary.md). Its `links:` line names no live Netlify address [S309](../sources/S309-swmm5plus-explorer-summary.md).

**A caution about its source.** The page ships no technical summary. [S309](../sources/S309-swmm5plus-explorer-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob marked it reviewed on 18 November 2026 (Q116, settled).

**What the summary says** [S309](../sources/S309-swmm5plus-explorer-summary.md)
- A single-file rebuild of a Lovable microsite about SWMM5+, the parallel Fortran hydraulics engine from the University of Texas at Austin published through CIMM.org: home, architecture, an engine tour, a hydraulics primer and a chat (HydroBot), with verbatim excerpts cut from the upstream source at commit afd44de. What the rebuild adds is verification: every claim the Lovable copy made is checked against the code.
- Of twelve Lovable claims in the defect register, 4 hold, 6 are wrong and 2 are partly right. It said "about 40k lines of modern Fortran" where upstream has 88,020 lines in 72 files; it said the step calls MPI_Bcast and MPI_Allreduce where no .f90 file makes an MPI call (SWMM5+ uses coarrays, with 111 sync all); it described a Roe-style upwind face flux where update.f90 uses timescale interpolation weights.
- Upstream cloned at afd44de (mirror CIMM-ORG/SWMM5plus-1); an extraction script cuts and anchors the verbatim excerpts and counts lines, files, coarray syncs and BIND(C) interfaces.
- Each Lovable claim given a verdict against the source (holds, partly, wrong).

**How to use it, as the summary puts it.** Use it to learn how SWMM5+ is built before reading the source. No SWMM5+ simulation was run, the proposed C engine has never compiled (its panes reference functions that are not defined), and the excerpts are one commit of a Beta repository. [S309](../sources/S309-swmm5plus-explorer-summary.md)

**What it does not show.** As the page lists it: no SWMM5+ simulation was run, so every number is about the source, not a result; the proposed C engine was never compiled; the excerpts are one commit of a Beta repository. [S309](../sources/S309-swmm5plus-explorer-summary.md)

**Noted at ingest.** The page shows Ben Hodges's email address as it appears in the SWMM5+ sources.

See [Apps summarized on 18 November 2026: SWMM6, SWMM5+ and solvers](../concepts/apps-from-pages-swmm6-solvers-and-swmm5plus.md), [SWMM5+ (CIMM finite-volume engine)](swmm5plus.md), [SWMM5+ Branch Atlas (app)](swmm5plus-branch-atlas.md).
