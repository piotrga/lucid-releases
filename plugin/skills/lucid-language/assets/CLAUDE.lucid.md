<!-- lucid-contract:start -->
## Lucid: intent → specification → tests → implementation

This project uses Lucid. Load the Lucid skill (`lucid-language:lucid-language`) before work that changes intended behavior, its implementation, or
derived artifacts.
Specification: {{SPEC_LOCATION}}. Tests and verification: {{TEST_LOCATION_OR_COMMAND}}.

The user normally talks about the application, not the spec. Treat every expressed
system-change intent as input to the contract even when Lucid is not mentioned.
Discuss goals, situations, outcomes, and tradeoffs. Derive definitions, invariants,
and technical formulations yourself; ask only about unresolved product choices.

Use simple language for readers who may not be native English speakers in the
spec, documentation, code names/comments, and dialogue. Preserve precise domain
terms and language idioms.

Follow the skill's `writing.md`: ASD-STE100 principles for prose, EARS for
requirements, C4 for architecture, ADRs for significant decisions, Design by
Contract for semantic guarantees, and Gherkin for useful behavioral examples.
Use only forms that add precision. Preserve public identifiers and a single
authoritative source for each rule; precision takes priority over notation.

For spec-only work, update the contract and record downstream impact. When implementation is also requested, follow this order:

1. **Spec first.** Read the wider relevant spec and prior decisions. Record the
   intended behavior, consequences, rationale, and adopted design choices before
   changing implementation. Keep unresolved proposals separate from agreed rules.
2. **Tests next.** Derive/update meaningful expectations from the spec, including
   relevant failure and boundary cases. Identify existing adequate coverage rather
   than duplicating it. Run targeted tests when feasible and verify that any red
   result concerns the intended behavior, not broken test setup.
3. **Implementation last.** Implement the settled contract and test expectations.
   If new behavior questions emerge, return to the spec and tests first. Never
   write code and retrospectively reshape the spec or assertions to justify it.
4. **Reconcile before completion.** Check intent, spec, tests, code, and affected
   maintained documentation/diagrams agree. Report actual verification and remaining
   uncertainty. Editing all three files or passing unrelated tests is insufficient.

For behavior already covered, identify and assess its current source rules and
tests; no cosmetic edits are needed. Refactors, configuration, and API/module
changes still account for their contract and checks before implementation.
Record work in progress explicitly: spec updated, tests pending/red, implementation
pending, verification pending, or synchronized. A TDD red stage is intentional;
it is not a completed change. Spec-only/test-only work records downstream work
as pending. Do not finalize/publish an implementation change or claim completion
with unresolved drift or required verification still pending.

Leave the touched spec better: repair small, demonstrably meaning-preserving
issues and look for shared definitions/laws across relevant contexts. Preserve
local policies, exceptions, rationale, and traceability. Propose substantial
generalizations with their domain benefit and migration scope before applying
them outside existing authorization. When preservation is uncertain, keep the
requirement and record the issue. First, do no harm.

When reported behavior differs from intent, compare the user's decisions, spec,
implementation, and observed execution. Explain the discrepancy in product terms.
A request for explanation/review stays read-only; an authorized fix includes the
necessary coordinated updates. Preserve unrelated work and existing approval,
commit, and publication rules.
<!-- lucid-contract:end -->
