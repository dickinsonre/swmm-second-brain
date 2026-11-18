---
name: Sisu Fire Control Drill
file: sisu-fire-control-drill.html
version: "1.0"
date: 2026-11
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/MSot2bgiDo1t5DW2scwHmq", repo: none}
engines: none (a seeded intercept engine written for the page)
units: thousands of miles on an invented scale
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude in a single chat session in November 2026 at Robert Dickinson's request. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/MSot2bgiDo1t5DW2scwHmq, version 1794366952-8422 (index.html, 126,166 bytes, SHA-256 3725c1833efe226d9bcba5534a2574e2189dcdad520ce83479e3ddfb23529cf3), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# Sisu Fire Control Drill: the computer scene from Heinlein's Citizen of the Galaxy, rebuilt as a game

## In three points
- **What:** A drill built around one scene in Robert A. Heinlein's Citizen of the Galaxy (1957): the boy Thorby at the fire-control computer of the Free Trader Sisu. A raider closes in straight legs; you guess his next leg, the computer solves the intercept, and you have two missiles to stop him before his beam is in range. Not a water-modeling app.
- **So what:** The engine passes 1,414 test assertions: the same seed gives the same run to the last digit, the raider's path does not depend on the time step, the aim point is exactly as far as the missile will fly, and with chance deviations off a correct read on a shot spanning one course change hit 303 times in 303. The charts come from 5,000 seeded runs per point.
- **Now what:** Play it, and read the Doc on the naval rangekeepers that Heinlein knew. It does not show Heinlein's computer (he did not describe one closely enough) or real fire control (flat two-dimensional space, instant turns, unsteered missiles), and the scene details come from memory of the novel, not checked against the printed page.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("Version 1.0, November 2026"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Drill, Console, Log, About, Doc. A launch that cannot arrive before the raider reaches beam range is refused and you keep the missile; every accepted shot spans at least one course change, so the guess always matters. The raider follows one of four habits, with a 12% chance of a deviation. Single file, no network calls.

## Checks (as stated on the page)

- 1,414 assertions against the engine, all passing (determinism, step independence, intercept closure, 303 of 303 hits with deviations off, a raider left alone always reaches beam range, refused launches).
- The page loaded headless in both themes; the same seed and key presses gave the same result in each.

## What this does not show

As the page lists it: Heinlein's computer (the console is a period guess); real fire control (two dimensions, no gravity, straight legs, instant turns, constant-speed missiles that cannot steer); the green curves are an upper bound for a firecontrolman who knows the raider's habit for certain. No person has checked the scene details against the novel or the history beyond the cited pages.

## Credits and licenses

Robert A. Heinlein, Citizen of the Galaxy (Scribner's, 1957; serialized in Astounding Science Fiction, September to December 1957), the scene reconstructed, not quoted; National Archives, Pieces of History blog, on Heinlein's Navy service; Thomas Wildenberg, The Revolutionary Rangekeeper, Naval History, October 2015; Warship Wednesday on USS Roper. By Robert (Bob) Dickinson, SWMM Enablement. Not affiliated with the Heinlein estate or any publisher; no text from the novel is reproduced.

## AI use

The page says: the app, its figures and essay were built with Claude, Anthropic's AI model, in a single chat session in November 2026 at the request of Robert (Bob) Dickinson, who chose the subject and asked in turn for a description of the scene, a picture of the computer, a playable version and the essay. Claude recalled the scene, designed the drill and its rules, wrote the engine, the page, the tests and the simulation, drew every figure, looked up the naval history in the cited sources, and wrote the text in the manner of Heinlein's engineering explanations without quoting him. The checks are mechanical. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 1.0 (2026-11): first version (the version read).
