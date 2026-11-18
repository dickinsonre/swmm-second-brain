---
name: Cube as a Graph
file: use-graphs-solve-cube.html
version: "1.7"
date: 2026-10-20
written: 2026-11-18
author: Robert Dickinson
links: {netlify: "https://use-graphs-solve-cube.netlify.app", artifact: "https://claude.ai/artifact/P3yLhK1Abk81uDgWByRRi4", repo: none named in the page}
engines: none (a Rubik's cube engine and nine solvers in JavaScript; no water model)
units: none (face turns, positions, search nodes)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says Claude (Opus 5) wrote the application in September 2026 and the Doc in October 2026, at Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/P3yLhK1Abk81uDgWByRRi4, version 1792448317-ea94 (index.html, 234,366 bytes, SHA-256 284845d37c1773ce00082f82e6db5a7968f59c708cf901387391d0f2a3097378), its App and Doc tabs read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# Cube as a Graph: solving Rubik's cube by walking its Cayley graph

## In three points
- **What:** A Rubik's cube (3x3x3 and 2x2x2) solved as a graph problem: every position is a vertex, every face turn an edge, in a graph of 43,252,003,274,489,856,000 vertices with degree 18 and diameter 20. The headline method is Thistlethwaite's ladder of four subgroups with a bidirectional breadth-first search in each much smaller coset graph (the first has 2,048 vertices); eight other methods (Kociemba, Korf-style IDA* optimal, commutators, CFOP searched and from a catalogue, Roux, ZZ, inverse word) can be picked.
- **So what:** It shows why nobody searches the full graph: a loose bound forces blind search. The optimal solver solved 0 of 5 full 25-turn scrambles in its 25-million-node budget (stopping at depth 12.4 on average), because the strongest lower bound the app has is 9 while a random cube sits near 18; Korf closed that gap with 88 million table entries.
- **Now what:** Use it to see group theory as graph search. It is not a water app; every solution is checked by replaying it, but no person has reviewed the solvers line by line against the published algorithms.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("v1.7 · 2026-10-20"). The file name above is the Netlify site's. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Demo, App, Doc. The App shows the subgroup ladder: Phase 1 (all 18 moves) orients all 12 edges in a coset graph of 2,048 vertices, longest path 7; Phase 2 (14 moves) orients corners and places the E-slice edges in 1,082,565 vertices, longest path 10; Phase 3 (10 moves) uses 29,400 vertices; Phase 4 finishes with half turns. Forward and backward searches meet in the middle.

## Checks (as stated on the page)

- 521 solutions across every method and both puzzles replayed move by move through the app's own move code to the solved state: none failed.
- Position counts by distance from solved reproduce the published table exactly out to distance 5 (1, 18, 243, 3,240, 43,239, 574,908); the branching factor settles near 13.3.
- The whole 2x2 graph enumerated and matched against the published table; 1,249,344 commutators re-tested; all 56 catalogue algorithms re-checked; every one-sided search in the comparison figure executed, not estimated.
- Three defects were found by reading the code for the write-up; there has been no systematic audit.

## What this does not show

As the page lists it: the optimal solver cannot reach a random cube's depth in a browser's budget (cost rose about sixfold per extra turn of depth); searched CFOP failed on 2 of 60 scrambles, always at the last F2L pair against a 4-million-node budget; no person has reviewed the solvers against the published descriptions of Thistlethwaite's, Kociemba's or Korf's algorithms.

## How to reproduce

App tab: scramble, pick a method, Solve by graph search; replay the moves on the cube.

## Credits and licenses

Thistlethwaite's, Kociemba's and Korf's algorithms; the published position-count tables. No license is stated for the page.

## AI use

The page says: Robert Dickinson directed the work, asked for the app, set the standard that a claim about a solver must be checked against the solver, and reviewed the result. Claude (Opus 5, Anthropic) wrote the application in September 2026 (cube engine, nine solvers, bidirectional search, pocket-cube distance table, validator, 3D rendering, demo, page) and in October 2026 wrote the Doc, its eight figures and the measurements behind them. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 1.7 (2026-10-20): the version read.
