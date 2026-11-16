---
title: "S175: note, keep ICM flood maps tied to the result definition and its time"
type: source
raw: raw/notes/icm-2d-results-and-hazard.md
kind: note
author: Robert Dickinson
published: 2026-11-16
ingested: 2026-11-16
tags: [icm, 2d, results, hazard, note]
drafted_by: GPT plugin for Autodesk (an AI), per S166
reviewed: no
---
**What it is.** A note on exporting ICM 2D results. Raw file: [raw/notes/icm-2d-results-and-hazard.md](../../raw/notes/icm-2d-results-and-hazard.md).

**How it was written.** One of ten notes Bob supplied on 16 November 2026 in `ICM-2D-Modeling-Notes.zip`, copied into `raw/notes/` unchanged, on the note template, dated 2026-11-16, status seed. Bob says the notes come from the GPT plugin for Autodesk [S166](S166-note-icm-notes-from-gpt-plugin.md): AI-written text. Its facts about ICM are reported from Autodesk's 2027 online help, linked in the note, and were not checked here against ICM or the help pages. Its procedure is a test design that has not been run. Every claim below is flagged accordingly: AI-written passage, not checked against ICM.

**Claims worth keeping** (as the note states them; AI-written, not checked against ICM)
- Depth, level, speed, time to first inundation and hazard answer different questions; record the quantity and time basis of each exported result.
- InfoWorks documents `Depth at first max hazard` and `Speed at first max hazard`, a matched pair for explaining a hazard map at a point.
- Record for depth or level: units, terrain reference or datum, timestep or maximum, wet/dry threshold; for speed: location, units and the same time as the plotted depth; for first inundation: the depth threshold; for flow across a transect: the line, sign convention, hydrograph and event volume.
- Test: three fixed points and a transect captured with Network Results objects, repeated after remeshing, with map and hydrograph exported together.

**Feeds:** [ICM 2D: timestep, volume balance and results](../concepts/icm-2d-runs-and-checks.md).
