---
title: "S246: ICM Sediment Field Guide, summary written from the page (v1.1)"
type: source
raw: raw/apps/icm-sediment-field-guide-v1.1.md
kind: app-md
author: Robert Dickinson
published: 2026-11-02
ingested: 2026-11-17
tags: [apps, icm, sediment, 2d, teaching]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app ICM Sediment Field Guide, version 1.1: Bob's earlier outline for a LinkedIn article on 1D and 2D sediment modeling in InfoWorks ICM, brought to November 2026 and written in full, with two labs that run the textbook formulas the article names. ICM's solver is not run. Raw file: [raw/apps/icm-sediment-field-guide-v1.1.md](../../raw/apps/icm-sediment-field-guide-v1.1.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 17 November 2026, at Bob's request, from the published Claude artifact, version 1793655822-9832, reading its About and Doc tabs in a headless browser; nothing was run to write it. Bob has not read it (Q108). The page says it was built with Claude in a session on 2 November 2026 under Bob's direction: Bob asked for the earlier outline to be updated to 2026 and delivered as an app with a Doc tab and a Word file; Claude searched the ICM 2027 help, Autodesk Learn and the release notes and wrote the article, formulas and tests; for 1.1 Claude checked an outside review's corrections against the ICM 2027 help and applied them.

**Claims worth keeping** (all copied from the file)
- A flat sediment bed in a circular pipe, with the same n and hydraulic gradient, takes 2.8, 7.7, 20.4 and 64.0 percent of full-flow capacity at 5, 10, 20 and 50 percent depth; a 24 in pipe half full drops from the 16 cfs on the drawings to 5.76 cfs.
- An independent review of version 1.0 (graded 78/100), supplied by Bob on 2 November 2026, reproduced the capacity curve to four decimals.
- Kinematic viscosity follows the water temperature through the Vogel equation, scaled so that 68 F gives 1.0 x 10^-6 m2/s.
- Checks are sorted by kind of evidence: branch continuity, hand calculations, independent references and outside reproduction; the page notes that agreement among outputs sharing one implementation does not verify the implementation.
- Version 1.1 separated total load from bed load, corrected transport units to ft2/s and marked undocumented ICM defaults.

**Limits it states.** Every number is a textbook formula at one instant, not ICM's solver. The capacity curve assumes the same Manning n and hydraulic gradient clean and sedimented; a real bed is rougher.

**Checked at ingest.** 16 x (1 - 0.640) = 5.76 cfs. The `links:` line gives Netlify as "not yet deployed"; Netlify reported a finished deploy at https://icm-sediment-field-guide.netlify.app on 17 November 2026 [S205](S205-note-netlify-addresses.md).

**Feeds:** [ICM Sediment Field Guide (app)](../entities/icm-sediment-field-guide.md), [Apps summarized on 17 November 2026: ICM, data and the tools around models](../concepts/apps-from-pages-icm-and-data.md), [InfoWorks ICM](../entities/infoworks-icm.md), [Conduit cross-sections: the built-in shapes](../concepts/conduit-cross-sections.md), [ICM 2D: terrain, mesh and subgrid sampling](../concepts/icm-2d-mesh-and-subgrid.md).
