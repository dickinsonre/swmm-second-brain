---
title: "S168: note, give each ICM 2D boundary segment a physical purpose"
type: source
raw: raw/notes/icm-2d-boundary-conditions.md
kind: note
author: Robert Dickinson
published: 2026-11-16
ingested: 2026-11-16
tags: [icm, 2d, boundary-conditions, note]
reviewed: no
---
**What it is.** A note on ICM 2D zone boundary types. Raw file: [raw/notes/icm-2d-boundary-conditions.md](../../raw/notes/icm-2d-boundary-conditions.md).

**How it was written.** One of ten notes Bob supplied on 16 November 2026 in `ICM-2D-Modeling-Notes.zip`, copied into `raw/notes/` unchanged, on the note template, dated 2026-11-16, status seed. Bob says the notes come from the GPT plugin for Autodesk [S166](S166-note-icm-notes-from-gpt-plugin.md): AI-written text. Its facts about ICM are reported from Autodesk's 2027 online help, linked in the note, and were not checked here against ICM or the help pages. Its procedure is a test design that has not been run. Every claim below is flagged accordingly: AI-written passage, not checked against ICM.

**Claims worth keeping** (as the note states them; AI-written, not checked against ICM)
- The 2D zone has a default boundary condition; a 2D Boundary line can assign a different one along part of the edge.
- Six types: Vertical Wall (closed); Critical Depth (outward flow when the 2D level is above the face, by the documented weir calculation); Supercritical; Normal Depth; Inflow (flow from a matching profile in an Inflow Event); Level (stage from a matching profile in a Level Event).
- Keep an inventory per edge: type, length, connected faces, ground levels, event profile, expected flow direction.
- Test: a small sloping zone with three closed edges and one outlet, a known inflow, and a comparison of downstream stage, outlet hydrograph and net boundary volume; if the outlet type changes interior results materially, document the sensitivity.

**Feeds:** [ICM 2D: boundaries and 1D-2D exchange](../concepts/icm-2d-boundaries-and-exchange.md).
