---
title: "S162: note, look up the ICM network type before choosing Ruby table and field names"
type: source
raw: raw/notes/icm-network-tables-and-fields.md
kind: note
author: not stated (supplied by Robert Dickinson)
published: 2026-11-16
ingested: 2026-11-16
tags: [icm, ruby, data-model, note]
reviewed: no
---
**What it is.** A note on finding the right table and field names for an ICM Ruby script, written for a Smart Table Exporter (the note's name for the script). Raw file: [raw/notes/icm-network-tables-and-fields.md](../../raw/notes/icm-network-tables-and-fields.md).

**How it was written.** One of seven notes Bob supplied on 16 November 2026 in `ICM-Ruby-SWMM-Markdown.zip`, copied into `raw/notes/` unchanged. It is on the note template, dated 2026-11-16, status seed. The note does not say who wrote it. The set refers to Bob in the third person and addresses "you", so it was not typed by Bob in his own voice; whether an AI wrote it is not stated (Q89). Its facts about ICM come from Autodesk's online help, linked in the note, and were not checked here against ICM or the help pages. Its procedure says it awaits a run in ICM: nothing in it has been run.

**Claims worth keeping** (as the note states them; Autodesk's facts are reported, not checked)
- InfoWorks and SWMM networks use different model data tables. Node: `hw_node` and `sw_node`. Conduit: `hw_conduit` and `sw_conduit`. Subcatchment: `hw_subcatchment` and `sw_subcatchment`.
- Autodesk's Network Data Fields index pairs each object type with its table and a detailed field reference.
- Identify the network type first, then resolve the exact database field for that table; keep the interface's label next to the database field so an exported column can be traced back to GeoPlan.
- For each exported value keep the network type, table, object ID, database field and unit; record a field missing from one network type as unavailable.
- It links Autodesk's open Ruby database reference and database fields guide on GitHub (`innovyze/Open-Source-Support`).

**Feeds:** [ICM network tables and result fields](../concepts/icm-tables-and-result-fields.md), [InfoWorks ICM](../entities/infoworks-icm.md).
