---
name: SWMM Enablement Showcase
file: swmm-enablement-showcase.html
version: 1.0
date: 2026-11-19
author: Robert Dickinson
links: {netlify: "not yet deployed (suggested site name swmm-enablement-showcase)", artifact: "https://claude.ai/artifact/MznecwPwqPM5HBCZjtKkLZ", repo: none}
engines: none (a gallery page; it links to the apps and runs none of them)
units: US customary, as the apps' own summaries give them
ai_use: "Written and built by Claude (Anthropic) on 2026-11-19 at Robert Dickinson's request, from the twelve apps' own technical summaries. See AI use."
---

# SWMM Enablement Showcase: twelve SWMM apps, each with one finding and one limit

## In three points
- **What:** One page that links twelve of Bob Dickinson's browser apps in four groups (Where SWMM came from; Inside the engine; Surfaces, meshes and sediment; How the claims are checked), each card with a screenshot, its Netlify address, one finding with its numbers and one limit.
- **So what:** Six of the twelve run EPA SWMM 5.2.4 in the browser; the other six show recorded runs of SWMM 5.2.4 and OpenSWMM 6, the engine source, a claims register or textbook formulas, and each card says which. Every finding and limit is copied from the app's own technical summary.
- **Now what:** Use it as the link to send someone who asks what the SWMM Enablement work is, for example a committee web page. It reflects the twelve apps as deployed on 17 November 2026 and checked on 19 November 2026.

## What it does
A static page. A header with a Dark, Light and Auto theme control (it opens dark; Auto follows the device). A hero with a drawing of a sewer profile (ground, three manholes, a surcharged pipe and its hydraulic grade line), which is an illustration and not a model result. Four bands of cards. A closing section on how the apps were picked, AI use and credits, and this summary in a collapsible panel.

## The twelve
| App | Address | Version and date (the app's own) | Engines, as the card states them |
|---|---|---|---|
| The Runoff Block | https://runoff-block.netlify.app | v1.1 · 2026-11-03 | EPA SWMM 5.2.4 in the page, SWMM 4.4H, SWMM 1 Runoff Block |
| OpenSWMM Code | https://openswmm-code.netlify.app | v1.0.0 · 2026-11-05 | No engine: a source atlas |
| SWMM5 Residual Walk | https://swmm5-residual-walk.netlify.app | v1.0 · 2026-11-04 | EPA SWMM 5.2.4 in the page |
| Non-Prismatic Channel Lab | https://non-prismatic-channel-lab.netlify.app | v1.0 · 2026-11-02 | EPA SWMM 5.2.4 in the page |
| The Rigid Column Test | https://rigid-column-test.netlify.app | Built 2026-09-30 | EPA SWMM 5.2.4, OpenSWMM 6.0.0-alpha.4, Runs recorded in the page |
| SWMM Rhythm Detector | https://swmm-rhythm-detector.netlify.app | v1.0 · 2026-11-06 | Reads EPA SWMM 5.2.4 output, No engine runs in the page |
| Walk the Mesh | https://walk-the-swmm6-2d-mesh.netlify.app | v1.0 · 2026-10-19 | EPA SWMM 5.2.4 in the page |
| Rain-on-Grid Workbench | https://rain-on-grid-workbench.netlify.app | v1.0 · 2026-10-06 | OpenSWMM 6, Runs recorded in the page |
| ICM Sediment Field Guide | https://icm-sediment-field-guide.netlify.app | v1.1 · 2026-11-02 | No engine: textbook formulas |
| SWMM Claim Frontier | https://swmm-claim-frontier.netlify.app | v1.0 · 2026-09-30 | No engine: a claims register |
| SWMM Engine Map | https://swmm-engine-map.netlify.app | Built 2026-10-29 | EPA SWMM 5.2.4 in the page, C++ and Rust ports |
| SWMM Clean Repro | https://swmm-clean-repro.netlify.app | v1.0 · 2026-10-13 | EPA SWMM 5.2.4 in the page |

## How it computes
Nothing is computed. A small script sets the theme from a stored choice (localStorage, wrapped in try/catch) or dark, and copies this summary into the panel. The screenshots are WebP files embedded as data URIs.

## Inputs and outputs
- In: the twelve apps' `.md` technical summaries (In three points, version, date, engines), and screenshots of each app taken in headless Chromium at 1280 by 800 in its dark theme, scaled to 800 by 500.
- Out: `swmm-enablement-showcase.html` (single file; `index.html` on Netlify) and this `swmm-enablement-showcase.md`.

## Checks
- Each card's finding and limit were compared with the app's own summary; numbers are unchanged. Some sentences were shortened or split.
- The twelve apps were checked on 19 November 2026 with first-minute.js (headless Chromium: script errors, dark first paint with the device set to light, 390 px phone width, values shown as NaN, undefined or Infinity, text contrast, a .md beside the page). Flagged items were looked at by hand. Items found and left as they are: one label in The Rigid Column Test's light theme at 2.06:1 contrast.
- This page was checked the same way, and at 390 px in both themes.
- The apps were checked from local copies of the deployed files; netlify.app could not be reached from the build machine.

## What this does not show
1. The apps' own checks are the apps'; this page repeats their stated findings and does not rerun them.
2. A screenshot shows the app's opening view only.
3. The apps may change after 19 November 2026; the version on each card is the one checked.
4. Three more apps (Visual SWMM, SWMM6 Hands-On Watershed and Four Ways to K) were fixed on 19 November 2026 and are not on the page until they are redeployed.
5. No person other than Bob has reviewed the page.

## How to reproduce
`python3 build.py [artifact URL]` beside `cards.py` and `template.html`, with the screenshots in `../webp/`. Screenshots: `node shoot.js <folder of deployed apps> shots`.

## Credits and licenses
EPA SWMM 5.2.4: US Environmental Protection Agency, public domain. OpenSWMM 6: HydroCouple, Apache-2.0. Rain-on-grid algorithms: Shrestha, Mustafa, Kennedy and McPhearson (2026), Urban Systems Lab. OpenSWMM 5.1.912: CHI. The apps are Robert Dickinson's (SWMM Enablement). Fonts: IBM Plex (SIL Open Font License), from Google Fonts.

## AI use
This page and this summary were written and built by Claude (Anthropic's AI model) on 19 November 2026 at the request of Robert (Bob) Dickinson. Claude proposed twenty candidates, wrote and ran the checks, looked at flagged items, took the screenshots, wrote the card text from each app's summary, and built the page. Bob approved the twelve and is responsible for publishing it.

## Changes
`1.0 (2026-11-19)`: first version.
