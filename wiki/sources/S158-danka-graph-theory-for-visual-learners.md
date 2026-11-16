---
title: "S158: Tivadar Danka, Graph Theory For Visual Learners (The Palindrome, 2026-11-11), reading note"
type: source
raw: raw/notes/graph-theory-for-visual-learners-danka-2026-11-11.md
kind: reading-note
author: Tivadar Danka
published: 2026-11-11
ingested: 2026-11-16
tags: [graph-theory, mathematics, third-party]
reviewed: no
---
**What it is.** A reading note on a third-party article. Citation: Danka, Tivadar. "Graph Theory For Visual Learners: A scenic tour into the heart of graph theory." *The Palindrome* (Substack newsletter), 11 November 2026. https://thepalindrome.org/p/graph-theory-for-visual-learners-320. Raw file: [raw/notes/graph-theory-for-visual-learners-danka-2026-11-11.md](../../raw/notes/graph-theory-for-visual-learners-danka-2026-11-11.md). Author: [Tivadar Danka](../entities/tivadar-danka.md).

**How it was written.** The article is by Tivadar Danka, with a companion video; it states no AI use. Bob asked on 16 November 2026 for it to be added "as graph concepts" with the right citation. The article is copyrighted, so `raw/` holds a digest Claude wrote in its own words after reading the whole post in a browser, not the text. Claims below rest on that digest; the original is the authority. Bob has not read the note (Q88). The article does not mention SWMM; every link from it to SWMM on the wiki pages rests on another source, cited there.

**Claims worth keeping**
- A simple graph is a set of nodes and edges, each edge a two-element subset of the nodes. A drawing is one of infinitely many pictures of it; drawings of one structure are isomorphic. Degrees alone do not determine a graph.
- A walk may repeat nodes and edges; a path repeats neither. Graph theory began with Euler and the seven bridges of Königsberg.
- Reachability is an equivalence relation; a graph is connected when every node reaches every other. BFS explores level by level and finds a path with the fewest edges; DFS goes deep and backtracks. Each finds one connected component.
- A cycle is a closed trail with no repeated node; removing an edge of a cycle leaves the graph connected. A tree is a connected acyclic graph, equivalently minimally connected, maximally acyclic, or one with exactly one path between any two nodes.
- Hamiltonian paths and cycles touch every node once; finding them is computationally hard. Shotgun sequencing assembles a genome along a Hamiltonian path of a directed overlap graph.
- Planarity: K4 is planar, K5 and K3,3 are not. Euler's formula v - e + f = 2 for connected planar graphs gives e ≤ 3v - 6; K5 has 10 edges against a bound of 9. Kuratowski's theorem: nonplanar if and only if a subdivision of K5 or K3,3 is a subgraph.
- Colorings: Europe's map graph has chromatic number 4 (Belgium, France, Germany and Luxembourg form a four-clique); the four-color theorem bounds planar graphs at 4; Mycielskian graphs are triangle-free with any chromatic number. The chromatic index is the maximum degree or one more (Vizing's theorem); Germany has 9 neighbors.
- Ramsey numbers: R(3) = 6, R(4) = 18, the last known exactly; R(5) between 43 and 46, R(6) between 102 and 160, R(7) between 205 and 492.
- Directed graphs model non-symmetric relations; weighted graphs give each edge a number; a Markov chain is a random walk on a weighted directed graph, described by a transition matrix, which with arbitrary weights becomes the adjacency matrix.
- The equilibrium distribution of a random walk is what PageRank computes; betweenness centrality counts the share of shortest paths through a node; high-centrality nodes and edges mark likely bottlenecks.

**Feeds:** [Graphs: nodes, edges, direction and weight](../concepts/graph-basics.md), [Walks, paths, connectivity and search](../concepts/graph-paths-and-search.md), [Cycles and trees](../concepts/graph-cycles-and-trees.md), [Planar graphs and Euler's formula](../concepts/planar-graphs.md), [Graph coloring and Ramsey numbers](../concepts/graph-coloring-and-ramsey.md), [Random walks and centrality](../concepts/graph-random-walks-and-centrality.md), [Tivadar Danka](../entities/tivadar-danka.md).
