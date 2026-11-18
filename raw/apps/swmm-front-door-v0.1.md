---
name: SWMM Front Door
file: swmm-front-door.html
version: "0.1"
date: 2026-11-09
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/MPAcBnRDgNMZzCk25VuiWF", repo: none}
engines: none (a design sketch; its numbers were copied from earlier engine runs and nothing runs in the page)
units: US customary (cfs, ft)
ai_use: "This summary was written by Claude (Anthropic) from the published design. The design says it was designed and built with Claude under Bob Dickinson's direction. See AI use."
written_from: "the published Claude Design artifact https://claude.ai/artifact/MPAcBnRDgNMZzCk25VuiWF, version 1794261785-8341, its one board project/Main.dc.html (21,286 bytes) read as source on 2026-11-18. The Netlify page beside this file was converted from that board by Claude on 2026-11-18. Nothing was run to write this file."
---

# SWMM Front Door: one page that asks what you want to do with a SWMM model

## In three points
- **What:** A clickable sketch, labelled "v0.1 sketch", of a front door for One SWMM: "Run, compare, check and explain SWMM5, SWMM6 and ICM results in one place." It asks "What do you want to do?" and offers four doors (Run my model, Compare engines, Is it stable?, Explain this number), each answered for EPA's Example1.inp, with a Simple or Expert switch that opens drawers naming the tool call behind each answer.
- **So what:** The compare door shows what the full app should do when engines disagree. On Example 1, SWMM6 alpha.4 dynamic wave agrees with SWMM 5.2.4 (peak flow in C11 73.76 against 73.90 cfs, 0.19% apart), while SWMM6 alpha.4 finite volume does not (deepest water at J1 0.24 ft against 0.72 ft), so the sketch shows no green check. ICM results come in as an imported CSV, labelled "imported".
- **Now what:** Use it to judge the layout and the wording before the app is built. It is a design: the Open .inp and Import buttons do nothing, the theme, help, GIF and Export buttons are drawn but not wired, and every number is fixed text copied from Seven SWMM Engines runs of EPA Example 1 on 28 October 2026.

This summary was written after the fact. The design ships no technical summary of its own. Its version is the design's own label ("v0.1 sketch"); the date above is when this version was published, and the run date is the design's own. The file name above is ours. Every number below is copied from the design. Nothing was run to write this file.

## What it shows

- Run my model: "Finished in EPA SWMM 5.2.4, no errors." Runoff continuity off by 0.11%, flow routing by 0.01%. Peak flow in C11 73.9 cfs at hour 12.18; deepest at J1 0.72 ft at hour 12.08; time step 4.99 s average, smallest 3.86 s. Expert: the call swmm.run, the results kit, and the engine (EPA SWMM 5.2.4 compiled to WebAssembly, sha256 4602e507…, run in the browser).
- Compare engines: the table above, an alert "These don't agree yet", and a note that ICM does not run in a browser. Expert: swmm.diff then swmm.certify with the tolerance |a−b| ≤ abs + rel·max(|a|,|b|); eight certificate gates; expected differences ED-1 to ED-8; seven engines pinned by sha256 (EPA SWMM 5.2.4, OpenSWMM 6 alpha.1 to alpha.4, SWMM 4.4H, EXTRAN III).
- Is it stable?: "No warning signs in what was checked", with the caution that "stable" means no problem was found in the evidence, not a proof. Expert: swmm.diagnose, and "insufficient evidence" when a report has no continuity block.
- Explain this number: where 73.9 cfs comes from (the Link Flow Summary, checked at every 5 s routing step, so it can exceed any value in the 5-minute results file). Expert: swmm.explain and swmm.series, and a link to the room in the SWMM5 Code House that computes it.

## What this does not show

As the design states: engines agreeing is not the same as either being right; ICM is never run, only read. It is a sketch: no file is opened and no engine runs.

## Credits and licenses

EPA SWMM 5.2.4 and its Example 1; OpenSWMM 6 (HydroCouple); the Seven SWMM Engines runs the numbers come from. No license is stated for the design.

## AI use

The design says: "Designed and built with Claude (Anthropic) under Bob Dickinson's direction. Numbers above are from Seven SWMM Engines runs of EPA Example 1, 28 October 2026." The Netlify copy was converted from the Design artifact by Claude on 18 November 2026 with a small script that stands in for the design tool's runtime. This summary was written by Claude on 18 November 2026.

## Changes

- 0.1 (2026-11-09): the sketch (the version read).
