---
title: "S46: swmm5-javascript, EPA SWMM 5.2.4 in JavaScript (README)"
type: source
raw: raw/ports/2026-11-09-swmm5-javascript-README.md
kind: repo-readme
author: Robert Dickinson
published: 2026-11-09
ingested: 2026-11-14
tags: [swmm5, translation, verification]
reviewed: no
---
**What it is.** The README of the public repository SWMMBobSWMM6/swmm5-javascript, as published on 2026-11-09: EPA SWMM 5.2.4 in JavaScript, "written by a translator that reads EPA's C, and judged against EPA itself". Raw file: [raw/ports/2026-11-09-swmm5-javascript-README.md](../../raw/ports/2026-11-09-swmm5-javascript-README.md).

**How it was written.** By Claude (Anthropic's AI model, Claude Opus 5.5) in Claude Code on 8 November 2026, for Bob, who chose the language for his Code Rosetta Stone app and set the byte-for-byte standard, as the README says. "Claude ran every gate and check reported here. The checks are mechanical; no person has yet reviewed the code." Most of the work is the TypeScript port's, carried over.

**Claims worth keeping**
- Result: 480 of 480 identical (`js_2a` to `js_2d`), and 480 of 480 again from a clean regeneration (`js_va` to `js_vd`); 1,737 s of wall time.
- `emit_js.py` (216 lines) subclasses the TypeScript back end: with signatures and hoisted declarations set aside, the 36,297 lines of function bodies are identical to a freshly generated `engine.ts`. The math (`glibm.js`) is line for line the TypeScript translation.
- The runtime was checked against glibc and changed in four places; replayed through the TypeScript runtime, the glibc cases differ in 964 places, none reached by the 480 models.
- V8 returned `strtod("-nan")` as `nan` with the sign bit cleared once the function was hot; passing the result through a `Float64Array` fixed it.
- V8's `Math.pow` differs from glibc on 9.1 % of the arguments tested.

**Shared with every README of this family**
- Reference: EPA SWMM 5.2.4 from the USEPA v5.2.4 tag, built with gcc 13.3 `-O2`, on x86-64 Linux with glibc 2.39. Pass: `.out` byte-identical (when EPA writes one), `.rpt` identical but the lines "Analysis begun on", "Analysis ended on" and "Total elapsed time"; from the Kotlin port on, also the same exit code (EPA's command line always exits 0); when an input error stops EPA before it writes results, the engine must not write a results file either.
- Built by the same front end, `tools/c2x/front.py`, which parses EPA's 54 C files with libclang. When the port disagreed with EPA, "the fix went into the translator or the runtime, never into the generated file".
- "It is not a new engine": every number it writes is EPA 5.2.4's, "including the results of EPA's own defects".
- Not exercised by any gate model that runs without an input error: streets and inlets, climate files, USE HOTSTART, USE INFLOWS, USE RUNOFF. The stepping API is translated, but only the command line was gated.

**Feeds:** [SWMM5 language translations](../entities/swmm5-language-ports.md), [Byte-for-byte gate](../concepts/byte-for-byte-gate.md), [What the gate cannot see](../concepts/gate-blind-spots.md), [Matching glibc math in a translation](../concepts/glibc-math-in-translation.md), [Where languages part from C](../concepts/where-languages-part-from-c.md), [EPA SWMM 5](../entities/swmm-5.md), [1729-SWMM5-Models-2030 (the corpus)](../entities/corpus-1729.md).
