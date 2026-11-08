# Implementing Lucid requirements

Use this reference to check whether a settled rule can be implemented and
verified. In a spec-only task, record consumers and missing decisions. Make
implementation changes only when the user has requested them.

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

## Mapping a rule to its enforcement

Identify the boundary that can uphold each guarantee. Value constraints may
hold at construction. Uniqueness across purchases requires coordination where
the buyers share stock. For a transition, preserve the specified pre-state,
result, next state and observable effects, including failure and retry paths.
For parallel branches, record the agreed ordering, cancellation and partial
outcomes. Leave the choice of language, libraries and local representation
to the project unless an adopted design decision constrains them.

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
