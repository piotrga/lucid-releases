---
name: lucid-language
description: Write, review and maintain .lucid specifications. Use for requirements, decisions, readiness and discrepancies in Lucid projects, including behaviour changes described in application terms.
---

# Working with a Lucid project

The user decides what the system should do and why. Translate their examples
into precise definitions, rules and observable outcomes. Read [the language
reference](language.md) before writing constructs. It owns the syntax,
semantics, required slots and legacy forms.

## Choose the reference for the job

| Task | Read |
| --- | --- |
| Write a rule, define vocabulary or specify a transition | [Language](language.md), [writing forms](writing.md) |
| Turn examples into obligations, find missing choices or contradictions | [Coherence and scenario coverage](tightening-coherence.md) |
| Test a proposed shared concept against exceptions | [Generalisation](generalization.md) |
| Split a growing spec by domain or responsibility | [Modularity](modularity.md) |
| Review or simplify a spec while preserving its meaning | [Review order](tightening.md), [structure](tightening-structural.md), [wording](tightening-noise.md) |
| Onboard a project, record a decision or propagate a change | [Project workflow](workflow.md), [project contract](assets/CLAUDE.lucid.md) |
| Derive documentation, state machines, message sequences or API views | [Projections](projections.md) |
| Map settled requirements to implementation and observable checks | [Lowering](lowering.md), [spec-derived tests](spec-tests.md) |
| Explain a difference between intent, spec, code and observed results | [Diagnostics](diagnostics.md) |
| See worked examples with decisions and counterexamples | [Examples](examples.md) |

Read the references needed for this task, the affected constructs, their assumptions and prior decisions before acting. After a context reset, reload them before describing their rules.
On the first authorised change, follow the project onboarding in [workflow.md](workflow.md).
During a review, report findings with the smallest case that distinguishes the outcomes.
When editing, follow affected consumers and preserve meaning, rationale, boundaries
and traceability. Keep a larger redesign as a separate proposal.

## Start or resume

Read the project's instructions, relevant specs and durable decisions before
answering questions about its behaviour. Re-read them in a fresh session or
after losing context. Locate the authoritative spec using the project's instructions and existing
layout. Update the rule where it already lives. When no existing construct
owns the agreed behaviour, add it in the appropriate domain. Use
`spec/<domain>.lucid` as the default for a new Lucid project. Record material unresolved choices and their basis in
the existing decision record, or `spec/decisions.md` when one is needed.
Record material accepted changes in the project change log as described in [workflow.md](workflow.md). A review or explanation stays read-only.

## Change behaviour

A spec-only request ends after the requirements, decisions and affected references
are reconciled. Record downstream tests or implementation as pending where needed.
Follow the full sequence below when implementation is also requested.

1. **Spec first.** Locate the rule and its dependants. Record the agreed
   outcome, scope, exceptions and rationale. Distinguish the user's decisions
   from their logical consequences, proposals and observations of current code.
   Use a concrete case to ask about choices that change an outcome. Leave
   those choices open and continue with settled behaviour.
2. **Tests next.** Derive expectations from the rule. Check existing coverage
   before adding cases. Include meaningful boundaries and failures. Run the
   targeted test when possible and check why it failed.
3. **Implementation last.** Implement the settled behaviour. Check the
   resulting outcome against the spec and tests. Report what ran, the observed
   result and anything still pending. For a spec-only request, record downstream
   work as pending.

When behaviour differs, compare the user's decision, the normative rule,
the implementation and an observed run. Each answers a different question.
Preserve agreed meaning and rationale during cleanup.

## Decide whether a rule is ready

For each material scenario, identify an expected outcome, the explicit bounds
of permitted variation, or an open decision. Ask about a gap using one case
where the possible answers would change what a user sees. Label recommendations
as proposals. Record the decision, its basis and affected rules when it is settled.
A request to change behaviour authorises its necessary consequences across the
spec. A review stays read-only.

For a material change, inspect analogous rules as well as named dependencies.
Share an abstraction only when meanings, operations, laws and assumptions agree.
Try a counterexample and retain independent policies. Preserve conditions,
exceptions, modality, time, rationale and traceability during cleanup. For
an allegedly redundant rule, identify the retained rules that imply it.

Before handoff, follow affected consumers through the maintained views, test
expectations and implementation. Report what is ready, the evidence, and which
specific unresolved decision or missing check still controls an outcome. For
a wording-only edit, check that the meaning is preserved.

## Worked example

“Two people must never buy the last ticket” gives a rule even while the
reservation policy is open.

```lucid
invariant a_ticket_has_at_most_one_buyer:
  Each individual ticket may be sold to at most one buyer.
  because: each ticket admits one person
```

Check two simultaneous purchases of the same ticket. Observe the recorded
sales and each buyer's result. The rule forbids two successful buyers. It
leaves open whether putting a ticket in a basket reserves it. Ask about that
choice before implementing a basket hold.
