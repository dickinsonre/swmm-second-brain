---
title: "S296: Surcell, summary written from the page (v2026-10-28)"
type: source
raw: raw/apps/surcell-fly-inside-4d-v2026-10-28.md
kind: app-md
author: Robert Dickinson
published: 2026-10-28
ingested: 2026-11-18
tags: [apps, geometry, four-dimensions, curvature, webgl]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app Surcell, version 2026-10-28: a flight game inside curved three-dimensional worlds that sit in four dimensions (the 3D boundary, or "surcell", of a 4D shape), with light traced along geodesics on the graphics card and a panel that measures curvature where you stand. Raw file: [raw/apps/surcell-fly-inside-4d-v2026-10-28.md](../../raw/apps/surcell-fly-inside-4d-v2026-10-28.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q111). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/6gFmSRkT8uHrEPV2YHJZG7, version 1793232062-aa89 (index.html, 463,123 bytes, SHA-256 e4c7472a686310d831805907a53064278c274617cea642dd7d39b7a80ed390e1). The page did not finish loading in headless Chromium, so its text was read from the HTML source on 2026-11-18. Nothing was run to write this file." The page says the flight app reached its import as a finished file supplied by Bob, with no record of who wrote it or with what tools; Claude did the import in October 2026, fixed five defects and wrote the About, Doc and checks.

**Claims worth keeping** (all copied from the file)
- Ten worlds: Glome, Spheritorus, Torisphere, Tiger, Ditorus, Hyperbolic, Catenoid, Helicoid, Schwarz P and Revolution with chosen profile curves.
- The lemniscate cosine for the 4D catenoid is computed with four steps of the arithmetic-geometric mean, good to a part in a trillion against the defining integral; the 4D catenoid stays inside a slab 2.62 neck-radii thick.
- Checks: closed-form curvature, the lemniscate integral, Gauss-Bonnet, an independent Gram-matrix calculation of honeycomb edges and 72 timed loop walks.

**Limits it states.** Rendering checked in software WebGL only, not on a GPU; Schwarz P is an approximation; the Helicoid has no recentring; the shader holds 40 to 128 objects; no person has flown the build or checked the history claims.

**Checked at ingest.** Not a water app. The page did not finish loading in headless Chromium, so the summary was written from its source text. The `links:` line gives Netlify as https://surcell-fly-inside-4d.netlify.app.

**Feeds:** [Surcell (app)](../entities/surcell.md), [Apps summarized on 17 and 18 November 2026: AI workflows, tools and puzzles](../concepts/apps-from-pages-tools-and-puzzles.md), [Graphs: nodes, edges, direction and weight](../concepts/graph-basics.md).
