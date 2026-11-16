---
title: "S159: note, the same ICM Ruby query starts differently in GeoPlan and Exchange"
type: source
raw: raw/notes/icm-ruby-ui-vs-exchange.md
kind: note
author: Robert Dickinson
published: 2026-11-16
ingested: 2026-11-16
tags: [icm, ruby, exchange, note]
reviewed: no
---
**What it is.** A note on running one ICM Ruby query, a node count, in the ICM desktop interface and in ICM Exchange. Raw file: [raw/notes/icm-ruby-ui-vs-exchange.md](../../raw/notes/icm-ruby-ui-vs-exchange.md).

**How it was written.** One of seven notes Bob supplied on 16 November 2026 in `ICM-Ruby-SWMM-Markdown.zip`, copied into `raw/notes/` unchanged. It is on the note template, dated 2026-11-16, status seed. The note does not name its author; Bob says the ICM notes come from the GPT plugin for Autodesk [S166](S166-note-icm-notes-from-gpt-plugin.md), so it is AI-written text (that his statement covers this set of seven is Claude's reading, Q89). Its facts about ICM come from Autodesk's online help, linked in the note, and were not checked here against ICM or the help pages. Its procedure says it awaits a run in ICM: nothing in it has been run.

**Claims worth keeping** (as the note states them; AI-written, not checked against ICM)
- In the ICM desktop interface, `WSApplication.current_network` returns the network open in the focused GeoPlan.
- In Exchange, the script is given the database path and the network's scripting path, opens the database with `WSApplication.open(database_path, false)` (the `false` skips the database upgrade), and opens the network from `database.model_object(network_path)`.
- Autodesk documents ICM Exchange for Ultimate licenses.
- Exchange runs from PowerShell in the ICM install folder as `ICMExchange.exe <script> [-login] <arguments>`; the optional `-login` starts sign-in if needed.
- `WSApplication.ui?` tells the two apart. The node table is `hw_node` in an InfoWorks network and `sw_node` in an ICM SWMM network.
- The test: both scripts should return the same node count for the same saved base network.

**Feeds:** [ICM Ruby: UI scripts and Exchange scripts](../concepts/icm-ruby-ui-and-exchange.md), [InfoWorks ICM](../entities/infoworks-icm.md).
