---
name: Chanakya's Counsel for SWMM
file: chanakya-swmm5-swmm6.html
version: 1.6.0
date: 2026-10-20
written: 2026-11-18
author: Robert Dickinson
links: {netlify: "https://chanakya-swmm5-swmm6.netlify.app", artifact: "https://claude.ai/artifact/DAmSUwjkmJT4qppSYm3BH6", repo: none named in the page}
engines:
  - {name: EPA SWMM, version: 5.2.4, note: "compiled from source; 64 runs of one sample model, all in the page's evidence package"}
units: US customary (in, cfs, ac-ft)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude in Claude Code sessions in October 2026 under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/DAmSUwjkmJT4qppSYm3BH6, version 1792434855-a876 (index.html, 2,133,599 bytes, SHA-256 18809cc3172052a84151227580a0ae3458aa4d6477f8fc0d9a7dc3ffcc88b5ee), its room, Sources and Doc tabs read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# Chanakya's Counsel for SWMM: Arthashastra statecraft applied to SWMM decisions

## In three points
- **What:** A decision app that walks one SWMM drainage decision through five stations taken from Kautilya's Arthashastra (Shamasastry's 1915 translation, paraphrased): Brief (purpose and criteria), Audit (input slips, after the text's forty ways to embezzle), Spies (independent checks, after three sources that agree), Alternatives (six measures) and Writ (a decision memo). The measures run in EPA SWMM 5.2.4 on one sample model.
- **So what:** It turns statecraft into modeling discipline: ask why before running, audit the input file for slips the engine passes without a word, accept a result only when independent checks agree, compare all six measures at the decision storm, and write the decision down. The page marks the pairing with modeling as its own analogy ("Kautilya wrote about kings") and says one popular "three questions" saying is not in the Arthashastra at all.
- **Now what:** Use it to structure a design review. It covers one sample network, one two-hour storm shape and no cost or water quality; the meter reading is invented for teaching.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("v1.6.0, 2026-10-20"). The file name above is the Netlify site's. Every number below is copied from the page. Nothing was run to write this file.

## What it does

A counsel room with numbered places, one per station; the table shows the measure being carried at the decision storm (a pool at J3 means it floods there), and a wall board shows flooding for all six measures. The opening state carries "War: enlarge the pipe", with a 2.0 in decision storm and an outfall peak of 42.3 cfs. The Sources tab sets every idea beside its book and chapter (for example II.8, II.9, I.12) and what the app does with it. Work is saved locally; Export holds Save, Load and Reset.

## Checks (as stated on the page)

Three separate builds of the engine reproduce every packaged report exactly. A regression suite drives the app in a simulated browser, with further checks in Chromium with axe-core. A script traces every number in the essay to its source. For 1.6, five separate Claude reviewers, none of which had seen the build history, checked the claims, code, accessibility, citations and importer.

## What this does not show

As the page lists it: cost; calibration (no observed data); any network but this one; any storm shape but a single two-hour peak; water quality; other solver settings (the runs use dynamic wave, a 5 s variable step and partial inertial damping; with damping off, storage at J3 floods 0.014 ac-ft at 2.0 in, and kinematic wave nearly quadruples the base flooding); the hand calculations use full-pipe Manning and a triangular hydrograph. No person has checked the essay's history or quotations against the printed books, and no screen reader, Safari or Firefox has been tried.

## How to reproduce

The page's evidence package holds all 64 engine runs; the Doc tab also reports reruns on other engine builds and solver settings, which are not packaged.

## Credits and licenses

Kautilya's Arthashastra, R. Shamasastry's 1915 translation (quotations gathered from web transcriptions); EPA SWMM 5.2.4 (public domain). No license is stated for the page.

## AI use

The page says: built with Claude, Anthropic's AI model, in Claude Code sessions in October 2026 under the direction of Robert (Bob) Dickinson, who asked for it, set its subject and brought nine outside reviews to it, and for 1.6 asked for a deep dive and the Doc essay. Claude wrote the code and every text, built the sample model, compiled EPA SWMM 5.2.4 and ran all 64 cases, drew the figures and wrote the essay with itself as narrator. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 1.6.0 (2026-10-20): deep dive with five independent reviewers; Doc essay. The version read.
