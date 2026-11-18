---
title: SWMM5 language translations (swmm5-*)
type: entity
updated: 2026-11-17
sources: [S36, S37, S38, S39, S40, S41, S42, S43, S44, S45, S46, S47, S48, S49, S50, S51, S52, S53, S54, S70, S71, S119, S204, S220, S221]
tags: [swmm5, translation, verification]
reviewed: 11/16/2026
changed_after_review: "2026-11-17 (S204 ingest): one paragraph added at the end on swmm5-ruby and the two-pipe benchmark (S204); 2026-11-17 (S205 to S223 ingest): a paragraph added near the end, headed Added 17 November 2026 (S220, S221)"
---
Nineteen public repositories under SWMMBobSWMM6, each EPA SWMM 5.2.4 "written by a translator that reads EPA's C, and judged against EPA itself" on 480 models [S41](../sources/S41-swmm5-go-readme.md). They are the languages of Bob's Code Rosetta Stone app [S47](../sources/S47-swmm5-php-readme.md). How a model passes is on [Byte-for-byte gate](../concepts/byte-for-byte-gate.md).

**How they were made.** One front end, `tools/c2x/front.py`, parses EPA's 54 C files with libclang and classifies all 2,083 pointer and array declarations. One back end per language writes the engine; a hand-written runtime supplies the C library pieces [S41](../sources/S41-swmm5-go-readme.md). Later back ends were built on earlier ones: Kotlin and Groovy on Java's analysis, Ruby, PHP, Perl and R on Python's, Free Pascal and Mojo on Zig's, JavaScript as a subclass of TypeScript's, F# on C#'s, and Hy re-spells the Python output node by node [S42](../sources/S42-swmm5-kotlin-readme.md) [S43](../sources/S43-swmm5-pascal-readme.md) [S46](../sources/S46-swmm5-javascript-readme.md) [S52](../sources/S52-swmm5-hy-readme.md) [S53](../sources/S53-swmm5-mojo-readme.md) [S54](../sources/S54-swmm5-r-readme.md).

**Results as published**

| Port | Result on 480 | Speed as stated | Source |
|---|---|---|---|
| Fortran, C#, TypeScript, Java, Go | 480 | 1.26, 5.19, 19.24, 9.18, 1.72 times EPA (median CPU, 12 models, interleaved) | [S36](../sources/S36-swmm5-fortran-readme.md) [S37](../sources/S37-swmm5-csharp-readme.md) [S39](../sources/S39-swmm5-typescript-readme.md) [S40](../sources/S40-swmm5-java-readme.md) [S41](../sources/S41-swmm5-go-readme.md) |
| Python | 465 (451 fast, 14 of 29 slow sampled) | 81.63 times EPA (same method) | [S38](../sources/S38-swmm5-python-readme.md) |
| Kotlin | 480 | 1.31 to 2.63 times EPA (six longer models) | [S42](../sources/S42-swmm5-kotlin-readme.md) |
| Free Pascal, Zig | 480 | 204 s and 138 s for the 480; no ratio claimed | [S43](../sources/S43-swmm5-pascal-readme.md) [S44](../sources/S44-swmm5-zig-readme.md) |
| Ruby | 478, 2 not run | median 70 times EPA | [S45](../sources/S45-swmm5-ruby-readme.md) |
| JavaScript | 480 | 1,737 s for the 480 | [S46](../sources/S46-swmm5-javascript-readme.md) |
| PHP | 480 | median 13.9 times EPA | [S47](../sources/S47-swmm5-php-readme.md) |
| F# | 480 | 372 s for the 480 | [S48](../sources/S48-swmm5-fsharp-readme.md) |
| Perl | 478, 2 not run | median 146 times EPA | [S49](../sources/S49-swmm5-perl-readme.md) |
| Groovy | 480 | 1,114 s for the 480 | [S50](../sources/S50-swmm5-groovy-readme.md) |
| Lua | 480 | 6,807 s for the 480 | [S51](../sources/S51-swmm5-lua-readme.md) |
| Hy | 480 (one given 4,475 s on its own) | median 56 times EPA | [S52](../sources/S52-swmm5-hy-readme.md) |
| Mojo | 480 | median 0.73 times EPA | [S53](../sources/S53-swmm5-mojo-readme.md) |
| R | 465, 15 not run | about 400 times EPA | [S54](../sources/S54-swmm5-r-readme.md) |

No port reports a model that ran to the end and differed from EPA. Every shortfall is a model stopped at the 1,800 s limit, counted as not run [S54](../sources/S54-swmm5-r-readme.md). The two that stop the slow ports are `SCANLON.inp` and `72_H&H_Elements(2).inp`, the models EPA itself takes longest on (34.8 s and 38.6 s) [S45](../sources/S45-swmm5-ruby-readme.md). EPA's reference run took 256 s for all 480 [S43](../sources/S43-swmm5-pascal-readme.md).

The speeds were measured three different ways (interleaved CPU benchmarks, the gate's clock on a shared machine, ratios to another port's stored times), so the column does not compare across rows. Several READMEs say no interleaved benchmark was run [S43](../sources/S43-swmm5-pascal-readme.md) [S48](../sources/S48-swmm5-fsharp-readme.md).

**A later re-run of all of them but R.** On 12 November 2026 twenty translations (the eighteen here other than R, with swmm5-cplus and swmm5-rust) were rebuilt on one machine, gated again and timed by one benchmark [S70](../sources/S70-swmm-engine-what-if-app-md.md). See [SWMM5 translations: the re-run of 12 November 2026](../concepts/swmm5-ports-rerun-2026-11.md). Stored results for eight of them are in [SWMM Engines, Byte for Byte (app)](swmm-engines-byte-for-byte.md) [S71](../sources/S71-swmm-engines-byte-for-byte-summary.md).

**Rechecks.** From Ruby on, the main session checked each port from a clean clone on 48 models drawn with seed 20261109 [S45](../sources/S45-swmm5-ruby-readme.md). From JavaScript on, each port also had an independent rerun from a clean checkout with the engine regenerated (a sample for R) [S46](../sources/S46-swmm5-javascript-readme.md) [S47](../sources/S47-swmm5-php-readme.md) [S54](../sources/S54-swmm5-r-readme.md).

**Two more engines in the same gate table**: swmm5-cplus and swmm5-rust, 480 of 480 each [S41](../sources/S41-swmm5-go-readme.md). They are not among the 19 sources here.

**Credit and licence.** "Its engine is Lewis Rossman's design, and this port keeps every algorithm as he wrote it." EPA SWMM is public domain; no licence has been chosen yet for the translators and runtimes; translated glibc math stays LGPL 2.1 or later [S41](../sources/S41-swmm5-go-readme.md).

**Added 15 November 2026: the app that runs them.** [SWMM5 Rosetta Stone, also called Code Rosetta Stone (app)](code-rosetta-stone.md) imports 20 SWMM5 translations at exact commits; all 20 matched the pinned EPA 5.2.4 binary-output hash on 3 models, a sampled check beside the 480-model gate above [S119](../sources/S119-code-rosetta-stone-replit-summary.md). Its 20 include C++ and Rust and leave out R (Q48). Replit Agent wrote that summary; Bob has not read it (Q74).

**Added 17 November 2026.** Two apps on the Rust translations. [swmm5-rs Side by Side (app)](swmm5-rs-side-by-side.md) compares 5.2.4's C with a c2rust translation on 113 models: 91 of 91 .out files identical, 25 reports differing by one warning traced to gage.c:251 [S220](../sources/S220-swmm5-rs-side-by-side-summary.md). [swmm5-rust in RustGIS (app)](swmm5-rust-rustgis.md) runs the safe-Rust swmm5-rust as a RustGIS plugin with no file system: 177 of 177 models byte-identical to EPA's WebAssembly build [S221](../sources/S221-swmm5-rust-rustgis-summary.md).

See [What the gate cannot see](../concepts/gate-blind-spots.md), [Where languages part from C](../concepts/where-languages-part-from-c.md), [SWMM6 language translations](swmm6-language-ports.md).

**Added 17 November 2026.** swmm5-ruby passed one more model outside the gate set, the two-pipe benchmark, at a fixed 1 s step and at EPA's default 20 s variable step: `.out` byte-identical and `.rpt` identical apart from the three time lines, under Ruby 3.3.6 at commit 0c97906 [S204](../sources/S204-note-two-pipe-benchmark-step1-run.md).
