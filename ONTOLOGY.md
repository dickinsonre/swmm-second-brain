# Ontology: typed relations for the wiki (draft)

A wiki link says "see also". A relation says how two things are related: `icm-iw:DEPNOD` *reports* water level, `ruby:3.4.6` *replaces* `ruby:2.4.0`. This file defines the small vocabulary the wiki uses for that, and how a page writes it down. `tools/ontology.py` reads every page's Relations table and writes the result as RDF into `ontology/`, where any RDF tool can query it.

Status: a draft, started 16 November 2026 after Caleb Buahin asked whether the wiki could have a formal ontology. Tried first on the ICM and Curve Number pages. The same day it was tightened in three ways that ChatGPT suggested when Bob showed it the draft: conditions a query can read, a check of what each relation can connect, and `unknown` where a source names no drafter, with a `verification` status for claims that depend on a run. Bob and the agent change this file together, like `CLAUDE.md`; every change gets a line in `log.md`.

## What a relation is, and is not

A relation restates, in a form a program can read, something the page already says with a citation. It adds no fact. Page rule 1 applies to every row: no source, no row. The statement is filed under each source it cites, so a query can ask which facts rest only on an AI-drafted note or on a page Bob has not reviewed.

## How a page writes relations

At the end of a page, a paragraph that is just `**Relations**`, then a table:

```
**Relations**

| Subject | Relation | Object | Note | Source |
|---|---|---|---|---|
| `icm-iw:DEPNOD` | `reports` | `qty:WaterLevel` | level at the current timestep | [S163](../sources/S163-note-icm-results-field-crosswalk.md) |
```

- **Subject, Object:** one or more term IDs in backticks, separated by commas, or a link to a wiki page. A row with two subjects and three objects states six relations.
- **Relation:** one name from the table below, in backticks.
- **Note:** optional. The condition, rule or caution that goes with the statement; it travels with it into the RDF. Conditions and evidence that a query should read go in as qualifiers (below).
- **Source:** one or more source page links. Required.
- **Term IDs** are `prefix:Name`. Keep the program's own spelling (`icm-iw:hw_node`, `icm-iw:DEPNOD`); otherwise use CamelCase (`qty:WaterLevel`). Letters, digits and `_ . -` only. A term needs no separate declaration: its label is its name, with CamelCase split into words.
- A class named as the object of `is_a` must be in the Classes table below.
- A term used by a relation whose subject or object must be of a class (see Relations) needs an `is_a` row somewhere in the wiki.

## Prefixes

| Prefix | IRI | Holds |
|---|---|---|
| `sb` | https://github.com/dickinsonre/swmm-second-brain/ontology# | this vocabulary: its relations and classes |
| `swmm5` | https://github.com/dickinsonre/swmm-second-brain/ontology/swmm5/ | EPA SWMM 5: objects, methods, source files, releases |
| `icm` | https://github.com/dickinsonre/swmm-second-brain/ontology/icm/ | InfoWorks ICM as a program: releases, Exchange, the Ruby API, licenses |
| `icm-iw` | https://github.com/dickinsonre/swmm-second-brain/ontology/icm-iw/ | things of an InfoWorks network: tables, result fields, 2D objects, infiltration types |
| `icm-swmm` | https://github.com/dickinsonre/swmm-second-brain/ontology/icm-swmm/ | things of an ICM SWMM network |
| `qty` | https://github.com/dickinsonre/swmm-second-brain/ontology/qty/ | physical quantities, independent of any program |
| `ruby` | https://github.com/dickinsonre/swmm-second-brain/ontology/ruby/ | Ruby runtimes |
| `fso` | https://w3id.org/fso# | the Flow Systems Ontology, an outside vocabulary for flow systems ([S191](wiki/sources/S191-paper-kukkonen-2022-flow-systems-ontology.md)); no row uses it yet |

Wiki pages are not written with a prefix; they are links, and become `https://github.com/dickinsonre/swmm-second-brain/blob/main/wiki/<path>`, which opens the page on GitHub.

## Relations

| Relation | Means | Standard property | Subject must be | Object must be |
|---|---|---|---|---|
| `is_a` | the subject is an instance of the class named by the object | `rdf:type` | | a class below |
| `part_of` | the subject belongs to the object | `dcterms:isPartOf` | | |
| `same_as` | the same thing under another name, with no caveat | `skos:exactMatch` | same | same |
| `close_match` | nearly the same; the condition or note says how they differ | `skos:closeMatch` | same | same |
| `approximates` | stands in for the object, under the conditions given | `skos:relatedMatch` | same | same |
| `reports` | a result field reports this quantity | | `sb:ResultField` | `sb:Quantity` |
| `derived_from` | computed from the object; the note gives the rule | `prov:wasDerivedFrom` | | |
| `has_parameter` | the method or object takes this input | | | `sb:Parameter` |
| `stored_in` | its data are kept in this table | | | `sb:DataTable` |
| `available_in` | available from this release on | | | `sb:Release` |
| `replaces` | takes the place of the object | `dcterms:replaces` | same | same |
| `requires` | needs the object to run or to apply | `dcterms:requires` | | |
| `translation_of` | a translation of the object into another programming language | `prov:wasDerivedFrom` | `sb:Program` | `sb:Program` |
| `finding_about` | a finding whose subject is the object | `dcterms:subject` | | |

`is_a` is written out as `rdf:type` itself. Every other relation becomes `sb:<name>`, declared a sub-property of the standard property where the table names one, so a tool that knows SKOS, PROV or Dublin Core but not this file still understands most of it.

**What each relation can connect.** The last two columns are checked by `tools/lint.py`. A class there means the term must be declared that class by an `is_a` row somewhere in the wiki; "same" means the subject and the object must share a class; empty means anything. A term that a checked relation uses must therefore have an `is_a` row. So `icm-iw:DEPNOD` `reports` `icm:2027.0` is an error: `icm:2027.0` is a Release, not a Quantity.

**`same_as` or `close_match`.** `same_as` maps to SKOS `exactMatch`, which is transitive: if A matches B and B matches C, a reasoner concludes A matches C. Use it only when the two are interchangeable with no caveat. A field mapping that needs a condition (a common datum, a unit change, a sign convention) is a `close_match`, and the condition goes on the row.

## Classes

| Class | Means |
|---|---|
| `sb:Program` | a modeling program or engine |
| `sb:Release` | a numbered release of a program |
| `sb:NetworkType` | a kind of model network inside a program |
| `sb:DataTable` | a database table of model data |
| `sb:ResultField` | a named result a program reports |
| `sb:Quantity` | a physical quantity |
| `sb:InfiltrationMethod` | a method for computing infiltration |
| `sb:Parameter` | an input a method or object takes |
| `sb:Setting` | an option a user sets on an object or run |
| `sb:ApiMethod` | a method of a scripting interface |
| `sb:RubyRuntime` | a Ruby interpreter version |
| `sb:License` | a license level of a program |

## Qualifiers: conditions and evidence on a statement

A row's Note may carry qualifiers, each written in backticks as `` `key: value` ``, with a space after the colon (which tells a qualifier from a term ID). They become properties of the statement itself, so a query can read them; the rest of the Note is kept as a comment. A qualifier states what the row's source says; like the rest of the row, it adds no fact.

| Key | Property | Holds |
|---|---|---|
| `condition` | `sb:condition` | the condition under which the statement holds (how a rate was set, a common datum) |
| `tested_on` | `sb:testedOn` | the models, storms or data it was tested on |
| `as_of` | `sb:asOf` | the date or release the statement describes |
| `verification` | `sb:verification` | what backs it: one of the three values below |

| `verification` | Means |
|---|---|
| `run` | a source reports a run of the program that shows it |
| `pending` | it depends on a run of the program that has not been made |
| `documented` | a source reports the program's documentation saying so; not checked against the program |

Example, from the 2023 Curve Number tests:

```
| `icm-iw:Horton2D` | `approximates` | `icm-iw:SubcatchmentCN` | `condition: a constant loss rate set by SQL from the CN peak infiltration rate, with simple hyetographs` `tested_on: 23 subcatchments whose IDs equal their CN; storms of 0.065, 0.65 and 6.5 in` `as_of: 2023, before CNSWMM on the mesh` `verification: run` peak and volume came close | [S177](...) |
```

**Comparisons must say what backs them.** A row with `same_as`, `close_match` or `approximates` needs a `verification` qualifier, and when it is `run`, a `tested_on` qualifier as well, so a query can keep run-backed comparisons apart from documented or pending ones. `tools/lint.py` reports a row without them as an error. Added 16 November 2026, after Grok's second review: "Keeping the `verification` and `tested_on` qualifiers mandatory on any comparison claim will stop the wiki from accumulating unverified statements that look like results."

A statement with a note or qualifiers is also written as an `rdf:Statement` that names its subject, relation and object and carries the qualifiers and comment.

**Who drafted a source, and whether Bob has read it.** Each source page's graph carries `sb:draftedBy` from its `drafted_by:` line, or `unknown` when the page has none; `sb:aiDrafted`, `yes` when that line begins with an AI's name, `no` when it names a person first, `unknown` otherwise; and `sb:reviewed` from its `reviewed:` line. So every statement can be traced to its source, to who or what drafted that source, to whether Bob has read it, and, through `verification`, to whether a run backs it.

## Outside vocabulary: the Flow Systems Ontology (proposed, not in use)

The Flow Systems Ontology (FSO) is a published vocabulary for the topology of flow systems: systems, components in eight classes, and directed flow relations such as `fso:feedsFluidTo` ([S191](wiki/sources/S191-paper-kukkonen-2022-flow-systems-ontology.md); page: [Flow Systems Ontology](wiki/concepts/flow-systems-ontology.md)). It was written for building HVAC and says nothing about drainage. Tying this wiki's network objects to its classes would let a query compare objects of SWMM 5, SWMM 6 and ICM by kind, for example every flow controller in a model and what each became in another program.

The table below is the wiki's proposal, written by Claude on 16 November 2026. Neither source states it: the left column quotes the EPA manual ([S60](wiki/sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md)), the middle column FSO ([S191](wiki/sources/S191-paper-kukkonen-2022-flow-systems-ontology.md)). No Relations table uses it until Bob accepts it (Q98). When he does, it needs a way to say "is a kind of", which the relation list above does not have yet (`rdfs:subClassOf` would be the standard property).

| SWMM 5 object, as S60 describes it | Proposed FSO class, as S191 defines it | Doubt |
|---|---|---|
| Conduit | `fso:Segment`, "a component used to enable the passage of mass or energy" | none seen |
| Junction, "a manhole, a fitting, a confluence" | `fso:Fitting`, used "to connect segments to other segments, or to other components" | a junction can hold ponded water when it floods (S60), so it is more than a connector |
| Storage unit, "the only node with storage volume and surface area" | `fso:StorageDevice` | none seen |
| Outfall, the terminal node that sets the downstream boundary | `fso:Terminal`, "a device through which a system interacts with the environment" | none seen |
| Flow divider | `fso:Fitting` or `fso:FlowController` | it splits flow by a rule, so it is neither a plain fitting nor an adjustable controller |
| Pump | `fso:FlowMovingDevice` | none seen |
| Orifice, weir, outlet (flow regulators with a setting) | `fso:FlowController` | none seen |

Direction: a link's defined direction runs from its inlet node to its outlet node, and flow can run against it. A row `swmm5:C1 fso:feedsFluidTo swmm5:J2` would have to say which it means.

## The test question

Every addition to this vocabulary should help answer: **which fields can I compare across InfoWorks and ICM SWMM networks, under what conditions, and what evidence supports the comparison?** `ontology/queries/5-comparable-fields.rq` asks it.

## What `tools/ontology.py` writes

| File | Holds |
|---|---|
| `ontology/second-brain.trig` | RDF in TriG: the vocabulary and labels in the default graph, and one named graph per source page holding the statements that cite it |
| `ontology/second-brain.jsonld` | the same, as JSON-LD |
| `ontology/relations.csv` | one row per statement: subject, relation, object, note, sources, page |
| `ontology/graph.md` | the statements as a Mermaid diagram, which GitHub draws |
| `ontology/queries/*.rq`, `*.txt` | sample SPARQL queries and their results, written by `--check` |

Each source page's graph carries its title, date, kind, author, `drafted_by:` (or `unknown`) and `reviewed:` from its front matter, so provenance can be queried.

```sh
python3 tools/ontology.py           # build ontology/ (standard library only)
python3 tools/ontology.py --check   # also parse the output and run the sample queries (needs rdflib)
```

`tools/lint.py` runs the same parser and reports as an error: an unknown relation, prefix, class or qualifier; a `verification` value not in the list; a relation connecting terms of the wrong class; a term a checked relation uses that has no `is_a`; or a row with no source.

## Not done yet

- Most pages have no Relations table; the first are `icm-tables-and-result-fields`, `icm-2d-rainfall-and-infiltration` and `icm-ruby-ui-and-exchange`.
- No link yet to outside vocabularies for units or hydrologic features. For network objects, an alignment to the Flow Systems Ontology is proposed above and waits for Bob (Q98).
- No `contradicts` relation yet for the open questions.
- `verification` is on the rows where a page says what backs the claim; a row without it says nothing either way, and queries show it as `not stated`. A `documented` or `pending` row becomes `run` only when a run is made and filed as a source (Q90).
