---
name: SWMM Rooms
file: swmm-rooms.html
version: "1.4"
date: 2026-10-20
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/WpawfdPqdgBj7TBMNicVP3", repo: none named in the page}
engines: none (a map of features; nothing runs)
units: none
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says Claude built the app under Robert Dickinson's direction and that he edited the room and pipe records. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/WpawfdPqdgBj7TBMNicVP3, version 1792448311-3401 (index.html, 170,296 bytes, SHA-256 f7b4b15de40b85ec95b1ce84b9240db749cb73f5bc8af2e826c46227c769c253), its Map and Doc tabs read in headless Chromium on 2026-11-17. Nothing was run to write this file."
---

# SWMM Rooms: 36 rooms of SWMM5, OpenSWMM 6 and HydroCouple, with a keeper in every room

## In three points
- **What:** An isometric building of 36 rooms, each one feature of EPA SWMM 5.2, OpenSWMM 6 or the HydroCouple component framework, with its input keywords, a plain description, a pipe to every feature it feeds, a provenance note, and a keeper who walks you through.
- **So what:** It uses the old method of loci: features in rooms in order are easier to remember than a list, and deciding the rooms forces each feature and its 56 pipes to be stated.
- **Now what:** Use it to learn or teach how the features connect. Nothing runs here, and the pipes are an author's reading, not a call graph from the source.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("v1.4 · 2026-10-20"). The file name above is the one Bob uses. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Wings: SWMM5 hydrology, SWMM5 hydraulics, SWMM5 analysis and API, SWMM6 dynamic wave, SWMM6 + HydroCouple, tooling and components. Controls: Walk the rooms, Speak, Flow, filters by family, search, CSV and GIF export. The isometric projection paints rooms in order of row plus column, which gives correct occlusion with no depth test.

## Checks (as stated on the page)

- The room and pipe arrays were extracted from the published page and every count, degree, cycle and keyword tally in the Doc's figures was computed from them. Example: kind 'w' occurs only on SWMM5-to-SWMM5 pipes (25 of 25).

## What this does not show

- Nothing runs: no engine, no input file, no results.
- The 56 pipes are an author's reading, not a call graph, data-flow analysis or compiler output.
- A room's claim (for example about Anderson acceleration) tells you what somebody read in the source, not a demonstration.

## How to reproduce

Open the page; Walk the rooms takes the tour; Export CSV writes the rooms and pipes.

## Credits and licenses

EPA SWMM 5.2, OpenSWMM 6 and HydroCouple, described. No license is stated for the page.

## AI use

The page says Robert (Bob) Dickinson directed the work and is responsible for it: he chose the subject, decided which features deserved rooms and which wing each belongs to, set the standard that a measured claim and a README claim must look different, and reviewed the result. Claude, Anthropic's AI model, built the app in Claude Code sessions in September 2026 (the projection and renderer, the 36 glyphs, the keeper and tour, the controls, the exports, and the room and pipe records, drafted from Bob's engine work and source readings and then edited by him); in October 2026 Claude wrote the Doc, its eight figures and the Word and PDF versions. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 1.4 (2026-10-20): the version read; earlier versions in September 2026 grew from 25 to 36 rooms.
