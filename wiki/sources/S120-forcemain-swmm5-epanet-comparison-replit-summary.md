---
title: "S120: ForceMain SWMM5 EPANET Comparison, summary written by Replit Agent (v1.0)"
type: source
raw: raw/apps/force-main-robertdickinson-v1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-11-15
ingested: 2026-11-15
tags: [apps, replit, swmm5, epanet, force-mains, pumps]
reviewed: 11/16/2026
---
**What it is.** A technical summary of ForceMain SWMM5 EPANET Comparison, version 1.0: a Streamlit app for designing and checking force mains: friction-loss calculators, a network analyzer, writers of SWMM5 and EPANET input files, and runs of both engines on paired generated models. It is one of Bob's Replit apps, at `forcemainswmm5epanetcomparison.com`. Raw file: [raw/apps/force-main-robertdickinson-v1.0.md](../../raw/apps/force-main-robertdickinson-v1.0.md).

**How it was written. This one is different.** The app ships no summary of its own making. Replit Agent wrote the file on 15 November 2026 from the project's source, and the file says Bob has not yet reviewed it (Q74). Of the app itself it says the repository does not record which AI tools helped build it. The copy here was read out of the editor of the Replit project named ForceMain_SWMM5_EPANET_Comparison on 15 November 2026 and matched a SHA-256 computed there (see the log).

**Claims worth keeping** (all copied from the file)
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

**Limits it states.** No design-engineer review, production study or comparison with a field system. The screenshot check caught a loading placeholder, so the layout is unverified. The project states no license.

**Checked at ingest.** The site address in the file is `forcemainswmm5epanetcomparison.com`, not a `.replit.app` name. The `date:` is the day of the summary (Q75). The calculator is SI; the US customary Hazen-Williams form is in [S115](S115-epanet-for-swmm5-experts-replit-summary.md).

**Feeds:** [ForceMain SWMM5 EPANET Comparison (app)](../entities/forcemain-swmm5-epanet-comparison.md), [Replit apps: the second seventeen summaries](../concepts/replit-app-summaries-second-batch.md), [Force main friction](../concepts/force-main-friction.md), [Pumps and pump curves](../concepts/pumps-and-pump-curves.md), [EPANET for SWMM5 Experts (app)](../entities/epanet-for-swmm5-experts.md).
