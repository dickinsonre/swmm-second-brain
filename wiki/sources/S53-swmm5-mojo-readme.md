---
title: "S53: swmm5-mojo, EPA SWMM 5.2.4 in Mojo (README)"
type: source
raw: raw/ports/2026-11-10-swmm5-mojo-README.md
kind: repo-readme
author: Robert Dickinson
published: 2026-11-10
ingested: 2026-11-14
tags: [swmm5, translation, verification]
drafted_by: Claude (Anthropic), in Claude Code, at Bob's direction
reviewed: 2026-11-15
---
**What it is.** The README of the public repository SWMMBobSWMM6/swmm5-mojo, as published on 2026-11-10: EPA SWMM 5.2.4 in Mojo, "written by a translator that reads EPA's C, and judged against EPA itself". Raw file: [raw/ports/2026-11-10-swmm5-mojo-README.md](../../raw/ports/2026-11-10-swmm5-mojo-README.md).

**How it was written.** By Claude (Anthropic's AI model, Claude Opus 5.5) in Claude Code on 9 November 2026, for Bob, who chose the language for his Code Rosetta Stone app and set the byte-for-byte standard, as the README says. "Claude ran every gate and check reported here. The checks are mechanical; no person has yet reviewed the code."

**Claims worth keeping**
- Result: 480 of 480 identical, twice; 186 s of engine time; median 0.73 times EPA's (103 models, range 0.33 to 5.81).
- Bob asked for Mojo "even [if] you cannot run the code"; the compiler (Mojo 1.2.0) could be installed from PyPI and run, so the port was built and gated like the others.
- Mojo fuses `a*b + c` into a fused multiply-add by default; the build uses `--fp-mode contract=off`, and `objdump` finds 0 FMA instructions.
- Mojo 1.2 has no global variables (all 626 of EPA's globals are fields of one struct passed to every function) and cannot keep a function value in a struct field (function pointers are numbers with generated dispatchers).
- Mojo marked a call `tail` even when a stack slot's address was an argument, so LLVM read the slot as unwritten; locals whose address is taken now live on a heap-allocated stack.
- Math: glibc's own through `external_call` from wrappers marked `@no_inline`, because LLVM folded `pow(1.1, 2.5)` at compile time in a test.

**Shared with every README of this family**
- Reference: EPA SWMM 5.2.4 from the USEPA v5.2.4 tag, built with gcc 13.3 `-O2`, on x86-64 Linux with glibc 2.39. Pass: `.out` byte-identical (when EPA writes one), `.rpt` identical but the lines "Analysis begun on", "Analysis ended on" and "Total elapsed time"; from the Kotlin port on, also the same exit code (EPA's command line always exits 0); when an input error stops EPA before it writes results, the engine must not write a results file either.
- Built by the same front end, `tools/c2x/front.py`, which parses EPA's 54 C files with libclang. When the port disagreed with EPA, "the fix went into the translator or the runtime, never into the generated file".
- "It is not a new engine": every number it writes is EPA 5.2.4's, "including the results of EPA's own defects".
- Not exercised by any gate model that runs without an input error: streets and inlets, climate files, USE HOTSTART, USE INFLOWS, USE RUNOFF. The stepping API is translated, but only the command line was gated.

**Feeds:** [SWMM5 language translations](../entities/swmm5-language-ports.md), [Byte-for-byte gate](../concepts/byte-for-byte-gate.md), [What the gate cannot see](../concepts/gate-blind-spots.md), [Matching glibc math in a translation](../concepts/glibc-math-in-translation.md), [Where languages part from C](../concepts/where-languages-part-from-c.md), [EPA SWMM 5](../entities/swmm-5.md), [1729-SWMM5-Models-2030 (the corpus)](../entities/corpus-1729.md).
