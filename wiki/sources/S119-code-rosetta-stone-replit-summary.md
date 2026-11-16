---
title: "S119: SWMM5 Rosetta Stone, summary written by Replit Agent (v1.0.0)"
type: source
raw: raw/apps/code-rosetta-stone-v1.0.0.md
kind: app-md
author: Robert Dickinson
published: 2026-11-15
ingested: 2026-11-15
tags: [apps, replit, swmm5, swmm6, translation, engines, verification]
reviewed: 11/16/2026
---
**What it is.** A technical summary of SWMM5 Rosetta Stone, version 1.0.0: an app that shows SWMM and EPANET algorithm examples side by side in many programming languages and runs uploaded SWMM models through labelled numerical engines. It is one of Bob's Replit apps, at `code-rosetta-stone.replit.app`. Raw file: [raw/apps/code-rosetta-stone-v1.0.0.md](../../raw/apps/code-rosetta-stone-v1.0.0.md).

**How it was written. This one is different.** The app ships no summary of its own making. Replit Agent wrote the file on 15 November 2026 from the project's source, and the file says Bob has not yet reviewed it (Q74). Of the app itself it says Git history records Replit Agent as author of app integration and configuration changes, and that the imported translations document Claude in Claude Code as their writer under Bob's direction. The copy here was read out of the editor of the Replit project named Code Rosetta Stone on 15 November 2026 and matched a SHA-256 computed there (see the log).

**Claims worth keeping** (all copied from the file)
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

**Limits it states.** No full validation. No comparison with an original OpenSWMM build. No fresh rebuild of every toolchain; the tests use existing local build artifacts. The licenses of the imported SWMM5 translators beyond EPA's public-domain portions are not checked. The `date:` is the day of the summary, not a release date.

**Checked at ingest.** The app's 20 SWMM5 translations include C++ and Rust, for which this wiki holds no README, and leave out R, for which it does [S54](S54-swmm5-r-readme.md); Q48 already records that swmm5-r was found empty. The gate on [SWMM5 language translations (swmm5-*)](../entities/swmm5-language-ports.md) is 480 models; here it is 3. The app goes by Code Rosetta Stone elsewhere in this wiki [S47](S47-swmm5-php-readme.md); the file's own name is SWMM5 Rosetta Stone (Q77).

**Feeds:** [SWMM5 Rosetta Stone, also called Code Rosetta Stone (app)](../entities/code-rosetta-stone.md), [Replit apps: the second seventeen summaries](../concepts/replit-app-summaries-second-batch.md), [SWMM5 language translations (swmm5-*)](../entities/swmm5-language-ports.md), [SWMM6 language translations (swmm6-*)](../entities/swmm6-language-ports.md), [Byte-for-byte gate](../concepts/byte-for-byte-gate.md), [SWMM Engines, Byte for Byte (app)](../entities/swmm-engines-byte-for-byte.md), [SWMM Engine What If (app)](../entities/swmm-engine-what-if.md).
