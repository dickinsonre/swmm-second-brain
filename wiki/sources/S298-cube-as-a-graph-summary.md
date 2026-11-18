---
title: "S298: Cube as a Graph, summary written from the page (v1.7)"
type: source
raw: raw/apps/use-graphs-solve-cube-v1.7.md
kind: app-md
author: Robert Dickinson
published: 2026-10-20
ingested: 2026-11-18
tags: [apps, graphs, search, group-theory, puzzles]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app Cube as a Graph, version 1.7: Rubik's cube (3x3x3 and 2x2x2) solved as a graph problem: Thistlethwaite's four subgroups with a bidirectional breadth-first search in each coset graph, and eight other methods to pick from. Raw file: [raw/apps/use-graphs-solve-cube-v1.7.md](../../raw/apps/use-graphs-solve-cube-v1.7.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q111). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/P3yLhK1Abk81uDgWByRRi4, version 1792448317-ea94 (index.html, 234,366 bytes, SHA-256 284845d37c1773ce00082f82e6db5a7968f59c708cf901387391d0f2a3097378), its App and Doc tabs read in headless Chromium on 2026-11-18. Nothing was run to write this file." The page says Bob directed the work and reviewed the result; Claude (Opus 5) wrote the application in September 2026 and the Doc in October 2026.

**Claims worth keeping** (all copied from the file)
- The cube graph has 43,252,003,274,489,856,000 vertices, degree 18, diameter 20; Thistlethwaite's first coset graph has 2,048 vertices (longest path 7), the second 1,082,565 (longest path 10).
- 521 solutions across every method and both puzzles replayed to the solved state with no failures; position counts by distance reproduce the published table out to distance 5 (574,908 at 5).
- The optimal solver solved 0 of 5 full 25-turn scrambles in a 25-million-node budget, stopping at depth 12.4 on average, because its strongest lower bound is 9 while a random cube sits near 18.

**Limits it states.** No person has reviewed the solvers against the published algorithms; searched CFOP failed on 2 of 60 scrambles; three defects found by reading the code, with no systematic audit.

**Checked at ingest.** Not a water app. 18 x 13.5 = 243 and 243 x 13.333 = 3,240, the branching factors the page gives (our arithmetic). The `links:` line gives Netlify as https://use-graphs-solve-cube.netlify.app.

**Feeds:** [Cube as a Graph (app)](../entities/cube-as-a-graph.md), [Apps summarized on 17 and 18 November 2026: AI workflows, tools and puzzles](../concepts/apps-from-pages-tools-and-puzzles.md), [Walks, paths, connectivity and search](../concepts/graph-paths-and-search.md), [Graphs: nodes, edges, direction and weight](../concepts/graph-basics.md).
