# Derive documentation and system views from the specification

Read for the derivability step of requirement changes and when generating tests,
documentation, APIs, or diagrams. A projection selects and explains established
facts for an audience; it does not independently decide system behavior. Generate
the requested outputs, not every possible view after every edit.
Apply [writing.md](writing.md) before generating a view. Use clear prose for
explanations, EARS for obligations, C4 for structure, ADRs for significant
decisions, contracts for semantic guarantees, and Gherkin for useful examples.

## Contents

- Authoritative facts and adopted design
- Information needed by each output
- Generate a faithful projection
- State machines
- Sequence diagrams
- Architecture, modules, and interfaces
- Readiness and change propagation

## Authoritative facts and adopted design

Keep product obligations, derived consequences, and adopted design decisions
distinguishable in the spec, with links between them. Requirements rarely fix a
unique architecture, transport, endpoint path, or module layout. Make routine
design choices within an authorized design/implementation task and record them
with their rationale and status. Ask only about unresolved product consequences
or constraints. During extraction/review, leave absent bindings open or present
separately labeled proposals. Do not claim a proposed API describes an existing one.

Use existing project locations. A project may keep logical contracts and adopted
technical mappings in separate spec files; a small project can keep them together.
Use the constructs in [language.md](language.md) and existing architecture decision
records. A role is a logical participant, not automatically a service or module;
a spec file is not automatically a deployment or consistency boundary.

Existing schemas, code, and architecture records supply evidence for technical
bindings. Check their agreement with the behavioral contract. Record discrepancies
instead of choosing whichever source makes generation easiest. Generated docs
must not silently become a second authority for behavior.

## Information needed by each output

| Output | Required source facts when applicable | Result to produce |
|---|---|---|
| User documentation | Goals, actors, prerequisites, visible actions/results, limitations, errors and recovery | Tasks and explanations in the user's vocabulary; UI instructions only from an established UI |
| Product manager documentation | Scope, value, capabilities, domain rules, scenarios, exclusions, decisions, acceptance outcomes | Logical product behavior and tradeoffs near the user level; no invented roadmap or commitments |
| Architect documentation | Context boundaries, responsibilities, state/data ownership, contracts, invariants, dependencies, quality constraints, consistency/failure assumptions, adopted decisions | High-level structure, collaboration, constraints and their rationale |
| Engineering/API documentation | Adopted modules and operations, types/schemas, binding to logical behavior, errors, authentication/authorization, protocol/version and delivery rules | Concrete contracts and mappings engineers can implement or consume; unknown bindings labeled |
| System tests | Preconditions, triggers, observable outcomes, invariants, boundaries, exceptions, allowed variation and controllable assumptions | Behavioral tests and a coverage map per [spec-derived tests](spec-tests.md) |
| State machine | State meanings/ownership, initial/terminal conditions, events, guards, transitions, outputs, failure paths | Lifecycle transitions with guards and effects, linked to their sources |
| Sequence diagram | Participants, triggering scenario, messages/results, dependencies, alternatives, concurrency, failure/recovery | A sourced interaction trace or explicitly bounded family of traces |
| Module/interaction map | Logical responsibilities plus adopted implementation mapping, public contracts, dependencies, ownership and external systems | Labeled nodes and directed interactions at a declared logical or implementation level |

The table is a source-sufficiency check, not a demand for every listed field in
every system. Identify the concrete missing fact and affected output. A stateless
calculation needs inputs, outputs and laws, not an invented lifecycle. Conversely,
an API consumer needs error and payload semantics even if a PM summary can omit
their wire representation.

## Generate a faithful projection

1. Identify audience, scope, system version/baseline, and whether the requested
   view describes agreed behavior, current implementation, or a proposed design.
2. Locate the authoritative constructs and decisions, then collect the source
   facts needed by the table. Resolve source disagreements before deriving a
   definitive claim. Continue with settled sections and mark unresolved ones.
3. Build a compact mapping from material output claims to source constructs.
   Existing stable names and file links are sufficient; no universal ID scheme
   or separate database is required. Put references per section/table/diagram
   where practical, not a distracting citation on every explanatory sentence.
4. Generate at the audience's level. Keep conditions, exceptions, allowed choices,
   and confidence/status intact. Distinguish explanatory example values from
   contractual constants and sample traces from an exhaustive behavior model.
   Start with the goal and outcome, then expose detail by topic or linked view.
   Use simple English without losing the domain's precise terms.
5. Inspect the mapping in both directions: every asserted behavior has a basis;
   every source fact material to the requested scope is represented or explicitly
   excluded. Exercise a relevant boundary/failure case through the spec, its
   explanation, diagram, and test expectation to expose drift.

A new question uncovered during generation goes back into the decision record.
Do not solve it only inside a diagram, test fixture, or documentation paragraph.
Keep a compact source baseline and affected-construct references with maintained
artifacts. A successful renderer verifies diagram syntax, not behavioral fidelity.

## State machines

Derive a transition table before drawing a nontrivial lifecycle:

| Source state | Trigger | Guard | Next state | Result/effects | Requirement |
|---|---|---|---|---|---|
| From an established state predicate | Named command/event | Applicable condition | Defined state update | Visible outcome and sends | Actual source name |

State names may abbreviate predicates over several fields; give that mapping.
An abstract diagram must preserve all distinctions relevant to its stated scope.
Do not imply that one summary state determines a unique next state when omitted
data can change the result; show guards, refine the state, or declare the view's
limited scope. Distinguish commands, events, and time-based eligibility changes.

Check initial reachability, valid/invalid triggers, overlapping guards, missing
outcomes, termination when promised, and preservation of invariants. Represent
failure branches and material unchanged-state outcomes. An unspecified event is
not automatically ignored, rejected, or a self-loop. Draw only transitions with
a source basis. A deadline does not imply a timer message or storage update;
those require an adopted mechanism if shown at the implementation level.

Use Mermaid or the project's diagram format, labeling edges with trigger, guard,
and important effects. Keep concurrency and multi-owner state visible where a
single linear machine would misrepresent the contract.

## Sequence diagrams

Select a sourced scenario. Identify participating roles/external actors and
extract each send, receive, result, and required causal dependency from flows
and handlers. Map roles to concrete components only where that mapping exists.
Keep this trace consistent with the transition table and ownership rules.

Use alternatives for conditional outcomes, parallel branches for permitted
concurrency, and repetition only where the repetition rule is established.
Keep correlation and delivery assumptions visible when needed to distinguish
retry from a new request. Acknowledgement is not completion unless specified.
Do not add a broker, synchronous call, timeout, compensation, or retry count to
make the drawing look realistic. Preserve partial order: visual placement alone
must not assert a new ordering guarantee. Label an illustrative interleaving
as one permitted trace rather than the required schedule.

## Architecture, modules, and interfaces

Use C4 levels for structural views: system context, containers, then components
where the audience needs them. Label relationships and external/ownership
boundaries. Keep the chosen level visible; use explicit mappings when a view
spans levels. A container means an application or data store, not necessarily
a deployment container. Do not promote every implementation class to a component.
Use state and sequence diagrams for behavior; C4 does not replace those views.

First locate bounded meanings and ownership. Use domain responsibilities and
consistency requirements to identify boundaries; inspect which operations must
coordinate and which may complete independently. A cross-boundary guarantee
needs an explicit coordination/failure contract. Do not silently replace required
consistency with eventual consistency to fit a preferred architecture.

Apply the ports-and-adapters perspective where useful: name the application
capabilities it exposes and the external capabilities it requires. For each port,
record the purpose, inputs/outputs, errors, and relevant delivery/ordering rules.
Keep those meanings stable across test, UI, transport, or storage adapters. A port
does not prescribe an HTTP route, database, or one interface per use case.

For a module map, extract nodes from adopted module assignments and label their
responsibilities and state ownership. Derive directed edges from actual contracts;
label whether an edge is a call/message, data dependency, or ownership relation.
Show external systems distinctly. Keep logical contexts, implementation modules,
and deployment units separate or provide an explicit mapping between levels.
If only logical facts exist, produce a logical map and identify the missing
implementation mapping rather than presenting guessed modules as current design.

For API documentation, map each public operation to its logical command/query,
guard, outcomes, and adopted binding. Resolve types, required/optional fields,
units, error meanings, and applicable authorization, versioning, pagination,
idempotency, or asynchronous completion semantics. Do not add irrelevant features.
Where design is authorized, choose ordinary representational details, record them,
and generate the API from that decision. Escalate product consequences through
concrete scenarios; the user need not design an OpenAPI schema.

This use of ports and adapters follows
[Alistair Cockburn's original article](https://alistair.cockburn.us/hexagonal-architecture).
It guides boundary decisions without requiring hexagonal boilerplate or changing
an existing stack. This reference is self-contained; background links need not
be fetched during routine Lucid work.

## Readiness and change propagation

Declare readiness for the requested output and affected behavior, not all future
views. A source-derived behavioral test can be specified before an HTTP binding
exists; executing it requires an actual test adapter. An architect's logical map
can be ready while the deployment view remains undecided.

When a rule changes, follow references into maintained docs, diagrams, interface
bindings, test expectations, and generated fixtures. Regenerate or edit affected
parts within scope; mark them stale and record pending work if outside scope.
If users edit a derived view to express a new requirement, reconcile it back to
the source contract before declaring the other views current. Do not silently
overwrite that input during regeneration. Follow [workflow.md](workflow.md).
