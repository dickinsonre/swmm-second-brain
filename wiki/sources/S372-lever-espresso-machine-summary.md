---
title: "S372: Lever Espresso Machine, summary written from the page (v2026-10-20)"
type: source
raw: raw/apps/lever-espresso-machine-v2026-10-20.md
kind: app-md
author: Robert Dickinson
published: 2026-10-20
ingested: 2026-11-18
tags: [apps, machines, not-water]
drafted_by: Claude (Anthropic), from the published page
reviewed: 2026-11-18
---
**What it is.** A technical summary of the app Lever Espresso Machine, version 2026-10-20: how a spring-lever espresso machine makes coffee, step by step. Raw file: [raw/apps/lever-espresso-machine-v2026-10-20.md](../../raw/apps/lever-espresso-machine-v2026-10-20.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/Wkuu66UaoVZThwAihF95e4, version 1792532163-8fba (index.html, 51,322 bytes, SHA-256 2650b8447779f02a08d1d13731b8881ba3e61195b2f1d385a082f068c9f12f85), its page read in headless Chromium and from its markup on 2026-11-18. Nothing was run to write this file." Its AI-use section: "The page says: "Built with AI assistance (Claude)." It says no more about who did what. This summary was written by Claude (Anthropic) on 18 November 2026 from the published page."

**Claims worth keeping** (all copied from the file)
- An animated cutaway of a one-group spring-lever espresso machine, answering "How does an espresso machine make coffee?" in eight steps: grind 18 g, tamp, lock in, pull the lever, let go, steam the milk, pour, new cup, in real time or three times faster. Gauges show boiler and brew pressure, spring force, puck height, flow, shot time and ratio. Not a water-modeling app.
- The big idea is that a spring makes the pressure: pressure is spring force over piston area, and as the spring extends with a constant puck resistance the brew pressure falls as p(t) = 9 x (6/9)^(t/22) bar, from about 130 psi to 87 psi (9 to 6 bar, psi ours) over the 22 s after you let go. A table grades every number as solid, estimate or illustration, with its source or reasoning.
- Each number carries a grade (solid, estimate, illustration) and its source or reasoning in the "Where the numbers come from" table. No other checks are stated.

**Limits it states.** As the page states: the numbers come from a simple model, not from measurements on a real machine; the model ignores puck erosion and heat loss; the piston size is a guess.

**Checked at ingest.** Read in full; nothing was rerun at ingest. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [Lever Espresso Machine (app)](../entities/lever-espresso-machine.md), [Apps summarized on 18 November 2026: calculators, toys and apps that are not about water](../concepts/apps-from-pages-calculators-toys-and-not-water.md).
