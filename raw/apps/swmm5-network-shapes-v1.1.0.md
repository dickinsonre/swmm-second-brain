---
name: The Shapes of SWMM5 Networks
file: swmm5-network-shapes.html
version: 1.1.0
date: 2026-11-16
author: Robert Dickinson
links: {netlify: none yet, artifact: private Claude artifact, repo: none}
engines: none (no hydraulic engine runs; the page reads geometry and inverts from .inp files)
data: {corpus: "github.com/SWMMBobSWMM6/1729-SWMM5-Models-2030", commit: 9ee63bd, files: 4540, measured: 3317, unique_shapes: 1311}
units: US customary (ft). SI models (CMS, LPS, MLD) are converted to feet for stem length, relief and slope.
ai_use: built with Claude (Anthropic); see AI use
---

# The Shapes of SWMM5 Networks: every network cut to one line and laid on the same outfall

## In three points
- **What:** Reduces each SWMM5 .inp to its tree and longest path to the outfall, and lays 1,311 network shapes from the 1729 corpus on one outfall, in five views.
- **So what:** The water's route to the outfall runs a median 1.356 times the straight-line distance, and an independent Python version agrees on sinuosity for 3,310 of 3,317 files.
- **Now what:** Load a folder of your own .inp files to compare their shapes. 465 built-in shapes come from schematic drawings, and a shape says nothing about flow or capacity.

In one sentence: The app cuts each SWMM5 model to its longest path, lays 1,311 of them on one outfall, and shows that the water's route to the outfall runs a median 1.36 times the straight-line distance.

In one paragraph: Give the app a folder of SWMM5 .inp files and it reduces every model to a shape. It finds the outfall, finds the node farthest from it along the drawn pipes, and keeps that one path. Then it moves the outfall to a common point, turns the path so its far end points straight up, and scales it to a common length. The built-in set holds 1,311 different shapes measured from 4,540 files of Bob's 1729 corpus. Their median sinuosity is 1.36. An independent Python version agrees on 3,310 of 3,317 files. The main limit: a shape is only as true as the coordinates in the file, and 465 of the shapes come from schematic drawings.

## What it does

Reads SWMM5 .inp files (built-in corpus, or a folder the user loads) and reduces each model to a shape: its whole tree, its main stem, its invert profile and its width function. Every shape is moved, turned and scaled the same way so that hundreds can be drawn on one canvas and compared. Five views: Whole tree (opening view, all trees stacked on one outfall), Gallery (one tile per network, largest first), Main stem, Profile, Width. It reports sinuosity, Strahler order, stem length, slope, profile concavity and a test of whether the drawing is to scale. Inspired by Dominic Royé's The Shapes of Rivers. For modellers who want to see what their networks have in common.

## How it computes

1. Parse 12 sections: JUNCTIONS, OUTFALLS, DIVIDERS, STORAGE (name, invert), CONDUITS (name, from, to, length), PUMPS, ORIFICES, WEIRS, OUTLETS (name, from, to), COORDINATES, VERTICES, OPTIONS (FLOW_UNITS, FLOW_ROUTING). Comments after `;` are dropped. Quoted names are honoured. (`parseInp` in shape.js)
2. Graph: nodes that have coordinates; links between two such nodes; undirected; weight g = drawn length from node through vertices to node, in map units.
3. Multi-source Dijkstra from every outfall with coordinates. Each node is owned by its nearest outfall. The outfall owning the most links (both ends owned) is kept; that node and link set is the tree.
4. Head = tree node with the largest distance dmax. Main stem = parent chain from head to outfall, through vertices.
5. Transform: translate outfall to (0,0); rotate so the head is on the +y axis; scale by 1/dmax. Stem resampled to 64 points by arc length.
6. sinuosity = dmax / straight distance head to outfall (undefined if the straight distance is under 1e-6 of dmax).
7. Profile: x = cumulative stated CONDUITS length from the outfall / total; z = node invert. Sampled at 33 points; y = (z - zmin)/(zmax - zmin). Needs at least 2 conduits with length on the stem. Stem length in ft = total stated length (x 3.280839895 for SI flow units). slope % = (z_head - z_outfall)/length x 100.
8. concavity = trapezoid area under (z - z_outfall)/(z_head - z_outfall) against x, only when z_head > z_outfall. Even grade = 0.5; steep head and flat outfall < 0.5.
9. Strahler order on the shortest-path tree: leaf = 1; a node takes max child order, plus 1 if two or more children share that max.
10. Width function: for each tree edge, s = mean of its two end distances / dmax; 24 equal bins; value = share of edges. The Width view draws only trees of 50 links or more.
11. Drawing agreement: for tree conduits with stated length > 0 and drawn length > 0, r = drawn/stated; agreement = share with |r/median(r) - 1| <= 0.25; needs 3 or more. >= 0.6 is "to scale", below is "schematic".
12. Gallery: each tile fits one tree's bounding box to the tile (own scale, common turn), sorted by tree link count, descending.
13. Two shapes are the same when tree link counts match and 16 stem points match after rounding to 1/50 of the stem length.

## Inputs and outputs

- Reads: .inp (windows-1252), by file picker, folder picker, or drop of files or folders (recursive). .rpt and .out are ignored. Files over 400 MB are skipped. Nothing is uploaded.
- Built-in: 1,311 shapes, gzip + base64 inside the page (5.0 MB). Stem points rounded to 1/16000 of the stem length; profile and width to 1/65535; tree nodes on a 2047 x 2047 grid (1/1023 of the stem length); link vertices kept for trees under 400 links and dropped for larger ones; 0 trees stored on a coarser grid.
- Writes: PNG of the canvas; CSV of shape numbers (22 columns, one row per network shown); a WebM or MP4 walkthrough recording.

## Checks

Mechanical, run on this build:

| Check | Result |
|---|---|
| Hand-worked fixtures (tests/fixtures.js) | 29 of 29 assertions pass |
| Second implementation, Python + SciPy, all measured files (tests/independent.py) | tree link count 3,317 of 3,317; sinuosity 3,310 of 3,317 to 1e-6 relative |
| The 7 sinuosity differences | copies of 3 models (force_main_example, force_main_gravity_example, routing_combo_all_links) with nodes exactly equidistant from two outfalls; confirmed by tests/tiecheck.js |
| Move, turn, rescale control (tests/invariance.js) | 332 models; 330 unchanged, largest stem shift 3.29e-12; 2 ties |
| Finished page in headless Chromium (tests/browser.js) | 59 of 59 pass |
| Source size | 1,733 lines with code, 481 functions, in hand-written source; complexity index against HydroCouple = 100 not computed (the Meter's analyzer could not be run from the build session) |

Measured facts of the built-in set (commit 9ee63bd):

- 4,540 .inp files, 2.23 GB; 3,317 measured; 1,311 unique shapes; 865 occur once; the most copied occurs 380 times.
- Not measured: no coordinates 499; no links 406; no links reach an outfall 103; no SWMM5 nodes 97; outfall has no coordinates 65; no located links 37; no outfall 15; all nodes at one point 1.
- Median sinuosity 1.356; median links in tree 25; median stem length 5,487 ft; longest stem 65.9 mi; median stem slope 0.172%.
- Median concavity 0.481 (n = 841).
- Drawing: 706 to scale, 465 schematic, 140 cannot tell.
- Strahler order 1 to 9: 318, 391, 251, 183, 101, 42, 23, 1, 1.

| Links in tree | Shapes | Median sinuosity | Median concavity (n) |
|---|---|---|---|
| under 10 | 452 | 1.167 | 0.500 (183) |
| 10 to 99 | 419 | 1.336 | 0.505 (287) |
| 100 to 999 | 331 | 1.482 | 0.438 (273) |
| 1,000 or more | 109 | 1.568 | 0.359 (98) |

## What this does not show

- No flow, capacity, convergence or correctness of any model.
- 465 built-in shapes come from schematic drawings; their stem shape and sinuosity describe the diagram. The 0.6 cut and 25% band are unreviewed choices.
- The tree is nearest outfall by drawn distance, undirected. It is not a flow-directed drainage area. Loops and inter-system overflows can assign nodes to an outfall their water never reaches.
- Only the largest tree of a multi-outfall model is drawn.
- Profile uses node inverts; conduit offsets are ignored; pumps and force mains on the stem appear as rises. 252 shapes have no profile.
- The corpus is one collection (725 of 1311 shapes from the XPSWMM folder), not a sample of sewer systems. The size and concavity trend rests on 98 shapes of 1,000 links or more and has not been tested against published data.
- Ties (equal distance to two outfalls, or two equally long stems) are broken by search order.
- Not built: GitHub loading, flow-directed trees, mirror folding.
- Not checked by a person: the method, the code, any shape against its model, the essay text.

## How to reproduce

```bash
git clone --depth 1 https://github.com/SWMMBobSWMM6/1729-SWMM5-Models-2030            # at commit 9ee63bd
node census.js <corpus> census.json                      # measure every .inp
node build_seed.js 9ee63bd                          # unique shapes -> build/seed.b64, seed-meta.json
node tests/fixtures.js
python3 tests/independent.py <corpus> census.json build/check-independent.json
node tests/invariance.js <corpus> census.json
node build.js && node tests/browser.js <corpus> && node build.js && node build_docx.js
```

## Credits and licenses

- Dominic Royé, *The Shapes of Rivers* (dominicroye.github.io). The idea of laying many networks on one point. No code or data of his is used.
- Robert Dickinson, *1729-SWMM5-Models-2030*, github.com/SWMMBobSWMM6/1729-SWMM5-Models-2030, commit 9ee63bd. Every built-in shape.
- R. E. Horton (1945), Erosional development of streams and their drainage basins, *Geological Society of America Bulletin* 56. Stream ordering.
- A. N. Strahler (1957), Quantitative analysis of watershed geomorphology, *Transactions of the American Geophysical Union* 38. The order used here.
- I. Rodríguez-Iturbe and J. B. Valdés (1979), The geomorphologic structure of hydrologic response, *Water Resources Research* 15. Network shape and the hydrograph.
- E. W. Dijkstra (1959), A note on two problems in connexion with graphs, *Numerische Mathematik* 1. The shortest-path method.
- S. Yang, K. Paik, G. S. McGrath, C. Urich, E. Krueger, P. Kumar and P. S. C. Rao (2017), Functional topology of evolving urban drainage networks, *Water Resources Research* 53, 8966 to 8979, doi:10.1002/2017WR021555. Sewer networks growing to resemble rivers.
- SciPy (scipy.sparse.csgraph.dijkstra), used only in the independent check.
- No third-party code is bundled in the page.

## AI use

This app was built with Claude (model Claude Fable 5.2), Anthropic's AI model, in one Claude session on 16 November 2026, under the direction of Robert (Bob) Dickinson. He brought the idea: a screenshot of Dominic Royé's *The Shapes of Rivers* and the question whether the same could be done for SWMM5 network models. He chose the first two views, and the model corpus the shapes come from is his. When the first build opened on a picture that looked like a river, he said it should look like a network; that made the whole tree the opening view and added the Gallery. Responsibility for the work is his.

**What Claude did.** It proposed the method, wrote the shape-measuring code, the page, the tests, this essay, the Word document and the technical summary, and ran the code over the corpus to make the built-in shapes.

**How the results were checked.** The checks are mechanical, not the AI's judgment: 29 of 29 hand-worked fixtures; a second implementation in Python and SciPy run on all 3,317 measured files; a move, turn and rescale control on 332 models; and 59 of 59 checks of the finished page in a headless browser.

**What no person has checked yet.** Bob has not yet reviewed the method, the code, or any of the 1,311 shapes by eye against its model. The choice of an undirected shortest-path tree, the 0.6 cut for "drawn to scale", and every sentence of this essay are Claude's and are unreviewed.

## Changes

`1.1.0 (2026-11-16)`: opens on Whole tree instead of Main stem, at Bob's direction that the picture should look like a network and not a river. New Gallery view (one tile per network). Pinned trees show their nodes. One more Doc figure. Every tree now stored on the full 2047 x 2047 grid.
`1.0.0 (2026-11-16)`: first version. Four views (main stem, whole tree, profile, width), three scales, filters, folder loading, 1,311 built-in shapes, Doc tab, .docx, this file.
