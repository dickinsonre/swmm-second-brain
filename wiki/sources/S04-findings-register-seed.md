---
title: "S04: SWMM Findings Register, seed entries F-0001 to F-0014"
type: source
raw: raw/notes/findings-register-seed.md
kind: note
author: Robert Dickinson
published: 2026-10-09
ingested: 2026-11-14
tags: [findings, swmm5, swmm6, verification]
drafted_by: Claude (Anthropic), from Bob's conversation archive
reviewed: 2026-11-15
---
**What it is.** Fourteen register entries extracted from Bob's conversation archive for June to August 2026. Raw file: [raw/notes/findings-register-seed.md](../../raw/notes/findings-register-seed.md). Dated by the file, 9 October 2026.

**How it was written.** By Claude from the archive. Every entry is marked `unconfirmed` until Bob reruns it, except where the entry itself says `fixed`, `corrected` or `disproven`. The source uses metric units in F-0007.

**Claims worth keeping**
- F-0001: on a pumped 1 ft pipe with a fixed 8 ft tailwater in EPA SWMM 5.2.4, EXTRAN settles at 5.0586 cfs and SLOT at 5.2475 cfs, 3.7 % higher. A steady-state difference, not a transient.
- F-0002: in the OWA corpus, 20 files fail ERROR 205 on underscore shape spellings; fixing those exposes ten ERROR 211 failures, and fixing those exposes three ERROR 209 failures.
- F-0003: a reversed sign in the Audusse well-balancing correction destroys still water while mass conservation stays perfect. After the fix, 39 of 39 analytic cases pass.
- F-0005: EPA SWMM 5.2.4 stops with ERROR 205 on SWMM6 `[OPTIONS]` keywords; legacy 5.3 silently ignores them.
- F-0007: conduit lengthening adds storage that continuity does not flag.
- F-0009 to F-0013: five negative results.

**Feeds:** [The SWMM findings register](../concepts/findings-register.md), [Negative results](../concepts/negative-results.md), [Preissmann slot and surcharge](../concepts/preissmann-slot-and-surcharge.md), [Conduit lengthening](../concepts/conduit-lengthening.md), [Continuity is not validation](../concepts/continuity-is-not-validation.md), [OpenSWMM 6 and HydroCouple](../entities/openswmm-6-and-hydrocouple.md).
