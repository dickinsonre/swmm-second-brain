# Distill a fast surrogate from SWMM's own storms, don't train a CNN to replace it

**Status:** seed  
**Date:** 2026-06-29

The idea
--------

Instead of training a CNN on sparse field gauges, train it on SWMM itself. Run a Monte Carlo library of thousands of synthetic storms through a calibrated SWMM model, generate unlimited labeled rain-to-flow and rain-to-depth response pairs, and then distill that behavior into a fast surrogate model. This changes the framing from "CNN instead of SWMM" to "CNN distilled from SWMM," which is a much better fit for sparse real-world monitoring. The payoff is a lightweight emulator that can run in a browser, support rapid what-if testing, or accelerate calibration loops.

Proof / from scratch
--------------------

../experiments/synthetic-storm-surrogate/

Start with a small benchmark SWMM network, vary storm patterns, antecedent conditions, and selected calibrated parameters, and export response hydrographs as supervised training data. Validate the surrogate against peak, timing, shape, surcharge behavior, and depth envelopes before trying larger networks.

Links
-----

* • [#SWMM idea search](https://www.linkedin.com/search/results/all/?keywords=%23swmm&origin=HASH_TAG_FROM_FEED) — source hashtag context
* • [LinkedIn post](https://www.linkedin.com/posts/robertdickinson_ive-been-following-googles-amazing-flood-activity-7477379595151802368-XYjZ?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAEAvcwBVte4NjFU9EyFPNigxyghgnrHf9c) — related discussion
