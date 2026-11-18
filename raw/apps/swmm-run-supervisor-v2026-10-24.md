---
name: SWMM Run Supervisor
file: swmm-run-supervisor.html
version: 2026-10-24
date: 2026-10-24
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/HnsApQERR8wDNwFtgN4rti", repo: none named in the page}
engines:
  - {name: EPA SWMM, version: 5.2.4, source: "Emscripten 3.1.51 build from dickinsonre/BatchSWMMRunner, hash-checked in the page", license: public domain}
units: US customary (ft)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says Claude wrote all of the app's code and text for Robert Dickinson, and that Claude is a live participant only in Claude mode. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/HnsApQERR8wDNwFtgN4rti, version 1792821210-3e6e (index.html, 1,426,231 bytes, SHA-256 e014edc5282c543449db09d52c3126d84e7b41ea866128af7bf9946d2009f641), its About and Doc tabs read in headless Chromium on 2026-11-17. No model was run to write this file; the version is the artifact's publish date."
---

# SWMM Run Supervisor: a supervisor that picks the SWMM solver settings window by window

## In three points
- **What:** EPA SWMM 5.2.4 in WebAssembly, cut into 15-minute windows joined by hot-start files; after each window a supervisor (Claude, rules, a fixed preset, or a replay) picks how hard the solver works in the next, and every run is scored against an all-careful dynamic-wave run.
- **So what:** Run as shipped the test model looks healthy (continuity 0.829%, 9,974 routing steps, 11.5% of a fixed 1 s step's cost), yet only 143 of 164 peak depths agree within 0.1 ft of the careful run; the 96-window restart floor itself is 0.045 ft rms.
- **Now what:** Use it to see what solver settings cost and where they matter in a storm. The rules were written with hindsight on one storm, no live Claude run is quoted, and Claude mode needs the claude.ai viewer (it is unavailable on an ordinary web host).

This summary was written after the fact. The page ships no technical summary and no version number of its own, so the version above is the artifact's publish date. The file name above is ours. Every number below is copied from the page. No model was run to write this file.

## What it does

Every SWMM run fixes its routing step, Courant factor, head tolerance and trial limit for the whole storm. Bob asked whether a language model could sit in the engine room during the run. The page reads each window's results, sums up hot spots, and the supervisor picks the next preset; in Claude mode, Claude sees one window's hot-spot summary, the rain forecast from the model's own series and a structural briefing, returns preset choices for up to eight windows plus wake-up conditions, and never sees the reference or edits the model. Claude is asked only when a person presses the button. Tabs: Run, Log, Compare, Model, Doc, About.

## Results the page reports

- Restart floor (all 96 windows at the careful preset against the unbroken careful run): node depth series differ by 0.045 ft rms; 158 of 164 node peaks within 0.1 ft, worst 0.51 ft at node 136; flooding +0.86%.
- Two hot-start seams were found and fixed (one missing flag made the first runoff step after a restart a dry step, giving 1% too much runoff).
- As shipped: continuity 0.829%, 9,974 routing steps (11.5% of a fixed 1 s step); 143 of 164 peak depths within 0.1 ft of the careful run; worst at JCT-138.
- The careful reference's own force-main peak moves 4.7 ft between a 1 s and a 0.9 s step.

## What this does not show

- That Claude beats the rules: the rules were written with hindsight on this storm, and no live Claude run is quoted; a stand-in planner proves the path works.
- Per-element solver choice: SWMM 5.2.4 options are global; Claude's watch list is recorded, not applied.
- That the careful run is right.
- Speed: wall time includes 96 engine restarts; the scoreboard counts routing steps.
- On Netlify or any ordinary host, Claude mode is unavailable; rules, fixed presets and replays still run.

## How to reproduce

Open the page, choose a supervisor on Run, and compare with the reference on Compare; Log records each window's choice.

## Credits and licenses

EPA SWMM 5.2.4 (public domain), build from dickinsonre/BatchSWMMRunner. No license is stated for the page.

## AI use

The page says Claude (Anthropic) wrote all of the app's code and text for Robert Dickinson: the segmenting, hot-start handling, hot-spot summaries, rules, prompt, charts, essay and page; it also found the two hot-start seams and measured every number quoted. Robert set the goal and the standards. Inside the app, Claude is a live participant only in Claude mode. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 2026-10-24: the version read.
