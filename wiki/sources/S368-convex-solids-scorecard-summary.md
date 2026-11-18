---
title: "S368: Convex Solids Scorecard, summary written from the page (v2026-10-09)"
type: source
raw: raw/apps/convex-solids-scorecard-v2026-10-09.md
kind: app-md
author: Robert Dickinson
published: 2026-10-09
ingested: 2026-11-18
tags: [dashboards, physics, not-water]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the dashboard Convex Solids Scorecard, version 2026-10-09: what the Convex Solids Physics build measures about itself. Raw file: [raw/apps/convex-solids-scorecard-v2026-10-09.md](../../raw/apps/convex-solids-scorecard-v2026-10-09.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude Data artifact https://claude.ai/artifact/NPJWmFKSksmYcKAr9jpq5z, version 1791516991-3e6b (index.html, 21,694 bytes), its page file (index.html in the files collection, 45,877 bytes) and its 12 datasets with their CSV files, read on 2026-11-18. The Netlify page beside this file was converted from them by Claude on 2026-11-18. Nothing was run to write this file." Its AI-use section: "The dashboard carries no AI-use note. The Netlify copy was converted from the Data artifact by Claude on 18 November 2026: the page's markup, styles and drawing code are unchanged and a small script stands in for the dashboard's data loader. This summary was written by Claude (Anthropic) on 18 November 2026."

**Claims worth keeping** (all copied from the file)
- A one-page dashboard about Convex Solids Physics v4.60, a 3D physics app of every convex polyhedron with regular faces. Every figure was read out of the running app, not written down beside it: 104 engine controls (91 pass, 13 reproduced limitations, 0 fail), a catalogue of 239 solids, the file's own size and surface, frame rates, the demo film and 13 defects closed in the session. Not a water-modeling app.
- It shows the largest limitation measured rather than described: cannon.js 0.6.2 bounds friction as an impulse per step, not as a force, so the same cube at the same friction slides 6.63 m (21.8 ft, ours) in 2 s at a 1/30 s step, 3.15 m at 1/60 s, 0.01 m at 1/120 s and 0.0 m at 1/240 s. At slider friction 0.4, Coulomb says sliding starts at 21.8°; the engine starts a 1 kg cube at 8.5° and a 1,000 kg tetrahedron at 9.0°.

**Limits it states.** As the dashboard states: the frame rates come from software WebGL in a headless container, and a machine with a GPU is far quicker; the gate's two figures are the code's own constants, not a dataset; the counts come from one headless run of v4.60.

**Checked at ingest.** 91 + 13 + 0 = 104 controls (our arithmetic). A Claude Data artifact, converted to a standalone page for Netlify with a small script standing in for the dashboard's data loader. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [Convex Solids Scorecard (dashboard)](../entities/convex-solids-scorecard.md), [Apps summarized on 18 November 2026: calculators, toys and apps that are not about water](../concepts/apps-from-pages-calculators-toys-and-not-water.md).
