---
title: Walks, paths, connectivity and search
type: concept
updated: 2026-11-16
sources: [S158]
tags: [graph-theory, mathematics, algorithms]
reviewed: no
---
How to move through a graph and how a program finds its way, from [Tivadar Danka](../entities/tivadar-danka.md)'s "Graph Theory For Visual Learners" [S158](../sources/S158-danka-graph-theory-for-visual-learners.md). Terms are on [Graphs: nodes, edges, direction and weight](graph-basics.md).

**Walks and paths.** A walk is an alternating sequence of nodes and edges, and may repeat both. Cutting out its round trips leaves a path: a walk with no repeated node or edge. Since any walk can be trimmed this way, paths usually suffice [S158](../sources/S158-danka-graph-theory-for-visual-learners.md).

**Where it began.** Euler asked for a walk across the seven bridges of Königsberg crossing each exactly once. On the graph of islands and bridges it is impossible, and the question started graph theory [S158](../sources/S158-danka-graph-theory-for-visual-learners.md).

**Connectivity.** b is reachable from a when a path joins them. Reachability is an equivalence relation: reflexive, symmetric and transitive. A graph is connected when every node is reachable from every other, so one walk that visits every node proves it. A graph that falls apart when one edge is removed is 1-connected. The article's example is a city on two banks of a river: remove the two bridge edges and it splits in two [S158](../sources/S158-danka-graph-theory-for-visual-learners.md).

**Search.** A program sees only nodes and their neighbor lists [S158](../sources/S158-danka-graph-theory-for-visual-learners.md).
- Breadth-first search (BFS) explores level by level from a start node. From A, it returns a path to B with the fewest edge traversals.
- Depth-first search (DFS) goes on to unvisited nodes as long as it can, then backtracks. It always finds a path, but possibly a long one.
- Each finds one connected component; to find the others, start again from an unvisited node.

So for finding a path between two nodes, BFS is usually the better choice [S158](../sources/S158-danka-graph-theory-for-visual-learners.md). The same two searches find cycles: see [Cycles and trees](graph-cycles-and-trees.md).

**Hamiltonian paths and cycles.** A Hamiltonian path touches every node exactly once; a Hamiltonian cycle does so and returns to its start. Neither is guaranteed to exist, and finding them is computationally hard. The edge graphs of all five Platonic solids have Hamiltonian cycles [S158](../sources/S158-danka-graph-theory-for-visual-learners.md).

**Genome assembly.** In shotgun sequencing, DNA fragments become nodes, and a directed edge runs from one fragment to another when the end of the first overlaps the start of the second. A Hamiltonian path through that graph stitches the fragments into a candidate genome [S158](../sources/S158-danka-graph-theory-for-visual-learners.md). The same overlap graph turns up on [Planar graphs and Euler's formula](planar-graphs.md).

**Shortest paths with weights.** On a weighted graph, shortest paths take the edge weights into account; the article's street graph uses street lengths [S158](../sources/S158-danka-graph-theory-for-visual-learners.md). Counting shortest paths through a node gives [betweenness centrality](graph-random-walks-and-centrality.md).
