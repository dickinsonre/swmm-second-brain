---
title: "S50: swmm5-groovy, EPA SWMM 5.2.4 in Groovy (README)"
type: source
raw: raw/ports/2026-11-09-swmm5-groovy-README.md
kind: repo-readme
author: Robert Dickinson
published: 2026-11-09
ingested: 2026-11-14
tags: [swmm5, translation, verification]
drafted_by: Claude (Anthropic), in Claude Code, at Bob's direction
reviewed: 2026-11-15
---
**What it is.** The README of the public repository SWMMBobSWMM6/swmm5-groovy, as published on 2026-11-09: EPA SWMM 5.2.4 in Groovy, "written by a translator that reads EPA's C, and judged against EPA itself". Raw file: [raw/ports/2026-11-09-swmm5-groovy-README.md](../../raw/ports/2026-11-09-swmm5-groovy-README.md).

**How it was written.** By Claude (Anthropic's AI model, Claude Opus 5.5) in Claude Code on 8 and 9 November 2026, for Bob, who chose the language for his Code Rosetta Stone app and set the byte-for-byte standard, as the README says. "Claude ran every gate and check reported here. The checks are mechanical; no person has yet reviewed the code."

**Claims worth keeping**
- Result: 480 of 480 identical, twice; 1,114 s of engine time in `gv_1`, 792 s in the rerun of the same code: "the load of the shared machine moves the gate's clock by that much".
- In Groovy, `a > b` and `a >= b` on doubles are true when either side is NaN; C says false. Found on `swmm5_shapes.inp`, whose report listed five NaN nodes as not converging.
- A decimal literal is a `BigDecimal`, `-0.0d` is folded to +0.0, and `/` on two ints gives a `BigDecimal`: each is written out.
- HotSpot never JIT-compiles a method over 8,000 bytes of bytecode; Groovy's pow is 9,161 bytes. With the default, SCANLON ran more than 380 s without finishing; with `-XX:-DontCompileHugeMethods`, 32.6 s.
- Math: `Glibm.groovy` from a Groovy back end of `gim2x.py`; 0 differ; the other back ends' outputs unchanged.

**Shared with every README of this family**
- Reference: EPA SWMM 5.2.4 from the USEPA v5.2.4 tag, built with gcc 13.3 `-O2`, on x86-64 Linux with glibc 2.39. Pass: `.out` byte-identical (when EPA writes one), `.rpt` identical but the lines "Analysis begun on", "Analysis ended on" and "Total elapsed time"; from the Kotlin port on, also the same exit code (EPA's command line always exits 0); when an input error stops EPA before it writes results, the engine must not write a results file either.
- Built by the same front end, `tools/c2x/front.py`, which parses EPA's 54 C files with libclang. When the port disagreed with EPA, "the fix went into the translator or the runtime, never into the generated file".
- "It is not a new engine": every number it writes is EPA 5.2.4's, "including the results of EPA's own defects".
- Not exercised by any gate model that runs without an input error: streets and inlets, climate files, USE HOTSTART, USE INFLOWS, USE RUNOFF. The stepping API is translated, but only the command line was gated.

**Feeds:** [SWMM5 language translations](../entities/swmm5-language-ports.md), [Byte-for-byte gate](../concepts/byte-for-byte-gate.md), [What the gate cannot see](../concepts/gate-blind-spots.md), [Matching glibc math in a translation](../concepts/glibc-math-in-translation.md), [Where languages part from C](../concepts/where-languages-part-from-c.md), [EPA SWMM 5](../entities/swmm-5.md), [1729-SWMM5-Models-2030 (the corpus)](../entities/corpus-1729.md).
