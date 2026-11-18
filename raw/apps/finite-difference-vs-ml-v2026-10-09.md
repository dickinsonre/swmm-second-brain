---
name: Finite difference vs ML for flood modeling
file: finite-difference-vs-ml.html
version: "2026-10-09"
date: 2026-10-09
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/MF4SmBcz852QKsLFwiQDUa", repo: none named in the page}
engines:
  - {name: none in the page, note: "the results are 15 fixed data files from a synthetic experiment run by Claude on 2026-10-09: a 1D Saint-Venant finite difference solver in Python and two scikit-learn surrogates"}
units: US customary (ft, cfs, acre-ft, mi)
ai_use: "This summary was written by Claude (Anthropic) from the published dashboard. Each of its data files says 'Synthetic experiment run by Claude on 2026-10-09'; the page itself carries no AI-use note. See AI use."
written_from: "the published Claude dashboard https://claude.ai/artifact/MF4SmBcz852QKsLFwiQDUa, version 1791519555-865a: its page file (files/index.html, 52,851 bytes, SHA-256 fe3ece0053f490d3aa21c31c9ea7dc0fc4bc23e4b2317584fdd37c52e7680b7c) and its 15 data files (27,269 bytes of CSV), rendered in headless Chromium on 2026-11-18 through the Netlify conversion and read in full. Nothing was rerun to write this file."
---

# Finite difference vs ML for flood modeling: ten reasons a surrogate cannot replace the solver, each with a test

## In three points
- **What:** A dashboard of one synthetic experiment: a 1D Saint-Venant finite difference solver on an 8-mile reach, and two machine-learning surrogates trained on 200 of its runs (a neural network and a random forest), scored against ten reasons the solver should be kept, each reason with its own test.
- **So what:** Inside the record (peaks 200 to 1,200 cfs) the network matches the solver's peak depth to 0.007 ft RMSE and answers 4,200 times faster. At a 3,000 cfs design flood, 2.5 times the largest on record, ten trainings of the same network give 5.90 to 9.75 ft against the solver's 8.40 ft, and the training charted loses 18% (251 acre-ft) of the 1,397 acre-ft that flowed in; the forest gives 5.50 ft and loses 56%.
- **Now what:** Read "Method and limits" before quoting a number. The reference is the solver itself, on one synthetic reach with no field data, and rows 3, 4, 5 and 8 of the scorecard are true by construction.

This summary was written after the fact. The dashboard ships no technical summary of its own and gives no version number; the version above is the date its data files carry. The file name is ours. Every number below is copied from the dashboard's text and data files. Nothing was run to write this file.

## What it does

The page opens with six tiles (past the record: the solver's case; inside the record: the surrogate's case), two wide charts (peak depth at mile 4 as the flood grows; the design flood at the outlet), a ten-row scorecard, one card per test, and a method section. Every figure is drawn in the browser from 15 data files.

## The experiment (as the page states it)

- Reach 8 miles; grid 528 ft (80 cells); time step 10 s; 36 hours per flood; bed slope 0.0008 (4.22 ft per mile); main channel 60 ft wide with 6 ft banks; floodplain widening to 400 ft over a 2 ft rise; Manning's n 0.035 in the channel, 0.08 on the floodplain; baseflow 50 cfs; bankfull 1,264 cfs.
- Solver: the full Saint-Venant dynamic wave on a staggered grid with semi-implicit friction, the same form as the SWMM5 dynamic wave link equation.
- Record: 200 floods, peaks 200 to 1,200 cfs, time to peak 2 to 6 hours; 40 more held back for testing. Every record flood stayed inside the banks.
- Surrogates: a network of two hidden layers of 64 (ReLU, 9,552 weights) and a 300-tree random forest, each mapping peak inflow and time to peak to peak depth at seven gauges and the outlet hydrograph; ten trainings each.

## Results the page reports

| No. | Reason | Finite difference | Surrogate | Result |
|---|---|---|---|---|
| 1 | Mass balance is checkable | 4 x 10^-12 % at worst over 265 runs | Lost 18% (network) and 56% (forest) of the design flood; in-record 0.2% and 1.6% | Measured |
| 2 | It extrapolates | 8.40 ft peak depth | Network 5.90 to 9.75 ft across 10 trainings; forest 5.50 ft | Measured |
| 3 | What-ifs are a geometry edit | -0.89 ft and +0.58 ft at mile 4 | 0.00 ft; no geometry input | By construction |
| 4 | Every number is traceable | Five momentum terms sum to zero within 1 x 10^-14 ft per mile | 9,552 weights, none tied to a term | By construction |
| 5 | Structures and controls are explicit | 9 ft tailwater: backwater 1.85 miles upstream, outlet flow reverses to -365 cfs | No change; no tailwater input | By construction |
| 6 | It needs less data | 0 floods and 8 channel numbers | 40 floods (network), 160 (forest) to reach 0.1 ft in-record | Mixed |
| 7 | Its errors behave predictably | Peak outflow error falls 17.7, 4.9, 1.5, 0.5, 0.1 cfs as dx halves | 3.85 ft spread from the random seed alone | Measured |
| 8 | You get the full state everywhere | 3,110,400 values per flood | 80 values per flood | By construction |
| 9 | Parameters mean something | n 0.035 to 0.045 raises steady depth 0.90 ft, matching Manning within 2 x 10^-13 ft | No roughness input | Measured |
| 10 | The ML model is usually trained on its output | Teacher with n off by 0.005: error 0.33 ft | 0.33 ft against the reference, 0.008 ft against its own teacher | Measured |

- Timing, one core: solver median 1,700 ms (1,639 to 1,751, 7 repeats); network 0.40 ms (0.36 to 0.55, 2,000 repeats); forest 17.9 ms (17.3 to 19.9, 200 repeats). Building the record took the solver 5 minutes.
- Design flood at the outlet (first training): solver 2,321 cfs, network 3,448 cfs (more than went in), forest 1,067 cfs.
- A defect the grid test caught: the first solver averaged the two face flows before squaring (Qc = 0.5 * (Q[:-1] + Q[1:]); F = Qc * Qc / A). It ran clean on five grids and broke on the 66 ft grid: peak out 2,348 cfs, depth kink 5.22 ft, 2,324 rising steps on the recession. The upwind fix (Qup = np.where(Qc >= 0.0, Q[:-1], Q[1:]); F = Qup * Qup / A) gives 2,322 cfs, 0.00015 ft and 0.
- Grid refinement: on the 528 ft grid the design flood's peak outflow is 1.5 cfs off the 66 ft reference of 2,322 cfs.

## Checks

- Arithmetic we checked (ours): 3,000 / 1,200 = 2.5; 1,699.8 ms / 0.404 ms = 4,206, given as 4,200; 251 / 1,397 = 18%; 9.75 - 5.90 = 3.85 ft.
- The page's own checks: solver continuity (volume in minus volume out minus change in storage) on 265 runs; steady depth against Manning normal depth from a separate root-finder; grid refinement over six grids from 2,112 ft to 66 ft.

## What this does not show

As the page lists it: the reference is the solver itself, so the tests measure how far a surrogate strays from its teacher, not whether the solver is right about a real river; one synthetic reach with no rainfall, no real gauges and no calibration, with roughness from handbook ranges; two small off-the-shelf surrogates with two inputs; rows 3, 4, 5 and 8 true by construction; a hydraulics test, not rainfall-runoff forecasting, where data-driven models have a strong record.

## How to reproduce

The page holds the setup table and every result as data; the solver and training scripts are not in the page.

## Credits and licenses

Python, NumPy and scikit-learn (named in the data files); d3 for the charts. No license is stated for the page.

## AI use

The page carries no AI-use note. Each data file says "Synthetic experiment run by Claude on 2026-10-09: a 1D Saint-Venant finite difference solver in Python and scikit-learn surrogates." It is a Claude dashboard on Robert Dickinson's account, built in a claude.ai session. The Netlify copy is a conversion made by Claude on 18 November 2026: the page's own markup, styles and drawing code unchanged, a small shim in place of the dashboard's data loader, the 15 data files embedded unchanged and listed at the foot, d3 7.9.0 from cdnjs, and a paragraph saying all this. This summary was written by Claude on 18 November 2026.

## Changes

- 2026-10-09: the version read (the date its data files carry).
