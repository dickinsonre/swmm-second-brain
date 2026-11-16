# Ontology: typed relations for the wiki (draft)

A wiki link says "see also". A relation says how two things are related: `icm-iw:DEPNOD` *reports* water level, `ruby:3.4.6` *replaces* `ruby:2.4.0`. This file defines the small vocabulary the wiki uses for that, and how a page writes it down. `tools/ontology.py` reads every page's Relations table and writes the result as RDF into `ontology/`, where any RDF tool can query it.

Status: a draft, started 16 November 2026 after Caleb Buahin asked whether the wiki could have a formal ontology. Tried first on the ICM and Curve Number pages. Bob and the agent change this file together, like `CLAUDE.md`; every change gets a line in `log.md`.

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
- **Note:** optional. The condition, rule or caution that goes with the statement; it travels with it into the RDF.
- **Source:** one or more source page links. Required.
- **Term IDs** are `prefix:Name`. Keep the program's own spelling (`icm-iw:hw_node`, `icm-iw:DEPNOD`); otherwise use CamelCase (`qty:WaterLevel`). Letters, digits and `_ . -` only. A term needs no separate declaration: its label is its name, with CamelCase split into words.
- A class named as the object of `is_a` must be in the Classes table below.

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

Wiki pages are not written with a prefix; they are links, and become `https://github.com/dickinsonre/swmm-second-brain/blob/main/wiki/<path>`, which opens the page on GitHub.

## Relations

| Relation | Means | Standard property |
|---|---|---|
| `is_a` | the subject is an instance of the class named by the object | `rdf:type` |
| `part_of` | the subject belongs to the object | `dcterms:isPartOf` |
| `same_as` | the same thing under another name | `skos:exactMatch` |
| `close_match` | nearly the same; the note says how they differ | `skos:closeMatch` |
| `approximates` | stands in for the object, under the conditions in the note | `skos:relatedMatch` |
| `reports` | a result field reports this quantity | |
| `derived_from` | computed from the object; the note gives the rule | `prov:wasDerivedFrom` |
| `has_parameter` | the method or object takes this input | |
| `stored_in` | its data are kept in this table | |
| `available_in` | available from this release on | |
| `replaces` | takes the place of the object | `dcterms:replaces` |
| `requires` | needs the object to run or to apply | `dcterms:requires` |
| `translation_of` | a translation of the object into another programming language | `prov:wasDerivedFrom` |
| `finding_about` | a finding whose subject is the object | `dcterms:subject` |

`is_a` is written out as `rdf:type` itself. Every other relation becomes `sb:<name>`, declared a sub-property of the standard property where the table names one, so a tool that knows SKOS, PROV or Dublin Core but not this file still understands most of it.

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

## What `tools/ontology.py` writes

| File | Holds |
|---|---|
| `ontology/second-brain.trig` | RDF in TriG: the vocabulary and labels in the default graph, and one named graph per source page holding the statements that cite it |
| `ontology/second-brain.jsonld` | the same, as JSON-LD |
| `ontology/relations.csv` | one row per statement: subject, relation, object, note, sources, page |
| `ontology/graph.md` | the statements as a Mermaid diagram, which GitHub draws |
| `ontology/queries/*.rq`, `*.txt` | sample SPARQL queries and their results, written by `--check` |

Each source page's graph carries its title, date, kind, author, `drafted_by:` and `reviewed:` from its front matter, so provenance can be queried.

```sh
python3 tools/ontology.py           # build ontology/ (standard library only)
python3 tools/ontology.py --check   # also parse the output and run the sample queries (needs rdflib)
```

`tools/lint.py` runs the same parser and reports an unknown relation, an unknown prefix or class, or a row with no source, as an error.

## Not done yet

- Most pages have no Relations table; the first are `icm-tables-and-result-fields`, `icm-2d-rainfall-and-infiltration` and `icm-ruby-ui-and-exchange`.
- No link yet to outside vocabularies (units, hydrologic features). A later `close_match` to an outside IRI would do it.
- No `contradicts` relation yet for the open questions.
