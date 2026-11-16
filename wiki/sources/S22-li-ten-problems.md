---
title: "S22: Ten Problems with How SWMM Was Developed and Explained from 1970 to 2025 (LinkedIn, 2026)"
type: source
raw: raw/linkedin/2026-11-05-ten-problems-how-swmm-developed-explained-from-1970-2025-dickinson-hsnae.md
kind: linkedin-article
author: Robert Dickinson
published: 2026-11-05
ingested: 2026-11-14
tags: [swmm-history, documentation, swmm5, swmm6]
drafted_by: Claude (Anthropic), in a chat with Bob, who reviewed it line by line
reviewed: 2026-11-15
---
**What it is.** A ranked list of ten problems, each with a comment by Bob in bold. Raw file: [raw/linkedin/2026-11-05-ten-problems-how-swmm-developed-explained-from-1970-2025-dickinson-hsnae.md](../../raw/linkedin/2026-11-05-ten-problems-how-swmm-developed-explained-from-1970-2025-dickinson-hsnae.md).

**How it was written.** Its Use of AI note: Claude wrote the ranking and the text in a chat with Bob on 5 November 2026 and drew the figures; the release and manual dates were checked against EPA's update logs and the 2022 hydraulics addendum; Bob reviewed it line by line. The ranking is a judgment, not a measurement.

**Claims worth keeping**
- SWMM 5.0 build 001 shipped on 29 October 2004. The hydraulics reference manual followed in May 2017.
- EPA's update notes date 5.1.013 to 10 May 2018 and say it added the SLOT surcharge option; 5.2.0 is dated 1 February 2022.
- There were 42 builds of SWMM 5 from 5.0.001 to 5.2.4.
- Subcatchment width is a fitting parameter presented as a measurable length, with one width shared by the pervious and impervious subareas. Bob: this goes back to the street models of SWMM 1.
- Conduit C11 of EPA Example 1 in SWMM 5.2.4 peaks at 73.9 cfs in the Link Flow Summary and at 71.18 cfs in the .out file.
- Problems 1, 2, 8 and 9 are one problem: no written, testable statement of what the engine does and how to read what it prints.
- Bob: EPA has the OWA test models from the SWMM 4 to SWMM 5 conversion; SWMM6 on the HydroCouple GitHub has at least 2,000 models.

**Feeds:** [The missing specification](../concepts/the-missing-specification.md), [Subcatchment width](../concepts/subcatchment-width.md), [Reading SWMM output](../concepts/reading-swmm-output.md), [Dynamic wave routing](../concepts/dynamic-wave-routing.md), [Preissmann slot and surcharge](../concepts/preissmann-slot-and-surcharge.md), [Block architecture and interface files](../concepts/block-architecture.md), [SWMM version history, 1969 to 2026](../concepts/swmm-version-history.md), [Lewis A. (Lew) Rossman](../entities/lew-rossman.md), [OpenSWMM 6 and HydroCouple](../entities/openswmm-6-and-hydrocouple.md).
