---
title: "S302: SWMM5 / SWMM6 Mograph, summary written from the page (v3.1)"
type: source
raw: raw/apps/swmm5-swmm6-mograph-v3.1.md
kind: app-md
author: Robert Dickinson
published: 2026-11-09
ingested: 2026-11-18
tags: [films, swmm5, swmm6, wasm, mograph]
drafted_by: Claude (Anthropic), from the published page
reviewed: 2026-11-18
---
**What it is.** A technical summary of the film SWMM5 / SWMM6 Mograph, version 3.1: one storm, start to finish, in 60 seconds, on real engine output. Raw file: [raw/apps/swmm5-swmm6-mograph-v3.1.md](../../raw/apps/swmm5-swmm6-mograph-v3.1.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/Sm3isXtCy3GcAjE7N7bnLd, version 1794277170-f07d (index.html, 9,924,565 bytes, SHA-256 819e95df3fee7b973a6f878adc26d588014d8a07c34700996c7df9e40cf4ad9f), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file." Its AI-use section: "The page says: built with Claude, Anthropic's AI model, in one chat session in November 2026; Robert (Bob) Dickinson asked what a mograph is, asked for one about SWMM5, then asked for the map and for a way to change the input file."

**Claims worth keeping** (all copied from the file)
- A 60-second motion graphic that follows one storm through the engine you pick, from the hyetograph through rain, runoff, routing and outfall to the continuity ledger. It runs on real output: EPA SWMM 5.2.4 and OpenSWMM 6 (dynamic wave and finite volume, through the swmm6-go translation) both run inside the page, so every bar, water level and curve is a number an engine wrote, and changing the model in the Model tab changes the film.
- The Compare tab runs the model through all three solvers, changing only the FLOW_ROUTING line between the two SWMM6 runs; the film picks the node with the widest gap in peak depth among the runs (J3 on the built-in model) and also counts how long each run holds it above the crown. The wasm EPA engine's results block is byte-identical to a native 5.2.4 build on the built-in model; on five pyswmm test models, three matched byte for byte and two agreed on outfall peak to 0.02% or better.
- The WebAssembly EPA engine and a native 5.2.4 build on the built-in model: results blocks byte-identical.
- The JavaScript readers compared with the Python originals on the same files; tank depths tested by mass balance against the report's final storage.
- Five public pyswmm example models against a native build: three byte for byte, two with outfall peak within 0.02%.
- Seventeen models (SI, kinematic wave, LID, pump and storage cases among them) run through every scene and the map with no drawing error; frames looked at for three. In a headless browser: three quick edits, a deliberate input error and three loaded files.

**Limits it states.** As the page lists it: a calibrated model of any real place; the real water profile inside a pipe; the separate depths inside a tank.

**Checked at ingest.** The page bundles swmm6-go, the Go translation of OpenSWMM 6 (Apache-2.0), without reproducing the upstream LICENSE and NOTICE, so its Netlify folder adds OPENSWMM-LICENSE and OPENSWMM-NOTICE (swmm6_rel at 2a98cbe). The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [SWMM5 / SWMM6 Mograph (film)](../entities/swmm5-swmm6-mograph.md), [Apps summarized on 18 November 2026: SWMM6, SWMM5+ and solvers](../concepts/apps-from-pages-swmm6-solvers-and-swmm5plus.md), [SWMM6 language translations (swmm6-*)](../entities/swmm6-language-ports.md), [OpenSWMM 6 and HydroCouple](../entities/openswmm-6-and-hydrocouple.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md).
