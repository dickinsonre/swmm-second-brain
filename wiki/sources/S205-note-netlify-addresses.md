---
title: "S205: Note, the 62 apps uploaded on 17 November 2026 are live on Netlify (2026-11-17)"
type: source
raw: raw/notes/netlify-addresses-2026-11-17.md
kind: note
author: Robert Dickinson
published: 2026-11-17
ingested: 2026-11-17
tags: [apps, netlify, handoff, assets]
drafted_by: Claude (Anthropic), from read-only Netlify queries at Bob's request
reviewed: no
---
**What it is.** A record, on the note template, of the Netlify addresses of the 62 apps whose summaries Bob uploaded to `raw/apps/` on 17 November 2026, with how each was checked. Raw file: [raw/notes/netlify-addresses-2026-11-17.md](../../raw/notes/netlify-addresses-2026-11-17.md).

**How it was written.** Claude (Anthropic) typed it in on 17 November 2026 from the answers of the Netlify connector, read-only, at Bob's request. Bob's three messages that day are quoted in it: he deployed the apps, uploaded the third group again, and renamed two sites. Bob has not read the note.

**Claims worth keeping**
- Bob deployed the 62 apps to Netlify on 17 November 2026.
- Each site was read with one `get-project` call: all 62 reported their current deploy as `ready`, with no password and no team sign-in required.
- The pages themselves were not opened, because netlify.app could not be reached from the session. "Live" means Netlify's own report that the deploy finished.
- Each address was matched to a summary by the file name without its version. Two sites first had other names, `hydroouple-interactive` and `icm-kcs`; Bob renamed them to `hydrocouple-interactive` and `icm-kcs-catalog`, and both read `ready` again.
- The twelve sites of the third group first showed no finished deploy; after Bob uploaded them again all twelve read `ready`.
- The note does not say that an app works or that the deployed page is the version its summary describes; the Netlify copies were uploaded separately from the artifacts the summaries were written from.

**Checked at ingest.** Several summaries say on their `links:` line that the app was "not yet deployed" or "none yet"; that was true when they were written, and this note overtakes it. With the note, the addresses of 62 more apps can be reached from this repository; see [Start here](../start-here.md) and Q104.

**Feeds:** every app page of the 17 November ingest, starting with [Apps summarized on 17 November 2026: SWMM history and the insides of SWMM5](../concepts/apps-from-pages-history-and-swmm5.md); [Start here](../start-here.md); [Open questions](../open-questions.md).
