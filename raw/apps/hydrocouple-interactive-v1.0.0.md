---
name: HydroCouple Interactive
file: hydrocouple-interactive.html
version: 1.0.0
date: 2026-11-13
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: private claude.ai artifact, repo: none}
subject: https://www.hydrocouple.org (read 2026-11-13; unofficial, not affiliated)
engines: none (no SWMM, HydroCouple or other engine is embedded or called)
units: US customary (cfs, MGD, ft, ft/s, acre-feet); the labs marked dimensionless are synthetic
dependencies: none (no libraries, fonts, images or network requests)
ai_use: built with Claude (Anthropic); see AI use
---

# HydroCouple Interactive: the six pages of hydrocouple.org, with 18 diagrams you can operate

## In three points
- **What:** Restates the six pages of hydrocouple.org and turns its eight static figures into 18 working diagrams and labs; unofficial, a snapshot of 2026-11-13.
- **So what:** 40 of 40 math checks pass, and one overturned an expectation: an adapter holding a 120 cfs hydrograph at a 5 min step keeps the volume exactly and still shifts its center of mass by 7.5 min.
- **Now what:** Use it to learn HydroCouple's ideas by operating them, then go to the site. No engine runs, the labs are synthetic, and no person has checked the paraphrases against the site.

**In one sentence.** HydroCouple Interactive restates the six pages of hydrocouple.org and rebuilds its eight static figures as 18 working diagrams and labs, backed by 40 passing math checks, so a reader can operate the ideas instead of only reading them.

**In one paragraph.** HydroCouple is Caleb Buahin's open architecture for coupling water models, with Open-Source SWMM 6.0 at its center. Its website explains the idea in six pages and eight static figures. This app, which is unofficial, restates those pages in its own words and turns the figures into diagrams that respond: boxes that explain themselves, a storm you can trace through the stack, an adapter you can break, a derivative chain you can run in both directions. Forty automated checks back the numbers. One of them overturned an expectation: an adapter can balance volume to 0.00 percent and still hand the next model a wrong hydrograph. The app is a snapshot of November 13, 2026. It runs no engine, and the site remains the authority.

## What it does

It mirrors hydrocouple.org tab for tab (Home, Standards, Ecosystem, Articles, Publications, Docs) for engineers who want to understand HydroCouple and Open-Source SWMM 6.0 (SWMM2D) quickly. Text is paraphrased; titles, names, numbers, dates and links are as printed on the site. Each section links to its source page. Static figures are replaced by clickable node-and-link diagrams and seven small computations. Two more tabs, About and Doc, hold provenance and a long-form essay.

## Site inventory as read

| Page | Content carried |
|---|---|
| Home | themes, three design ideas, architecture figure (4 inputs, 6 interface names, engine, 4 components, 3 applications), 3 flagship cards, 5 stat tiles |
| Standards | status (interface 2.0.0-alpha.2, C++20, Python bindings, MIT), 3 pillars, 5 lifecycle phases, coupling contract, Jacobian/JVP/VJP, checkpoint and replay scope, 3 application cards, 4D-Var cycle, 3 data cards, 6-row interface contract table, 4 primary sources |
| Ecosystem | ring of hub plus 7 neighbors, 20 projects (15 available, 5 planned), 3 AI and physics cards, benchmark platform (1,396 models, 5 dimensions stated, 3 described, 5 corpus categories) |
| Articles | 8 notes dated 2026-04-23 to 2026-10-04; authors Caleb Buahin (6) and Corinne Wiesner-Friedman (2); 2 to 3 sentence summaries |
| Publications | 9 papers (2 foundational, 3 in preparation, 4 applied), 13 authors |
| Docs | 8 documentation sets (2 standard, 6 flagship) with links |

## The 18 interactive diagrams and labs

1. Home: glue-script slider. 2. Home: layered architecture with Trace a storm. 3. Home: site map.
4. Standards: lifecycle stepper. 5. Standards: coupling strip plus adapter lab. 6. Standards: derivative chain, forward and reverse. 7. Standards: uncertainty propagation. 8. Standards: checkpoint and replay stepper. 9. Standards: hybrid physics and learning. 10. Standards: 4D-Var cycle. 11. Standards: 4D-Var on one store.
12. Ecosystem: ring. 13. Ecosystem: three AI loops.
14. Articles: timeline. 15. Articles: Preissmann slot lab. 16. Articles: RTK lab with parameter count.
17. Publications: co-author network. 18. Docs: documentation tree.

## How it computes

All numbers come from `src/model.js` (object `HCModel`, inlined in the HTML).

- Glue arithmetic: `scripts = n(n-1)/2`, `wrappers = n`. This app's illustration, not a site figure.
- Adapter: source is a triangle hydrograph, peak qp at 45 min, base 2.67 x 45 min, sampled every 15 min to 180 min. Receiver samples at 1, 5, 15, 30 or 60 min by linear interpolation `q(t) = q_i + (q_i+1 - q_i)(t - t_i)/(t_i+1 - t_i)` or by holding the last value. Units: `MGD = cfs x 0.646317`. Volume by trapezoid (linear) or rectangle (hold). Timing by center of mass.
- Derivative chain: `A = [[1, 0.2], [0.1, 0.8]]`, `B = [[1.2, 0.4], [0.3, 0.9]]` (as printed on standards.html), `M = diag(gain, 1)`, `J = B M A`, `Sigma_y = J Sigma_x J^T`, JVP of tangent (0.01, 0), VJP for L = output 1. Input 2 standard deviation fixed at 0.10. Default gain 1.00 is this app's choice; the site does not print its default.
- Replay: `x[k+1] = x[k] + dt (u[k] - c x[k]^1.5)`, dt = 1, c = 0.3, u = (1.2, 0.8, 0.4), L = x[3]. Reverse: `lambda[k] = lambda[k+1] (1 - 1.5 c dt x[k]^0.5)`, `dL/du[k] = lambda[k+1] dt`.
- 4D-Var: `x[t+1] = 0.85 x[t] + 0.5 r[t]`, 12 steps, truth x0 = 2.0, background x0 = 1.0, six observations at even steps with fixed noise. `J(x0) = 0.5 (x0 - xb)^2 / sb^2 + 0.5 sum (x[t] - y[t])^2 / so^2`. Gradient by one backward sweep; analysis in closed form because J is quadratic in x0.
- Preissmann slot: `T_slot = g A / c^2`, g = 32.174 ft/s2, A = pi D^2 / 4. Textbook formula; the dynamic slot method of the article is not implemented.
- RTK: triangle with peak `2R / (T(1+K))` at T, base `T(1+K)`; three fixed (T, K) pairs: (1, 2), (4, 3), (12, 5) hours.

## Inputs and outputs

No file input. Output: CSV per tab through the Export button (site inventory, interface contracts, projects, articles, publications, docs links), and an optional WebM walkthrough recording where the browser allows screen capture. The technical summary (this file) is embedded in the HTML as `<script type="text/markdown" id="app-md">`.

## Checks

Mechanical, `node test/math.test.js`, 40 of 40 passing in the build that produced this file:

- Glue: pairs for n = 2, 3, 5, 8 are 1, 3, 10, 28; break-even at n = 3.
- Adapter, qp = 120 cfs: source volume 432,646.7 ft3 = 9.93 ac-ft. Linear at 1, 5, 15 min returns the same volume (tolerance 1e-6 ft3) and the same center of mass, 55.07 min. Hold at 5 min returns the same volume and a center of mass of 62.57 min: shift exactly 7.5 min. Linear at 30 min: peak seen 96.05 cfs, volume error -6.63 percent. 120 cfs = 77.558 MGD.
- Jacobian at gain 1: J = [[1.24, 0.56], [0.39, 0.78]]. Sigma inputs (0.15, 0.10), rho 0: output standard deviations 0.19425 and 0.09750, output correlation 0.805. JVP (0.0124, 0.0039). VJP (1.24, 0.56). Seeded Monte Carlo, 200,000 samples: 0.19447 and 0.09741.
- Replay, x0 = 1.0: x = (1, 1.9, 1.9143, 1.5197); dL/du = (0.1433, 0.3774, 1.0); dL/dx0 = 0.07882. All four match central finite differences within 1e-7. Reverse pass from the final state only gives dL/dx0 = 0.0883, 12 percent high.
- 4D-Var: backward-sweep gradient equals finite difference at (sb, so) = (0.5, 0.1), (1, 0.1), (0.2, 0.5); gradient at the analysis is zero within 1e-9. Analysis x0 = 2.001 at (0.5, 0.1) and 1.777 at the app default (0.5, 0.3).
- Slot: 1 percent slot on a 3 ft pipe gives 87.07 ft/s; width and celerity functions invert each other.
- RTK: triangles with R = 0.02, 0.03, 0.05 integrate to 0.10.

Rendering: loaded in headless Chromium at 1280 px and 375 px, dark and light themes, all eight tabs, no console errors, no horizontal overflow; each diagram operated once. Colour: contrast-check.js run on both palettes.

Human review: none yet of the paraphrases against the site.

## What this does not show

1. It is a snapshot of 2026-11-13. The site changes.
2. Article bodies (about 144,000 characters on one page) are reduced to a few sentences each. No article equations, figures or results are reproduced.
3. No engine runs. All labs are synthetic.
4. The glue arithmetic, the SWMM lifecycle analogy and all click-through notes are this app's, not the site's.
5. Not read: API reference, engine manuals, benchmark dashboard, GitHub source. Outbound links were taken from the fetched pages and not each opened.
6. Five apparent inconsistencies on the site, listed in the About tab, need a person to confirm: an `#ai` anchor that may not exist on ecosystem.html; five benchmark dimensions stated and three described; interface names on the home figure versus the Standards table; two descriptions of FVQual; Apache-2.0 (home page) versus an MIT license link (May 2026 alpha announcement) for the engine.
7. Screenshots and the HydroCouple logo are not copied.

## How to reproduce

`node build.js` runs the tests, then assembles `dist/hydrocouple-interactive.html` from `src/`. `node doc/build-docx.js` writes the .docx from `doc/essay.js` and `doc/figs.js`, the same sources as the Doc tab.

## Credits and licenses

HydroCouple and Open-Source SWMM 6.0 (SWMM2D): Caleb Buahin and contributors, (c) 2014 to 2026 HydroCouple. Articles: Caleb Buahin and Corinne Wiesner-Friedman. The site states the HydroCouple interface is MIT licensed. This app contains no HydroCouple code, text or images and is not affiliated with or endorsed by HydroCouple. App code: Robert Dickinson with Claude.

## AI use

Built with Claude, Anthropic's AI model, in one session in November 2026, at the direction of Robert Dickinson, who chose the subject and the form and is responsible for publishing it. Claude read the six pages of hydrocouple.org through a web fetch tool, wrote every paraphrase, designed and coded the diagrams and labs, wrote the math functions and their 40 tests, and wrote the About tab, the Doc essay, the .docx and this file. The math was checked by the automated tests; the rendering in a headless browser. Not yet checked by a person: the paraphrases against the site, the five observations, and the outbound links.

## Changes

`1.0.0 (2026-11-13)`: first build.
