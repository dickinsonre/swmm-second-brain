---
title: What the gate cannot see
type: concept
updated: 2026-11-15
sources: [S39, S40, S41, S43, S44, S45, S47, S49, S50, S54, S87]
tags: [verification, method, translation]
reviewed: 2026-11-15
---
A [Byte-for-byte gate](byte-for-byte-gate.md) passes or fails a whole model. The SWMM5 translation READMEs record what it misses and what was added to cover the gaps.

**Controls: does the gate notice anything?** [S41](../sources/S41-swmm5-go-readme.md)
- Null control: EPA run twice gives 40 of 40 identical files, so a pass is not luck of timing.
- Positive control: the Fortran engine rebuilt with fused multiply-add allowed differs from EPA on 87 of 480 models. "The gate catches a one-rounding-step change", and those 87 are the models that notice one.
- Math controls: the same engines with the language's own math library in place of glibc's differ on 108 of 480 (Go), 38 of 480 (Java) and 6 of 40 control models (TypeScript) [S41](../sources/S41-swmm5-go-readme.md) [S40](../sources/S40-swmm5-java-readme.md) [S39](../sources/S39-swmm5-typescript-readme.md).

**The gate cannot vouch for the runtime.** The Free Pascal port's first strtod got 115,302 of 200,052 test cases wrong "while the gate passed all 480 models" [S43](../sources/S43-swmm5-pascal-readme.md). So each runtime is also replayed against glibc on 1,394,252 printf, strtod and sscanf cases, and each math function on millions of arguments [S43](../sources/S43-swmm5-pascal-readme.md) [S45](../sources/S45-swmm5-ruby-readme.md).

**Checked builds.** A Zig build with bounds, overflow and cast checks trapped on all but 3 of 480 models: the runtime's `calloc(0)` returned a pointer one past its block. The ordinary build had passed all 480 [S44](../sources/S44-swmm5-zig-readme.md). Free Pascal was run with range checks on every fixed-array index: no error [S43](../sources/S43-swmm5-pascal-readme.md). The memory-safe languages cannot do this: a C overrun that stays inside an array's bounds, or a write past an end that the language quietly grows, "would not show; the gate would see it only if it changed an output" [S47](../sources/S47-swmm5-php-readme.md) [S49](../sources/S49-swmm5-perl-readme.md).

**Paths no gate model reaches.** Streets and inlets (one deck, which stops on input errors), climate files, USE HOTSTART, USE INFLOWS and USE RUNOFF. The stepping API (`swmm_open`, `swmm_step`, ...) is translated, but only the command line was gated [S41](../sources/S41-swmm5-go-readme.md) [S45](../sources/S45-swmm5-ruby-readme.md).

**Models stopped at the limit.** A model stopped at 1,800 s counts as not run, even when everything it wrote matches EPA. R's 15 such models had written from 0 to 96 % of their `.out` files, all matching so far [S54](../sources/S54-swmm5-r-readme.md).

**Speed is not what it seems.** Groovy's gate took 1,114 s and, for the same code rebuilt, 792 s: "the load of the shared machine moves the gate's clock by that much" [S50](../sources/S50-swmm5-groovy-readme.md).

**What no gate shows.** "That SWMM is right: identical to EPA means EPA's answers, good or bad. No observed data enter anywhere" [S41](../sources/S41-swmm5-go-readme.md). See [Continuity is not validation](continuity-is-not-validation.md).

**Added 15 November 2026.** The corpus the gate draws on has been measured against a list of known defects. Before two folders were added on 23 October 2026, 53 of the input-reachable findings of the HydroCouple swmm-code-review (200 findings in all) had no model in the corpus, and 25 had only one to three. The review's 351 reproducer decks are now in the corpus; 11 of them crash or hang EPA SWMM 5.2.4 [S87](../sources/S87-corpus-1729-readme.md). Whether any of the 351 has joined the 480-model gate set is not in the sources. See [1729-SWMM5-Models-2030 (the corpus)](../entities/corpus-1729.md).

See [SWMM5 language translations](../entities/swmm5-language-ports.md), [Where languages part from C](where-languages-part-from-c.md).
