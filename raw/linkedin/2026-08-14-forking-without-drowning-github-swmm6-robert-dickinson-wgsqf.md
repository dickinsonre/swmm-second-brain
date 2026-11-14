---
title: "Forking without Drowning on GitHub for #SWMM6"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/forking-without-drowning-github-swmm6-robert-dickinson-wgsqf
created: "2026-08-14 14:25"
published: "2026-08-14 14:33"
words: 929
export_sha256: 226178d24e333e6fad3e2dd2ac265da7aae5f78e2a7d46b299ffb32f64f5ae3d
---
# Forking without Drowning on GitHub for #SWMM6

![](https://media.licdn.com/dms/image/v2/D4E12AQHBow7-cAKBmw/series-logo_image-shrink_300_300/series-logo_image-shrink_300_300/0/1707065394509?e=1795651200&v=beta&t=tN-hhC1z9uquar5xA2f4iKHMUJauOcieSynf04B5KXc)

### EPASWMM5 Related Software Five decades with SWMM, still shipping code. SWMM5/6, ICM with Ruby, browser apps that teach the engines — and the art

![Forking without Drowning on GitHub for SWMM6 ](https://media.licdn.com/mediaD4D12AQGg8BPdPHkXSg "Forking without Drowning on GitHub for SWMM6 ")

Me: This is all from Claude Fable to help me. I often Fork a repo without getting al of the branches so i am lost. I also use many PCs so I am often lost when switching PCs. Where is my Ruby script?

Fable: Before the workflow answer, three things I verified in those repos that change what "contribute back" actually requires:

**Both** and now carry a full governance stack — , (v1.0, May 2026), , . Caleb is named Technical Manager. Every PR needs **three** approvals: Caleb, an AI Copilot review, and a community reviewer who isn't the author. First-time contributors must sign the CLA before merge, and the CLA grants Caleb a relicensing right (including to a commercial license) — worth reading §2 yourself before you sign, given how much of your work you might route through there.

**The CONTRIBUTING branching table says target** . The engine has no branch — it has (updated Aug 11), (updated today), and a stale from May. The GUI does have , and PR \#6 targets it. So the doc is generic boilerplate applied to both repos, and the real PR target differs per repo. Ask Caleb once rather than guessing.

### The shape that works

The fork is your sync point. Not Dropbox, not a USB stick, not PC-to-PC remotes — every machine clones the same fork, and GitHub is the only place the truth lives.

Fork only the repos you actually modify. HydroCouple has ~40; you probably touch three or four. For the rest, a plain clone or just a watch is enough — a fork you never push to is a fork that silently rots and misleads you later about what's current.

Put the forks in one place and decide now, because you can only have one fork of a given repo per account or org and moving it later means a transfer. You already have holding the EPA fork; that's the natural home for the HydroCouple ones too — it keeps "Bob's engine forks" in one namespace and off your personal account.

**Don't rename the forks.** expects the engine at . GitHub Desktop clones into , so as long as the names stay stock and you set the *same clone root on every PC* ( or wherever), the sibling layout resolves identically everywhere. This is the single highest-value multi-PC habit here — a different root on one laptop means CMake configure fails there and nowhere else, and you'll spend an evening on it.

### Branch discipline — this is what keeps "my version" and "contribute back" from fighting

Branch Rule , , **Pristine mirrors.** Never commit here. Their only job is to be a clean base and a clean diff target. Your work, one topic per branch, branched off the mirror. Small and single-purpose. Optional. Merge of upstream + whichever branches you want in the build you personally run. **Never PR this branch.**

The moment you commit your own change onto a mirror branch, you lose the ability to answer "what did I change?" with a single , and syncing from upstream turns into conflict resolution forever. This is the same two-branch pattern you're already using for the LID work on the EPA fork — engine-only minimal diff for the PR, everything else on a branch that never goes upstream.

For a PR, follow their rules literally: branch off the target branch, name it or , write the failing test first, keep the diff minimal, add yourself to .

### Where GitHub Desktop helps and where it stops

It's fine for the daily loop — commit, push, branch switch, open PR, and it signs you in per machine with no key management. Two limits will bite you here:

It only knows how to sync from the **parent's default branch**. won't help you track or , which are exactly the branches that matter. And it has no UI for adding or fetching arbitrary remotes.

So do the initial wiring once per machine from :

After that, refreshing a mirror is , and Desktop handles the rest. The is the safety catch: if it refuses, you accidentally committed onto a mirror and you want to know immediately.

Alternatively the web UI's **Sync fork** button works per-branch when the branch exists on both sides — enough if you'd rather not touch the terminal, though you still need the initial branch creation above.

One small thing: Caleb's commits carry lines. GitHub Desktop won't add those. Nothing in CONTRIBUTING requires DCO today (the CLA covers it), but if that ever gets enforced in CI, is the only way to satisfy it.

### Following without drowning

Watching ~40 repos on "All Activity" will bury you. Use **Watch → Custom → Issues + Pull requests + Releases** on the three or four that matter, and skip the rest.

Better for your case — the branches move faster than the issues do, and Atom feeds track branches directly with no email:

That last one is Caleb's public activity across everything, which covers most of the org in a single feed. Drop them in any reader and you'll see the SWMM6 work land the day it lands, which is roughly how you found the GUI branch in the first place.
