---
name: SWMM5 Implicit Box Solver Test Bench
file: swmm5-implicit-box-bench.html
version: 2026-10-02
date: 2026-10-30
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/9itk9v4KByziktaA1ogGRx", repo: "branch dev-pbox-implicit-wasm on a SWMMBob GitHub repository (the repository name is cut off in the text read)"}
engines:
  - {name: EPA SWMM 5.2.4 + pbox.c, note: "stock dynamic wave and an implicit Preissmann four-point box scheme in the same engine, compiled to WebAssembly, build 2026-10-02", license: "pbox.c and the page public domain; @bjorn3/browser_wasi_shim MIT or Apache-2.0; wasi-libc and LLVM compiler-rt linked"}
units: US customary (ft, cfs)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says the bench and the solver were built with Claude under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/9itk9v4KByziktaA1ogGRx, version 1793394709-117e (index.html, 1,245,158 bytes, SHA-256 49647033e35547648007808418b0ae28d5ede5312495f082bc39a43f45ce5a76), its page text read in headless Chromium on 2026-11-17 (the page has no About or Doc tab). No model was run to write this file."
---

# SWMM5 Implicit Box Solver Test Bench: stock dynamic wave against an implicit Preissmann box scheme in one engine

## In three points
- **What:** Runs one .inp twice in the browser: with stock EPA SWMM 5.2.4 dynamic wave and with an implicit Preissmann four-point box scheme (pbox.c) built into the same engine, the published method InfoWorks ICM's 1D engine is documented as using.
- **So what:** On 16 test models the implicit scheme's conduit peaks fall within 5.5% of stock, node peak depths within 9.8% and routing continuity within 0.11%, at 16 times stock's run time on the chain model at the same 5 s step.
- **Now what:** Use it to compare the two schemes on small networks you load. It is not InfoWorks code and will not reproduce InfoWorks numbers, and nothing bigger than 8 conduits has been run.

This summary was written after the fact. The page ships no technical summary and no Doc or About tab. The version above is its engine build date ("build 2026-10-02"); the date field is the artifact's publish date. The file name is ours. Every number below is copied from the page. No model was run to write this file.

## What it does

Choose one of sixteen built-in test models (chains at 5 s and 60 s steps, backwater, surcharge, flooding, steep 5% and flat 0.05% slopes, a pressurised box culvert, an open trapezoidal channel, runoff with storage, orifice, weir and pump, a split junction, a diamond, a braided network, a relief loop, a storage unit) or load your own DYNWAVE .inp. Options: time weighting theta (0.5 to 1), slot width, base depth and section spacing as fractions of the conduit. The implicit run uses the ROUTING_STEP as a fixed step and halves it only when Newton fails.

## Checks (as stated on the page)

- Off means stock: with the extension off, the .out is byte-identical to pristine EPA SWMM 5.2.4 on all 16 test models.
- The wasm engine is byte-identical to a native musl build of the same source on all 16 models, extension off and on; a glibc build on four models differs by at most 7e-7 ft and 3e-8 cfs.
- Against stock on the 16 models: conduit peaks within 5.5%, node peak depths within 9.8%, routing continuity within 0.11%, no step accepted unconverged.
- Cost: 16 times stock on the chain model (range 15.0 to 16.4 over seven interleaved pairs), 8.7 times on the pump model.
- Theta below 1 failed on two of the sixteen models.

## What this does not show

- No comparison with InfoWorks ICM and no field data; agreement with stock says the schemes solve the same equations, not that either is right.
- Test models have 3 to 8 conduits.
- Not modelled: flap gates, culvert inlet control, force-main equations (Manning is used), conduit seepage and evaporation, conduit flow limits.
- Every conduit keeps a base depth of 5% of its height; link flows and volumes are net of the base flow.

## How to reproduce

Open the page, pick a model, set the options and press Run both engines.

## Credits and licenses

EPA SWMM 5.2.4 (public domain); pbox.c and the page are public domain; @bjorn3/browser_wasi_shim (MIT or Apache-2.0); wasi-libc and LLVM compiler-rt. Third-party notices on the dev-pbox-implicit-wasm branch.

## AI use

The page says the bench and the solver were built with Claude, Anthropic's AI model, in a claude.ai session in October 2026, under the direction of Robert (Bob) Dickinson, who asked for the solver, chose to put it in SWMM 5.2.4 and is running the InfoWorks ICM comparison himself. Claude wrote pbox.c and its hooks into the engine, compiled the WebAssembly engine, wrote the sixteen test models and the page, and found and fixed the convergence faults. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- Engine build 2026-10-02: the version read.
