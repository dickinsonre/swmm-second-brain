---
title: "S380: Flood Pipeline Audit Bench, app .md (v1.0.0)"
type: source
raw: raw/apps/flood-audit-bench.md
kind: app-md
author: Robert Dickinson
published: 2026-11-18
ingested: 2026-11-19
tags: [apps, 2d, flood, audit, verification]
drafted_by: Claude (Anthropic), with the app
reviewed: no
---
**What it is.** A technical summary of the app Flood Pipeline Audit Bench, version 1.0.0: an audit of a 506-line open-source flood model by re-running its own solver. Raw file: [raw/apps/flood-audit-bench.md](../../raw/apps/flood-audit-bench.md).

**How it was written.** The app ships this file. Its AI-use section says the bench "was built with Claude, Anthropic's AI model, in sessions during August and November 2026, under the direction of Robert Dickinson", who chose the subject, supplied the repository link, relayed an external review and decided what shipped. Claude transcribed the solver into Python and JavaScript, designed and ran every experiment, and "found and corrected three errors in its own earlier work". The checks are mechanical; nobody has validated the reconstructed velocity diagnostics or verified the literature references, which were written without a bibliographic database. The file opens with In one sentence and In one paragraph, not In three points.

**Claims worth keeping** (all copied from the file)
- The subject is github.com/Muhammad7006/3D-flood-modeling at commit e7da94d, 506 lines, no license declared. Its storage-cell solver was transcribed into an instrumented Python harness and again into JavaScript, so the page runs the reviewed code rather than describing it. The flux is Manning's on a LISFLOOD-FP effective depth, which the file calls correct.
- The two published figures are the same field twice. Pressure as shipped is `P = rho*g*h/1000`, which is 9.81 times h; the two normalised fields differ by at most 2.22e-16 in the page and 1.110e-16 in Python, over 7,200 cells.
- Reference configuration: 120 x 60 cells of 32.8 ft (10 m), n = 0.045, 5,400 s, peak inflow 3,178 cfs (90 m3/s). Continuity in the page: 197 acre-feet in, closure error -2.3e-12 percent.
- 92.2 % of wet cells passed Froude 1, peak Fr 19, peak reconstructed velocity 51.0 ft/s (15.53 m/s).
- The volume limiter is active on 18.04 % of wet-cell timesteps at dt_max 5 s (median demand 2.23 times the water in the cell, p90 5.6 times, max 10 times) and falls to 0.89 % at 0.3 s. Peak depth is flat at 19.0 ft from dt_max 5 s to 0.75 s, then 12.0 ft at 0.3 s, a change of -36.609 %. In the Python harness the step taken is a median 4.6 times and a maximum 5.8 times the Hunter et al. diffusive limit the docstring names.
- Nodata: on the sample clipped raster, 92.223 % of stored volume ends in voids under the subject's rule; outfall volume is 4 against 122 acre-feet, and the reported peak depth 97.5 ft against 15.1 ft, a factor of 6.448. The paragraph summary says the continuity error stays at zero while this happens.
- Hazard: the envelope max(h) x max(v) overstates the time-coincident hazard by 1x to 2.217x by terrain, and 6.167x in the worst single cell.
- The bench reports fifteen severity-ranked findings and four disproved hypotheses. Parser 23 of 23 cases and end to end 12 of 12 pass. Complexity index 54.4 (HydroCouple = 100).

**Limits it states.** The velocity, Froude and hazard fields are reconstructed audit diagnostics, not the output of a verified hydraulic solver; cell velocity is a per-face maximum, not a vector magnitude. "Percent supercritical" is a peak-over-time share of ever-wet cells. Nothing is validated against gauged data, an analytical solution or a benchmark suite. The literature references may be wrong and are labeled unverified. The grade is one reviewer's judgement against a rubric that reviewer wrote.

**Checked at ingest.** Two different measurements both read 92.2 %: the share of wet cells passing Froude 1 and the share of stored volume ending in nodata voids (92.223 %) (Q122). The Python harness's peak depth falls from 5.965 m to 5.451 m, -8.6 % (our arithmetic agrees). The subject repository is public, and the file quotes its code only in short excerpts. The `links:` line names no Netlify address and no artifact address. The file name carries no version.

**Feeds:** [Flood Pipeline Audit Bench (app)](../entities/flood-audit-bench.md), [Continuity is not validation](../concepts/continuity-is-not-validation.md).
