---
name: Ommatidia Flyover
file: ommatidia-flyover.html
version: 1.4.1
date: 2026-11
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/PVchfLBNcohExVSAN43Ubd", repo: none}
engines: none (reads a SWMM model's .inp and .out; the .out reader is checked against the SWMM Results Kit reader)
units: US customary (ft, in/hr, cfs); SI models converted for display
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude starting 3 November 2026 under Robert Dickinson's direction, and that version 1.4 answers an outside review. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/PVchfLBNcohExVSAN43Ubd, version 1793750422-2be7 (index.html, 1,111,001 bytes, SHA-256 619b732209d20a04058b2edd6e917df792f2c99bb57c8c7c380a87712392d1fb), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# Ommatidia Flyover: a compound-eye organism that flies over a SWMM model to where flow is peaking

## In three points
- **What:** A compound-eye creature that flies over a SWMM model and goes where flow is peaking. The map outside its lenses is the model; the picture inside each lens is the run: bright dots for a parcel running off, dashes for moving water, line width for the share of a pipe filled, white dashes for a full pipe, orange for a flooding node, and two numbers in feet (the nearest node's invert over the nearest pipe's length). It works as a page and as one file to add to other apps.
- **So what:** Its .out reader matched 8,875,800 values across four models (the Bellinge test network included) against the SWMM Results Kit reader with 0 wrong; 5 of 5 lens depths matched the .out with 0 ft difference; 400 printed lens numbers and 448 node and 448 pipe labels matched a separate .inp parser. A regression suite of 31 cases built from an outside review: version 1.3 passes 0, version 1.4 passes 31.
- **Now what:** Use it to see where a model's runoff and flow peak, as a pointer. A bright lens gives no depth on the ground; the track is an average of votes and can sit over a block with no pipe; between saved reports the app draws a straight line.

This summary was written after the fact. The page ships no technical summary of its own. Its version is the page's own ("v1.4.1"); the first build was 3 November 2026, and the page gives no date for 1.4.1. The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Flight, In your apps, About, Doc. Pause freezes the clock, the fly and the water. The Inspector holds one node, pipe or subcatchment and reads it at the shown time. Light blue lines are pipes, white squares nodes, yellow outfalls, green storage; subcatchments are hatched by imperviousness (wide under 25%, medium 25 to 60%, close above 60%). The fly tags the nearest nodes and pipes with their IDs. A bright lens marks a parcel near the 92nd percentile of peak runoff per acre.

## Checks (as stated on the page)

- .out reader: 8,875,800 values across four models, 0 wrong. Lens readings: 5 of 5 depths with 0 ft difference.
- Regression suite: 31 cases from the outside review (1.3 passes 0, 1.4 passes 31).
- Numbers in the lenses: 400 at the default size on four models, 0 wrong (Bellinge is metric and its labels convert to feet; the smallest text is 7.7 px). Full labels at a 36 px lens: 448 node and 448 pipe labels, 0 wrong, none of 1,792 rows overflowing. ID tags on the map: 362, 0 wrong, 0 overlaps, 0 off the map.
- Size: in normal flight on a 1,200 px map, the fly spans 11.1% to 18.1% of the model's long side across the four models; a separating-axis test on all 676 convex parcels.

## What this does not show

As the page lists it: no depth on the ground from a bright lens; the track is a pointer, not a path; lens numbers belong to the node and pipe nearest the +, which can sit just outside the patch a lens shows; ID tags skip any that would overlap, so one pass does not show every ID; between saved reports the app interpolates, and SWMM computed nothing there.

## Credits and licenses

The form follows a screenshot of the post "ommatidia" by Kat the Poet Engineer (@poetengineer__); this is an independent build from that one image, none of her code was seen or used, and the SWMM reading of the lenses is new. Bellinge test network: Nedergaard Pedersen et al. (2021), CC BY 4.0, used for testing only. The SWMM Results Kit reader. No license is stated for the page.

## AI use

The page says: built with Claude, Anthropic's AI model, in a Claude session on 3 November 2026 under the direction of Robert (Bob) Dickinson, who chose the project, supplied the screenshot and set the standing rules; responsibility is his. Versions 1.1 to 1.3 followed his requests after each version (a smaller fly, IDs, inverts and pipe lengths in the lenses, standing-out nodes and links, a GIF of the whole app, hatched subcatchments), and 1.4 answers an outside review. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 1.4.1: the version read. 1.4: fixes from an outside review (31 regression cases). 1.3: hatched subcatchments, lenses sized to their numbers. 1.2: smaller fly, light green subcatchments, a GIF. 1.1: IDs, inverts and pipe lengths in the lenses. 1.0 (2026-11-03): first version.
