---
name: SWMM Engines, Byte for Byte
file: swmm-engines.html
version: 2026-11-06
date: 2026-11-14
author: Robert Dickinson
links: {artifact: "https://claude.ai/artifact/W1Qz387qewJSpmAHkZtUMs", netlify: "https://nine-swmm5-engines-not-c.netlify.app (serves an earlier build titled Nine SWMM5 Engines)", repo: "SWMMBobSWMM6/swmm5-go, app/swmm-engines.html, per that repository's README"}
engines:
  - {name: EPA SWMM, version: 5.2.4, source: "USEPA/Stormwater-Management-Model, tag v5.2.4", license: public domain, use: "the reference; not embedded, not run in the page"}
  - {name: OpenSWMM 6 1D engine, source: "HydroCouple/openswmm.engine, branch swmm6_rel, commit 88329d6", license: Apache-2.0, use: "reference for the SWMM6 tab; not embedded, not run in the page"}
units: each model's own flow units (CFS, GPM, MGD, CMS, LPS, MLD), as read from its .out file
ai_use: the app was built with Claude (Anthropic). This summary was written by Claude from the page's source. See AI use.
written_from: "the published artifact's page source and its embedded results data (build stamp 2026-11-06 02:23), read on 2026-11-14. No engine was run and no test was rerun to write this file."
---

# SWMM Engines, Byte for Byte: stored gate results for translations of SWMM 5.2.4 and OpenSWMM 6

This summary was written after the fact. The page carries no technical summary of its own and shows no version number, so the version above is its build stamp. Every number below is copied from the data object embedded in the page (`const APP`) or from its About tab. Nothing here was measured again.

## What it does

It shows the stored results of one test: each translated engine runs a set of models, and its binary `.out` file must equal EPA SWMM 5.2.4's byte for byte and its `.rpt` report line for line, apart from three lines that print the wall clock. It shows results only. It runs no engine in the browser and contains no engine code.

Tabs: Scoreboard, Models, Graphs, Speed, Verify, SWMM6, About, Doc.

## What the data holds

- 480 gate models from SWMMBobSWMM6/1729-SWMM5-Models-2030, in six folders (EPA, Hydraulics, Hydrology, LID, OWA_EXTRAN, OWA_ROUTING).
- Nine engines: EPA 5.2.4 (C) as the reference, C++ (swmm5-cplus), Rust (swmm5-rust), Fortran, C#, Python, TypeScript, Java, Go.
- Per model and engine: a verdict, the run time in the gate, and short fingerprints of the `.out` and `.rpt`.
- 12 models with stored series for the Graphs tab.

## Results as stored

| Engine | Models identical to EPA | Not run |
|---|---|---|
| C++ swmm5-cplus | 480 | 0 |
| Rust swmm5-rust | 480 | 0 |
| Fortran | 480 | 0 |
| C# | 480 | 0 |
| TypeScript | 480 | 0 |
| Java | 480 | 0 |
| Go | 480 | 0 |
| Python | 465 | 15 |

- For each engine that ran all 480: 152,690 report lines and 1,244,999,775 `.out` bytes compared. For Python: 132,566 lines and 966,242,270 bytes.
- Python ran 451 of 451 fast models and 14 of the 29 slow ones; all 14 passed.
- 49 of the 480 models stop on an input error; 10 of those still write a short `.out`.

## Speed, as stored

One interleaved benchmark, 2026-10-29: 12 models, 3 repetitions, EPA taking 0.008 to 0.724 s per model. Median CPU time as a ratio to EPA:

| Engine | Median ratio |
|---|---|
| EPA run again (noise floor) | 1.005 (range 0.984 to 1.056) |
| C++ | 0.943 |
| Rust | 1.106 |
| Fortran | 1.260 |
| Go | 1.723 |
| C# | 5.194 |
| Java | 9.175 |
| TypeScript | 19.236 |
| Python | 81.628 |

The page says the gate's own run times are not used for speed, because the gate ran two jobs at once on a two-core machine.

A separate table gives one run of a model it calls Greenville, in seconds: EPA 2.021, C++ 1.868, Rust 2.335, Fortran 2.47, Go 3.745, C# 6.186, Java 7.95, TypeScript 27.178, Python 180.501; and for the SWMM6 family: Rust 5.782, C++ 6.143, C# 15.468, Java 15.964, Go 23.328, Fortran 72.758, TypeScript 83.356, Python 676.276.

## Controls, as stored

- Null control: EPA run twice on 40 models, 40 of 40 identical.
- Positive control (a one-rounding-step change; the data keys name it `fma`, fused multiply-add): 87 of 480 models change; in the 40-model set, 3 of 40.
- EPA on glibc's generic math routines: 43 of 480 models change.
- Fortran formatter against glibc: 52,402,636 printf, 531,658 sscanf and 248,060 strtod cases, 0 mismatches.
- Go formatter against glibc: 1,194,187 printf cases with 1 mismatch (`%#g` of 999999.5, a form the page says SWMM never uses), 200,052 strtod and 13 sscanf cases with 0.
- Math library: over the gate models EPA makes 1,524,961,124 calls to the math library, 1,235,269,125 of them to `pow`. The TypeScript, Java and Go copies of glibc's routines each show 0 mismatches against glibc on every function tested (for example 7,988,343 `pow` cases).

## The translator's census of EPA's C, as stored

The page stores what the translator's front end counted in EPA SWMM 5.2.4: 54 files, 968 functions, 626 globals, 103 records, 714 enumerators and 2,083 pointer and array declarations. It stores line counts too: 50,788 lines of EPA's C, 10,231 lines of translator, and for the generated engines 46,364 lines of Fortran, 41,429 of C#, 31,568 of Python, 41,192 of TypeScript, 44,855 of Java and 40,094 of Go, each with a hand-written runtime of 971 to 4,048 lines.

## Defect register: EPA SWMM 5.2.4

Five entries, each with file and line: `inlet.c:146` (a keyword list with no NULL sentinel), `gage.c:251` (an int overflow when a time series has one point), `swmm5.c:1593` (a full path written into a 260-byte buffer), `output.c:523` (an 8-byte value written with a 4-byte size), `project.c:421` (a memset that counts doubles where bytes are needed). The page says how each port handles each one.

## SWMM6 tab, as stored

Six translations of the OpenSWMM 6 1D engine at commit 88329d6, each judged against the C++ engine built from the same commit and run on one thread, on the same 480 models and on 452 extra decks (336 from the upstream tests, 116 from swmm6-rust).

| Port | 480 models | 452 extra decks |
|---|---|---|
| C# | 480 of 480 | 452 of 452 |
| Go | 480 of 480 | 452 of 452 |
| Java | 480 of 480 | 452 of 452 |
| TypeScript | 480 of 480 | 452 of 452 |
| Fortran | 480 of 480 | 452 of 452 |
| Python | 412 of 413 run | 450 of 452 |

31 lessons from the translation are listed, each linked to the swmm6-csharp repository.

## What this does not show

From the page's own list:

1. Identical to EPA means EPA's answers, right or wrong. No observed flow enters anywhere.
2. One platform: x86-64 Linux, glibc 2.39, gcc 13.3.
3. The gate set is 480 of the 518 distinct models in six folders of a corpus of 4,540 `.inp` files. The other 38 were left out by an early timing survey whose records were not kept.
4. Only 87 of the 480 models noticed the positive control, so the bit-level evidence rests mostly on them.
5. Among models that ran without an input error, none exercises streets and inlets, a climate file, USE HOTSTART, USE INFLOWS or USE RUNOFF. Snowmelt runs in 4.
6. The stepping API was translated but not gated; only the command line was.
7. No person has read the generated code line by line.

Added by this summary:

8. This file was written from the page, not from the repositories. The stored results were not rerun.
9. The page shows no version number. The public Netlify address serves an earlier build under the name Nine SWMM5 Engines.
10. The embedded data does not say what the two first-pass counts on the extra decks mean, so they are left out.

## How to reproduce

The page points to the repositories: the gate and benchmark scripts are in SWMMBobSWMM6/swmm5-go, and each engine is in its own repository under SWMMBobSWMM6. To check this summary, open the artifact, view the page source, and read the `const APP` object.

## Credits and licenses

- EPA SWMM 5.2.4: USEPA, public domain.
- OpenSWMM Engine: Copyright 2026 HydroCouple Developers, Apache-2.0. Portions derive from USEPA SWMM. The page says it contains no engine code and that neither HydroCouple nor the USEPA endorses it.
- glibc 2.39 math routines (translated in the TypeScript, Java and Go ports): LGPL-2.1-or-later.
- The engines, the corpus and the app: Robert Dickinson, github.com/SWMMBobSWMM6.

## AI use

From the page's About tab: the six ports, the translator, the translated math routines, the app and its essay were made with Claude, Anthropic's AI model, in Claude Code sessions in October 2026, under the direction of Robert (Bob) Dickinson. He chose the languages, set the test, chose the repositories and the app, and is responsible for the work. The SWMM6 ports (November 2026) were made the same way with Claude Opus 5.5. A second Claude instance audited the essay's claims against the stored evidence. The page says no person has reviewed the generated code line by line.

This summary: written by Claude (model claude-fable-5-2) on 14 November 2026 at Bob's request, from the page source only. Bob has not yet read it.

## Changes

- `2026-11-06`: build stamp of the page this summary describes. The page records no change history. The public Netlify build is titled Nine SWMM5 Engines, and the page's own storage key is `sixengines_seen`, which suggests earlier builds with six and nine engines.
