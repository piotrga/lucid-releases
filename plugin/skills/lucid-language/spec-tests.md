# Derive checks from an agreed rule

1. Identify the rule, its scope, assumptions, observable result and rationale.
2. Build one example and a contrasting case at the boundary. For a transition,
   record the prior state, event, result, resulting state and observable effects.
3. Exercise relevant failure, retry, ordering, concurrency and recovery cases.
   For allowed variation, assert the set of acceptable outcomes. Keep an
   unresolved product choice in the decision record.
4. Map each expectation to a source rule and each material rule to a relevant
   check or an explicit coverage gap. Review existing tests first.
5. Run at the boundary that owns the guarantee. A pure transition test can
   establish a local rule. A concurrent uniqueness claim also needs evidence
   at the shared coordination boundary. Report what actually ran.

For example, two buyers try to buy the last ticket. Observe the replies to
both buyers and the persisted sales. A final inventory of zero alone would
miss a success response to both buyers. See [worked examples](examples.md).
