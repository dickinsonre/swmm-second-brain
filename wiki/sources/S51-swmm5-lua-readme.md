---
title: "S51: swmm5-lua, EPA SWMM 5.2.4 in Lua (README)"
type: source
raw: raw/ports/2026-11-09-swmm5-lua-README.md
kind: repo-readme
author: Robert Dickinson
published: 2026-11-09
ingested: 2026-11-14
tags: [swmm5, translation, verification]
reviewed: no
---
**What it is.** The README of the public repository SWMMBobSWMM6/swmm5-lua, as published on 2026-11-09: EPA SWMM 5.2.4 in Lua, "written by a translator that reads EPA's C, and judged against EPA itself". Raw file: [raw/ports/2026-11-09-swmm5-lua-README.md](../../raw/ports/2026-11-09-swmm5-lua-README.md).

**How it was written.** By Claude (Anthropic's AI model, Claude Opus 5.5) in Claude Code on 8 and 9 November 2026, for Bob, who chose the language for his Code Rosetta Stone app and set the byte-for-byte standard, as the README says. "Claude ran every gate and check reported here. The checks are mechanical; no person has yet reviewed the code."

**Claims worth keeping**
- Result: 480 of 480 identical, twice; 6,807 s of engine time; 72_H&H_Elements(2).inp 1,318 s, under the 1,800 s limit. Total 2.05 times the PHP port's.
- Lua 5.4.8 runs inside lupa, a Python extension; the launcher is Python, the engine is Lua.
- Lua's `x ^ 2` is `x * x`, which differs from glibc's `pow(x, 2)` in 12,953 of 20,000,000 arguments; `math.atan(x)` is `atan2(x, 1)`, different in 539 of 20,000,000. Both are glibc's code translated from GIMPLE; the rest of the math is glibc called at run time.
- lupa binds glibc's oldest symbol versions, the SVID wrappers; they differ only in `log` of a negative number (NaN sign), which the runtime corrects.
- printf/strtod/sscanf checked on 1,394,252 cases: 0 differ, `%#g` included (formatting is handed to the C library's `snprintf`).
- An array of more than 100,000 elements stores only nonzero writes: `sewer_rdii_problem.inp` runs with 1.5 GB resident instead of about 12 GB.

**Shared with every README of this family**
- Reference: EPA SWMM 5.2.4 from the USEPA v5.2.4 tag, built with gcc 13.3 `-O2`, on x86-64 Linux with glibc 2.39. Pass: `.out` byte-identical (when EPA writes one), `.rpt` identical but the lines "Analysis begun on", "Analysis ended on" and "Total elapsed time"; from the Kotlin port on, also the same exit code (EPA's command line always exits 0); when an input error stops EPA before it writes results, the engine must not write a results file either.
- Built by the same front end, `tools/c2x/front.py`, which parses EPA's 54 C files with libclang. When the port disagreed with EPA, "the fix went into the translator or the runtime, never into the generated file".
- "It is not a new engine": every number it writes is EPA 5.2.4's, "including the results of EPA's own defects".
- Not exercised by any gate model that runs without an input error: streets and inlets, climate files, USE HOTSTART, USE INFLOWS, USE RUNOFF. The stepping API is translated, but only the command line was gated.

**Feeds:** [SWMM5 language translations](../entities/swmm5-language-ports.md), [Byte-for-byte gate](../concepts/byte-for-byte-gate.md), [What the gate cannot see](../concepts/gate-blind-spots.md), [Matching glibc math in a translation](../concepts/glibc-math-in-translation.md), [Where languages part from C](../concepts/where-languages-part-from-c.md), [EPA SWMM 5](../entities/swmm-5.md), [1729-SWMM5-Models-2030 (the corpus)](../entities/corpus-1729.md).
