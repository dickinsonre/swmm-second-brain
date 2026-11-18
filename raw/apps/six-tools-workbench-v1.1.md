---
name: Six Tools Workbench
file: six-tools-workbench.html
version: "1.1"
date: 2026-10-11
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/SKg2Ac3uNGGnfnxuw8EpJU", repo: none named in the page}
engines:
  - {name: none in the page, note: "real-code results are a fixed snapshot measured on 10 and 11 Oct 2026 by swmm-quality-tools (tree-sitter parsers, gcov, a model-based mutation runner)"}
units: none (scores and counts)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The published page carries no AI-use note; it is a Claude artifact on Robert Dickinson's account. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/SKg2Ac3uNGGnfnxuw8EpJU, version 1791651656-f2f7 (index.html, 1,007,353 bytes, SHA-256 83e641ea0c818e94d013e720e880210a480cfc7454556bdb24b3b0c3ecc3c974), every tab read in headless Chromium on 2026-11-17. Nothing was run to write this file."
---

# Six Tools Workbench: Robert C. Martin's agent-built code tools, at toy size and then run on SWMM5, SWMM6 and ICM scripts

## In three points
- **What:** Shows Robert C. Martin's six public agent-built tools (bookwriter, scriptwriter, crapper, mutator, dryer, uml-viewer) at toy size in the browser, then gives results from rebuilt versions of the four code tools run on EPA SWMM 5.2.4, OpenSWMM 6 and Autodesk's public ICM Ruby scripts.
- **So what:** CRAP scores (complexity squared, discounted by coverage cubed), mutation testing with models as the tests, duplicate finding and a component map were measured on the real engine code, and the toolkit that did it (swmm-quality-tools) came out of the session.
- **Now what:** Hand swmm-quality-tools and the page's brief to an agent to rerun the scores on newer code. The toy tabs are miniatures, not his tools, and the real-code results are a fixed snapshot.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("v1.1 · 2026-10-11"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Six tools, Crapper, Mutator, Dryer, UML viewer, Writers, Your brief. His repositories were read on 10 October 2026 at commits bookwriter 236ff41, scriptwriter fa26c24, crapper 9f1bead, mutator c57f038, dryer 66ff6d2 and uml-viewer f65dafe; the scoring rules follow their READMEs and source. The sample project's numbers are measured in the browser, and that engine agreed with a plain Node run of the same modules on every test. The four tool tabs load a JavaScript parser from a CDN. The Writers tab shows a short sample book about one 24 in pipe (at 0.5 percent slope and n = 0.013 it carries 17.2 cfs at 22.5 in deep and 16.0 cfs full).

## Real-code sources (as stated on the page)

EPA SWMM tag v5.2.4 (7952ca8); HydroCouple/openswmm.engine swmm6_rel at a070e98; Innovyze/Open-Source-Support at 58d610e; models from SWMMBobSWMM6/1729-SWMM5-Models-2030 at 70b8f6e. For a simulation engine the tests are models, not unit tests.

## What this does not show

- The sample tabs are miniatures read through a different parser, so Dryer's scores can differ a little from the real tool's.
- The real-code coverage comes from a subset of the corpus (the page gives 3,099 models) and is a fixed snapshot.

## How to reproduce

The page's brief and swmm-quality-tools.zip (from the build session) rerun the measurements.

## Credits and licenses

Robert C. Martin's six public repositories. EPA SWMM (public domain); OpenSWMM (Apache-2.0); Autodesk's Open-Source-Support repository (MIT). No license is stated for the page.

## AI use

The published page carries no AI-use note. It is a Claude artifact on Robert Dickinson's account, built in a claude.ai session. The Netlify copy in this batch adds a one-line AI-use note at the foot of the page. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 1.1 (2026-10-11): the version read.
