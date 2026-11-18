---
title: "S307: SWMM Front Door, summary written from the page (v0.1)"
type: source
raw: raw/apps/swmm-front-door-v0.1.md
kind: app-md
author: Robert Dickinson
published: 2026-11-09
ingested: 2026-11-18
tags: [designs, swmm5, swmm6, icm, one-swmm]
drafted_by: Claude (Anthropic), from the published page
reviewed: 2026-11-18
---
**What it is.** A technical summary of the design sketch SWMM Front Door, version 0.1: one page that asks what you want to do with a SWMM model. Raw file: [raw/apps/swmm-front-door-v0.1.md](../../raw/apps/swmm-front-door-v0.1.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude Design artifact https://claude.ai/artifact/MPAcBnRDgNMZzCk25VuiWF, version 1794261785-8341, its one board project/Main.dc.html (21,286 bytes) read as source on 2026-11-18. The Netlify page beside this file was converted from that board by Claude on 2026-11-18. Nothing was run to write this file." Its AI-use section: "The design says: "Designed and built with Claude (Anthropic) under Bob Dickinson's direction. Numbers above are from Seven SWMM Engines runs of EPA Example 1, 28 October 2026." The Netlify copy was converted from the Design artifact by Claude on 18 November 2026 with a small script that stands in for the design tool's runtime. This summary was written by Claude on 18 November 2026."

**Claims worth keeping** (all copied from the file)
- A clickable sketch, labelled "v0.1 sketch", of a front door for One SWMM: "Run, compare, check and explain SWMM5, SWMM6 and ICM results in one place." It asks "What do you want to do?" and offers four doors (Run my model, Compare engines, Is it stable?, Explain this number), each answered for EPA's Example1.inp, with a Simple or Expert switch that opens drawers naming the tool call behind each answer.
- The compare door shows what the full app should do when engines disagree. On Example 1, SWMM6 alpha.4 dynamic wave agrees with SWMM 5.2.4 (peak flow in C11 73.76 against 73.90 cfs, 0.19% apart), while SWMM6 alpha.4 finite volume does not (deepest water at J1 0.24 ft against 0.72 ft), so the sketch shows no green check. ICM results come in as an imported CSV, labelled "imported".

**Limits it states.** As the design states: engines agreeing is not the same as either being right; ICM is never run, only read. It is a sketch: no file is opened and no engine runs.

**Checked at ingest.** A Claude Design artifact, converted to a standalone page for Netlify with a small script standing in for the design tool's runtime; its numbers are fixed text. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [SWMM Front Door (sketch)](../entities/swmm-front-door.md), [Apps summarized on 18 November 2026: SWMM6, SWMM5+ and solvers](../concepts/apps-from-pages-swmm6-solvers-and-swmm5plus.md), [One SWMM (app)](../entities/one-swmm.md), [Seven SWMM Engines (app)](../entities/seven-swmm-engines.md), [OpenSWMM 6 and HydroCouple](../entities/openswmm-6-and-hydrocouple.md).
