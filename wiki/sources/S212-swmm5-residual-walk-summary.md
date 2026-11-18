---
title: "S212: SWMM5 Residual Walk, summary written from the page (v1.0)"
type: source
raw: raw/apps/swmm5-residual-walk-v1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-11-04
ingested: 2026-11-17
tags: [apps, swmm5, dynamic-wave, numerics, continuity, wasm]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app SWMM5 Residual Walk, version 1.0: four tests of the dynamic wave iteration on EPA SWMM 5.2.4 in the page, made from two fractal pictures: the walk of trials inside one time step, the cliff where a short outfall link breaks it, step-halving refinement, and a Cantor storm. Raw file: [raw/apps/swmm5-residual-walk-v1.0.md](../../raw/apps/swmm5-residual-walk-v1.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 17 November 2026, at Bob's request, from the published Claude artifact, version 1793828431-ed0a, reading its About and Doc tabs in a headless browser; nothing was run to write it. Bob has not read it (Q108). The page says the app, its engine build, its tests and its Doc were made with Claude in a session in November 2026 under Bob's direction: Bob supplied the graphics and the question (does fractal geometry have any use in SWMM or ICM?); Claude added a read-only trial trace to the engine, compiled it, wrote the tests and census scripts and derived the linear loop model.

**Claims worth keeping** (all copied from the file)
- Each dynamic wave trial keeps half the old value: OMEGA = 0.5 at dynwave.c line 61, so the trials close on their answer by about half per trial.
- A chain of pipes holds 0.00 % continuity through stage 8 (last link 1.17 ft, outfall peak 7.96 cfs against 7.95 for the one pipe, mean step 0.55 s).
- Stage 9, last link 0.59 ft: continuity 3.2 %, outfall peak 16.9 cfs. Stage 12, 0.073 ft: continuity -11,199 %, 3,688 cfs out from an 8 cfs inflow, and SWMM5 runs to the end with no error. Past the cliff the peak is noise and can fall (stage 10: 0.79 cfs).
- A 300 ft tail after the short links hides the failure (stage 11 at 0.00 %). A FIXED outfall moves the failure in: at a 0.4 ft last link continuity is -0.96 % against 65.0 % for FREE.
- Loop gain near critical flow is about (2/3) c dt/L; relaxed at omega = 1/2 the loop reaches r = 1 at a gain of 3, which puts the failure at c dt/L = 4.5.
- The trace changes nothing: on 100 corpus models the traced build's .out matched the pristine native build byte for byte.
- Browser against native: byte for byte on 89 of 100; on 5 of the other 11 conduit flows differ, largest 100 % of peak at pump MANLAKES1 in manifold_pumps, a pump switch moved by a last-bit change. Past the cliff stage 12 reads -11,199 % in the browser and -9,283 % native.
- Census: of 307 unique files from the 1729 corpus, 216 gave dynamic wave results for the screen and 158 ran the step-halving test.

**Limits it states.** No field data, and no claim that a walk that converges has converged on the truth. The omega figure on the Walk tab comes from a patched engine, for study only. No person has reviewed the Doc, checked the loop-gain derivation or tried the screen on a real pump station.

**Checked at ingest.** (2/3) x 4.5 = 3, as stated. The page also corrects its source pictures: a countable union of segments has dimension 1, not 0. Here the continuity figure is what shows the failure, since the run ends with no error; [Continuity is not validation](../concepts/continuity-is-not-validation.md) is the opposite case, a good continuity figure on a wrong result. The `links:` line gives Netlify as "not yet deployed"; Netlify reported a finished deploy at https://swmm5-residual-walk.netlify.app on 17 November 2026 [S205](S205-note-netlify-addresses.md).

**Feeds:** [SWMM5 Residual Walk (app)](../entities/swmm5-residual-walk.md), [Apps summarized on 17 November 2026: SWMM history and the insides of SWMM5](../concepts/apps-from-pages-history-and-swmm5.md), [Dynamic wave routing](../concepts/dynamic-wave-routing.md), [Continuity is not validation](../concepts/continuity-is-not-validation.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md), [1729-SWMM5-Models-2030 (the corpus)](../entities/corpus-1729.md).
