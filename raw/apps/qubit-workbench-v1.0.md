---
name: Qubit Workbench
file: qubit-workbench.html
version: "1.0"
date: 2026-10-09
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/EptQzoVw88vgJx3aN9naH5", repo: none}
engines: none (a state-vector simulator for 1 to 12 qubits written for the page)
units: not applicable
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page carries no AI-use note."
written_from: "the published Claude artifact https://claude.ai/artifact/EptQzoVw88vgJx3aN9naH5, version 1791517603-55ff (index.html, 134,122 bytes, SHA-256 39baffe13c3b8287a3b48deaa5412384c1a006e2ec6cabeb4699eb2e159292a7), its page read in headless Chromium and from its markup on 2026-11-18. Nothing was run to write this file."
---

# Qubit Workbench: exact quantum arithmetic on 1 to 12 qubits in the browser

## In three points
- **What:** A small quantum simulator in five tabs: one qubit on the Bloch sphere (drag θ and φ or press a gate, then measure along Z, X or Y), a circuit builder, Grover's search (step it and watch the answer rise, peak and fade), Shor's period finding (factor a small number), and Scale (what doubles, what halves and what collapses). Not a water-modeling app.
- **So what:** Every number is computed in the browser by a state-vector simulator with complex amplitudes, gates as matrices and measurement by seeded sampling, so a fresh load repeats the same shots; for example 500 shots along Z of an equal superposition gave 262 zeros and 238 ones against an expected 250 ± 11. The "Try this" tip shows why phase matters: after H, dragging φ leaves P(0) and P(1) at 0.5, invisible to a Z measurement but not to X.
- **Now what:** Use it to build intuition for small quantum circuits. It leaves out noise, decoherence and error correction, the hard part of building the machine; the Period tab computes a^x mod N directly instead of running the modular exponentiation gate by gate; and the table of estimates on the Scale tab is quoted from a news summary, not re-derived.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("Qubit Workbench v1.0, 9 October 2026"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: One qubit, Circuit, Search (Grover), Period (Shor), Scale. Two-qubit gates take two taps in one column. Each tab opens with a one-line tip; Export CSV saves the numbers on the tab in view; Make a GIF records a short captioned demo; a self-check panel runs on demand.

## Checks (as stated on the page)

The page carries a "Run the self-checks" button with results shown in place; it lists no other checks. The Fourier step in the Period tab is exact.

## What this does not show

As the page lists it: noise, decoherence and error correction; the modular-exponentiation circuit (computed directly); the cost curves are scaling laws without constants; the table of estimates is quoted from a news summary.

## Credits and licenses

Grover's and Shor's algorithms as published. No license is stated for the page.

## AI use

The page carries no AI-use note. This summary was written by Claude (Anthropic) on 18 November 2026 from the published page.

## Changes

- 1.0 (2026-10-09): first version (the version read).
