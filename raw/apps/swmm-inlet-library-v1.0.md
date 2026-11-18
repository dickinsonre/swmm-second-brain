---
name: SWMM Inlet Library
file: swmm-inlet-library.html
version: "1.0"
date: 2026-10-26
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/Uo53zpEt2aZ1kYieEo99Jo", repo: none named in the page}
engines:
  - {name: EPA SWMM, version: 5.2.4, source: "USEPA tag v5.2.4 (7952ca83); Emscripten 3.1.51 single file from Seven SWMM Engines", glue_sha256: 4602e507bb5c372c5b80952e585eb13f61137251b87fdddf2ff56f2d2eb8a45f, license: public domain}
  - {name: OpenSWMM, version: 6.0.0-alpha.4, branch: swmm6_rel, commit: 3c30f1e6, commit_date: 2026-10-17, note: "GeoPackage/2D/HDF5/GPU off", glue_sha256: 5ae19ddf4c12587206ebdef3ed3f623aabe887575ddec971fac7d2072fa2b8bf, license: Apache-2.0}
units: US customary with a US/SI switch
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was made with Claude at Robert Dickinson's request. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/Uo53zpEt2aZ1kYieEo99Jo, version 1793026266-0b06 (index.html, 7,236,441 bytes, SHA-256 e8eab201b424f137edfecf8321e67dd12f0936c20743e0c545c6ff65493da614), its About and Doc tabs read in headless Chromium on 2026-11-17. No model was run to write this file."
---

# SWMM Inlet Library: street-inlet libraries for SWMM 5.2.4 and SWMM6, after Christian Leonardo's Drainage.4d generator

## In three points
- **What:** The SWMM counterpart of Christian Leonardo's Drainage.4d file generator for 12d Model: keeps agency libraries of street sections and inlet designs, shows each inlet in plan and 3D, computes its capture with the HEC-22 code SWMM runs, and writes [STREETS], [INLETS], [CURVES] and [INLET_USAGE] for EPA SWMM 5.2.4 or SWMM6.
- **So what:** Its JavaScript port of the HEC-22 code agrees with both engines to 0.01 percentage point on seven inlet cases, and on the OpenSWMM team's sixteen street-inlet decks 13 of the 14 that print street capture agree on peak capture to the printed precision.
- **Now what:** Use it to build and check inlet libraries before writing them into a model. The example custom curves are illustrative, not agency charts, and there is no 2D surface flow or changing clogging.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("SWMM Inlet Library v1.0 · 2026-10-26"). The file name above is ours. Every number below is copied from the page. No model was run to write this file.

## What it does

The starter library holds 13 HEC22-generic inlet types (3 curb, 4 grate, 2 combination, 1 slot, 1 drop grate, 2 custom), 3 street sections and pipe sizes (19 RCP, 21 RCBC). Output for SWMM 5.2.4 or for SWMM6 with its [INLET_JUNCTIONS] and solver options. Tabs: Inlets, Catalogue, Street & Gutter, Pipes, Output, Files, Method, Engines, About, Doc. Libraries are a working copy in the browser.

## Checks (as stated on the page)

- Both engines are WebAssembly builds carried over byte for byte from Bob's Seven SWMM Engines app, hashes matched to its build record.
- JavaScript port against the engines on seven inlet cases from six EPA steady decks (grates, curb openings, a combination with a sweeper, depressed and plain gutters, one- and two-sided streets): all seven agree to 0.01 percentage point.
- The sixteen street-inlet decks the OpenSWMM team uses for parity, run through both engines: fourteen print street capture and thirteen agree on peak capture to the printed precision; the two drop-grate decks print no street row and their routing continuity matches.

## What this does not show

- Agency inlet charts (the example custom curves are illustrative).
- 2D surface flow, or grate clogging that changes during a storm.
- SWMM6 alpha builds other than the one listed.

## How to reproduce

Open the page, edit the libraries, and write the sections on Output; Engines runs both engines.

## Credits and licenses

Christian Leonardo's Drainage.4d generator for 12d Model (the idea; no code). HEC-22 inlet methods as coded in EPA SWMM 5.2.4 (public domain). OpenSWMM Engine (HydroCouple), Apache-2.0. No license is stated for the page.

## AI use

The page says the app and essay were made with Claude, Anthropic's AI model, in October 2026, at Robert (Bob) Dickinson's request; he supplied the 12d screenshot and set the goal. Claude read the EPA SWMM 5.2.4 and OpenSWMM inlet sources, ported the HEC-22 code to JavaScript, wrote the library model, the .inp writer and importer, the page, its 3D view, the tests and the text. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 1.0 (2026-10-26): first version.
