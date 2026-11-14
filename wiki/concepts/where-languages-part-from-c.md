---
title: Where languages part from C
type: concept
updated: 2026-11-14
sources: [S38, S39, S40, S43, S44, S45, S46, S47, S48, S49, S50, S51, S53, S54, S70]
tags: [translation, numerics]
reviewed: no
---
The traps the SWMM5 translations met: places where a language computes something other than what EPA's C computes on x86-64. Each README lists its own; these are the ones with numbers or a found case.

On 12 November 2026, 24 of these traps were rerun as probes of a few lines each, and 24 reproduced [S70](../sources/S70-swmm-engine-what-if-app-md.md).

**The sign of zero and of NaN**
- Perl adds, subtracts and multiplies whole-number doubles as 64-bit integers, so `0.0 * -3.0` is +0.0 in Perl and -0.0 in C [S49](../sources/S49-swmm5-perl-readme.md).
- PHP's `-$x` multiplies by -1 and leaves a NaN's sign bit alone; C's negation flips it [S47](../sources/S47-swmm5-php-readme.md).
- Groovy folds `-0.0d` to +0.0 [S50](../sources/S50-swmm5-groovy-readme.md). PHP's OPcache optimizer treats 0.0 and -0.0 as the same constant [S47](../sources/S47-swmm5-php-readme.md).
- x86 makes NaNs with the sign bit set (EPA prints `-nan`). Ruby's `Float#/` and V8's optimized code gave NaNs with it clear [S45](../sources/S45-swmm5-ruby-readme.md) [S46](../sources/S46-swmm5-javascript-readme.md).

**Comparisons and truth**
- In Groovy, `a > b` and `a >= b` on doubles are true when either side is NaN; C says false. One model's report listed five NaN nodes as not converging [S50](../sources/S50-swmm5-groovy-readme.md).
- In R a comparison with NaN is NA, and `if (NA)` is an error. The R port runs a fast engine and falls back to a NaN-proof one [S54](../sources/S54-swmm5-r-readme.md).
- 0 and 0.0 are true in Ruby [S45](../sources/S45-swmm5-ruby-readme.md).

**Division and integers**
- Division by zero throws or dies in PHP and Perl, for doubles too; C gives infinities or NaN [S47](../sources/S47-swmm5-php-readme.md) [S49](../sources/S49-swmm5-perl-readme.md).
- Lua's, Ruby's and Mojo's integer `//` and `%` floor where C truncates [S45](../sources/S45-swmm5-ruby-readme.md) [S51](../sources/S51-swmm5-lua-readme.md) [S53](../sources/S53-swmm5-mojo-readme.md). In Groovy `/` on two ints gives a `BigDecimal` [S50](../sources/S50-swmm5-groovy-readme.md).
- Double to int: x86 gives INT_MIN for NaN and out-of-range values; Java's cast saturates and LLVM's is undefined, so the ports write x86's rule out [S40](../sources/S40-swmm5-java-readme.md) [S53](../sources/S53-swmm5-mojo-readme.md).
- JavaScript has only doubles, so integer code is spelled out "so it can never yield -0" [S39](../sources/S39-swmm5-typescript-readme.md).

**Rounding**
- An untyped real constant in Free Pascal is 80-bit Extended, so `x * 0.1` rounds twice [S43](../sources/S43-swmm5-pascal-readme.md).
- Mojo fuses `a*b + c` into one fused multiply-add by default; C as EPA's gcc build compiles it rounds twice [S53](../sources/S53-swmm5-mojo-readme.md).
- MRI's `format` printed 36.15 as "36.2" with `%.1f`; glibc prints "36.1" [S45](../sources/S45-swmm5-ruby-readme.md).
- R's parser misreads 30 of 199,988 plain decimals [S54](../sources/S54-swmm5-r-readme.md).

**Power and other functions**
- Lua's `x ^ 2` and R's `x ^ 2` are `x * x`, which differs from glibc's `pow(x, 2)` in 12,953 of 20,000,000 arguments [S51](../sources/S51-swmm5-lua-readme.md) [S54](../sources/S54-swmm5-r-readme.md).
- Perl's `**` on two whole numbers is exact integer code, not glibc's `pow` [S49](../sources/S49-swmm5-perl-readme.md).
- Zig's own compiler-rt captured the engine's calls to exp, log, sin and cos: 39 models differed [S44](../sources/S44-swmm5-zig-readme.md).

**Memory and the machine**
- C's `calloc` costs nothing until written. R zero-fills up front, and Lua and PHP arrays take 16 bytes an element, so one model's 3.38 GB of RDII history needed special storage [S47](../sources/S47-swmm5-php-readme.md) [S51](../sources/S51-swmm5-lua-readme.md) [S54](../sources/S54-swmm5-r-readme.md).
- HotSpot never compiles a method over 8,000 bytes; Groovy's pow is 9,161 bytes, and one model ran more than 380 s instead of 32.6 s [S50](../sources/S50-swmm5-groovy-readme.md).
- F# has no `return`, `break`, `continue` or `goto`; 551 returns became flags [S48](../sources/S48-swmm5-fsharp-readme.md).

See [Matching glibc math in a translation](glibc-math-in-translation.md), [SWMM5 language translations](../entities/swmm5-language-ports.md).
