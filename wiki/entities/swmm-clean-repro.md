---
title: "SWMM Clean Repro (app)"
type: entity
updated: 2026-11-17
sources: [S205, S219]
tags: [apps, swmm5, sharing, anonymizing, wasm]
reviewed: no
---
Bob's app SWMM Clean Repro: a tool that takes a SWMM5 model that cannot be shared, cuts out the smallest piece that shows the problem, removes names, comments, paths, coordinates, dates and datum, and runs both versions through EPA SWMM 5.2.4 in the browser to show the answer did not change. The file stays in the browser. Version 1.0, 2026-10-13 [S219](../sources/S219-swmm-clean-repro-summary.md). Netlify address: https://swmm-clean-repro.netlify.app [S205](../sources/S205-note-netlify-addresses.md).

**A caution about its source.** The page ships no technical summary. [S219](../sources/S219-swmm-clean-repro-summary.md) was written by Claude on 17 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q108).

**What the summary says** [S219](../sources/S219-swmm-clean-repro-summary.md)
- For a cut, the engine first runs the full model and records boundary levels and flows in the cut pipes every 20 s, which become the cut-out's boundary conditions.
- The scrub renames every ID in every section, control rules included and case-insensitively as SWMM does; moves the map; shifts dates by a multiple of 28 years (same weekday and leap-year pattern); and shifts the elevation datum without changing any conduit's direction.
- Scrubbing without a cut is bit-for-bit identical on 30 of 30 public test models, because the dates move within one power-of-two band of SWMM's day count.
- A careless 28-year shift into another band changed the number of report periods on 16 of 31 models; the tool offers only shifts that stay in the band.
- Datum shift with the tool's choice: identical on 26 of 30 models; the others are metric (SWMM divides by 0.3048 on input) or span several bands; the largest effect was 1.15 % of a link's peak at one instant.
- The sample is EPA EXTRAN Example 1 with a fictional city, people, monitor names and coordinates added, hydraulics unchanged; the page counts 23 object names, 3 title lines, 19 comments, 10 map coordinates, 2 file paths and 4 tags and labels that point back to the owner.
- Engine: tag v5.2.4, commit 7952ca8, compiled to wasm32-wasi and run in a Web Worker with a fresh instance per run.

**What it does not show.** It does not show that the model is right or that the cut-out answers every question the full model does. It removes names and offsets, not the network's shape, which a person who knows the system could recognise. [S219](../sources/S219-swmm-clean-repro-summary.md)

**Noted at ingest.** Two counts of the public test models appear, 30 and 31; the summary does not say why. Day counts and float rounding of this kind are the subject of [Run duration floored to whole seconds](../concepts/run-duration-floor.md).

See [Apps summarized on 17 November 2026: SWMM history and the insides of SWMM5](../concepts/apps-from-pages-history-and-swmm5.md), [Run duration floored to whole seconds](../concepts/run-duration-floor.md), [Byte-for-byte gate](../concepts/byte-for-byte-gate.md).
