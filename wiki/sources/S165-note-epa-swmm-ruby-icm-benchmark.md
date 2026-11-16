---
title: "S165: note, a two-pipe benchmark to separate engine differences from conversion differences"
type: source
raw: raw/notes/epa-swmm-ruby-icm-benchmark.md
kind: note
author: Robert Dickinson
published: 2026-11-16
ingested: 2026-11-16
tags: [icm, swmm5, ruby, benchmark, comparison, note]
drafted_by: ChatGPT (OpenAI), from Autodesk Help, per S179
reviewed: no
---
**What it is.** A test design: one tiny model run in EPA SWMM 5.2.4, the Ruby translation, ICM SWMM and ICM InfoWorks. Raw file: [raw/notes/epa-swmm-ruby-icm-benchmark.md](../../raw/notes/epa-swmm-ruby-icm-benchmark.md).

**How it was written.** One of seven notes Bob supplied on 16 November 2026 in `ICM-Ruby-SWMM-Markdown.zip`, copied into `raw/notes/` unchanged (byte for byte, checked against the ZIP [S179](S179-note-icm-notes-drafted-by-chatgpt.md)). It is on the note template, dated 2026-11-16, status seed. The note does not name its author. It was drafted by ChatGPT from Autodesk Help [S179](S179-note-icm-notes-drafted-by-chatgpt.md), so it is AI-written text; Bob adds them from the GPT plugin for Autodesk he uses [S166](S166-note-icm-notes-from-gpt-plugin.md). Its facts about ICM come from Autodesk's online help, linked in the note, and were not checked here against ICM or the help pages. Its procedure says it awaits a run in ICM: nothing in it has been run.

**Claims worth keeping** (as the note states them; AI-written, not checked against ICM)
- The model: two junctions and a free outfall at inverts of 100, 99 and 98 ft; junction rims 5 ft above invert; two circular conduits, 200 ft long and 12 in in diameter, Manning's n 0.013, zero offsets; dry start; one hour; results every 1 min.
- Inflow at the first junction: 0.0 ft³/s at 0 min, 0.5 at 10, 1.0 at 20, 0.0 at 30 and at 60.
- Step 1: run the same `.inp` in pinned EPA 5.2.4 and `swmm5-ruby` and compare `.out` and `.rpt` by the Ruby port's gate.
- Step 2: import and run in ICM SWMM, keeping its log and engine input; check offsets, inflow interpolation and output intervals.
- Step 3: map to ICM InfoWorks; check geometry, boundary, initial state and inflow; record each engine's hydraulic step.
- Step 4: compare outfall peak flow, peak time, volume and continuity error, and plot outfall flow and upstream level on a common time grid, with the acceptable differences agreed before running.
- It links Q16 of this wiki. The note calls itself "a test design awaiting runs".

**Feeds:** [Checking a SWMM5 model's conversion into ICM](../concepts/swmm5-to-icm-conversion-checks.md), [SWMM5 language translations](../entities/swmm5-language-ports.md), [Open questions](../open-questions.md).
