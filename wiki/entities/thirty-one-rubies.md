---
title: "Thirty-One Rubies (app)"
type: entity
updated: 2026-11-17
sources: [S205, S244, S250]
tags: [apps, icm, ruby, wasm, testing]
reviewed: no
---
Bob's app Thirty-One Rubies: one file that runs 44 ICM Ruby scripts from 31 of Bob's apps on CRuby 3.4.1 compiled to WebAssembly, against a strict stand-in for the ICM Ruby API built from Autodesk's public table, field and method lists, on a made-up sewer network. Version 1.0, 2026-11-03 [S250](../sources/S250-thirty-one-rubies-summary.md). Netlify address: https://thirty-one-rubies.netlify.app [S205](../sources/S205-note-netlify-addresses.md).

**A caution about its source.** The page ships no technical summary. [S250](../sources/S250-thirty-one-rubies-summary.md) was written by Claude on 17 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q108).

**What the summary says** [S250](../sources/S250-thirty-one-rubies-summary.md)
- The stand-in's rules come from Autodesk's Open-Source-Support repository (MIT): 136 tables and 2,644 fields in hw_parameters.rb and sw_parameters.rb, and 336 methods in ruby_icm_help.md.
- All 43 compared scripts gave character-for-character identical output on native Ruby 3.3.6 and browser Ruby 3.4.1; the Set timing script was left out because its output is a stopwatch. The comparison first showed 37 of 43, mostly because JavaScript rewrote 500.0 as 500.
- A volume check caught an RTK script reading 24.0000 ac-in where 6.0000 was right, four times high, because a Delta-t was missing from the convolution.
- Hand check: Harmon at 1 MGD and 100 gpcd gives 2.955.
- The stand-in's refusals were tested: a wrong field, a wrong table, map on a custom collection, an undocumented method, a real method it does not implement, and a change without .write.

**What it does not show.** No script has run in real ICM: a pass means the Ruby runs and the names are on Autodesk's lists. Ruby 2.4.0, for ICM before 2027.0, was not tested. [S250](../sources/S250-thirty-one-rubies-summary.md)

**Noted at ingest.** The stand-in counts 336 methods in ruby_icm_help.md; [ICM Exchange 2026 (app)](icm-exchange-2026.md) counts 335 in the same file at commit c580601 [S244](../sources/S244-icm-exchange-2026-summary.md). Neither summary says which revision the other read, or what makes the difference of one (Q109).

See [Apps summarized on 17 November 2026: ICM, data and the tools around models](../concepts/apps-from-pages-icm-and-data.md), [ICM Ruby: UI scripts and Exchange scripts](../concepts/icm-ruby-ui-and-exchange.md), [ICM Exchange 2026 (app)](icm-exchange-2026.md), [RDII unit hydrographs (RTK)](../concepts/rdii-unit-hydrographs.md), [InfoWorks ICM Ruby Script Runner (app)](icm-ruby-script-runner.md).
