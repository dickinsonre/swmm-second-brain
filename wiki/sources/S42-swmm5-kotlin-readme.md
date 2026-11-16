---
title: "S42: swmm5-kotlin, EPA SWMM 5.2.4 in Kotlin (README)"
type: source
raw: raw/ports/2026-11-08-swmm5-kotlin-README.md
kind: repo-readme
author: Robert Dickinson
published: 2026-11-08
ingested: 2026-11-14
tags: [swmm5, translation, verification]
drafted_by: Claude (Anthropic), in Claude Code, at Bob's direction
reviewed: 2026-11-15
---
**What it is.** The README of the public repository SWMMBobSWMM6/swmm5-kotlin, as published on 2026-11-08: EPA SWMM 5.2.4 in Kotlin, "written by a translator that reads EPA's C, and judged against EPA itself". Raw file: [raw/ports/2026-11-08-swmm5-kotlin-README.md](../../raw/ports/2026-11-08-swmm5-kotlin-README.md).

**How it was written.** By Claude (Anthropic's AI model, Claude Opus 5.5) in Claude Code on 6 November 2026, for Bob, who chose the language for his Code Rosetta Stone app and set the byte-for-byte standard, as the README says. "Claude ran every gate and check reported here. The checks are mechanical; no person has yet reviewed the code."

**Claims worth keeping**
- Result: 480 of 480 identical (gate run `kt_1`, 6 November 2026), 397 s of engine time for the 480. Median CPU time 1.31 to 2.63 times EPA's on six longer models, Java 1.26 to 2.06 in the same interleaved runs.
- Toolchain: Kotlin 2.0.21 bundled with Gradle 8.14.3. The sandbox refused Maven Central, and running a compiler downloaded from npm was refused as code from outside; the compiler already installed with Gradle was neither.
- `emit_kotlin.py` writes 37,246 lines and reuses the Java back end's analysis. Kotlin needed every C conversion written out, infix bitwise operators, `!!` on every dereference, C `for` as `while`, `switch` as `when` with fall-through written out, and nested C blocks flattened (a bare `{ }` is a lambda).
- Math: `Glibm.kt` (4,944 lines) from the Kotlin back end of `gim2x.py`; checked on 11,000,672 random arguments and 3,300,000 edge cases, 0 differences. Adding the back end left the Go, Java and TypeScript outputs byte-identical.
- One corpus model, `Hydrology/sewer_rdii_problem.inp`, allocates 3.38 GB of RDII rainfall history, as EPA does; the launcher gives the JVM three quarters of memory.

**Shared with every README of this family**
- Reference: EPA SWMM 5.2.4 from the USEPA v5.2.4 tag, built with gcc 13.3 `-O2`, on x86-64 Linux with glibc 2.39. Pass: `.out` byte-identical (when EPA writes one), `.rpt` identical but the lines "Analysis begun on", "Analysis ended on" and "Total elapsed time"; from the Kotlin port on, also the same exit code (EPA's command line always exits 0); when an input error stops EPA before it writes results, the engine must not write a results file either.
- Built by the same front end, `tools/c2x/front.py`, which parses EPA's 54 C files with libclang. When the port disagreed with EPA, "the fix went into the translator or the runtime, never into the generated file".
- "It is not a new engine": every number it writes is EPA 5.2.4's, "including the results of EPA's own defects".
- Not exercised by any gate model that runs without an input error: streets and inlets, climate files, USE HOTSTART, USE INFLOWS, USE RUNOFF. The stepping API is translated, but only the command line was gated.

**Feeds:** [SWMM5 language translations](../entities/swmm5-language-ports.md), [Byte-for-byte gate](../concepts/byte-for-byte-gate.md), [What the gate cannot see](../concepts/gate-blind-spots.md), [Matching glibc math in a translation](../concepts/glibc-math-in-translation.md), [Where languages part from C](../concepts/where-languages-part-from-c.md), [EPA SWMM 5](../entities/swmm-5.md), [1729-SWMM5-Models-2030 (the corpus)](../entities/corpus-1729.md).
