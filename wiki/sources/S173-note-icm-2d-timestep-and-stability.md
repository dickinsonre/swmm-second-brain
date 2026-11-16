---
title: "S173: note, test ICM 2D time stepping with a fixed mesh and event"
type: source
raw: raw/notes/icm-2d-timestep-and-stability.md
kind: note
author: Robert Dickinson
published: 2026-11-16
ingested: 2026-11-16
tags: [icm, 2d, timestep, stability, note]
drafted_by: GPT plugin for Autodesk (an AI), per S166
reviewed: no
---
**What it is.** A note on the time step settings of an ICM 2D run. Raw file: [raw/notes/icm-2d-timestep-and-stability.md](../../raw/notes/icm-2d-timestep-and-stability.md).

**How it was written.** One of ten notes Bob supplied on 16 November 2026 in `ICM-2D-Modeling-Notes.zip`, copied into `raw/notes/` unchanged, on the note template, dated 2026-11-16, status seed. Bob says the notes come from the GPT plugin for Autodesk [S166](S166-note-icm-notes-from-gpt-plugin.md): AI-written text. Its facts about ICM are reported from Autodesk's 2027 online help, linked in the note, and were not checked here against ICM or the help pages. Its procedure is a test design that has not been run. Every claim below is flagged accordingly: AI-written passage, not checked against ICM.

**Claims worth keeping** (as the note states them; AI-written, not checked against ICM)
- Record the run timestep, the 1D-2D coupling options, the 2D stability control and the reporting interval separately.
- In the InfoWorks 2D Parameters dialog, Timestep Stability Control sets the CFL bound the 2D engine uses for internal stepping; the same dialog has an option to link 1D and 2D calculations at minor timesteps, and thresholds for depth and momentum.
- Test: one case with a wetting front, bank spill or reversing manhole; repeat with a smaller run timestep at the same reporting interval; test the minor-timestep coupling in a separate run; test a mesh change in a separate comparison; record whether the result and the warning changed together.
- Keep the depth threshold, momentum threshold and any velocity limit in the run record.

**Feeds:** [ICM 2D: timestep, volume balance and results](../concepts/icm-2d-runs-and-checks.md).
