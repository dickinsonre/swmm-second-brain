---
title: "S71: SWMM Engines, Byte for Byte, summary written from the page (2026-11-14)"
type: source
raw: raw/apps/swmm-engines-v2026-11-06.md
kind: app-md
author: Robert Dickinson
published: 2026-11-14
ingested: 2026-11-14
tags: [apps, swmm5, swmm6, translation, verification, benchmarks]
reviewed: 2026-11-15
---
**What it is.** A technical summary of the app SWMM Engines, Byte for Byte, which shows the stored gate results for translations of EPA SWMM 5.2.4 and OpenSWMM 6. Raw file: [raw/apps/swmm-engines-v2026-11-06.md](../../raw/apps/swmm-engines-v2026-11-06.md).

**How it was written. This one is different.** The page carries no summary of its own. Claude (Anthropic, model claude-fable-5-2) wrote this file on 14 November 2026, at Bob's request, from the published artifact's page source and the results data embedded in it (build stamp 2026-11-06 02:23). No engine was run and no test was rerun. Bob has not read it. The app itself was built with Claude in October and November 2026 under Bob's direction, and its About tab says so.

**Claims worth keeping** (all copied from the page's data)
- 480 gate models; nine engines with EPA 5.2.4 as the reference. C++, Rust, Fortran, C#, TypeScript, Java and Go are identical to EPA on 480. Python on 465, with 15 not run.
- Per engine that ran all 480: 152,690 report lines and 1,244,999,775 `.out` bytes compared.
- Benchmark of 2026-10-29, 12 models, 3 repetitions, median CPU ratio to EPA: C++ 0.943, Rust 1.106, Fortran 1.260, Go 1.723, C# 5.194, Java 9.175, TypeScript 19.236, Python 81.628. EPA against itself 1.005 (0.984 to 1.056).
- Controls: EPA twice, 40 of 40 identical. A one-rounding-step change (keyed `fma`) alters 87 of 480 models. EPA on glibc's generic math alters 43 of 480.
- Fortran formatter against glibc: 52,402,636 printf, 531,658 sscanf and 248,060 strtod cases, 0 mismatches.
- EPA makes 1,524,961,124 math-library calls over the gate models, 1,235,269,125 of them to `pow`.
- The translator's front end counts 54 files, 968 functions, 626 globals and 2,083 declarations in EPA's C, and 50,788 lines.
- A defect register for EPA SWMM 5.2.4 with five entries: `inlet.c:146`, `gage.c:251`, `swmm5.c:1593`, `output.c:523`, `project.c:421`.
- 49 of the 480 models stop on an input error. Among models that ran, none exercises streets and inlets, a climate file, USE HOTSTART, USE INFLOWS or USE RUNOFF.
- SWMM6 tab: six translations at commit 88329d6. C#, Go, Java, TypeScript and Fortran pass 480 of 480 and 452 of 452 extra decks; Python 412 of 413 run and 450 of 452. 31 lessons are listed.
- One run of a model the page calls Greenville, in seconds: EPA 2.021, C++ 1.868, Rust 2.335, Fortran 2.47, Go 3.745, C# 6.186, Java 7.95, TypeScript 27.178, Python 180.501.

**Limits it states.** "Identical to EPA means EPA's answers, right or wrong." One platform. Only 87 models noticed the positive control. The stepping API was not gated. No person has read the generated code line by line. And of itself: written from the page, not from the repositories.

**Checked at ingest.** Every number in the raw file was read from the page's `const APP` object by script, in the same session that wrote it. That is a copy check, not an independent one.

**Feeds:** [SWMM Engines, Byte for Byte (app)](../entities/swmm-engines-byte-for-byte.md), [SWMM5 language translations](../entities/swmm5-language-ports.md), [SWMM6 language translations](../entities/swmm6-language-ports.md), [EPA SWMM 5](../entities/swmm-5.md), [The SWMM findings register](../concepts/findings-register.md).
