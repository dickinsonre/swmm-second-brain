---
name: SWMM5 Residual Walk
file: swmm5-residual-walk.html
version: "1.0"
date: 2026-11-04
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/9HVoefSo84J7RWJxZhBnXA", repo: none named in the page}
engines:
  - {name: EPA SWMM, version: 5.2.4, source: "tag v5.2.4, compiled to WebAssembly with clang 18 for wasm32-wasi, with a read-only trial trace added; the page checks its hash", license: public domain}
units: US customary (ft, cfs, in, s)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says the app, its engine build, tests and Doc were made with Claude under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/9HVoefSo84J7RWJxZhBnXA, version 1793828431-ed0a (index.html, 1,380,937 bytes, SHA-256 dfa99a992e89c7eafa541847b9f4fb5c771ec9e0100f5a83604d5f0638ad182d), its About and Doc tabs read in headless Chromium on 2026-11-17. No model was run to write this file; the date is the artifact's publish date."
---

# SWMM5 Residual Walk: four tests of the dynamic wave iteration on a real SWMM 5.2.4 engine

## In three points
- **What:** Turns two fractal pictures (a Cantor set and a walk whose steps halve) into four tests on EPA SWMM 5.2.4 running in the page: the walk of trials inside one time step, the cliff where a short outfall link breaks it, step-halving refinement, and a Cantor storm.
- **So what:** A chain of pipes holds 0.00% continuity until its last link at the outfall gets short: at 0.59 ft continuity is 3.2%, and at 0.073 ft it is -11,199% with 3,688 cfs out of an 8 cfs inflow, while SWMM5 runs to the end and returns no error.
- **Now what:** Screen models for very short links at free outfalls and halve the routing step to read off the limit. It tests a model's numerics, not whether a converged answer is true.

This summary was written after the fact. The page ships no technical summary of its own. Its version is the page's own ("v1.0"); the date is the artifact's. The file name above is ours. Every number below is copied from the page's About tab or its Doc essay. No model was run to write this file.

## What it does

Bob was asked whether fractal geometry has any use in SWMM or ICM modeling. No equation in either engine takes a fractal dimension. But every dynamic wave step in SWMM 5.2.4 is a walk of the second picture's kind: OMEGA = 0.5 at dynwave.c line 61, so each trial keeps half the old value and closes on its answer by about half per trial. Tabs: Walk (the guesses inside one time step), Cliff (the link length where SWMM5 falls apart, and a network number Lambda as a screen), Refine (halve the routing step and read off the limit, Q-infinity = Q + Delta-Q r/(1 - r)), Cantor Storm (how fine rain data must be), Verify, About, Doc. The page also corrects the source pictures: a countable union of segments has dimension 1, not 0, and the walk graphic's alpha-3 should be 1/8.

## Results the page reports

- The chain's null test passes through stage 8: last link 1.17 ft, outfall peak 7.96 cfs against 7.95 for the one pipe, continuity 0.00%, mean step 0.55 s.
- Stage 9, last link 0.59 ft: continuity 3.2%, outfall peak 16.9 cfs. Stage 12, 0.073 ft: continuity -11,199%, outfall 3,688 cfs from an 8 cfs inflow; no error is returned. Past the cliff the peak is noise and can fall (stage 10 reports 0.79 cfs).
- The ratio does not matter: the Cantor ratio holds at 1.23 ft and fails at 0.41 ft (continuity 94%); the ratio 1/4 holds at 1.17 ft and fails at 0.29 ft. A 300 ft tail after the short links hides the failure (stage 11 at 0.00%).
- Loop gain near critical flow is about (2/3) c dt/L; relaxed at omega = 1/2 the loop reaches r = 1 at a gain of 3, putting the failure at c dt/L = 4.5. A FIXED outfall moves the failure in: at a 0.4 ft last link continuity is -0.96% against 65.0% for FREE; the FIXED chain fails at 0.2 ft.
- Census: of 307 unique files from the 1729 corpus, 216 gave dynamic wave results for the screen and 158 ran the step-halving test (files, not independent systems).

## Checks (as stated on the page)

- The trace changes nothing: on 100 corpus models the traced build's .out matched the pristine native build byte for byte, 100 of 100.
- Browser against native: byte for byte on 89 of 100; the other 11 differ through math-library rounding; on 5 of them conduit flows differ, median changes up to 0.24%, largest 100% of peak at pump MANLAKES1 in manifold_pumps (a switch moved by a last-bit change). Past the cliff stage 12 reads -11,199% here and -9,283% native.
- Null controls: the same file twice gives the same bytes; setting omega = 0.5 by hand gives the same bytes; the chain matches its one pipe within 0.3% through the last good stage.
- Arithmetic: S_n plus what is left equals 2 l; D matches log 2 / log 3; the Cantor storm returns 1.00 in of rain at every stage.
- The checks are mechanical.

## What this does not show

- No field data or measured flows, and no claim that a walk that converges has converged on the truth.
- The omega figure on the Walk tab comes from a patched engine, for study only.
- No person has reviewed the Doc, checked the loop-gain derivation by hand, or tried the screen on a real pump station.

## How to reproduce

Open the page, pick a sample model or open an .inp, and use each tab; Verify checks the engine hash in the browser.

## Credits and licenses

EPA SWMM 5.2.4 source, tag v5.2.4 (public domain; line numbers refer to this tag). Rossman (2017), SWMM Reference Manual Volume II: Hydraulics, EPA/600/R-17/111. No license is stated for the page.

## AI use

The page says the app, its engine build, its tests and its Doc were made with Claude, Anthropic's AI model, in a working session in November 2026, under the direction of Robert (Bob) Dickinson, who supplied the graphics and the question and set the standing requirements. Claude read the SWMM 5.2.4 source, added the read-only trial trace, compiled the engine, wrote the page, generators, tests and census scripts, derived the linear loop model, and wrote the text. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 1.0: first version.
