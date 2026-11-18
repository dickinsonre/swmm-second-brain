---
name: HydroCouple Study Guide
file: hydrocouple-study-guide.html
version: "1.0"
date: 2026-10-25
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/BdkdNWB8EBKDXu8i5LqFgz", original: "HydroCouple-Guide.zip (a study guide whose author is not named in the zip)", repo: "https://github.com/HydroCouple/HydroCouple (read at b1722c4 and v1.0.0)"}
engines:
  - {name: HydroCouple, version: "b1722c4 (2026-10-06, 2.0.0-alpha.2 + Unreleased, ABI 4) and v1.0.0 (f65dfd4, 2017-11-19, Qt, LGPL-3)", note: "headers parsed and compiled against with g++; no HydroCouple build runs in the page"}
  - {name: HydroCoupleSDK, version: "main c048f52 (2019-07-25); removing_qt 636266c (2026-10-03)", note: "cloned and read"}
units: US customary (cfs, in, ac, ft, F); the guide's example is in m3/s
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude on 25 October 2026 under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/BdkdNWB8EBKDXu8i5LqFgz, version 1792946561-c5fe (index.html, 1,407,762 bytes, SHA-256 bddec357eb68021e1e02a15df856793779b8d8ba8f44c26c3420b352e926ae1f), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# HydroCouple Study Guide: the guide, checked against the headers it describes

## In three points
- **What:** A study guide to HydroCouple, Caleb Buahin's C++ interface standard for coupling environmental models, arrived as a zip (five chapters, two C++ files, one Graphviz drawing) whose README asks the reader to check the real headers. This app does, claim by claim, against the 2017 v1.0.0 release and the 2026 2.0 code, and runs the guide's own coupling example in a JavaScript simulator so the pull can be watched.
- **So what:** The architecture in the guide is right, and much of the API it shows is the 2017 Qt interface or never existed: 19 of 27 code lines compile against v1.0.0 and 13 against 2.0. The page lists twenty findings, and its corrected C++ files compile with -Wall.
- **Now what:** Use it to learn HydroCouple's pull-driven coupling and to know which guide code to trust. The simulator is not HydroCoupleSDK, loads no component library, and its runoff model is a SWMM-style nonlinear reservoir, not SWMM. No person has reviewed the twenty findings against the headers.

This summary was written after the fact. The page ships no technical summary of its own. Its version is the page's own ("v1.0 · HC b1722c4"); the date is the build session the page names. The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Guide (read a chapter; click a chip for the evidence), Pull Chain (step or run to end; change TimeKind, method and weights; export the time series), Lifecycle (click a state), Types, Code, Verify (search, compare, filter), About, Doc. The coupling example joins a runoff model (a nonlinear reservoir per subcatchment with a constant loss rate) to a reach model (fixed volumes, perfect mixing, no heat exchange with the air), so its temperatures show the coupling, not a stream.

## Checks (as stated on the page)

Checked by a machine: 27 guide lines, each compiled twice (against v1.0.0 and b1722c4); the corrected .cpp compiles with -Wall; the lifecycle transition table dumped from C++; 26 simulator tests in node; 95 interfaces parsed from the headers; a browser test of every tab in both themes. Checked by reading: verdicts on header comments rest on Claude's reading of the cited lines.

## What this does not show

As the page lists it: the simulator is a JavaScript model of the pull using the standard's names and compiled transition table; it is not HydroCoupleSDK, loads no component library, and nothing was run through a HydroCouple build. The runoff model is not SWMM (no Horton or Green-Ampt infiltration, no routing, no report-step averaging). No person has yet reviewed the twenty findings against the headers.

## Credits and licenses

HydroCouple is by Caleb Buahin (MIT), described in Buahin and Horsburgh (2018), Environmental Modelling & Software 108, 133-153, doi:10.1016/j.envsoft.2018.07.015. The study guide's author is not named in the zip. No license is stated for the page.

## AI use

The page says: built with Claude, Anthropic's AI model, in a Claude session on 25 October 2026 at the direction of Robert (Bob) Dickinson, who supplied the guide and is responsible for the work. Claude cloned HydroCouple (v1.0.0 and b1722c4) and HydroCoupleSDK, wrote the header parser, the 27 compile probes and the corrected C++ files, compiled the lifecycle table, wrote the simulator and its 26 tests, and built the page, its figures and text, including the Doc essay. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 1.0 (2026-10-25): first version (the version read).
