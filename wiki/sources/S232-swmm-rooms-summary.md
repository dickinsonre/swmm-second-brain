---
title: "S232: SWMM Rooms, summary written from the page (v1.4)"
type: source
raw: raw/apps/swmm-rooms-v1.4.md
kind: app-md
author: Robert Dickinson
published: 2026-10-20
ingested: 2026-11-17
tags: [apps, swmm5, swmm6, hydrocouple, teaching]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app SWMM Rooms, version 1.4: an isometric building of 36 rooms, each one feature of EPA SWMM 5.2, OpenSWMM 6 or the HydroCouple component framework, with its input keywords, a plain description, a pipe to every feature it feeds, a provenance note and a keeper who walks you through. Nothing runs. Raw file: [raw/apps/swmm-rooms-v1.4.md](../../raw/apps/swmm-rooms-v1.4.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 17 November 2026, at Bob's request, from the published Claude artifact, version 1792448311-3401, reading its Map and Doc tabs in a headless browser; nothing was run to write it. Bob has not read it (Q108). The page says Bob directed the work, chose which features deserved rooms and which wing each belongs to, set the standard that a measured claim and a README claim must look different, and reviewed the result; Claude built the app in Claude Code sessions in September 2026 and drafted the room and pipe records, which Bob then edited; Claude wrote the Doc in October 2026.

**Claims worth keeping** (all copied from the file)
- 36 rooms in six wings (SWMM5 hydrology, SWMM5 hydraulics, SWMM5 analysis and API, SWMM6 dynamic wave, SWMM6 + HydroCouple, tooling and components) joined by 56 pipes.
- It uses the method of loci: features in rooms in order are easier to remember than a list.
- Every count, degree, cycle and keyword tally in the Doc's figures was computed from the room and pipe arrays of the published page; kind 'w' occurs only on SWMM5-to-SWMM5 pipes (25 of 25).
- Earlier versions in September 2026 grew from 25 to 36 rooms.

**Limits it states.** Nothing runs. The 56 pipes are an author's reading, not a call graph or data-flow analysis. A room's claim tells you what somebody read in the source, not a demonstration.

**Checked at ingest.** The page's figures were computed from its own arrays, as it says; nothing in the summary can be checked by arithmetic beyond that. The `links:` line gives Netlify as "not yet deployed"; Netlify reported a finished deploy at https://swmm-rooms.netlify.app on 17 November 2026 [S205](S205-note-netlify-addresses.md).

**Feeds:** [SWMM Rooms (app)](../entities/swmm-rooms.md), [Apps summarized on 17 November 2026: generators, rain and surfaces for SWMM5](../concepts/apps-from-pages-generators-rain-surfaces.md), [How SWMM 5 is organized: objects, state and the time loop](../concepts/swmm5-objects-state-time-loop.md), [OpenSWMM 6 and HydroCouple](../entities/openswmm-6-and-hydrocouple.md), [Graphs: nodes, edges, direction and weight](../concepts/graph-basics.md).
