---
title: SWMM5 Code House (app)
type: entity
updated: 2026-11-14
sources: [S68, S71, S72]
tags: [apps, swmm5, source-code, wasm, verification]
reviewed: no
---
Bob's walkable 3D map of the [EPA SWMM 5](swmm-5.md) 5.2.4 source, with the engine running in the page. Version 1.15.1 [S68](../sources/S68-swmm5-code-house-app-md.md). Its sister app is the [SWMM6 Code House (app)](swmm6-code-house.md).

**The house.** 58 rooms on 5 floors hold 51,080 lines in 54 files, with 969 functions and 160 doorways [S68](../sources/S68-swmm5-code-house-app-md.md). Room size comes from the code: `link.c`, at 2,692 lines, is a hall 26 ft on a side, and `error.c`, at 49 lines, is a closet. The doors come from a parser's count of calls between files [S72](../sources/S72-li-swmm6-code-house-article.md). The reader walks as Froude, a water drop, or uses a Read tab with no 3D [S68](../sources/S68-swmm5-code-house-app-md.md).

**How it began.** On 2 November 2026 Bob asked Claude for a 3D house of the SWMM5 C code with the code on the walls, interactive diagrams, doorways to connected rooms and a water drop as guide. He then steered it with outside reviews from ChatGPT, attaching each and typing "add" [S72](../sources/S72-li-swmm6-code-house-article.md). Ten rounds of reviews had been applied by version 1.15 [S68](../sources/S68-swmm5-code-house-app-md.md).

**The engine inside** [S68](../sources/S68-swmm5-code-house-app-md.md)
- A WebAssembly build of 5.2.4 from USEPA commit 7952ca8, Emscripten 3.1.51, taken from Bob's Seven SWMM Engines app. The build was not repeated for the house.
- Against stored native 5.2.4 output on 78 corpus models: 78 inside the limits, 75 identical to the last stored digit, 801,567 of 805,991 values exactly equal, largest gap 2.4 % of one series' range.
- The limits were set after the first comparison, and why three models differ was not traced.

**Checks** [S68](../sources/S68-swmm5-code-house-app-md.md)
- 28 test scripts on the delivered file.
- 59 engine checks and 97 verification rows required.
- 344 of 344 deliberately forced engine failures were caught.
- 8,745 of 8,745 struct field uses resolve to their owner.

**Doors to the other house.** 454 of 962 SWMM 5 function names appear in the OpenSWMM 6 text, at 1,266 places. A door is a name match; it does not show the logic is the same [S68](../sources/S68-swmm5-code-house-app-md.md).

**A possible defect found while checking the diagrams.** In `culvert.c`, for a Form 1 culvert, the code returns the flow from the root finder's last trial and not from the root; flow can jump by up to 2.29 cfs across 0.005 ft of head. The article says the fix exists only as a JavaScript copy and has not been compiled or tested on a real build [S72](../sources/S72-li-swmm6-code-house-article.md). It has no register ID (Q47).

**What no person has done.** Read the diagrams against the C line by line, reviewed the lessons, or listened to the sound. Bob had not yet reviewed build 1.15.1 [S68](../sources/S68-swmm5-code-house-app-md.md).

**Open.** The public page at swmm5-code-house.netlify.app, and a second copy at an auto-named Netlify address, show a v1.0.0 badge in their page source (Q45). The function count is given as 969 and 962 here, and as 968 by the translator's census [S71](../sources/S71-swmm-engines-byte-for-byte-summary.md) (Q46). See [Open questions](../open-questions.md).
