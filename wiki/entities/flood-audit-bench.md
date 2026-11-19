---
title: "Flood Pipeline Audit Bench (app)"
type: entity
updated: 2026-11-19
sources: [S380]
tags: [apps, 2d, flood, audit]
reviewed: no
---
Bob's app Flood Pipeline Audit Bench audits one small open-source flood model, github.com/Muhammad7006/3D-flood-modeling at commit e7da94d (506 lines), by re-running its own storage-cell solver, transcribed into Python and into JavaScript. Version 1.0.0, 2026-11-18 [S380](../sources/S380-flood-audit-bench-app-md.md). Six sample terrains ship with it, and a user can load an ESRI ASCII grid, a numeric grid or x y z triples [S380](../sources/S380-flood-audit-bench-app-md.md). Its `links:` line names no Netlify or artifact address [S380](../sources/S380-flood-audit-bench-app-md.md).

**What the audit found** [S380](../sources/S380-flood-audit-bench-app-md.md)
- The two published panels are one field twice: pressure as shipped is 9.81 times depth, and the normalised fields differ by at most 2.22e-16.
- 92.2 % of wet cells passed Froude 1 (peak Fr 19) in a scheme whose physics assumes inertia is negligible.
- The volume limiter is active on 18.04 % of wet-cell timesteps at the default step, and is what makes the timestep change the answer: peak depth 19.0 ft at dt_max 5 s, 12.0 ft at 0.3 s.
- On a clipped raster, 92.223 % of stored volume ends in nodata voids and the reported peak depth is 97.5 ft against 15.1 ft, while continuity stays at zero.

**What it does not show** [S380](../sources/S380-flood-audit-bench-app-md.md). Its velocity, Froude and hazard fields are audit diagnostics reconstructed from the model's fluxes, not a verified solver's output. Nothing is checked against gauged data or a benchmark; the literature references are unverified.

See [Continuity is not validation](../concepts/continuity-is-not-validation.md).
