---
name: swmm5-rust
file: swmm5-rust.html
version: 1.0.1
date: 2026-11-22
author: Robert Dickinson
written_from: the published swmm5-rust page (Claude artifact version 1793295967-a398, page built 2026-10-29), its Verify, Inside and About tabs and its Doc essay; nothing was rerun for this file
links: {netlify: none yet, artifact: see the published Claude artifact, repo: not named on the page}
engines:
  - {name: EPA SWMM, version: 5.2.4, source: "USEPA/Stormwater-Management-Model tag v5.2.4", license: public domain, wasm_sha256: 56d9191b3f906691c58f3663e41eabf99e3ca8853691e33bdbb6f9e42e192eae}
  - {name: swmm5-cplus, version: "the C++ restructuring of EPA 5.2.4", source: "SWMMBobSWMM6/swmm5-cplus", wasm_sha256: a16d08e75b9c3febeeaee8791cb4a93f33a71ad33ba239aa1c5cf165da18a82d}
  - {name: swmm5-rust, version: "engine commit d37bbc5d9da33243ddbe789d182c1c758fccea1f; page built from commit 7cb779e87efea2a754acda8811064a029bac16fd", license: not stated on the page, wasm_sha256: da181e90221d6359681dfe857620096d55d0b20feccb482d643771428e5595dd}
units: the model's own (FLOW_UNITS); ten of the eleven samples are CFS and ft, one is GPM
ai_use: built with Claude (Anthropic); this summary written by Claude from the page; see AI use
---

# swmm5-rust: EPA SWMM 5.2.4 in safe Rust, byte-identical to EPA wherever EPA's behavior is defined

This file was written from the published page on 22 November 2026. Nothing was rerun to write it; every number below is copied from the page.

## In three points

- **What:** EPA SWMM 5.2.4 translated into safe Rust, 56,001 lines in 63 files with no unsafe code in the engine, and an app that runs it beside EPA's C and swmm5-cplus in the browser and compares the bytes.
- **So what:** It matches EPA's .out byte for byte, and the .rpt after three wall-clock lines are removed, on 215 of 215 defined smoke and coverage models and 3,742 of 3,759 corpus models (15 undefined in C, 2 inconclusive, 0 different). Where EPA's C reads or writes memory it does not own, the Rust stops and names the line instead of computing from the wrong memory.
- **Now what:** Use it where a report must not rest on numbers read from the wrong memory; the essay's case is reports that go into permits, bond issues and flood maps. It is not more accurate (EPA's defects RS-1 to RS-4 are kept on purpose) and not faster (native median 1.12 times EPA's run time), and no person has read the translation line by line.

## What it does

swmm5-rust is EPA SWMM 5.2.4 written again in safe Rust. The crate carries `#![forbid(unsafe_code)]`, so the compiler checks every array index and reference. The goal was to change nothing: not the physics, not the order of the arithmetic, not the wording of a warning, not the last bit of a number in the .out file. The app runs three engines compiled to WebAssembly in a background worker (EPA 5.2.4 C, swmm5-cplus C++, swmm5-rust) on a sample or any .inp, and compares the .out files by SHA-256 and value by value, and the .rpt files number by number. Its Many at once tab opens every sample in one swmm5-rust instance, one handle each. Its Doc tab is the essay *Every Byte Accounted For*.

## How it computes

- Source: 54 C files of EPA 5.2.4, 46,467 lines (50,788 with headers).
- Reference translation: c2rust 0.22.1 over the same source gives 71,226 lines in which all 978 functions are unsafe and 632 globals and statics are `static mut`. It never ships. It is a second copy of EPA that compiles into the same program as the safe engine.
- Lockstep tool: steps the c2rust copy and the safe engine side by side and compares every node, link and subcatchment state after every routing step; the first variable whose bits differ names the function.
- Safe engine: a skeleton with one `Project` that owns the model, then the 54 modules translated in ten parallel batches from one rule book (TRANSLATING.md). Rules: same functions, names, statements and order; arithmetic bit for bit (`a*b*c` is `(a*b)*c`; no `x*0.5` for `x/2.0`); strings as bytes; no globals.
- `Project`: 166 fields, 114 of them EPA's globals and 52 module states holding every file-scope static. Every function that touches the model takes it as `prj`.
- C constructs: a pointer that may be NULL becomes an `Option`; a malloc'd array a `Vec`; a callback with `void*` a closure (8); a linked list a vector in the order C walks it, with 7 places where C prepends.
- ccast: 62 float-to-integer conversions give the x86 answer on purpose. Rust's `as` clamps an out-of-range value; x86 gives -2,147,483,648. gage.c line 251 converts about 8.6e14 for any one-point rain series, and the difference decides whether WARNING 09 is written.
- cio: printf, strtod, atoi and sscanf rewritten in safe Rust and compared with glibc on about 11 million inputs.
- FILLED_CIRCULAR: C edits the link's own yFull and aFull as it reads them, and the add-then-subtract round trip can leave either one bit low. Every conduit cross-section query goes through a getter that copies the section, asks, and writes the copy back, so the bit is lost exactly where EPA loses it.
- Undefined C: where C reads past an array, the Rust stops and names the line; on the two CRASH-08 decks it writes the error report; in the cross-section table lookup an out-of-range read gives 0.0 (RS-10).
- C interface: 269 lines with 7 small unsafe blocks where pointers come in from the caller, the only unsafe code in the engine and its interface.
- Browser: MemWasi, an in-memory file system of about 150 lines, answers the 19 WASI calls the engines use (the C engines need 13; Rust's standard library 6 more).

## Inputs and outputs

- Reads any SWMM 5.2.4 .inp plus the data files it names (rain, inflow, hot start). Eleven samples are built in: exam79, extran1_egg, extran1_irregular, controlExample, small_pump_fm_model (GPM), siphon_larger_SW5, transect_example, filled_circ_drift (RS-3), storage_order_A and storage_order_B (RS-1), lid_error_message (RS-2).
- Writes .rpt and .out in EPA's formats. Saves a series CSV, a statistics CSV, a report comparison CSV and a .zip of all three engines' .out and .rpt files.

## Checks

From the page's Verify tab and Doc essay. The gate builds EPA from the v5.2.4 tag with GCC 13.3 at -O2 and swmm5-rust with Rust 1.97 at opt-level 2, on x86-64 Linux, and compares the .out byte for byte and the .rpt byte for byte after removing the three wall-clock lines.

| Check | Result |
|---|---|
| Smoke and coverage set, native | 221 models: 215 identical, 6 undefined in C, 0 different |
| Corpus models with FILLED_CIRCULAR conduits, native | 68 of 68 identical |
| Corpus set (1729-SWMM5-Models-2030), native | 3,759 models: 3,742 identical, 15 undefined in C, 2 inconclusive, 0 different |
| After the control-rule velocity change | 415 models rerun: 409 identical, 6 undefined in C, 0 different |
| Long rerun of runs that hit the five-minute cap | 16 models, one hour each: 15 finished, 15 identical; Session38_100_Control_Rules.inp inconclusive (first 2,147,483,648 bytes of both .out files identical) |
| WebAssembly, in node | 215 of 215 defined models identical to EPA's WebAssembly build |
| Platform control: EPA native against EPA WebAssembly | 194 of 215 agree; the 21 that do not are listed on the Verify tab |
| c2rust translation control | 221 of 221 identical once its casts went through ccast; before that 12 reports differed by one line |
| Positive control, before the FILLED_CIRCULAR fix | 13 of 7,848 .out values differed (largest 3.8e-06) and one time of maximum depth read 01:04 against EPA's 01:06 |
| Lockstep on the engine before that fix | stops at routing step 29, conduit C0, new depth, last bit |
| Null control | each engine run twice writes the same bytes |
| Section-order control (RS-1 network) | all three engines agree with EPA on each order; the orders disagree as EPA does |
| Undefined-behavior control, six decks in four builds | EPA's answer changes with the platform on 3; swmm5-rust's on none |

Inconclusive: IO-02_end-time-1e30.inp (END_TIME 1e30 hours, the run would last 4.2e28 days; not rerun) and Session38_100_Control_Rules.inp (stopped at the 2 GiB file cap after 87 minutes for EPA and 100 for the Rust).

Timing, interleaved EPA, C++, Rust, EPA, with the second EPA run as the noise floor:

| Build | Median run time against EPA | Notes |
|---|---|---|
| swmm5-rust, native, 12 models | 1.12 | model by model 0.98 to 1.42; slower beyond the noise on 10 of 12 |
| swmm5-cplus, native (-O2 -flto) | 0.94 | |
| swmm5-rust, WebAssembly in node | 1.36 | slower beyond the noise on all 12 |
| swmm5-cplus, WebAssembly | 0.99 | |

Instruction counts (callgrind) on four models: swmm5-rust executes 11 to 26 percent more instructions than EPA; on manifold_pumps.inp 8.87 billion against 7.23 billion. 204 of the 215 engine functions both builds keep are called exactly as often. The table `lookup()` is called 22,640,867 times in both and costs 62.1 instructions a call against EPA's 35.5; eleven of the 26.6 extra are the x86-exact cast. On 10_Subs_Continuous.inp the output writer makes 2,182,316 calls to malloc against EPA's 6,834.

Human review: none. The translation has not been read line by line against the C by a person.

## Defect register (EPA 5.2.4, as found by the translation)

| ID | Where | What | Status in swmm5-rust |
|---|---|---|---|
| RS-1 | node.c lines 923-925 | storage_getVolDiff() passes a storage index where a node index belongs; with section orders swapped, S2 peaks at 9.82 ft or 10.43 ft (also NUM-55 in the OpenSWMM 2026 code review) | reproduced |
| RS-2 | report.c line 1433; lid.c | LID parameter errors print the message template instead of the LID name | reproduced |
| RS-3 | xsect.c, filled_circ_* | FILLED_CIRCULAR geometry edits the link's full depth and area as it reads them | reproduced |
| RS-4 | gage.c line 251 and 61 other conversions | out-of-range float-to-int conversion is undefined in C (also CRASH-21) | x86 behavior reproduced |
| RS-5 | rdii.c line 1062 | IO-23: unit hydrograph group with no rain gage reads Gage[0] of an empty array | Rust stops; C reads on |
| RS-6 | link.c line 190 | CRASH-02: an [XSECTIONS] row before its link's row writes past the Conduit array | Rust stops; C writes on |
| RS-7 | table.c line 382 | CRASH-03: a curve with no points is dereferenced through a NULL cursor | Rust stops; C crashes natively |
| RS-8 | project.c line 227 | CRASH-04: a quoted "Shape" leaves the Shape array empty | Rust stops; C aborts |
| RS-9 | controls.c line 313 | CRASH-08: controls_delete() walks a NULL Expression array after an early input error | Rust writes the error report |
| RS-10 | xsect.c line 1488 (and 1441, 1651) | CRASH-07: a NaN or overflowing ratio indexes a cross-section table far outside its bounds | Rust reads 0.0; C crashes natively |

## What this does not show

1. Not a new engine and not more accurate: every number is EPA 5.2.4's, defects included; RS-1 to RS-4 are reproduced on purpose.
2. It does not reproduce EPA where EPA's behavior is undefined (RS-5 to RS-10).
3. It does not run out of memory the way EPA does: where C reports ERROR 101, the Rust stops with "memory allocation failed" and writes no report. One corpus model asks both engines for 3.4 GB of RDII rainfall history.
4. Safe Rust rules out memory errors, not wrong arithmetic; the arithmetic is checked only by the gate, on the models the gate ran.
5. Not faster than the C: native median 1.12 times EPA's run time, WebAssembly 1.36.
6. EPA's own C differs native against WebAssembly on 21 of 215 models; which library functions cause it was not traced.
7. No person has reviewed the translation line by line.
8. This summary was written from the page. It was not checked against the engine's repository, and the page does not name that repository or a license.

## How to reproduce

- In the browser: the Run tab runs any sample or .inp through all three engines and repeats the per-model comparison; the Inside tab reruns the RS-1 section-order test and the six memory-error decks live.
- The page names the tools behind the native numbers (the gate, the lockstep tool, the cio tests against glibc, callgrind) and result files (results/lockstep_samples.log, results/lookup_disasm.txt, tests/models/filled_circ_control.inp, tests/models/lid_error_message.inp), but not the repository that holds them.
- Corpus: SWMMBobSWMM6/1729-SWMM5-Models-2030.

## Credits and licenses

- EPA SWMM 5.2.4: U.S. EPA, public domain; engine design by Lewis Rossman.
- swmm5-cplus: Robert Dickinson; the C++ engine on the page.
- swmm5-rust: Robert Dickinson. The page states no license.
- The OpenSWMM 2026 code review, whose decks and findings (NUM-55, IO-23, CRASH-02 to CRASH-08, CRASH-21) are in the gate.
- c2rust 0.22.1 (immunant); Rust 1.91 and 1.97; GCC 13.3; Clang 18 with wasi-libc; valgrind (callgrind).
- Fonts: Archivo, IBM Plex Sans and Mono, Source Serif 4, from Google Fonts.

## AI use

The engine, the app and its essay were built with Claude, Anthropic's AI model (Claude Opus 5.5), on 28 and 29 October 2026, at the request of Robert (Bob) Dickinson, who chose safe Rust with byte identity as the goal and supplied the model corpus. Claude ran c2rust and wrote the passes over its output, the skeleton and the rule book, ran the ten translation batches as separate agents and integrated them, wrote ccast, cio and their glibc tests, found and fixed the FILLED_CIRCULAR drift, and built the WebAssembly engine, the gates, the app, its figures and the essay. The checking was done by the gate, not by the AI's judgment. This summary was written by Claude on 22 November 2026 from the published page, because the app shipped without one; Bob has not yet read it.

## Changes

- 1.0.1 (2026-11-22): this technical summary, embedded in the page and linked from the head and the About tab. Nothing that computes changed.
- 1.0 (2026-10-29): first release.
