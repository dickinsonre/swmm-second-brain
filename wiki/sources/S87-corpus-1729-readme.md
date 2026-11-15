---
title: "S87: 1729-SWMM5-Models-2030, repository README (inventory of 23 October 2026)"
type: source
raw: raw/apps/1729-SWMM5-Models-2030 README (1).md
kind: readme
author: Robert Dickinson
published: 2026-10-23
ingested: 2026-11-15
tags: [corpus, swmm5, swmm6, test-models, verification]
reviewed: no
---
**What it is.** The README of Bob's model corpus, SWMMBobSWMM6/1729-SWMM5-Models-2030. It is a repository README, not an app summary, though it sits in `raw/apps/`. Raw file: [raw/apps/1729-SWMM5-Models-2030 README (1).md](../../raw/apps/1729-SWMM5-Models-2030%20README%20%281%29.md). Bob uploaded it on 14 November 2026.

**How it was written.** The README does not say who or what wrote it. It says the two newest folders each carry an AI-use note of their own. The publication date here is the date of its inventory.

**Claims worth keeping**
- 4,540 EPA SWMM 5 `.inp` files; maintained by Bob.
- Inventory of the maintainer's working copy, 23 October 2026: 22,208 files, 15,977 MB, in 44 top-level folders and the root. 4,099 `.rpt`, 3,461 `.out` and 4,029 `.md` files.
- Largest folders by `.inp` count: XPSWMM 1,859 (conversions made with the XPSWMM Card Reader, with 1,859 `.xp` and 111 `.xpx` files); SWMM5_NCIMM 589; OpenSWMM_Code_Review_2026 351; OpenSWMM_Engine_Test_Decks 335; EPA 154; OWA_USER 151; Hydrology 149; Hydraulics 140.
- Binary `.out` results are 10,464.6 MB, 65.5 % of the collection's size.
- Added 23 October 2026: `EPA_PYSWMM_Additions`, 40 previously missing models matched by file content, not file name.
- Added the same day, after measuring the corpus against the 200 findings of the HydroCouple swmm-code-review: the review's 351 reproducer decks, and the 335 input files of the OpenSWMM engine repository not already present. Before these, 53 of the review's input-reachable findings had no corpus model and 25 had only one to three.
- 11 of the reproducer decks crash or hang EPA SWMM 5.2.4. 250 of the engine test decks need OpenSWMM 6.
- `january5_2003_examples` holds 276 `.dat` files and no `.inp`.
- The repository-level dedication is The Unlicense. Named or contributed folders (Greenville, Matt_Anderson_Teams, Sam, logan, Special) "require provenance checks before redistribution". Both OpenSWMM folders are Apache-2.0 material from HydroCouple.
- Per-model markdown summaries are auto-generated.

**Limits it states.** Equal counts of `.inp`, `.rpt`, `.out` and `.md` in a folder do not prove each input has its results. `.inp` totals are file counts, "not counts of distinct networks or passing tests". Inclusion is not a guarantee of successful execution, calibration or suitability for design. The inventory describes a local working copy, not the GitHub download.

**Checked at ingest.** 351 + 335 = 686, the count of inputs it gives for the two new folders. The eight largest folders listed above sum to 3,728 of the 4,540 (our arithmetic). 10,464.6 / 15,977 = 65.5 %. Other sources name a second repository, SWMMEnablement/1729-SWMM5-Models, as the corpus they ran (Q51).

**Feeds:** [1729-SWMM5-Models-2030 (the corpus)](../entities/corpus-1729.md), [What the gate cannot see](../concepts/gate-blind-spots.md), [OpenSWMM 6 and HydroCouple](../entities/openswmm-6-and-hydrocouple.md).
