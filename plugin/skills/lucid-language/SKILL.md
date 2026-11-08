---
name: lucid-language
description: Maintain .lucid specifications and derive tests and implementation from agreed behaviour. Use when adopting Lucid in a project, changing what its users experience, reviewing requirements or explaining a mismatch, even if the request does not mention the spec.
---

# Working with a Lucid project

The user decides what the system should do and why. Translate their examples
into precise definitions, rules and observable outcomes. Read [the language
reference](language.md) before writing constructs. It owns the syntax,
semantics, required slots and legacy forms.

## Start or resume

Read the project's instructions, relevant specs and durable decisions before
answering questions about its behaviour. Re-read them in a fresh session or
after losing context. Follow the project's layout. If this is its first
authorised behaviour change, create the smallest useful spec under
`spec/<domain>.lucid`. Record material unresolved choices and their basis in
the existing decision record, or `spec/decisions.md` when one is needed.
Keep an existing change log current. A review or explanation stays read-only.

## Change behaviour

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
