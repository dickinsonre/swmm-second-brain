---
title: Planar graphs and Euler's formula
type: concept
updated: 2026-11-16
sources: [S158]
tags: [graph-theory, mathematics]
reviewed: no
---
When can a graph be drawn with no crossing edges? From [Tivadar Danka](../entities/tivadar-danka.md)'s "Graph Theory For Visual Learners" [S158](../sources/S158-danka-graph-theory-for-visual-learners.md).

**Definition.** A graph is planar if it can be drawn without any edges crossing. Planarity belongs to the graph, not to one drawing of it (see [Graphs: nodes, edges, direction and weight](graph-basics.md)) [S158](../sources/S158-danka-graph-theory-for-visual-learners.md).

**Examples** [S158](../sources/S158-danka-graph-theory-for-visual-learners.md)
- K4, the complete graph on four nodes, is planar.
- K5, the complete graph on five nodes, is not.
- K3,3, the complete bipartite graph on three and three nodes, is not. It is the utility graph; in Hungary it is called the 3-houses-3-wells graph.
- The edge graph of every convex polyhedron is planar.

**Euler's formula.** For a connected planar graph with v nodes, e edges and f faces (regions bounded by edges), v - e + f = 2 [S158](../sources/S158-danka-graph-theory-for-visual-learners.md).

**A bound on edges.** Each edge borders two faces and each face is bordered by at least three edges, so 2e ≥ 3f. With Euler's formula that gives e ≤ 3v - 6 [S158](../sources/S158-danka-graph-theory-for-visual-learners.md).

**The proof for K5.** It has 5 nodes and 10 edges; 3v - 6 = 9, and 10 > 9, so K5 is not planar [S158](../sources/S158-danka-graph-theory-for-visual-learners.md).

**Subdivisions and Kuratowski's theorem.** Splitting an edge with new nodes is a subdivision; a subdivision of a nonplanar graph is nonplanar. Kuratowski's theorem: a graph is nonplanar if and only if it contains a subdivision of K5 or K3,3 as a subgraph. The article finds a subdivision of K3,3 in its DNA overlap graph, so that graph is not planar [S158](../sources/S158-danka-graph-theory-for-visual-learners.md). The overlap graph is on [Walks, paths, connectivity and search](graph-paths-and-search.md).

**Where it leads.** Planarity is the hypothesis of the four-color theorem; see [Graph coloring and Ramsey numbers](graph-coloring-and-ramsey.md) [S158](../sources/S158-danka-graph-theory-for-visual-learners.md).

**Not in the sources.** Whether SWMM networks, drawn on a map, are planar. Pipes can cross at different elevations without joining, so a drainage network's map drawing may cross where its graph does not; no source here tests this.
