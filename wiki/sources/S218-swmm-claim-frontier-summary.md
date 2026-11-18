---
title: "S218: SWMM Claim Frontier, summary written from the page (v1.0)"
type: source
raw: raw/apps/swmm-claim-frontier-v1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-09-30
ingested: 2026-11-17
tags: [apps, verification, findings, claims-register]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app SWMM Claim Frontier, version 1.0: a register of the claims made in Bob's SWMM work, each placed on a tier (analytic or exhaustive, engine-verified, evidence, wall, conjecture, hunch) and tied to the engine builds it was verified on, with a graph, the walls, corpus coverage and the loop that produces new claims. It reruns none of them. Raw file: [raw/apps/swmm-claim-frontier-v1.0.md](../../raw/apps/swmm-claim-frontier-v1.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 17 November 2026, at Bob's request, from the published Claude artifact, version 1790769393-3fe8, reading every tab in a headless browser; nothing was run to write it. Bob has not read it (Q108). The published page carries no AI-use note; it is a Claude artifact on Bob's account, built in a claude.ai session. The summary says the Netlify copy adds a one-line AI-use note.

**Claims worth keeping** (all copied from the file)
- Tiers: analytic or exhaustive 12, engine-verified 43, evidence 10, wall 19, conjecture 9, hunch 2. So 65 claims hold at a stated tier; the 19 walls each carry a lesson.
- 20 claims are stale on the builds in service. A claim goes hollow when none of the builds it was verified on is still in service; unticking a build retires it.
- Builds listed, with the claims verified on each: EPA SWMM 5.2.4 (gcc from the v5.2.4 tag; swmm-toolkit and pyswmm 2.1.0 carry the same engine, 52004) 40; EPA SWMM 5.2.2 wasm (@fileops/swmm-wasm-web 0.0.4) 13; EPA develop 2; 5.2.4 with Slot Lab variants 2; openswmm-legacy 5.3.0-beta.3 2; OpenSWMM 6.0.0-alpha.2 handle and CLI builds 14 and 5.
- 99.9 % of the corpus by nodes is uncharted (the mean of four coverage measures); for one build, 589 models covering 66.5 % of corpus nodes show 0 of 589 on each of Q1 to Q4.

**Limits it states.** The claims are not rerun by the page; each carries the build it was verified on.

**Checked at ingest.** 12 + 43 + 10 = 65, as stated. The summary gives 11 claims as open; conjecture 9 plus hunch 2 is 11. The page is older than the [The SWMM findings register](../concepts/findings-register.md) format of October 2026 and keeps a different set of tiers; neither cites the other in what was read. The `links:` line gives Netlify as "not yet deployed"; Netlify reported a finished deploy at https://swmm-claim-frontier.netlify.app on 17 November 2026 [S205](S205-note-netlify-addresses.md).

**Feeds:** [SWMM Claim Frontier (app)](../entities/swmm-claim-frontier.md), [Apps summarized on 17 November 2026: SWMM history and the insides of SWMM5](../concepts/apps-from-pages-history-and-swmm5.md), [The SWMM findings register](../concepts/findings-register.md), [Negative results](../concepts/negative-results.md), [1729-SWMM5-Models-2030 (the corpus)](../entities/corpus-1729.md).
