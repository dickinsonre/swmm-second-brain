---
title: "S219: SWMM Clean Repro, summary written from the page (v1.0)"
type: source
raw: raw/apps/swmm-clean-repro-v1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-13
ingested: 2026-11-17
tags: [apps, swmm5, sharing, anonymizing, wasm]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app SWMM Clean Repro, version 1.0: a tool that takes a SWMM5 model that cannot be shared, cuts out the smallest piece that shows the problem, removes names, comments, paths, coordinates, dates and datum, and runs both versions through EPA SWMM 5.2.4 in the browser to show the answer did not change. The file stays in the browser. Raw file: [raw/apps/swmm-clean-repro-v1.0.md](../../raw/apps/swmm-clean-repro-v1.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 17 November 2026, at Bob's request, from the published Claude artifact, version 1791872997-4291, reading every tab in a headless browser; nothing was run to write it. Bob has not read it (Q108). The published page carries no AI-use note; it is a Claude artifact on Bob's account, built in a claude.ai session. The summary says the Netlify copy adds a one-line AI-use note.

**Claims worth keeping** (all copied from the file)
- For a cut, the engine first runs the full model and records boundary levels and flows in the cut pipes every 20 s, which become the cut-out's boundary conditions.
- The scrub renames every ID in every section, control rules included and case-insensitively as SWMM does; moves the map; shifts dates by a multiple of 28 years (same weekday and leap-year pattern); and shifts the elevation datum without changing any conduit's direction.
- Scrubbing without a cut is bit-for-bit identical on 30 of 30 public test models, because the dates move within one power-of-two band of SWMM's day count.
- A careless 28-year shift into another band changed the number of report periods on 16 of 31 models; the tool offers only shifts that stay in the band.
- Datum shift with the tool's choice: identical on 26 of 30 models; the others are metric (SWMM divides by 0.3048 on input) or span several bands; the largest effect was 1.15 % of a link's peak at one instant.
- The sample is EPA EXTRAN Example 1 with a fictional city, people, monitor names and coordinates added, hydraulics unchanged; the page counts 23 object names, 3 title lines, 19 comments, 10 map coordinates, 2 file paths and 4 tags and labels that point back to the owner.
- Engine: tag v5.2.4, commit 7952ca8, compiled to wasm32-wasi and run in a Web Worker with a fresh instance per run.

**Limits it states.** It does not show that the model is right or that the cut-out answers every question the full model does. It removes names and offsets, not the network's shape, which a person who knows the system could recognise.

**Checked at ingest.** Two counts of the public test models appear, 30 and 31; the summary does not say why. Day counts and float rounding of this kind are the subject of [Run duration floored to whole seconds](../concepts/run-duration-floor.md). The `links:` line gives Netlify as "not yet deployed"; Netlify reported a finished deploy at https://swmm-clean-repro.netlify.app on 17 November 2026 [S205](S205-note-netlify-addresses.md).

**Feeds:** [SWMM Clean Repro (app)](../entities/swmm-clean-repro.md), [Apps summarized on 17 November 2026: SWMM history and the insides of SWMM5](../concepts/apps-from-pages-history-and-swmm5.md), [Run duration floored to whole seconds](../concepts/run-duration-floor.md), [Byte-for-byte gate](../concepts/byte-for-byte-gate.md).
