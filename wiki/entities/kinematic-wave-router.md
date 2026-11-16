---
title: Kinematic Wave Router (app)
type: entity
updated: 2026-11-15
sources: [S60, S125]
tags: [apps, replit, swmm5, ruby, routing, kinematic-wave]
reviewed: 11/16/2026
---
Bob's Replit app Kinematic Wave Router: a Ruby (Sinatra) web app that reads a SWMM5 INP network and routes a constant inflow from a chosen inlet by kinematic wave, with dendritic routing or an iterative loop solver. Version 2026.11.15, at `ruby-swmm-router.replit.app` [S125](../sources/S125-kinematic-wave-router-replit-summary.md).

**A caution about its source.** Everything on this page rests on [S125](../sources/S125-kinematic-wave-router-replit-summary.md), which Replit Agent wrote on 15 November 2026 from the project's source. Nothing here has been read by Bob (Q74).

**What the summary says** [S125](../sources/S125-kinematic-wave-router-replit-summary.md)
- The engine is the app's own Ruby code, `lib/kinematic_wave_router.rb`, which references EPA SWMM5 `kinwave.c`. No version is stated.
- Full flow is from Manning: `Qfull = (1.486 / n) * A * R^(2/3) * sqrt(|S|)`. Slope is estimated from the invert drop over length, with a minimum fallback where the drop is not positive.
- In dendritic networks conduits are sorted from upstream to downstream, and a flow split is divided equally among the outgoing conduits.
- Loops are found as strongly connected components. A looped network is routed repeatedly with under-relaxation, checking the maximum outflow change.
- Each conduit step solves `f(a) = beta1 * section_factor(a) + c1 * a + c2 = 0` by Newton-Raphson within bounds.
- `ruby tests/test_runner.rb`: zero passed and eight failed, each with `no block given (yield)`, so the intended assertions do not run.
- The loop test routed a fixture of four nodes and four conduits but logged that the solver did not fully converge after 20 iterations, with a maximum change of 0.0203 CFS.
- Results are peak and final outflow, time to peak and a CSV of conduit outflows in CFS. Units are US customary.
- A separate module imports from and exports to ICM InfoWorks through its Ruby API; it was not run.
- The README credits L. Rossman and M. Tryby for the SWMM5 C code and says the Ruby implementation keeps its public-domain status.

**What it does not show.** No upload of a user's own INP file was tried, and no network beyond the sample. The ICM integration needs the ICM host and was not run. Production behavior was not checked. [S125](../sources/S125-kinematic-wave-router-replit-summary.md)

**Noted at ingest.** The version, 2026.11.15, is the day of the summary, used because the app shows no release version; the README says `1.0 (2025)` (Q75). EPA SWMM 5 stops with an error on a loop under kinematic wave [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md); this app iterates instead.

See [Replit apps: the second seventeen summaries](../concepts/replit-app-summaries-second-batch.md), [Kinematic wave and steady flow routing](../concepts/kinematic-wave-and-steady-flow.md), [InfoWorks ICM](infoworks-icm.md), [EPA SWMM 5](swmm-5.md).
