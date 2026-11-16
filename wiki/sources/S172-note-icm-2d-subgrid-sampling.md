---
title: "S172: note, test ICM subgrid storage and flow across faces separately"
type: source
raw: raw/notes/icm-2d-subgrid-sampling.md
kind: note
author: Robert Dickinson
published: 2026-11-16
ingested: 2026-11-16
tags: [icm, 2d, subgrid, mesh, note]
drafted_by: GPT plugin for Autodesk (an AI), per S166
reviewed: no
---
**What it is.** A note on ICM's subgrid sampling. Raw file: [raw/notes/icm-2d-subgrid-sampling.md](../../raw/notes/icm-2d-subgrid-sampling.md).

**How it was written.** One of ten notes Bob supplied on 16 November 2026 in `ICM-2D-Modeling-Notes.zip`, copied into `raw/notes/` unchanged, on the note template, dated 2026-11-16, status seed. Bob says the notes come from the GPT plugin for Autodesk [S166](S166-note-icm-notes-from-gpt-plugin.md): AI-written text. Its facts about ICM are reported from Autodesk's 2027 online help, linked in the note, and were not checked here against ICM or the help pages. Its procedure is a test design that has not been run. Every claim below is flagged accordingly: AI-written passage, not checked against ICM.

**Claims worth keeping** (as the note states them; AI-written, not checked against ICM)
- Subgrid sampling uses finer terrain to form volume-level tables inside 2D elements and to sample the terrain profile along their faces; the face profile enters the mass and momentum flux calculations.
- Autodesk documents that a crest through the middle of an element can be bypassed.
- Autodesk's 2027 help calls the feature a Tech Preview and says meshing or running it needs a license with unlimited elements.
- The subgrid speed theme shows the parent element's speed on wetted subtriangles.
- Test: a corridor with an embankment and one surveyed gap, in four runs: a fine mesh aligned to the crest (reference), a coarser mesh, the coarser mesh with subgrid sampling, and subgrid with mesh edges aligned to the crest; compare storage, arrival on both sides, flow through the gap and volume over the embankment.
- The note calls this a proposed comparison for the SWMM2D work.

**Feeds:** [ICM 2D: terrain, mesh and subgrid sampling](../concepts/icm-2d-mesh-and-subgrid.md).
