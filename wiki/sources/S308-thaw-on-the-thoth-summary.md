---
title: "S308: Thaw on the Thoth, summary written from the page (v2026-10-21)"
type: source
raw: raw/apps/thaw-on-the-thoth-v2026-10-21.md
kind: app-md
author: Robert Dickinson
published: 2026-10-21
ingested: 2026-11-18
tags: [documents, swmm5, fiction, gravity, weirs, finite-volume]
drafted_by: Claude (Anthropic), from the published page
reviewed: 2026-11-18
---
**What it is.** A technical summary of the document Thaw on the Thoth, version 2026-10-21: a story of two boys, one Martian canal and the spring thaw of 2097. Raw file: [raw/apps/thaw-on-the-thoth-v2026-10-21.md](../../raw/apps/thaw-on-the-thoth-v2026-10-21.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude Docs document https://claude.ai/artifact/CmsNSow2yFY9dS72KHRc2R, artifact version 1793394821-af7e, document revision 13, exported as HTML with its 16 pictures on 2026-11-18. The Netlify page beside this file was set from that export by Claude on 2026-11-18. Nothing was run to write this file." Its AI-use section: "The document says: the story and everything behind it were made with Claude, Anthropic's AI model, in a Claude Code session in October 2026 at the request of Robert (Bob) Dickinson, who asked for a story about boys on Mars modeling canal flow in the spirit of Red Planet, set the house style and is responsible for what is published."

**Claims worth keeping** (all copied from the file)
- A short story in seven chapters and an afterword, in the spirit of Robert A. Heinlein's Red Planet (1949). Two boys at a Mars colony check the Canal Company's SWMM forecast for a thaw on an invented canal, the Thoth, and find that gravity hides in Manning's n and the weir coefficient. The people, the colony and the night of the thaw are invented. The canal model, the two engines and every number on every chart come from runs of EPA SWMM 5.2.4 and swmm524-fvlink rebuilt with Mars gravity, and the afterword sorts one from the other.
- Changing GRAVITY from 32.2 to 12.2 alone left mile one at 2.38 ft at base flow, because gravity sits in both the slope term and the friction term (Conduit[k].roughFactor = GRAVITY * SQR(roughness/PHI)). Holding g·n² fixed scales n by 1.625 (0.015 to 0.0244) and the weir coefficient by 0.6155 (3.33 to 2.050). The Upper Thoth then carries 4,439 cfs bank-full instead of 7,213, against a 4,200 cfs crest, and the basin reaches the top of its 14.5 ft levee at hour 40.3 (the chart's legend says 40.4) instead of cresting at the Company's 13.3 ft. Building the model also found water running uphill through a finite volume throat, now entered as FVL-15 in the branch's defect register.

**Limits it states.** As the document states: the Thoth is invented and has no survey behind it; the scaling of n and the weir coefficient is ordinary dimensional reasoning that has never been checked against flow in a lined canal on Mars; the gauge readings are fiction set near the model's values; no person has yet reviewed the story or rerun the models, and no other engineer has checked the scaling.

**Checked at ingest.** The story's text says the basin reaches the top of the levee at hour 40.3; the legend of its chart "The forecast at the levee" says "at the crest by hour 40.4" (Q118). A Claude Docs document, exported as HTML with its 16 pictures for Netlify. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [Thaw on the Thoth (document)](../entities/thaw-on-the-thoth.md), [Apps summarized on 18 November 2026: SWMM6, SWMM5+ and solvers](../concepts/apps-from-pages-swmm6-solvers-and-swmm5plus.md), [Dynamic wave routing](../concepts/dynamic-wave-routing.md), [Weirs and outlets](../concepts/weirs-and-outlets.md), [EPA SWMM 5](../entities/swmm-5.md).
