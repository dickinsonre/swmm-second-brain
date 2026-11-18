---
title: "OpenSWMM 3D Code Model (app)"
type: entity
updated: 2026-11-17
sources: [S205, S251, S256]
tags: [apps, swmm6, openswmm, source-code, 3d]
reviewed: no
---
Bob's app OpenSWMM 3D Code Model: the OpenSWMM engine source (HydroCouple/openswmm.engine, swmm6_rel at b92a4f1 of 11 November 2026, 6.0.0-alpha.4) drawn as a city: 925 hand-written source files as boxes on folder platforms, with include links, git activity and change since the previous survey. It measures source code and contains no engine. Version 1.1, 2026-11-11 [S256](../sources/S256-openswmm-3d-code-model-app-md.md). Netlify address: https://openswmm-3d-code-model.netlify.app [S205](../sources/S205-note-netlify-addresses.md).

**Its source.** [S256](../sources/S256-openswmm-3d-code-model-app-md.md) is the technical summary the app ships with. Bob has not read this page.

**What the summary says** [S256](../sources/S256-openswmm-3d-code-model-app-md.md)
- 925 source files, 482,467 lines: the legacy SWMM 5 tree 86 files and 64,205 lines (median 527 per file); the new engine tree 714 files and 366,435 lines (median 268); Python bindings 125 files and 51,827 lines.
- Largest district 2d, 83,342 lines; second core, 66,157. Largest and busiest file SWMMEngine.cpp: 12,364 lines, 222 commits in the 90 days before the head commit (319 in all).
- SimulationContext.hpp is included directly by 158 files; Infiltration.hpp has the widest rebuild reach, 252 files. 871 of 925 files were touched in the last 30 days.
- 53 files carry the EPA SWMM5 project header; 5 name Dickinson in their comments: dwflow.c, dynwave.c, objects.h, rdii.c and stats.c.
- Checks: find returns 925 files; wc -l reports 482,460, and the 7 extra lines are the 7 files with no final newline; 917 lines added less 209 deleted = 708 = 482,467 less the previous survey's 481,759.
- Excluded: tests (595 files, 271,673 lines, 56 percent of the model's size), one Cython-generated C file (33,790 lines), documentation (536 files) and example models (381 .inp files).

**What it does not show.** One commit of an alpha that moves daily. An include link is a compile-time fact, not a call. History is by path, so no path is older than 300 days though the log runs back to 2014-03-14. Lines are not difficulty and commits are not quality. No person has checked the numbers against the repository. The survey script is not published. [S256](../sources/S256-openswmm-3d-code-model-app-md.md)

**Noted at ingest.** 64,205 + 366,435 + 51,827 = 482,467 lines and 86 + 714 + 125 = 925 files. [Understand Anything for SWMM and ICM (app)](understand-anything-swmm-icm.md) counts 284 .cpp files at an earlier commit, 79bb4e1 [S251](../sources/S251-understand-anything-swmm-icm-summary.md); that is one kind of file, not the 925 here.

See [Apps summarized on 17 November 2026: SWMM6, HydroCouple and AI](../concepts/apps-from-pages-swmm6-hydrocouple-ai.md), [OpenSWMM 6 and HydroCouple](openswmm-6-and-hydrocouple.md), [SWMM6 Code House (app)](swmm6-code-house.md), [OpenSWMM Code (app)](openswmm-code.md), [Understand Anything for SWMM and ICM (app)](understand-anything-swmm-icm.md).
