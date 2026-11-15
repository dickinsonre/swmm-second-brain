---
title: "S45: swmm5-ruby, EPA SWMM 5.2.4 in Ruby (README)"
type: source
raw: raw/ports/2026-11-09-swmm5-ruby-README.md
kind: repo-readme
author: Robert Dickinson
published: 2026-11-09
ingested: 2026-11-14
tags: [swmm5, translation, verification]
reviewed: 2026-11-15
---
**What it is.** The README of the public repository SWMMBobSWMM6/swmm5-ruby, as published on 2026-11-09: EPA SWMM 5.2.4 in Ruby, "written by a translator that reads EPA's C, and judged against EPA itself". Raw file: [raw/ports/2026-11-09-swmm5-ruby-README.md](../../raw/ports/2026-11-09-swmm5-ruby-README.md).

**How it was written.** By Claude (Anthropic's AI model, Claude Opus 5.5) in Claude Code on 8 November 2026, for Bob, who chose the language for his Code Rosetta Stone app and set the byte-for-byte standard, as the README says. "Claude ran every gate and check reported here. The checks are mechanical; no person has yet reviewed the code."

**Claims worth keeping**
- Result: 478 of 480 ran and all 478 are identical; SCANLON.inp and 72_H&H_Elements(2).inp were not run (stopped at 1,800 s), the two models EPA takes longest on (34.8 s and 38.6 s). A later try with 3,300 s did not finish either.
- Ruby replaced Scala: the sandbox could not fetch or run a Scala compiler, and Bob chose Ruby, "the scripting language of InfoWorks ICM".
- Discovery runs found 27 models differing in a report's last digit, because MRI's `format` is not correctly rounded (36.15 printed as "36.2" with `%.1f`; glibc prints "36.1"), and one `.out` differing in its NaNs' sign bits.
- Speed: median 70 times EPA's (101 models, range 11 to 147), 1.10 times the Python port's. 11,303 s of engine time for the 478.
- Math: MRI's `Math` calls glibc at EPA's symbol versions; what MRI adds (domain errors, `Math.sqrt(-0.0)` = +0.0, a Complex for a negative base) is undone. Checked on 17,300,528 math vectors, 0 differ; printf/strtod/sscanf 1 of 1,394,252 (`%#g` of 999999.5).

**Shared with every README of this family**
- Reference: EPA SWMM 5.2.4 from the USEPA v5.2.4 tag, built with gcc 13.3 `-O2`, on x86-64 Linux with glibc 2.39. Pass: `.out` byte-identical (when EPA writes one), `.rpt` identical but the lines "Analysis begun on", "Analysis ended on" and "Total elapsed time"; from the Kotlin port on, also the same exit code (EPA's command line always exits 0); when an input error stops EPA before it writes results, the engine must not write a results file either.
- Built by the same front end, `tools/c2x/front.py`, which parses EPA's 54 C files with libclang. When the port disagreed with EPA, "the fix went into the translator or the runtime, never into the generated file".
- "It is not a new engine": every number it writes is EPA 5.2.4's, "including the results of EPA's own defects".
- Not exercised by any gate model that runs without an input error: streets and inlets, climate files, USE HOTSTART, USE INFLOWS, USE RUNOFF. The stepping API is translated, but only the command line was gated.

**Feeds:** [SWMM5 language translations](../entities/swmm5-language-ports.md), [Byte-for-byte gate](../concepts/byte-for-byte-gate.md), [What the gate cannot see](../concepts/gate-blind-spots.md), [Matching glibc math in a translation](../concepts/glibc-math-in-translation.md), [Where languages part from C](../concepts/where-languages-part-from-c.md), [EPA SWMM 5](../entities/swmm-5.md), [1729-SWMM5-Models-2030 (the corpus)](../entities/corpus-1729.md).
