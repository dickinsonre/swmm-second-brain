---
title: "SWMM Inlet Library (app)"
type: entity
updated: 2026-11-17
sources: [S205, S234]
tags: [apps, swmm5, swmm6, inlets, streets, wasm]
reviewed: no
---
Bob's app SWMM Inlet Library: the SWMM counterpart of Christian Leonardo's Drainage.4d file generator for 12d Model: agency libraries of street sections and inlet designs, each inlet shown in plan and 3D with its capture computed by the HEC-22 code SWMM runs, written as [STREETS], [INLETS], [CURVES] and [INLET_USAGE] for EPA SWMM 5.2.4 or SWMM6. Version 1.0, 2026-10-26 [S234](../sources/S234-swmm-inlet-library-summary.md). Netlify address: https://swmm-inlet-library.netlify.app [S205](../sources/S205-note-netlify-addresses.md).

**A caution about its source.** The page ships no technical summary. [S234](../sources/S234-swmm-inlet-library-summary.md) was written by Claude on 17 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q108).

**What the summary says** [S234](../sources/S234-swmm-inlet-library-summary.md)
- The starter library holds 13 HEC22-generic inlet types (3 curb, 4 grate, 2 combination, 1 slot, 1 drop grate, 2 custom), 3 street sections, and pipe sizes (19 RCP, 21 RCBC).
- Both engines are WebAssembly builds carried over byte for byte from Seven SWMM Engines, hashes matched to its build record: EPA SWMM 5.2.4 (tag v5.2.4, 7952ca83) and OpenSWMM 6.0.0-alpha.4 (swmm6_rel, commit 3c30f1e6 of 17 October 2026, GeoPackage, 2D, HDF5 and GPU off).
- The JavaScript port agrees with both engines to 0.01 percentage point on seven inlet cases from six EPA steady decks.
- Of the sixteen street-inlet decks the OpenSWMM team uses for parity, fourteen print street capture and thirteen of those agree on peak capture to the printed precision; the two drop-grate decks print no street row and their routing continuity matches.

**What it does not show.** The example custom curves are illustrative, not agency charts. No 2D surface flow, and no grate clogging that changes during a storm. No other SWMM6 alpha build. [S234](../sources/S234-swmm-inlet-library-summary.md)

**Noted at ingest.** The summary does not say which of the fourteen decks disagrees on peak capture, or by how much. 3 + 4 + 2 + 1 + 1 + 2 = 13 inlet types.

See [Apps summarized on 17 November 2026: generators, rain and surfaces for SWMM5](../concepts/apps-from-pages-generators-rain-surfaces.md), [Seven SWMM Engines (app)](seven-swmm-engines.md), [Water on the Road (app)](water-on-the-road.md), [SWMM 5 network objects, boundary and initial conditions](../concepts/swmm5-network-objects.md).
