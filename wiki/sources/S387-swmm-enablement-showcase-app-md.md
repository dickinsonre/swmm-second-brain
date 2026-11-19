---
title: "S387: SWMM Enablement Showcase, app .md (v1.0)"
type: source
raw: raw/apps/swmm-enablement-showcase-v1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-11-19
ingested: 2026-11-19
tags: [apps, showcase, sites, publishing]
drafted_by: Claude (Anthropic), with the app
reviewed: no
---
**What it is.** The technical summary of SWMM Enablement Showcase, version 1.0: one page that links twelve of Bob's browser apps, each with one finding and one limit. Raw file: [raw/apps/swmm-enablement-showcase-v1.0.md](../../raw/apps/swmm-enablement-showcase-v1.0.md).

**How it was written.** By Claude (Anthropic) on 19 November 2026, with the page, at Bob's request. The file's AI-use section: "Claude proposed twenty candidates, wrote and ran the checks, looked at flagged items, took the screenshots, wrote the card text from each app's summary, and built the page. Bob approved the twelve and is responsible for publishing it."

**Claims worth keeping** (all copied from the file)
- Twelve apps in four groups: Where SWMM came from; Inside the engine; Surfaces, meshes and sediment; How the claims are checked. Each card has a screenshot, the Netlify address, the app's own version and date, one finding with its numbers, one limit, and the engines.
- Six of the twelve run EPA SWMM 5.2.4 in the browser. The other six show recorded runs of SWMM 5.2.4 and OpenSWMM 6, the engine source, a claims register or textbook formulas, and each card says which.
- "Every finding and limit is copied from the app's own technical summary." Numbers are unchanged; some sentences were shortened or split.
- The twelve were checked on 19 November 2026 with first-minute.js in headless Chromium: script errors, dark first paint with the device set to light, 390 px phone width, values shown as NaN, undefined or Infinity, text contrast, and a .md beside the page. Flagged items were looked at by hand. One item was left as it is: a label in The Rigid Column Test's light theme at 2.06:1 contrast.
- The apps were checked from local copies of the deployed files, because netlify.app could not be reached from the build machine.
- The page computes nothing. It opens dark, with a Dark, Light and Auto control, and its sewer-profile drawing is an illustration, not a model result.
- It gives Walk the Mesh's address as https://walk-the-swmm6-2d-mesh.netlify.app.

**Limits it states.** The apps' own checks are repeated, not rerun. A screenshot shows only the app's opening view. The apps may change after 19 November 2026. Visual SWMM, SWMM6 Hands-On Watershed and Four Ways to K were fixed that day and are left off until they are redeployed.

**Checked at ingest.** Each of the twelve versions and dates matches the current source page the wiki holds for that app: S206, S257, S212, S240, S209, S216, S242, S253, S246, S218, S263 and S219. Eleven addresses match the Netlify note [S205](S205-note-netlify-addresses.md); Walk the Mesh's follows [S388](S388-note-walk-the-mesh-address.md). The `links:` line gives Netlify as "not yet deployed (suggested site name swmm-enablement-showcase)", and no project of that name was on Bob's Netlify team when it was read through his connector at ingest. Item 5 of "What this does not show" reads "No person other than Bob has reviewed the page"; the AI-use section says only that Bob approved the twelve.

**Feeds:** [SWMM Enablement Showcase (app)](../entities/swmm-enablement-showcase.md), [Walk the Mesh (app)](../entities/walk-the-mesh.md).
