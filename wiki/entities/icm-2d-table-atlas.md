---
title: "ICM 2D Table Atlas (app)"
type: entity
updated: 2026-11-17
sources: [S205, S243]
tags: [apps, icm, 2d, ruby, schema]
reviewed: no
---
Bob's app ICM 2D Table Atlas: a reference to the 21 hw_2d network tables of InfoWorks ICM: every field from a Ruby schema dump set beside the types, US display units, defaults, limits and meanings in Autodesk's help, each row labelled by its evidence. It runs nothing. Version 1.1, 2026-11-02 [S243](../sources/S243-icm-2d-table-atlas-summary.md). Netlify address: https://icm-2d-table-atlas.netlify.app [S205](../sources/S205-note-netlify-addresses.md).

**A caution about its source.** The page ships no technical summary. [S243](../sources/S243-icm-2d-table-atlas-summary.md) was written by Claude on 17 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q108).

**What the summary says** [S243](../sources/S243-icm-2d-table-atlas-summary.md)
- Nine lines of Ruby walk every ICM table and print every column; the run behind the atlas printed 7,300 lines: 91 tables, 6,823 fields and 385 blob sub-fields. Twenty-one tables start with hw_2d.
- A JavaScript and a separate Python parser agree on 91 tables, 6,823 fields and 385 blob sub-fields; writing the parsed schema back reproduces the 7,300-line paste line for line.
- Dump against help: eight field names only in the help, seven only in the dump, five of those seven coordinate arrays.
- Where the help page text lost empty cells, the cell was left blank and the row marked; this affects many rows on the linear structures and the infiltration surface.
- The three Ruby scripts were checked with ruby -c and run under Ruby 3.3.6 against a stub, not inside ICM.

**What it does not show.** The ICM version that produced the dump was not recorded. The ICM 2026 help pages could not be opened, so rows name the edition used (ICMLive 2026 or ICM 2027). Four open questions need a stamped dump from a live ICM install. Defaults and limits copied from help pages have not been checked by a person. [S243](../sources/S243-icm-2d-table-atlas-summary.md)

**Noted at ingest.** The atlas covers the same tables as [ICM network tables and result fields](../concepts/icm-tables-and-result-fields.md) and the ICM 2D pages, from a schema dump rather than from help pages alone.

See [Apps summarized on 17 November 2026: ICM, data and the tools around models](../concepts/apps-from-pages-icm-and-data.md), [ICM network tables and result fields](../concepts/icm-tables-and-result-fields.md), [ICM 2D: boundaries and 1D-2D exchange](../concepts/icm-2d-boundaries-and-exchange.md), [ICM Ruby: UI scripts and Exchange scripts](../concepts/icm-ruby-ui-and-exchange.md), [InfoWorks ICM](infoworks-icm.md).
