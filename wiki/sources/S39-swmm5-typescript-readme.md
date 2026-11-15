---
title: "S39: swmm5-typescript, EPA SWMM 5.2.4 in TypeScript (README)"
type: source
raw: raw/ports/2026-11-06-swmm5-typescript-README.md
kind: repo-readme
author: Robert Dickinson
published: 2026-11-06
ingested: 2026-11-14
tags: [swmm5, translation, verification]
reviewed: 2026-11-15
---
**What it is.** The README of the public repository SWMMBobSWMM6/swmm5-typescript, as published on 2026-11-06: EPA SWMM 5.2.4 in TypeScript, "written by a translator that reads EPA's C, and judged against EPA itself". Raw file: [raw/ports/2026-11-06-swmm5-typescript-README.md](../../raw/ports/2026-11-06-swmm5-typescript-README.md).

**How it was written.** The README's own text does not say who wrote it; its AI-use section points to `AI-USE.md`, which is not a raw source here. The later READMEs of the same family say Claude wrote them. The counts rest on this text and on the gate records it names; no person has rechecked them.

**Claims worth keeping**
- Result: 480 of 480 identical. Median CPU time 19.24 times EPA's (11.44 to 73.66 over 12 models, 5 interleaved repetitions in a run of their own; EPA against itself 0.87 to 1.32).
- `emit_ts.py` writes 41,192 lines (`ts/src/engine.ts`); hand-written runtime 971 lines.
- Every number is a JavaScript double, so integer arithmetic is spelled out so it can never yield -0: `(0 - x)`, `Math.imul`, `(a / b) | 0`; unsigned values with `>>> 0`.
- Math: `ts/src/glibm.ts` is glibc 2.39's FMA build of the ten functions, translated from GCC's GIMPLE. Positive control: with JavaScript's own `Math` the engine differs from EPA on 6 of 40 control models.
- Needs Node.js 18 or newer; `npm install` fetches TypeScript 5.6.

**Shared with every README of this family**
- Reference: EPA SWMM 5.2.4 from the USEPA v5.2.4 tag, built with gcc 13.3 `-O2`, on x86-64 Linux with glibc 2.39. Pass: `.out` byte-identical (when EPA writes one), `.rpt` identical but the lines "Analysis begun on", "Analysis ended on" and "Total elapsed time"; from the Kotlin port on, also the same exit code (EPA's command line always exits 0); when an input error stops EPA before it writes results, the engine must not write a results file either.
- Built by the same front end, `tools/c2x/front.py`, which parses EPA's 54 C files with libclang. When the port disagreed with EPA, "the fix went into the translator or the runtime, never into the generated file".
- "It is not a new engine": every number it writes is EPA 5.2.4's, "including the results of EPA's own defects".
- Not exercised by any gate model that runs without an input error: streets and inlets, climate files, USE HOTSTART, USE INFLOWS, USE RUNOFF. The stepping API is translated, but only the command line was gated.

**Feeds:** [SWMM5 language translations](../entities/swmm5-language-ports.md), [Byte-for-byte gate](../concepts/byte-for-byte-gate.md), [What the gate cannot see](../concepts/gate-blind-spots.md), [Matching glibc math in a translation](../concepts/glibc-math-in-translation.md), [Where languages part from C](../concepts/where-languages-part-from-c.md), [EPA SWMM 5](../entities/swmm-5.md), [1729-SWMM5-Models-2030 (the corpus)](../entities/corpus-1729.md).
