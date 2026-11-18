---
name: SWMM Claim Frontier
file: swmm-claim-frontier.html
version: "1.0"
date: 2026-09-30
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/PRB5oUEFxb1W8wG6x9pu2a", repo: none named in the page}
engines:
  - {name: none in the page, note: "a register of claims, each verified on named builds (EPA SWMM 5.2.4, 5.2.2 wasm, develop, Slot Lab variants, legacy 5.3, OpenSWMM 6 alpha builds)"}
units: none (claims and coverage)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The published page carries no AI-use note; it is a Claude artifact on Robert Dickinson's account. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/PRB5oUEFxb1W8wG6x9pu2a, version 1790769393-3fe8 (index.html, 161,750 bytes, SHA-256 d586011eeebf577ab5e460a355c31ee5c50ee5139fd558c89fc3a1deff710924), every tab read in headless Chromium on 2026-11-17. Nothing was run to write this file."
---

# SWMM Claim Frontier: what holds, what failed, and what is still dark in the SWMM work

## In three points
- **What:** A register of the claims made in Bob's SWMM work, each placed on a tier (analytic or exhaustive, engine-verified, evidence, wall, conjecture, hunch) and tied to the engine builds it was verified on, with a graph, walls, corpus coverage and the loop that produces new claims.
- **So what:** 65 claims hold at a stated tier (12 analytic or exhaustive, 43 engine-verified, 10 evidence), 19 are walls each with a lesson, 11 are open, 20 are stale on the builds in service, and 99.9% of the corpus by nodes is uncharted.
- **Now what:** Retire a build to see which claims go hollow, and pick the next test from the dark part of the corpus. It is a register of claims, not a rerun of them.

This summary was written after the fact. The page ships no technical summary of its own. Its version is the page's own ("v1.0"); the date is the artifact's. The file name is the one Bob uses. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Frontier, Graph, Register, Walls, Coverage, Loop. A claim goes hollow when none of the builds it was verified on is still in service; unticking a build retires it. Builds listed include EPA SWMM 5.2.4 (gcc from the v5.2.4 tag; swmm-toolkit and pyswmm 2.1.0 carry the same engine, 52004) with 40 claims, EPA SWMM 5.2.2 wasm (@fileops/swmm-wasm-web 0.0.4) with 13, EPA develop with 2, 5.2.4 plus Slot Lab variants with 2, openswmm-legacy 5.3.0-beta.3 with 2, and OpenSWMM 6.0.0-alpha.2 handle and CLI builds with 14 and 5.

## Results the page reports

- 65 claims hold at a stated tier.
- Tiers: analytic or exhaustive 12, engine-verified 43, evidence 10, wall 19, conjecture 9, hunch 2.
- 20 claims are stale on the builds in service.
- 99.9% of the corpus by nodes is uncharted (mean of four coverage measures); for one build, 589 models covering 66.5% of corpus nodes show 0 of 589 on each of Q1 to Q4.

## What this does not show

- The claims are not rerun by the page; each carries the build it was verified on.

## How to reproduce

Open the page; untick builds on Frontier to retire them.

## Credits and licenses

No license is stated in the page.

## AI use

The published page carries no AI-use note. It is a Claude artifact on Robert Dickinson's account, built in a claude.ai session. The Netlify copy in this batch adds a one-line AI-use note at the foot of the page. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 1.0: first version.
