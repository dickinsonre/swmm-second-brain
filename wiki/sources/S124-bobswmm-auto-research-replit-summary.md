---
title: "S124: bobSWMM Auto Research, summary written by Replit Agent (v0.0.0)"
type: source
raw: raw/apps/bob-swmm-auto-research-v0.0.0.md
kind: app-md
author: Robert Dickinson
published: 2026-03-12
ingested: 2026-11-15
tags: [apps, replit, swmm5, ai, calculators]
drafted_by: Replit Agent (an AI), from the project's source
reviewed: 11/16/2026
---
**What it is.** A technical summary of bobSWMM Auto Research, version 0.0.0: an app that answers SWMM modeling questions with AI-written reports and chat, and adds browser calculators and inspectors for `.inp` and `.rpt` files. It is one of Bob's Replit apps, at `bob-swmm-auto-research.replit.app`. Raw file: [raw/apps/bob-swmm-auto-research-v0.0.0.md](../../raw/apps/bob-swmm-auto-research-v0.0.0.md).

**How it was written. This one is different.** The app ships no summary of its own making. Replit Agent wrote the file on 15 November 2026 from the project's source, and the file says Bob has not yet reviewed it (Q74). Of the app itself it says the project documents and Git subjects do not establish which edits were made by Replit Agent or another AI builder. The copy here was read out of the editor of the Replit project named BobSWMM Auto Research on 15 November 2026 and matched a SHA-256 computed there (see the log).

**Claims worth keeping** (all copied from the file)
- No SWMM engine is called; the calculators are educational examples in the browser. `engines: none`.
- Reports come from OpenAI model `gpt-5.2`. The context is found by matching keywords against 8 curated topics; the file calls this keyword retrieval, not a demonstrated live literature search.
- 23 application routes, 6 calculator tabs, 60 research presets and 3 database tables.
- Green-Ampt is an explicit approximation, `fp = Ks*(1 + psi*dTheta/F)`, in inches and inches/hour, not the engine's iterative solver.
- RTK sums triangular responses with `Tb = Tp*(1+K)` and `qp = 2*R/Tb`, sampled every `0.1` hour. Plotting is capped at `72` hours, which can truncate long responses.
- Manning uses `k=1.49` in US customary units and `k=1.0` in SI. The surcharge calculator applies a synthetic inflow to a fixed capacity of `10` cubic feet/second.
- The TypeScript check failed with 7 diagnostics. No test files were found: 0 passed, 0 failed.
- A read-only browser run loaded 22/22 static pages and 1/1 research-detail page with HTTP 200.
- Knowledge entries carry `reviewed: true`, but the records name no human reviewer.
- Repository: https://github.com/SWMMBobSWMM6/BobSWMM-Auto-Research. Project license MIT, with Robert Dickinson named in `LICENSE`.

**Limits it states.** No numerical comparison with EPA SWMM. New AI reports, chat and citation accuracy were not checked. Uploads, downloads and deletion were not checked. The repository address was not checked for reachability.

**Checked at ingest.** Version 0.0.0; the `date:` is the earliest package-history date, 12 March 2026 (Q75).

**Feeds:** [bobSWMM Auto Research (app)](../entities/bobswmm-auto-research.md), [Replit apps: the second seventeen summaries](../concepts/replit-app-summaries-second-batch.md), [RDII unit hydrographs (RTK)](../concepts/rdii-unit-hydrographs.md), [Infiltration methods](../concepts/infiltration-methods.md).
