---
title: "S167: note, build the ICM 2D mesh around the flow paths that matter"
type: source
raw: raw/notes/icm-2d-terrain-and-mesh.md
kind: note
author: Robert Dickinson
published: 2026-11-16
ingested: 2026-11-16
tags: [icm, 2d, mesh, terrain, note]
reviewed: no
---
**What it is.** A note on building an InfoWorks ICM 2D mesh and checking its terrain. Raw file: [raw/notes/icm-2d-terrain-and-mesh.md](../../raw/notes/icm-2d-terrain-and-mesh.md).

**How it was written.** One of ten notes Bob supplied on 16 November 2026 in `ICM-2D-Modeling-Notes.zip`, copied into `raw/notes/` unchanged, on the note template, dated 2026-11-16, status seed. Bob says the notes come from the GPT plugin for Autodesk [S166](S166-note-icm-notes-from-gpt-plugin.md): AI-written text. Its facts about ICM are reported from Autodesk's 2027 online help, linked in the note, and were not checked here against ICM or the help pages. Its procedure is a test design that has not been run. Every claim below is flagged accordingly: AI-written passage, not checked against ICM.

**Claims worth keeping** (as the note states them; AI-written, not checked against ICM)
- The 2D zone defines the area to mesh; ICM forms triangular elements from the meshing inputs and takes elevations from the selected ground model.
- Inputs and what to check: ground model (source, coordinate system, vertical datum, survey date); 2D zone (what is included, where the boundary meets flow paths); mesh zone (local refinement around a channel, gutter or entrance); break line (mesh edges follow it); mesh level zone (which element elevations change); roughness zone (resistance, and whether its boundary is a break line); void, building or wall (removes area, changes levels or controls cross-flow).
- First check: one street reach, a baseline mesh and a locally refined mesh on the same terrain and event; compare crest and gutter elevations, inundation timing at fixed coordinates, and discharge across one results line; record the generation method, element count and meshing log.

**Feeds:** [ICM 2D: terrain, mesh and subgrid sampling](../concepts/icm-2d-mesh-and-subgrid.md).
