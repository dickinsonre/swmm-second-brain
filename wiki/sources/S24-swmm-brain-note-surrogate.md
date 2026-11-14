---
title: "S24: Note, distill a fast surrogate from SWMM's own storms"
type: source
raw: raw/swmm-brain/notes/synthetic-storm-surrogate.md
kind: note
author: Robert Dickinson
published: 2026-06-29
ingested: 2026-11-14
tags: [surrogates, machine-learning, ideas]
reviewed: no
---
**What it is.** The only note in the old swmm-brain repository, written to its one-idea-per-file template. Status in the note: seed. Raw file: [raw/swmm-brain/notes/synthetic-storm-surrogate.md](../../raw/swmm-brain/notes/synthetic-storm-surrogate.md).

**How it was written.** Not stated. The template asks for the author's own words.

**Claims worth keeping**
- The idea: do not train a neural network on sparse field gauges; train it on SWMM. Run thousands of synthetic storms through a calibrated SWMM model and distill the rain-to-flow and rain-to-depth pairs into a fast surrogate.
- The framing changes from "CNN instead of SWMM" to "CNN distilled from SWMM".
- Intended payoff: an emulator light enough for a browser, for what-if testing and for speeding calibration loops.
- Plan: start with a small benchmark network; vary storm patterns, antecedent conditions and selected calibrated parameters; validate on peak, timing, shape, surcharge behavior and depth envelopes before trying larger networks.
- It points to `../experiments/synthetic-storm-surrogate/`, which is not in the repository, and to a LinkedIn post of Bob's on Google's flood work, going by its address.

**Feeds:** [A surrogate distilled from SWMM](../concepts/surrogate-distilled-from-swmm.md), [swmm-brain (the old brain repository)](../entities/swmm-brain-repo.md).
