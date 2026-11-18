---
title: "S373: Qubit Workbench, summary written from the page (v1.0)"
type: source
raw: raw/apps/qubit-workbench-v1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-09
ingested: 2026-11-18
tags: [apps, quantum, not-water]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app Qubit Workbench, version 1.0: exact quantum arithmetic on 1 to 12 qubits in the browser. Raw file: [raw/apps/qubit-workbench-v1.0.md](../../raw/apps/qubit-workbench-v1.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/EptQzoVw88vgJx3aN9naH5, version 1791517603-55ff (index.html, 134,122 bytes, SHA-256 39baffe13c3b8287a3b48deaa5412384c1a006e2ec6cabeb4699eb2e159292a7), its page read in headless Chromium and from its markup on 2026-11-18. Nothing was run to write this file." Its AI-use section: "The page carries no AI-use note. This summary was written by Claude (Anthropic) on 18 November 2026 from the published page."

**Claims worth keeping** (all copied from the file)
- A small quantum simulator in five tabs: one qubit on the Bloch sphere (drag θ and φ or press a gate, then measure along Z, X or Y), a circuit builder, Grover's search (step it and watch the answer rise, peak and fade), Shor's period finding (factor a small number), and Scale (what doubles, what halves and what collapses). Not a water-modeling app.
- Every number is computed in the browser by a state-vector simulator with complex amplitudes, gates as matrices and measurement by seeded sampling, so a fresh load repeats the same shots; for example 500 shots along Z of an equal superposition gave 262 zeros and 238 ones against an expected 250 ± 11. The "Try this" tip shows why phase matters: after H, dragging φ leaves P(0) and P(1) at 0.5, invisible to a Z measurement but not to X.
- The page carries a "Run the self-checks" button with results shown in place; it lists no other checks. The Fourier step in the Period tab is exact.

**Limits it states.** As the page lists it: noise, decoherence and error correction; the modular-exponentiation circuit (computed directly); the cost curves are scaling laws without constants; the table of estimates is quoted from a news summary.

**Checked at ingest.** Read in full; nothing was rerun at ingest. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [Qubit Workbench (app)](../entities/qubit-workbench.md), [Apps summarized on 18 November 2026: calculators, toys and apps that are not about water](../concepts/apps-from-pages-calculators-toys-and-not-water.md).
