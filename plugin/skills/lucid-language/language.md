# Lucid language reference

Contents: Meaning and rationale · Logical contract conventions · Entities ·
Definitions · Invariants · Roles and messages · Pure operations and effectful
flows · Design by Contract · Conditions and collections · Sets and relations ·
System-level claims · Required slots and references · Compatibility

Lucid combines structured declarations with precise prose. This reference
defines the constructs and their meaning. Syntax highlighting alone checks
neither syntax nor meaning.

## Meaning and rationale

Conditions, exceptions, quantifiers, units, and time belong in the requirement.
`because:` explains its benefit or the harm prevented; it cannot add a hidden
condition. State necessary mechanisms and assumptions separately.

Create domain vocabulary when it clarifies recurring meaning. Definitions and
rationales may use several sentences when needed. Prefer one main idea per
sentence and preserve the conditions that belong together.

Write normative behavior in EARS form when that makes the obligation clear.
Place the sentence in the relevant invariant, effect, or postcondition body.
Keep rationale separate. EARS clauses are structured prose, not new Lucid slots.
Use ordinary definitions for meaning and Gherkin for examples of that meaning.

## Logical contract conventions

Apply these while authoring, not only during a later review. Express them in
the existing constructs and their prose; they are not additional syntax slots.

- **Vocabulary and scope:** give each recurring concept one definition and
  use its name consistently. Bind actors, entities, quantifiers, and references
  to their population and context. Define identity and equality where they
  affect counts, uniqueness, retries, or matching messages.
- **Conditions and obligation:** separate necessary conditions from sufficient
  ones. "Succeeds only if authorized" does not promise success whenever
  authorized. State the success conditions, relevant failure outcomes, and
  priority or compatibility of overlapping cases.
- **Values and boundaries:** specify units, time reference, interval endpoints,
  cardinalities, and missing/empty/default behavior where they change an outcome.
  Replace material vagueness such as "recent" with a sourced definition or an
  open decision, not an invented threshold.
- **Transitions:** identify the state owner, admissible source states, trigger,
  guard, next state, observable result, and outgoing effects. State affected
  fields and what remains unchanged when omission would leave multiple readings.
  Define initial and terminal conditions when the lifecycle relies on them.
- **Interaction:** identify participants, message meaning and recipients,
  causal dependencies, alternatives, and required ordering. State correlation,
  retries, duplicate handling, and failure/recovery behavior when material.
  Unknown ordering is not automatically permission to reorder.
- **Allowed variation:** name the full constraint on outcomes when more than
  one is permitted. Do not turn a representative example into a required order,
  particular winner, algorithm, or incidental numerical constant.
- **Source and status:** distinguish agreed product rules, their derived
  consequences, adopted technical decisions, external assumptions, and open
  proposals. Put each normative fact at an authoritative definition site;
  link consumers rather than independently maintaining competing formulations.

An operation may specify a relation between permitted states and outcomes,
rather than a single deterministic function, when the agreed contract allows it.
Make the allowed relation explicit. Pure intents and individual role handlers
still have their documented deterministic semantics; resolve external choices
through explicit inputs or orchestration rather than hiding nondeterminism there.

Use predicates, decision tables, or transition tables when they clarify branching,
alongside domain-language explanations. Each shared abstraction states how a
reader recovers the local rule. Examples illustrate the contract; example values
bind behavior only when explicitly declared requirements. A readable paraphrase
must not weaken conditions, exceptions, modality, or timing.

## Entities

```lucid
Name
  represents: <domain concept; required when the name is ambiguous>
  has
    field: Type [constraint] [= default]
  [ordered by field1 then field2]
  [forbidden:
    - <excluded state combination> because: <reason>]
  [invariant name:
    <predicate>
    because: <reason>]
```

An entity is a value describing a domain concept at one moment. Constraints
such as `> 0`, `unique`, and `non-empty` describe its valid value space.
Specify the scope of uniqueness; a population constraint cannot be checked
on one instance. Use `T or none = none` for an optional value and `[T]` for a
collection. Distinguish missing from empty when behavior depends on it.

`ordered by` compares only the named keys lexicographically. Define ties or
key uniqueness when distinct values need a strict total order. `forbidden:`
anchors excluded combinations on their owning entity, each with its rationale.

## Definitions

```lucid
definition: overdue loan — a loan whose due time has passed and whose
  book has not been returned
  meets:
    - a loan due yesterday with no recorded return
  meets-not:
    - a loan returned before its due time
    - a loan whose due time has not yet passed
```

A definition gives reusable meaning to a domain noun phrase; it has no function
signature. Cite its exact name. Prefer natural domain terms, often positive
ones, over opaque negations. Create the definition yourself rather than asking
the user to invent its name or wording.

Include `meets:` and `meets-not:` when they clarify boundaries. They must agree
with the definition. A definition needs no `because:` slot; a normative choice
within its meaning still needs an accessible reason in the surrounding
requirement or a decision reference.

Put intrinsic value semantics and recurring classifications in definitions.
Keep obligations such as "show every overdue loan" in behavioral rules.
Rules may constrain one entity or many. Avoid copying a full definition into
each consumer. For shared algebraic structures, define the roles of values and
operations, name their laws as invariants, and state each domain's mapping.

## Invariants

```lucid
invariant member_portal_lists_overdue_loans:
  THE member portal SHALL include every overdue loan in its action list
  because: members need to know which books require action to avoid fees
```

Invariants can be top-level or belong to an entity or role. Give each a stable,
descriptive name. Specify scope, conditions, and exceptions. State whether it
constrains a snapshot or a transition when relevant. Every invariant needs
`because:`. Split independent obligations when useful, not just because a
sentence contains "and". A rule need not be weakened to shorten its rationale.

## Roles and messages

```lucid
role Name:
  purpose: <why this participant exists>
  [assumes: <external conditions>]
  state:
    field: Type [= default]
  accepts:
    MessageName(field: Type, ...) [from sender_role]:
      purpose: <what this request accomplishes>
      [requires: <caller obligations>]
      [assumes: <conditions relied on>]
      [fails when: <named failure conditions>]
      [ensures: <postconditions; existing guarantees is also supported>]
      effect:
        <next-state changes and explicitly addressed outgoing messages>
  [invariant name:
    <predicate>
    because: <reason>]
```

A role is an addressable participant with private state. Handlers are pure
transitions from `(state, message)` to `(next state, outgoing messages)`.
Effect prose describes the next state, not mutation or I/O. A separate driver
performs sends and storage. Split `effect:` into `on success:` and `on failure:`
when outcomes differ. Name recipients, including replies to the caller.

Describe every relevant outcome branch, including failed requests and partial
effects. Silence does not establish that state is unchanged or that an operation
is atomic. A concise statement such as "all other fields remain unchanged" is
useful when it is supported by the contract. Material missing behavior is an
open decision. A lifecycle can be expressed through named state values and these
handlers; it needs no invented `state_machine` keyword.

Messages are immutable payloads declared by the receiving handler's signature
under `accepts:`. New specs use no standalone message declaration. Replies may
be constructed inline in `effect:`, with clear fields and meaning. Reuse that
meaning across producers. Delivery, durability, ordering, deduplication, and
serialization are not implied by pure transitions; record the requirements or
external assumptions on which user-visible guarantees depend.

## Pure operations and effectful flows

```lucid
intent name(arg: Type, ...) [-> ReturnType]:
  [purpose: <why this operation exists>]
  [requires: <caller obligations>]
  [ensures: <postconditions>]
  <expression or named pure steps>

flow name(arg: Type, ...) [-> ReturnType] [as Role]:
  purpose: <user or system outcome>
  [requires: <caller obligations>]
  [assumes: <external conditions>]
  [fails when: <named failure conditions>]
  [ensures: <observable postconditions; existing guarantees is also supported>]
  steps:
    <named step = expression>
```

`intent` is pure: explicit inputs determine the result without I/O. Its
`purpose:` is optional when self-explanatory. Use `intent ... -> Bool` for a
parameterized predicate whose call sites supply different inputs; use
`definition:` for vocabulary cited without a call interface.

`flow` interacts with the environment. Verbs such as `fetch`, `send`, `store`,
and `wait for` signal effects. A pure calculation over a supplied clock value
or snapshot remains an intent. Specify failure outcomes and nontrivial
guarantees, including recovery and partial completion when observable.

Steps express dependencies and required ordering. Do not infer new user
requirements from incidental presentation order. Preserve existing behavior
when interpreting an older spec, and ask about any observable ambiguity.

```lucid
alongside:
  a = <independent step producing a>
  b = <independent step producing b>
```

`alongside` permits concurrent independent branches. It does not imply identical
start times, atomicity, completion order, or cancellation behavior. Specify
observable failure/cancellation outcomes; no future/fiber syntax is needed.

## Design by Contract

Use `requires:` for material caller obligations on intents, flows, or handlers.
Use `ensures:` for their postconditions. Existing `guarantees:` remains supported
as a postcondition spelling; use one authoritative block, not duplicate versions.
Use named `invariant` constructs for properties across the declared valid states
or transitions. They retain `because:` and normal reference rules.

State which values are inputs, results, pre-state, and post-state. A postcondition
can refer to the returned value as `result`. Define any other symbols it needs.
Do not silently add a narrower input domain while extracting a contract.

```lucid
intent remaining_capacity(capacity: Int, allocated: Int) -> Int:
  purpose: report unused capacity for a valid allocation
  requires: 0 <= allocated and allocated <= capacity
  ensures: result = capacity - allocated and result >= 0
  capacity - allocated
```

This pure operation requires a valid allocation. It does not specify how a public
request for too much capacity is rejected. An application that promises such
rejection must define that behavior in its flow or handler and its failure results.
Do not convert the promised rejection into a precondition that excludes the case.
Keep environmental assumptions in `assumes:`. Neither a contract clause nor a
pure transition proves the mechanism needed for concurrent enforcement.

## Conditions and collections

```lucid
when the order is Pending and payment succeeds -> Paid
otherwise -> unchanged

a majority of Acceptors accepted the same proposal
at least 3 of Workers reported healthy
every Order in batch is paid
some Replica has version >= v
```

These illustrate logical conditions, not an exhaustive list of special cases.
Specify the population, time, and distinct participants a quantifier refers to.
Resolve overlapping branch priority when it changes behavior. Keep undecided
product cases open rather than inventing an arbitrary branch.

## Sets and relations

```lucid
set name : EntityType
  purpose: <why this concrete corpus belongs in the spec>
  - field: value, other_field: value

relation name : EdgeType from SourceType to TargetType
  purpose: <meaning of this connection set>
  - from: SourceInstance, to: TargetInstance
```

A Lucid `set` is a named ordered collection of typed records. Do not infer
mathematical set deduplication or unordered behavior. Items conform to the
entity's fields; omissions need an optional field or declared default. Items
need no individual rationale. The whole collection is one movable block.

A `relation` is a collection of directed edges. Endpoint fields belong to its
edge type and match source/target identifiers. Names may be `from`/`to`,
`upstream`/`downstream`, or another explicit pair. Use `from T to T` for edges
within one type. Unrelated paired identifiers are not automatically a relation.

Keep large or volatile inventories in their authoritative data source where
listing them would make the spec stale. Extracted types commonly live in
`<domain>.lucid` and corpora in `<domain>.<sub>.lucid`; domain boundaries and
reader needs determine the split.

## System-level claims

```lucid
safety name:
  statement: <system property>
  rests_on: <actual named requirements supporting the property>
  [assumes: <external conditions>]
  because: <explanation connecting the basis to the property>
```

Use this for properties supported by cooperating rules or roles. Every
`rests_on` name must resolve to an actual construct. Do not invent supporting
names only inside the claim. The prose explanation is not a formal proof.

Legacy `safety` also covers progress claims. Preserve the keyword but distinguish
"nothing bad happens" from "something eventually happens" in the statement and
review. Progress needs relevant delivery, fairness, recovery, or time assumptions.
Eventual progress alone does not specify an acceptable user waiting time.

## Required slots and references

| Slot | Required on |
|---|---|
| `purpose:` | Roles, handlers, flows, sets, relations; intents when purpose is unclear |
| `represents:` | Entities whose meaning is ambiguous |
| `because:` | Invariants, forbidden entries, system-level claims |
| `assumes:` | Constructs relying on material external conditions |
| `requires:` | Intents, flows, or handlers with material caller obligations |
| `fails when:` | Flows and handlers with non-success outcomes |
| `ensures:` or `guarantees:` | Intents, flows, or handlers with nontrivial postconditions |
| `statement:`, `rests_on:` | System-level claims |

Missing required content is a spec defect. Call it a parser/compile error only
when an actual tool reports it. Use stable names and explicit cross-file
references, such as `see bookings.lucid → active reservation`. Comments may
link decisions or explain mappings; normative behavior belongs in constructs.

## Compatibility

- Keep the `lucid-language` skill name and `.lucid` extension.
- Preserve existing `guarantees:` blocks. New Design by Contract descriptions
  can use `ensures:`. A local change does not require a project-wide rename.
- Accept legacy `dataset N : T` as `set N : T`. Emit `set` for new constructs;
  a local change does not require a project-wide rename.
- Read older entity `purpose:` as `represents:` when it describes the concept;
  preserve meaning during authorized normalization.
- Recognize old standalone `message` and `when ... arrives as Role` forms.
  During authorized migration, move them under `accepts:` without changing
  guards, delivery, or outcomes. Clarify observable ambiguity first.
- Recognize legacy `context`, context-level `intent` prose, `params`, and
  `invariants` grouping headings. Preserve meaning; distinguish context prose
  from a pure `intent` function.
- Preserve existing `tightening_history:` and `calibration_history:` records
  as maintenance metadata rather than runtime behavior.

Use existing forms instead of ad hoc top-level keywords. Algebraic reasoning
does not require language-level generics or monadic/effect syntax. Target-language
machinery belongs in implementation unless it is an agreed requirement.

Record adopted architecture and public interface bindings when the project
needs them, at a clearly identified design layer in its spec. Reuse entities,
definitions, roles, flows, sets, and relations; do not invent a top-level `module`
or `api` construct. Distinguish logical responsibility from its implementation
mapping.
