---
name: Trireme Under Oar and Sail
file: trireme-under-oar-and-sail.html
version: "1.2"
date: 2026-10-22
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/96DCWvyVWcJ4mygU4cqG6U", repo: none}
engines: none (a rowing speed model and a sailing solver written for the page, calibrated to the Olympias trials)
units: US customary with metric in parentheses (ft, knots)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was made with Claude in October 2026 under Robert Dickinson's direction, and that two external reviews he obtained were applied. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/96DCWvyVWcJ4mygU4cqG6U, version 1792687488-14cb (index.html, 179,513 bytes, SHA-256 0e5ac697d73c6ce7be92659b56b4d8067d3052ae8061b71804aeaae09995b3e2), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# Trireme Under Oar and Sail: how 170 rowers drove a 120-foot Athenian warship

## In three points
- **What:** An interactive explainer of how a classical Greek trireme was rowed and sailed: 170 rowers in three tiers on a 120-ft hull, and what its two square sails could and could not do. Click the parts, move the sliders, call the stroke. The ship follows the Olympias reconstruction of 1987, the only full-size trireme built and rowed in modern times. Not a water-modeling app.
- **So what:** The speed model is calibrated to two Olympias trial figures, each now quoted with its conditions: 5.4 kn at 30 strokes a minute was in a 20-knot tailwind; 8.3 kn is the adjusted average over the last 45 s of a 90-s sprint at 44 to 47 a minute with the steering oars lifted. The page reproduces both within 0.05 kn, and every number carries a tag in the Evidence tab: ancient testimony, reconstruction choice, trial observation, or teaching-model assumption.
- **Now what:** Use it to see what is known and what is reconstructed about ancient oared ships. The model's world is still water, flat calm, a fresh crew and one hull shape; wind on the hull, waves, fouling, fatigue and current are left out, and most of them would make a real ship slower.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("v1.2 · 2026-10-22"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Motion, Anatomy, Three Tiers, Rowing, The Stroke, Sailing, Crew, Evidence, About, Doc. Version 1.2, after a second review, reformulates sailing: the limit applies to the apparent wind (65°, the measured figure) and the ship's speed, apparent wind, leeway and ground to windward are solved together, so near the limit the model makes a little ground to windward and the prose says so. The Mytilene verdicts split into arithmetic, a comparison with a named trial figure, and a statement that feasibility is not estimated. The enlarged-figure view is a native dialog; tab changes update the address hash.

## Checks (as stated on the page)

- Calculation checks run on every load: the two calibration targets within 0.05 kn; the solved speed satisfies the power balance to one part in a million across 42 crew-and-rate combinations; speed rises with rate and with crew, and zero crew gives zero.
- The Evidence tab says for each claim whether it was checked and against what. The ancient evidence: the Athenian naval inventories, the Lenormant relief from the Acropolis, the ship-shed foundations.

## What this does not show

As the page lists it: wind on hull and deck, waves and pitching, a fouled or waterlogged hull, crew fatigue over hours, current and tide (a following current makes a ship faster over the ground, a different quantity), and oar interference (folded into an efficiency). No ancient trireme hull survives.

## Credits and licenses

The Olympias reconstruction (1987) and its sea trials; the Athenian naval inventories; the Lenormant relief. No license is stated for the page.

## AI use

The page says: made with Claude, Anthropic's AI model, in October 2026 under the direction of Robert (Bob) Dickinson, who asked for the page, set its scope, obtained two external reviews and asked for their findings to be applied; responsibility for the content is his. Claude wrote all of the HTML, CSS and JavaScript, drew every figure as generated SVG, wrote and calibrated the speed model and the sailing solver, and drafted all of the text, including the evidence entries. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 1.2 (2026-10-22): sailing reformulated on the apparent wind, after the second review (the version read).
- 1.1: changes after the first review. 1.0: first version.
