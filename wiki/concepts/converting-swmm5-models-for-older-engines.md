---
title: Converting SWMM 5 models for older engines
type: concept
updated: 2026-11-15
sources: [S73, S74, S81]
tags: [swmm-history, conversion, swmm1, swmm4, extran, swmm5]
reviewed: 2026-11-15
---
Three of Bob's apps take a modern SWMM 5 `.inp` and run it on an engine from 1971, 1981 or 2004. Each needs a converter, and each converter loses something. This page collects what the converters do and what they report as lost.

| App | Target engine | Converter |
|---|---|---|
| [SWMM 1 Engine (app)](../entities/swmm-1-engine-app.md) | SWMM 1 Runoff Block (1971) | `.inp` to 80-column Runoff cards [S73](../sources/S73-swmm1-engine-app-md-v3-13.md) |
| [EXTRAN III Workbench (app)](../entities/extran-iii-workbench.md) | EXTRAN III (1981) | `.inp` to an EXTRAN deck, `convert.js`; and the reverse, `deck2inp.js` [S74](../sources/S74-extran3-workbench-app-md.md) |
| [Bellinge (app)](../entities/bellinge-app.md) | SWMM 4.4H and EXTRAN III | The Workbench's S5to4 converter, with a ledger of every approximation and drop [S81](../sources/S81-bellinge-summary.md) |

**An older engine with no hydrology borrows SWMM 5's.** EXTRAN III routes flow and computes no runoff. The Workbench runs SWMM 5.2.4 first and turns each node's total lateral inflow into hydrograph cards. So a comparison "tests routing, not hydrology" [S74](../sources/S74-extran3-workbench-app-md.md). In the Bellinge app EXTRAN III is fed the runoff SWMM 4.4H computed [S81](../sources/S81-bellinge-summary.md).

**Size limits of the old programs.** EXTRAN III as printed holds 187 junctions and links and 65 inflow hydrographs. At those sizes the converter keeps hydrographs for the 65 largest-volume inflow junctions and gives the rest their mean flow. An enlarged build holds 5,000 [S74](../sources/S74-extran3-workbench-app-md.md). The whole Bellinge model is refused; one branch of 159 nodes fits [S81](../sources/S81-bellinge-summary.md).

**Things with no equivalent** [S74](../sources/S74-extran3-workbench-app-md.md)
- Control rules, minor losses, ponding and conduit flap gates have no EXTRAN III equivalent.
- Shapes map to EXTRAN's six classes; others become a rectangle or trapezoid of equal depth and full area.
- Models with ideal pumps, more than 8 links at a node, or over 99,999 steps cannot run.

**What the SWMM 1 importer taught, review by review** [S73](../sources/S73-swmm1-engine-app-md-v3-13.md)

| Subject | The difficulty | What the importer now does |
|---|---|---|
| Rain | WSHED reads the rain histogram once per step, at the step's middle (`WSHE 24`); a rain block shorter than the step is partly skipped | Makes every rain block a whole number of steps |
| Zeros | RHYDRO replaces a 0 with its own default (slope 0.03, depression storage 0.062 and 0.184 in, Horton 3.0 and 0.52 in/hr) | Punches the smallest value the field holds, and reports the value as approximated |
| Zero slope | Cannot be expressed on a card | Says so; a one-acre level lot ran off 3,368 of 3,630 cu ft |
| Time step | Runoff routes gutters and pipes at its one step | Uses WET_STEP; ROUTING_STEP is reported and not used |
| Names | The converter's lookups were case-sensitive, and an unknown gage fell back silently to gage 1 | Resolves names without regard to case, as SWMM 5 does; an undefined gage fails a status row |
| Infiltration | The Runoff Block has Horton infiltration | Green-Ampt carried as a stand-in: maximum 3 times conductivity, minimum the conductivity, "a rule of thumb" |

Inputs SWMM 1 cannot carry are "reported, not emulated": the Horton infiltration cap, subarea routing, LID, groundwater, snowmelt, dry-weather and external inflows, RDII, storage, flow regulators, controls and evaporation [S73](../sources/S73-swmm1-engine-app-md-v3-13.md).

**Checks a converter can and cannot make.** The SWMM 1 importer reads the punched deck back with the 1971 FORMATs and compares rain depth, run length, geometry and effective parameters with the `.inp`, and runs the deck on a second engine. Its summary names the weakness: the reader and the converter "were written by the same hand", and a review found two rules both had misread. No EPA SWMM 5 run was made to compare hydrographs [S73](../sources/S73-swmm1-engine-app-md-v3-13.md). The EXTRAN converter checks that its cards hold SWMM's inflow volume within 1 % (199 of 202 runs with inflow) [S74](../sources/S74-extran3-workbench-app-md.md).

**The reverse direction.** The Workbench also writes a 1981 deck as a SWMM 5 model. On 171 decks the median peak-depth difference between EXTRAN III and SWMM 5 is 0.16 ft as printed and 0.12 ft with bugs fixed [S74](../sources/S74-extran3-workbench-app-md.md).

**The standing caution.** "SWMM 5 is a different program, not the truth. A difference is not always a mistake" [S74](../sources/S74-extran3-workbench-app-md.md).

See [Verification against printed runs](verification-against-printed-runs.md), [SWMM version history, 1969 to 2026](swmm-version-history.md), [Block architecture and interface files](block-architecture.md).
