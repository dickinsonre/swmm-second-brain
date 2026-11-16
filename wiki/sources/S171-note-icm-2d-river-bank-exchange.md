---
title: "S171: note, use bank crest profiles to check river-floodplain exchange in ICM"
type: source
raw: raw/notes/icm-2d-river-bank-exchange.md
kind: note
author: Robert Dickinson
published: 2026-11-16
ingested: 2026-11-16
tags: [icm, 2d, river, banks, note]
reviewed: no
---
**What it is.** A note on a River Reach spilling to a connected 2D zone over its banks. Raw file: [raw/notes/icm-2d-river-bank-exchange.md](../../raw/notes/icm-2d-river-bank-exchange.md).

**How it was written.** One of ten notes Bob supplied on 16 November 2026 in `ICM-2D-Modeling-Notes.zip`, copied into `raw/notes/` unchanged, on the note template, dated 2026-11-16, status seed. Bob says the notes come from the GPT plugin for Autodesk [S166](S166-note-icm-notes-from-gpt-plugin.md): AI-written text. Its facts about ICM are reported from Autodesk's 2027 online help, linked in the note, and were not checked here against ICM or the help pages. Its procedure is a test design that has not been run. Every claim below is flagged accordingly: AI-written passage, not checked against ICM.

**Claims worth keeping** (as the note states them; AI-written, not checked against ICM)
- Autodesk documents the bank calculation as a segmented irregular weir with forward and reverse modes; bank crest, adjoining mesh elevations and the water levels on each side decide when a segment flows.
- The run option `Adjust bank levels based on adjacent element ground levels` can raise low bank sections to the adjoining mesh elevation.
- Test: drive one hydrograph past the bank crest and back; record river stage, floodplain stage and signed bank discharge; test return flow; compare time of first spill and exchange volume under a local mesh refinement.
- Validation error E10553 during clip meshing points at bank geometry incompatible with the 2D mesh between two vertices.

**Feeds:** [ICM 2D: boundaries and 1D-2D exchange](../concepts/icm-2d-boundaries-and-exchange.md).
