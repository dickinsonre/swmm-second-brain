---
title: "S03: SWMM Findings Register, format and candidate list"
type: source
raw: raw/notes/findings-register.md
kind: note
author: Robert Dickinson
published: 2026-10-09
ingested: 2026-11-14
tags: [findings, method]
reviewed: no
---
**What it is.** A proposal for a numbered, dated register of what was checked and what came back, kept as plain markdown in a git repository, with a table of twenty candidate entries. Raw file: [raw/notes/findings-register.md](../../raw/notes/findings-register.md). The date is the file's own date, 9 October 2026; the text carries none.

**How it was written.** By Claude in a chat with Bob, drawn from his conversation archive. It says each candidate needs Bob's confirmation before publishing.

**Claims worth keeping**
- One file per finding, `findings/F-0042.md`, with sequential IDs that never renumber, cited as `SWMM-F-0042`.
- Four rules: negative results are entries; no claim without a procedure; numbers, not adjectives; status can change but the entry does not.
- Twenty candidates, five of them negative results. Named ones include two interpolations of the same quantity (`output.c:590` against `routing.c:592`, USEPA issue 229), a `PUMP3` curve-order bug, a metric-units defect in the OpenSWMM 6.0.0-alpha.2 timeseries inflow path, and phantom `hw_storage` and `hw_outfall` tables in ICM.
- A keyword search for defect language in the archive returned 44 conversations with unrelated apps in the top ten, so findings have to be read out, not searched out.

**Feeds:** [The SWMM findings register](../concepts/findings-register.md), [Negative results](../concepts/negative-results.md).
