---
name: ICM Sediment Field Guide
file: icm-sediment-field-guide.html
version: "1.1"
date: 2026-11-02
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/1JeyHk3G8vx2S7QCSx416Q", repo: none named in the page}
engines: none (textbook sediment formulas in sedphys.js; ICM's solver is not run)
units: US customary by default with a US/SI switch; grain sizes in mm; internally SI with g = 9.81 m/s2
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/1JeyHk3G8vx2S7QCSx416Q, version 1793655822-9832 (index.html, 1,850,045 bytes, SHA-256 f3668ad4135967cdabb03446fec4a8b18531e91f4c302f0d5aa0a49f335aad9c), its About and Doc tabs read in headless Chromium on 2026-11-17. Nothing was run to write this file."
---

# ICM Sediment Field Guide: 1D conduits, river reaches and the 2D mesh in InfoWorks ICM 2027

## In three points
- **What:** Bob's earlier outline for a LinkedIn article on 1D and 2D sediment modeling in InfoWorks ICM, brought to November 2026 and written in full, with two labs that run the formulas the article names.
- **So what:** A flat sediment bed takes 2.8, 7.7, 20.4 and 64.0 percent of a circular pipe's full-flow capacity at 5, 10, 20 and 50 percent depth (a 24 in pipe half full drops from 16 to 5.76 cfs), figures an outside review reproduced to four decimals.
- **Now what:** Use it to set up and explain ICM sediment runs. Every number is a textbook formula at one instant, not ICM's solver, and a real bed adds roughness the capacity curve leaves out.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("v1.1 · 2026-11-02"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Article, 1D Conduits, 2D Mesh, Setup, About, Doc. The article opens with arithmetic: a flat sediment bed in a circular pipe, with the same n and hydraulic gradient, takes 2.8, 7.7, 20.4 and 64.0 percent of full-flow capacity at 5, 10, 20 and 50 percent depth; a 24 in pipe half full drops from the 16 cfs on the drawings to 5.76 cfs. The physics is in one script (sedphys.js) shared by the labs, figures and test script. Kinematic viscosity follows the water temperature through the Vogel equation, scaled so that 68 F gives 1.0 x 10^-6 m2/s.

## Checks (as stated on the page)

- Checks are sorted by kind of evidence: branch continuity (a table typed consistently, for example the Ackers-White 1973 n and A at Dgr = 60), hand calculations, independent references (pipe tables, part-full charts, water property tables), and outside reproduction.
- The page notes that agreement among outputs sharing one implementation does not verify the implementation.
- An independent review of version 1.0 (graded 78/100), supplied by Bob on 2 November 2026, reproduced the capacity curve to four decimals.

## What this does not show

- ICM's own solver: every number is a textbook formula at one instant.
- The capacity curve assumes the same Manning n and hydraulic gradient clean and sedimented; a real bed is rougher.
- Undocumented ICM defaults are marked as such.

## How to reproduce

Open the page; the labs compute in the browser with the US/SI switch.

## Credits and licenses

ICM 2027 help, Autodesk Learn and release notes; the KUL technical note named in the page; Ackers and White (1973). No license is stated for the page.

## AI use

The page says it was built with Claude, Anthropic's AI model, in a Claude session on 2 November 2026, under the direction of Robert (Bob) Dickinson, who asked for the earlier outline to be updated to 2026 and delivered as an HTML app with a Doc tab and a Word file. Claude searched the ICM 2027 help, Autodesk Learn and release notes, and wrote the article, the essay, the formulas, the figures, the test script and the page. For 1.1 Claude checked the outside review's corrections against the ICM 2027 help and the KUL note and applied them. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 1.1 (2026-11-02): total load and bed load separated; transport units corrected to ft2/s; deposition limits restated; undocumented defaults marked; initialisation and results wording fixed.
- 1.0: first version (graded 78/100 by an outside review).
