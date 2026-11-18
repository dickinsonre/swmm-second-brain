---
title: "S364: LEGO Water Flow Lab, summary written from the page (v1.0)"
type: source
raw: raw/apps/lego-water-flow-lab-v1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10
ingested: 2026-11-18
tags: [apps, toys, lego]
drafted_by: Claude (Anthropic), from the published page
reviewed: 2026-11-18
---
**What it is.** A technical summary of the app LEGO Water Flow Lab, version 1.0: will a molecule built from LEGO parts go down a pipe?. Raw file: [raw/apps/lego-water-flow-lab-v1.0.md](../../raw/apps/lego-water-flow-lab-v1.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/L1QkxgaadXnwuKyqyzNuoQ, version 1792897503-c98a (index.html, 514,628 bytes, SHA-256 449e9c5820df63c55cb9215b20094f4071d4ee814db89d76f9c05601b8839034), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file." Its AI-use section: "The page says: built with Claude, Anthropic's AI model, in a Claude Code session in October 2026 at the request of Robert (Bob) Dickinson, who wrote the original on Lovable (an AI app-building platform), published it under the MIT licence and supplied its source; responsibility is his."

**Claims worth keeping** (all copied from the file)
- A playful lab that asks whether a molecule built from LEGO parts fits down a household pipe, with a Pipe Fit Tester, a Flow Simulator with Auto-Test, sound and reassembly, a parts list, an assembly guide and a specs table. A single-file edition of Bob's Lovable project; it adds an Engineer's switch with real pipe tables (Schedule 40 steel, copper Type L, PEX SDR 9) and three fit rules, and an Audit tab.
- The audit of the Lovable source lists 12 findings (5 fixed, 2 with a switch added, 4 flagged, 1 changed). The worst: Auto-Test ran the starting pipe four times and recorded one row (D1); the fixed Auto-Test returns all four. Pipe tolerances are larger than several of the clearances shown, so a fit on paper can fail in the pipe.
- Node assertions that the as-shipped table reproduces every verdict hard-coded in the original.
- Headless-browser runs of both builds; the fixed Auto-Test returns all four rows.
- A console-error and contrast check of the rendered page in both themes.
- Every file in the source zip read, the original built and run, and every number that decides a fit checked against a published table.

**Limits it states.** As the page lists it: no water is modelled; the fit rules are for a straight pipe; pipe tables print nominal dimensions and the allowed tolerances are larger than several clearances shown; the stage draws the bore in proportion and the molecule as a fixed cartoon (the Pipe Fit Tester is the to-scale view). Not yet checked by a person: the edition as a whole, the bores against the printed standards, the faucet claim on the Problem card, and the parts list against a LEGO catalogue.

**Checked at ingest.** A different app from [SWMM5 Lego Model (app)](../entities/swmm5-lego-model.md). The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [LEGO Water Flow Lab (app)](../entities/lego-water-flow-lab.md), [Apps summarized on 18 November 2026: calculators, toys and apps that are not about water](../concepts/apps-from-pages-calculators-toys-and-not-water.md), [SWMM5 Lego Model (app)](../entities/swmm5-lego-model.md).
