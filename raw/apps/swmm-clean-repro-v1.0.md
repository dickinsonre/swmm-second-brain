---
name: SWMM Clean Repro
file: swmm-clean-repro.html
version: "1.0"
date: 2026-10-13
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/SEj5sGGXi14FwsmEnzrK4Z", repo: none named in the page}
engines:
  - {name: EPA SWMM, version: 5.2.4, source: "tag v5.2.4, commit 7952ca8, compiled to wasm32-wasi, run in a Web Worker with a fresh instance per run", license: public domain}
units: the model's own
ai_use: "This summary was written by Claude (Anthropic) from the published page. The published page carries no AI-use note; it is a Claude artifact on Robert Dickinson's account. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/SEj5sGGXi14FwsmEnzrK4Z, version 1791872997-4291 (index.html, 1,326,054 bytes, SHA-256 04cd23c8c39e4c27019b69e5b1f0d0d23c010444739cf3f654512b30430d0617), every tab read in headless Chromium on 2026-11-17. Nothing was run to write this file; the date is the artifact's publish date."
---

# SWMM Clean Repro: cut out the problem, strip what identifies it, prove it still runs the same

## In three points
- **What:** Takes a SWMM5 model that cannot be shared (for example under a client agreement), cuts out the smallest piece that shows the problem, removes names, comments, paths, coordinates, dates and datum, and runs both versions through EPA SWMM 5.2.4 in the browser to show the answer did not change.
- **So what:** Scrubbing without a cut is bit-for-bit identical on 30 of 30 public test models, because dates move by 28 years within one power-of-two band of SWMM's day count; a careless 28-year shift changed the report periods on 16 of 31 models.
- **Now what:** Use it to share a reproducible problem model with open-source developers. It cannot remove the network's shape, and it does not show the model or the cut-out is right.

This summary was written after the fact. The page ships no technical summary of its own. Its version is the page's own ("v1.0 · EPA 5.2.4 ready"); the date is the artifact's. The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Steps: 1 Model, 2 Cut, 3 Scrub, 4 Verify, 5 Package, About. The file stays in the browser. For a cut, the engine first runs the full model and records boundary levels and flows in the cut pipes every 20 s, which become the cut-out's boundary conditions. The scrub renames every ID in every section (control rules included, case-insensitively as SWMM does), removes title words, comments and paths, moves the map, shifts dates by a multiple of 28 years (same weekday and leap-year pattern), and shifts the elevation datum without changing any conduit's direction. The sample is EPA EXTRAN Example 1 with a fictional city, people, monitor names and coordinates added (the hydraulics unchanged); the page counts 23 object names, 3 title lines, 19 comments, 10 map coordinates, 2 file paths and 4 tags and labels that point back to the owner.

## Checks (as stated on the page)

- Scrub without a cut: bit-for-bit identical on 30 of 30 public test models.
- A careless date shift into a different power-of-two band changed the number of report periods on 16 of 31 models; the tool offers only shifts that stay in the band.
- Datum shift with the tool's choice: identical on 26 of 30 models; the others are metric (SWMM divides by 0.3048 on input) or span several bands; the largest effect was 1.15% of a link's peak at one instant.
- The output is checked for original names, comments, paths, title words and coordinates.

## What this does not show

- That the model is right, or that the cut-out answers every question the full model does.
- That a determined person who knows the system could not recognise its shape: it removes names and offsets, not the network itself.

## How to reproduce

Open the page, load a model or the sample, and step through Cut, Scrub, Verify and Package.

## Credits and licenses

EPA SWMM 5.2.4 (public domain). No license is stated for the page.

## AI use

The published page carries no AI-use note. It is a Claude artifact on Robert Dickinson's account, built in a claude.ai session. The Netlify copy in this batch adds a one-line AI-use note at the foot of the page. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 1.0: first version.
