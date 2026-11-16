---
title: "S52: swmm5-hy, EPA SWMM 5.2.4 in Hy (README)"
type: source
raw: raw/ports/2026-11-10-swmm5-hy-README.md
kind: repo-readme
author: Robert Dickinson
published: 2026-11-10
ingested: 2026-11-14
tags: [swmm5, translation, verification]
drafted_by: Claude (Anthropic), in Claude Code, at Bob's direction
reviewed: 2026-11-15
---
**What it is.** The README of the public repository SWMMBobSWMM6/swmm5-hy, as published on 2026-11-10: EPA SWMM 5.2.4 in Hy, "written by a translator that reads EPA's C, and judged against EPA itself". Raw file: [raw/ports/2026-11-10-swmm5-hy-README.md](../../raw/ports/2026-11-10-swmm5-hy-README.md).

**How it was written.** By Claude (Anthropic's AI model, Claude Opus 5.5) in Claude Code on 9 November 2026, for Bob, who chose the language for his Code Rosetta Stone app and set the byte-for-byte standard, as the README says. "Claude ran every gate and check reported here. The checks are mechanical; no person has yet reviewed the code."

**Claims worth keeping**
- Result: all 480 identical. 479 in the first gate (`hy_1`); 72_H&H_Elements(2).inp, which routes a dry year at a 10 s step before its 36-hour storm, timed out at 1,800 s and was identical when run on its own with a 90-minute limit (4,475 s).
- In the independent rerun 478 were identical and two not run in 1,800 s; SCANLON.inp was stopped with 98.7 % and 98.1 % of its `.out` written, identical so far, and was identical in 1,897 s on its own.
- The Hy engine is the Python back end's translation re-spelled: the emitter parses the Python with `ast` and writes each node as the Hy form that compiles back to it. The check: 3,529 top-level statements, 0 differ.
- Speed: median 56 times EPA's, 0.89 times the Python port's.
- CPython imports `exp`, `log` and `pow` at the old GLIBC_2.2.5 versions; the runtime calls glibc through `ctypes` (default versions, EPA's) wherever Python raises or decides itself.

**Shared with every README of this family**
- Reference: EPA SWMM 5.2.4 from the USEPA v5.2.4 tag, built with gcc 13.3 `-O2`, on x86-64 Linux with glibc 2.39. Pass: `.out` byte-identical (when EPA writes one), `.rpt` identical but the lines "Analysis begun on", "Analysis ended on" and "Total elapsed time"; from the Kotlin port on, also the same exit code (EPA's command line always exits 0); when an input error stops EPA before it writes results, the engine must not write a results file either.
- Built by the same front end, `tools/c2x/front.py`, which parses EPA's 54 C files with libclang. When the port disagreed with EPA, "the fix went into the translator or the runtime, never into the generated file".
- "It is not a new engine": every number it writes is EPA 5.2.4's, "including the results of EPA's own defects".
- Not exercised by any gate model that runs without an input error: streets and inlets, climate files, USE HOTSTART, USE INFLOWS, USE RUNOFF. The stepping API is translated, but only the command line was gated.

**Feeds:** [SWMM5 language translations](../entities/swmm5-language-ports.md), [Byte-for-byte gate](../concepts/byte-for-byte-gate.md), [What the gate cannot see](../concepts/gate-blind-spots.md), [Matching glibc math in a translation](../concepts/glibc-math-in-translation.md), [Where languages part from C](../concepts/where-languages-part-from-c.md), [EPA SWMM 5](../entities/swmm-5.md), [1729-SWMM5-Models-2030 (the corpus)](../entities/corpus-1729.md).
