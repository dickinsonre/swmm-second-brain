---
title: "Edition 53: The Measure of Honest Numbers, the app version of Rules for Responsible Modeling by William James (CHI)"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/measure-honest-numbers-app-version-rules-responsible-james-dickinson-fdjxc
created: "2026-02-22 18:29"
published: "2026-02-23 15:13"
words: 2118
export_sha256: 635fe23349a74d9bb929d5eb19d6a1b85251dffd59d91c2d3d96965d2d7a65ad
---
# Edition 53: The Measure of Honest Numbers, the app version of Rules for Responsible Modeling by William James (CHI)

![](https://media.licdn.com/dms/image/v2/D4E12AQHBow7-cAKBmw/series-logo_image-shrink_300_300/series-logo_image-shrink_300_300/0/1707065394509?e=1795651200&v=beta&t=tN-hhC1z9uquar5xA2f4iKHMUJauOcieSynf04B5KXc)

### EPASWMM5 Related Software Five decades with SWMM, still shipping code. SWMM5/6, ICM with Ruby, browser apps that teach the engines — and the art

![The Measure of Honest Numbers, the app version of Rules for Responsible Modeling by William James (CHI)](https://media.licdn.com/mediaD4E12AQGvyInrKLOpQg "The Measure of Honest Numbers, the app version of Rules for Responsible Modeling by William James (CHI)")

> **The Measure of Honest Numbers**

It is a peculiar feature of the human mind that we are most easily deceived by things that look precisely the way we expect them to look. A forged painting fools the eye not because it is beautiful but because it contains exactly the right cracks in exactly the right places. A confidence man succeeds not by being extraordinary but by being perfectly, unremarkably ordinary. And a mathematical model of a storm sewer network achieves its most dangerous state not when it fails spectacularly, producing nonsense that any first year engineer would reject, but when it succeeds just a little too well, producing a hydrograph that matches the observed data with the serene perfection of a thing that has learned to tell you what you want to hear. (AI sometimes in 2026 as well)

> **Overfitting your model**

There is a name for this in the modeling profession, it is called overfitting. The phenomenon is well understood in the abstract and persistently ignored in practice. A model with enough adjustable parameters can be made to fit any dataset. This is not a sign of understanding. It is a sign that the model has memorized the noise in your calibration data along with the signal, the way a student who memorizes the answer key can ace the test without comprehending the subject. Ask that student a question that was not on the test and you discover, too late, that no learning occurred.

> **Famous Bill James's in Recent History**

I learned to recognize this particular species of deception from a Canadian (South Afirican)( engineer named William James. Not the baseball sabermetic or philosopher and psychologist. A different William James, one who spent his career in the less glamorous but considerably more consequential field of computational hydraulics. James understood, earlier than most and more clearly than almost anyone, that the central challenge of hydrological modeling is not computational power or algorithmic sophistication or software capability. The central challenge is honesty. Honesty about what your data can support. Honesty about what your model cannot know. Honesty about the gap between the number the computer produces and the confidence you are entitled to place in that number.

> **How I met the PCSWMM Bill James**

I first met Bill James in 1978 when he came to the University of Florida with Mark Robinson to teach a class on SWMM 2. To appreciate what this involved, you must understand the technological landscape of 1978. Personal computers did not exist in any form a modern engineer would recognize. James had, through some combination of resourcefulness and audacity, arranged to run SWMM 2 on a Boeing mainframe computer located in Seattle, Washington. We had thirty students sat in a classroom in Gainesville, Florida, and connected to that distant machine through a 4k modem. For those too young to know what this means, a 4k modem transmits data at roughly one ten thousandth the speed of a modern cell phone connection. Thirty people sharing that single thread of bandwidth meant that submitting a job and receiving results was an exercise in patience that would test a Buddhist monk. Not to mention that your cell phone now would run rings around the Boeing super comptuer.

> **Punch Cards, Giant reams of paper output from SWMM 2.5**

The output, when it finally arrived, came on massive continuous feed paper printouts. Green bar paper, we called it, printed in that distinctive dot matrix typeface that future generations will never see (lucky you) The printouts folded into accordion stacks that could reach three feet tall. You carried your model results home like cordwood. You spread them across the floor of your apartment and crawled along on hands and knees, scanning row after row of numbers, looking for the one line buried on page forty seven that told you whether Junction 12 had flooded or not.

> **Bill James Pushing Continuous Simulation even in the 70s**

And yet. Even in that primitive arrangement, with thirty people sharing one wheezing modem connection to a computer two thousand miles away, James was asking questions that the rest of us would not think to ask for another decade. He talked about data reliability while we were still learning how to keypunch input cards without putting a decimal point in the wrong column. He discussed the difference between calibration and validation while we were still celebrating the fact that the model ran to completion without aborting. He raised the subject of uncertainty quantification while we were still trying to figure out what the numbers meant at all.

In those days you submitted your input on punch cards. Eighty columns per card. One character per column. One error in column 47 of card 312 and the entire run failed, and you would not find out until the next morning when the printout arrived and informed you, on page one, that your data contained a format error, please resubmit. The turnaround time for a single model run could be twenty four hours. You learned to check your work meticulously, because the cost of a mistake was not a five second delay. It was a lost day

> **A thinker even with poor computing tools**

He was, in the way that matters most, ahead of his time. Not ahead in the sense of having access to better technology. He had worse technology than almost anyone. Ahead in the sense of asking better questions. The questions that determine whether a model is a tool for understanding or a machine for generating false confidence.

> **A developer of PCSWMM in 1983**

I was also one of the first people to use PCSWMM when it became available in 1983. I still have that original copy, though I confess the floppy disks it arrived on would require archaeological equipment to read today. Running SWMM on a personal computer for the first time felt like a small revolution. You could submit a run and get results in minutes instead of hours. You could change a parameter and immediately see the effect. You could iterate. You could explore. The mechanical friction between having an idea and testing it shrank from a day to an afternoon to an hour. He and Mark Robinson even had an Expert system to quiz you on the width parameter of SWMM 3.

> **Rules for Responsible Modeling.**

But the fundamental questions James had posed in that classroom in 1978 did not change with the technology. They became, if anything, more urgent. Because the easier it became to run models, the easier it became to run them carelessly. The faster the turnaround, the less time anyone spent thinking about whether the inputs justified the outputs. The prettier the graphics, the more convincing the results appeared, regardless of whether the underlying data supported three significant figures or barely one.

In 2005, James published the distillation of everything he had learned. He called it Rules for Responsible Modeling. Three hundred and three pages covering seventeen chapters on everything from the reliability of input data to the mathematics of fuzzy logic to the ethical obligations of an engineer who reports a number knowing that someone will spend public money based on that number. It addressed optimal complexity, the idea that a model should be as simple as possible but not simpler, which sounds like common sense until you watch an engineer build a five hundred subcatchment model calibrated against two rain gauges and call it thorough. It addressed sensitivity analysis, the practice of determining which parameters actually matter, which sounds obvious until you realize that most project schedules do not include time for it. It addressed the most uncomfortable topic of all, uncertainty disclosure, the professional obligation to tell your client not just what the model predicts but how much confidence that prediction deserves.

It was the most important book in our profession. It was also a PDF. And it suffered the fate of most PDFs, which is to be downloaded once, filed in a folder called Reference Material, and never opened again.

> **Why I made this App**

The problem was never the ideas. James's ideas were and remain correct. The problem was the delivery mechanism. A working engineer with a project deadline and a model that is producing continuity errors does not have twelve hours to read a book. They need the specific chapter that addresses their specific problem, delivered in a format that respects the reality of their Tuesday afternoon.

So I built an interactive edition. It lives at [**rulesforresponsiblemodeling.lovable.app**](http://rulesforresponsiblemodeling.lovable.app/), and it does something the PDF never could. It makes the wisdom findable and searchable.

> **Guided Pathways**

There are four guided pathways through the material. A student path that builds foundational understanding over eight to ten hours. A practitioner review that covers the essential rules in four to five hours for those who have been modeling for years and need a structured refresher. An ethics and uncertainty deep dive for those who present results to stakeholders who make decisions based on numbers they cannot independently verify. And a comprehensive journey through all seventeen chapters for those building deep expertise.

There is a diagnostic tool that works the way an engineer thinks. You do not start with a chapter number. You start with a problem. My calibration looks overfit. My model does not match observed flows. I cannot quantify the uncertainty in my results. My client does not understand what my output means. You describe your symptom and the application delivers the relevant rules, the pertinent chapters, and the common mistakes to avoid. It is, in effect, a consultation with William James, available at any hour, on any device.

There is a checklist generator that converts philosophy into procedure. Select your project phase. Scoping, building, calibrating, or reporting. The application generates a customized forty item checklist, each item traceable to a specific rule in James's framework. Download it. Print it. Use it as a gate. No model leaves the office until the checklist is satisfied.

> **Templates**

There are downloadable templates. A model scoping report that forces you to define your objectives and inventory your data before you build anything. A calibration and validation log that distinguishes between the two, which is critical because James was emphatic that they are not the same thing. An uncertainty disclosure template that provides a professional format for telling your client the truth about what the model can and cannot predict.

**I do mention SWMM5 and ICM**

Here is the thing about responsible modeling that James understood and that fifty years of practice have confirmed for me personally. The model is never the problem. SWMM 5 solves the Saint Venant equations correctly. InfoWorks ICM solves them correctly. The mathematics is sound. The numerical methods are stable. The software does what it is told.

The problem is what it is told. The problem is the human being who selects the data, chooses the complexity, adjusts the parameters, interprets the output, and writes the report. The problem is the human being who, under deadline pressure, skips the validation run because the calibration looked good enough. The problem is the human being who reports six decimal places because the computer generated six decimal places, not because the physics supports six decimal places.

James wrote the rules to protect that human being from the consequences of haste and overconfidence. I built the application to make the rules available at the moment they are needed most, which is always Tuesday afternoon, with the deadline approaching and the model misbehaving.

> **Link**

The interactive edition is free and available now at [**rulesforresponsiblemodeling.lovable.app**](http://rulesforresponsiblemodeling.lovable.app). Seventeen chapters. Four learning pathways. A diagnostic tool. A checklist generator. Templates for every phase of a modeling project. And a weekly reminder that the most dangerous model is not the one that fails. It is the one that succeeds too perfectly, and is believed.

The water, as always, does not care what the model predicted. It flows according to physics, not according to our spreadsheets. James wanted to close the gap between the two. The least we can do is read the rules.

[https://rulesforresponsiblemodeling.lovable.app/](https://rulesforresponsiblemodeling.lovable.app/)
