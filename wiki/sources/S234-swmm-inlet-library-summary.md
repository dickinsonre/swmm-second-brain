---
title: "S234: SWMM Inlet Library, summary written from the page (v1.0)"
type: source
raw: raw/apps/swmm-inlet-library-v1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-26
ingested: 2026-11-17
tags: [apps, swmm5, swmm6, inlets, streets, wasm]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app SWMM Inlet Library, version 1.0: the SWMM counterpart of Christian Leonardo's Drainage.4d file generator for 12d Model: agency libraries of street sections and inlet designs, each inlet shown in plan and 3D with its capture computed by the HEC-22 code SWMM runs, written as [STREETS], [INLETS], [CURVES] and [INLET_USAGE] for EPA SWMM 5.2.4 or SWMM6. Raw file: [raw/apps/swmm-inlet-library-v1.0.md](../../raw/apps/swmm-inlet-library-v1.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 17 November 2026, at Bob's request, from the published Claude artifact, version 1793026266-0b06, reading its About and Doc tabs in a headless browser; nothing was run to write it. Bob has not read it (Q108). The page says the app and essay were made with Claude in October 2026 at Bob's request; he supplied the 12d screenshot and set the goal. Claude read the EPA SWMM 5.2.4 and OpenSWMM inlet sources, ported the HEC-22 code to JavaScript and wrote the library model, the .inp writer and importer and the tests.

**Claims worth keeping** (all copied from the file)
- The starter library holds 13 HEC22-generic inlet types (3 curb, 4 grate, 2 combination, 1 slot, 1 drop grate, 2 custom), 3 street sections, and pipe sizes (19 RCP, 21 RCBC).
- Both engines are WebAssembly builds carried over byte for byte from Seven SWMM Engines, hashes matched to its build record: EPA SWMM 5.2.4 (tag v5.2.4, 7952ca83) and OpenSWMM 6.0.0-alpha.4 (swmm6_rel, commit 3c30f1e6 of 17 October 2026, GeoPackage, 2D, HDF5 and GPU off).
- The JavaScript port agrees with both engines to 0.01 percentage point on seven inlet cases from six EPA steady decks.
- Of the sixteen street-inlet decks the OpenSWMM team uses for parity, fourteen print street capture and thirteen of those agree on peak capture to the printed precision; the two drop-grate decks print no street row and their routing continuity matches.

**Limits it states.** The example custom curves are illustrative, not agency charts. No 2D surface flow, and no grate clogging that changes during a storm. No other SWMM6 alpha build.

**Checked at ingest.** The summary does not say which of the fourteen decks disagrees on peak capture, or by how much. 3 + 4 + 2 + 1 + 1 + 2 = 13 inlet types. The `links:` line gives Netlify as "not yet deployed"; Netlify reported a finished deploy at https://swmm-inlet-library.netlify.app on 17 November 2026 [S205](S205-note-netlify-addresses.md).

**Feeds:** [SWMM Inlet Library (app)](../entities/swmm-inlet-library.md), [Apps summarized on 17 November 2026: generators, rain and surfaces for SWMM5](../concepts/apps-from-pages-generators-rain-surfaces.md), [Seven SWMM Engines (app)](../entities/seven-swmm-engines.md), [Water on the Road (app)](../entities/water-on-the-road.md), [SWMM 5 network objects, boundary and initial conditions](../concepts/swmm5-network-objects.md).
