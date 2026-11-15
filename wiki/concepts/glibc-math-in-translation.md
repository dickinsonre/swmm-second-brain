---
title: Matching glibc math in a translation
type: concept
updated: 2026-11-15
sources: [S23, S24, S27, S28, S30, S32, S33, S34, S35, S41, S44, S51, S52, S54, S70, S82]
tags: [translation, numerics, verification]
reviewed: 2026-11-15
changed_after_review: "2026-11-15: one paragraph added near the end, headed Added 15 November 2026"
---
A byte-for-byte translation needs every math function to return the same bits as the one the original engine calls. The SWMM6 C++ engine calls glibc 2.39's math library; the SWMM6 ports use 19 of its functions [S24](../sources/S24-swmm6-go-readme.md). The ports took two routes.

**Route 1: translate glibc's own code.** Go, Java, TypeScript, Kotlin, Groovy and JavaScript carry bit-exact translations of the 19 functions [S24](../sources/S24-swmm6-go-readme.md). From Kotlin on, the source of the translation is named: GCC's compiled form of glibc 2.39 (GIMPLE), turned into the target language by `tools/libm/gim2x.py`. glibc's source is compiled only; nothing of glibc is run [S30](../sources/S30-swmm6-kotlin-readme.md). The translated math stays under glibc's licence, LGPL 2.1 or later, inside an Apache-licensed repository [S24](../sources/S24-swmm6-go-readme.md). JavaScript has its own back end in the same tool [S32](../sources/S32-swmm6-javascript-readme.md).

**Route 2: call the system's glibc.** CPython's `math` module calls glibc, "so its results are glibc's" [S28](../sources/S28-swmm6-python-readme.md). F# declares the calls by P/Invoke at the same symbol versions the C++ engine binds [S33](../sources/S33-swmm6-fsharp-readme.md). The interpreted languages need help where the language decides a result itself:
- Hy: ctypes calls into glibc at the GLIBC_2.29 symbol versions where CPython would decide, and a hand-written module to match glibc on signalling NaNs [S34](../sources/S34-swmm6-hy-readme.md).
- Ruby: Fiddle calls where MRI decides or has no function: `cbrt`, `expm1`, `log1p`, `fmod`, `remainder`, `nextafter`, `pow` of a negative base, and `acos`, `asin` and the logarithms outside their domains [S35](../sources/S35-swmm6-ruby-readme.md).

**In the SWMM5 translations.** EPA calls ten glibc functions (exp, log, log10, pow, sin, cos, tan, asin, acos, atan) 1,524,961,124 times over the 480 gate models. On x86-64, glibc picks versions compiled with fused multiply-add at start-up when the processor has FMA and AVX2, and EPA run on the generic routines changes 43 of 480 models [S41](../sources/S41-swmm5-go-readme.md). So the routes split: a port carrying translated glibc (Go, Java, TypeScript, Kotlin, JavaScript, Groovy) matches EPA on an FMA processor anywhere, but would not follow EPA onto one without; a port that calls the system glibc (Fortran, C#, Zig, Free Pascal, Ruby, PHP, F#, Perl, Hy, Mojo, R) should follow EPA there, which was not tested [S41](../sources/S41-swmm5-go-readme.md) [S44](../sources/S44-swmm5-zig-readme.md). Lua does both: glibc at run time, plus translated `pow` for an exponent of 2 and `atan` [S51](../sources/S51-swmm5-lua-readme.md). Calling glibc is not enough on its own: the binary must bind the symbol versions EPA binds (`exp@GLIBC_2.29` and so on), and the language must not decide some cases itself. CPython and lupa bind the older SVID wrappers, and R, Ruby, Perl and PHP each decide some zero, NaN or domain-error cases on their own [S52](../sources/S52-swmm5-hy-readme.md) [S51](../sources/S51-swmm5-lua-readme.md) [S54](../sources/S54-swmm5-r-readme.md). See [Where languages part from C](where-languages-part-from-c.md).

**Which ports follow EPA off FMA, measured.** On 12 November 2026 glibc was forced to its generic routines (`GLIBC_TUNABLES=glibc.cpu.hwcaps=-AVX2,-FMA,-FMA4`). EPA's output changed on 43 of 480 models. Fourteen ports followed EPA to the new answers on every affected model run: C++, Rust, Fortran, Zig, Pascal, Mojo, C#, F#, Python, PHP, Ruby, Lua, Hy, Perl. Six kept the FMA answers: Go, Java, Kotlin, Groovy, TypeScript, JavaScript. The test forces the routines on an FMA machine; it was not run on a processor without FMA [S70](../sources/S70-swmm-engine-what-if-app-md.md).

**How each route is proved.** Each translated function is tested against the system's glibc 2.39 on about a million arguments, special values and NaN payloads included, with no difference. The READMEs call that "a test, not a proof" [S24](../sources/S24-swmm6-go-readme.md). The math tests of each newer port are kept in its `results/libm_tests.txt` [S30](../sources/S30-swmm6-kotlin-readme.md).

**Not in the sources.** The trade between the routes: route 1 gives an engine that carries its own math; route 2 is less code, but its result is only as fixed as the glibc it runs on. Why glibc and not another C library: the reference engine was built on Linux with glibc, so glibc's last-bit choices are the ones to match. The SWMM6 C# and Fortran READMEs do not say which route those ports took [S23](../sources/S23-swmm6-csharp-readme.md) [S27](../sources/S27-swmm6-fortran-readme.md).

**Added 15 November 2026.** The same problem appears without any translation, between a native build and a WebAssembly build of the same C. In one census 59 of 449 models gave different `.out` files in the browser than in a native glibc build, and all 59 matched a native build linked against musl [S82](../sources/S82-mirab-test-bench-summary.md). See [WebAssembly builds against native builds](wasm-against-native-builds.md).

See [Byte-for-byte gate](byte-for-byte-gate.md), [SWMM6 language translations](../entities/swmm6-language-ports.md).
