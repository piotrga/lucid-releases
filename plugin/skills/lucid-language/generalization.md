# Generalization across the specification

Contents: Search beyond the edited construct · Establish the common structure
· Preserve domain boundaries · Challenge the candidate · Example: combining
partial results · Express and apply the result

Use this analysis for each material requirement change and for reviews of
shared concepts. [SKILL.md](SKILL.md) defines the user-facing conversation.
The model searches, proposes abstractions, and writes their definitions and
laws. The user decides observable behavior where existing intent is insufficient.

## Search beyond the edited construct

Start with the spec overview, vocabulary, and affected dependencies. Search
across all spec files for analogous behaviors and operations, including
different names for the same concept. Read promising candidates in context,
including their assumptions, exceptions, consumers, and local decisions.

Look for repeated meanings, ways of combining results, lifecycle transitions,
resource allocation, transformations, ordering, and failure behavior. Similar
fields or wording trigger investigation; they do not establish equivalence.
If the spec is large, use a broad index/search followed by focused reading.
Do not claim a global analysis when only the edited file was inspected.

## Establish the common structure

For a candidate abstraction, identify:

- The concepts and valid values involved in each application.
- The corresponding operations and their observable meaning.
- The common laws, their scope, and necessary assumptions.
- The mapping from each domain's operations to the shared operations.
- The local restrictions, exceptions, and stronger laws that must stay local.
- The benefit: a reusable definition, shared rule, derived result, or simpler
  check that matters to the current specification.

Derive these from the requirements. Do not invent a missing identity element,
inverse, ordering guarantee, or policy to make an abstraction fit. Unknown
laws remain unknown. Choose the least demanding useful structure supported
by all applications. Two examples are candidates for investigation, not proof
that every member of a broad family obeys the same laws.

Separate the rule from the examples that suggested it. Vary incidental names,
identifiers, quantities, and arrangements while preserving the relevant domain
conditions. Check meaningful boundaries and an excluded case. If the proposed
rule depends on an incidental fixture value, identify an agreed reason for that
dependence or remove it. Conversely, retain a concrete threshold when it is an
actual product policy. Generality is supported scope, not maximum abstraction.

Recognize established mathematical structures where useful: orders, monoids,
monads, rings, and others are available reasoning tools, not a required
classification scheme. Verify the relevant laws, operations, and equivalence
notion before using the name. For example, a monad needs lawful sequencing
and a neutral introduction operation; a sequence of steps alone is not enough.
A ring needs the additive, multiplicative, and interaction laws; numeric-looking
fields alone do not establish them. Do not import a library just to name a law.

## Preserve domain boundaries

Distinguish three possible outcomes:

1. **One domain concept expressed several ways:** extract a shared definition
   and update its consumers, preserving all membership conditions.
2. **Different concepts with a shared lawful operation:** share that operation
   and its laws, retaining separate domain types, identities, and policies.
3. **Superficial similarity or no useful shared contract:** keep the concepts
   separate and retain the useful finding without forcing a refactor.

Ask whether an independent change to one domain's policy would unnecessarily
change another. If so, move that policy out of the common definition. Shared
laws can remain valid even when the domains evolve independently.

Identical current values do not imply shared policy: a 30-day refund window
and a 30-day log retention period may change for unrelated reasons. Matching
record fields do not make a customer and an employee one concept. Avoid a
single generalized entity filled with optional fields solely to merge shapes.

## Challenge the candidate

For every application, map its original requirements to the proposed common
definition and local rules. Check representative ordinary, boundary, exception,
and interaction cases; use executable law checks when suitable tooling exists.
Try to construct a valid local case where a proposed shared law fails.

Inspect empty values, repeated operations, ordering, finite precision,
partial operations, and side effects when relevant. For example, algebraic
laws for exact arithmetic may fail under floating-point rounding. Preserve
the distinction between associativity, commutativity, and idempotence.

State what was established by the specification, tested, or left uncertain.
Neither a familiar algebraic name nor several successful examples prove the
mapping. If a counterexample breaks only a stronger law, keep a weaker useful
abstraction when it genuinely fits; otherwise retain separate structures.

## Example: combining partial results

Adding exact nonnegative event counts has a neutral zero and is associative.
Concatenating ordered event lists has a neutral empty list and is associative.
Both can share a rule for combining partial results while preserving the
order of the parts. Counts and lists remain separate concepts.

Reordering parts does not change an exact count, but can change an event list.
Do not promote that extra property into the common rule. Duplicate delivery
also matters: neither addition nor concatenation removes duplicates. If the
product requires each event to count once, derive a separate requirement for
that behavior rather than calling the combination operation idempotent.

Explain the result to the user through its consequence: "These reports can
combine partial results consistently. Event histories still preserve order."
The user need not select the algebraic structure or write its laws.

## Express and apply the result

Use a `definition:` for shared vocabulary, `intent` for parameterized pure
operations, and named invariants for their laws, following
[language.md](language.md). A general definition may name roles such as the
values, combination operation, and empty value; each application states how
its domain fills those roles. Do not introduce a new top-level syntax or erase
domain names merely to expose a type-class hierarchy.

A reader must be able to instantiate the shared rule for each domain without
guessing hidden parameters, assumptions, or exceptions. Include a concise domain
explanation and useful positive/boundary/negative examples where the mapping is
not obvious. If the abstraction cannot support clear local test expectations
or hides a material product distinction, repair its mapping or keep it local.
Derived diagrams and documents must preserve these same local distinctions.

Within an authorized requirement update, create derived definitions and small,
well-supported generalizations yourself under SKILL.md's safe stewardship rule.
Update references, local rules, and dependent guarantees together. Review the
aggregate change as well as individual rewrites. Propose substantial cross-context
generalizations with their benefit, boundaries, migration scope, and checks unless
already authorized. Necessary consequences of the requested change are still part
of that change. If preservation is uncertain, retain the existing requirements.

Ask a user-level question only if the generalization introduces an undecided
behavior, contradicts an existing decision, or needs an unknown domain fact.
When abstract membership depends on an answer, record it as provisional and
continue the independent work.

Report the common requirement, affected areas, preserved differences, and any
decision needed. Keep formal mappings available in the spec or review material.
Do not burden the user with a report for every rejected abstraction candidate.
