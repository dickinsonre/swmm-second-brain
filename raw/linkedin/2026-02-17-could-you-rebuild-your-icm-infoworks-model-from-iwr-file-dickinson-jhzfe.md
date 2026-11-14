---
title: "Could you rebuild your ICM InfoWorks model from results (the IWR file) alone?"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/could-you-rebuild-your-icm-infoworks-model-from-iwr-file-dickinson-jhzfe
created: "2026-02-17 21:35"
published: "2026-02-17 23:30"
words: 1278
export_sha256: b7ee52949021a6795294f8ce3d3c7c00ab1be90c3b24b38901450b2ec0c4fe47
---
# Could you rebuild your ICM InfoWorks model from results (the IWR file) alone?

![Could you rebuild your ICM InfoWorks Model from results (the IWR file) alone?](https://media.licdn.com/mediaD4E12AQHHttplUzfewA "Could you rebuild your ICM InfoWorks Model from results (the IWR file) alone?")

*By Robert Dickinson • Autodesk Water Technologist •* [*SWMM5.org*](http://SWMM5.org)

Here's a question that stumped me today **"If all you had was the IWR results file, could you reconstruct the modeling network?"**

The question came from **Yi Jiang**, our Enterprise Business Architect at Autodesk Water, who holds a PhD from the University of Mississippi. It sounds simple enough. After all, the IWR file contains results for every node, every conduit, and every subcatchment in your model. But when you really dig into it—and I mean really pull it apart field by field—the answer is both humbling and illuminating.

So naturally, I did what any self-respecting 70-year-old who's been coding since 1974 does: I asked my AI coding partner Claude to help me build a forensic analysis tool. In Ruby. For ICM InfoWorks. With a dark-themed HTML dashboard. Because why not?

### The Short Answer

**~70+%**

of your network definition data would be **lost** if you only had the IWR file

![](https://media.licdn.com/dms/image/v2/D4E12AQHOB3dnsG3zFw/article-inline_image-shrink_1500_2232/B4EZxtikzxGsAU-/0/1771364306764?e=1795651200&v=beta&t=vt-nd7jnwFHCCHqfcmpp2MfI8kO8j8mULvglDPKx5AQ)

That number surprised me too. Let me walk you through why.

### What the IWR File Keeps

An IWR results file is a time-series archive. It's great at storing *what happened*—depths at nodes, flows through conduits, runoff from subcatchments, velocities, Froude numbers, and capacity usage. It also preserves element IDs and, critically, the upstream/downstream node connections for every link. So you know the topology—the skeleton of who connects to whom.

**What survives in the IWR:**

✅ Element identifiers (node IDs, link IDs, subcatchment IDs)

✅ Network topology (US/DS connectivity)

✅ Complete simulation time-series (depth, flow, velocity, head)

✅ A few inferable quantities (like gradient from flow behavior)

### What's Gone Forever

Now here's where it gets interesting—and a bit sobering. Everything that makes a model *a model* lives exclusively in the network definition. The IWR file has no idea what your pipes look like, where they are, or how they were designed. Let alone the actual geometry of the nodes.

![](https://media.licdn.com/dms/image/v2/D4E12AQEYAOAclWkVdQ/article-inline_image-shrink_1000_1488/B4EZxt6G4gGsAU-/0/1771370475513?e=1795651200&v=beta&t=6D0_KtubCYClxtFxKPGwPVi4MGc7b9WTfQquUflqKkk)

In other words, you'd know *that* 42 liters per second flowed through Conduit C-247 at 3:15 AM, but you wouldn't know whether C-247 was a 300 mm PVC pipe at 0.5% slope or a 1200mm brick egg-shape on a 30-year-old trunk main. That's a pretty important distinction.

> **The Tool: IWR Gap Analysis in Ruby for ICM Infoworks**

The Ruby script we built runs as a UI script inside ICM InfoWorks. It iterates through every element type — manholes, storage nodes, outfalls, conduits, pumps, orifices, weirs, subcatchments — and categorizes each field into one of three buckets:

🟢 **In IWR (direct)** — stored in the results file

🟡 **Inferable** — can be back-calculated from results with some assumptions

🔴 **Network-only (LOST)**—exists only in the network definition

It then generates a dark-themed HTML dashboard right inside ICM's view window, with stacked bar charts showing the recovery ratio per element type, a field-by-field breakdown with populated/blank counts from your actual network, and a reconstruction feasibility summary table.

For conduits alone—typically the biggest table in any sewer model—you keep 3 fields out of 17. That's an 76% information loss rate. For manholes, it's 90%. For subcatchments? A staggering 92%.

![](https://media.licdn.com/dms/image/v2/D4E12AQFjspqtt701Xw/article-inline_image-shrink_1500_2232/B4EZxt40VSH0AU-/0/1771370137419?e=1795651200&v=beta&t=xQmk3Drg2bnZ73ICbievaN85OZ7_7z2Wb1wz2nacEcI)

> **Why This Matters to You**

Yi's question isn't just an intellectual exercise. It touches on several real-world concerns that utilities and consultants face every day:

**Data portability:** When you move between platforms or hand a model to a new consultant, what actually transfers? If someone only sends you the results file thinking it's "the model," now you know what's missing.

**Disaster recovery:** If your model database gets corrupted and all you have is the last simulation's IWR output, can you rebuild? The answer is you can rebuild the skeleton but not the flesh.

**Archival strategy:** Utilities archiving old models need to think carefully about what they're preserving. Results without the network are like answers without the equation—interesting but not reproducible.

**Quality assurance:** Running this analysis on your own network is a great way to audit data completeness. The "populated vs blank" column in the report tells you how much of your network definition is actually filled in versus defaulted.

> **What You Could Infer**

Now, if you're an experienced modeler—and if you're reading this, you probably are—you might be thinking, "But Bob, I could back-calculate some of those parameters from the results!"

And you'd be partially right. From the hydraulic head time series, you could infer approximate inverts. From velocity and depth, you could estimate pipe sizes using Manning's equation (if you guess the roughness). From maximum pump flows, you could sketch a pump curve.

But here's what 50 years in the trenches has taught me: every one of those inferences requires assumptions, and assumptions compound. By the time you've back-calculated your way through a 5,000-conduit network, the accumulated uncertainty makes the "reconstructed" model useful only as a conversation starter, not a design tool.By the time you've back-calculated your way through a 5,000-conduit network, the accumulated uncertainty makes the "reconstructed" model useful only as a conversation starter, not a design tool.

![](https://media.licdn.com/dms/image/v2/D4E12AQHUhGzw25J7pg/article-inline_image-shrink_1500_2232/B4EZxt4cTBKoAU-/0/1771370044458?e=1795651200&v=beta&t=Y2ZQueY5EKyOSWqf_TqP-WpExSo-dgIj2Xc68XfN_F4)

### A Thank You

**This tool exists because Yi Jiang asked the right question.**

Yi is the Enterprise Business Architect at Autodesk Water, with a PhD from the University of Mississippi. The question—deceptively simple, architecturally profound—is exactly the kind of systems-level thinking that makes the difference between building software and building solutions. Thank you, Yi.

And a nod to Claude (Opus 4.6 in this instance), my AI coding partner, who turned this idea into a working Ruby script with a full HTML dashboard in about 20 minutes. This is what I mean by "vibe "coding"—having a creative idea and seeing it materialize almost as fast as you can describe it. At 70, after coding since punch cards (1974 to 1980), I can honestly say this is the most exciting era to be building tools though it does remind of using an Apple in 1981)

### Try It Yourself

The Ruby script is available for download and runs as a UI script in any ICM InfoWorks network. Open your network, run the script, and see for yourself what percentage of your model could survive a results-only world.

I'd love to hear what you find. What's the gap percentage for your networks? Does it change the way you think about archival and data exchange?

Drop your results in the comments 👇

> **Full script and details on our Innovye GitHub**

Here is a nano banana image of the code (I like to see a visual representation of the code)

\#SWMM \#HydraulicModeling \#InfoWorksICM \#WaterEngineering \#AutodeskWater \#RubyScripting \#VibeCoding \#DataPortability \#Stormwater \#DigitalTwin \#WaterInfrastructure \#ModelMigration

The Dickinson Canon • Robert Dickinson • [SWMM5.org](http://SWMM5.org) Autodesk Water Technologist • 51+ years with SWMM • TAC Chair, [CIMM.org](http://CIMM.org)
