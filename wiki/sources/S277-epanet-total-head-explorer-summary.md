---
title: "S277: EPANET Total Head Explorer, summary written from the page (v2026-11-03)"
type: source
raw: raw/apps/epanet-total-head-explorer-v2026-11-03.md
kind: app-md
author: Robert Dickinson
published: 2026-11-03
ingested: 2026-11-18
tags: [apps, epanet, head, solver, javascript-port, verification]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app EPANET Total Head Explorer, version 2026-11-03: a teaching explorer built on a JavaScript port of the EPANET 2.2 hydraulic solver, run on the EPANET manual's tutorial network (Listing C.1), from the three heads at one point to the network solve trial by trial. Raw file: [raw/apps/epanet-total-head-explorer-v2026-11-03.md](../../raw/apps/epanet-total-head-explorer-v2026-11-03.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q111). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/TTtt1KdWs3jrqJiGnxk3Zh, version 1793732520-dde4 (index.html, 450,814 bytes, SHA-256 22c022dec680fbb6bba4fa6ba4d0c7adb66576fe2923ef2c312081af6c45d869), every tab read in headless Chromium on 2026-11-18. The page calls itself the 2026 edition and gives no version number; the version above is the date of the review fixes. Nothing was run to write this file." The page says it was made with Claude (configured as claude-sonnet-5-5) in November 2026 under Bob's direction, after a written review of the first 2026 build graded 82 out of 100.

**Claims worth keeping** (all copied from the file)
- On the tutorial network the port agrees with compiled EPANET 2.2 and OWA-EPANET 2.3.5 to 4.4 x 10^-12 ft in head and 6.4 x 10^-11 gpm in flow over all 25 hourly steps, with equal trial counts and times; the two compiled engines are byte-identical.
- On 300 random small networks the port agrees with EPANET 2.2 to 4.0 x 10^-8 ft in 241 and to 1.7 x 10^-4 ft in 59.
- The first 2026 edition used 2.31 ft per psi and put node 2 at 386.66 psi instead of 387.02 (defect APP-1); pressure now uses EPANET's 0.4333 psi per ft (2.3079 ft per psi).
- The manual's printed Listing C.2 for hours 0 and 1: 14 of 14 node rows and 7 of 7 link rows within the printed precision; pump head -193.19 ft.

**Limits it states.** No valves, controls, rules, emitters, pressure-driven demand or water quality, and such input is refused; only gpm; the random networks are small; no person has read the port line by line against the C source.

**Checked at ingest.** At node 2, hour 0: 73.52 / 0.4333 = 169.67 ft, and 710 + 169.67 = 879.67 ft; the velocity head 2.98^2 / 64.4 = 0.138 ft (our arithmetic agrees). The `links:` line gives Netlify as https://epanet-total-head-explorer.netlify.app.

**Feeds:** [EPANET Total Head Explorer (app)](../entities/epanet-total-head-explorer.md), [Apps summarized on 17 and 18 November 2026: SWMM5, EPANET and the checks on them](../concepts/apps-from-pages-swmm5-epanet-checks.md), [EPANET](../entities/epanet.md), [Verification against printed runs](../concepts/verification-against-printed-runs.md), [Byte-for-byte gate](../concepts/byte-for-byte-gate.md).
