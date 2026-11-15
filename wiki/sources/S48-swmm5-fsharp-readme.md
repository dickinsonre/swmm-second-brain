---
title: "S48: swmm5-fsharp, EPA SWMM 5.2.4 in F# (README)"
type: source
raw: raw/ports/2026-11-09-swmm5-fsharp-README.md
kind: repo-readme
author: Robert Dickinson
published: 2026-11-09
ingested: 2026-11-14
tags: [swmm5, translation, verification]
reviewed: 2026-11-15
---
**What it is.** The README of the public repository SWMMBobSWMM6/swmm5-fsharp, as published on 2026-11-09: EPA SWMM 5.2.4 in F#, "written by a translator that reads EPA's C, and judged against EPA itself". Raw file: [raw/ports/2026-11-09-swmm5-fsharp-README.md](../../raw/ports/2026-11-09-swmm5-fsharp-README.md).

**How it was written.** By Claude (Anthropic's AI model, Claude Opus 5.5) in Claude Code on 8 November 2026, for Bob, who chose the language for his Code Rosetta Stone app and set the byte-for-byte standard, as the README says. "Claude ran every gate and check reported here. The checks are mechanical; no person has yet reviewed the code."

**Claims worth keeping**
- Result: 480 of 480 identical (`fs_1`), and again in the independent rerun (`fs_v`); 372 s of wall time.
- F# has no `return`, `break`, `continue` or `goto`. Of 2,336 returns, 476 switch breaks, 86 continues and 50 loop breaks in EPA's 951 functions, 1,785 returns, all switch breaks and 85 continues became structure; 551 returns, the 50 loop breaks and 1 continue set a flag. No exception is used for control flow.
- Math: glibc called by P/Invoke (`DllImport("libm.so.6")`) at EPA's default symbol versions; 0 differ on the math checks.
- "The F# engine passed every gate model on its first gate run"; its four translator fixes were found by the compiler or by reading the output.
- The clean rebuild's `.dll` has the same IL in all 3,795 method bodies; the two files differ in 81 bytes of debug-directory padding.

**Shared with every README of this family**
- Reference: EPA SWMM 5.2.4 from the USEPA v5.2.4 tag, built with gcc 13.3 `-O2`, on x86-64 Linux with glibc 2.39. Pass: `.out` byte-identical (when EPA writes one), `.rpt` identical but the lines "Analysis begun on", "Analysis ended on" and "Total elapsed time"; from the Kotlin port on, also the same exit code (EPA's command line always exits 0); when an input error stops EPA before it writes results, the engine must not write a results file either.
- Built by the same front end, `tools/c2x/front.py`, which parses EPA's 54 C files with libclang. When the port disagreed with EPA, "the fix went into the translator or the runtime, never into the generated file".
- "It is not a new engine": every number it writes is EPA 5.2.4's, "including the results of EPA's own defects".
- Not exercised by any gate model that runs without an input error: streets and inlets, climate files, USE HOTSTART, USE INFLOWS, USE RUNOFF. The stepping API is translated, but only the command line was gated.

**Feeds:** [SWMM5 language translations](../entities/swmm5-language-ports.md), [Byte-for-byte gate](../concepts/byte-for-byte-gate.md), [What the gate cannot see](../concepts/gate-blind-spots.md), [Matching glibc math in a translation](../concepts/glibc-math-in-translation.md), [Where languages part from C](../concepts/where-languages-part-from-c.md), [EPA SWMM 5](../entities/swmm-5.md), [1729-SWMM5-Models-2030 (the corpus)](../entities/corpus-1729.md).
