---
name: SWMM5 / SWMM6 Mograph
file: swmm5-swmm6-mograph.html
version: "3.1"
date: 2026-11-09
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/Sm3isXtCy3GcAjE7N7bnLd", repo: none}
engines:
  - {name: EPA SWMM, version: 5.2.4, note: "unmodified source compiled to WebAssembly, running in the page", license: public domain}
  - {name: OpenSWMM 6, version: "6.0.0-alpha.4 through swmm6-go, the Go translation, compiled to WebAssembly", note: "dynamic wave and finite volume solvers, running in the page; OpenSWMM 6 is Apache-2.0"}
units: US customary for the built-in model; loaded models in their own units
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude in one chat session in November 2026 under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/Sm3isXtCy3GcAjE7N7bnLd, version 1794277170-f07d (index.html, 9,924,565 bytes, SHA-256 819e95df3fee7b973a6f878adc26d588014d8a07c34700996c7df9e40cf4ad9f), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# SWMM5 / SWMM6 Mograph: one storm, start to finish, in 60 seconds, on real engine output

## In three points
- **What:** A 60-second motion graphic that follows one storm through the engine you pick, from the hyetograph through rain, runoff, routing and outfall to the continuity ledger. It runs on real output: EPA SWMM 5.2.4 and OpenSWMM 6 (dynamic wave and finite volume, through the swmm6-go translation) both run inside the page, so every bar, water level and curve is a number an engine wrote, and changing the model in the Model tab changes the film.
- **So what:** The Compare tab runs the model through all three solvers, changing only the FLOW_ROUTING line between the two SWMM6 runs; the film picks the node with the widest gap in peak depth among the runs (J3 on the built-in model) and also counts how long each run holds it above the crown. The wasm EPA engine's results block is byte-identical to a native 5.2.4 build on the built-in model; on five pyswmm test models, three matched byte for byte and two agreed on outfall peak to 0.02% or better.
- **Now what:** Use it to show a storm moving through SWMM and to see where the SWMM6 solvers part from SWMM5. The built-in model is one synthetic storm on an invented catchment (3 subcatchments, 4 nodes, 3 links); the pipe surface is drawn straight between node and mid-pipe depths.

This summary was written after the fact. The film ships no technical summary of its own. Its version and date are the page's own ("v3.1 · 2026-11-09"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Film, Map, Model, Compare, Report, Doc, About. The film shows SWMM5, SWMM6 dynamic wave, SWMM6 finite volume, or all three compared; pause, restart, speed, loop, full screen; scenes 00 Title, 01 Rain, 02 Runoff, 03 Routing, 04 Outfall, 05 Ledger. The Model tab holds the .inp with quick edits and file loading. Tanks show an area-average depth.

## Checks (as stated on the page)

- The WebAssembly EPA engine and a native 5.2.4 build on the built-in model: results blocks byte-identical.
- The JavaScript readers compared with the Python originals on the same files; tank depths tested by mass balance against the report's final storage.
- Five public pyswmm example models against a native build: three byte for byte, two with outfall peak within 0.02%.
- Seventeen models (SI, kinematic wave, LID, pump and storage cases among them) run through every scene and the map with no drawing error; frames looked at for three. In a headless browser: three quick edits, a deliberate input error and three loaded files.

## What this does not show

As the page lists it: a calibrated model of any real place; the real water profile inside a pipe; the separate depths inside a tank.

## Credits and licenses

EPA SWMM 5.2.4 (public domain); OpenSWMM 6 by HydroCouple (Apache-2.0), here through swmm6-go, Bob's Go translation; pyswmm's example models. The page does not reproduce OpenSWMM's LICENSE and NOTICE.

## AI use

The page says: built with Claude, Anthropic's AI model, in one chat session in November 2026; Robert (Bob) Dickinson asked what a mograph is, asked for one about SWMM5, then asked for the map and for a way to change the input file. Claude chose the storyboard and designed the built-in model, wrote the built-in input file, compiled the unmodified EPA SWMM 5.2.4 source and swmm6-go to WebAssembly with a small in-memory file layer, ported the output readers, and wrote the page and the Doc. The checks are mechanical. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 3.1 (2026-11-09): the version read. 3.0: OpenSWMM 6 added beside EPA SWMM 5.2.4. Earlier versions: SWMM5 only.
