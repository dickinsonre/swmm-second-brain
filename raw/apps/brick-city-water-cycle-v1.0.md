---
name: Brick City Water Cycle
file: brick-city-water-cycle.html
version: "1.0"
date: 2026-10-24
written: 2026-11-18
author: Robert Dickinson
links: {netlify: "https://brick-city-water-cycle.netlify.app", artifact: "https://claude.ai/artifact/EpyKacUscNdqfMxdvEsA6Z", repo: none named in the page}
engines:
  - {name: EPA SWMM, version: 5.2.4, note: "run through swmm-toolkit 0.17.0 on 2026-10-24 while building; the 5-minute results are embedded in the page, which runs no engine"}
units: US customary (in, in/hr, cfs, ft, ac, ft3, gpm)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude in October 2026 under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/EpyKacUscNdqfMxdvEsA6Z, version 1792849940-43e0 (index.html, 181,361 bytes, SHA-256 f996e84794f8865610904763fa84218593350745974cc52270cc3a94fcebb04c), its About and Doc tabs read in headless Chromium on 2026-11-18 with three.js r128 supplied from a local copy. Nothing was run to write this file."
---

# Brick City Water Cycle: supply, wastewater and storm on one toy-brick board, with the storm drains run in EPA SWMM 5.2.4

## In three points
- **What:** An original toy-brick 3D model of a small town's water on a 96 x 64 stud board: the water it drinks, the water it flushes and the rain off its roofs, in sixteen stages from clouds to groundwater, each carrying the design numbers engineers use. The storm drains, the pond and the green infrastructure are a real EPA SWMM 5.2.4 model whose results the storm player replays.
- **So what:** The pond cuts the peak by 86 percent and does not reduce the volume one gallon. With a green roof, 18 rain gardens and 40,000 ft2 of pavers, runoff falls from 1.84 to 1.43 in and the pond's peak inflow from 100 to 77 cfs, yet the release to the river falls only 12 percent (14.4 to 12.6 cfs): the outlet orifice, not the rain, sets that number, so the pond and the gardens have to be designed together.
- **Now what:** Use it to teach the whole urban water cycle on one picture and the pond-plus-LID lesson with real engine numbers. Only the storm system is computed; supply and sewer flows are drawn, and heights are not to scale.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("Version 1.0 · 2026-10-24"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Scene, Storm, Stages, About, Doc. Drag to orbit, tap a numbered pin for a stage, toggle flow paths, X-ray the ground to see buried pipes. The storm: 2.5 in of rain in 2 hours on 33.7 ac, played at 12 simulated minutes per second, as built or with green infrastructure. Stage cards carry standards such as flocculation about 30 minutes, conventional sedimentation about 4 hours, rapid gravity filters at 2 to 6 gpm per ft2, and at least 0.2 mg/L disinfectant residual entering the mains. Export gives the two .inp files and the time series. Three.js r128, OrbitControls and gifenc load from jsDelivr.

## Results the page reports (EPA SWMM 5.2.4)

| Quantity | As built | Green infrastructure |
|---|---|---|
| Runoff volume, in | 1.84 | 1.43 |
| Infiltration, in | 0.64 | 0.86 |
| Peak inflow to pond, cfs | 100 | 77 |
| Peak pond depth, ft | 2.44 | 1.88 |
| Peak release to river, cfs | 14.4 | 12.6 |

## Checks (as stated on the page)

- Both runs finished with no errors, no warnings and no flooded nodes. Continuity: runoff -0.021% and routing -0.016% as built; -0.029% and -0.014% with green infrastructure.
- Rain volume by hand: 2.5 in x 33.7 ac / 12 = 7.018 ac-ft; SWMM reports 7.018.
- Pond mass balance: summed five-minute inflow minus outflow to the peak gives 172,949 ft3 against 70,000 ft2 x 2.44 ft = 171,100 ft3, 1.1% apart, from sampling a fast hydrograph every five minutes.
- The seven subcatchment polygons overlap by 0 ft2. The exported .inp files are the text that was run, byte for byte.
- Arithmetic we checked (ours): two of the printed hand checks do not multiply out as printed. 2.5 x 33.7 / 12 = 7.021, not 7.018; SWMM's 7.018 ac-ft implies 33.69 ac, so the 33.7 is rounded. 70,000 x 2.44 = 170,800 ft3, not 171,100; the printed figure implies about 70,120 ft2 or a depth of about 2.444 ft. Neither changes the page's point (a 1.1% gap from five-minute sampling).

## What this does not show

As the page lists it: drinking water and sanitary flows are drawn, not computed; heights are not to scale (at 25 ft per stud the tower would stand more than 300 ft tall); one design storm, with no dry-weather flow and no water quality; the stage design values come from published standards and were not computed; the LID and infiltration parameters are textbook values, not calibrated; no person has reviewed the design values, the essay or the scene geometry.

## How to reproduce

Export menu or Storm tab: the two .inp files; run them in EPA SWMM 5.2.4.

## Credits and licenses

EPA SWMM; swmm-toolkit; FHWA water balance against impervious cover (after Livingston and McCarron, 1992); EPA WaterSense (82 gal per person per day); 40 CFR Parts 133 and 503; EPA Surface Water Treatment Rules; Ten States Standards; three.js r128; gifenc 1.0.3. No license is stated for the page.

## AI use

The page says: built with Claude, Anthropic's AI model, in October 2026 under the direction of Robert (Bob) Dickinson, who asked for a toy-brick 3D scene of the urban water cycle and supplied a reference photo of a brick-built water plant; the board is an original layout, not a copy. Claude designed the layout, wrote all the code, chose the storm, pipe, pond and LID parameters, ran both SWMM scenarios, and wrote the stage notes, the Doc essay, its figures and the Word copy. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 1.0 (2026-10-24): first version (the version read).
