---
name: EPANET Total Head Explorer
file: epanet-total-head-explorer.html
version: "2026-11-03"
date: 2026-11-03
written: 2026-11-18
author: Robert Dickinson
links: {netlify: "https://epanet-total-head-explorer.netlify.app", artifact: "https://claude.ai/artifact/TTtt1KdWs3jrqJiGnxk3Zh", repo: none named in the page}
engines:
  - {name: JavaScript port of the EPANET 2.2 hydraulic solver, note: "written for the page from the C source; a second mode follows OWA-EPANET v2.3.5 where the two differ"}
  - {name: EPANET, version: 2.2, commit: "598ee6c (2025-09-15)", license: MIT, note: "compiled from source to record reference runs; not in the page"}
  - {name: OWA-EPANET, version: 2.3.5, commit: "444725f (2026-02-19)", license: MIT, note: "compiled from source to record reference runs; not in the page"}
units: US customary (gpm, ft, in, ft/s, psi; 0.4333 psi per ft)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was made with Claude (configured as claude-sonnet-5-5) in November 2026 under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/TTtt1KdWs3jrqJiGnxk3Zh, version 1793732520-dde4 (index.html, 450,814 bytes, SHA-256 22c022dec680fbb6bba4fa6ba4d0c7adb66576fe2923ef2c312081af6c45d869), every tab read in headless Chromium on 2026-11-18. The page calls itself the 2026 edition and gives no version number; the version above is the date of the review fixes. Nothing was run to write this file."
---

# EPANET Total Head Explorer: how EPANET finds head, trial by trial

## In three points
- **What:** A teaching explorer built on a JavaScript port of the EPANET 2.2 hydraulic solver, run in the browser on the tutorial network from the EPANET manual (Listing C.1: 24 hours, five junctions, one reservoir, one tank, six pipes, one pump). Tabs walk from the three heads at one point to the network solve, trial by trial, with an editable network and a Compare tab.
- **So what:** The port agrees with compiled EPANET 2.2 and OWA-EPANET 2.3.5 on the tutorial to 4.4 x 10^-12 ft in head and 6.4 x 10^-11 gpm in flow over all 25 hourly steps, with equal trial counts and times; on 300 random small networks it agrees with EPANET 2.2 to 4.0 x 10^-8 ft in 241 and to 1.7 x 10^-4 ft in 59. The 2026 edition fixed its own pressure constant: 2.31 ft per psi put node 2 at 386.66 psi instead of 387.02.
- **Now what:** Use it to teach what EPANET calls head (z + p/c, without the velocity head) and how the solver converges. It does not model valves, controls, rules, emitters, pressure-driven demand or water quality, and refuses input that uses them. No person has read the port line by line against the C source.

This summary was written after the fact. The page ships no technical summary of its own. The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Head, Chain, Solve, Network, Compare, Verify, Formulas, About, Doc. The Head tab adds elevation, pressure head and velocity head at one node: at node 2, hour 0, z = 710 ft, p = 73.52 psi, so p/c = 73.52 / 0.4333 = 169.67 ft and EPANET head = 879.67 ft; the velocity head of 2.98 ft/s is 0.138 ft and is not part of EPANET's head. Edits (pump, pipes, demand, tank, loss law, closing a pipe) export as an .inp. Compare can shift every elevation and fixed head together and watch every head follow, to rounding.

## Checks (as stated on the page)

- Eight checks re-run in the browser (8 of 8 pass in 10 ms), among them: the manual's printed Listing C.2 for hours 0 and 1 (14 of 14 node rows, 7 of 7 link rows, pump head -193.19 ft, trial errors 0.431541, 0.072835, 0.004398, 0.000008, within the printed ±0.005); the port against recorded EPANET 2.2 and OWA 2.3.5 runs; the solver's slope against a numerical derivative of its head loss over 401 flows from 0.1 to 10,000 gpm (Hazen-Williams 1.7 x 10^-10, Darcy-Weisbach 6.0 x 10^-10, Chezy-Manning 1.4 x 10^-10, pump 6.6 x 10^-11 relative).
- The two compiled engines give byte-identical output on the tutorial.
- An outside review of the source on 3 November, graded 82/100, found three display defects and smaller ones; each is in the defect register, fixed and covered by a test. One correction was to Claude's own earlier experiment (ACC-1).

## What this does not show

As the page lists it: no valves, controls, rules, emitters, pressure-driven demand or water quality; flow units other than gpm are refused; the 300 random networks are small; no person has yet read the port line by line against the C source.

## How to reproduce

Verify tab: Run them again; it also lists the recorded checks and the one command that re-runs them against the compiled engines.

## Credits and licenses

EPANET 2.2 (U.S. EPA, MIT) and OWA-EPANET v2.3.5 (Open Water Analytics, MIT); the tutorial network and its printed results from the EPANET 2.2 User Manual. The page says it is independent of both projects and neither has reviewed it.

## AI use

The page says: the explorer, its tests and the write-up were made with Claude, Anthropic's AI model (configured as claude-sonnet-5-5), in November 2026, under the direction of Robert (Bob) Dickinson, who chose the topic and sent a written review of the first 2026 build. Claude wrote the solver from the C source, a C driver that runs both real engines, a random-network generator, the sweep and noise-floor study, every figure, the app, the Doc and the Word file. The checks are mechanical, not the AI's judgment. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 2026 edition (fixes after the 3 November review): the version read. Pressure uses EPANET's 0.4333 psi per ft (defect APP-1); a real port of 2.2 with a 2.3.5 mode; an editable network; a Compare tab; a Verify tab; a Doc tab with nine figures.
