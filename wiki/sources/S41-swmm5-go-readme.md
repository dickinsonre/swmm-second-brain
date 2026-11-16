---
title: "S41: swmm5-go, EPA SWMM 5.2.4 in Go (README)"
type: source
raw: raw/ports/2026-11-06-swmm5-go-README.md
kind: repo-readme
author: Robert Dickinson
published: 2026-11-06
ingested: 2026-11-14
tags: [swmm5, translation, verification]
drafted_by: unknown; the later READMEs of the same family name Claude (Anthropic)
reviewed: 2026-11-15
---
**What it is.** The README of the public repository SWMMBobSWMM6/swmm5-go, as published on 2026-11-06: EPA SWMM 5.2.4 in Go, "written by a translator that reads EPA's C, and judged against EPA itself". Raw file: [raw/ports/2026-11-06-swmm5-go-README.md](../../raw/ports/2026-11-06-swmm5-go-README.md).

**How it was written.** The README's own text does not say who wrote it; its AI-use section points to `AI-USE.md`, which is not a raw source here. The later READMEs of the same family say Claude wrote them. The counts rest on this text and on the gate records it names; no person has rechecked them.

**Claims worth keeping**
- Result: 480 of 480 identical. Median CPU time 1.72 times EPA's (1.47 to 2.14 over 12 models, 5 interleaved repetitions in a run of its own; EPA against itself 0.95 to 1.07).
- Corpus: 1729-SWMM5-Models-2030, folders EPA, Hydraulics, Hydrology, LID, OWA_EXTRAN and OWA_ROUTING. The gate set is 480 of the 518 distinct models (distinct by content) in those six folders; the corpus holds 4,540 .inp files. The other 38 were left out by an early timing survey with a 12-second limit, "whose records were not kept. The cut is rough": re-timed, 13 of the 38 ran past 30 s, the rest took 5.8 to 29.6 s, 4 within 12 s; and 3 gate models took longer than 12 s in the reference run (attenuation_KW_High_CE.inp 13 s, SCANLON.inp 35 s, 72_H&H_Elements(2).inp 39 s).
- 49 of the 480 stop on an input error; for 39 EPA writes no results file, the other 10 write a short one.
- Gate table on the same 480: swmm5-cplus, swmm5-rust, Fortran, C#, TypeScript, Java and Go 480 of 480; Python 465.
- Controls: EPA run twice gives 40 of 40 identical files (null control). The Fortran engine rebuilt with fused multiply-add allowed differs from EPA on 87 of 480 (positive control: "the gate catches a one-rounding-step change").
- EPA calls glibc for exp, log, log10, pow, sin, cos, tan, asin, acos and atan 1,524,961,124 times over the gate models; on x86-64 glibc picks FMA versions at start-up when the CPU has FMA and AVX2. Go's port carries glibc 2.39's FMA routines translated from GIMPLE, checked on 21,992,590 arguments, 0 differences. With Go's own `math` package the engine differs from EPA on 108 of 480.
- EPA itself, run on glibc's generic (non-FMA) routines, changes 43 of 480 models; ports that carry translated math would not follow it there.
- Every float operation is wrapped in `float64(...)`, which the Go specification says a compiler may not fuse into an FMA (Go 1.24 does fuse the unwrapped form on arm64). Engine 40,094 lines; runtime 1,846 lines.
- The repository carries an app, `app/swmm-engines.html` (*SWMM Engines, Byte for Byte*), with the essay as its Doc tab and `docs/swmm-engines-byte-for-byte.docx`.
- Not shown: "That SWMM is right: identical to EPA means EPA's answers, good or bad. No observed data enter anywhere." Speed ratios come from 12 short models. "No person has reviewed the generated code line by line."

**Shared with every README of this family**
- Reference: EPA SWMM 5.2.4 from the USEPA v5.2.4 tag, built with gcc 13.3 `-O2`, on x86-64 Linux with glibc 2.39. Pass: `.out` byte-identical (when EPA writes one), `.rpt` identical but the lines "Analysis begun on", "Analysis ended on" and "Total elapsed time"; from the Kotlin port on, also the same exit code (EPA's command line always exits 0); when an input error stops EPA before it writes results, the engine must not write a results file either.
- Built by the same front end, `tools/c2x/front.py`, which parses EPA's 54 C files with libclang. When the port disagreed with EPA, "the fix went into the translator or the runtime, never into the generated file".
- "It is not a new engine": every number it writes is EPA 5.2.4's, "including the results of EPA's own defects".
- Not exercised by any gate model that runs without an input error: streets and inlets, climate files, USE HOTSTART, USE INFLOWS, USE RUNOFF. The stepping API is translated, but only the command line was gated.

**Feeds:** [SWMM5 language translations](../entities/swmm5-language-ports.md), [Byte-for-byte gate](../concepts/byte-for-byte-gate.md), [What the gate cannot see](../concepts/gate-blind-spots.md), [Matching glibc math in a translation](../concepts/glibc-math-in-translation.md), [Where languages part from C](../concepts/where-languages-part-from-c.md), [EPA SWMM 5](../entities/swmm-5.md), [1729-SWMM5-Models-2030 (the corpus)](../entities/corpus-1729.md).
