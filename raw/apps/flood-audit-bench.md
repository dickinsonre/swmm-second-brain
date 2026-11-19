---
name: Flood Pipeline Audit Bench
file: flood-audit-bench.html
version: 1.0.0
date: 2026-11-18
author: Robert Dickinson
links: {netlify: none recorded, artifact: see delivery note, repo: none}
subject:
  - {repository: "github.com/Muhammad7006/3D-flood-modeling", commit: e7da94dffcf58139a188a52d98721d08461c1567, branch: main, retrieved: 2026-08-06, lines: 506, license: none declared}
engines: none. The page runs a transcription of the subject's own solver, not a hydraulic engine.
harnesses:
  - {name: verify.py, language: Python 3.12.3, numpy: 2.4.4, role: canonical measurements}
  - {name: in-page port, language: JavaScript, node: v22.23.5, role: live runs in the browser}
units: US customary (ft, ft/s, cfs, acre-feet) with SI in parentheses; Defra hazard rating left in metric by definition
ai_use: built with Claude (Anthropic); see AI use
---

# Flood Pipeline Audit Bench: auditing a 506-line flood model by re-running its own solver

## In one sentence

A 506-line Python flood model was transcribed and re-run inside this page, and its two published figures turned out to be the same field twice, differing by 1.11e-16 once each is normalised.

## In one paragraph

The bench is a single HTML page that audits one small open-source flood model. The repository's solver was transcribed twice, once into an instrumented Python harness and once into JavaScript, so the page runs the reviewed code rather than describing it. Six sample terrains ship with it, and you can load your own raster. The audit found that the two published panels are one field twice, that 92.2% of wet cells pass Froude 1 where the physics assumes inertia is negligible, and that a clipped raster sends 92.2% of the flood into its own nodata holes while the continuity error stays at zero. The limit is plain: the velocity and Froude fields here are audit diagnostics reconstructed from the model's own fluxes, not the output of a verified hydraulic solver.

## What it does

Audits one open-source flood model (github.com/Muhammad7006/3D-flood-modeling at e7da94d). The repository's storage-cell solver was transcribed into an instrumented Python harness and again into JavaScript, so the page runs the reviewed code rather than describing it. Six sample terrains ship with it; a user can load an ESRI ASCII grid, a headerless numeric grid or x y z triples, plus a hydrograph CSV. Outputs: a graded rubric, fifteen severity-ranked findings tagged measured, read or latent, four disproved hypotheses, live runs with scheme switches, A/B comparison, parameter sweeps, cell-level CSV export and a provenance package.

## How it computes

The transcribed scheme, unchanged from the subject:

- Flux across a face, from Manning: `q = (1/n) * d_flow^(5/3) * sqrt(|d(z+h)/dx|)`
- Effective flow depth: `d_flow = max(wse_a, wse_b) - max(z_a, z_b)` (LISFLOOD-FP form, correct)
- Volume limiter: `scale = min(1, available / requested)`, applied per face as the minimum of the two neighbouring cells' factors
- Adaptive step: `dt = alpha * dx / sqrt(g * h_max)`, capped by `--dt-max` (default 5 s)
- Outlet boundary as shipped: `h[outlet] *= 0.5` every step
- Pressure, as shipped: `P = rho * g * h / 1000`, which is `9.81 * h`

Reconstructed diagnostics, added by the audit and not present in the subject:

- Face velocity `v = |q| / d_flow`, evaluated where `d_flow > 0.01 m`, taken after the limiter
- Cell velocity: the maximum over the up to four faces touching the cell. A scalar upper bound on one directional component, not a vector magnitude
- Froude: `Fr = v / sqrt(g*h)` formed in-step from coincident values, gated at `h > 0.05 m`
- Hazard: `max over time of h*v` and `max over time of h*(v + 0.5)`, both accumulated in-loop from coincident values. The envelope `max(h) * max(v)` is reported only to show how much it overstates

## Inputs and outputs

Reads ESRI ASCII grid (.asc, .txt, .agr, .grd), headerless numeric grids, x y z triples, and `time_s,discharge_m3s` hydrograph CSV. GeoTIFF is not parsed; convert with `gdal_translate -of AAIGrid`. Nodata is held as a mask separate from the elevations so the rule can be switched between the subject's (global minimum) and the correct one (wall). Writes an ESRI ASCII grid as the solver saw it, a hydrograph CSV, a cell-level results CSV, a findings CSV and a run-summary CSV.

## Checks

Reference configuration: 120 x 60 cells, 32.8 ft (10 m) cells, n = 0.045, 5,400 s, peak inflow 3178 cfs (90 m3/s).

- Continuity, in-page port: 197 acre-feet in, closure error -2.3e-12 percent. Python harness: -0.000 percent with the negative-depth clip creating 6.527e-09 m3.
- Twin-panel identity: largest difference between the two normalised fields 2.22e-16 (in-page) and 1.110e-16 (Python), over 7,200 cells. Ratio P/h constant at exactly 9.81.
- Froude: 92.2% of wet cells passed Fr = 1, peak Fr 19, peak reconstructed velocity 51.0 ft/s (15.53 m/s).
- Froude restricted to cells holding more than 0.5 m: meandering valley 96.614%, mild floodplain 100%.
- Volume limiter activity: active on 18.04% of wet-cell timesteps at dt_max 5 s, median demand 2.23x the water in the cell, p90 5.6x, max 10x. Falls to 0.89% at dt_max 0.3 s.
- Timestep: peak depth flat at 19.0 ft from dt_max 5 s to 0.75 s, then 12.0 ft at 0.3 s, a change of -36.609%. Python harness at the same configuration: 5.965 m to 5.451 m from 5.0 s to 0.5 s, -8.6%.
- Cited stability limit: step taken is a median 4.6x and maximum 5.8x the Hunter et al. diffusive limit named in the docstring (Python harness).
- Nodata: on the sample clipped raster, 92.223% of stored volume ends in voids under the subject's rule, outfall volume 4 vs 122 acre-feet, reported peak depth 97.5 ft vs 15.1 ft, a factor of 6.448.
- Hazard envelope vs time-coincident: overstatement 1.281x, 2.217x, 1.79x, 1x, 1.245x, 1.01x by terrain; worst single cell 6.167x. Invariant asserted: envelope >= coincident in every cell of all six terrains.
- Parser: 23 of 23 cases pass (CRLF, BOM, tab headers, xllcenter, missing NODATA, reflowed values, scientific notation, commas, truncation, ragged rows, XYZ, over-coarsening, all-nodata, geographic cell size).
- End to end: 12 of 12 pass, including a 600 x 400 raster at 8.2 ft cells with 7,317 voids, auto-coarsened 7x, and an export then re-import round trip (max |dz| 5e-4 m, void mask identical).
- Accessibility: 53 contrast pairs pass in both themes.
- Complexity index: 54.4 (HydroCouple = 100, analyzer 1.7.0, baseline HC-2026-11-10-h).

Human review: none independent. Every check above is mechanical.

## What this does not show

- The velocity, Froude and hazard fields are reconstructed audit diagnostics, not the output of a verified hydraulic solver. Cell velocity is a per-face maximum, not a vector magnitude, and does not resolve direction.
- "Percent supercritical" is a peak-over-time share of ever-wet cells. A cell that crosses Fr = 1 for one step counts.
- Nothing here is validated against gauged data, an analytical solution or a benchmark suite. The lake-at-rest, Ritter dam-break and Environment Agency benchmark cases recommended in the Fix Plan have not been run.
- The literature references were written without a bibliographic database. Authors, years and volumes may be wrong, and the Method tab labels them unverified.
- The grade is one reviewer's judgement against a rubric that reviewer wrote.
- Known limits of the subject that this audit did not exercise: geographic coordinate systems, rainfall on grid, infiltration, spatially varying roughness, buildings, culverts and 1D-2D coupling. The subject has none of these.

## How to reproduce

```
git clone --depth 1 https://github.com/Muhammad7006/3D-flood-modeling.git repo   # pins to e7da94d
sha256sum repo/*
python3 verify.py      # timestep sensitivity, Hunter ratio, limiter, outlet BC,
                       # twin-panel identity, hazard, argmax location
python3 verify2.py     # single-cell inlet, in-loop velocity, nodata handling
node tools/test-loader.js   # 23 parser + 12 end-to-end cases, against the shipped file
node tools/measure.js       # every number in the Doc tab and this file
node tools/complexity.js
```

`verify.py` ships with the bench and is downloadable from the Method tab. It imports nothing from the subject, so a difference in results cannot be blamed on a difference in the code under test.

## Credits and licenses

Subject repository by its author (GitHub user Muhammad7006); no license is declared there, which is itself finding 15. Scheme after the LISFLOOD-FP storage-cell family (Bates and co-workers). Hazard rating after Defra and Environment Agency R&D FD2317 and FD2321. Complexity index from Robert Dickinson's SWMM App Complexity Meter, with the HydroCouple GitHub organization as the baseline. This bench is Robert Dickinson's work; the subject repository's code is quoted only in short excerpts for review.

## AI use

This bench was built with Claude, Anthropic's AI model, in sessions during August and November 2026, under the direction of Robert Dickinson. He chose the subject, supplied the repository link, set the direction at each round, relayed an external review for the bench to answer, and decided what shipped. Responsibility for the work is his.

What Claude did. It cloned and read the repository, transcribed the solver into an instrumented Python harness and then into JavaScript, designed and ran every experiment quoted here, wrote the page, the DEM parser, the figures, this essay, the Word document and the technical summary, and ran the verification suites. It also found and corrected three errors in its own earlier work, including computing a hazard field from non-coincident maxima.

How the results were checked. The checks are mechanical. Every number in this document is produced by a script that re-runs the shipped solver, and the figures are drawn from that script's output rather than from prose. The parser and loader carry 34 assertions. Contrast ratios were computed for 53 text and surface pairs across both themes.

What no person has checked. Nobody has validated the reconstructed velocity diagnostics against an independent solver. Nobody has verified the literature references, which were written without a bibliographic database and are labelled unverified in the Method tab. No person has re-derived the audit's arithmetic by hand.

## Changes

`1.0.0 (2026-11-18)`: Doc tab, About tab, .docx and this file added. Units switch (US customary default, SI available). New measured finding: the volume limiter is active on 18.04% of wet-cell timesteps and is what makes the timestep change the answer. Timestep evidence extended from two points to eight.
