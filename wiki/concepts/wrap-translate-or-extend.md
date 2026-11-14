---
title: Wrap, translate or extend
type: concept
updated: 2026-11-14
sources: [S70, S72]
tags: [swmm5, swmm6, translation, method]
reviewed: no
---
Three roads for getting SWMM into another language or making it compute something new, as Bob's [SWMM Engine What If (app)](../entities/swmm-engine-what-if.md) sets them out [S70](../sources/S70-swmm-engine-what-if-app-md.md).

| Road | What it is | Evidence on record |
|---|---|---|
| Wrap | Call EPA's C from the other language | Fit judgments only |
| Translate | Rewrite the engine in the other language and hold it to EPA byte for byte | 20 translations of SWMM 5.2.4, 12 of OpenSWMM 6 |
| Extend | Add an option to EPA's C and leave the old path byte-identical | 4 engines |

Table from [S70](../sources/S70-swmm-engine-what-if-app-md.md). See [SWMM5 language translations](../entities/swmm5-language-ports.md), [SWMM6 language translations](../entities/swmm6-language-ports.md) and [Byte-for-byte gate](byte-for-byte-gate.md).

**The constraint behind most of the judgments.** EPA SWMM 5 keeps a model in file and program scope, 415 mutable variables, so one process holds one model [S70](../sources/S70-swmm-engine-what-if-app-md.md). A wrapper inherits that. So does an extended engine. Among the translations the fleet table marks only swmm5-cplus and swmm5-rust as holding state per model [S70](../sources/S70-swmm-engine-what-if-app-md.md). OpenSWMM 6 moved a run's state into one context object, one per concurrent simulation [S72](../sources/S72-li-swmm6-code-house-article.md).

**Fit, for three of the seven goals** [S70](../sources/S70-swmm-engine-what-if-app-md.md)

| Goal | Wrap | Translate | Extend |
|---|---|---|---|
| Hold several models in one process | poor in every language but TypeScript and JavaScript (fair) | strong in C++ and Rust | poor |
| Stop at a bad array index | poor in every language | strong in Rust, Go, C#, Java, Kotlin, F#, Groovy, Python, Hy | poor |
| Try a new numerical method | strong in C only | strong in C, C++, Fortran | strong |

The app has 294 such cells plus 7 for the extend road. They are "editorial judgment, not measurement", written by Claude, and 175 of them have had no human review [S70](../sources/S70-swmm-engine-what-if-app-md.md).

**The four extended engines** [S70](../sources/S70-swmm-engine-what-if-app-md.md)

| Engine | Adds | With the option off | With it on |
|---|---|---|---|
| swmm5-kw | Kinematic wave and steady flow that split at junctions and iterate loops | 3,737 of 3,759 corpus models identical to stock, 0 different | No reference engine; flow conserved at every split to 6e-14 cfs |
| [swmm524-perched](../entities/swmm524-perched.md) | A second soil layer in bio-retention cells | 598 of 598 inputs write the same `.out` bytes | No reference engine; a limiting case matches stock to 0.000 in |
| swmm5-raspipe | A semi-implicit pipe solver after the HEC-RAS pipe method | 4 of 4 control decks identical | Not compared with HEC-RAS; median routing continuity error 0.005 % against stock's 0.795 % on 1,600 models, at 2.6 times the run time |
| swmm5-infosewer | InfoSewer's calculations as a routing option | 14 models identical | Reference is InfoSewer: 11,408,158 of 11,894,156 values bit-identical on 71 models, the rest within 4.2e-11 |

**The rule the extend road follows.** A new option sits behind a normal `.inp`, and with the option off the engine must still equal stock EPA [S70](../sources/S70-swmm-engine-what-if-app-md.md). That gives a null test even where no reference exists for the new path.

**Its weak point.** "The extended engines' new paths are judged by weaker tests than a byte gate; three have no reference engine" [S70](../sources/S70-swmm-engine-what-if-app-md.md). A lower continuity error is not proof the new solver is right; see [Continuity is not validation](continuity-is-not-validation.md).

**Not in the sources yet.** The repositories of swmm5-kw, swmm5-raspipe and swmm5-infosewer, and any use of a wrapper in practice.
