---
title: "S318: WNTR Toolkit, summary written from the page (v1.0.0)"
type: source
raw: raw/apps/wntr-toolkit-v1.0.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-25
ingested: 2026-11-18
tags: [apps, epanet, wntr, resilience, tanks]
drafted_by: Claude (Anthropic), from the published page
reviewed: 2026-11-18
---
**What it is.** A technical summary of the app WNTR Toolkit, version 1.0.0: resilience ensembles for EPANET networks, from real WNTR runs on Net3. Raw file: [raw/apps/wntr-toolkit-v1.0.0.md](../../raw/apps/wntr-toolkit-v1.0.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/DzZ1WF3R9PiQrVkiobDcRm, version 1792896828-01b3 (index.html, 2,522,846 bytes, SHA-256 ce75bd8f0a7281d61d28c9f7cffbb1b76278bbcfa93068989c2efecc6f981034), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file." Its AI-use section: "The page says: built with Claude, Anthropic's AI model, in a Claude session on 24 October 2026 at the request of Robert (Bob) Dickinson, who supplied the Lovable project and owns the work. Claude read the Lovable source, ran the shipped runner, notebook and guide against WNTR 1.5.0 and logged what failed, fixed them, ran every study behind the page, and wrote the page and the Doc. The checks are mechanical."

**Claims worth keeping** (all copied from the file)
- A single-file rebuild of Bob's Lovable WNTR Toolkit. The landing page is kept and corrected; the Explorer, which drew synthetic curves on an invented "Net3-like" network, now shows WNTR 1.5.0 results for the real Net3 model (92 junctions, 117 pipes, 2 pumps, 3 tanks, 2 reservoirs), with criticality, ensemble and timing studies and a fixed toolkit (runner, notebook and guide) to run on your own model.
- When WNTR's own simulator and EPANET 2.2 disagree over two days, the tanks' books settle it: WNTR's worst tank is off by 4.2% of its working volume, while EPANET 2.2's tanks are off by 119%, 122% and 53%, because an empty tank keeps flowing out (from hour 18 tank 1 sits at its minimum level and EPANET still draws from it). The page traces this to a 0.0005-ft dead band in EPANET 2.2's head comparison, which EPANET 2.3 replaces. The shipped runner, notebook and guide failed; each failure on the Defects tab is a recorded error message.
- The shipped runner executed for each scenario family, the shipped notebook cell by cell and the shipped guide block by block on WNTR 1.5.0 with Net3; the fixed versions executed end to end the same way: all 140 ensemble runs, 4 baselines, 234 sweep runs and 200 timing runs completed with no failures.
- Baseline agreement between the two simulators: largest pressure difference 0.0006 psi (0.0004 m) over all junctions and hours.
- Tank continuity and empty-tank discharge computed for every run; WNTR's empty-tank discharge was zero in all of them.
- The EPANET mechanism confirmed from the result tables (head drops of 1.3e-05 to 1.4e-04 ft across the tank links against an HTOL of 5e-4 ft), read alongside src/hydstatus.c at tag v2.2 and on the development branch.

**Limits it states.** As the page lists it: one network (nothing run on a 10,000-pipe system, where WNTRSimulator is far slower); the page runs no hydraulics; hourly reporting, so controls and tank events inside an hour are not drawn and continuity errors of a few percent remain in healthy runs; pipe closures are idealized status changes; the earthquake model is WNTR's tutorial recipe with one fragility curve, uncorrelated damage, no tank damage and no repairs, and Net3's coordinates were multiplied by 1,000 to make meters; population is demand / 200 gal/person/day, not a census; EPANET 2.3 was not run (its empty-tank fix is taken from its source and release notes); water quality appears only in the fixed notebook.

**Checked at ingest.** Read in full; nothing was rerun at ingest. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [WNTR Toolkit (app)](../entities/wntr-toolkit.md), [Apps summarized on 18 November 2026: EPANET, converters and SWMM5 tools](../concepts/apps-from-pages-epanet-converters-and-swmm5-tools.md), [EPANET](../entities/epanet.md).
