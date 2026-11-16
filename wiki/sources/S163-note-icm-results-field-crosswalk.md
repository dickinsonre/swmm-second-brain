---
title: "S163: note, compare node level and node depth on the same reference elevation"
type: source
raw: raw/notes/icm-results-field-crosswalk.md
kind: note
author: not stated (supplied by Robert Dickinson)
published: 2026-11-16
ingested: 2026-11-16
tags: [icm, results, comparison, note]
reviewed: no
---
**What it is.** A note on matching node results between ICM's two network types. Raw file: [raw/notes/icm-results-field-crosswalk.md](../../raw/notes/icm-results-field-crosswalk.md).

**How it was written.** One of seven notes Bob supplied on 16 November 2026 in `ICM-Ruby-SWMM-Markdown.zip`, copied into `raw/notes/` unchanged. It is on the note template, dated 2026-11-16, status seed. The note does not say who wrote it. The set refers to Bob in the third person and addresses "you", so it was not typed by Bob in his own voice; whether an AI wrote it is not stated (Q89). Its facts about ICM come from Autodesk's online help, linked in the note, and were not checked here against ICM or the help pages. Its procedure says it awaits a run in ICM: nothing in it has been run.

**Claims worth keeping** (as the note states them; Autodesk's facts are reported, not checked)
- Autodesk labels `DEPNOD` as level at the current timestep in an InfoWorks network.
- ICM SWMM documents `HEAD` as hydraulic head elevation and `DEPTH` as water depth above the node inlet elevation.
- So InfoWorks `DEPNOD` compares with ICM SWMM `HEAD` on a common vertical datum, and an InfoWorks depth has to be computed from level and the inlet elevation before it compares with `DEPTH`.
- Worked example: a node with an inlet at 106.00 ft and a level of 109.25 ft has a depth of 3.25 ft.
- Record quantity, unit, reference elevation, and whether the value is a time series or a summary; record the flow sign convention before comparing link flows or runoff.

**Feeds:** [ICM network tables and result fields](../concepts/icm-tables-and-result-fields.md), [SWMM 5 versus ICM InfoWorks](../concepts/swmm5-versus-icm-infoworks.md).
