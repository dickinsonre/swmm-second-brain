---
title: "S47: swmm5-php, EPA SWMM 5.2.4 in PHP (README)"
type: source
raw: raw/ports/2026-11-09-swmm5-php-README.md
kind: repo-readme
author: Robert Dickinson
published: 2026-11-09
ingested: 2026-11-14
tags: [swmm5, translation, verification]
reviewed: 2026-11-15
---
**What it is.** The README of the public repository SWMMBobSWMM6/swmm5-php, as published on 2026-11-09: EPA SWMM 5.2.4 in PHP, "written by a translator that reads EPA's C, and judged against EPA itself". Raw file: [raw/ports/2026-11-09-swmm5-php-README.md](../../raw/ports/2026-11-09-swmm5-php-README.md).

**How it was written.** By Claude (Anthropic's AI model, Claude Opus 5.5) in Claude Code on 8 November 2026, for Bob, who chose the language for his Code Rosetta Stone app and set the byte-for-byte standard, as the README says. "Claude ran every gate and check reported here. The checks are mechanical; no person has yet reviewed the code."

**Claims worth keeping**
- Result: 480 of 480 identical, twice (first gate and an independent rerun from a clean checkout). No model timed out; the longest took 620 s (72_H&H_Elements(2).inp), SCANLON.inp 431 s.
- Speed: median 13.9 times EPA's (103 models, range 3.6 to 25.7); 0.20 times the Ruby port's. 3,315 s of engine time for the 480, with OPcache's tracing JIT on.
- PHP keeps C's statements (`switch` with fall-through, `break`, `continue`); the differences are in the data: arrays are values, so every C array is an object; `/` throws on division by zero even for floats; `-$x` leaves a NaN's sign alone where C flips it.
- OPcache's SCCP optimizer pass treats 0.0 and -0.0 as the same constant; it is switched off.
- A double array of more than 100,000 elements is FFI storage: `sewer_rdii_problem.inp`'s 3.4 GB of RDII history would not fit as PHP arrays in 7 GB.
- Math: PHP calls glibc at EPA's symbol versions; PHP's `floor` and `ceil` return a signaling NaN unchanged where glibc quiets it. A check found 0 fused multiply-adds under the interpreter and both JITs.

**Shared with every README of this family**
- Reference: EPA SWMM 5.2.4 from the USEPA v5.2.4 tag, built with gcc 13.3 `-O2`, on x86-64 Linux with glibc 2.39. Pass: `.out` byte-identical (when EPA writes one), `.rpt` identical but the lines "Analysis begun on", "Analysis ended on" and "Total elapsed time"; from the Kotlin port on, also the same exit code (EPA's command line always exits 0); when an input error stops EPA before it writes results, the engine must not write a results file either.
- Built by the same front end, `tools/c2x/front.py`, which parses EPA's 54 C files with libclang. When the port disagreed with EPA, "the fix went into the translator or the runtime, never into the generated file".
- "It is not a new engine": every number it writes is EPA 5.2.4's, "including the results of EPA's own defects".
- Not exercised by any gate model that runs without an input error: streets and inlets, climate files, USE HOTSTART, USE INFLOWS, USE RUNOFF. The stepping API is translated, but only the command line was gated.

**Feeds:** [SWMM5 language translations](../entities/swmm5-language-ports.md), [Byte-for-byte gate](../concepts/byte-for-byte-gate.md), [What the gate cannot see](../concepts/gate-blind-spots.md), [Matching glibc math in a translation](../concepts/glibc-math-in-translation.md), [Where languages part from C](../concepts/where-languages-part-from-c.md), [EPA SWMM 5](../entities/swmm-5.md), [1729-SWMM5-Models-2030 (the corpus)](../entities/corpus-1729.md).
