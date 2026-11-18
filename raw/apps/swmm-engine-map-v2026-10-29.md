---
name: SWMM Engine Map
file: swmm-engine-map.html
version: 2026-10-29
date: 2026-10-29
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/Xequ1gR8cKfcpD2LXrbhUs", repo: none named in the page}
engines:
  - {name: EPA SWMM, version: 5.2.4, role: "the fixed reference; built natively and as WebAssembly"}
  - {name: "swmm5-cplus, swmm5-rust and the translated ports", note: "three WebAssembly engines extracted from the swmm5-rust app and the TypeScript port bundled for the browser"}
units: none (counts, bytes, times)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says the site, its essay and the .docx were made with Claude (Claude Opus 5.5) under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/Xequ1gR8cKfcpD2LXrbhUs, version 1793318466-1416 (index.html, 1,777,018 bytes, SHA-256 0be0cf1c0e1fccace400cd06158ac824f9fa2e01650c97dd858f10634a4e7765), its About and Doc tabs read in headless Chromium on 2026-11-17. Nothing was run to write this file."
---

# SWMM Engine Map: the SWMM engines built and measured by SWMM Enablement, laid out the way hydrocouple.org lays out OpenSWMM 6

## In three points
- **What:** A hydrocouple.org-style site that maps the engines Bob's SWMM Enablement work has built or measured (C++, Rust, the translated ports), with EPA SWMM 5.2.4 as the fixed point, and runs four engines in the browser against EPA byte for byte.
- **So what:** EPA 5.2.4 keeps its state in 415 file- and program-scope variables, so it holds one model per process (a second swmm_open returns 0 and leaks 361,322 bytes in 134 allocations); the new engines exist to get around that and are gated on identical .out files.
- **Now what:** Use it as the front page for the engine work and to run the gates yourself. 781 large corpus models are not yet gated by C++ and Rust, the five translated ports are gated on 480 models, and SWMM6 is measured on one alpha commit.

This summary was written after the fact. The page ships no technical summary and no version number of its own, so the version above is its build date. The file name is the one Bob uses for it. Every number below is copied from the page. Nothing was run to write this file.

## What it does

The site follows hydrocouple.org's section order and palette with no HydroCouple logo, image or text reused, and changes five things after a review of that site: Engines and Benchmarks in the top bar with Run the engines highlighted; a hero button that runs four engines and compares each output byte for byte with the EPA build it should match; a real run's .out animated as the hero; a benchmark snapshot with gate results and timing beside their control and noise floor; and an engine map with the reference in the middle, plus a code view with five ways to call the same engine. Tabs include Home, Engines, Benchmarks, About, Doc and a code view (C, C++ and C ABI calls, the browser, the command line).

## The gate (as the page states it)

- The limit it works around: EPA 5.2.4 keeps its state in 415 file- and program-scope variables; opening a second model over the first returns 0 from swmm_open, empties the first report, and leaks 361,322 bytes in 134 allocations under AddressSanitizer.
- The .out file, which holds every reported value as 32-bit numbers, matches EPA's byte for byte.
- The .rpt matches byte for byte after removing the three wall-clock lines.
- No tolerance, because a last-bit difference in dynamic wave can change the iteration count at the next step.

## What this does not show

- Not a new or more accurate engine.
- 781 large corpus models not yet gated by C++ and Rust; the five translated ports gated on 480 models.
- TypeScript and Java match EPA on FMA/AVX2 processors.
- Timing on one two-core machine; SWMM6 measured on one alpha commit.

## How to reproduce

Press Run the engines on the home page; the Benchmarks section traces each number to a result file.

## Credits and licenses

EPA SWMM 5.2.4 (public domain). Layout ideas from hydrocouple.org (no content reused). The 1729-SWMM5-Models-2030 corpus. No license is stated for the page.

## AI use

The page says the site, its Doc essay and the .docx were made with Claude, Anthropic's AI model (Claude Opus 5.5), on 29 October 2026, under the direction of Robert (Bob) Dickinson, who chose the subject, asked for a HydroCouple-style map that answers the review of hydrocouple.org, and supplied the corpus and the engines. Claude read hydrocouple.org and its public source, wrote the page's code, copy and figures, extracted the three WebAssembly engines from the swmm5-rust app and checked their SHA-256 against that repository's manifest, bundled the TypeScript port with an in-memory file system, and built EPA 5.2.4 natively. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 2026-10-29: the version read.
