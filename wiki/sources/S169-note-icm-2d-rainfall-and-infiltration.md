---
title: "S169: note, assign rainfall and infiltration explicitly where ICM domains overlap"
type: source
raw: raw/notes/icm-2d-rainfall-and-infiltration.md
kind: note
author: Robert Dickinson
published: 2026-11-16
ingested: 2026-11-16
tags: [icm, 2d, rainfall, infiltration, curve-number, note]
drafted_by: GPT plugin for Autodesk (an AI), per S166
reviewed: no
---
**What it is.** A note on direct rainfall and infiltration on an ICM 2D mesh where subcatchments overlap it. Raw file: [raw/notes/icm-2d-rainfall-and-infiltration.md](../../raw/notes/icm-2d-rainfall-and-infiltration.md).

**How it was written.** One of ten notes Bob supplied on 16 November 2026 in `ICM-2D-Modeling-Notes.zip`, copied into `raw/notes/` unchanged, on the note template, dated 2026-11-16, status seed. Bob says the notes come from the GPT plugin for Autodesk [S166](S166-note-icm-notes-from-gpt-plugin.md): AI-written text. Its facts about ICM are reported from Autodesk's 2027 online help, linked in the note, and were not checked here against ICM or the help pages. Its procedure is a test design that has not been run. Every claim below is flagged accordingly: AI-written passage, not checked against ICM.

**Claims worth keeping** (as the note states them; AI-written, not checked against ICM)
- InfoWorks can apply a rainfall event to subcatchments and directly to 2D mesh elements; with direct mesh rainfall enabled, overlapping areas can receive rainfall in both domains.
- The 2D zone setting `outside subcatchments` excludes the overlap from direct mesh rainfall; rainfall percentages are set on the 2D zone and on infiltration zones.
- An Infiltration Surface (2D) is assigned to the zone or to an Infiltration Zone (2D). For CNSWMM, record Curve Number, initial abstraction factor and drying time.
- Test: a closed flat zone with no infiltration, then one with an infiltration surface; with no boundary flow or evaporation, applied rain should equal final surface storage plus infiltrated volume.
- It points to Bob's 2023 Curve Number approximation article and his 2025.1 CNSWMM article as the history.

**Feeds:** [ICM 2D: rainfall and infiltration on the mesh](../concepts/icm-2d-rainfall-and-infiltration.md).
