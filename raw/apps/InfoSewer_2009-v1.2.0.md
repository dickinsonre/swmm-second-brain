---
name: InfoSewer_2009
file: InfoSewer_2009.html
version: 1.2.0
date: 2026-11-12
author: Robert Dickinson
links: {artifact: "https://claude.ai/artifact/QKLaUj747DpmhJ5XsK6Csz (private)", netlify: none, repo: "SWMMBobSWMM6/swmm5-infosewer (private; engine only, the app is not in it yet)"}
engines:
  - {name: swmm5-infosewer, version: commit 12492d6, base: EPA SWMM 5.2.4, option: FLOW_ROUTING INFOSEWER, license: "EPA SWMM public domain; InfoSewer rules derived from Autodesk/Innovyze source, private"}
  - {name: InfoSewer engine (HeEngPkg), version: "MWH Soft / Innovyze 1996-2011", role: reference only, license: proprietary}
libraries:
  - {name: three.js, version: r128, source: cdnjs, license: MIT}
runs_engine_in_browser: false
units: US customary (ft, in, gpm, ft/s, ft3, hp)
ai_use: built with Claude (Anthropic); see AI use
---

# InfoSewer_2009: a 3D viewer of one sewer model and its swmm5-infosewer results

## In three points
- **What:** A 3D viewer of a 2009 InfoSewer sewer model (2,250 gravity pipes, 5 force mains, 5 pump stations) colored with swmm5-infosewer steady-state and 24-hour EPS results.
- **So what:** The engine matches the InfoSewer engine built from its source on this network: 58,487 of 58,487 steady-state values and 900,500 of 900,500 EPS values identical in every bit.
- **Now what:** Use it to see where the network surcharges (33 of 2,250 gravity pipes in steady state) and how stations cycle. It copies InfoSewer's rules, oddities included, and shows hourly snapshots only.

## What it does
Draws the active part of an InfoSewer sewer model (dated June 17, 2009) in 3D at its plan positions and invert elevations, and colours it with precomputed results from swmm5-infosewer: one steady-state run and 25 hourly report times (hours 0 to 24) of a 24-hour extended period (EPS) run. It is for engineers who want to see where a network is surcharged, how its pump stations behave, and what the InfoSewer method produces. Output is a picture, per-pipe and per-station readouts, charts, and CSV. It does not run an engine.

## The model
| Item | Count |
|---|---|
| Gravity pipes | 2,250 (125.5 mi) |
| Force mains | 5 (5.85 mi) |
| Total pipe length | 693,463 ft (131.3 mi) |
| Loading manholes | 2,231 |
| Junction chambers / wet wells / outfalls | 5 / 5 / 3 |
| Pumps / pump stations | 9 / 5 |
| Diameters | 7.0 to 60 in |
| Invert elevations | 4,947.66 to 5,440.0 ft (492 ft of fall) |
| Plan extent | 11.9 mi north-south, 10.3 mi east-west |

Pump stations (steady state; flow is the sum of the station's pump element flows):

| Wet well | Chamber | Pumps | Force main | Pump flow, gpm | Pump head, ft | FM loss, ft |
|---|---|---|---|---|---|---|
| 9002 | 2905 | REM_2 (point), REM_3 (point) | 1675: 8 in, 2,385 ft, C 100 | 68 | 46.65 | 0.48 |
| 9004 | 2931 | 5042 (point), RIV-2 (point) | 1693: 8 in, 3,951 ft, C 100 | 439 | 73.25 | 25.58 |
| 9022 | MH-6347 | 5054 (capacity) | P-7958: 10 in, 3,602 ft, C 140 | 1,200 | 25.31 | 27.11 |
| WW3 | 2513 | BDC-1 (point) | 959: 30 in, 20,249 ft, C 100 | 10,960 | 283.63 | 81.03 |
| WW303 | 2515 | GHC-1 (threepoint), GHC-2 (threepoint), GHC_3 (threepoint) | 501: 21 in, 680 ft, C 110 | 4,326 | 24.16 | 2.32 |

## How it computes
The page computes only the scene and the readouts. All hydraulics come from the engine run.

Scene (three.js r128, y up):
- World position of a point at plan (x, y) ft and elevation z ft: `X = x`, `Z = -y` (x and y are stored relative to the network's centre; the original map offsets are not in the page), `Y = (z - 4940) * VE`. `VE` is the vertical exaggeration slider, 1 to 50, default 15. The floor grid is at elevation 4,940 ft with 5,000 ft squares.
- Each link is a polyline through its IEDB vertices. Invert along it is linear from upstream invert to downstream invert. The centre line is invert + D/2.
- Drawn pipe radius: `max(D/2 * RS, 0.25 * RS)` ft, times 1.25 for force mains. `RS` is the pipe size slider, 1 to 100, default 30.
- HGL at a node = node invert + packed depth. Where the engine's head sweep left a node at 0, the display uses the node invert.
- HGL line and curtain are drawn on a segment only where the HGL is more than 0.02 ft above the crown (invert + D) at either end and the link has flow or is a force main. Amber over gravity pipes, violet over force mains.
- Station: wet well cylinder from bottom to bottom + max level; water to the current level (initial level in steady state); green tower from wet well water level to the HGL at the discharge chamber, shown when any pump of the station has flow.
- Station inflow on the Pump stations tab = sum of the flows of links whose downstream node is the wet well.
- Colour scales: depth/diameter linear 0 to 1; flow log10 from 1 to 10,000 gpm; velocity linear 0 to 8 ft/s; diameter log from 7 to 60 in. In depth/diameter mode a surcharged pipe and a force main get their own colours. A pipe with zero flow is grey.

Engine rules behind the numbers (swmm5-infosewer, written up with InfoSewer source file:line references in the repo's `docs/spec_steady.md`, `docs/spec_eps.md`, `docs/spec_pressure.md`):
- Pump curve `H = H0 - a Q^b`; force main loss by Hazen-Williams `hL = 4.727 L Q^1.852 / (C^1.852 D^4.871)` (Q in cfs, L and D in ft); station flow where pump head = static lift + loss.
- Steady state reports force main flow = station inflow and head loss at the pump flow (InfoSewer "Pump Flow Continuity" 0).
- EPS steps each wet well on a 1-minute pump step with level switching (on at max level, off at min level) and reports hourly. A station's force main carries the station flow sampled at the report hour.

## Inputs and outputs
- Input, at build time only: InfoSewer IEDB (dBase tables: NODE.DBF and VERTEX.DBF for coordinates; element tables via `iedb2ise.py`), converted by `ise2inp.py` to a SWMM5 `.inp` with `FLOW_ROUTING INFOSEWER`, run by swmm5-infosewer with `INFOSEWER_RESULTS_FILE` (full-precision CSV).
- Embedded data: 1.37 MB of JSON. Flows to 4 significant figures (gpm), depth/diameter to 0.001, velocity to 0.01 ft/s, node depth and pump head to 0.01 ft, wet well level to 0.001 ft.
- The page reads no files. Outputs: CSV of all 2,255 links for the current result (copy or save), CSV of the station time series (5 stations x 25 hours), and a WebM walkthrough recording.

## Checks
Mechanical:
- Engine against the InfoSewer engine built from its source, this network: 58,487 of 58,487 steady-state values and 900,500 of 900,500 EPS values identical in every bit (swmm5-infosewer `tests/pressure`, `tests/eps_pressure`). Whole test set: 11,894,156 values, all identical except LPS and MLD models within 4.2e-11.
- Packed data against the engine CSVs (`check_data.py`): 293,272 values; flows within 0.05%; depth ratios within 0.0005; velocities and heads within 0.005; wet well levels within 0.0005. That is the rounding.
- Pump operating point, station WW303, solved again from pump and pipe data by a separate bisection: 4,327 gpm at 24.16 ft; engine 4,326 gpm at 24.16 ft.
- Station WW3 arithmetic: 5,039.86 + 283.63 - 81.03 = 5,242.46 ft; force main outlet crown 5,242.46 ft.
- Theme: the HUD text and the pipe CSV are identical in dark and light themes. Contrast script: 34 checks, 0 below target, lowest 4.10:1.

Results the checks cover:
- Steady state: 33 of 2,250 gravity pipes surcharged; 11,987 gpm to the outfalls (1269: 3,615, 1444: 402, 4723: 7,970).
- EPS: surcharged pipes between 12 and 44 across the 25 report times; outfall 4723 peak 10,850 gpm at hour 18 (steady 7,970); outfall 1269 peak 4,423 (steady 3,615); outfall 1444 peak 601 (steady 402).
- Station WW3 in EPS: pump on in 6 of 25 hourly snapshots at about 11,070 gpm; inflow peak 4,716 gpm.
- InfoSewer mass balance, EPS: in 2,310,736 ft3, out 1,579,256, pipe storage 385,715, wet wells 10,492 to 16,962, unaccounted 339,295 (14.6 percent).

Human review: the 3D scene was rendered in headless Chrome (software WebGL) at desktop and phone widths and the screenshots were looked at.

## What this does not show
1. It is not a second opinion on InfoSewer. The engine copies InfoSewer's rules, oddities included.
2. Hourly snapshots only. Wet well levels and pump states between report times are not shown and are not linear.
3. Elevation and pipe size are exaggerated. Slopes and clearances cannot be judged by eye.
4. No terrain, streets or basemap. Ground is known only at manhole rims.
5. Known source-data defect: pipe P-8076 has inverts of 0.00 ft. The app draws it 10 ft below the rim and flags it; the engine used 0.00 as given.
6. The model is from 2009 and has not been compared with the present system or the utility's GIS.
7. The page cannot edit the model or rerun it.
8. Pump station rules are checked on this network and variants of it only. Two engine paths have no reference case: a bisection that converges after Newton fails, and a gravity pipe leaving a wet well.
9. Not yet tested: a real GPU, a real phone, Claude's artifact viewer, and the Save buttons inside that viewer.
10. No person has reviewed the page's code or read the essay against the engine source.

## How to reproduce
In the session workspace (`/home/claude/th3d`, not yet in a repo):
1. `ise2inp.py tha_steady.txt st.inp --mode steady --results st.csv --iedb <IEDB>` and the same with `--mode eps` for `ep.inp`, `ep.csv`.
2. `swmm5_is st.inp st.rpt st.out` and `swmm5_is ep.inp ep.rpt ep.out` (swmm5-infosewer commit 12492d6).
3. `build/build_data.py` packs `data.json`; `build/check_data.py` compares it with the CSVs and writes `check.json`.
4. `build/figures.py` draws the 8 essay figures from `data.json`; `build/gen_doc.py`, `build/make_docx.js`, `build/gen_md.py` write the Doc tab, the .docx and this file from `essay.json` and the same facts.
5. `build/build.py` assembles `InfoSewer_2009.html` from `template.html`.

## Credits and licenses
- InfoSewer and its engine: MWH Soft / Innovyze (now Autodesk), 1996 to 2011. Source supplied by Robert Dickinson; proprietary; not included here.
- An InfoSewer model (IEDB folder) dated June 17, 2009. A real utility's network. Keep the app private unless the utility agrees.
- EPA SWMM 5.2.4: U.S. Environmental Protection Agency, public domain.
- three.js r128: three.js authors, MIT license.
- swmm5-infosewer and this app: Robert Dickinson, SWMM Enablement.

## AI use
This app was built with Claude, Anthropic's AI model, in Claude Code sessions in November 2026, under the direction of Robert (Bob) Dickinson. He chose the project (InfoSewer's engine inside SWMM5), supplied the InfoSewer engine source and the 2009 InfoSewer model from his files, set the method (write up the engine's rules, then match its output value for value), and asked for this 3D model. Responsibility for the work is his.

Claude wrote swmm5-infosewer's InfoSewer routines and the converters, ran the model, packed the results, and wrote the page, its charts, the Doc essay, the .docx and this file.

The checks are mechanical, except the look at the screenshots. No person has yet reviewed the page's code, compared the 3D geometry with the utility's GIS, or checked the model's 2009 data against the system as it is today.

## Changes
- `1.2.0 (2026-11-12)`: renamed to InfoSewer_2009 (page, .md, .docx, saved file names); the utility's name no longer appears anywhere in them; the plan-coordinate offsets were removed from the embedded data, so node positions are relative to the network's centre only.
- `1.1.0 (2026-11-12)`: Doc tab and .docx open with one-sentence, one-paragraph and one-page summaries (one image); this .md added, embedded in the page and linked from About; version stamp.
- `1.0.0 (2026-11-10)`: first build: 3D network, steady and EPS results, pump stations tab, About, Doc, .docx, CSV, walkthrough recording.
