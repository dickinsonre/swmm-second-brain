---
title: "CHM Reader 2026 (app)"
type: entity
updated: 2026-11-17
sources: [S205, S252]
tags: [apps, file-formats, documentation, tools]
reviewed: no
---
Bob's app CHM Reader 2026: a single-file app that opens Microsoft Compiled HTML Help (.chm) files without Windows, a plugin or an upload, shows their Contents, Index, full-text Search and raw Files, and exports the text as Markdown or plain text in parts sized to a context window, to get old SWMM, ICM or other help files into a form Claude reads. Version 1.0.0, 2026-11-02 [S252](../sources/S252-chm-reader-2026-summary.md). Netlify address: https://chm-reader-2026.netlify.app [S205](../sources/S205-note-netlify-addresses.md).

**A caution about its source.** The page ships no technical summary. [S252](../sources/S252-chm-reader-2026-summary.md) was written by Claude on 17 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q108).

**What the summary says** [S252](../sources/S252-chm-reader-2026-summary.md)
- Its own LZX decoder matched 7-Zip 16.02 and chmlib 0.40 byte for byte on all 7,038 entries of three test files: PyWin32.chm (6,880 files, 11.1 MB), fpc1.chm (130 files) and the bundled sample (28 files).
- The first run on fpc1.chm failed four entries because Free Pascal codes the short last frame as a full 32 KB block; the decoder now accepts the overrun.
- 15 deliberately damaged files from libmspack's test suite each read or stop with a plain error; none hangs.
- Topics are rendered with every script removed, in a sandboxed frame; the file is read in memory and not uploaded.

**What it does not show.** Stored (uncompressed) blocks passed a hand-built stream test only, and the x86 E8 translation is written but untested. Upload limits were read on 2 November 2026 and may change; token counts are estimates at four characters per token. [S252](../sources/S252-chm-reader-2026-summary.md)

**Noted at ingest.** 6,880 + 130 + 28 = 7,038 entries.

See [Apps summarized on 17 November 2026: ICM, data and the tools around models](../concepts/apps-from-pages-icm-and-data.md), [SWMM Documents Explorer (app)](swmm-documents-explorer.md), [Master SWMM PDF (app)](master-swmm-pdf.md).
