---
title: "S243: ICM 2D Table Atlas, summary written from the page (v1.1)"
type: source
raw: raw/apps/icm-2d-table-atlas-v1.1.md
kind: app-md
author: Robert Dickinson
published: 2026-11-02
ingested: 2026-11-17
tags: [apps, icm, 2d, ruby, schema]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app ICM 2D Table Atlas, version 1.1: a reference to the 21 hw_2d network tables of InfoWorks ICM: every field from a Ruby schema dump set beside the types, US display units, defaults, limits and meanings in Autodesk's help, each row labelled by its evidence. It runs nothing. Raw file: [raw/apps/icm-2d-table-atlas-v1.1.md](../../raw/apps/icm-2d-table-atlas-v1.1.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 17 November 2026, at Bob's request, from the published Claude artifact, version 1793656582-99ad, reading its About and Doc tabs in a headless browser; nothing was run to write it. Bob has not read it (Q108). The page says it was built with Claude on 2 November 2026 under Bob's direction: Bob supplied the table dump, chose the scope and passed on an outside review of 1.0; Claude parsed the dump and wrote the app, its parser tests and three Ruby scripts; Claude research agents read Autodesk's help pages, release blogs and the ICM Ruby reference.

**Claims worth keeping** (all copied from the file)
- Nine lines of Ruby walk every ICM table and print every column; the run behind the atlas printed 7,300 lines: 91 tables, 6,823 fields and 385 blob sub-fields. Twenty-one tables start with hw_2d.
- A JavaScript and a separate Python parser agree on 91 tables, 6,823 fields and 385 blob sub-fields; writing the parsed schema back reproduces the 7,300-line paste line for line.
- Dump against help: eight field names only in the help, seven only in the dump, five of those seven coordinate arrays.
- Where the help page text lost empty cells, the cell was left blank and the row marked; this affects many rows on the linear structures and the infiltration surface.
- The three Ruby scripts were checked with ruby -c and run under Ruby 3.3.6 against a stub, not inside ICM.

**Limits it states.** The ICM version that produced the dump was not recorded. The ICM 2026 help pages could not be opened, so rows name the edition used (ICMLive 2026 or ICM 2027). Four open questions need a stamped dump from a live ICM install. Defaults and limits copied from help pages have not been checked by a person.

**Checked at ingest.** The atlas covers the same tables as [ICM network tables and result fields](../concepts/icm-tables-and-result-fields.md) and the ICM 2D pages, from a schema dump rather than from help pages alone. The `links:` line gives Netlify as "not yet deployed"; Netlify reported a finished deploy at https://icm-2d-table-atlas.netlify.app on 17 November 2026 [S205](S205-note-netlify-addresses.md).

**Feeds:** [ICM 2D Table Atlas (app)](../entities/icm-2d-table-atlas.md), [Apps summarized on 17 November 2026: ICM, data and the tools around models](../concepts/apps-from-pages-icm-and-data.md), [ICM network tables and result fields](../concepts/icm-tables-and-result-fields.md), [ICM 2D: boundaries and 1D-2D exchange](../concepts/icm-2d-boundaries-and-exchange.md), [ICM Ruby: UI scripts and Exchange scripts](../concepts/icm-ruby-ui-and-exchange.md), [InfoWorks ICM](../entities/infoworks-icm.md).
