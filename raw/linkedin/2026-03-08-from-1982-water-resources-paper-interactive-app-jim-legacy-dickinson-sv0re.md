---
title: "From a 1982 Water Resources Paper to an Interactive App: Honoring Jim Heaney's Legacy Through Game Theory and Fair Cost Allocation"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/from-1982-water-resources-paper-interactive-app-jim-legacy-dickinson-sv0re
created: "2026-03-08 22:19"
published: "2026-03-08 22:46"
words: 1742
export_sha256: 1b254b1cf70aa177d1aaf7136063d57e9cdc47de0756156d5e466f62685fc990
---
# From a 1982 Water Resources Paper to an Interactive App: Honoring Jim Heaney's Legacy Through Game Theory and Fair Cost Allocation

![From a 1982 Water Resources Paper to an Interactive App: Honoring Jim Heaney's Legacy Through Game Theory and Fair Cost Allocation ](https://media.licdn.com/mediaD4E12AQG4PaT45UCNuQ "From a 1982 Water Resources Paper to an Interactive App: Honoring Jim Heaney's Legacy Through Game Theory and Fair Cost Allocation ")

### From a 1982 Water Resources Paper to an Interactive App: Honoring Jim Heaney's Legacy Through Game Theory and Fair Cost Allocation

> **A Personal Loss and a Professional Tribute**

On August 24, 2024, the water resources engineering community lost one of its most influential figures. **James Patrick "Papa" Heaney** passed away at the age of 84 in Newberry, Florida. Jim was a devoted husband, father, grandfather — and one of the most creative minds I ever worked with.

I first met Jim Heaney in 1976 at the University of Florida (he was teaching a water resources class - there is an interesting anecdote about that) .I really started working with him in 1977 in another class and later on side on his ideas about applying game theory to water resources. What followed was one of the great experiences of my life ad I explored game theory for the first time. The 1977 works lead to a paper he wrote in 1982. Jim was nice enough to make me a co-author the 1982 paper published in *Water Resources Research*: This interactive app is that paper.

**"Methods for Apportioning the Cost of a Water Resource Project"** James P. Heaney & Robert E. Dickinson *Water Resources Research*, Vol. 18, No. 3, pp. 476–482, June 1982

> **Methods for Apportioning the Cost of a Water Resource Project**

That paper explored how cooperative game theory — specifically the **Shapley Value**, the **Core**, the **Nucleolus**, and what we called the **MCRS (Minimum Costs, Remaining Savings) method** — could provide mathematically fair solutions to the problem of splitting shared infrastructure costs among multiple participants. The work grew out of real questions facing water resource projects with multiple beneficiaries: How do you divide costs so that every participant is better off cooperating than going alone, and no group has an incentive to break away?

Forty-three years later, I've turned that paper into an interactive web application.

**Live app:** [https://heaneywrr1982.lovable.app/](https://heaneywrr1982.lovable.app/)

> **The Paper's Core Question**

The problem is deceptively simple: Three towns — Riverside, Hilltop, and Lakeview — share a reservoir. Building separately would cost them \$12 million total. Building together costs \$7 million. That's \$5 million in savings. But how do you split the \$7 million fairly?

"Just divide it equally" ignores that the towns have different standalone costs and contribute differently to the savings. "Make each pay their standalone cost" removes any incentive to cooperate. Jim's insight, building on decades of game theory from Lloyd Shapley, Howard Raiffa, and David Schmeidler, was that **cooperative game theory provides principled answers** — answers that are stable (no group wants to leave), efficient (total costs are recovered), and fair (each participant pays according to their contribution).

Our 1982 paper compared several methods and proposed the MCRS approach as an improvement over the widely-used SCRB (Separable Costs, Remaining Benefits) method. The key contribution was showing that MCRS uses actual Core boundaries rather than nominal bounds, ensuring the allocation always lies within the stable region.

> **The Shapley Value: From 1953 to 2026 AI**

Here's something that still astonishes me. The **Shapley Value** — the same mathematical concept Jim and I were applying to water resource cost allocation in 1977 — has become one of the foundational tools in modern artificial intelligence.

Lloyd Shapley introduced his value in 1953 as a way to fairly allocate gains among players in a cooperative game. In 2012, Shapley shared the Nobel Prize in Economics for this and related work. But the Shapley Value's second life began when machine learning researchers realized it could solve a completely different problem: **explaining how AI models make decisions**.

**SHAP (SHapley Additive exPlanations)**, developed by Scott Lundberg and Su-In Lee, uses the Shapley Value to decompose any machine learning prediction into contributions from each input feature. When a neural network predicts flood risk, SHAP tells you: "Rainfall contributed 40% to this prediction, imperviousness contributed 25%, slope contributed 20%..." — exactly the way the Shapley Value tells you each town's fair share of the reservoir cost.

The mathematical structure is identical:

In cost allocation: What is each participant's average marginal contribution to every possible coalition?

In AI terms: What is each feature's average marginal contribution to every possible subset of features?

SHAP is now used across every industry that deploys AI — healthcare, finance, environmental modeling, autonomous systems. Recent research (2025) has applied SHAP specifically to **water quality prediction**, using it to explain which parameters most influence Water Quality Index forecasts.

Jim would have been fascinated by this. As his colleague Wayne Huber wrote in his memorial tribute: *"Jim was one of the earliest to become captivated by the possibility of Lotus 1-2-3 for solving engineering problems. He would have loved the current AI environment."* Jim always saw the connection between mathematical elegance and practical engineering tools. The fact that our 1977 work on fair cost allocation shares its mathematical DNA with the tools now explaining AI decisions worldwide is a testament to the enduring power of the ideas he championed.

> **The Interactive App**

The app at [https://heaneywrr1982.lovable.app](https://heaneywrr1982.lovable.app) transforms our 7-page academic paper into an interactive learning experience:

> **What You Can Do**

**Calculate cost allocations** using four methods (SCRB, Shapley Value, Nucleolus, Equal Split) for 3- or 4-player scenarios

**Visualize the Core** on a triangular barycentric coordinate plot — drag allocation points and watch them turn red when they leave the stable region

**Step through every calculation** transparently: all 6 Shapley permutations, the SCRB decomposition, the Nucleolus iteration

\- **Compare methods side-by-side** with five chart modes (grouped, stacked, pie, radar, comparison)

**Build the Core step by step** in Story Mode, adding constraints one at a time to understand why stability matters

**Test your understanding** with quizzes that use live calculator data

**Load real-world scenarios**: the Three Towns reservoir, airport runway cost sharing, factory pollution cleanup, and an "Empty Core" game where no stable allocation exists

> **The Pedagogical Design**

The app uses four layers of progressive disclosure:

1\. **First-Time Experience** — A narrative walkthrough introducing the Three Towns problem

2\. **Onboarding Tour** — Interactive demo of the Core visualization with clickable constraints

3\. **Story Mode** — Step-by-step construction of the Core with embedded quiz checkpoints

4\. **Active Learning Challenges** — Questions that use the current calculator state, not memorized facts

The Core visualization — where you can drag Shapley, SCRB, and Nucleolus points and see whether they're stable — is the feature I'm most proud of. It makes tangible what the paper could only describe in equations: **the geometric space where cooperation holds together**.

> **A Glossary of the Field**

The app includes a searchable glossary covering all the key terms: subadditivity, characteristic functions, imputations, coalition rationality, individual rationality, the Core, marginal contributions, separable costs, excess, and the grand coalition. Each term links to the relevant section of the calculator.

> **Jim Heaney's Broader Legacy**

Our 1982 cost allocation paper was just one facet of Jim's extraordinary career. He was a co-author on **SWMM1, SWMM2, and SWMM3** — the foundational versions of the EPA's Storm Water Management Model that I've spent the last 50+ years working with. Jim and Wayne Huber, starting at the University of Florida in 1967, created stormwater software that remains in active use nearly 60 years later. I documented Jim's role in my \[SWMM History app\]([https://swmm5.org](https://swmm5.org)), where he appears as one of the key contributors across multiple SWMM generations.

Jim's Google Scholar page lists **253 citations** spanning water system optimization, stormwater management, cost allocation, and urban water infrastructure. His most-cited paper, "Robust water system design with commercial intelligent search optimizers" (1999, 144 citations), showed his lifelong ability to bring cutting-edge mathematical tools to practical water engineering problems.

The paper that became this app has been cited in research on renewable energy cooperatives, transboundary water treaties, wind-solar-hydro hybrid generation systems, and supply chain cost sharing. The ideas Jim and I explored in 1977-1982 continue to inform how the world allocates shared resources.

> **Why I Built This**

I've spent 50+ years in water modeling — from the early SWMM3 days through InfoSWMM, XPSWMM, and now Autodesk's InfoWorks ICM. Building interactive apps that preserve and teach the foundational knowledge of our field has become a central part of my work. . Apps like this one capture the ideas and the people behind them.

> **James Heaney and AI (early interest in expert systems)**

Jim didn't get an extended chance to use AI. He built some early expert systems in Spreadsheets (Lotus 123 in the 80s) But I wanted to make sure his ideas live on in a format that the next generation of water engineers can discover, explore, and apply. When a young engineer opens this app and drags the Shapley Value point across the Core triangle, they're engaging with the same mathematics that Jim and I worked through by hand in Gainesville in 1977 — and the same mathematics that now powers explainable AI worldwide.

Building this app is my way of saying: **Remember the good man that he was and all the great memories. He and Wayne Huber were a water resources modeling team at UF that complemented each other wonderfully,**

> **Try It Yourself**

🔗 **Interactive App:** \[[https://heaneywrr1982.lovable.app\](https://heaneywrr1982.lovable.app)](https://heaneywrr1982.lovable.app%5D(https://heaneywrr1982.lovable.app))

📄 **Original Paper:** Heaney, J.P. and Dickinson, R.E., 1982, "Methods for Apportioning the Cost of a Water Resource Project." *Water Resources Research*, 18(3): 476–482.

🕊️ **Jim Heaney's Memorial:** \[Williams-Thomas Funeral Home\]([https://www.williamsthomasfuneralhome.com/obituaries/James-Heaney-2/](https://www.williamsthomasfuneralhome.com/obituaries/James-Heaney-2/))

*Robert Dickinson is a water modeling technologist at Autodesk, the creator of* [*SWMM5.org*](http://SWMM5.org)*, and a 50-year practitioner in stormwater and flood modeling. He co-authored the SWMM4 User's Manual with Wayne Huber and the SWMM3 manual with James Heaney and Wayne Huber and has worked with every generation of EPA SWMM from version 2.5 to version 5.*

*\#WaterResources \#GameTheory \#ShapleyValue \#CooperativeGameTheory \#SWMM \#HydraulicModeling \#WaterEngineering \#CostAllocation \#AIExplainability \#SHAP \#InMemoriam \#JamesHeaney*
