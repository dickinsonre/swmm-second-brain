---
title: ForceMain SWMM5 EPANET Comparison (app)
type: entity
updated: 2026-11-15
sources: [S115, S120]
tags: [apps, replit, swmm5, epanet, force-mains, pumps]
reviewed: no
---
Bob's Replit app ForceMain SWMM5 EPANET Comparison: a Streamlit app for designing and checking force mains: friction-loss calculators, a network analyzer, writers of SWMM5 and EPANET input files, and runs of both engines on paired generated models. Version 1.0, at `forcemainswmm5epanetcomparison.com` [S120](../sources/S120-forcemain-swmm5-epanet-comparison-replit-summary.md).

**A caution about its source.** Everything on this page rests on [S120](../sources/S120-forcemain-swmm5-epanet-comparison-replit-summary.md), which Replit Agent wrote on 15 November 2026 from the project's source. Nothing here has been read by Bob (Q74).

**What the summary says** [S120](../sources/S120-forcemain-swmm5-epanet-comparison-replit-summary.md)
- It runs SWMM5 through PySWMM 2.1.0 and EPANET through WNTR 1.5.0 (`EpanetSimulator`). The native engine versions, commits and licenses are not reported.
- The comparison takes median pumping flow, velocity, force main headloss and pump head. Percent difference is relative to the mean of the two values. The default review and exceedance thresholds are 5% and 10%.
- The calculator takes SI inputs. Hazen-Williams headloss is `hf = 10.67 * Q^1.852 * L / (C^1.852 * D^4.87)`. Darcy-Weisbach uses `64/Re` for laminar flow and Swamee-Jain for turbulent flow, with a linear transition between them.
- NPSH available is `H_atm + H_static - H_friction - H_vapor - H_velocity`.
- The network analyzer solves junction continuity residuals by Newton-Raphson and limits head updates.
- `python -m pytest -q`: 5 passed, 0 failed. One test is a real-engine comparison on one paired configuration.
- Streamlit `AppTest` executed all 10 sidebar views with 0 exceptions.
- Reference data: 10 pipe-material records and 50 pump curve points across 8 curve IDs.
- The footer shows version 1.0; `pyproject.toml` declares 0.1.0.
- An optional assistant sends questions to OpenAI GPT-5. No request was made during the checks.

**What it does not show.** No design-engineer review, production study or comparison with a field system. The screenshot check caught a loading placeholder, so the layout is unverified. The project states no license. [S120](../sources/S120-forcemain-swmm5-epanet-comparison-replit-summary.md)

**Noted at ingest.** The site address in the file is `forcemainswmm5epanetcomparison.com`, not a `.replit.app` name. The `date:` is the day of the summary (Q75). The calculator is SI; the US customary Hazen-Williams form is in [S115](../sources/S115-epanet-for-swmm5-experts-replit-summary.md).

See [Replit apps: the second seventeen summaries](../concepts/replit-app-summaries-second-batch.md), [Force main friction](../concepts/force-main-friction.md), [Pumps and pump curves](../concepts/pumps-and-pump-curves.md), [EPANET for SWMM5 Experts (app)](epanet-for-swmm5-experts.md).
