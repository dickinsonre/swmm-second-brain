---
title: "S125: Kinematic Wave Router, summary written by Replit Agent (v2026.11.15)"
type: source
raw: raw/apps/ruby-swmm-router-v2026.11.15.md
kind: app-md
author: Robert Dickinson
published: 2026-11-15
ingested: 2026-11-15
tags: [apps, replit, swmm5, ruby, routing, kinematic-wave]
reviewed: 11/16/2026
---
**What it is.** A technical summary of Kinematic Wave Router, version 2026.11.15: a Ruby (Sinatra) web app that reads a SWMM5 INP network and routes a constant inflow from a chosen inlet by kinematic wave, with dendritic routing or an iterative loop solver. It is one of Bob's Replit apps, at `ruby-swmm-router.replit.app`. Raw file: [raw/apps/ruby-swmm-router-v2026.11.15.md](../../raw/apps/ruby-swmm-router-v2026.11.15.md).

**How it was written. This one is different.** The app ships no summary of its own making. Replit Agent wrote the file on 15 November 2026 from the project's source, and the file says Bob has not yet reviewed it (Q74). Of the app itself it says the project code and documentation do not identify AI tools used to build it. The copy here was read out of the editor of the Replit project named RubySwmmRouter on 15 November 2026 and matched a SHA-256 computed there (see the log).

**Claims worth keeping** (all copied from the file)
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

**Limits it states.** No upload of a user's own INP file was tried, and no network beyond the sample. The ICM integration needs the ICM host and was not run. Production behavior was not checked.

**Checked at ingest.** The version, 2026.11.15, is the day of the summary, used because the app shows no release version; the README says `1.0 (2025)` (Q75). EPA SWMM 5 stops with an error on a loop under kinematic wave [S60](S60-epa-swmm5-reference-manual-vol2-hydraulics.md); this app iterates instead.

**Feeds:** [Kinematic Wave Router (app)](../entities/kinematic-wave-router.md), [Replit apps: the second seventeen summaries](../concepts/replit-app-summaries-second-batch.md), [Kinematic wave and steady flow routing](../concepts/kinematic-wave-and-steady-flow.md), [InfoWorks ICM](../entities/infoworks-icm.md), [EPA SWMM 5](../entities/swmm-5.md).
