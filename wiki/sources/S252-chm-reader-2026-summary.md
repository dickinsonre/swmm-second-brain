---
title: "S252: CHM Reader 2026, summary written from the page (v1.0.0)"
type: source
raw: raw/apps/chm-reader-2026-v1.0.0.md
kind: app-md
author: Robert Dickinson
published: 2026-11-02
ingested: 2026-11-17
tags: [apps, file-formats, documentation, tools]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app CHM Reader 2026, version 1.0.0: a single-file app that opens Microsoft Compiled HTML Help (.chm) files without Windows, a plugin or an upload, shows their Contents, Index, full-text Search and raw Files, and exports the text as Markdown or plain text in parts sized to a context window, to get old SWMM, ICM or other help files into a form Claude reads. Raw file: [raw/apps/chm-reader-2026-v1.0.0.md](../../raw/apps/chm-reader-2026-v1.0.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 17 November 2026, at Bob's request, from the published Claude artifact, version 1793635652-9de8, reading its About and Doc tabs in a headless browser; nothing was run to write it. Bob has not read it (Q108). The page says it was built with Claude (Claude Opus 5.5) in a session on 2 November 2026 at Bob's request, to bring two earlier answers up to 2026 (that Claude could not read a CHM file, and how big a file Claude can take). Claude wrote the container reader and LZX decoder from the published format and libmspack's behaviour, the viewer and the sample help file, and looked up the upload limits on the Claude Help Center.

**Claims worth keeping** (all copied from the file)
- Its own LZX decoder matched 7-Zip 16.02 and chmlib 0.40 byte for byte on all 7,038 entries of three test files: PyWin32.chm (6,880 files, 11.1 MB), fpc1.chm (130 files) and the bundled sample (28 files).
- The first run on fpc1.chm failed four entries because Free Pascal codes the short last frame as a full 32 KB block; the decoder now accepts the overrun.
- 15 deliberately damaged files from libmspack's test suite each read or stop with a plain error; none hangs.
- Topics are rendered with every script removed, in a sandboxed frame; the file is read in memory and not uploaded.

**Limits it states.** Stored (uncompressed) blocks passed a hand-built stream test only, and the x86 E8 translation is written but untested. Upload limits were read on 2 November 2026 and may change; token counts are estimates at four characters per token.

**Checked at ingest.** 6,880 + 130 + 28 = 7,038 entries. The `links:` line gives Netlify as "not yet deployed"; Netlify reported a finished deploy at https://chm-reader-2026.netlify.app on 17 November 2026 [S205](S205-note-netlify-addresses.md).

**Feeds:** [CHM Reader 2026 (app)](../entities/chm-reader-2026.md), [Apps summarized on 17 November 2026: ICM, data and the tools around models](../concepts/apps-from-pages-icm-and-data.md), [SWMM Documents Explorer (app)](../entities/swmm-documents-explorer.md), [Master SWMM PDF (app)](../entities/master-swmm-pdf.md).
