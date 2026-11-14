---
title: "People of PySWMM and The Man Who Gave the Pipes a Python Voice"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/people-pyswmm-man-who-gave-pipes-python-voice-robert-dickinson-k1w5c
created: "2026-03-01 18:50"
published: "2026-03-02 14:27"
words: 2164
export_sha256: a2a5e871cd45b00bdc120e96b4a445ce077867e767dafd42bcff66c3b5f15463
---
# People of PySWMM and The Man Who Gave the Pipes a Python Voice

![People of PySWMM and The Man Who Gave the Pipes a Python Voice](https://media.licdn.com/mediaD5612AQGwdPlG7Vz5hg "People of PySWMM and The Man Who Gave the Pipes a Python Voice")

### The Man Who Gave the Pipes a Python Voice

*A brief history of how one engineer connected a fifty-year-old government program to the future of intelligent infrastructure or how SWMM5 was connected to Python Code (AI favorite)*

It is a peculiar feature of technological civilizations that their most critical infrastructure is also their most invisible (see a cutout of NYC for example). You do not think about the sewer beneath your street until it fails or stormwater until it floods. You do not contemplate the storm drain at the corner until it overflows onto your lawn or like me see it is clogged with leaves and you clean it. And you certainly do not consider the simulation model that an engineer used, fifteen years ago, to determine the diameter of the pipe that is, at this very moment, carrying last night's rainfall away from your house onto the street.

> **SWMM and Fortran Interlude**

But someone did think about it. Many someones, in fact, across fifty-five years and four computer languages and three complete rewrites of a program called SWMM — the Storm Water Management Model — which the United States Environmental Protection Agency first commissioned in 1969, the same year humans walked on the Moon.

The Moon walkers got a parade. The pipe modelers got a FORTRAN compiler and a government contract for three hundred and fifty thousand dollars. (See my other LI articles on the history of SWMM and links to what Wayne Huber says about the history of SWMM).

> **Back to Python and PySWMM**

This is not their story. Their story has been well told elsewhere. This is the story of what happened fifty years later, when a young engineer in South Bend, Indiana, looked at the model those pioneers had built and said, in effect: *"This is magnificent. But it doesn't talk to anything." That person is* **Bryant McDonnell.**

> **The Architecture of Isolation**

To understand what Bryant McDonnell did, you must first understand what he found.

By 2014, EPA SWMM was the most widely used stormwater simulation model on Earth. It could route rainfall through a thousand pipes, calculate surcharge in a hundred manholes, and predict flooding at a dozen outfalls — all in less time than it takes to drink a cup of coffee. It was, by any reasonable measure, a triumph of computational engineering.

It was also, by any reasonable measure, a hermit.

SWMM ran on your Windows desktop. It read an input file. It wrote an output file. It did not converse. It did not listen. It did not negotiate. You could not, while it was running, lean over and say: *"Excuse me — node J-47 is flooding. Would you kindly open pump P-3?"* The simulation had started. The simulation would finish. Your opinions were not welcome.

**Now Lew Rossman of the USEPA**

This was not a flaw. It was a feature — of 2004, when the model was rewritten in C by a brilliant EPA engineer named Lewis Rossman. Rossman, with an architect's foresight that would prove prophetic, designed the SWMM engine not as a sealed box but as a callable library — a DLL, in the parlance of Windows. Other programs could, in theory, invoke SWMM's functions. They could start a simulation, advance it, query its state, and modify its parameters.

In theory.

In practice, doing so required writing C code. You needed to understand memory allocation, pointer arithmetic, and the exact layout of SWMM's internal data structures. You needed, in short, to be the kind of person who enjoys reading other people's C header files for recreation. (I liked it)

There were perhaps two hundred such people in the world. There were two hundred thousand who needed what they could build.

> **The Problem That Demanded a Solution**

Bryant McDonnell had a reason.

He was working at EmNet, a small company in South Bend, Indiana, that did something most people didn't know was possible: it monitored live sewer systems in real time. Sensors in manholes. Flow meters in pipes. Data streaming to servers every five minutes. And when the data showed a storm was about to overwhelm the system — when combined sewage was about to overflow into the St. Joseph River — EmNet's algorithms would send commands to gates and pumps, rerouting flow to where capacity still existed.

This was, and remains, one of the most sophisticated applications of real-time control in municipal infrastructure. And it needed SWMM.

> **PySWMM**

Not SWMM the desktop tool. Not SWMM the input-file-in, output-file-out hermit. It needed SWMM the *engine* — callable, controllable, interruptible. It needed to run a simulation, pause at each timestep, look at the results, make a decision, change a pump setting, and continue. It needed SWMM to be a *participant* in a conversation, not a lecturer delivering a monologue.

McDonnell could have written the C code to do this. He was capable. But he was also practical — a Heinlein hero in a SF Asimov universe (Foundation) — and he knew that whatever he built for EmNet's control algorithms today would need to work with Python's data science libraries tomorrow. With numpy and pandas. With scikit-learn. With whatever machine learning framework was going to emerge next year and the year after that.

The C wall between SWMM and Python wasn't just inconvenient. It was a civilizational barrier. On one side: fifty years of hydraulic engineering knowledge, encoded in a hundred thousand lines of validated C code. On the other side: the entire modern ecosystem of scientific computing, artificial intelligence, and data analysis.

Between them: a DLL that technically allowed communication but practically demanded a translator.

> **McDonnell decided to be the translator.**

### Eight Lines That Changed a Profession

PySWMM — the Python interface to SWMM — was not a large program. It was not a rewrite. It did not touch a single line of Rossman's C code. It used Python's\`ctypes\` library to call the SWMM DLL's exported functions, wrapping each one in a Pythonic interface that any graduate student could understand.

The result looked like this:

Eight lines.

In eight lines, a Python programmer — who might never have heard of the Saint-Venant equations, who might not know a Preissmann Slot from a mail slot — could run a SWMM simulation with real-time control logic. Open the pump when the water gets deep. Close it when the water recedes. Watch what happens.

In the previous era, this would have required several hundred lines of C, a working knowledge of SWMM's internal memory layout, and approximately three weeks of debugging.

**The Connection Machine**

But PySWMM was not merely a simplification. A simplification makes the same thing easier. PySWMM made *new things possible*.

Consider what it connected:

On one side of the bridge: SWMM — a validated, peer-reviewed, FEMA-approved hydraulic engine trusted by regulatory agencies in a hundred and sixty countries.

On the other side: *everything else.*

Numpy. Pandas. Matplotlib. Scikit-learn. TensorFlow. PyTorch. GeoPandas. Jupyter. Docker. Kubernetes. AWS. Azure. GitHub Actions. Every optimization algorithm. Every machine learning framework. Every data visualization tool. Every cloud computing platform.

PySWMM didn't just give SWMM a Python interface. It gave SWMM *citizenship in the 21st century computational ecosystem.* A model born on CDC 6400 mainframes, raised on IBM PCs, and matured on Windows desktops was suddenly available to a data scientist running Jupyter notebooks on a MacBook in a coffee shop in Singapore.

The consequences were immediate and profound.

A researcher at the University of Michigan trained a **reinforcement learning agent** to control a stormwater system — the AI learned to operate gates and valves by running thousands of PySWMM simulations, the same way AlphaGo learned to play Go by playing millions of games against itself. The drainage system became the game board. PySWMM was the game engine.

A team at the University of Virginia built **swmm_rl** — a framework for applying reinforcement learning to any SWMM model. They published it as open source. Graduate students around the world downloaded it and began training AI agents to manage their local drainage systems.

Consulting engineers ran **ten thousand SWMM simulations overnight** — varying rainfall, soil parameters, pipe sizes — to find optimal designs. What had taken weeks of manual iteration now took a single Python script and a good night's sleep.

Climate scientists ran SWMM under **hundreds of future rainfall scenarios**, each derived from different global climate models, to estimate how urban drainage systems would perform in 2050. The batch processing that PySWMM enabled turned a single-scenario analysis into a full probabilistic assessment.

And in cities like Cincinnati and Columbus, Ohio, PySWMM-based control algorithms eliminated **tens of millions of gallons of combined sewer overflows annually** — not in simulation, but in the real pipes under real streets carrying real sewage.

The hermit had learned to talk. And it turned out it had quite a lot to say.

> **The Community**

McDonnell did not work alone, and he would be the first to tell you so.

He co-founded **Open Water Analytics** — OWA — as an organizational home for open-source water infrastructure tools. OWA maintained not just PySWMM but a community-maintained fork of the SWMM source code itself, a toolkit for reading SWMM's binary output files, and parallel efforts for EPANET (EPA's drinking water model).

**Gonzalo Peña-Castellanos** served as co-maintainer, keeping PySWMM alive through the inevitable valleys between peaks of the creator's attention — reviewing pull requests, managing releases, maintaining the continuous integration pipeline. Every open-source project needs someone who shows up on the boring Tuesdays. Peña-Castellanos was that person.

**Michael Tryby** at EPA provided the API enhancements in the official SWMM engine that PySWMM wrapped — new getter and setter functions that made it possible to read and modify simulation parameters that had previously been locked behind C-only interfaces.

**Katherine Ratliff**, **Jennifer Wu**, C Karos,and **Abhiram Mullapudi** contributed to the project's growth, documentation, and academic validation. The 2020 paper in the *Journal of Open Source Software* — McDonnell et al. — formalized PySWMM's place in the scientific literature.

**The Lineage**

Every great technological achievement stands on the shoulders of decisions made decades earlier by people who could not have imagined the consequence.

In 1969, **John Lager** at Metcalf & Eddy managed three competing firms into a collaboration that produced SWMM 1. He could not have imagined a Python wrapper.

In 1975, **Larry Roesner** and **Robert Shubinski** developed the EXTRAN dynamic wave solver — descended, improbably, from an estuary model — that gave SWMM the ability to simulate pressurized pipe flow. They could not have imagined a reinforcement learning agent operating their solver.

In 1980, **Robert Dickinson** at the University of Florida took over the SWMM codebase and maintained it through the PC revolution. He could not have imagined that code running in a web browser. It was 1980.

In 1988, **Chuck Moore** at CDM developed the RTK method for rainfall-derived infiltration and inflow. He could not have imagined ten thousand automated RTK calibration runs executing overnight on a cloud server.

In 2001, **Lewis Rossman** at EPA made the decision — the *critical* decision, the one that made everything else possible — to design SWMM 5 as a callable DLL. A shared library. An engine that other programs could invoke. He could not have imagined PySWMM specifically, but he *could* imagine that someone, someday, would want to call his engine from somewhere other than his GUI. So he made it possible.

And in 2014, in South Bend, Indiana, a young engineer who needed SWMM to talk to Python reached across the DLL boundary and **connected fifty years of hydraulic engineering to the future of computing.**

The Foundation, as it were, had been laid.

> **The Lesson**

There is a pattern here that extends far beyond drainage engineering, and I commend it to your attention.

The most transformative contributions to a technology are not always new features. They are not always faster algorithms or more accurate equations. Sometimes — perhaps most of the time — the most transformative contribution is a *connection*. A bridge between two worlds that did not previously communicate.

Rossman built the engine. McDonnell built the bridge.

The engine was necessary. The bridge was transformative.

If you are an engineer, a scientist, or a programmer reading this, the lesson is not "learn Python" — though you should. The lesson is: *look for the DLL.* Look for the powerful, validated, trusted tool that sits in isolation because nobody has bothered to connect it to the modern world. Look for the locked door with no lockpick.

Then build the lockpick.

The world is full of extraordinary engines waiting for someone to give them a voice.

> ***Bryant McDonnell, continues to build things that make pipes smarter. He can be found on GitHub.***

**\#PySWMM \#OpenWaterAnalytics \#SWMM \#WaterResources \#StormwaterManagement \#OpenSource \#Python \#Infrastructure \#DigitalTwins**
