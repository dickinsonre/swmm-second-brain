---
title: "S44: swmm5-zig, EPA SWMM 5.2.4 in Zig (README)"
type: source
raw: raw/ports/2026-11-08-swmm5-zig-README.md
kind: repo-readme
author: Robert Dickinson
published: 2026-11-08
ingested: 2026-11-14
tags: [swmm5, translation, verification]
drafted_by: Claude (Anthropic), in Claude Code, at Bob's direction
reviewed: 2026-11-15
---
**What it is.** The README of the public repository SWMMBobSWMM6/swmm5-zig, as published on 2026-11-08: EPA SWMM 5.2.4 in Zig, "written by a translator that reads EPA's C, and judged against EPA itself". Raw file: [raw/ports/2026-11-08-swmm5-zig-README.md](../../raw/ports/2026-11-08-swmm5-zig-README.md).

**How it was written.** By Claude (Anthropic's AI model, Claude Opus 5.5) in Claude Code on 6 November 2026, for Bob, who chose the language for his Code Rosetta Stone app and set the byte-for-byte standard, as the README says. "Claude ran every gate and check reported here. The checks are mechanical; no person has yet reviewed the code."

**Claims worth keeping**
- Result: 480 of 480 identical (`zig_5`); 138 s of wall time for the 480.
- The first build gave 441 of 480: 39 differed in the last digits because Zig's own compiler-rt defines exp, log, sin, cos and others and captured the engine's calls. Built with `-fno-compiler-rt`, all 480 matched.
- A checked build (bounds, overflow and cast checks) first trapped on all but 3 models: the runtime's `calloc(0)` returned a pointer one past its block. After the fix: 480 of 480, no trap.
- Flags: `-mcpu=x86_64` (no FMA instruction can appear), `-fno-builtin` (LLVM keeps every libm call as written instead of folding or rewriting it).
- Engine 39,134 lines in one file; runtime 1,672 lines. Float literals are written as the shortest decimal only where a double rounding is impossible, else in hexadecimal.
- printf/strtod/sscanf checked on 1,394,252 cases: 1 differs, `%#g` of 999999.75.

**Shared with every README of this family**
- Reference: EPA SWMM 5.2.4 from the USEPA v5.2.4 tag, built with gcc 13.3 `-O2`, on x86-64 Linux with glibc 2.39. Pass: `.out` byte-identical (when EPA writes one), `.rpt` identical but the lines "Analysis begun on", "Analysis ended on" and "Total elapsed time"; from the Kotlin port on, also the same exit code (EPA's command line always exits 0); when an input error stops EPA before it writes results, the engine must not write a results file either.
- Built by the same front end, `tools/c2x/front.py`, which parses EPA's 54 C files with libclang. When the port disagreed with EPA, "the fix went into the translator or the runtime, never into the generated file".
- "It is not a new engine": every number it writes is EPA 5.2.4's, "including the results of EPA's own defects".
- Not exercised by any gate model that runs without an input error: streets and inlets, climate files, USE HOTSTART, USE INFLOWS, USE RUNOFF. The stepping API is translated, but only the command line was gated.

**Feeds:** [SWMM5 language translations](../entities/swmm5-language-ports.md), [Byte-for-byte gate](../concepts/byte-for-byte-gate.md), [What the gate cannot see](../concepts/gate-blind-spots.md), [Matching glibc math in a translation](../concepts/glibc-math-in-translation.md), [Where languages part from C](../concepts/where-languages-part-from-c.md), [EPA SWMM 5](../entities/swmm-5.md), [1729-SWMM5-Models-2030 (the corpus)](../entities/corpus-1729.md).
