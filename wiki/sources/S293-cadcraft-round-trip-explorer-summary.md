---
title: "S293: CADCraft Round-Trip Explorer, summary written from the page (v1.1)"
type: source
raw: raw/apps/cadcraft-round-trip-explorer-v1.1.md
kind: app-md
author: Robert Dickinson
published: 2026-10-19
ingested: 2026-11-18
tags: [apps, cad, dxf, interoperability, testing]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app CADCraft Round-Trip Explorer, version 1.1: a test of CADCraft (github.com/storytold/cadcraft), an open-source AutoCAD clone: 112 third-party DXF files opened and re-saved, then judged entity by entity by ezdxf 1.4.4. Raw file: [raw/apps/cadcraft-round-trip-explorer-v1.1.md](../../raw/apps/cadcraft-round-trip-explorer-v1.1.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q111). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/2GBHe4SenVyAsrpBWTL4ZF, version 1792368979-d84e (index.html, 230,709 bytes, SHA-256 c5867526a871d9b0f15ef92167172a758a9b34eaddcbcb817e7600e3fc4b9aa6), its Summary, Verify and Doc tabs read in headless Chromium on 2026-11-18. The date above is the artifact's last publish. Nothing was run to write this file." The page says it was built with Claude in October 2026 under Bob's direction; Claude built CADCraft, assembled the corpus, wrote the judge and ran the sweep; a second AI agent, not a person, re-checked the defects.

**Claims worth keeping** (all copied from the file)
- CADCraft re-saved 108 of 112 files without a crash (17 deliberately broken); ezdxf read all 108 in strict mode with 0 audit errors; same input twice gives byte-identical output.
- Of 21,091 scored entities in 66 complete drawings: 99.19% identical, 0.44% rewritten with the same extents, 77 (0.37%) not reproduced.
- CC-1: a 2D entity in a tilted coordinate system is saved at the wrong place or plane with no warning; 70 of the 77 losses, in 8 files; in a georeferenced drawing polylines tilted about 2 degrees moved 2.4 to 4.9 million units.
- Null control: ezdxf's own read-and-save, judged the same way, gave 0 differences in 65 of 67 complete drawings.

**Limits it states.** No AutoCAD in the loop; no DWG; test files, not production drawings (largest 2.7 MB); open and save only; entity data, not pixels; one commit (e707ab4) on one machine.

**Checked at ingest.** 99.19 + 0.44 + 0.37 = 100.00% (our arithmetic). The `links:` line gives Netlify as https://cadcraft-round-trip-explorer.netlify.app.

**Feeds:** [CADCraft Round-Trip Explorer (app)](../entities/cadcraft-round-trip-explorer.md), [Apps summarized on 17 and 18 November 2026: AI workflows, tools and puzzles](../concepts/apps-from-pages-tools-and-puzzles.md), [Negative results](../concepts/negative-results.md).
