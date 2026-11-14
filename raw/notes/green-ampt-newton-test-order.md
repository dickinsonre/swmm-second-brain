# SWMM5's Green-Ampt solver tests the Newton correction before applying it, so some wet steps infiltrate at Ksat alone

**Status:** working
**Date:** 2026-11-14

## The idea
In EPA SWMM 5.2.4, `grnampt_getF2` checks the size of each Newton correction before it applies it, against a fixed 0.00001 ft. When Ksat times the wet step is small, the very first correction is already under that limit, so the function returns the minimum volume and the step infiltrates at Ksat alone, with the suction term dropped. The result then depends on the wet step in a way nobody would choose: a clay soil lost 21% of its infiltration at a 15-second wet step and nothing at 5, 30, 60 or 300 seconds, while the continuity error stayed at -0.001%. What broke: four independent solvers of the same equation agreed with each other and not with the stock engine. What fixed it: moving `f2 -= df2;` above the convergence test.

## Proof / from scratch
The equation being solved for F2, with c1 = (suction head + ponded depth) x moisture deficit:

```
F2 - F1 - c1 * ln((F2 + c1) / (F1 + c1)) = Ks * ts
```

The code as it is, `src/solver/infil.c` lines 847 to 856 (`f2` starts equal to `f1`):

```c
    for ( i = 1; i <= 20; i++ )
    {
        df2 = (f2 - f1 - c1 * log(f2 + c1) + c2) / (1.0 - c1 / (f2 + c1) );
        if ( fabs(df2) < 0.00001 )
        {
            return MAX(f2, f2min);
        }
        f2 -= df2;
    }
    return f2min;
```

At the `return`, `f2` has not yet had `df2` applied.

The fix is one line moved:

```c
        f2 -= df2;
        if ( fabs(df2) < 0.00001 ) return MAX(f2, f2min);
```

When the early return happens: wet step of 10 s or more, and

```
Ks (in/hr) x wet step (s) x (1 + c1/F) < 0.432
```

Test model: one 10 ac pervious subcatchment, suction 12.6 in, Ksat 0.01 in/hr, deficit 0.10, 24 hours of rain totaling 6.137 in. Here c1 = 1.26 in, so at 15 s the early return starts once F passes 0.67 in. At 30 s it would need F above 2.86 in, which this run never reaches.

| Run | Infiltration, in | Peak runoff, cfs |
|---|---|---|
| Stock, wet step 5, 30, 60 or 300 s | 1.096 to 1.097 | 3.3109 |
| Stock, wet step 15 s | 0.868 | 3.4858 |
| One line moved, wet step 15 s | 1.096 | 3.3109 |
| Four independent solvers, wet step 15 s | 1.096 | 3.3109 |

A smaller effect comes from the same lines in every run. The returned value is the iterate before its last correction, and Newton comes at this root from above, so stock is high by up to 0.00001 ft per call. On a silt loam test that was 1.287 in against 1.286 in.

Not shown: any real model, LID, snowmelt or storage seepage. The runs were made once and have not been rerun by Bob.

To rerun: `./greenampt_clay_15s.inp` on stock 5.2.4 gives 0.868 in. Apply `./swmm524_greenampt_alternates.patch`, set `GA_ALT=6`, and it gives 1.096 in.

## Links
- [Full write-up with every number](./green-ampt-newton-stop-2026-11-14.md): the register-format note this idea was cut from
- [Infiltration methods](../../wiki/concepts/infiltration-methods.md): where the Green-Ampt entry points are listed
- [Continuity is not validation](../../wiki/concepts/continuity-is-not-validation.md): another run whose mass balance closed while the answer was off
- [The SWMM findings register](../../wiki/concepts/findings-register.md): this needs an ID there
- [infil.c in EPA's repository](https://github.com/USEPA/Stormwater-Management-Model/blob/master/src/solver/infil.c): the stock code

AI use: drafted by Claude (Anthropic) on 14 November 2026 from test runs Claude made in a chat with Bob Dickinson. The wording is Claude's until Bob rewrites it.
