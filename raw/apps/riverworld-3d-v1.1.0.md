---
name: Riverworld in 3D
file: riverworld-3d.html
version: 1.1.0
date: 2026-11-17
author: Robert Dickinson (requested); built with Claude, see AI use
links: {netlify: none yet, artifact: private Claude artifact, repo: none}
engines:
  - {name: rw-core, version: 1.1.0, source: inline script "rw-core" in the html, license: none stated}
  - {name: three.js, version: r128, source: cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js, license: MIT}
units: US customary (miles, feet, cfs, horsepower); GW shown beside horsepower
ai_use: built with Claude (Anthropic); see AI use
---

# Riverworld in 3D: a 3D model of Philip José Farmer's river planet, with three engineering checks

## In three points
- **What:** A 3D model of Philip José Farmer's Riverworld at four zoom levels (globe, 60 miles of neighbouring reaches, a 10-mile valley at true scale with an eye-level bank view, and the polar sea), with three engineering checks on the novels' dimensions: surface budget, grailstone seats, and the fall the River needs.
- **So what:** A 9-mile valley on an Earth-size planet has room for 21.9 million miles of River, so both of the books' lengths fit (10 million miles uses 46% of the surface, 20 million 91%). Grailstones at 700 seats seat 39% or 78% of the 36 billion people, and a 3 ft/s River at n 0.03 and 7,920 ft deep needs 5,308 ft of fall over 10 million miles; 61 of 61 checks pass.
- **Now what:** Use it for the books, or as a worked Manning example at planetary scale. Every book figure came through secondary sources, the course is a guess, the planet view draws 24 switchbacks where 632 are called for, and no person has reviewed the page.

This is a 3D model of Philip José Farmer’s Riverworld with the engineering checked: a 9-mile valley on an Earth-size planet has room for 21.9 million miles of River, so both of the books’ lengths fit.

Riverworld in 3D is a single web page that draws Philip José Farmer’s river planet at four levels you can zoom through: the whole globe with the River wound across it, sixty miles of country where neighbouring reaches lie side by side with the mountains between them, ten miles of valley at true scale down to eye level on the bank, and the polar sea with its tower. Every dimension comes from the novels as summarized in checked sources or is marked as assumed. One set of functions computes the surface budget, the grailstone count and the Manning slope, and feeds the model, the charts and this document. 61 automated checks pass. The globe is a diagram, and nothing here was checked against the novels’ own pages.

## What it does

Draws the Riverworld setting in four WebGL scenes (planet; a 64 by 40 mile patch of neighbouring reaches at true scale; a 10-mile valley reach with an eye-level bank view; north polar sea). Zooming in past the closest view moves planet to reaches to valley, and zooming out moves back. It and computes whether the published dimensions close: surface budget, grailstone seats, and the fall the River needs. For readers of the books and for hydraulic engineers who want a worked Manning example at planetary scale. Output is on screen; "Copy numbers" gives the current figures as text.

## How it computes

All functions are in the inline script `rw-core` (also `src/core.js`).

- Sphere area: `A = 4 pi R^2`. R = 3,958.8 mi (Earth mean radius, assumed).
- Longest river that fits: `Lmax = A / w`, w = valley width.
- Surface share: `L w / A`.
- Switchbacks per hemisphere, east-west course: `N = L / (4 R)` (a half circle of latitude averages 2R).
- Spacing of neighbouring reaches: `pi R / N`. Rock between reaches: `spacing - w`.
- Grailstones: `2 L / spacing_stone`. Seats: `stones x seats_per_stone`. Length to seat all: `pop x spacing_stone / (2 x seats_per_stone)`.
- Manning (US): `V = (1.486/n) Rh^(2/3) S^(1/2)`, rectangular section, `Rh = W D / (W + 2D)`. Slope for a given V: `S = (V n / (1.486 Rh^(2/3)))^2`. Fall: `S x L x 5280` ft.
- Discharge `Q = V W D`. Power `P = 62.4 Q H / 550` hp.
- Terrain, miles: `ground(xr, z, wallMi)` gives height and zone across one valley (River 1.5 mi wide, plain, foothills to about 1,000 ft, wall at full height 4.35 mi from the axis). `groundReaches(x, z, sp, wallMi)` repeats it every `sp` miles, where `sp` is the calculated spacing of reaches.
- Drawn course: `riverPath(N)` returns colatitude and longitude points in flow order: polar sea rim (colatitude 12 deg), N east-west bands across longitudes 8 to 172 deg stepping south to colatitude 172 deg, a crossing, then the mirror image north across 188 to 352 deg. Meander amplitude 0.16 of a band; valley ribbon 0.60 of a band wide.

## Inputs and outputs

No files are read or written. Inputs are sliders. Constants and their sources:

| Quantity | Value | Source |
|---|---|---|
| River length | 10,000,000 mi (Books I to III); 20,000,000 mi (first supposition) | Wikipedia, "Riverworld" |
| Valley width | 9 mi average | Wikipedia, "Riverworld" (archived copy) |
| River width | 1.5 mi | The Fabulous Riverboat, excerpt on Biblio |
| River depth | 1.5 mi average | Wikipedia, "Riverworld" |
| Grailstone spacing | 1 mi on each bank | The Fabulous Riverboat excerpt; Ruiz (1995) |
| Seats per grailstone | about 700 | Ruiz (1995) |
| Population | 36,006,009,637 | Wikipedia, "Riverworld" |
| Planet radius | 3,958.8 mi | assumed (Earth) |
| Velocity, Manning n, boat speed | 3 ft/s, 0.03, 15 mph | assumed |

## Checks

Mechanical, run by `node build.js` on 2026-11-17: 61 of 61 checks pass (`test/test.js`).

| Result | 10 million mi | 20 million mi |
|---|---|---|
| Longest river that fits a 9-mile valley | 21.9 million mi | same |
| Surface used | 46 % | 91 % |
| Switchbacks per hemisphere | 632 | 1,263 |
| Spacing of reaches | 19.7 mi | 9.8 mi |
| Rock between reaches | 10.7 mi | 0.8 mi |
| Grailstones | 20.0 million | 40.0 million |
| People per stone | 1,800 | 900 |
| Seats at 700 per stone | 14.0 billion (39 % of people) | 28.0 billion (78 %) |
| Fall at 3 ft/s, n 0.03, 7,920 ft deep | 5,308 ft | 10,616 ft |
| Boat at 15 mph, end to end | 76 yr | 152 yr |

- Length to seat everyone at 700 per stone: 25.7 million mi (more than fits).
- Fall for a 30 ft deep river, 10 million mi: 397 mi.
- Discharge 188.2 million cfs; power to lift it 5,308 ft: 113.3 billion hp (84,509 GW).
- Band-by-band sum of half circles of latitude reproduces 10 and 20 million mi within 0.1 %.
- Drawn course at 24 switchbacks: 407,443 mi; no step longer than one band; neighbouring valley ribbons do not overlap (least gap 0.76 of a band against a ribbon 0.60 wide).
- Terrain: River 1.5 mi wide; plain dry and within 40 ft of the water; foothills under 1,100 ft; wall at 90 % of full height 4.5 mi from the axis; rock between neighbouring valleys above 75 % of wall height at both lengths.
- Browser check: opened in headless Chromium, four scenes, the zoom-through, the dive, the bank view and four tabs rendered in both themes without console errors; contrast checker passed.
- Complexity: SWMM App Complexity Meter analyzer not run for this build; raw counts only: 1,357 hand-written source lines in 9 files, 61 checks.
- Human review: none yet.

## What this does not show

1. The planet view is a diagram: 24 switchbacks drawn against 632 or 1,263 called for.
2. The east-west course is a guess; the sources give no map. The Reaches scene draws reaches straight and parallel at the calculated spacing.
3. Plain and foothill widths are by eye. Mountain wall drawn at 20,000 ft from the builder's recollection, not confirmed by a source.
4. Polar sea, gaps and tower have no sourced dimensions.
5. Stones, huts and the boat are oversized, less so in the bank view; river bed not drawn to depth.
6. Hydraulics: rectangular section, uniform flow, single n and V.
7. Every book figure came through secondary sources; none checked against the novels.
8. No person has reviewed the page.

## How to reproduce

`node test/test.js` prints each check. `node build.js` reruns them and rebuilds the page and this file. `node build-docx.js` builds the Word document from the same essay. In the app, Numbers tab, "Reset to the stated figures" returns every slider to the values above.

## Credits and licenses

Riverworld is the creation of Philip José Farmer (1918 to 2009). Unofficial reader's model; no text, artwork or characters from the books. three.js r128, MIT license, by the three.js authors. Sources: Wikipedia "Riverworld"; Antoine Ruiz, "Redemption in Philip José Farmer's Riverworld" (Université d'Avignon, 1995); Biblio excerpt of The Fabulous Riverboat; publisher's description of Gods of Riverworld.

## AI use

This page was built with Claude, Anthropic’s AI model, in one conversation in November 2026. Robert (Bob) Dickinson asked for a 3D model of Riverworld, and then asked to be able to zoom into the River and see the valley and the mountains. He did not specify the scenes, the checks or the sources.

What Claude did: searched for and read the sources listed on the About tab, chose the four scenes and the three checks, wrote the calculation functions, the 3D code, the figures, the tests, this essay, the Word document and the technical summary.

How the results were checked: 61 automated checks run at every build, the page was opened once in a headless browser and looked at, and color contrast was measured. Those checks cover the arithmetic and the drawing. No person has yet reviewed the page, the essay or the numbers, and no figure was checked against the novels themselves.

## Changes

`1.1.0 (2026-11-17)`: zoom into the River. New Reaches scene (neighbouring reaches and the mountains between, true scale, 10 or 20 million miles); scrolling past the zoom limit changes level; Dive to the River; Stand on the bank (eye-level view, walk with W A S D); shift-drag pan; terrain moved into rw-core with 9 new checks.
`1.0.0 (2026-11-17)`: first build. Three scenes, Numbers tab, Doc tab, .docx, this file.
