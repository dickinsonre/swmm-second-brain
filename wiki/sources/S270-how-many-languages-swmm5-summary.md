---
title: "S270: How Many Languages Can the SWMM5 Engine Live In?, summary written from the page (v2026-10-28)"
type: source
raw: raw/apps/how-many-languages-swmm5-v2026-10-28.md
kind: app-md
author: Robert Dickinson
published: 2026-10-28
ingested: 2026-11-18
tags: [documents, swmm5, language-ports, glibc, wasm, byte-for-byte]
drafted_by: Claude (Anthropic), from the published document
reviewed: no
---
**What it is.** A technical summary of the document How Many Languages Can the SWMM5 Engine Live In?, version 2026-10-28: a Claude Docs document that measures which languages can host a port of EPA SWMM 5.2.4 matching a Linux build byte for byte, and why the math library and number formatter decide it. Raw file: [raw/apps/how-many-languages-swmm5-v2026-10-28.md](../../raw/apps/how-many-languages-swmm5-v2026-10-28.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q111). Its `written_from:` line: "the Claude Docs document https://claude.ai/artifact/72uvQomSDrpo3UokrFrCii, revision 17, its one tab exported as HTML on 2026-11-18 (28,768 bytes, SHA-256 9f481b90bc168b0067e41f1e41495d0e63f808495160710e77e527e3762cfa1f), and the data of its one chart read from the document; read in full. Nothing was run to write this file." The document says Claude (Anthropic, Opus 5.5) did the work on 2026-10-28, a Claude research sub-agent compiled the inventory of existing ports, and Bob had not reviewed the findings.

**Claims worth keeping** (all copied from the file)
- About 28 languages can run the engine by calling the compiled C or loading the wasm build; six can host a native port that matches a Linux build of EPA 5.2.4 without extra work: C++, Rust, Fortran, C#, Python and PHP.
- EPA 5.2.4 rebuilt with musl's math library in place of glibc's changed 55 of 440 corpus runs (12.5%) and moved Hydrology/SCANLON.inp node 09304006R0 from 20.56 to 23.21 ft; FMA contraction on against off changed 107 of 440; the null and repeat controls changed none; wasm32 against native musl changed 1 of 437.
- Of the 55 changed models, 36% have pumps, 27% control rules and 44% weirs or orifices; of the 385 unchanged, 11%, 7% and 13%.
- Last-bit differences from glibc: Java Math on 1% of calls, JavaScript 6%, Go 32%; for pow(r, 2/3) over radii from 0.000001 to 1,000 ft, JavaScript 9.8%, Java StrictMath 9.7%, Go 56%. Go's acos at 0.9999954 is 21,016 ULP from glibc.
- JavaScript toFixed rounds exact ties up, Java String.format and Ruby format round the shortest decimal string, and Free Pascal prints 0.00 for -0.001; Go, Rust, Python, PHP, C#, Fortran and musl matched C on all 320,000 values.
- Recommended next ports: Fortran and C#, then the existing wasm hosted from more languages.

**Limits it states.** Windows (the Microsoft C runtime) not measured; Julia, Swift, Kotlin/Native, Dart, D and Nim inferred without a toolchain; nothing timed; 440 models from six folders, 57 slow ones skipped; Go's FMA from the assembly listing only; existing ports described from their own pages.

**Checked at ingest.** 55 / 440 = 12.5% and 23.21 - 20.56 = 2.65 ft, as the document states (our arithmetic). The document predates Bob's own ports in Go, PHP and Mojo, dated 6 to 10 November ([S41](S41-swmm5-go-readme.md), [S47](S47-swmm5-php-readme.md), [S53](S53-swmm5-mojo-readme.md)); its "not found anywhere: an engine in Go" was true on 28 October and has since been overtaken. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [How Many Languages Can the SWMM5 Engine Live In? (document)](../entities/how-many-languages-swmm5.md), [Apps summarized on 17 and 18 November 2026: SWMM5, EPANET and the checks on them](../concepts/apps-from-pages-swmm5-epanet-checks.md), [Matching glibc math in a translation](../concepts/glibc-math-in-translation.md), [Where languages part from C](../concepts/where-languages-part-from-c.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md), [SWMM5 language translations (swmm5-*)](../entities/swmm5-language-ports.md), [Byte-for-byte gate](../concepts/byte-for-byte-gate.md).
