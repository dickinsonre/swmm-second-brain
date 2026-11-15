---
title: "S54: swmm5-r, EPA SWMM 5.2.4 in R (README)"
type: source
raw: raw/ports/2026-11-12-swmm5-r-README.md
kind: repo-readme
author: Robert Dickinson
published: 2026-11-12
ingested: 2026-11-14
tags: [swmm5, translation, verification]
reviewed: 2026-11-15
---
**What it is.** The README of the public repository SWMMBobSWMM6/swmm5-r, as published on 2026-11-12: EPA SWMM 5.2.4 in R, "written by a translator that reads EPA's C, and judged against EPA itself". Raw file: [raw/ports/2026-11-12-swmm5-r-README.md](../../raw/ports/2026-11-12-swmm5-r-README.md).

**How it was written.** By Claude (Anthropic's AI model, Claude Opus 5.5) in Claude Code on 10 to 12 November 2026, for Bob, who chose the language for his Code Rosetta Stone app and set the byte-for-byte standard, as the README says. "Claude ran every gate and check reported here. The checks are mechanical; no person has yet reviewed the code."

**Claims worth keeping**
- Result: 465 of 480 identical; 15 not run (timed out after 1,800 s), each identical to EPA's output as far as it had got; 0 differ, 0 crashed. Independent rerun of a sample: 102 of 103, 1 not run. Main session's check: 46 of 47, 1 not run.
- Speed: on the 465, R took 37,055 s, EPA 91.4 s and the Hy port 4,402 s: "about 400 times EPA's time and 8.4 times Hy's".
- Two engines from the same C: a fast one with R's plain comparisons, which stops with an error on a NaN, and a safe one, NaN-proof, which reruns the model from the start when the fast one stops. "The fast engine never gives a different answer silently."
- The first R run of `sewer_rdii_problem.inp` was killed at 6 GB: rdii.c callocs 375 million past-rainfall values that EPA almost never touches, and R zero-fills up front. Three rdii.c functions are hand ports in which an empty array stands for zeros; all 23 RDII decks were rerun on that engine.
- R's `x ^ 2` squares; `pow(x, 2)` is reached through `qweibull`, which calls glibc's pow inside R's math library. R hands signaling NaNs back unchanged (663 test cases), which no SWMM value can be.
- printf/strtod/sscanf: 0 of 1,389,850 differ, `%#g` included.

**Shared with every README of this family**
- Reference: EPA SWMM 5.2.4 from the USEPA v5.2.4 tag, built with gcc 13.3 `-O2`, on x86-64 Linux with glibc 2.39. Pass: `.out` byte-identical (when EPA writes one), `.rpt` identical but the lines "Analysis begun on", "Analysis ended on" and "Total elapsed time"; from the Kotlin port on, also the same exit code (EPA's command line always exits 0); when an input error stops EPA before it writes results, the engine must not write a results file either.
- Built by the same front end, `tools/c2x/front.py`, which parses EPA's 54 C files with libclang. When the port disagreed with EPA, "the fix went into the translator or the runtime, never into the generated file".
- "It is not a new engine": every number it writes is EPA 5.2.4's, "including the results of EPA's own defects".
- Not exercised by any gate model that runs without an input error: streets and inlets, climate files, USE HOTSTART, USE INFLOWS, USE RUNOFF. The stepping API is translated, but only the command line was gated.

**Feeds:** [SWMM5 language translations](../entities/swmm5-language-ports.md), [Byte-for-byte gate](../concepts/byte-for-byte-gate.md), [What the gate cannot see](../concepts/gate-blind-spots.md), [Matching glibc math in a translation](../concepts/glibc-math-in-translation.md), [Where languages part from C](../concepts/where-languages-part-from-c.md), [EPA SWMM 5](../entities/swmm-5.md), [1729-SWMM5-Models-2030 (the corpus)](../entities/corpus-1729.md).
