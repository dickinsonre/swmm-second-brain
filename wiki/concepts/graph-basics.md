---
title: "Graphs: nodes, edges, direction and weight"
type: concept
updated: 2026-11-16
sources: [S158, S60]
tags: [graph-theory, mathematics]
reviewed: no
---
The vocabulary of graphs, from [Tivadar Danka](../entities/tivadar-danka.md)'s "Graph Theory For Visual Learners" [S158](../sources/S158-danka-graph-theory-for-visual-learners.md), and where it meets a SWMM network.

**A graph** is a set of nodes and edges. In a simple graph each edge is a two-element subset of the nodes: no loops, no weights, no directions [S158](../sources/S158-danka-graph-theory-for-visual-learners.md).

**A drawing is not the graph.** Dots and lines are one picture of a graph among infinitely many. Two drawings of the same underlying structure are isomorphic [S158](../sources/S158-danka-graph-theory-for-visual-learners.md).

**Degree** is a node's number of incident edges. It is local information and does not fix the graph: a cycle of eight nodes and two cycles of four have every degree equal to two and are not isomorphic [S158](../sources/S158-danka-graph-theory-for-visual-learners.md).

**Directed graphs.** A symmetric relation (a is friends with b) gives unordered edges. A non-symmetric one (a follows b, a links to b, a one-way street) gives edges as ordered pairs. A function such as f(n) = n + 1 is a directed graph, with an arrow from each n to n + 1 [S158](../sources/S158-danka-graph-theory-for-visual-learners.md).

**Computational graphs** hold variables in nodes and computational dependencies as edges. Logistic regression, σ(ax + b), takes three steps. Neural networks are computational graphs, and the gradients needed to train them can be stored on the edges [S158](../sources/S158-danka-graph-theory-for-visual-learners.md).

**Weighted graphs** give each edge a number. The article's street graph is weighted by street length, and its shortest paths use those weights [S158](../sources/S158-danka-graph-theory-for-visual-learners.md).

**Matrices.** A random walk on a directed graph whose weights are probabilities is a Markov chain, described by its transition matrix; with arbitrary weights the same table is the adjacency matrix, a compact form for directed, weighted graphs [S158](../sources/S158-danka-graph-theory-for-visual-learners.md). See [Random walks and centrality](graph-random-walks-and-centrality.md).

**Where it meets SWMM.** The article does not mention SWMM; these facts come from the EPA hydraulics manual. SWMM models a conveyance system as a network of links joined at nodes; flows enter at nodes, travel along links, and leave at terminal nodes [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md). For kinematic wave routing every link is first oriented in the direction of positive slope [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md). In the terms above, that makes the network a directed graph (our reading, not the manual's words). What that requires of the network is on [Cycles and trees](graph-cycles-and-trees.md); the objects themselves are on [SWMM 5 network objects, boundary and initial conditions](swmm5-network-objects.md).

**Related.** [Walks, paths, connectivity and search](graph-paths-and-search.md), [Planar graphs and Euler's formula](planar-graphs.md), [Graph coloring and Ramsey numbers](graph-coloring-and-ramsey.md).
