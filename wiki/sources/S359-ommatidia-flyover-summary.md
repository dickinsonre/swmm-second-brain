---
title: "S359: Ommatidia Flyover, summary written from the page (v1.4.1)"
type: source
raw: raw/apps/ommatidia-flyover-v1.4.1.md
kind: app-md
author: Robert Dickinson
published: 2026-11
ingested: 2026-11-18
tags: [apps, swmm5, out-reader, 3d]
drafted_by: Claude (Anthropic), from the published page
reviewed: 2026-11-18
---
**What it is.** A technical summary of the app Ommatidia Flyover, version 1.4.1: a compound-eye organism that flies over a SWMM model to where flow is peaking. Raw file: [raw/apps/ommatidia-flyover-v1.4.1.md](../../raw/apps/ommatidia-flyover-v1.4.1.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/PVchfLBNcohExVSAN43Ubd, version 1793750422-2be7 (index.html, 1,111,001 bytes, SHA-256 619b732209d20a04058b2edd6e917df792f2c99bb57c8c7c380a87712392d1fb), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file." Its AI-use section: "The page says: built with Claude, Anthropic's AI model, in a Claude session on 3 November 2026 under the direction of Robert (Bob) Dickinson, who chose the project, supplied the screenshot and set the standing rules; responsibility is his. Versions 1.1 to 1.3 followed his requests after each version (a smaller fly, IDs, inverts and pipe lengths in the lenses, standing-out nodes and links, a GIF of the whole app, hatched subcatchments), and 1.4 answers an outside review."

**Claims worth keeping** (all copied from the file)
- A compound-eye creature that flies over a SWMM model and goes where flow is peaking. The map outside its lenses is the model; the picture inside each lens is the run: bright dots for a parcel running off, dashes for moving water, line width for the share of a pipe filled, white dashes for a full pipe, orange for a flooding node, and two numbers in feet (the nearest node's invert over the nearest pipe's length). It works as a page and as one file to add to other apps.
- Its .out reader matched 8,875,800 values across four models (the Bellinge test network included) against the SWMM Results Kit reader with 0 wrong; 5 of 5 lens depths matched the .out with 0 ft difference; 400 printed lens numbers and 448 node and 448 pipe labels matched a separate .inp parser. A regression suite of 31 cases built from an outside review: version 1.3 passes 0, version 1.4 passes 31.
- .out reader: 8,875,800 values across four models, 0 wrong. Lens readings: 5 of 5 depths with 0 ft difference.
- Regression suite: 31 cases from the outside review (1.3 passes 0, 1.4 passes 31).
- Numbers in the lenses: 400 at the default size on four models, 0 wrong (Bellinge is metric and its labels convert to feet; the smallest text is 7.7 px). Full labels at a 36 px lens: 448 node and 448 pipe labels, 0 wrong, none of 1,792 rows overflowing. ID tags on the map: 362, 0 wrong, 0 overlaps, 0 off the map.
- Size: in normal flight on a 1,200 px map, the fly spans 11.1% to 18.1% of the model's long side across the four models; a separating-axis test on all 676 convex parcels.

**Limits it states.** As the page lists it: no depth on the ground from a bright lens; the track is a pointer, not a path; lens numbers belong to the node and pipe nearest the +, which can sit just outside the patch a lens shows; ID tags skip any that would overlap, so one pass does not show every ID; between saved reports the app interpolates, and SWMM computed nothing there.

**Checked at ingest.** Read in full; nothing was rerun at ingest. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [Ommatidia Flyover (app)](../entities/ommatidia-flyover.md), [Apps summarized on 18 November 2026: papers, AI and films about the work](../concepts/apps-from-pages-papers-ai-and-films.md), [SWMM Results Kit](../entities/swmm-results-kit.md), [Bellinge (app)](../entities/bellinge-app.md).
