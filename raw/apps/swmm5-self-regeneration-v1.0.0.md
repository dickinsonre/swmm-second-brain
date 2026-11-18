---
name: SWMM5 Self-Regeneration
file: swmm5-self-regeneration.html
version: 1.0.0
date: 2026-10-26
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/2nZDYfaQ7DkBRoKB17VHYF", repo: none named in the page}
engines:
  - {name: EPA SWMM, version: 5.2.4, source: "USEPA tag v5.2.4, src/solver + src/run/main.c; zig cc 0.17 -target wasm32-wasi -O2, one shim (mkstemp), 524 KB, embedded", license: public domain}
units: US customary as the models carry them
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/2nZDYfaQ7DkBRoKB17VHYF, version 1793053288-ffa0 (index.html, 4,320,697 bytes, SHA-256 26890ce33db3c5d47bb428467eaa5ff28ae12835644b391df5e5579cabd0a498), its About and Doc tabs read in headless Chromium on 2026-11-17. No model was run to write this file."
---

# SWMM5 Self-Regeneration: can a model's .out give back its .inp?

## In three points
- **What:** Reads only a SWMM5 binary .out, writes a new .inp in four rungs, runs each in EPA SWMM 5.2.4 in the page, and diffs every regenerated .out against the original, element by element.
- **So what:** On the demo, rung R1 (topology only, default circles and n = 0.013) keeps 9% of conduits within 10% of their own peak; R2 (shapes, sizes, Manning's n) keeps every conduit within 10% (median 5.2%); R2b, with the engine refining n, gets the median to 1.8%; R3 explains the inflows from rain and still lands within two percent.
- **Now what:** Use it to see how much of a model its results pin down, for example to rebuild a lost .inp. Same .out is not the same .inp, and nothing faster than about two report steps can be recovered.

This summary was written after the fact. The page ships no technical summary of its own. Its version and build date are the page's own ("1.0.0 · built 2026-10-26"). The file name above is ours. Every number below is copied from the page. No model was run to write this file.

## What it does

The question came from an infographic, Can an Object Model Itself?, which separates an object's size (how much it can hold) from its structure (what it can compute); here the report step is the size and the routing method, controls and parameters are the structure. The page collects witnesses (relationships SWMM's bookkeeping guarantees), fits what they cannot pin down, writes an .inp per rung, runs it, and diffs. The original .inp, when present, is used only to score. Tabs: Run, Topology, Sections, Hydrology, Diff, Corpus, About, Doc.

## Results the page reports (the demo)

- R1 joins the network with default circles and n = 0.013: 9% of conduits stay within 10% of their own peak, median worst-instant error 32%.
- R2 adds shapes, sizes and Manning's n: every conduit within 10%, median 5.2%.
- R2b lets the engine refine n: median 1.8%.
- R3 explains the inflows from rain instead of replaying them and still lands within two percent.

## Checks (as stated on the page)

- The page's engine run twice on the same .inp writes byte-identical .out files (demo models).
- Against EPA SWMM 5.2.4 built natively with gcc on the same source, 46 of 60 corpus models give byte-identical .out files; the other 14 differ from the last bit onward.
- A 277-model corpus sweep was run; every regenerated .inp is scored against its original.
- The checks are mechanical.

## What this does not show

- No field data; one engine.
- Equivalence (same .out) is not identity (same .inp).
- Nothing faster than about two report steps.

## How to reproduce

Open the page; it shows the precomputed site-drainage demo; press Regenerate to run it in the browser, or load your own .out (and optionally .inp).

## Credits and licenses

EPA SWMM 5.2.4 (public domain). Bore Shell 1.0.0. No license is stated for the page.

## AI use

The page says it was built with Claude, Anthropic's AI model, in a Claude session on 26 October 2026, under the direction of Robert (Bob) Dickinson, who posed the question, chose the .out-to-.inp test as the definition of a model that models itself, and set the verification standards. Claude compiled EPA SWMM 5.2.4 to WebAssembly, wrote the in-memory WASI host, the .out reader, the topology, cross-section, roughness, regulator and hydrology inference, the .inp writer, the engine-in-the-loop refinement and the diff, ran the 277-model sweep, and wrote the page, figures and essay. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 1.0.0 (2026-10-26): first version.
