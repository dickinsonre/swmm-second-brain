---
title: "S361: Ponce Hydrology Lab, summary written from the page (v1.2)"
type: source
raw: raw/apps/ponce-hydrology-lab-v1.2.md
kind: app-md
author: Robert Dickinson
published: 2026-10-22
ingested: 2026-11-18
superseded_by: S390
tags: [apps, hydrology, calculators, audits]
drafted_by: Claude (Anthropic), from the published page
reviewed: 2026-11-18
---
**What it is.** A technical summary of the app Ponce Hydrology Lab, version 1.2: thirty-six hydrology and hydraulics modules after Victor Miguel Ponce's web library. Raw file: [raw/apps/ponce-hydrology-lab-v1.2.md](../../raw/apps/ponce-hydrology-lab-v1.2.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/68sBRNXNG46AvRq1NscxMQ, version 1792675605-04c4 (index.html, 3,539,623 bytes, SHA-256 df2047d8c726534595017834d7e6da186bc6faa73e2bff46af8c5c6747784199), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file." Its AI-use section: "The page says: the original React project (aquifer-quest-zone) was built in Lovable, an AI app builder, under the direction of Robert (Bob) Dickinson, from Prof. Ponce's published material. This single-file edition was made with Claude, Anthropic's AI model, in Claude Code sessions on 21 and 22 October 2026."

**Claims worth keeping** (all copied from the file)
- Thirty-six hands-on hydrology and hydraulics modules in one file, built on the web hydrology library of Prof. Victor Miguel Ponce at San Diego State University: move a slider and the equation, the numbers and the chart answer at once. An independent adaptation, from Bob's Lovable project aquifer-quest-zone, and a teaching instrument, not a design code.
- Fifty-seven calculation defects were fixed across three versions (nineteen in v1.0, seven in v1.1, thirty-one in v1.2), each with the original code quoted in the Doc register. The page passes 208 unit tests and 26 formulation checks against Prof. Ponce's own calculator pages; in v1.2 the theory and reference text got 32 corrections and 13 dead links fixed.
- 208 unit tests; 26 formulation checks against Prof. Ponce's calculator pages.
- Every one of the 36 module pages, plus the home, About and Doc pages, opened in headless Chromium in both themes, both unit systems and at 375 px: no console errors, no sideways scroll, and in US mode no SI unit left on any page.
- 57 defects fixed, listed with the original code.

**Limits it states.** As the page lists it, starting with the curve number method: no runoff below the initial abstraction, and runoff under 0.5 in is the least reliable region (TR-55). It is a teaching instrument, not a design code. The page lists further limits by module in the Doc.

**Checked at ingest.** Read in full; nothing was rerun at ingest. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [Ponce Hydrology Lab (app)](../entities/ponce-hydrology-lab.md), [Apps summarized on 18 November 2026: calculators, toys and apps that are not about water](../concepts/apps-from-pages-calculators-toys-and-not-water.md), [Infiltration methods](../concepts/infiltration-methods.md).
