---
title: "S388: Note, Walk the Mesh's Netlify address (2026-11-19)"
type: source
raw: raw/apps/walk-the-mesh-address-2026-11-19.md
kind: note
author: Robert Dickinson
published: 2026-11-19
ingested: 2026-11-19
tags: [apps, sites, netlify]
drafted_by: Robert Dickinson (his words, typed in by Claude)
reviewed: no
---
**What it is.** Bob's answer to a question about where Walk the Mesh is deployed, with the checks Claude made before asking. Raw file: [raw/apps/walk-the-mesh-address-2026-11-19.md](../../raw/apps/walk-the-mesh-address-2026-11-19.md).

**How it was written.** Claude asked the question in a Claude session on 19 November 2026 as a multiple-choice question; Bob chose an answer. Claude (Anthropic) wrote the note on the note template, copying the question and the answer as they appeared. The checks are Claude's, and the note marks them as such. Bob has not yet read the note.

**Claims worth keeping**
- The question: "The showcase links Walk the Mesh to walk-the-mesh.netlify.app, but that site isn't on your Netlify team. A site named walk-the-swmm6-2d-mesh was drag-and-dropped today at 11:59 am. Is that Walk the Mesh?" Bob's answer: "Yes, point the showcase there".
- So Walk the Mesh is at https://walk-the-swmm6-2d-mesh.netlify.app. The address https://walk-the-mesh.netlify.app in the note of 17 November 2026 [S205](S205-note-netlify-addresses.md) is not on his team.
- Claude's checks, through Bob's Netlify connector, read-only, on 19 November 2026: no project named walk-the-mesh was on his team, and of the 62 addresses in that note it was the only one missing. The project walk-the-swmm6-2d-mesh had one production deploy, by drag and drop, published 2026-11-19 16:59 UTC, with one file, index.html.

**Checked at ingest.** The note sits in `raw/apps/`, not `raw/notes/` where notes go, and the manifest files it as an app with no version. The agent does not move raw files; Bob may move it, and this page's `raw:` line would then change with it.

**Feeds:** [Walk the Mesh (app)](../entities/walk-the-mesh.md), [SWMM Enablement Showcase (app)](../entities/swmm-enablement-showcase.md).
