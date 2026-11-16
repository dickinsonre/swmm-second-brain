---
title: Graph coloring and Ramsey numbers
type: concept
updated: 2026-11-16
sources: [S158]
tags: [graph-theory, mathematics]
reviewed: no
---
Coloring nodes, coloring edges, and the structure no coloring can avoid. From [Tivadar Danka](../entities/tivadar-danka.md)'s "Graph Theory For Visual Learners" [S158](../sources/S158-danka-graph-theory-for-visual-learners.md).

**Vertex colorings** [S158](../sources/S158-danka-graph-theory-for-visual-learners.md)
- Make each country of Europe a node and join neighbors with an edge. A coloring is proper when no two neighbors share a color.
- The chromatic number χ is the fewest colors a proper coloring needs.
- Europe's map is colored with four. It cannot be done with three: Belgium, France, Germany and Luxembourg are all neighbors of each other, a four-clique. So χ = 4.
- A complete graph needs as many colors as it has nodes. But a high chromatic number does not require a large complete subgraph: the Mycielskian construction, started from a five-node cycle, gives triangle-free graphs of any chromatic number.
- The four-color theorem: a planar graph has χ ≤ 4. Planarity is on [Planar graphs and Euler's formula](planar-graphs.md).

**Edge colorings** [S158](../sources/S158-danka-graph-theory-for-visual-learners.md)
- A proper edge coloring gives all the edges at a node different colors. The fewest colors is the chromatic index χ′.
- χ′ is at least the maximum degree. On the Europe graph that is Germany, with 9 neighbors.
- Vizing's theorem: χ′ is either the maximum degree or the maximum degree plus one. Cycles with an even number of nodes take the first, odd cycles the second.
- The contrast with vertex colors: a star needs as many edge colors as its center's degree, but only two vertex colors.

**Ramsey numbers** [S158](../sources/S158-danka-graph-theory-for-visual-learners.md)
- Color every edge of K6 one of two colors: a one-color triangle always appears. The article proves it with the pigeonhole principle rather than checking all 2^15 colorings.
- K5 can be colored without one, so the smallest such n is 6: R(3) = 6.
- R(m) is the smallest n for which every two-coloring of Kn contains a one-color Km.

| m | R(m) |
|---|---|
| 1 | 1 |
| 2 | 2 |
| 3 | 6 |
| 4 | 18, the last value known exactly |
| 5 | between 43 and 46 |
| 6 | between 102 and 160 |
| 7 | between 205 and 492 |

Table from [S158](../sources/S158-danka-graph-theory-for-visual-learners.md).

**A social reading.** Drop one color and R(4) = 18 says that among any 18 people, some 4 either all know each other or all do not [S158](../sources/S158-danka-graph-theory-for-visual-learners.md).

**Related.** [Graphs: nodes, edges, direction and weight](graph-basics.md) for degree and complete graphs.
