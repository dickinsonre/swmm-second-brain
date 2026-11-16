---
title: Random walks and centrality
type: concept
updated: 2026-11-16
sources: [S158]
tags: [graph-theory, mathematics, networks]
reviewed: no
---
Two ways to measure which nodes of a graph matter, from [Tivadar Danka](../entities/tivadar-danka.md)'s "Graph Theory For Visual Learners" [S158](../sources/S158-danka-graph-theory-for-visual-learners.md). Directed and weighted graphs are on [Graphs: nodes, edges, direction and weight](graph-basics.md).

**Random walks.** A coin-flip walk is a random walk on a graph with probability 0.5 on each step. A Markov chain is a random walk on a directed graph whose edge weights are the transition probabilities, described by a transition matrix [S158](../sources/S158-danka-graph-theory-for-visual-learners.md).

**The equilibrium distribution.** The long-run share of time a random walk spends at each node is its equilibrium distribution. It is what Google's PageRank computes on the graph of websites [S158](../sources/S158-danka-graph-theory-for-visual-learners.md).

**Betweenness centrality.** For a node v: for every pair of nodes s and t, take the share of shortest paths from s to t that pass through v; sum those shares over all pairs. Edge centrality is defined the same way for edges [S158](../sources/S158-danka-graph-theory-for-visual-learners.md).

**What it shows.** On the article's city graph, the nodes and streets near the two bridges score highest. Without any traffic data, high-centrality nodes and edges point to likely bottlenecks [S158](../sources/S158-danka-graph-theory-for-visual-learners.md). Shortest paths themselves are on [Walks, paths, connectivity and search](graph-paths-and-search.md).

**Not in the sources.** Any use of these measures on a drainage network. A SWMM network's flow is set by hydraulics, not by shortest paths, so betweenness on its graph would describe its topology, not where water goes; no source here has tried it.
