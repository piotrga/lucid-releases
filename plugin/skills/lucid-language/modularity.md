# Modularity — organize a specification without accidental coupling

Use when splitting, extracting, or reorganizing Lucid files. For every material
requirement change, the wider-context and generalization analysis already
applies through [SKILL.md](SKILL.md) and [generalization.md](generalization.md).
A request to change one requirement does not authorize unrelated reorganization.

This reference organizes specification files. For a map of system modules and
their interactions, read [projections.md](projections.md). Contexts, consistency
boundaries, spec files, code modules, and deployment units are different concepts;
derive or record their mappings instead of equating them from matching names.

## Boundaries follow meaning

Give each file a coherent domain purpose. Keep requirements together when
understanding or changing one normally requires the others. Separate populations
of changing instances from stable definitions when this improves review;
small coherent contexts may remain together.

Shared definitions and laws can support several distinct domain types. Similar
fields, percentages of overlap, identical thresholds, or matching wording do
not establish that two entities are the same concept. Analyze operations,
laws, assumptions, and independent policy changes before unifying anything.
Do not merge entities into a bag of optional fields just to reduce repetition.

Stable definitions should not depend on volatile inventories. Prefer an
acyclic dependency structure and explicit references. A cycle is a signal to
inspect joint meaning or extract a shared concept, not automatic proof that
all affected domains must merge. Preserve necessary dependencies even when
they make a numerical metric worse.

## Analyze the candidate split

Inspect the overview, definitions, source file, references, consumers, and
analogous structures elsewhere in the spec. Use a broad inventory/search and
then read relevant constructs. Record any missing context. Propose a small
number of useful candidates instead of an arbitrary menu.

For each candidate assess:

| Check | Evidence |
|---|---|
| Purpose | A clear domain description for each file; natural conjunctions are allowed |
| Change locality | Concrete plausible changes and which files they affect |
| Reference integrity | All existing references resolve after the move |
| Dependencies | Known cycles and their meaning; stable definitions stay independent of volatile data |
| Vocabulary | Definition ownership and understandable imports/references |
| Preservation | Each original construct and its full body has an accounted-for destination |
| Generalization | Any shared definition has justified laws and preserves local distinctions |
| Reader navigation | A reader can locate a requirement and follow its dependencies without hidden context |

These combine mechanical checks with judgment. Do not call a forecast of
future edits deterministic or use arbitrary thresholds such as 70% co-change,
80% common fields, or a ban on the word "and".

Count cross-file references if useful, but treat the count as evidence rather
than a pass/fail gate. Splitting one coherent file may introduce legitimate
references where there were none. Evaluate their meaning and locality.

## Preserve whole constructs

Move an entity, role, set, or relation with its complete body. A collection's
items are not independent top-level blocks. Keep relations with the domain
they describe or with their instances when natural; shared endpoint types
alone do not dictate one file for all relations.

For a pure split, compare original and resulting constructs, including bodies,
conditions, defaults, examples, and rationale, not just names and signatures.
Each construct must appear exactly once unless duplication is explicitly part
of an agreed design. Changes in wording or generalization are separate semantic
operations and need their own meaning-preservation analysis.

If the project has a parser, run it and report actual results. Otherwise perform
explicit structural and reference checks and state that parsing was not verified.
The bundled syntax highlighter is not a parser. Preserve legacy forms according
to [language.md](language.md).

## Challenge the boundary

Consider where a realistic next requirement would belong. Try an independent
change in each domain and inspect whether the proposed abstraction forces
unrelated edits elsewhere. Compare merging candidate files back together: does
separation aid understanding, ownership, or change locality?

A lawful shared operation can remain shared even if domain policies evolve
independently. Conversely, fields can look identical today while their meaning
and lifecycle differ. Keep meaningful distinctions visible in either case.

## Present and apply

Explain the domain organization, common concepts, preserved differences, and
tradeoffs in user terms. Provide a file/construct mapping and verification
results as supporting detail. Ask only about unresolved domain boundaries or
behavioral choices, not how to express the syntax.

A report-only request yields a proposal. An authorized reorganization can be
applied after the checks without another approval for every move. Recheck the
actual baseline before applying saved proposals, update references coherently,
and record material changes per [workflow.md](workflow.md).
