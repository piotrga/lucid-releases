# Implementing Lucid requirements

Contents: Establish what is ready · Python conventions · Scala and other
targets · Verify behavior

Use only when implementation or translation is requested. Read the relevant
spec and [language.md](language.md). Honor the project's language, architecture,
and conventions. Prefer explicit types and a pure domain core where compatible;
do not switch stacks to satisfy a generic preference.

Apply [writing.md](writing.md) to names, comments, docstrings, and error messages.
Use clear domain terms and control flow. Preserve public API compatibility and
target-language idioms; avoid comments that merely repeat the code.

## Establish what is ready

Follow [workflow.md](workflow.md): account for the change in the spec first,
establish or update its tests second, then change implementation. This applies
to direct code/fix requests in a Lucid project as well as explicit spec work.

Read intent, definitions, rationale, guarantees, failure outcomes, and decisions.
Treat `ensures:` as postconditions. Distinguish `requires:` caller obligations
from external assumptions and required rejection of invalid requests.
Resolve questions controlling observable behavior; do not implement a proposed
policy as agreed. Continue independent work where requirements are settled.

Map requirements to code responsibilities and meaningful checks. Inspect the
existing implementation: a clarification may already be satisfied. Make only
necessary changes and preserve traceability. Requirements do not determine
every representation, algorithm, or optimization.

Read [projections.md](projections.md) for architecture and interface bindings.
Reuse adopted mappings; where design is authorized, choose routine technical
details consistent with product constraints and record their rationale and
status. Describe current code as observed until conformance is checked; do not
silently turn an implementation discrepancy into the required behavior.

## Python conventions

Default mappings for new Python code; adapt to established project conventions
while preserving requirements:

| Lucid | Python mapping |
|---|---|
| Entity | Annotated immutable value, normally `@dataclass(frozen=True)` |
| Collection in immutable state | `tuple[T, ...]` or an appropriate immutable collection |
| Optional field | `T | None`, preserving default and missing/empty semantics |
| Local constraint or forbidden state | Construction/domain-boundary validation plus behavior checks |
| Population-wide uniqueness | Enforcement at the owning collection/store boundary |
| Transition or cross-role invariant | Enforcement at the relevant coordination boundary; interaction/trace tests |
| `ordered by a then b` | Comparison of specified keys only |
| Pure `intent` | Fully annotated pure function |
| Effectful `flow` | Driver/service operation, commonly `async def` in an async project |
| Role handler | Pure function/method returning `(next_state, outgoing_effects)` |
| State change in `effect:` | New immutable state, often `dataclasses.replace` |
| Reply/send | Typed effect values with explicit target and payload |
| Named failure | Explicit result matching the domain outcome |
| `alongside` | Concurrency primitive matching agreed failure/cancellation semantics |
| Collection predicates | `all`, `any`, or counts over the defined population |
| Sets and relations | Validated typed data in its appropriate authoritative source |
| Definitions and rationale | Names, documentation, and relevant behavioral checks |

Frozen dataclasses do not recursively freeze
members: mutable dictionaries/lists need an immutable representation or suitable
encapsulation. Choose clear function boundaries rather than a line-count target.

Handlers perform no I/O or mutation. They return new state and effects for the
driver. Implement the specified failure-state behavior; if a material state or
effect outcome is absent, resolve it rather than assuming rejection is atomic
or leaves everything unchanged.
Invalid-value guards may raise validation errors; named protocol failures remain
explicit outcomes. Preserve rationale in useful documentation, not only test names.

`asyncio.gather` is not a universal lowering for parallel branches: inspect
failure, cancellation, ordering, and partial effects. Likewise, configure or
implement comparison so incidental dataclass fields do not become tie-breakers.

## Scala and other targets

For Scala, entities normally become immutable case classes; intents become
pure functions; handlers return new state and typed effect collections. Use
the project's ZIO, Cats Effect, or other stack for flows. Parallel composition
must preserve declared failure/cancellation behavior.

In every target, preserve valid states, outcomes, temporal guarantees, and
explicit assumptions. Shared code can use algebraic structures whose instances
satisfy the laws established by [generalization.md](generalization.md), while
retaining domain type boundaries and local policies.

## Verify behavior

Read [spec-derived tests](spec-tests.md) for deriving or generating tests and for the
incremental TDD cycle during behavioral implementation. Use application ports
and test adapters where they expose the contract independently of infrastructure;
keep real adapter and coordination checks for guarantees that depend on them.

Derive executable checks from agreed outcomes and meaningful boundaries. Preserve
user scenarios as acceptance evidence. For temporal/concurrent requirements,
exercise event sequences and interacting operations. Use property tests for
suitable laws; merely copying an implementation predicate adds little evidence.

Do not generate passing `pass`/TODO test stubs and call requirements covered.
An unimplemented check must fail explicitly, be skipped with a reason, or be
recorded as missing coverage according to project conventions. Generated tests
can repeat a misunderstood requirement: compare outcomes with original user
scenarios as well.

Run appropriate checks and record actual results, unverified requirements,
and limitations. Do not weaken a requirement or assertion just to pass a test.
If the spec conflicts with intended behavior, ask about that behavior.

Lead the report with resulting behavior and validation. Include implementation
details needed to understand material limitations. Maintain decisions and
change records per [workflow.md](workflow.md).
