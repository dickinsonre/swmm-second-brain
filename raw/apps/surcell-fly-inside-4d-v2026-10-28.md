---
name: Surcell
file: surcell-fly-inside-4d.html
version: "2026-10-28"
date: 2026-10-28
written: 2026-11-18
author: Robert Dickinson
links: {netlify: "https://surcell-fly-inside-4d.netlify.app", artifact: "https://claude.ai/artifact/6gFmSRkT8uHrEPV2YHJZG7", repo: none named in the page}
engines: none (a WebGL 2 ray tracer of curved 3D spaces; no water model)
units: none (lengths in model units and neck radii)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says the flight app reached its import as a finished file supplied by Robert Dickinson, with no record of who wrote it or with what tools, and that Claude did the import in October 2026. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/6gFmSRkT8uHrEPV2YHJZG7, version 1793232062-aa89 (index.html, 463,123 bytes, SHA-256 e4c7472a686310d831805907a53064278c274617cea642dd7d39b7a80ed390e1). The page did not finish loading in headless Chromium, so its text was read from the HTML source on 2026-11-18. Nothing was run to write this file."
---

# Surcell: fly inside the 3D boundary of a 4D shape

## In three points
- **What:** A flight game in curved three-dimensional worlds that sit in four dimensions: each world is the set of 4D points where one formula is zero (the 3D boundary, or "surcell", of a 4D shape, or a near relative). Ten worlds (Glome, Spheritorus, Torisphere, Tiger, Ditorus, Hyperbolic, Catenoid, Helicoid, Schwarz P, Revolution with profile curves), light traced live along geodesics on the graphics card, gravity toward a painted ground, donuts to eat, and a panel that measures the curvature where you stand.
- **So what:** It teaches what Gauss proved in 1827 with an ant on a doughnut: you can measure the shape of a space from inside it. The page computes the lemniscate cosine for the 4D catenoid with four steps of the arithmetic-geometric mean, good to a part in a trillion against the defining integral, and shows that the 4D catenoid stays inside a slab 2.62 neck-radii thick.
- **Now what:** Fly it in a browser with WebGL 2, drop a marker and walk a loop to see it come round. It is not a water app. Rendering was checked only in software WebGL, and no person has flown this build on real hardware.

This summary was written after the fact. The page ships no technical summary of its own and gives no version number; the version above is its import date ("Imported 28 October 2026"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Keys: W A S D move, Q E yaw, R F pitch, Space jump, X autopilot, G gravity, M marker, T teleport side, Y tiling, H honeycomb. Tabs: Fly, About, Doc. Each world's table row gives its topology and what space does to light (the Glome focuses all rays at the far pole; the Hyperbolic world spreads them and far things shrink fast; the Catenoid and Helicoid are exactly minimal, zero mean curvature). Custom profiles rho(w) are spun round in 4D; "Copy link to this view" saves position and heading.

## Checks (as stated on the page)

Mechanical comparisons: closed-form curvature; the lemniscate's defining integral; Gauss-Bonnet; an independent Gram-matrix calculation of honeycomb edges; 72 timed loop walks. The import found and fixed five defects, listed on the page.

## What this does not show

As the page lists it: rendering was checked in a software WebGL, not on a GPU; Schwarz P is an approximation of the true 4D minimal sponge and is not smooth at c = 0; the Helicoid has no recentring outward (76 units after a 300-unit walk) and 32-bit GPU numbers will blur a very long walk; the shader holds 40 to 128 objects depending on the card; collisions can push autopilot off a loop; on the Peanut profile only 2 of 12 planned donuts find room; the essay's history claims were not re-checked by a person.

## How to reproduce

Open the page in a browser with WebGL 2; the Doc page explains each check.

## Credits and licenses

Carl Friedrich Gauss (1827 theorem; the 1799 diary entry on the arithmetic-geometric mean); Jakob Bernoulli's lemniscate (1694). No license is stated for the page.

## AI use

The page says: the flight app itself, every world, the ray tracer and the instruments reached the import as a finished single HTML file supplied by Robert (Bob) Dickinson, and the import does not record who wrote that file or with what tools. Claude, Anthropic's AI model, did the import in October 2026 at Bob's direction: it ran the app headless, wrote and ran the checks, fixed five defects, added the About and Doc pages and the light theme, and wrote the Doc essay, its nine figures and the .docx. This summary was written by Claude on 18 November 2026 from the page's source.

## Changes

- 2026-10-28: the import read.
