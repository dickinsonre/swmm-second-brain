---
title: Cycles and trees
type: concept
updated: 2026-11-16
sources: [S158, S60, S08]
tags: [graph-theory, mathematics, kinematic-wave, swmm5]
reviewed: no
---
Cycles make a graph resilient and its paths ambiguous; trees have none. From [Tivadar Danka](../entities/tivadar-danka.md)'s "Graph Theory For Visual Learners" [S158](../sources/S158-danka-graph-theory-for-visual-learners.md), with the SWMM side from other sources.

**Definitions** [S158](../sources/S158-danka-graph-theory-for-visual-learners.md)
- A walk is closed if it ends where it started.
- A trail is a walk with no repeated edge.
- A cycle is a closed trail with no repeated node.

**Why cycles matter, both ways.** Remove any edge of a cycle and the graph stays connected, so cycles resist edge removal. But they make the path between two nodes ambiguous and block any hierarchical ordering [S158](../sources/S158-danka-graph-theory-for-visual-learners.md). BFS and DFS find cycles by tracking visited nodes and their parents; see [Walks, paths, connectivity and search](graph-paths-and-search.md).

**A tree** is a connected graph with no cycles. Three equivalent definitions [S158](../sources/S158-danka-graph-theory-for-visual-learners.md):
1. Minimally connected: removing any edge splits it in two. The article's analogy is a power grid with no wasted lines.
2. Maximally acyclic: adding any edge creates a cycle.
3. Exactly one path joins any two nodes. Connectedness gives at least one; acyclicity forbids a second.

**Roots and levels.** In a tree any node can be the root, and each other node's level is its distance from the root. DFS from the root goes as deep as it can; BFS works level by level [S158](../sources/S158-danka-graph-theory-for-visual-learners.md).

**Two uses from the article.** A labyrinth drawn as a tree is solved by DFS, which is the left-hand rule. A decision tree asks one question per level; its example asks x ≤ 0.13, then y ≤ 0.09, then x ≤ -0.94, and predicts yellow, having split the plane into rectangles [S158](../sources/S158-danka-graph-theory-for-visual-learners.md).

**Where it meets SWMM.** Not in the article; from the EPA hydraulics manual and Bob's swmm5.org pages.
- Kinematic wave routing in SWMM 5 accepts only directed acyclic networks, and a junction may have at most one outlet link [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md). The manual's Table 2-1 calls this branched networks only.
- Each link is oriented by its slope, and the conduits are processed in topologically sorted order, found once before time 0 by Kahn's algorithm. If a loop is found, the program stops with an error [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).
- Dynamic wave analysis has no such limit and handles any layout [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).
- Bob's swmm5-kw repository routes kinematic wave and steady flow through junctions that split flow and through loops [S08](../sources/S08-swmm5org-topic-inside-swmm5.md).

More on [Kinematic wave and steady flow routing](kinematic-wave-and-steady-flow.md).

**Not in the sources.** Kahn's algorithm itself (repeatedly take a node with no unprocessed incoming edges) is general knowledge, not described in either source.
