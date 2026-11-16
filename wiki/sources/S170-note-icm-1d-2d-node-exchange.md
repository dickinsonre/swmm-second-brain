---
title: "S170: note, the ICM node flood type sets the 1D-2D exchange relation"
type: source
raw: raw/notes/icm-1d-2d-node-exchange.md
kind: note
author: Robert Dickinson
published: 2026-11-16
ingested: 2026-11-16
tags: [icm, 2d, 1d-2d, manholes, note]
drafted_by: GPT plugin for Autodesk (an AI), per S166
reviewed: no
---
**What it is.** A note on how an InfoWorks manhole exchanges water with the 2D mesh. Raw file: [raw/notes/icm-1d-2d-node-exchange.md](../../raw/notes/icm-1d-2d-node-exchange.md).

**How it was written.** One of ten notes Bob supplied on 16 November 2026 in `ICM-2D-Modeling-Notes.zip`, copied into `raw/notes/` unchanged, on the note template, dated 2026-11-16, status seed. Bob says the notes come from the GPT plugin for Autodesk [S166](S166-note-icm-notes-from-gpt-plugin.md): AI-written text. Its facts about ICM are reported from Autodesk's 2027 online help, linked in the note, and were not checked here against ICM or the help pages. Its procedure is a test design that has not been run. Every claim below is flagged accordingly: AI-written passage, not checked against ICM.

**Claims worth keeping** (as the note states them; AI-written, not checked against ICM)
- Flood type 2D: a weir relation, with the node ground level as the crest and the shaft circumference as its length.
- Gully 2D: a user-specified head-discharge relationship. Inlet 2D: user-specified inlet parameters.
- Autodesk lists Outfall 2D and Connect 2D as further node types, with their own connection rules.
- Test: one manhole and a small receiving depression; drive the sewer head above the opening, then lower it while the surface holds water; plot both levels and the exchange flow on one time axis; a second run raises the cover above the terrain to test the elevation linkage setting.
- Warning 1053 means one or more nodes had their flow from the 2D zone limited; identify the nodes and record the warning and limited flow with the run.

**Feeds:** [ICM 2D: boundaries and 1D-2D exchange](../concepts/icm-2d-boundaries-and-exchange.md).
