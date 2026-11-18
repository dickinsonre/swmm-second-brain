---
name: SWMM Hydraulic Library
file: swmm-hydraulic-library.html
version: "2.0"
date: 2026-10-21
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/TdqpXe77kA4VN2FK7MCGkq", repo: none named in the page}
engines: none (library entries, diagrams and calculators in JavaScript)
units: US customary
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says Bob built the original in Lovable and version 2.0 was rebuilt with Claude under his direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/TdqpXe77kA4VN2FK7MCGkq, version 1792597788-50a9 (index.html, 2,992,174 bytes, SHA-256 4890201d7cec9bd35cd5d60e01caa81f7c4027dbb6511681768f91aa600c1cc6), its About and Doc tabs read in headless Chromium on 2026-11-17. Nothing was run to write this file."
---

# SWMM Hydraulic Library: how SWMM5, InfoWorks ICM and SWMM6 solve the Saint-Venant equations

## In three points
- **What:** 70 library entries, each an equation with a SWMM 5, ICM and SWMM 6 note, and 119 interactive diagrams and calculators from Bob's SWMM-ICM-StVenant project, rebuilt from his Lovable app into one file that runs from disk, Netlify or a Claude artifact.
- **So what:** Eight audits read all 26 diagram files, the 70 entries and the benchmark page and fixed 199 defects (units errors the commonest), flagged 114 more without changing them, and swept 197 pages headless with 0 console errors after.
- **Now what:** Use it to see, one slider at a time, where the three engines keep their unknowns and what each does when the arithmetic fails. Ask AI needs your own Anthropic API key outside the Claude artifact.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("VERSION 2.0 · 21 OCTOBER 2026"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

The physics is Saint-Venant's (1871): mass and momentum. The disagreement among EPA SWMM 5, InfoWorks ICM and SWMM 6 (with its finite-volume engine beside the inherited dynamic wave) is arithmetic: where each keeps its unknowns, when it evaluates them, and what it does when the arithmetic fails. The library holds 70 short entries and 119 interactive diagrams and calculators, each diagram one React component in one of 26 files. Views include Sewer scenario (a three-pipe scenario that computes normal depths exactly), Overview, Browse, FV vs DYNWAVE, Diagrams, Builder, About and Doc. Entries and diagrams are linked when they share words.

## What changed from the Lovable original (as the page lists it)

- One file, no server: TanStack Start, server routes, Supabase and the Lovable sign-in removed; routing uses the URL hash.
- Saving: scenarios and custom diagrams go to the artifact's shared store inside a Claude artifact, otherwise to the browser; Builder exports and imports the library as JSON.
- Ask AI: the original sent questions to an OpenAI model through Lovable's gateway; now Claude answers, inside a Claude artifact on the viewer's own account, anywhere else with the viewer's own Anthropic API key kept in memory only (the page sends it only to api.anthropic.com).
- Added: Dark | Light | Auto (dark default), a drawing-sheet switch on every diagram, a welcome screen, a tour, a GIF recorder and exports.

## Checks (as stated on the page)

- 199 defects fixed, 114 flagged and not changed, 197 pages swept headless, 0 console errors after.
- Eight audits, seven in parallel sub-agents.

## What this does not show

- No engine runs; the diagrams and calculators are teaching models.
- On Netlify, Ask AI and shared saving fall back to the viewer's own API key and this browser.

## How to reproduce

Open the page; Builder exports the library as JSON.

## Credits and licenses

Bob's SWMM-ICM-StVenant project (the diagrams); the OpenSWMM reference manual (cited at swmm6_rel @ fbd1d7b0). No license is stated for the page.

## AI use

The page says version 2.0 was rebuilt with Claude, Anthropic's AI model, in a Claude session on 21 October 2026, under the direction of Robert (Bob) Dickinson, who built the original in Lovable, supplied its source, and asked for a fixed single-file version. Claude ported the app to one client-only file, replaced the server, sign-in and AI gateway, added the tour, the GIF recorder, the exports, the page and the essay, ran eight audits and made the 199 fixes. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 2.0 (2026-10-21): single-file rebuild of the Lovable app, with the fixes above.
- 1.x: the Lovable original.
