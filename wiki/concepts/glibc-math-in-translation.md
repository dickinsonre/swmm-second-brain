---
title: Matching glibc math in a translation
type: concept
updated: 2026-11-14
sources: [S23, S24, S27, S28, S30, S32, S33, S34, S35]
tags: [translation, numerics, verification]
reviewed: no
---
A byte-for-byte translation needs every math function to return the same bits as the one the original engine calls. The SWMM6 C++ engine calls glibc 2.39's math library; the SWMM6 ports use 19 of its functions [S24](../sources/S24-swmm6-go-readme.md). The ports took two routes.

**Route 1: translate glibc's own code.** Go, Java, TypeScript, Kotlin, Groovy and JavaScript carry bit-exact translations of the 19 functions [S24](../sources/S24-swmm6-go-readme.md). From Kotlin on, the source of the translation is named: GCC's compiled form of glibc 2.39 (GIMPLE), turned into the target language by `tools/libm/gim2x.py`. glibc's source is compiled only; nothing of glibc is run [S30](../sources/S30-swmm6-kotlin-readme.md). The translated math stays under glibc's licence, LGPL 2.1 or later, inside an Apache-licensed repository [S24](../sources/S24-swmm6-go-readme.md). JavaScript has its own back end in the same tool [S32](../sources/S32-swmm6-javascript-readme.md).

**Route 2: call the system's glibc.** CPython's `math` module calls glibc, "so its results are glibc's" [S28](../sources/S28-swmm6-python-readme.md). F# declares the calls by P/Invoke at the same symbol versions the C++ engine binds [S33](../sources/S33-swmm6-fsharp-readme.md). The interpreted languages need help where the language decides a result itself:
- Hy: ctypes calls into glibc at the GLIBC_2.29 symbol versions where CPython would decide, and a hand-written module to match glibc on signalling NaNs [S34](../sources/S34-swmm6-hy-readme.md).
- Ruby: Fiddle calls where MRI decides or has no function: `cbrt`, `expm1`, `log1p`, `fmod`, `remainder`, `nextafter`, `pow` of a negative base, and `acos`, `asin` and the logarithms outside their domains [S35](../sources/S35-swmm6-ruby-readme.md).

**How each route is proved.** Each translated function is tested against the system's glibc 2.39 on about a million arguments, special values and NaN payloads included, with no difference. The READMEs call that "a test, not a proof" [S24](../sources/S24-swmm6-go-readme.md). The math tests of each newer port are kept in its `results/libm_tests.txt` [S30](../sources/S30-swmm6-kotlin-readme.md).

**Not in the sources.** The trade between the routes: route 1 gives an engine that carries its own math; route 2 is less code, but its result is only as fixed as the glibc it runs on. Why glibc and not another C library: the reference engine was built on Linux with glibc, so glibc's last-bit choices are the ones to match. The C# and Fortran READMEs do not say which route those ports took [S23](../sources/S23-swmm6-csharp-readme.md) [S27](../sources/S27-swmm6-fortran-readme.md).

See [Byte-for-byte gate](byte-for-byte-gate.md), [SWMM6 language translations](../entities/swmm6-language-ports.md).
