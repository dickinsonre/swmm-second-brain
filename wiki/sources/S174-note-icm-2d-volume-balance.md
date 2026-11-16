---
title: "S174: note, check water volume for the 2D domain and the combined ICM model"
type: source
raw: raw/notes/icm-2d-volume-balance.md
kind: note
author: Robert Dickinson
published: 2026-11-16
ingested: 2026-11-16
tags: [icm, 2d, continuity, volume-balance, note]
reviewed: no
---
**What it is.** A note on volume balance for an ICM 2D model. Raw file: [raw/notes/icm-2d-volume-balance.md](../../raw/notes/icm-2d-volume-balance.md).

**How it was written.** One of ten notes Bob supplied on 16 November 2026 in `ICM-2D-Modeling-Notes.zip`, copied into `raw/notes/` unchanged, on the note template, dated 2026-11-16, status seed. Bob says the notes come from the GPT plugin for Autodesk [S166](S166-note-icm-notes-from-gpt-plugin.md): AI-written text. Its facts about ICM are reported from Autodesk's 2027 online help, linked in the note, and were not checked here against ICM or the help pages. Its procedure is a test design that has not been run. Every claim below is flagged accordingly: AI-written passage, not checked against ICM.

**Claims worth keeping** (as the note states them; AI-written, not checked against ICM)
- Balance each control volume over the same interval: residual = starting storage + inputs - outputs - ending storage.
- For the 2D mesh alone, sewer or river exchange crosses its boundary; for the combined 1D and 2D model the same transfer is internal and cancels. Include each transfer once for the domain being checked.
- Terms for the 2D mesh: direct rain, boundary flows, signed transfer with 1D, applied losses, change in surface volume. For the combined model: external inflows, delivered runoff, direct mesh rain, external discharges, external losses, change in combined storage.
- Infiltration routed into 1D through a permeable zone is a transfer in the combined balance.
- Use the PRN volume summary alongside local checks; in a subgrid case, the volume-level table gives element storage.
- If reported and independent volumes disagree, compare time window, units, boundary sign and results used before changing solver controls.

**Feeds:** [ICM 2D: timestep, volume balance and results](../concepts/icm-2d-runs-and-checks.md).
