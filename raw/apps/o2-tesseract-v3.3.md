---
name: O2 Tesseract
file: o2-tesseract.html
version: "3.3"
date: 2026-10-20
written: 2026-11-18
author: Robert Dickinson
links: {netlify: "https://o2-tesseract.netlify.app", artifact: "https://claude.ai/artifact/5dg4Y9uySBXb4U34A4MjTF", repo: none named in the page}
engines: none (a puzzle engine over signed permutations; no water model)
units: none (moves, positions)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says Claude built the app in October 2026 under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/5dg4Y9uySBXb4U34A4MjTF, version 1792425917-d049 (index.html, 430,461 bytes, SHA-256 c151aeda6881859e588875d83f2edadb393f12c617050ecfd6930b0475009b20), its Play, Numbers, How it works and Doc tabs read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# O2 Tesseract: the QiYi O2 cube in three to seventeen dimensions

## In three points
- **What:** The QiYi O2 puzzle (balls in windows, moved by turning a plane) carried from its 3D toy into four dimensions and on up to seventeen: in 4D, eight balls in eight windows turned by the six planes xy, xz, xw, yz, yw and zw, with quarter and double moves, a Magic Cube 4D style view, scramble, solve, step and share.
- **So what:** In 4D there are 192 positions, never more than three moves from solved. A cycle formula gives the distance of any position from its even and odd cycles (n - E - O/2 moves, n - E quarter turns); it matches every position searched exhaustively from 3D to 8D, and above 8D the page relies on it.
- **Now what:** Play it as a puzzle and a lesson in counting; it is not a water app. It models what you can see, not a mechanism: nobody has shown the higher-dimensional pieces could be held together.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("v3.3 · 2026-10-20"). The file name above is the Netlify site's. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Play, Numbers, How it works, Doc. Pick a ball, then the cell to send it to, or turn a plane; "Opposite cells same colour" reduces eight colours to four (+x matches -x, and so on). Dimensions from 3D to 17D; above about 8D the page samples corners. The fan view is decoration. The construction of the O2 follows its TwistyPuzzles museum entry.

## Checks (as stated on the page)

Every count and distance up to 7D was computed twice by breadth-first search, in Python over signed permutation matrices and again by the page's code, and they agree; 8D was searched exhaustively too. Above that, distances come from the cycle formula, which matches every searched position and is proved on the Numbers tab. No person has yet written out and checked the formula's case-by-case proof.

## What this does not show

As the page lists it: a model of what you can see, not a mechanism; the pieces hidden inside the cage are not modelled; distances count a move as a quarter turn or a double move in one plane; the fan is decoration.

## How to reproduce

Play: Scramble, then Solve or Step; Numbers shows the counts by distance and the formula.

## Credits and licenses

The QiYi O2 and its TwistyPuzzles museum entry; Magic Cube 4D for the look. No license is stated for the page.

## AI use

The page says: Claude, Anthropic's AI model, built the app in Claude sessions in October 2026 under the direction of Robert (Bob) Dickinson, who asked for a four-dimensional O2 and each later stage (double moves, paired colours, clicking opposite cells, five to seven and then seventeen dimensions), rejected layouts that were not true projections, brought in an outside review, and asked for the essay in the manner of Isaac Asimov as a Word file and the Doc tab. Claude wrote all of the code, worked out the cycle formula and counting method, ran the searches in Python and Node.js, and drafted the essay. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 3.3 (2026-10-20): the version read.
