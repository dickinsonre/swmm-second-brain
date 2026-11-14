# SWMM Findings Register — seed

Extracted from the conversation archive, batch 1 (Jun–Aug 2026).
Every entry below carries the detail actually recorded in the source
conversation. **Status is `unconfirmed` until you re-run it** — the whole
point of the register is that entries are re-runnable, and I cannot
re-run engine cases here.

Split into `findings/F-00NN.md` when you publish; kept in one file here
so it is reviewable in a sitting.

---

## SWMM-F-0001 — Preissmann slot and EXTRAN disagree at steady state
**date** 2026-08-26 · **subject** EPA SWMM 5.2.4 · **severity** wrong-answer
· **status** unconfirmed · **tags** [surcharge, slot, extran]

**Claim.** The Preissmann slot and EXTRAN surcharge methods converge to
different steady states on the same model — not a transient difference.

**How it was checked.** Simple-Pump analog: pump into a pressurized 1-ft
pipe, fixed 8-ft tailwater. One engine patched with a runtime-switchable
variant system (five formulations, including Lew Rossman's from issue
#231), pristine copy retained for byte-identity verification so the patch
is provably a no-op until flipped. clang 18 + wasi-libc.

**What came back.** Steady Q in C1: EXTRAN **5.0586 cfs**, SLOT stock
**5.2475 cfs** (+3.7 %). Steady J1 depth, EXTRAN **16.06 ft**.
Independently reproduced the issue #231 thread's claims.

**Source.** USEPA/Stormwater-Management-Model issue #231.

---

## SWMM-F-0002 — Three stacked errors hidden behind one bad shape spelling
**date** 2026-08-10 · **subject** OWA test corpus · **severity** wrong-answer
· **status** unconfirmed · **tags** [xsect, corpus, error-205]

**Claim.** Invalid `[XSECT]` shape tokens masked two further defect layers
in the OWA corpus. Fixing each one exposed the next.

**How it was checked.** Pulled the folder from GitHub master, reproduced
on engine 5.2.4, applied fixes, re-ran.

**What came back.** Layer 1 — underscore spellings (`SEMI_ELLIPTICAL` and
similar) throw **ERROR 205**; not one file but **20**. A keyword sweep of
all 151 files confirmed those were the only invalid shape tokens.
Layer 2 — with spelling fixed, ten files immediately fail **ERROR 211**:
every `MODBASKETHANDLE` line has `Geom2 = 0.0`, and unlike `BASKETHANDLE`
that shape requires a nonzero base width.
Layer 3 — peeling off the 211s, three files fail **ERROR 209**: their
`CUSTOM` section references a `CustomShape` curve that only two of the
five variants define.

**Note.** A corpus that fails at the first error tells you nothing about
the errors behind it. Worth a standing habit: fix and re-run until clean,
never fix and assume.

---

## SWMM-F-0003 — Audusse sign error survives mass conservation intact
**date** 2026-08-11 · **subject** own FV port · **severity** wrong-answer
· **status** fixed · **tags** [finite-volume, verification]

**Claim.** The Audusse well-balancing correction must be added to the
cell's **own** side of each face. Reversed, it destroys still water
completely — and mass conservation stays perfect throughout.

**How it was checked.** Ported the OpenSWMM FV kernels and tested against
the engine's own analytic cases before building any UI.

**What came back.** Correct form is `+(fq + corr_R)` at the left face,
`−(fq + corr_L)` at the right. Backwards: still water destroyed, mass
conservation unaffected. After fixing, **39/39** green against the
engine's own gate (relative L1 inside the fan plus shock position).

**Why it matters.** This is the cleanest counter-example to treating
continuity as validation. Every entry in this register that says "checked
against the engine" rather than "continuity closed" exists because of
this class of bug.

---

## SWMM-F-0004 — A benchmark harness that silently undercounts its corpus
**date** 2026-08-16 · **subject** swmmbench · **severity** silent
· **status** unconfirmed · **tags** [benchmark, corpus]

**Claim.** `discover()` uses a case-sensitive glob and drops uppercase
`.INP` files, while the harness self-check still reports success.

**What came back.** **57** uppercase `.INP` in the 2030 tree missed,
including `HALF_A_MiLLION.INP` and `SWMM5_NCIMM/newII°.inp`. Also flagged:
the sweep checks cleanliness once at the end rather than per model, and
results are unstratified — "Anderson only moves where…" so an aggregate
number says nothing.

---

## SWMM-F-0005 — SWMM6 keywords: fatal in 5.2.4, silent in legacy 5.3
**date** 2026-08-11 · **subject** EPA 5.2.4 / SWMM 5.3 · **severity** silent
· **status** partly unconfirmed · **tags** [swmm6, back-compat]

**Claim.** A `.inp` carrying SWMM6 `[OPTIONS]` keywords is rejected
outright by 5.2.4 and silently accepted by legacy 5.3.

**What came back.** 5.2.4 dies with fatal **ERROR 205** on the SWMM6
`[OPTIONS]` keywords — verified. `FV_*` keywords expected to behave the
same, **not** run as a specific case. Legacy 5.3 silently ignores options
that 5.2.4 rejects.

**Why it matters.** The silent path is the dangerous one: the model runs,
produces plausible numbers, and the intended behaviour is absent. The same
failure class was later flagged in a proposed EPANET `[SCRIPT]` section.

---

## SWMM-F-0006 — Own published accuracy claim was wrong by an order
**date** 2026-07-26 · **subject** Fourier cross-section fitter
· **severity** doc · **status** corrected · **tags** [xsect, self-audit]

**Claim.** An earlier claim of "well under 1 % of full depth" for Fourier
cross-section fits does not hold.

**What came back.** Conveyance error is ~**0.5–1.5 % at N=6**, but local
width error at invert and crown runs **4–14 %**. Two different quantities
were being conflated.

**Also found.** The level-crossing test missed vertices lying exactly on a
level (θ=0 and θ=π land precisely at mid-depth), so a circle would not fit
with zero harmonics. Fixed with a half-open rule.

---

## SWMM-F-0007 — LENGTHENING_STEP invents storage that continuity will not flag
**date** 2026-07-12 · **subject** EPA SWMM5 · **severity** silent
· **status** unconfirmed · **tags** [dynamic-wave, extran-lineage]

**Claim.** Conduit lengthening adds phantom storage, attenuates peaks and
suppresses node flooding, and nothing in the run warns you.

**What came back.** A 1 m pipe has c ≈ 3.1 m/s, so `Δt_L = 10 s` stretches
every conduit under ~31 m. A 6 m connector becomes 31 m — roughly **20 m³**
of storage that does not exist. **150 short stubs** in a flat combined
system ≈ **3,000 m³** of invisible attenuation, precisely where flooding
accuracy matters. Continuity closes throughout. Travel time and
water-column mass both inflate by the same factor.

**Also found.** The achieved curve never touches y = x — the velocity blind
spot. The demo's fully-lengthened stub reaches only **5.1 s** of a 10 s
target.

---

## SWMM-F-0008 — Twelve source-level defects in a third-party Rust rewrite
**date** 2026-08-04 · **subject** neeraip/hydra · **severity** mixed
· **status** unconfirmed · **tags** [third-party, review]

**Claim.** Twelve claims checked against source; all confirmed.

**Selected.** `TYPE5_PUMP` absent from the switch, falls through to
`return q`, while the adjacent comment claims it handles "other types of
pumps." `PARABOLOID` is a declared shape, absent from the switch, with no
`default:` — and the struct is `malloc`'d, not `calloc`'d. The tidal
branch omits `StartDateTime`, which the `TIMESERIES` case eight lines
below adds.

**Scope note.** The project ships no published drainage comparison against
SWMM's validation corpus. The performance table is EPANET-only: **21**
drainage fixtures against **108** distribution ones.

---

## Negative results

The entries below record ideas that did **not** work. They produced no
app worth keeping and are the most reusable part of this register.

### SWMM-F-0009 — Two-harmonic DWF parameterisation fails on real data
**date** 2026-07-26 · **status** disproven
Low-order Fourier parameterisation of diurnal dry-weather-flow patterns was
tested against real patterns and failed. Do not propose it again without
new evidence.

### SWMM-F-0010 — Monster Moonshine structure does not transfer
**date** 2026-06-30 · **status** disproven
The moonshine torus was usable as a *visual* projection only. The
underlying mathematics has no correspondence in SWMM's topology. A
by-product worth keeping: an angle-wraparound bug that would have
overlapped the first and last ring elements, caught in Node before the UI.

### SWMM-F-0011 — Klein-bottle topology does not apply
**date** 2026-07-17 · **status** disproven
Rejected on inspection. The kinematic-vs-dynamic-wave app was built
instead.

### SWMM-F-0012 — Hyperbolic geometry does not touch the hydraulics
**date** 2026-06 · **status** disproven-with-scope
St. Venant and Manning are Euclidean; reprojecting pipe coordinates into a
Poincaré disk is a category error. Curvature *does* earn its place in three
narrower places: network connectivity embedding, the drainage hierarchy
(Horton–Strahler, fractal river basins), and equifinality/calibration
space. Ran against five real networks.

### SWMM-F-0013 — Anderson acceleration gave no speedup on the test case
**date** 2026-07 · **status** disproven-on-this-case
Recorded as a negative result rather than a general claim; the honest
scope is "on this case," and a noise floor must precede any speed ratio.

---

## Corrections issued to other reviewers

Kept because a register of findings should include findings that went the
other way.

### SWMM-F-0014 — Two review claims that did not hold
**date** 2026-06-30 · **status** confirmed-against-source
An external review asserted "no resize handling / critical bug" — the plan
SVG uses a `viewBox`, which rescales natively, and the orbit canvas
re-checks its size every render. And "selection doesn't sync between
views" — `App.selectedId` was already shared. No action taken on either.

---

## What is still to extract

Batch 1 covers Jun–Aug 2026. Remaining populations, in priority order:

1. **Mar–May 2026** — Rosetta Stone (`PUMP3` curve order), ICMT parser,
   Four-Engine Comparator (terminal inlet, SLOT-vs-EXTRAN), Phase Space,
   Inspector Rover, MCP server `fd-1` finding.
2. **2025** — InfoSewer peaking replication, ICM Ruby refactors, the
   `hw_storage`/`hw_outfall` phantom-table correction.
3. **2024** — thinner, mostly product and workflow rather than engine.

Roughly 30–40 more entries expected.
