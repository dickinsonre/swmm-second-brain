---
title: SWMM6 language translations (swmm6-*)
type: entity
updated: 2026-11-14
sources: [S23, S24, S25, S26, S27, S28, S29, S30, S31, S32, S33, S34, S35]
tags: [swmm6, translation, verification]
reviewed: no
---
Thirteen public repositories under SWMMBobSWMM6, each a translation of the OpenSWMM 6 1D engine (HydroCouple/openswmm.engine, branch `swmm6_rel`, commit 88329d6) into one language, held to the same `.out` and `.rpt` as the C++ engine [S23](../sources/S23-swmm6-csharp-readme.md). Each README says it is "not SWMM6 and not a HydroCouple or EPA release; it is a translation checked against SWMM6" [S23](../sources/S23-swmm6-csharp-readme.md). How a model passes is on [Byte-for-byte gate](../concepts/byte-for-byte-gate.md).

**The chain.** The C++ was translated to C# first, by reading clang's AST of every engine source file (`tools/cpp2x`), and the C# gated to 480 of 480. Every other language except Rust is translated from that C#, not from the C++, by a Roslyn program in `tools/cs2x` [S23](../sources/S23-swmm6-csharp-readme.md). [swmm6-rust](swmm6-rust.md) is translated from the C++ directly and also covers 2D [S29](../sources/S29-swmm6-rust-readme.md). Some ports were begun from another port's translator: Kotlin and Groovy from Java's, JavaScript from TypeScript's, Ruby from Python's [S30](../sources/S30-swmm6-kotlin-readme.md) [S31](../sources/S31-swmm6-groovy-readme.md) [S32](../sources/S32-swmm6-javascript-readme.md) [S35](../sources/S35-swmm6-ruby-readme.md). Hy is the Python output re-spelled node by node and compiled back to check it [S34](../sources/S34-swmm6-hy-readme.md).

**Results as published** (corpus of 480, extra decks of 452; median seconds per model as each README gives it)

| Port | Corpus | Extra | Median s | Math | Source |
|---|---|---|---|---|---|
| C# | 480 | 452 | 0.76 | not stated | [S23](../sources/S23-swmm6-csharp-readme.md) |
| Go | 480 | 452 | 0.14 | translated glibc | [S24](../sources/S24-swmm6-go-readme.md) |
| Java | 480 | 452 | 1.92 | translated glibc | [S25](../sources/S25-swmm6-java-readme.md) |
| TypeScript | 480 | 452 | 2.02 | translated glibc | [S26](../sources/S26-swmm6-typescript-readme.md) |
| Fortran | 480 | 452 | 0.25 | not stated | [S27](../sources/S27-swmm6-fortran-readme.md) |
| Python | 412 of 413 run | 450 | 1.92 | system glibc | [S28](../sources/S28-swmm6-python-readme.md) |
| Kotlin | 480 | 452 | 2.96 | translated glibc | [S30](../sources/S30-swmm6-kotlin-readme.md) |
| Groovy | 480 | 452 | 3.04 | translated glibc | [S31](../sources/S31-swmm6-groovy-readme.md) |
| JavaScript | 480 | 452 | 1.33 | translated glibc | [S32](../sources/S32-swmm6-javascript-readme.md) |
| F# | 480 | 452 | 0.95 | system glibc (P/Invoke) | [S33](../sources/S33-swmm6-fsharp-readme.md) |
| Hy | 478 | 450 | 2.38 | system glibc (+ ctypes) | [S34](../sources/S34-swmm6-hy-readme.md) |
| Ruby | 478 | 450 | 2.89 | system glibc (+ Fiddle) | [S35](../sources/S35-swmm6-ruby-readme.md) |
| Rust | 480 | 452 | not given | not stated | [S29](../sources/S29-swmm6-rust-readme.md) |

No port reports a model that ran to the end and differed. Every shortfall in the table is a run that did not finish within its limit, counted as "untested, not failed" [S28](../sources/S28-swmm6-python-readme.md) [S34](../sources/S34-swmm6-hy-readme.md) [S35](../sources/S35-swmm6-ruby-readme.md). Python stopped by choice after 413 models; its 67 slowest were not run on that build [S28](../sources/S28-swmm6-python-readme.md). The same four decks stopped Hy and Ruby at 1,800 s: `SCANLON.inp`, `72_H&H_Elements(2).inp`, `legacy_small.inp`, `refactored_small.inp` [S34](../sources/S34-swmm6-hy-readme.md) [S35](../sources/S35-swmm6-ruby-readme.md).

**Checks beyond the first gate.** From Kotlin on, each port had an independent rerun from a clean copy, with the engine regenerated and compared byte for byte with the committed files: all 480 for Kotlin, Groovy, JavaScript and F#, a sample of 142 for Hy and Ruby. Then a second check from a clean clone on 48 corpus models and 12 extra decks [S30](../sources/S30-swmm6-kotlin-readme.md) [S33](../sources/S33-swmm6-fsharp-readme.md) [S34](../sources/S34-swmm6-hy-readme.md) [S35](../sources/S35-swmm6-ruby-readme.md).

**Licences.** The engine is OpenSWMM's, Apache 2.0; the translators, runtimes and gate are Bob's, Apache 2.0. Ports that carry translated glibc math keep that math under LGPL 2.1 or later [S24](../sources/S24-swmm6-go-readme.md) [S30](../sources/S30-swmm6-kotlin-readme.md).

**Not in the sources.** How long each port took to build, and what each cost. The speeds are medians on a shared two-core machine and "a rough guide, not a benchmark" [S23](../sources/S23-swmm6-csharp-readme.md).

See [Matching glibc math in a translation](../concepts/glibc-math-in-translation.md), [OpenSWMM 6 and HydroCouple](openswmm-6-and-hydrocouple.md), [1729-SWMM5-Models-2030 (the corpus)](corpus-1729.md).
