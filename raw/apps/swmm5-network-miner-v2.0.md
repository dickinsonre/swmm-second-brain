---
name: SWMM5 Network Miner (single-file edition)
file: swmm5-network-miner.html
version: "2.0"
date: 2026-10
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/GZspfddPZFMUQx9NWAg3Dv", original: "Replit app SWMM5 Network Miner (https://swmm-filebase--robertdickinson.replit.app, v1.0.0), whose own summary is raw/apps/swmm-filebase--robertdickinson-v1.0.0.md", repo: "https://github.com/dickinsonre/SWMM-Filebase"}
engines:
  - {name: EPA SWMM, version: 5.2.4, build: "USEPA tag v5.2.4, src/solver/*.c unmodified; clang 18.1.3, wasm32-wasi reactor (wasi-sdk-24) with mkstemp and realpath stand-ins; @bjorn3/browser_wasi_shim 0.4.2 in a Web Worker, fresh instance per run; 539,885 bytes, SHA-256 e448f6928f1b4c1bff2a4d204a9d908fa8b90cda4732164cc653b764255415e1", license: public domain}
units: US customary or SI, following each model's FLOW_UNITS; display units in the header
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude in October 2026 under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/GZspfddPZFMUQx9NWAg3Dv, version 1792949039-0c6d (index.html, 1,591,279 bytes, SHA-256 1723acf9258eb51055a568ebe69c28ad8087209f285755d7d71b44b8cf04b8d6), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# SWMM5 Network Miner, single-file edition: a library tool for SWMM5 models with EPA SWMM 5.2.4 in the page

## In three points
- **What:** Load a pile of .inp files, see what is in them, check them, compare them, cut long conduits with ReSWMM, and run any of them in EPA SWMM 5.2.4, all in one HTML file with nothing leaving the browser. A single-file edition of Bob's Replit app SWMM5 Network Miner, which kept models in PostgreSQL and Replit Object Storage behind an Express server and whose browser engine was 5.1.015.
- **So what:** The Audit lists ReSWMM defects R1 to R11 (junction rows, cross-sections, offsets, rims and references written wrongly), now fixed, with unit conversion for SI models and a CFL time-step preview. "AI Analysis" is renamed Health Check because it is a rule list; a new rule catches the rain-gage interval mistake in all five samples. The page hashes the wasm it decodes and shows that it matches the build (e448f692...).
- **Now what:** Use it to triage a folder of models before running them. A clean run means the arithmetic closed, not that the model is right; a Health score of 100 means no rule fired. XP files are kept but not parsed, and only EPA SWMM 5.2.4 runs here.

This summary was written after the fact. The page ships no technical summary of its own. Its version is the page's own ("v2.0 · HTML · EPA 5.2.4"); it gives the build month (October 2026) but no day. The file name above is ours; the name above adds "single-file edition" to tell it from the Replit original. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Library, Compare, Health Check, Insights, ReSWMM, Audit, About, Doc. The library is held in the tab's memory and saved with Export library (ZIP). Insights reads FLOW_UNITS before converting diameters and lengths; the diff no longer needs an m x n table; maps draw real node types; slopes use conduit inverts. Theme (Dark, Light, Auto), the four Replit colour themes (EPA, UF, Oregon State, Auburn) and US/SI units sit in the header. Controls that did nothing in the Replit app are gone.

## Checks (as stated on the page)

- A Node suite, engine runs and a headless-browser test (described in the Doc).
- Every run's .rpt header reads "VERSION 5.2 (Build 5.2.4)"; the page computes the SHA-256 of the wasm it decodes and shows it next to the build hash (matching hashes show the bytes are the bytes built; they are not a signature).
- The Replit source read line by line for the Audit findings.

## What this does not show

As the page lists it: a clean run is not a correct model (nothing here knows where the city put its pipes, whether roughness was calibrated, or whether the storm is the one the permit asked for); XP files are kept, shown and searched but not parsed; EPA SWMM 5.2.4 only, not SWMM 5.1, OpenSWMM 6 or InfoWorks ICM; ReSWMM's interior junctions are computational points. No person has run this edition against Bob's full thousand-model library, and the 0.10 conservative time-step factor in the ReSWMM spec has not been checked against the paper it cites.

## Credits and licenses

U.S. EPA, SWMM 5.2.4 source (public domain); @bjorn3/browser_wasi_shim; the Replit SWMM5 Network Miner and its repository dickinsonre/SWMM-Filebase.

## AI use

The page says: built with Claude, Anthropic's AI model, in a Claude session in October 2026 under the direction of Robert (Bob) Dickinson, who wrote and ran the original Replit app, supplied its source, and asked for this single-file edition; responsibility is his. Claude read the Replit source line by line and wrote the Audit findings, ported the parser, rule set, diff, statistics and ReSWMM to browser JavaScript and repaired the defects, compiled EPA SWMM 5.2.4 to WebAssembly and wrote the worker and shim glue, and built the interface, maps, charts and the Doc. The checks are mechanical. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 2.0 (2026-10): single-file edition with EPA SWMM 5.2.4 in the page (the version read).
- 1.0.0 (Replit): the original app.
