---
title: "S38: swmm5-python, EPA SWMM 5.2.4 in Python (README)"
type: source
raw: raw/ports/2026-11-06-swmm5-python-README.md
kind: repo-readme
author: Robert Dickinson
published: 2026-11-06
ingested: 2026-11-14
tags: [swmm5, translation, verification]
drafted_by: unknown; the later READMEs of the same family name Claude (Anthropic)
reviewed: 2026-11-15
---
**What it is.** The README of the public repository SWMMBobSWMM6/swmm5-python, as published on 2026-11-06: EPA SWMM 5.2.4 in Python, "written by a translator that reads EPA's C, and judged against EPA itself". Raw file: [raw/ports/2026-11-06-swmm5-python-README.md](../../raw/ports/2026-11-06-swmm5-python-README.md).

**How it was written.** The README's own text does not say who wrote it; its AI-use section points to `AI-USE.md`, which is not a raw source here. The later READMEs of the same family say Claude wrote them. The counts rest on this text and on the gate records it names; no person has rechecked them.

**Claims worth keeping**
- Result: 451 of the 451 fast models (EPA within 1.5 s) identical, and 14 of a 14-model sample of the 29 slower ones identical: 465 in all.
- Median CPU time 81.63 times EPA's (57.02 to 99.04 over 12 models, 3 interleaved repetitions).
- `emit_py.py` writes 31,568 lines (`py/swmm5/engine.py`); hand-written runtime 1,253 lines; standard library only, Python 3.10 or newer.
- Scalars whose address C takes are boxed; C's integer division, modulo and 32-bit wraparound are spelled out; floating division by zero returns C's infinities and the x86 NaN (sign bit set, printed `-nan`).

**Shared with every README of this family**
- Reference: EPA SWMM 5.2.4 from the USEPA v5.2.4 tag, built with gcc 13.3 `-O2`, on x86-64 Linux with glibc 2.39. Pass: `.out` byte-identical (when EPA writes one), `.rpt` identical but the lines "Analysis begun on", "Analysis ended on" and "Total elapsed time"; from the Kotlin port on, also the same exit code (EPA's command line always exits 0); when an input error stops EPA before it writes results, the engine must not write a results file either.
- Built by the same front end, `tools/c2x/front.py`, which parses EPA's 54 C files with libclang. When the port disagreed with EPA, "the fix went into the translator or the runtime, never into the generated file".
- "It is not a new engine": every number it writes is EPA 5.2.4's, "including the results of EPA's own defects".
- Not exercised by any gate model that runs without an input error: streets and inlets, climate files, USE HOTSTART, USE INFLOWS, USE RUNOFF. The stepping API is translated, but only the command line was gated.

**Feeds:** [SWMM5 language translations](../entities/swmm5-language-ports.md), [Byte-for-byte gate](../concepts/byte-for-byte-gate.md), [What the gate cannot see](../concepts/gate-blind-spots.md), [Matching glibc math in a translation](../concepts/glibc-math-in-translation.md), [Where languages part from C](../concepts/where-languages-part-from-c.md), [EPA SWMM 5](../entities/swmm-5.md), [1729-SWMM5-Models-2030 (the corpus)](../entities/corpus-1729.md).
