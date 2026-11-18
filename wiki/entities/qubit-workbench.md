---
title: "Qubit Workbench (app)"
type: entity
updated: 2026-11-18
sources: [S373]
tags: [apps, quantum, not-water]
reviewed: no
---
Bob's app Qubit Workbench: exact quantum arithmetic on 1 to 12 qubits in the browser. Version 1.0, 2026-10-09 [S373](../sources/S373-qubit-workbench-summary.md). Its `links:` line names no live Netlify address [S373](../sources/S373-qubit-workbench-summary.md).

**A caution about its source.** The page ships no technical summary. [S373](../sources/S373-qubit-workbench-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q116).

**What the summary says** [S373](../sources/S373-qubit-workbench-summary.md)
- A small quantum simulator in five tabs: one qubit on the Bloch sphere (drag θ and φ or press a gate, then measure along Z, X or Y), a circuit builder, Grover's search (step it and watch the answer rise, peak and fade), Shor's period finding (factor a small number), and Scale (what doubles, what halves and what collapses). Not a water-modeling app.
- Every number is computed in the browser by a state-vector simulator with complex amplitudes, gates as matrices and measurement by seeded sampling, so a fresh load repeats the same shots; for example 500 shots along Z of an equal superposition gave 262 zeros and 238 ones against an expected 250 ± 11. The "Try this" tip shows why phase matters: after H, dragging φ leaves P(0) and P(1) at 0.5, invisible to a Z measurement but not to X.
- The page carries a "Run the self-checks" button with results shown in place; it lists no other checks. The Fourier step in the Period tab is exact.

**How to use it, as the summary puts it.** Use it to build intuition for small quantum circuits. It leaves out noise, decoherence and error correction, the hard part of building the machine; the Period tab computes a^x mod N directly instead of running the modular exponentiation gate by gate; and the table of estimates on the Scale tab is quoted from a news summary, not re-derived. [S373](../sources/S373-qubit-workbench-summary.md)

**What it does not show.** As the page lists it: noise, decoherence and error correction; the modular-exponentiation circuit (computed directly); the cost curves are scaling laws without constants; the table of estimates is quoted from a news summary. [S373](../sources/S373-qubit-workbench-summary.md)

See [Apps summarized on 18 November 2026: calculators, toys and apps that are not about water](../concepts/apps-from-pages-calculators-toys-and-not-water.md).
