# SWMM Findings Register — format and seed

A numbered, dated record of what was checked and what came back. Plain
markdown in a git repo. Not an app — apps rot, text diffs.

## Why this and not the apps

The apps are safe: Netlify, GitHub, gists. The findings are not. The
`#229` root cause, the `MODIFIED_HORTON` behaviour, the two-harmonic
failure — those exist only inside chat transcripts. A register is the
form that survives the tooling that produced it.

## Entry format

One file per finding: `findings/F-0042.md`. Sequential IDs so they cite
cleanly (`SWMM-F-0042`) and never renumber.

```markdown
---
id: SWMM-F-0042
date: 2026-08-18
status: confirmed | fixed-upstream | open | disproven | superseded
subject: EPA SWMM 5.2.4          # engine, version, or repo
severity: wrong-answer | crash | silent | doc | performance
tags: [dynamic-wave, reporting]
---

## Claim
One sentence. What is wrong, or what was shown not to hold.

## How it was checked
The actual procedure. Engine + version, model, what was compared against
what. Enough that a stranger can repeat it.

## What came back
The numbers. Not "it matched" — the values, the tolerance, the run count.

## Reproduce
Exact steps or a pointer to a fixture in this repo.

## Status notes
Filed upstream? Issue number? Fixed in which version?

## Source
Conversation date and link, or the app that carries the test.
```

Four rules that make it worth keeping:

1. **Negative results are entries.** A disproven idea is a finding. Most
   registers only record bugs and lose the more valuable half.
2. **No claim without a procedure.** An entry whose "how it was checked"
   is empty is a note, not a finding. Keep notes elsewhere.
3. **Numbers, not adjectives.** "Matches well" is not a result.
4. **Status can change; the entry does not.** Supersede by adding a new
   entry that references the old ID. Never rewrite history.

## Seed — candidates from the archive

These are drawn from conversation records. **Each needs your confirmation
before publishing** — several are engine specifics I cannot re-run here,
and the register's whole value is that entries are re-runnable.

| Candidate | Subject | Status |
|---|---|---|
| Two interpolations of the same quantity (`output.c:590` vs `routing.c:592`) | EPA 5.2.4 | root-caused, USEPA #229 |
| `[XSECT]` shape names wrong across 20 OWA corpus `.inp` files | OWA corpus | confirmed |
| `MODIFIED_HORTON` / MaxInfil behaviour | SWMM5 | confirmed |
| Metric-units defect, timeseries inflow | OpenSWMM 6.0.0-alpha.2 | confirmed |
| `PUMP3` curve-order bug | EPANET | caught by Rosetta Stone |
| Terminal inlet behaviour | four-engine comparison | confirmed |
| CHANGELOG lists 17 `FV_` keys; `OptionsHandler.cpp` parses 21 | OpenSWMM develop | doc |
| Audusse correction sign error (own FV port) | own code | fixed |
| Dry-bed front tip lags 10–15 ft regardless of refinement | FV solver | characterised |
| `ERROR 205` on SWMM6 keywords in stock 5.2.4 | EPA 5.2.4 | confirmed |
| Legacy 5.3 silently ignores SWMM6 keywords | SWMM 5.3 | silent |
| Virtual-junction crash | OpenSWMM alpha.2 | confirmed |
| `hw_storage` / `hw_outfall` are phantom tables | ICM IWR | corrected |
| Kriging bug | Stochastic Hydrology Studio | fixed |
| Ghost names / duplicates on bulk SWMM5→ICM import | ICM Ruby | fixed |
| **Two-harmonic DWF parameterisation fails on real data** | — | **disproven** |
| **Anderson acceleration gave no speedup on the test case** | SWMM6 | **disproven** |
| **Monster Moonshine structure does not transfer to SWMM** | — | **disproven** |
| **Klein-bottle topology does not apply** | — | **disproven** |
| **Hyperbolic geometry does not touch the hydraulics** | — | **disproven** |

Twenty entries, five of them negative results. That last group is the
part no other register in this field has.

## Keeping it current

`corinne-testing` already requires a numbered defect register per app.
Add one line to it: *findings that outlive the app get filed upstream in
the findings register with a permanent ID.* Then the register fills as a
by-product of work already being done, rather than as a separate chore.

## Extraction plan for the back catalogue

Keyword search does not work — a scan for defect language returned 44
conversations, with prose-editing and Mars-habitat apps in the top ten.
The findings have to be read out.

Bounded approach, roughly 50–80 conversations:

1. Engine-verified app conversations (the `corinne-testing` population).
2. Review conversations — AquaTwin, Hydra, swmmbench, the 3D flood repo,
   Caleb's routing scheme.
3. First-principles threads, which is where the disproven results live.

Do it in batches of ten, newest first. The recent ones are freshest and
most likely still actionable; the 2024 material can wait.
