---
title: "S176: note, three small ICM 2D cases isolate rain, exchange and barrier alignment"
type: source
raw: raw/notes/icm-2d-benchmark-cases.md
kind: note
author: Robert Dickinson
published: 2026-11-16
ingested: 2026-11-16
tags: [icm, 2d, benchmark, note]
reviewed: no
---
**What it is.** Three test designs for ICM 2D, for what the note calls the ICM Lab Canon. Raw file: [raw/notes/icm-2d-benchmark-cases.md](../../raw/notes/icm-2d-benchmark-cases.md).

**How it was written.** One of ten notes Bob supplied on 16 November 2026 in `ICM-2D-Modeling-Notes.zip`, copied into `raw/notes/` unchanged, on the note template, dated 2026-11-16, status seed. Bob says the notes come from the GPT plugin for Autodesk [S166](S166-note-icm-notes-from-gpt-plugin.md): AI-written text. Its facts about ICM are reported from Autodesk's 2027 online help, linked in the note, and were not checked here against ICM or the help pages. Its procedure is a test design that has not been run. Every claim below is flagged accordingly: AI-written passage, not checked against ICM.

**Claims worth keeping** (as the note states them; AI-written, not checked against ICM)
- Case 1, closed rainfall box: a flat, dry 100 ft by 100 ft zone with Vertical Wall boundaries, 1.00 in of rain over one hour, no infiltration or evaporation, `Ignore rain falling on dry elements` unchecked. Expected storage for exactly 10,000 sq ft: 833.33 cu ft, a mean depth of 1.00 in. Record the residual against the actual meshed area.
- Case 2, reversing manhole: one 1D node and a small surface depression; raise the sewer head above the opening, then lower it while water remains; read the signed exchange hydrograph.
- Case 3, embankment with a gap: one opening in a raised feature, a short pulse on one side, the mesh configurations of the subgrid note; read transects through the gap and across intact crest.
- These are test designs; set acceptance criteria before running.

**Feeds:** [ICM 2D: three benchmark cases](../concepts/icm-2d-benchmark-cases.md).
