---
title: "SWMM5 Residual Walk (app)"
type: entity
updated: 2026-11-17
sources: [S205, S212]
tags: [apps, swmm5, dynamic-wave, numerics, continuity, wasm]
reviewed: no
---
Bob's app SWMM5 Residual Walk: four tests of the dynamic wave iteration on EPA SWMM 5.2.4 in the page, made from two fractal pictures: the walk of trials inside one time step, the cliff where a short outfall link breaks it, step-halving refinement, and a Cantor storm. Version 1.0, 2026-11-04 [S212](../sources/S212-swmm5-residual-walk-summary.md). Netlify address: https://swmm5-residual-walk.netlify.app [S205](../sources/S205-note-netlify-addresses.md).

**A caution about its source.** The page ships no technical summary. [S212](../sources/S212-swmm5-residual-walk-summary.md) was written by Claude on 17 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q108).

**What the summary says** [S212](../sources/S212-swmm5-residual-walk-summary.md)
- Each dynamic wave trial keeps half the old value: OMEGA = 0.5 at dynwave.c line 61, so the trials close on their answer by about half per trial.
- A chain of pipes holds 0.00 % continuity through stage 8 (last link 1.17 ft, outfall peak 7.96 cfs against 7.95 for the one pipe, mean step 0.55 s).
- Stage 9, last link 0.59 ft: continuity 3.2 %, outfall peak 16.9 cfs. Stage 12, 0.073 ft: continuity -11,199 %, 3,688 cfs out from an 8 cfs inflow, and SWMM5 runs to the end with no error. Past the cliff the peak is noise and can fall (stage 10: 0.79 cfs).
- A 300 ft tail after the short links hides the failure (stage 11 at 0.00 %). A FIXED outfall moves the failure in: at a 0.4 ft last link continuity is -0.96 % against 65.0 % for FREE.
- Loop gain near critical flow is about (2/3) c dt/L; relaxed at omega = 1/2 the loop reaches r = 1 at a gain of 3, which puts the failure at c dt/L = 4.5.
- The trace changes nothing: on 100 corpus models the traced build's .out matched the pristine native build byte for byte.
- Browser against native: byte for byte on 89 of 100; on 5 of the other 11 conduit flows differ, largest 100 % of peak at pump MANLAKES1 in manifold_pumps, a pump switch moved by a last-bit change. Past the cliff stage 12 reads -11,199 % in the browser and -9,283 % native.
- Census: of 307 unique files from the 1729 corpus, 216 gave dynamic wave results for the screen and 158 ran the step-halving test.

**What it does not show.** No field data, and no claim that a walk that converges has converged on the truth. The omega figure on the Walk tab comes from a patched engine, for study only. No person has reviewed the Doc, checked the loop-gain derivation or tried the screen on a real pump station. [S212](../sources/S212-swmm5-residual-walk-summary.md)

**Noted at ingest.** (2/3) x 4.5 = 3, as stated. The page also corrects its source pictures: a countable union of segments has dimension 1, not 0. Here the continuity figure is what shows the failure, since the run ends with no error; [Continuity is not validation](../concepts/continuity-is-not-validation.md) is the opposite case, a good continuity figure on a wrong result.

See [Apps summarized on 17 November 2026: SWMM history and the insides of SWMM5](../concepts/apps-from-pages-history-and-swmm5.md), [Dynamic wave routing](../concepts/dynamic-wave-routing.md), [Continuity is not validation](../concepts/continuity-is-not-validation.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md), [1729-SWMM5-Models-2030 (the corpus)](corpus-1729.md).
