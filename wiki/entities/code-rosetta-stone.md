---
title: "SWMM5 Rosetta Stone, also called Code Rosetta Stone (app)"
type: entity
updated: 2026-11-15
sources: [S47, S54, S119]
tags: [apps, replit, swmm5, swmm6, translation, engines, verification]
reviewed: no
---
Bob's Replit app SWMM5 Rosetta Stone: an app that shows SWMM and EPANET algorithm examples side by side in many programming languages and runs uploaded SWMM models through labelled numerical engines. Version 1.0.0, at `code-rosetta-stone.replit.app` [S119](../sources/S119-code-rosetta-stone-replit-summary.md).

**A caution about its source.** Everything on this page rests on [S119](../sources/S119-code-rosetta-stone-replit-summary.md), which Replit Agent wrote on 15 November 2026 from the project's source. Nothing here has been read by Bob (Q74).

**What the summary says** [S119](../sources/S119-code-rosetta-stone-replit-summary.md)
- 72 engine selections: 1 pinned EPA reference, 26 language adapters that call that same EPA solver, 30 imported independent translations, 1 limited Python subset and 14 concept entries.
- The EPA reference is 5.2.4 at commit `7952ca837988b1c32f791812eccc9fd64547e093`.
- The 30 imported translations are 20 of SWMM5 and 10 of OpenSWMM 6, each with its repository under SWMMBobSWMM6 and an exact commit in the front matter. 29 are configured to execute; OpenSWMM Groovy is source only because of compiler memory limits.
- The 20 SWMM5 translations: C++, C#, Fortran, Go, Java, Python, Rust, TypeScript, F#, Groovy, Hy, JavaScript, Kotlin, Lua, Mojo, Free Pascal, Perl, PHP, Ruby and Zig. The 10 of OpenSWMM 6.0.0-alpha.4 (1D): C#, Fortran, Go, Java, Python, Rust, TypeScript, JavaScript, Groovy and Kotlin.
- The run made for the summary produced 60 successful SWMM5 comparisons: all 20 SWMM5 translations on `sample.inp`, `user1.inp` and `python-storage.inp` matched the pinned EPA binary-output hash. The file calls these sampled checks, not exhaustive certification.
- OpenSWMM results were compared with translated peers, not with an original OpenSWMM reference build.
- Tests: the first run of `node --test tests/*.test.mjs` gave 147 passed and 7 failed, all seven being API cases answered with HTTP 502 before the server was ready. The API suite rerun gave 33 passed and 0 failed. The Python subset suite gave 12 passed and 0 failed.
- The comparison viewer holds 50 SWMM modules in 37 languages (1,850 code strings) and 25 EPANET modules (575 code strings). Displaying a translation does not run or validate it.
- An imported translation runs with no numerical fallback to EPA.
- The published site is a static deployment: `https://code-rosetta-stone.replit.app/api/engines` returned HTTP 404, so published simulation and chat are not demonstrated.
- The Python subset solves `dV/dt = rate + slope*t - decay*V` analytically, for storage and outlet inputs only.
- Chat calls Anthropic Claude. Repository: https://github.com/dickinsonre/Code-Rosetta-Stone. No project-wide app license is stated.

**What it does not show.** No full validation. No comparison with an original OpenSWMM build. No fresh rebuild of every toolchain; the tests use existing local build artifacts. The licenses of the imported SWMM5 translators beyond EPA's public-domain portions are not checked. The `date:` is the day of the summary, not a release date. [S119](../sources/S119-code-rosetta-stone-replit-summary.md)

**Noted at ingest.** The app's 20 SWMM5 translations include C++ and Rust, for which this wiki holds no README, and leave out R, for which it does [S54](../sources/S54-swmm5-r-readme.md); Q48 already records that swmm5-r was found empty. The gate on [SWMM5 language translations (swmm5-*)](swmm5-language-ports.md) is 480 models; here it is 3. The app goes by Code Rosetta Stone elsewhere in this wiki [S47](../sources/S47-swmm5-php-readme.md); the file's own name is SWMM5 Rosetta Stone (Q77).

See [Replit apps: the second seventeen summaries](../concepts/replit-app-summaries-second-batch.md), [SWMM5 language translations (swmm5-*)](swmm5-language-ports.md), [SWMM6 language translations (swmm6-*)](swmm6-language-ports.md), [Byte-for-byte gate](../concepts/byte-for-byte-gate.md), [SWMM Engines, Byte for Byte (app)](swmm-engines-byte-for-byte.md), [SWMM Engine What If (app)](swmm-engine-what-if.md).
