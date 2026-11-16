---
title: "S43: swmm5-pascal, EPA SWMM 5.2.4 in Free Pascal (README)"
type: source
raw: raw/ports/2026-11-08-swmm5-pascal-README.md
kind: repo-readme
author: Robert Dickinson
published: 2026-11-08
ingested: 2026-11-14
tags: [swmm5, translation, verification]
drafted_by: Claude (Anthropic), in Claude Code, at Bob's direction
reviewed: 2026-11-15
---
**What it is.** The README of the public repository SWMMBobSWMM6/swmm5-pascal, as published on 2026-11-08: EPA SWMM 5.2.4 in Free Pascal, "written by a translator that reads EPA's C, and judged against EPA itself". Raw file: [raw/ports/2026-11-08-swmm5-pascal-README.md](../../raw/ports/2026-11-08-swmm5-pascal-README.md).

**How it was written.** By Claude (Anthropic's AI model, Claude Opus 5.5) in Claude Code on 6 November 2026, for Bob, who chose the language for his Code Rosetta Stone app and set the byte-for-byte standard, as the README says. "Claude ran every gate and check reported here. The checks are mechanical; no person has yet reviewed the code."

**Claims worth keeping**
- Result: 480 of 480 identical (`pas_3`); 204 s of wall time for the 480 (EPA's reference run records 256 s; no speed ratio claimed).
- The engine is one unit of 52,072 lines; the 1,477-line back end is built on the Zig back end's analysis. Like Zig, it keeps C's data layout and pointers; `odesolve.c` and `mempool.c` are translated, nothing overridden.
- "Every float literal is a typed constant": an untyped real constant in Free Pascal is 80-bit Extended, so `x * 0.1` would round twice. No x87 instruction computes or compares in the engine or the runtime.
- The runtime check found the first strtod slow path wrong on 115,302 of 200,052 cases "while the gate passed all 480 models".
- printf/strtod/sscanf checked on 1,394,252 cases: 1 differs, `%#g` of 999999.75. Math is glibc's own, declared `external 'm'`, so the port follows EPA on whatever CPU both run on.
- A run built with range checks on every fixed-array index: 480 of 480, no range error.

**Shared with every README of this family**
- Reference: EPA SWMM 5.2.4 from the USEPA v5.2.4 tag, built with gcc 13.3 `-O2`, on x86-64 Linux with glibc 2.39. Pass: `.out` byte-identical (when EPA writes one), `.rpt` identical but the lines "Analysis begun on", "Analysis ended on" and "Total elapsed time"; from the Kotlin port on, also the same exit code (EPA's command line always exits 0); when an input error stops EPA before it writes results, the engine must not write a results file either.
- Built by the same front end, `tools/c2x/front.py`, which parses EPA's 54 C files with libclang. When the port disagreed with EPA, "the fix went into the translator or the runtime, never into the generated file".
- "It is not a new engine": every number it writes is EPA 5.2.4's, "including the results of EPA's own defects".
- Not exercised by any gate model that runs without an input error: streets and inlets, climate files, USE HOTSTART, USE INFLOWS, USE RUNOFF. The stepping API is translated, but only the command line was gated.

**Feeds:** [SWMM5 language translations](../entities/swmm5-language-ports.md), [Byte-for-byte gate](../concepts/byte-for-byte-gate.md), [What the gate cannot see](../concepts/gate-blind-spots.md), [Matching glibc math in a translation](../concepts/glibc-math-in-translation.md), [Where languages part from C](../concepts/where-languages-part-from-c.md), [EPA SWMM 5](../entities/swmm-5.md), [1729-SWMM5-Models-2030 (the corpus)](../entities/corpus-1729.md).
