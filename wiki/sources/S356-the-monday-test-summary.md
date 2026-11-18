---
title: "S356: The Monday Test, summary written from the page (v1.1)"
type: source
raw: raw/apps/the-monday-test-v1.1.md
kind: app-md
author: Robert Dickinson
published: 2026-10-20
ingested: 2026-11-18
tags: [apps, teaching, swmm5, icm, swmm6, evidence]
drafted_by: Claude (Anthropic), from the published page
reviewed: 2026-11-18
---
**What it is.** A technical summary of the app The Monday Test, version 1.1: nine experiences for SWMM5, ICM and SWMM6 modelers. Raw file: [raw/apps/the-monday-test-v1.1.md](../../raw/apps/the-monday-test-v1.1.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/3aqovTBsG3FZq36JBRmjBS, version 1792448291-0d78 (index.html, 262,238 bytes, SHA-256 ed2df5fd372fdf5fcfe797800151586b874d14d98f6173dbe601953461ce0204), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file." Its AI-use section: "The page says: Robert Dickinson directed the work and is responsible for it; he chose the frame, decided to apply it to SWMM teaching, supplied the nine findings from his own measured work, set the standard that any engine number must be run rather than recalled, and reviewed the result."

**Claims worth keeping** (all copied from the file)
- Nine short "journeys" for SWMM5, InfoWorks ICM and SWMM6 modelers, each built on a finding from Bob's own measured work and walked through Jeff Bullas's six-stage Transformation Economy arc (surprise, understand, choose, act, reflect, transform), ending in a Monday card: what you will do differently on Monday. Examples: "The sealed lawn" (MaxInfil = 0.5 in or 50 in, the lawn seals either way); "Two missing lines" (same .inp, two builds, 64.31 cfs and 24.69 cfs); "Exit code zero" (the run failed and the process says it did not); "HYDGRAD, not gradient" (ICM field names are case-sensitive).
- The app does not let the frame vouch for the claims: its Evidence table has one row per claim with the engine, build, date and what the claim does not cover. Of 23 claims, 12 were run on a compiled engine or a real script for this app on 27 September 2026, 3 were exercised against a stub of ICM, and 8 are cited from earlier work and not re-run.
- The Evidence table's census: engine-verified 9, source read and engine-confirmed 2, tested 1, stub-verified 3, from Bob's record 3, from his record and not re-run 5.

**Limits it states.** As the page states: that any finding holds on your models, builds or ICM version.

**Checked at ingest.** Read in full; nothing was rerun at ingest. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [The Monday Test (app)](../entities/the-monday-test.md), [Apps summarized on 18 November 2026: papers, AI and films about the work](../concepts/apps-from-pages-papers-ai-and-films.md), [Six quality markers for app-building work](../concepts/app-quality-markers.md), [LinkedIn posts that were well received](../concepts/linkedin-post-reception.md).
