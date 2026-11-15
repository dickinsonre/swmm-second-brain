---
title: "SWMM5 translations: the re-run of 12 November 2026"
type: concept
updated: 2026-11-14
sources: [S70, S71]
tags: [swmm5, translation, benchmarks, verification]
reviewed: 2026-11-15
---
On 12 November 2026 all twenty translations of EPA SWMM 5.2.4 were cloned at their listed commits, rebuilt on one machine and run again, for version 1.4 of the [SWMM Engine What If (app)](../entities/swmm-engine-what-if.md) [S70](../sources/S70-swmm-engine-what-if-app-md.md). It is the first time the [SWMM5 language translations](../entities/swmm5-language-ports.md) were all measured the same way. Claude ran it; no person has repeated it [S70](../sources/S70-swmm-engine-what-if-app-md.md).

**The machine.** Intel Xeon, 2.10 GHz, 2 cores, with FMA, AVX2 and AVX-512; 8 GB; Ubuntu 24.04, glibc 2.39. EPA 5.2.4 built with gcc 13.3.0 at -O2 ran the 480 gate models in 190 s [S70](../sources/S70-swmm-engine-what-if-app-md.md).

**Gate and speed** [S70](../sources/S70-swmm-engine-what-if-app-md.md)

Speed is the median CPU-time ratio to EPA over 12 models (EPA 0.007 to 0.688 s each), with the range in parentheses. Every engine matched EPA on every model it ran.

| Engine | Models run | Speed against EPA |
|---|---|---|
| EPA again (noise) | 480 | 1.005 (0.819 to 1.181) |
| C++ | 480 | 0.94 (0.843 to 1.058) |
| Zig | 480 | 1.033 (0.757 to 1.17) |
| Mojo | 480 | 1.082 (0.991 to 1.754) |
| Rust | 480 | 1.163 (0.952 to 1.349) |
| Fortran | 480 | 1.281 (1.048 to 1.373) |
| Go | 480 | 1.542 (1.281 to 2.478) |
| Pascal | 480 | 1.59 (1.435 to 1.872) |
| C# | 480 | 5.353 (2.883 to 30.304) |
| F# | 480 | 6.79 (3.377 to 40.696) |
| Java | 480 | 9.847 (4.931 to 91.986) |
| Kotlin | 480 | 13.648 (6.679 to 138.029) |
| JavaScript | 480 | 17.281 (9.156 to 73.841) |
| TypeScript | 480 | 19.323 (10.879 to 73.145) |
| PHP | 451 | 21.947 (15.083 to 49.978) |
| Groovy | 480 | 22.974 (9.987 to 328.551) |
| Lua | 451 | 47.401 (42.136 to 74.726) |
| Python | 393 | 87.397 (69.58 to 111.754) |
| Hy | 393 | 96.839 (80.638 to 129.125) |
| Ruby | 393 | 101.653 (85.489 to 129.881) |
| Perl | 393 | 249.478 (209.797 to 339.114) |

The 393 are the models EPA runs in 0.1 s or less, and the 451 those it runs in 1 s or less. The interpreters and PHP and Lua ran 2 repetitions; the rest 5 [S70](../sources/S70-swmm-engine-what-if-app-md.md).

**What the numbers can bear** [S70](../sources/S70-swmm-engine-what-if-app-md.md)
- C++, Rust, Zig and Mojo fall inside EPA's own band of 0.819 to 1.181, so they are not shown to differ from EPA in speed.
- The models are short and start-up time is inside every figure. That is most of what the JVM, .NET and interpreter figures measure on the smallest models.
- No long continuous run was timed.

**Against what the repositories had said** [S70](../sources/S70-swmm-engine-what-if-app-md.md)
- The 8 figures that came from interleaved benchmarks reproduced within 11 percent. The earlier figures are on [SWMM Engines, Byte for Byte (app)](../entities/swmm-engines-byte-for-byte.md) [S71](../sources/S71-swmm-engines-byte-for-byte-summary.md).
- The 5 "rough" guides (Mojo, PHP, Ruby, Hy, Perl) came back 1.45 to 1.73 times higher. Mojo's rough figure was about 0.73; measured, 1.082.
- Kotlin's README range of 1.31 to 2.63, on six longer models, was not repeated; on the 12 short models it is 13.648.

**Generic math.** With glibc forced to its non-FMA routines, EPA's own output changes on 43 of 480 models. Fourteen ports follow EPA to the new answers and six keep the old ones. The lists are on [Matching glibc math in a translation](glibc-math-in-translation.md) [S70](../sources/S70-swmm-engine-what-if-app-md.md).

**Probes.** 24 language traps from the ports' lessons were rerun in a few lines each, and 24 reproduced. See [Where languages part from C](where-languages-part-from-c.md) [S70](../sources/S70-swmm-engine-what-if-app-md.md).

**What it is not.** The sandbox was the kind the ports were built in, with the same compilers. "It shows the commits rebuild and still match. It is not a test on other hardware, another libc or another compiler" [S70](../sources/S70-swmm-engine-what-if-app-md.md). The R translation was not in it: its repository was empty when read (Q48 in [Open questions](../open-questions.md)).
