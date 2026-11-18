---
name: Pipes & Cistern
file: pipes-and-cistern.html
version: "1.0"
date: 2026-10-25
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/Diae8f2gzMwTokUbuRzYDq", original: "https://spark-diagrams-playground.lovable.app (Lovable project Pipes & Cistern; repository SWMMEnablement/spark-diagrams-playground)", repo: none for this edition}
engines:
  - {name: EPA SWMM, version: 5.2.4, note: "three exported Real Tank .inp files run while building; the page exports the model and does not run an engine"}
units: US customary by default (ft, hours), SI behind a switch
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude in October 2026 under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/Diae8f2gzMwTokUbuRzYDq, version 1792898560-6bb1 (index.html, 1,206,613 bytes, SHA-256 5ac2ab99236c7ad160e04aeb27f6bbf9892c0a8d072c18da81dba42eee6b0d2e), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18, with its CDN libraries supplied from local npm copies of the same versions. Nothing was run to write this file."
---

# Pipes & Cistern: the exam rate problems, and what a real tank with a hole does instead

## In three points
- **What:** Practice problems, live calculators and the formula sheet for the two classic rate problems, Time & Work and Pipes & Cistern, plus a Real Tank tab that shows what a straight-walled tank with a hole in the floor actually does, with an exact Torricelli solution and a SWMM5 model to export.
- **So what:** The exam answer assumes constant rates; a real leak slows as the water falls. With a 6-hour pipe and an 18-hour leak the exam line fills at 9 h and the real tank at 11.66 h; with a 6-hour pipe and a 10-hour leak the exam fills at 15 h and the real tank stalls at 69.4% full. Depths from EPA SWMM 5.2.4 runs of the exported files fall on the exact curve. Sixteen defects in the Lovable version are fixed (D1 to D16), including a chart that ignored Pipe B.
- **Now what:** Use it to drill the exam method and to see where it stops matching a tank. The exam model ignores pump curves and falling heads, the Real Tank covers one kind of leak, and the SWMM check covers three cases, not the whole map.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("Single-file edition v1.0 · 2026-10-25"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Practice, Calculators, Formulas, Real Tank, About, Doc. Answers update as you type; the pipe calculator has a draggable clock, and its tank, chart and answer share one function. Practice draws from eighteen problem templates, checks your answer (within 1% or 0.011 of exact), keeps a session log and exports CSV. The formula database exports as CSV, JSON or PDF. The Real Tank writes a storage node of constant area, a constant inflow, a BOTTOM orifice to a free outfall, and dynamic wave routing at a one-second step; in a published artifact the file saves as .inp.txt.

## Checks (as stated on the page)

- The generator harness: 20,000 draws per template, each answer re-solved independently from the question text; six generator defects and one duplicate template fixed (D1 to D6).
- Ten calculator and formula defects fixed (D7 to D16), among them the √xy and pairwise formulas.
- The exact tank solution against Runge-Kutta integration and against SWMM 5.2.4 (three cases).
- Contrast check of both themes; headless-browser screenshots at desktop and phone widths in both themes.

## What this does not show

As the page lists it: constant rates in the exam model (no pump curves, no reservoir-fed pipe that slows as heads converge); one kind of leak (a sharp-edged hole in the floor of a straight-walled tank, constant discharge coefficient, nothing downstream); the SWMM check covers three cases, not a sweep; the eighteen templates cover the common exam patterns, not every one in the books.

## Credits and licenses

Evangelista Torricelli (1640s); EPA SWMM 5.2.4 (public domain); the Lovable Pipes & Cistern (handover document dated 2026-02-12) and its reference formula sheet, credited rather than embedded. MIT License, © 2026 Robert Dickinson.

## AI use

The page says: built with Claude, Anthropic's AI model, in October 2026 under the direction of Robert (Bob) Dickinson, who built the original Lovable app, supplied its source and asked for an HTML version; responsibility is his. Claude read the Lovable source, ran every possible draw of its eighteen templates to find the defects, rewrote the app as one HTML file (practice generator, answer checker, five calculators, formula sheet with hand-set LaTeX, charts and tank drawings), added the Real Tank tab with its exact solution and SWMM export, and wrote the Doc and its Word copy. The checks are mechanical. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 1.0 (2026-10-25): first single-file edition (the version read).
