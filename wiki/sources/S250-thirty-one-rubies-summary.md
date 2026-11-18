---
title: "S250: Thirty-One Rubies, summary written from the page (v1.0)"
type: source
raw: raw/apps/thirty-one-rubies-v1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-11-03
ingested: 2026-11-17
tags: [apps, icm, ruby, wasm, testing]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app Thirty-One Rubies, version 1.0: one file that runs 44 ICM Ruby scripts from 31 of Bob's apps on CRuby 3.4.1 compiled to WebAssembly, against a strict stand-in for the ICM Ruby API built from Autodesk's public table, field and method lists, on a made-up sewer network. Raw file: [raw/apps/thirty-one-rubies-v1.0.md](../../raw/apps/thirty-one-rubies-v1.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 17 November 2026, at Bob's request, from the published Claude artifact, version 1793713065-d89a, reading its About and Doc tabs in a headless browser; nothing was run to write it. Bob has not read it (Q108). The page says the app was built with Claude in a session in November 2026 under Bob's direction; Bob chose the 31 apps and asked for the combination. Claude read the past chats for the 31 apps with three delegated readers and wrote the stand-in, the checker and all 44 scripts; many are new or heavily rewritten, not copies of the originals. Bob has not yet reviewed the 46 corrections.

**Claims worth keeping** (all copied from the file)
- The stand-in's rules come from Autodesk's Open-Source-Support repository (MIT): 136 tables and 2,644 fields in hw_parameters.rb and sw_parameters.rb, and 336 methods in ruby_icm_help.md.
- All 43 compared scripts gave character-for-character identical output on native Ruby 3.3.6 and browser Ruby 3.4.1; the Set timing script was left out because its output is a stopwatch. The comparison first showed 37 of 43, mostly because JavaScript rewrote 500.0 as 500.
- A volume check caught an RTK script reading 24.0000 ac-in where 6.0000 was right, four times high, because a Delta-t was missing from the convolution.
- Hand check: Harmon at 1 MGD and 100 gpcd gives 2.955.
- The stand-in's refusals were tested: a wrong field, a wrong table, map on a custom collection, an undocumented method, a real method it does not implement, and a change without .write.

**Limits it states.** No script has run in real ICM: a pass means the Ruby runs and the names are on Autodesk's lists. Ruby 2.4.0, for ICM before 2027.0, was not tested.

**Checked at ingest.** The stand-in counts 336 methods in ruby_icm_help.md; [ICM Exchange 2026 (app)](../entities/icm-exchange-2026.md) counts 335 in the same file at commit c580601 [S244](S244-icm-exchange-2026-summary.md). Neither summary says which revision the other read, or what makes the difference of one (Q109). The `links:` line gives Netlify as "not yet deployed"; Netlify reported a finished deploy at https://thirty-one-rubies.netlify.app on 17 November 2026 [S205](S205-note-netlify-addresses.md).

**Feeds:** [Thirty-One Rubies (app)](../entities/thirty-one-rubies.md), [Apps summarized on 17 November 2026: ICM, data and the tools around models](../concepts/apps-from-pages-icm-and-data.md), [ICM Ruby: UI scripts and Exchange scripts](../concepts/icm-ruby-ui-and-exchange.md), [ICM Exchange 2026 (app)](../entities/icm-exchange-2026.md), [RDII unit hydrographs (RTK)](../concepts/rdii-unit-hydrographs.md), [InfoWorks ICM Ruby Script Runner (app)](../entities/icm-ruby-script-runner.md).
