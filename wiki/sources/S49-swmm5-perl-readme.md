---
title: "S49: swmm5-perl, EPA SWMM 5.2.4 in Perl (README)"
type: source
raw: raw/ports/2026-11-09-swmm5-perl-README.md
kind: repo-readme
author: Robert Dickinson
published: 2026-11-09
ingested: 2026-11-14
tags: [swmm5, translation, verification]
reviewed: 2026-11-15
---
**What it is.** The README of the public repository SWMMBobSWMM6/swmm5-perl, as published on 2026-11-09: EPA SWMM 5.2.4 in Perl, "written by a translator that reads EPA's C, and judged against EPA itself". Raw file: [raw/ports/2026-11-09-swmm5-perl-README.md](../../raw/ports/2026-11-09-swmm5-perl-README.md).

**How it was written.** By Claude (Anthropic's AI model, Claude Opus 5.5) in Claude Code on 8 and 9 November 2026, for Bob, who chose the language for his Code Rosetta Stone app and set the byte-for-byte standard, as the README says. "Claude ran every gate and check reported here. The checks are mechanical; no person has yet reviewed the code."

**Claims worth keeping**
- Result: 478 of 480 ran and all 478 are identical; 72_H&H_Elements(2).inp and SCANLON.inp not run (stopped at 1,800 s). An independent rerun from a clean checkout gave the same.
- Speed: median 146 times EPA's (101 models, range 17 to 291); 10.3 times PHP's; 2.1 times Ruby's. 23,845 s of engine time for the 478.
- Perl adds, subtracts and multiplies whole-number doubles as 64-bit integers, so `0.0 * -3.0` is +0.0 in Perl and -0.0 in C; such operations are written `((A * B) || rt_zm(A, B))`. About 11 % of one model's time is in these zero-sign helpers.
- `**` calls glibc's `pow` except when both operands are whole numbers; `(-214.0) ** 8.0` differs from glibc's in the last bit. Division by zero dies, for doubles too.
- What the two stopped models wrote matched EPA as far as it went: SCANLON the first 36,364,288 bytes of its 78,975,850-byte `.out`.
- Beyond 2**53 a chain of Perl integer operations keeps bits C rounds away; "Nothing in the engine prevents that".

**Shared with every README of this family**
- Reference: EPA SWMM 5.2.4 from the USEPA v5.2.4 tag, built with gcc 13.3 `-O2`, on x86-64 Linux with glibc 2.39. Pass: `.out` byte-identical (when EPA writes one), `.rpt` identical but the lines "Analysis begun on", "Analysis ended on" and "Total elapsed time"; from the Kotlin port on, also the same exit code (EPA's command line always exits 0); when an input error stops EPA before it writes results, the engine must not write a results file either.
- Built by the same front end, `tools/c2x/front.py`, which parses EPA's 54 C files with libclang. When the port disagreed with EPA, "the fix went into the translator or the runtime, never into the generated file".
- "It is not a new engine": every number it writes is EPA 5.2.4's, "including the results of EPA's own defects".
- Not exercised by any gate model that runs without an input error: streets and inlets, climate files, USE HOTSTART, USE INFLOWS, USE RUNOFF. The stepping API is translated, but only the command line was gated.

**Feeds:** [SWMM5 language translations](../entities/swmm5-language-ports.md), [Byte-for-byte gate](../concepts/byte-for-byte-gate.md), [What the gate cannot see](../concepts/gate-blind-spots.md), [Matching glibc math in a translation](../concepts/glibc-math-in-translation.md), [Where languages part from C](../concepts/where-languages-part-from-c.md), [EPA SWMM 5](../entities/swmm-5.md), [1729-SWMM5-Models-2030 (the corpus)](../entities/corpus-1729.md).
