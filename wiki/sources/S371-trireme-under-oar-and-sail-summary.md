---
title: "S371: Trireme Under Oar and Sail, summary written from the page (v1.2)"
type: source
raw: raw/apps/trireme-under-oar-and-sail-v1.2.md
kind: app-md
author: Robert Dickinson
published: 2026-10-22
ingested: 2026-11-18
tags: [apps, history, ships, not-water]
drafted_by: Claude (Anthropic), from the published page
reviewed: 2026-11-18
---
**What it is.** A technical summary of the app Trireme Under Oar and Sail, version 1.2: how 170 rowers drove a 120-foot Athenian warship. Raw file: [raw/apps/trireme-under-oar-and-sail-v1.2.md](../../raw/apps/trireme-under-oar-and-sail-v1.2.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/96DCWvyVWcJ4mygU4cqG6U, version 1792687488-14cb (index.html, 179,513 bytes, SHA-256 0e5ac697d73c6ce7be92659b56b4d8067d3052ae8061b71804aeaae09995b3e2), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file." Its AI-use section: "The page says: made with Claude, Anthropic's AI model, in October 2026 under the direction of Robert (Bob) Dickinson, who asked for the page, set its scope, obtained two external reviews and asked for their findings to be applied; responsibility for the content is his. Claude wrote all of the HTML, CSS and JavaScript, drew every figure as generated SVG, wrote and calibrated the speed model and the sailing solver, and drafted all of the text, including the evidence entries."

**Claims worth keeping** (all copied from the file)
- An interactive explainer of how a classical Greek trireme was rowed and sailed: 170 rowers in three tiers on a 120-ft hull, and what its two square sails could and could not do. Click the parts, move the sliders, call the stroke. The ship follows the Olympias reconstruction of 1987, the only full-size trireme built and rowed in modern times. Not a water-modeling app.
- The speed model is calibrated to two Olympias trial figures, each now quoted with its conditions: 5.4 kn at 30 strokes a minute was in a 20-knot tailwind; 8.3 kn is the adjusted average over the last 45 s of a 90-s sprint at 44 to 47 a minute with the steering oars lifted. The page reproduces both within 0.05 kn, and every number carries a tag in the Evidence tab: ancient testimony, reconstruction choice, trial observation, or teaching-model assumption.
- Calculation checks run on every load: the two calibration targets within 0.05 kn; the solved speed satisfies the power balance to one part in a million across 42 crew-and-rate combinations; speed rises with rate and with crew, and zero crew gives zero.
- The Evidence tab says for each claim whether it was checked and against what. The ancient evidence: the Athenian naval inventories, the Lenormant relief from the Acropolis, the ship-shed foundations.

**Limits it states.** As the page lists it: wind on hull and deck, waves and pitching, a fouled or waterlogged hull, crew fatigue over hours, current and tide (a following current makes a ship faster over the ground, a different quantity), and oar interference (folded into an efficiency). No ancient trireme hull survives.

**Checked at ingest.** Read in full; nothing was rerun at ingest. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [Trireme Under Oar and Sail (app)](../entities/trireme-under-oar-and-sail.md), [Apps summarized on 18 November 2026: calculators, toys and apps that are not about water](../concepts/apps-from-pages-calculators-toys-and-not-water.md).
