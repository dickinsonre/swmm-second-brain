---
name: Lever Espresso Machine
file: lever-espresso-machine.html
version: 2026-10-20
date: 2026-10-20
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/Wkuu66UaoVZThwAihF95e4", repo: none}
engines: none (one small model, model(step, t), in the page's script)
units: metric as built (g, bar, °C, mm); US customary conversions below are ours
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says: Built with AI assistance (Claude). See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/Wkuu66UaoVZThwAihF95e4, version 1792532163-8fba (index.html, 51,322 bytes, SHA-256 2650b8447779f02a08d1d13731b8881ba3e61195b2f1d385a082f068c9f12f85), its page read in headless Chromium and from its markup on 2026-11-18. Nothing was run to write this file."
---

# Lever Espresso Machine: how a spring-lever espresso machine makes coffee, step by step

## In three points
- **What:** An animated cutaway of a one-group spring-lever espresso machine, answering "How does an espresso machine make coffee?" in eight steps: grind 18 g, tamp, lock in, pull the lever, let go, steam the milk, pour, new cup, in real time or three times faster. Gauges show boiler and brew pressure, spring force, puck height, flow, shot time and ratio. Not a water-modeling app.
- **So what:** The big idea is that a spring makes the pressure: pressure is spring force over piston area, and as the spring extends with a constant puck resistance the brew pressure falls as p(t) = 9 x (6/9)^(t/22) bar, from about 130 psi to 87 psi (9 to 6 bar, psi ours) over the 22 s after you let go. A table grades every number as solid, estimate or illustration, with its source or reasoning.
- **Now what:** Use it as a friendly example of a physical model that says how sure it is of each number. The numbers come from a simple model, not measurements on a real machine; the piston diameter (49 mm, about 1.9 in, ours) is a guess, and every number derived from it is an estimate.

This summary was written after the fact. The page ships no technical summary of its own and gives no version or date; the artifact was last published on 20 October 2026. The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Steps 1 to 8 with a speed switch. Recipe: 18 g in, 36 g out in 27 s (a 1:2 ratio in 25 to 30 s is the common modern guideline, "a recipe, not physics"). Boiler 1.1 bar (about 16 psi, ours) with steam at 122 °C (about 252 °F, ours), computed from the Antoine equation at 2.1 bar absolute. Spring force 1.70 falling to 1.13 kN, spring rate 278 N per cm (derived). Stroke 20.4 mm, 38.4 mL (derived). About 20 g of water kept by the puck; 10% strength assumed; milk 150 g heated from 4 to 62 °C in 36 s, implying about 0.95 kW of steam and about 14 g of steam condensed (energy balance with latent heat 2,194 J/g). The cutaway draws the piston stroke 2.5 times taller than the model's so it can be seen to move.

## Checks (as stated on the page)

Each number carries a grade (solid, estimate, illustration) and its source or reasoning in the "Where the numbers come from" table. No other checks are stated.

## What this does not show

As the page states: the numbers come from a simple model, not from measurements on a real machine; the model ignores puck erosion and heat loss; the piston size is a guess.

## Credits and licenses

The Antoine equation; steam tables. No license is stated for the page.

## AI use

The page says: "Built with AI assistance (Claude)." It says no more about who did what. This summary was written by Claude (Anthropic) on 18 November 2026 from the published page.

## Changes

- No version history on the page (the version read was published on 20 October 2026).
