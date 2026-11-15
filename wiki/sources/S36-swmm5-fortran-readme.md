---
title: "S36: swmm5-fortran, EPA SWMM 5.2.4 in Fortran (README)"
type: source
raw: raw/ports/2026-11-06-swmm5-fortran-README.md
kind: repo-readme
author: Robert Dickinson
published: 2026-11-06
ingested: 2026-11-14
tags: [swmm5, translation, verification]
reviewed: 2026-11-15
---
**What it is.** The README of the public repository SWMMBobSWMM6/swmm5-fortran, as published on 2026-11-06: EPA SWMM 5.2.4 in Fortran, "written by a translator that reads EPA's C, and judged against EPA itself". Raw file: [raw/ports/2026-11-06-swmm5-fortran-README.md](../../raw/ports/2026-11-06-swmm5-fortran-README.md).

**How it was written.** The README's own text does not say who wrote it; its AI-use section points to `AI-USE.md`, which is not a raw source here. The later READMEs of the same family say Claude wrote them. The counts rest on this text and on the gate records it names; no person has rechecked them.

**Claims worth keeping**
- Result: 480 of 480 identical. Median CPU time 1.26 times EPA's (1.13 to 1.40 over 12 models, 3 interleaved repetitions; EPA against itself 0.98 to 1.06).
- `emit_f90.py` writes 46,364 lines (`f90/gen/swmm5_engine.f90`, one module); hand-written runtime 4,048 lines, with hand ports of `odesolve.c`, `mempool.c` and six helpers.
- Fortran may evaluate both sides of `.and.`/`.or.`, so every C `&&`/`||` whose right side could fault or change state is written as nested IFs.
- Build flags that matter: `-fwrapv` (C's wrapping integers) and `-ffp-contract=off` (no fused multiply-add). printf, sscanf and strtod are written in pure Fortran.
- The parity table and the controls are the same as in [S41](S41-swmm5-go-readme.md).

**Shared with every README of this family**
- Reference: EPA SWMM 5.2.4 from the USEPA v5.2.4 tag, built with gcc 13.3 `-O2`, on x86-64 Linux with glibc 2.39. Pass: `.out` byte-identical (when EPA writes one), `.rpt` identical but the lines "Analysis begun on", "Analysis ended on" and "Total elapsed time"; from the Kotlin port on, also the same exit code (EPA's command line always exits 0); when an input error stops EPA before it writes results, the engine must not write a results file either.
- Built by the same front end, `tools/c2x/front.py`, which parses EPA's 54 C files with libclang. When the port disagreed with EPA, "the fix went into the translator or the runtime, never into the generated file".
- "It is not a new engine": every number it writes is EPA 5.2.4's, "including the results of EPA's own defects".
- Not exercised by any gate model that runs without an input error: streets and inlets, climate files, USE HOTSTART, USE INFLOWS, USE RUNOFF. The stepping API is translated, but only the command line was gated.

**Feeds:** [SWMM5 language translations](../entities/swmm5-language-ports.md), [Byte-for-byte gate](../concepts/byte-for-byte-gate.md), [What the gate cannot see](../concepts/gate-blind-spots.md), [Matching glibc math in a translation](../concepts/glibc-math-in-translation.md), [Where languages part from C](../concepts/where-languages-part-from-c.md), [EPA SWMM 5](../entities/swmm-5.md), [1729-SWMM5-Models-2030 (the corpus)](../entities/corpus-1729.md).
