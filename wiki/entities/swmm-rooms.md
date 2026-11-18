---
title: "SWMM Rooms (app)"
type: entity
updated: 2026-11-17
sources: [S205, S232]
tags: [apps, swmm5, swmm6, hydrocouple, teaching]
reviewed: no
---
Bob's app SWMM Rooms: an isometric building of 36 rooms, each one feature of EPA SWMM 5.2, OpenSWMM 6 or the HydroCouple component framework, with its input keywords, a plain description, a pipe to every feature it feeds, a provenance note and a keeper who walks you through. Nothing runs. Version 1.4, 2026-10-20 [S232](../sources/S232-swmm-rooms-summary.md). Netlify address: https://swmm-rooms.netlify.app [S205](../sources/S205-note-netlify-addresses.md).

**A caution about its source.** The page ships no technical summary. [S232](../sources/S232-swmm-rooms-summary.md) was written by Claude on 17 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q108).

**What the summary says** [S232](../sources/S232-swmm-rooms-summary.md)
- 36 rooms in six wings (SWMM5 hydrology, SWMM5 hydraulics, SWMM5 analysis and API, SWMM6 dynamic wave, SWMM6 + HydroCouple, tooling and components) joined by 56 pipes.
- It uses the method of loci: features in rooms in order are easier to remember than a list.
- Every count, degree, cycle and keyword tally in the Doc's figures was computed from the room and pipe arrays of the published page; kind 'w' occurs only on SWMM5-to-SWMM5 pipes (25 of 25).
- Earlier versions in September 2026 grew from 25 to 36 rooms.

**What it does not show.** Nothing runs. The 56 pipes are an author's reading, not a call graph or data-flow analysis. A room's claim tells you what somebody read in the source, not a demonstration. [S232](../sources/S232-swmm-rooms-summary.md)

**Noted at ingest.** The page's figures were computed from its own arrays, as it says; nothing in the summary can be checked by arithmetic beyond that.

See [Apps summarized on 17 November 2026: generators, rain and surfaces for SWMM5](../concepts/apps-from-pages-generators-rain-surfaces.md), [How SWMM 5 is organized: objects, state and the time loop](../concepts/swmm5-objects-state-time-loop.md), [OpenSWMM 6 and HydroCouple](openswmm-6-and-hydrocouple.md), [Graphs: nodes, edges, direction and weight](../concepts/graph-basics.md).
