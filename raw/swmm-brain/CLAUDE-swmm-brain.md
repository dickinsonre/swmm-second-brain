# CLAUDE.md — Hydraulic-modeling app repo

Single-file, browser-based educational apps for SWMM5 / EPANET hydraulics.
Audience: water engineers and students who learn a concept faster from a slider
than from 50 pages of docs. Each app replaces static documentation with one
explorable, parameterized HTML/React file.

The full build contract, design system, onboarding templates, and physics
library live in the **swmm-vibe-coding-apps** skill. Read it before building;
don't re-derive it here. This file is only the four working principles, scoped
to this repo.

## 1. State assumptions; don't pick silently

Before writing code, state the modeling assumptions in play — units, equation
form, boundary conditions, defaults. If the request has more than one reasonable
reading, present the options and ask; don't choose one and run with it.
Clarifying questions come before the build, not after a wrong one.

## 2. Simplicity — beyond the contract, not below it

Write the minimum that solves the problem, then stop. No unrequested features,
no abstractions for single use, no refactoring or modularizing a deliberately
single-file app.

This does **not** mean stripping the build contract. These ship on every app and
are the floor, never "speculative":

- "How to Use" welcome modal on first load (dismissable, reopenable via `?`)
- step-by-step tour, or per-tab intro banners on multi-tab apps
- "Make a GIF" walkthrough button
- CSV export for tables; `.inp` export where a model is generated

"Simplest thing that works well" means minimum code *above* this line. If
onboarding or export is missing, the app is incomplete — not lean.

## 3. Surgical changes

On iteration, patch the named section only. Never regenerate the whole file to
change one part. Every changed line must trace to the request; don't improve
adjacent code, comments, or formatting nobody asked about.

## 4. Define success as a runnable check

An app is done when:

- the displayed equation matches the computation exactly
- presets produce expected values — verify the model functions in a quick node
  test before wiring the UI (the FableMeter pattern)
- no console errors; responsive at 375px; sliders have sane ranges/steps/units;
  chart axes labeled with units

Verify against these before reporting done. Open the reply with what you built
and any deviation from spec.
