---
title: "Cube as a Graph (app)"
type: entity
updated: 2026-11-18
sources: [S298]
tags: [apps, graphs, search, group-theory, puzzles]
reviewed: no
---
Bob's app Cube as a Graph: Rubik's cube (3x3x3 and 2x2x2) solved as a graph problem: Thistlethwaite's four subgroups with a bidirectional breadth-first search in each coset graph, and eight other methods to pick from. Version 1.7, 2026-10-20 [S298](../sources/S298-cube-as-a-graph-summary.md). Netlify address, from its `links:` line: https://use-graphs-solve-cube.netlify.app [S298](../sources/S298-cube-as-a-graph-summary.md).

**A caution about its source.** The page ships no technical summary. [S298](../sources/S298-cube-as-a-graph-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q111).

**What the summary says** [S298](../sources/S298-cube-as-a-graph-summary.md)
- The cube graph has 43,252,003,274,489,856,000 vertices, degree 18, diameter 20; Thistlethwaite's first coset graph has 2,048 vertices (longest path 7), the second 1,082,565 (longest path 10).
- 521 solutions across every method and both puzzles replayed to the solved state with no failures; position counts by distance reproduce the published table out to distance 5 (574,908 at 5).
- The optimal solver solved 0 of 5 full 25-turn scrambles in a 25-million-node budget, stopping at depth 12.4 on average, because its strongest lower bound is 9 while a random cube sits near 18.

**What it does not show.** No person has reviewed the solvers against the published algorithms; searched CFOP failed on 2 of 60 scrambles; three defects found by reading the code, with no systematic audit. [S298](../sources/S298-cube-as-a-graph-summary.md)

**Noted at ingest.** Not a water app. 18 x 13.5 = 243 and 243 x 13.333 = 3,240, the branching factors the page gives (our arithmetic).

See [Apps summarized on 17 and 18 November 2026: AI workflows, tools and puzzles](../concepts/apps-from-pages-tools-and-puzzles.md), [Walks, paths, connectivity and search](../concepts/graph-paths-and-search.md), [Graphs: nodes, edges, direction and weight](../concepts/graph-basics.md).
