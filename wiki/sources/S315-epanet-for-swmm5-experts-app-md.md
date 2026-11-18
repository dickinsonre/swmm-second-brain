---
title: "S315: EPANET for SWMM5 Experts, app .md (v2.0.0)"
type: source
raw: raw/apps/epanet-for-swmm5-experts-v2.0.0.md
kind: app-md
author: Robert Dickinson
published: 2026-11-12
ingested: 2026-11-18
tags: [apps, epanet, swmm5, force-mains, verification]
drafted_by: Claude (Anthropic), with the app
reviewed: no
---
**What it is.** A technical summary of the app EPANET for SWMM5 Experts, version 2.0.0: EPANET explained in SWMM5 terms, checked against both engines. Raw file: [raw/apps/epanet-for-swmm5-experts-v2.0.0.md](../../raw/apps/epanet-for-swmm5-experts-v2.0.0.md).

**How it was written.** The app ships this file; Claude added its In three points block on 18 November 2026 when it was packaged for Netlify. Its AI-use section: "This app was built with AI, and so were its errors. Robert Dickinson chose the subject, supplied the source material and the reviews, set the standard that numbers must come from the engines, and is responsible for the work. **Versions 1.0 and 1.1 (March 2026).** Claude, the AI model made by Anthropic, wrote the first build in a chat session, from his direction and attachments."

**Claims worth keeping** (all copied from the file)
- A single HTML file of 35 tabs that explains the EPANET water distribution engine to engineers who already know SWMM5: objects, demands, head loss formulas, solvers, pumps, valves, water quality and file formats, mapped from one program to the other, with calculators. Version 2.0 adds a Verify tab (engine comparisons and a corrections register), an About tab and a Doc tab.
- Version 2.0 ran the central claim through EPA SWMM 5.2.4, EPANET 2.2 and EPANET 2.3.5, all built from source. For one 12-in pipe, 1,000 ft long, Hazen-Williams C of 130, at six flows from 100 to 2,000 gpm, SWMM 5.2.4's FORCE_MAIN matched the formula within 0.001 ft and EPANET 2.2 matched to its 0.01 ft print resolution. The same work found 15 errors in version 1, among them printed source code that is not in SWMM5; all 15 are corrected and listed. 47 in-page tests compare the page's formulas with the stored engine numbers at every load.
- V1. SWMM 5.2.4 FORCE_MAIN matched the formula within 0.001 ft at 6 of 6 flows. EPANET 2.2 matched to its 0.01 ft print resolution.
- V2. Partly full (free outfall, 0.2, 0.5, 1.0 cfs): FORCE_MAIN and CIRCULAR with n = 0.01082 ran at depths 0.250, 0.397, 0.589 ft, identical to 0.001 ft. CIRCULAR with n = 0.013: 0.275, 0.440, 0.650 ft.
- V3. Manning with the equivalent n equals Hazen-Williams at 605 gpm (friction slope = pipe slope). It reads -24.0% at 100 gpm and +18.4% at 2000 gpm.
- V4. Flat main: WARNING 04, slope 1e-6, equivalent n 0.014263. Full-flow head loss unchanged (0.702 ft at 500 gpm). Partly full at 0.3 cfs: FORCE_MAIN depth 0.462 ft = CIRCULAR with n = 0.014263 (0.462 ft); CIRCULAR with n = 0.01082 gives 0.421 ft.

**Limits it states.** One pipe, one diameter, one C, one slope, steady flow. No loops, tanks, valves or pumps in the engine-to-engine comparison. No field data. Agreement between engines is not agreement with a real main. No test of the SWMM5 unsteady solution. Neither engine models water hammer. 13 of the original 32 tabs had passages corrected. 19 were not changed and were not audited beyond the source scan. A wrong number in a table that names no source would not have been caught. SI mode was exercised in a browser, not against an SI engine run. One machine, gcc 13.3 on Linux. No timing claims. Legacy diagrams and code blocks keep a dark background in the light theme.

**Checked at ingest.** Version 2.0 of the app whose version 1.0 summary is [S115](S115-epanet-for-swmm5-experts-replit-summary.md), by the app's own change list (1.0 of 2026-03-15, 1.1 in Replit). The two files name different apps on their `file:` lines (`epanet-swmm-experts` and `epanet-for-swmm5-experts.html`), so tools/manifest.py treats them as two apps; the wiki treats 2.0 as superseding 1.0 (Q117). Bob has since ruled that the two are one app, named EPANET for SWMM5 Experts [S376](S376-note-epanet-for-swmm5-experts-one-app.md), and the manifest groups them so. Its corrections register (C-1 to C-15) corrects version 1.x. The `links:` line names no Netlify address.

**Feeds:** [EPANET for SWMM5 Experts (app)](../entities/epanet-for-swmm5-experts.md), [Apps summarized on 18 November 2026: EPANET, converters and SWMM5 tools](../concepts/apps-from-pages-epanet-converters-and-swmm5-tools.md), [EPANET](../entities/epanet.md), [Force main friction](../concepts/force-main-friction.md), [Lewis A. (Lew) Rossman](../entities/lew-rossman.md).
