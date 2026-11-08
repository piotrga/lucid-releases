# Requirement consistency and completeness

Contents: Establish context · Turn intent into a domain contract · Classify
what the evidence shows · Cover relevant behavior · Distinguish
interpretations with concrete cases · Derive, then ask only what remains
undecided · Check logical claims honestly · Preserve meaning when rewriting ·
Finish with an assessed scope

Use this reference while authoring or changing requirements and during semantic
review. The conversation and authority rules in [SKILL.md](SKILL.md) apply.
The model performs the logical work; the user resolves product choices.

## Establish context

Read the changed requirement, its rationale, relevant definitions, assumptions,
prior decisions, and dependent behavior. Search the wider spec for other uses
of the same concept and analogous behavior with different names. Follow
cross-file references in both directions. Inspect the surrounding constructs;
a matching sentence alone can hide a different scope or precondition.

Build enough of a requirement map to connect user needs to rules, scenarios,
and dependents. Use existing names or IDs rather than adding a separate index
for a small spec. Distinguish explicit references, relationships inferred from
prose, and unresolved relationships. Only a tool-backed graph over defined
references supports claims of mechanically computed completeness.

## Turn intent into a domain contract

Use this loop for a new capability or a material semantic change. The model
chooses the useful notation; the user answers product questions, not the steps
of a modeling worksheet. Existing adequate information need not be restated.

1. Identify the actor, goal, observable outcome, scope, and rationale from the
   request and existing spec. Extract the important domain terms and decisions.
2. Describe the main example as initial domain conditions, a trigger, and an
   expected result. Contrast it with a relevant boundary, refusal/failure, or
   interacting case. Use the contrast to expose the condition that changes
   behavior, rather than inventing more decorative examples.
3. Locate each term's meaning within its domain context. Resolve synonyms and
   distinguish terms with different meanings in different contexts. Identify
   identity, values, lifecycle ownership, and operations where they matter.
4. Derive a rule covering the meaningful input/state partitions. For complex
   branches, use a decision table: conditions, allowed result, excluded result,
   and source. Identify uncovered cases and compatible/competing overlaps.
   For stateful behavior, form transitions using language.md's conventions.
5. Locate where an invariant must hold and which operations can violate it.
   Identify required coordination and failure outcomes before choosing a
   mechanism. A requirement spanning owners is not enforced merely by naming
   each owner or declaring its handlers pure.
6. Read analogous contexts and perform [generalization.md](generalization.md).
   Check the proposed general rule against the original cases and a case that
   challenges it. Preserve local policy and supported implementation freedom.
7. Resolve uncovered product outcomes from prior decisions or focused questions.
   Record the rules, rationale, dependencies, and material unresolved decisions.
   Check whether a meaningful test oracle and applicable system views can be
   derived; use a missing fact discovered there to refine the source contract.

The domain modeling perspective follows
[Eric Evans' DDD Reference](https://www.domainlanguage.com/ddd/reference/):
use a shared language within explicit contexts, model identity and values
deliberately, and establish consistency boundaries around domain rules.
For Lucid, contexts are boundaries of meaning; aggregates, when appropriate,
describe consistency ownership. Neither implies one microservice, one database
table, or one spec file. Cross-context mappings can translate distinct models
without forcing a global canonical entity. Apply useful concepts without
requiring every project to adopt every DDD pattern. These instructions are
self-contained; the link is background, not a routine prerequisite.

## Classify what the evidence shows

| Finding | Evidence needed | Response |
|---|---|---|
| Contradiction | An applicable situation in which requirements demand incompatible outcomes | Check scope and precedence; ask if the product choice is unresolved |
| Ambiguity | Two supported readings produce different observable outcomes | Show a distinguishing scenario and ask |
| Missing decision | A relevant scenario has no specified outcome or permitted range | Ask about that behavior; record what depends on it |
| Compatible overlap | Requirements constrain the same subject and can hold together | Keep both or derive an equivalent clearer formulation |
| Redundancy | Named retained requirements imply the candidate's full content | Consolidate while preserving rationale and references |
| Unsupported guarantee | The described behavior and assumptions do not establish the promised result | Locate the missing condition; ask about any new product choice |
| External assumption | The requirement relies on an environmental condition | Record the condition, available evidence, and behavior if it fails when material |

For example, a group may require at least two and at most ten participants.
Both rules constrain group size without contradicting each other. A different
rule demanding at least twelve participants in the same situation conflicts.

A new request can intentionally replace an earlier rule. Follow explicit
supersession and inspect the consequences; do not ask the user to reconfirm
the change. If it is unclear whether the request replaces the rule, creates
an exception, or concerns another scope, ask using a concrete scenario.

## Cover relevant behavior

For each affected user capability, consider these dimensions when applicable:

- Who may act, on what, under which conditions, and with what visible result.
- Ordinary success; empty, absent, invalid, and boundary inputs.
- Denied actions and failures, including partial completion and recovery.
- Cancellation, repeated requests, retries, and concurrent actions.
- Time: expiry, deadlines, ordering, stale observations, and eventual progress.
- Interactions with other capabilities, shared resources, and exceptions.
- Agreed non-functional requirements such as latency, access, retention, or
  capacity when they constrain this behavior.

These are model-facing lenses, not a questionnaire to read to every user.
Do not manufacture features or ask about irrelevant failure modes. Prioritize
gaps that affect current behavior, undermine a guarantee, or have broad impact.

An assessed scenario has one of three outcomes: specified behavior, explicitly
bounded freedom, or an open decision. "The implementation will choose" is
valid only when that freedom is intended and consumers know its bounds.
Do not count an unresolved proposal as coverage.

## Distinguish interpretations with concrete cases

Apply the logical-contract conventions in [language.md](language.md). For a
materially ambiguous clause, identify the alternative readings and a situation
where their allowed outcomes differ. Resolve it from definitions and decisions;
ask about the user-visible difference when neither reading is established.
Formatting a sentence as a predicate does not remove ambiguity in its terms.

Check necessary versus sufficient conditions, bound variables, quantifier scope,
overlapping guards, missing cases, units, equality, and inclusive/exclusive time
boundaries where relevant. For stateful behavior, inspect pre-state, event,
guard, post-state, unchanged state, outputs, and failure paths together. A guard
without an outcome does not describe a complete transition.

Distinguish underspecification from intended freedom: if either concurrent
request may win, preserve that choice while forbidding two winners. An example
showing one winner supplies no priority policy. Where outcomes are intentionally
open, state their bounds so an implementation and a test can respect them.

Check the human explanation against the same rule: a reader should be able to
locate the applicable conditions, expected consequence, and reason, including
exceptions, without reconstructing an unexplained mathematical hierarchy.

Assess derivability using [projections.md](projections.md): can the relevant
transitions, interactions, documentation claims, and test expectations be traced
to actual requirements? Missing API or implementation mappings can block that
engineering view without making the product requirement undecided. Resolve
ordinary authorized design choices as design choices, not invented product rules.

## Derive, then ask only what remains undecided

Create definitions, predicates, invariants, and their wording yourself.
Infer logical consequences of agreed rules and cite their basis. A plausible
domain convention is a proposal, not an agreed requirement. Inspect existing
decisions before asking, and distinguish uncertainty about product intent
from uncertainty in your own analysis.

A question contains the situation, the competing outcomes or missing behavior,
and the decision needed. Offer concise options and their consequences when
helpful. Ask a small batch of the highest-impact independent questions; keep
the others in the decision record described in [workflow.md](workflow.md).

Example:

> A customer cancels after payment but before shipment. Cancellation is
> allowed, but the refund is unspecified. Should cancellation automatically
> issue a full refund, or send the request to support?

Do not turn this into "What should the refund invariant say?" or request
approval for the names and syntax needed to express the answer.

After an answer, update its definition sites, applicable rules, exceptions,
dependent guarantees, and scenarios. Verify the answer against other agreed
requirements. If it reveals a new contradiction, ask about that concrete
consequence. Do not ask already-resolved questions again without new evidence.

## Check logical claims honestly

- **Rationale alignment:** check that the rule serves the stated need. A
  rationale does not uniquely determine a predicate, threshold, or policy.
  Different valid formulations are not automatically evidence of a defect.
- **Counterexamples:** try situations and event sequences that would violate
  the claim. When testing whether a rule is redundant, reason without that
  rule while retaining the other requirements. Including the rule among the
  assumptions would make the test circular.
- **Absence of a counterexample:** report that none was found in the inspected
  cases. It does not prove a rule is vacuous, redundant, or universally true.
- **Safety and progress:** "never double-charge" constrains what can happen;
  "eventually refund" also needs progress assumptions and possibly a deadline.
  An instantaneous-state example cannot check every temporal property.
- **Enforcement:** a deterministic decision does not imply safe concurrent
  updates. Ordered messages do not imply eventual delivery. Examine the
  scenario or trace that connects an assumption to the promised outcome.
- **Evidence:** distinguish source requirements, model reasoning, executed
  checks, and any formal proof. Never label generated examples as executed
  tests or manual inspection as a parser/solver result.

Multiple generations can explore alternatives when available and appropriate,
but their agreement is not a confidence score or a substitute for evidence.
Do not describe repeated passes in the same context as independent reviews.

## Preserve meaning when rewriting

Compare requirements before and after, including quantifiers, boundaries,
permissions, exception priority, ordering, and time. Use representative
positive and negative scenarios, relevant boundaries, and event traces.
Check that each original requirement can still be recovered from the result.

Examples provide counterexamples or supporting evidence; a fixed number of
matching examples cannot prove semantic equivalence. Use a suitable checker
for executable fragments when available. State unverified areas explicitly.
If the rewrite would make a new product choice, surface that choice before
applying the dependent change. Routine formalization needs no separate approval.

## Finish with an assessed scope

Record the inspected contexts, resolved findings, open decisions and their
impact, and any uninspected dependencies. Stop when the relevant coverage
review and change-impact work are complete or the remaining work depends on
specific answers. Do not describe the entire system as complete because the
model stopped finding issues in one pass. Recheck affected coverage after
answers or material changes rather than repeating every check mechanically.
