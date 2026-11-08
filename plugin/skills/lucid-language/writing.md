# Clear writing and complementary conventions

Contents: Select the form before writing · Technical prose: ASD-STE100
principles · Presenting a specification · Requirements: EARS ·
Architecture: C4 · Decisions: ADR · Interfaces and invariants: Design by
Contract · Behavioral examples: Gherkin · Document structure and Lucid
compatibility

Read before authoring or substantially rewriting a spec, code explanation,
documentation, or user-facing explanation. Apply this guidance to English text
for readers who may not be native speakers. Use the user's language in dialogue
and preserve the project's established language in artifacts. The same clarity
principles apply in other languages; do not translate identifiers mechanically.

Lucid coordinates the representations below and their source links. Use established
notation where it fits. Select the smallest form that preserves the meaning.
These forms complement each other within a document. They are not competing
formats for the whole specification. Precision takes priority over notation.

## Select the form before writing

| Information | Preferred form | Main question it answers |
|---|---|---|
| Explanation, goal, context, scope | ASD-STE100-style prose | What does this mean, and why does it matter? |
| Normative system behavior | EARS | Under which conditions must the system do what? |
| Architecture and boundaries | C4 | Which system, application/data store, or component owns and interacts with what? |
| Significant design decision | ADR | What was decided, why, and with which consequences? |
| Interface guarantee or invariant | Design by Contract | What must hold before, after, and across operations? |
| Behavioral example or important edge case | Gherkin | What happens in this concrete situation? |

First identify the source fact and its status. Then select the form, write it,
and check that conditions, modality, scope, timing, and exceptions did not change.
Separate mixed information when it serves different purposes. Keep one authoritative
statement and link its explanations, contracts, examples, and decisions. Do not
maintain six independent versions of every rule or require all six forms.

## Technical prose: ASD-STE100 principles

Write short sentences with one main idea. Name the subject and use active voice.
Use one consistent term for a concept within its context. Prefer familiar verbs
and concrete nouns. Avoid idioms, ornamental synonyms, long noun chains, ambiguous
pronouns, and unnecessary prefaces. Define unfamiliar domain terms near first use.

Example, assuming eligibility and attempted recovery are established requirements:

- Vague: "The system should generally be capable of attempting recovery when appropriate."
- Clear: "The healer attempts recovery for eligible failures."

Define "eligible failure" at its source; a shorter sentence alone does not remove
the ambiguity. If the source only permits recovery, preserve that permission
instead of rewriting it as an obligation.

Use established software and mathematical terms when they are more precise.
Explain them through their domain consequence. Do not enforce the full controlled
dictionary or claim formal ASD-STE100 compliance. This is a practical use of its
writing principles, as described by the
[ASD maintenance group](https://www.asd-ste100.org/STE_faq.html).

## Presenting a specification

Start with the outcome, then link to rules and evidence. Keep each rule's
conditions, exceptions and uncertainty alongside it. Use the project's
vocabulary and include all information needed to decide a concrete case.

## Requirements: EARS

Use EARS for normative behavior. Name the responsible system or subsystem instead
of an ambiguous "it". Choose the trigger pattern that matches the actual meaning:

| Kind | Pattern |
|---|---|
| Always applicable | THE <system> SHALL <response>. |
| Event response | WHEN <event>, THE <system> SHALL <response>. |
| State-dependent obligation | WHILE <state>, THE <system> SHALL <response>. |
| Unwanted condition | IF <condition>, THEN THE <system> SHALL <response>. |
| Optional product feature | WHERE <feature is included>, THE <system> SHALL <response>. |

Combine state and event clauses when both matter. Use IF/THEN for an unwanted
condition; it is not a substitute for every WHEN or WHILE clause. Sentence case
is acceptable: uppercase keywords aid recognition but do not change meaning.
These patterns follow [Alistair Mavin's EARS guide](https://alistairmavin.com/ears/).

Bind the conditions, response, time reference, and quantifiers to defined concepts.
Replace material vagueness such as "fast", "normally", "robust", "where possible",
or "as appropriate" with established conditions or an open decision. Do not invent
a deadline to make a vague statement look testable. Distinguish more than 60 minutes
from at least 60 minutes, and specify whose clock/time interval is relevant.

SHALL states an obligation; a draft containing SHALL is still a draft. Preserve
explicit permissions and allowed variation rather than silently making them mandatory.
A required permission can be expressed as an obligation to permit that behavior.
Do not convert a necessary condition into a sufficient one during an EARS rewrite.
Use precise prose or a decision table if the pattern obscures the actual logic.

## Architecture: C4

Start with the system, its users, and external systems. Expand to containers
(applications or data stores), then to components when that detail helps. Dependencies
are labeled relationships at the chosen level, not another level of decomposition.
A C4 container is not necessarily a Docker container, and a component is not every
class. See the [C4 abstractions](https://c4model.com/abstractions).

State the view's scope and level. Name responsibilities, ownership boundaries,
and the meaning/direction of interactions. Show deeper detail through another
view or an explicit mapping. Do not invent container assignments or deployment
facts to fill out the hierarchy. A logical pipeline can remain a behavior view
until its architecture mappings exist. Use C4 for structure; retain transition
tables/state diagrams and sequence diagrams for behavior. See [projections.md](projections.md).

## Decisions: ADR

For a decision that constrains future architecture or significant engineering,
use **Context → Decision → Rationale → Consequences**. Record status and links
to affected requirements using the project's existing ADR convention. Explain
relevant alternatives or tradeoffs in the context/rationale when useful.
Consequences include costs, limitations, and follow-up obligations.

Keep proposed, adopted, and superseded decisions distinct. Preserve an old
decision's history and link its replacement. Trivial local choices need no ADR.
This layout adapts [Michael Nygard's decision records](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions)
with an explicit Rationale section. An ADR records a decision; it does not replace
the affected behavioral requirements or turn a model proposal into user approval.

## Interfaces and invariants: Design by Contract

Use `requires`, `ensures`, and named `invariant` clauses when they make a semantic
guarantee precise. Specify the operation, input/state scope, pre-state/post-state
meaning, and unchanged state where material. A precondition states a caller
obligation. A postcondition states the operation's guarantee when its preconditions
hold. An invariant constrains the declared valid states or transitions.
See [Design by Contract](https://www.eiffel.com/values/design-by-contract/introduction/).

A required rejection of invalid or ineligible input is system behavior. Specify
that outcome; do not remove the case from the contract by making eligibility a
precondition. External assumptions are also distinct from caller obligations.
A before/after assertion alone does not establish concurrency safety or a property
over the entire execution history. Preserve any required coordination and temporal
conditions. Contracts written in prose are not automatically checked at runtime.

Use [language.md](language.md) for placement and compatibility with `guarantees:`.
Keep ordinary API documentation focused on operations, payloads, errors, and bindings;
do not wrap every parameter description in a contract. Prefer a clear predicate
or sentence over extra notation that adds no precision.

## Behavioral examples: Gherkin

Use Given/When/Then for acceptance examples, transitions, important edge cases,
and behavior with interacting conditions. Given establishes domain context; When
identifies the action/event; Then states observable outcomes. And/But can express
related conditions or consequences. Use established terms and concrete test data.

Link each scenario to its general rule. Include contrasting boundaries or failure
cases where they clarify that rule. Do not translate every requirement into a
scenario or mistake example constants for a general policy. Use Scenario Outline
only when cases share meaningful behavior. A Gherkin example becomes an executed
test only through a working test binding and an actual run; see [spec-derived tests](spec-tests.md)
and the [Gherkin reference](https://cucumber.io/docs/gherkin/reference/).

## Document structure and Lucid compatibility

When these sections add information, use this order:

Goal → Context → Scope → Requirements → Architecture → Decisions →
Interfaces/Invariants → Behavior/Edge Cases.

The first three use clear prose. The remaining sections use the matching forms
above. Omit empty or redundant sections. A small change may need only a requirement
and one example. Technical details do not belong in a PM summary just to complete
the template. Full contracts still retain everything their intended reader needs.

Keep Lucid names and references stable. EARS belongs in requirement prose; contracts
describe existing operations and invariants. C4 views, ADRs, and Gherkin examples
can live in linked project artifacts. Do not add custom top-level constructs for
these formats or reformat an unrelated spec wholesale. Review the combined result
for lost conditions, stronger claims, duplicate authorities, and increased reading
effort. Prefer clear prose whenever notation would make the meaning less clear.
