---
title: "S164: note, a SWMM conversion needs checks for each import and export route"
type: source
raw: raw/notes/swmm-inp-conversion-qa.md
kind: note
author: Robert Dickinson
published: 2026-11-16
ingested: 2026-11-16
tags: [icm, swmm5, conversion, verification, note]
drafted_by: ChatGPT (OpenAI), from Autodesk Help, per S179
reviewed: no
---
**What it is.** A note on checking what survives when a SWMM5 `.inp` is brought into ICM. Raw file: [raw/notes/swmm-inp-conversion-qa.md](../../raw/notes/swmm-inp-conversion-qa.md).

**How it was written.** One of seven notes Bob supplied on 16 November 2026 in `ICM-Ruby-SWMM-Markdown.zip`, copied into `raw/notes/` unchanged (byte for byte, checked against the ZIP [S179](S179-note-icm-notes-drafted-by-chatgpt.md)). It is on the note template, dated 2026-11-16, status seed. The note does not name its author. It was drafted by ChatGPT from Autodesk Help [S179](S179-note-icm-notes-drafted-by-chatgpt.md), so it is AI-written text; Bob adds them from the GPT plugin for Autodesk he uses [S166](S166-note-icm-notes-from-gpt-plugin.md). Its facts about ICM come from Autodesk's online help, linked in the note, and were not checked here against ICM or the help pages. Its procedure says it awaits a run in ICM: nothing in it has been run.

**Claims worth keeping** (as the note states them; AI-written, not checked against ICM)
- Three routes to track separately: EPA SWMM `.inp` to ICM SWMM, `.inp` to ICM InfoWorks, and ICM's own conversion between its network types.
- Autodesk publishes conversion notes for each `.inp` destination and describes partial imports and objects that need extra data for the InfoWorks destination.
- The 2027 conversion pages list importer support through EPA SWMM 5.1.015.
- Check, per route: IDs and topology; units and geometry; options and events; inflows and treatment (DWF patterns, RDII, LID and SuDS, network-specific objects); and results (continuity, peak and timing, volume, one downstream hydrograph). For each feature, record preserved, mapped, omitted or edited by hand.
- Worked example: an upstream node invert of 102.0 ft with a 1.5 ft depth offset implies a link end elevation of 103.5 ft; verify it after conversion.
- For a round trip, compare the source and exported `.inp` sections and run both through the same pinned EPA executable.

**Feeds:** [Checking a SWMM5 model's conversion into ICM](../concepts/swmm5-to-icm-conversion-checks.md), [SWMM 5 versus ICM InfoWorks](../concepts/swmm5-versus-icm-infoworks.md).
