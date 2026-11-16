---
title: "S160: note, an ICM Ruby script needs a test in the embedded runtime"
type: source
raw: raw/notes/icm-ruby-version-compatibility.md
kind: note
author: not stated (supplied by Robert Dickinson)
published: 2026-11-16
ingested: 2026-11-16
tags: [icm, ruby, exchange, versions, note]
reviewed: no
---
**What it is.** A note on testing an ICM Ruby script in the Ruby that ICM embeds, after ICM changed Ruby versions. Raw file: [raw/notes/icm-ruby-version-compatibility.md](../../raw/notes/icm-ruby-version-compatibility.md).

**How it was written.** One of seven notes Bob supplied on 16 November 2026 in `ICM-Ruby-SWMM-Markdown.zip`, copied into `raw/notes/` unchanged. It is on the note template, dated 2026-11-16, status seed. The note does not say who wrote it. The set refers to Bob in the third person and addresses "you", so it was not typed by Bob in his own voice; whether an AI wrote it is not stated (Q89). Its facts about ICM come from Autodesk's online help, linked in the note, and were not checked here against ICM or the help pages. Its procedure says it awaits a run in ICM: nothing in it has been run.

**Claims worth keeping** (as the note states them; Autodesk's facts are reported, not checked)
- Autodesk documents Ruby 3.4.6 for embedded UI and Exchange scripting beginning with ICM 2027.0.
- Autodesk's upgrade article names Ruby 2.4.0 as the earlier runtime and describes a `LoadError` when a script requires a library that changed or is unavailable.
- The smoke test prints `WSApplication.version`, `RUBY_VERSION` and `WSApplication.ui?`, then tests the script's own `require` lines (the example: `require 'csv'`, expected to print the header `node_id,level`) before its model operations.
- Keep the ICM build and Ruby version next to each script's test result, in a table of script and commit, ICM build, Ruby version, UI or Exchange, network type, dependencies loaded, known object read.

**Feeds:** [ICM Ruby: UI scripts and Exchange scripts](../concepts/icm-ruby-ui-and-exchange.md), [InfoWorks ICM](../entities/infoworks-icm.md).
