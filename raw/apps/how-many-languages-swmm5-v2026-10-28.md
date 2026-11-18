---
name: How Many Languages Can the SWMM5 Engine Live In?
file: how-many-languages-swmm5.html
version: "2026-10-28"
date: 2026-10-28
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/72uvQomSDrpo3UokrFrCii", repo: none named in the document}
engines:
  - {name: EPA SWMM, version: 5.2.4, source: tag v5.2.4 of USEPA/Stormwater-Management-Model, note: "built five ways: gcc -O2 with glibc, with FMA contraction, a null control, with musl, and as wasm32"}
  - {name: corpus, note: "440 unique models from six folders of SWMMBobSWMM6/1729-SWMM5-Models-2030"}
units: US customary (ft, cfs, gpm); SI models converted to US units by the document
ai_use: "This summary was written by Claude (Anthropic) from the published document. The document says Claude (Anthropic, Opus 5.5) did the work on 2026-10-28 and that Bob Dickinson has not yet reviewed the findings. See AI use."
written_from: "the Claude Docs document https://claude.ai/artifact/72uvQomSDrpo3UokrFrCii, revision 17, its one tab exported as HTML on 2026-11-18 (28,768 bytes, SHA-256 9f481b90bc168b0067e41f1e41495d0e63f808495160710e77e527e3762cfa1f), and the data of its one chart read from the document; read in full. Nothing was run to write this file."
---

# How Many Languages Can the SWMM5 Engine Live In? Which languages can host a byte-identical port of EPA SWMM 5.2.4, measured

## In three points
- **What:** A measured answer, dated 28 October 2026: about 28 languages can run the SWMM5 engine by calling the compiled C or loading Bob's wasm build, but only six can host a native port that matches a Linux build of EPA 5.2.4 byte for byte without extra work: C++, Rust, Fortran, C#, Python and PHP.
- **So what:** The limit is the math library and number formatter each language ships, not the language. Rebuilding EPA's own C with musl's math library in place of glibc's changed 55 of 440 corpus runs (12.5%) and moved one peak node depth from 20.56 to 23.21 ft; turning on fused multiply-add changed 107 of 440 (24.3%); both controls changed none.
- **Now what:** Fortran and C# are the document's next two ports; host the existing wasm from more languages; hold every port to a byte comparison of .out and .rpt on a corpus slice with a null control and a repeat control. Windows was not measured, and Bob has not reviewed the findings.

This summary was written after the fact. The document ships no technical summary of its own and gives no version number; the version above is its date. The file name is ours. Every number below is copied from the document. Nothing was run to write this file.

## What it does

A Claude Docs document, not an app. Sections: bottom line; what the EPA 5.2.4 source is made of; the byte-match traps, measured; a language-by-language matrix; ports and bindings that already exist; recommended next languages; what this does not show; sources; AI use.

## The source, counted (src/solver at tag v5.2.4)

54 .c and 21 .h files, 50,296 lines (30,795 non-blank, non-comment); about 1,017 function definitions; 114 globals in globals.h; about 165 file-scope statics; 57 struct typedefs and 51 enums; 19 function-pointer callback sites; one union (TInfil); 168 malloc-family calls; 172 binary I/O calls; 602 printf-family calls (%.3f used 123 times, %.2f 61); 453 math-library calls (pow 146, of which 48 are pow(x, 2/3) for Manning and 14 pow(x, 1.5) for weirs and orifices); 2 OpenMP regions in dynwave.c; 23 exported functions in swmm5.h. No goto, no setjmp/longjmp.

## Results the document reports

- Math library: sqrt matched glibc in all 13 libraries compared. The transcendental functions differ in the last bit on 1% of calls for Java's Math, 6% for JavaScript and 32% for Go. For pow(r, 2/3) over hydraulic radii from 0.000001 to 1,000 ft: JavaScript 9.8%, Java StrictMath 9.7%, Go 56%. Go's acos at 0.9999954 (xsect.c line 2047) is 21,016 ULP from glibc. The wasm build matched native musl bit for bit and differed from glibc on 2.9% of calls.
- Formatting %.3f: JavaScript toFixed rounds exact ties up (812.3125 prints 812.313; C prints 812.312); Java String.format and Ruby format round the shortest decimal string (543.4145 prints 543.415 in Java, 543.414 in C; 696.2685 prints 696.268 in Ruby, 696.269 in C); Free Pascal prints 0.00 for -0.001 where C prints -0.00. Go, Rust, Python, PHP, C#, Fortran and musl matched C on all 320,000 values.
- Fused multiply-add: Go 1.24 fuses a*b + c on arm64 (from the assembly listing, not run on arm64); on x86-64, 0 of 1,000,000 results differed. gcc -O2 -march=haswell put 340 vfmadd instructions into the engine; plain -O2 puts none.
- Two more traps: Free Pascal stores 2.0/3.0 as a 4-byte single unless compiled with -CF64; Linux builds of 5.2.4 abort on a relative input path (swmm5.c line 1593, a 260-byte InpDir buffer against POSIX realpath).
- Corpus runs (chart): same binary run twice 0 of 51 changed; null control (-march=haswell, FMA off) 0 of 440; wasm32 in Node against native musl 1 of 437; musl against glibc 55 of 440; FMA on against off 107 of 440.
- Largest moves when only the math library changed: Hydrology/SCANLON.inp node 09304006R0 20.56 to 23.21 ft and link 09204002C0 858.12 to 888.08 cfs; Hydraulics/vsp_pump_si_units.inp FIT2 25.85 to 29.20 ft; EPA/5_H&H_Elements.inp J012 4.02 to 5.16 ft.
- Of the 55 models that changed, 36% have pumps, 27% control rules and 44% weirs or orifices; of the 385 that did not, 11%, 7% and 13%.
- The one wasm-against-musl difference is undefined behavior in gage.c line 251: a one-entry time series overflows int. Native x86-64 C gives -2,147,483,648 with no warning; wasm, Rust and Java saturate to 2,147,483,647 and print WARNING 09; JavaScript gives -1,391,067,136; Python gives 864,000,000,000,000. The .out of Hydrology/Baisismodell_SI_Units.inp was identical; only the warning line differed.
- Existing native engines outside Bob's own C++ and Rust work: swmmrs and Hydra (Rust), OpenSWMM (C++20), jswmm (Java), noodl (Python with PyTorch). Only noodl publishes a step-by-step parity test against live 5.2.4. None found in Go, Julia, Kotlin, Swift, Dart, Haskell, OCaml or Lua.

## Checks

- Arithmetic we checked (ours): 55 / 440 = 12.5%; 107 / 440 = 24.3%; 23.21 - 20.56 = 2.65 ft, the move the bottom line quotes; 1 / 437 = 0.2%.
- The document states where each number was measured: in its sandbox on 2026-10-28, glibc 2.39, x86-64; "not measured" where no toolchain was present.

## What this does not show

As the document lists it: Windows (EPA's distributed build uses the Microsoft C runtime, not measured); Julia, Swift, Kotlin/Native, Dart, D and Nim (no toolchain, rows inferred); speed (nothing timed); the corpus slice (440 models, 57 slower than 12 s skipped, serial builds without OpenMP); microbenchmarks on random SWMM-like arguments; Go's FMA confirmed from assembly only; Chicory, wazero and wasmtime for .NET not run; a full port can still drift through operation order; existing ports described from their own pages (the swmmrs solver source is private).

## How to reproduce

Build EPA 5.2.4 from tag v5.2.4 with glibc, musl, -march=haswell with and without -ffp-contract=off, and wasm32; run the six corpus folders through each; byte-compare .out and .rpt minus the three timestamp lines.

## Credits and licenses

EPA SWMM 5.2.4 (public domain); the 1729-SWMM5-Models-2030 corpus; the existing ports named above and their authors (Issac Gardner's swmm-js, NEER's Hydra, GEOframe's jswmm, Imperial College's noodl, CIMM's SWMM5+, MatSWMM, swmmr, swmm5.net); CORE-MATH, c2rust, ccgo, cxgo, Hebron, Emscripten, Chicory, wasmtime-py. No license is stated for the document.

## AI use

The document says: Claude (Anthropic, Opus 5.5) did this work on 2026-10-28; it wrote and ran every test harness, built the five engine variants (glibc, FMA, null control, musl, wasm32), ran the corpus comparisons and drafted all text; a Claude research sub-agent compiled the existing-ports inventory; Bob Dickinson asked the question and has not yet reviewed the findings. The Netlify copy adds a line that it was exported from the Docs document on 18 November 2026 and that its one chart was redrawn from the document's own numbers. This summary was written by Claude on 18 November 2026 from the exported document.

## Changes

- 2026-10-28: the version read (the document's date; it carries no version number).
