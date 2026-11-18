---
title: "S370: Sisu Fire Control Drill, summary written from the page (v1.0)"
type: source
raw: raw/apps/sisu-fire-control-drill-v1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-11
ingested: 2026-11-18
tags: [apps, games, fiction, not-water]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app Sisu Fire Control Drill, version 1.0: the computer scene from Heinlein's Citizen of the Galaxy, rebuilt as a game. Raw file: [raw/apps/sisu-fire-control-drill-v1.0.md](../../raw/apps/sisu-fire-control-drill-v1.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/MSot2bgiDo1t5DW2scwHmq, version 1794366952-8422 (index.html, 126,166 bytes, SHA-256 3725c1833efe226d9bcba5534a2574e2189dcdad520ce83479e3ddfb23529cf3), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file." Its AI-use section: "The page says: the app, its figures and essay were built with Claude, Anthropic's AI model, in a single chat session in November 2026 at the request of Robert (Bob) Dickinson, who chose the subject and asked in turn for a description of the scene, a picture of the computer, a playable version and the essay."

**Claims worth keeping** (all copied from the file)
- A drill built around one scene in Robert A. Heinlein's Citizen of the Galaxy (1957): the boy Thorby at the fire-control computer of the Free Trader Sisu. A raider closes in straight legs; you guess his next leg, the computer solves the intercept, and you have two missiles to stop him before his beam is in range. Not a water-modeling app.
- The engine passes 1,414 test assertions: the same seed gives the same run to the last digit, the raider's path does not depend on the time step, the aim point is exactly as far as the missile will fly, and with chance deviations off a correct read on a shot spanning one course change hit 303 times in 303. The charts come from 5,000 seeded runs per point.
- 1,414 assertions against the engine, all passing (determinism, step independence, intercept closure, 303 of 303 hits with deviations off, a raider left alone always reaches beam range, refused launches).
- The page loaded headless in both themes; the same seed and key presses gave the same result in each.

**Limits it states.** As the page lists it: Heinlein's computer (the console is a period guess); real fire control (two dimensions, no gravity, straight legs, instant turns, constant-speed missiles that cannot steer); the green curves are an upper bound for a firecontrolman who knows the raider's habit for certain. No person has checked the scene details against the novel or the history beyond the cited pages.

**Checked at ingest.** Read in full; nothing was rerun at ingest. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [Sisu Fire Control Drill (app)](../entities/sisu-fire-control-drill.md), [Apps summarized on 18 November 2026: calculators, toys and apps that are not about water](../concepts/apps-from-pages-calculators-toys-and-not-water.md).
