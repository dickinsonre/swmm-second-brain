---
name: People as Pollutants
file: people-as-pollutants.html
version: 1.0.0
date: 2026-10-29
written: 2026-11-14
author: Robert Dickinson
links: {artifact: "https://claude.ai/artifact/NYos9pM4nie5zTLTaot9kN", netlify: "https://people-are-pollutants-swmm5.netlify.app (not read for this summary; it may serve another build)", repo: none recorded in the page}
engines:
  - {name: EPA SWMM, version: 5.2.4, source: "USEPA/Stormwater-Management-Model, tag v5.2.4, unmodified", license: public domain, use: "runs in the page; clang 18 to a wasm32-wasi reactor; sha256 0225fd30c79f9d38976e246e39eb3a3409a8e3d354651a7838a2c0d4360f06e5"}
units: US customary inside the model (CFS, ft, ft²). One cubic foot of water is one person. The page quotes Weidmann's parameters and two level depths in SI; US values are given first and those conversions are this summary's unless the page gives them.
ai_use: the app was built with Claude (Anthropic). This summary was written by Claude from the page's source. See AI use.
written_from: "the published artifact's page source, its About and Verify tabs, its Doc essay and its two embedded records (window.PAP_BUILD, built 2026-10-29 21:36 UTC, and window.PAP_DOC), read on 2026-11-14. No engine was run and no test was rerun to write this file."
---

# People as Pollutants: a transit station written as a SWMM 5.2.4 model, with the water read as a crowd

This summary was written after the fact. The page carries no technical summary of its own. Every number below is copied from the page's embedded records, its Verify and About tabs or its Doc essay. Nothing here was measured again. The page records no file name; `people-as-pollutants.html` is taken from its title.

## What it does

It writes a three-level interchange station (street, concourse, platform) as an EPA SWMM 5.2.4 input file and runs it with the unmodified EPA engine compiled to WebAssembly. The question it answers is Bob Dickinson's: could SWMM5 show that station if the water quality were people? The user changes the timetable, the arrivals, the traveler mix and the devices, runs again, and sees the result in a 3D station view.

It was prompted by Gavin Nicholls' LinkedIn post about Throng, his pedestrian simulator. The page says it is not affiliated with Throng and uses none of its code or data.

## How it computes

The mapping from a station to SWMM objects:

| Station | SWMM object |
|---|---|
| One person | One cubic foot of water. The flow unit is CFS, so 1 cfs is one person per second |
| A floor zone | A storage unit. Its area is the real floor area divided by 100, so a zone 1 ft deep holds one person per 100 ft² |
| A walkway, stair, escalator, fare gate, lift or train door | A TYPE4 pump, whose flow is a function of the depth at its inlet node |
| Arrivals from the street | Rain on three subcatchments, 100 percent impervious with no depression storage |
| Passengers off trains | External inflows |
| Trains | Outfalls. The doors are pumps set to 1 or 0 by a control rule that reads a time series |
| Kinds of traveler | Pollutants read as percent of the crowd: COMMUTER, LUGGAGE, MOBILITY, ELDERLY, FAMILY |
| Where people came from | Tracer pollutants SRC_CITY, SRC_SB, SRC_NB |
| Waiting | A pollutant PATIENCE that starts at 100 and decays at a first-order rate of 1 per 600 seconds |

- The station has twelve floor zones and twenty-two pumps. Where both directions share a floor, the zone has an IN node and an OUT node over the same floor area.
- Each pump curve is the rising half of a pedestrian fundamental diagram, then holds the peak. Stored constants: free walking speed 4.396 ft/s (the page cites Weidmann's 1.34 m/s), critical density 0.1625 people per ft², jam density 0.5017 people per ft² (Weidmann's 5.4 p/m²), peak specific flow 0.3734 people per ft of width per second.
- Control rules throttle each feeder pump as the zone it feeds passes 85 percent of its receiving density. A lane rule gives each direction on a shared stair a share of the width in proportion to its share of the people on it.
- The lift is two pumps on a 120-second cycle.
- The runner asks the engine after every 1-second step for the runoff from each shed, the volumes on the two platforms and the flows through four pumps, and integrates them. The report step is 10 seconds.

## Results as stored (baseline)

The baseline is a two-hour morning peak from 07:00 with a 20-minute drain. Street arrivals peak at 320 a minute. Trains run every 4 minutes each way, southbound with 560 spaces to spare and northbound with 520. The record holds 70 trains, 35 each way.

| Quantity | Stored value |
|---|---|
| Walked in from the street | 23,241.8 people |
| Got off trains | 4,200 southbound and 7,000 northbound |
| Boarded | 11,413.6 southbound and 11,793.1 northbound |
| Left by the street | 5,248.5 north and 5,723.3 south |
| Lost to flooding | 0 |
| Still inside at the end | 260.4 |
| Most in the station at once | 2,939 |
| Southbound platform, peak density | 0.0436 people per ft², level of service A |
| Northbound platform, peak density | 0.0722 people per ft², level A |
| North entrance stair, peak density | 0.162 people per ft², level E |
| North plaza, peak density | 0.1289 people per ft², level E, at 08:25:50 |
| Most left behind by one train | 38 southbound, 356 northbound |
| Lowest average PATIENCE on a platform | 46.8 southbound, 37.72 northbound |

The essay's reading: the pinch is the 16-foot north entrance stair, which sits at the critical density; downstream of it the station is starved, not crowded.

Four stored variants, each changing one thing:

| Variant | Stored result |
|---|---|
| One of the two northbound down escalators closed | 1,568 left behind by one southbound train, against 38 in the baseline |
| Lift out of service | Most left behind northbound goes from 356 to 322 |
| Lane formation off | North plaza peak 0.0108 people per ft². The essay calls this a wrong station, not a better one |
| Peak arrivals up 25 percent | North plaza at level F, 0.3625 people per ft²; a northbound train leaves 743 behind |

## Checks

Mechanical, on the stored baseline:

- People census: in minus out minus still inside is 2.86 people, 0.008 percent.
- SWMM's flow routing continuity error: 0.004 percent. No pollutant's quality continuity error is worse than 0.256 percent.
- Shares add to 100: where a node holds at least 5 people, the five traveler types sum to 100 within 0.767 percent across 13,289 node-periods (worst at STSB_UP at 07:43:20). Below 5 people, 102 of 1,240 node-periods miss by more than 1 percent, the worst by 11.1 percent.
- The Verify tab also offers a null-effect run (no arrivals and no alighting passengers), a determinism run (the same `.inp` run twice must write byte-identical `.out` files) and a live rerun of the two traps below. Their results are computed in the browser and are not stored in the page.

Human review: none recorded.

## Defect register, as stored

| ID | Where | What | Status in the page |
|---|---|---|---|
| D-1 | `qualrout.c` line 41, `static const double ZeroDepth = 0.003281; // 1 mm in ft`, and the dry-node branch of `findStorageQual` | A node shallower than 1 mm with no inflow has its concentrations set to zero. With depth read as density 1:1 that is 0.0033 people per ft², 122 people on the 37,200 ft² paid concourse. Stored run at 1:1: southbound origin tracer quality continuity -30.395 percent, census error 0.353 percent | Mitigated by depth = 100 × density. Residue: the small-node misses in the checks above |
| D-2 | `dynwave.c`, `setNodeDepth()`, `surfArea = MAX(surfArea, MinSurfArea);` | A storage unit smaller than MIN_SURFAREA (default 12.566 ft²) changes depth as if it had 12.566 ft² while its volume comes from its own curve. Stair and escalator zones here are 2.4 to 6.4 ft². Stored run with the default: census error 0.573 percent (197.45 people), worst node ESCNB_UP at 1.16 percent | Fixed with MIN_SURFAREA 0.01 in `[OPTIONS]` |
| D-3 | The in-memory file system (browser_wasi_shim 0.4.2), not SWMM: `OpenFile.fd_write` reallocated and copied the whole file on every extending write | Nothing to the results. A 6 MB report took 5.7 s to write | Fixed with a growable file; results byte-identical; run about 0.5 s |

The page calls D-1 and D-2 "two SWMM defaults" that leak into a crowd model. It does not call them errors in SWMM for water.

## What this does not show

From the page's own list:

1. Water has no destination. At a fork every pollutant splits in the flow ratio, so a wheelchair user cannot choose the lift; MOBILITY is 2 percent of whatever goes down the stair. Route choice is fixed by pump curve shares.
2. Storage units are mixed tanks, not queues. Waiting time and PATIENCE are room averages.
3. No field data. Speeds and capacities come from Weidmann (1993) and Fruin (1971) and round numbers for gates, escalators and the lift. The model has not been compared with a real station or with Throng.
4. The geometry is drawn, not surveyed. Level depths match the Throng screenshot, 19.69 ft and 39.17 ft (6.00 and 11.94 m); the floor plan is invented.
5. One machine, one engine build. The page has not been diffed against the EPA Windows binary.

Not checked by any person, by the page's own account: the station geometry, the device capacities, the Weidmann parameters as entered, and the essay against a real station or against Throng.

Added by this summary:

6. This file was written from the page, not from the build. No stored result was rerun.
7. The null-effect, determinism and live trap checks leave no stored result in the page, so this summary cannot report their outcomes.
8. The page records no file name. The build record carries no engine size.
9. D-1 to D-3 are the page's own IDs. This summary does not map them to any other register.

## How to reproduce

Open the artifact. Run the baseline, then open the Verify tab: the census, continuity and share checks recompute for whatever scenario is set, and the null, determinism and trap runs each have a button. The page shows the input file the engine ran and the report it wrote. To check this summary, view the page source and read `window.PAP_BUILD` and `window.PAP_DOC`.

## Credits and licenses

- EPA SWMM 5.2.4: USEPA, tag v5.2.4, public domain.
- WASI shim: bjorn3/browser_wasi_shim 0.4.2 (MIT/Apache-2.0), with a growable in-memory file added. Bundle sha256 `76f64ddcb60f7bb368587b1a9d23c5dde3e6467d7e9c7f503c4a167fe102ec63`.
- U. Weidmann (1993), Transporttechnik der Fussgänger, IVT Schriftenreihe 90, ETH Zürich.
- J. J. Fruin (1971), Pedestrian Planning and Design.
- L. F. Henderson (1971), "The statistics of crowd fluids", Nature 229, 381-383.
- Gavin Nicholls, LinkedIn post on Throng, October 2026. The page says its station layout and level depths are only inspired by that post's screenshot.

## AI use

From the page's About tab: the app was built with Claude, Anthropic's AI model, in one session on 29 October 2026, at the request of Robert (Bob) Dickinson, who chose the question and set the direction. Responsibility for the work is his. Claude designed the mapping from a station to SWMM objects, wrote the `.inp` generator, compiled EPA SWMM 5.2.4 from the USEPA v5.2.4 source tag to WebAssembly, wrote the engine runner, the `.out` reader, the analysis, the 3D station view, the charts, the GIF encoder, the checks, the Doc essay and the .docx, and the page's text. It found and measured the two SWMM defaults in the defect register while building. The checks are mechanical. Not checked by any person yet: the station geometry, the device capacities, the Weidmann parameters as entered, and the essay against a real station or against Throng.

This summary: written by Claude (model claude-fable-5-2) on 14 November 2026 at Bob's request, from the page source only. Bob has not yet read it.

## Changes

- `1.0.0 (2026-10-29)`: the build this summary describes. The page records no change history.
