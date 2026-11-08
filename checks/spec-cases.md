# Behavioral evaluation cases for Lucid

Contents: Missing product decision · Compatible constraints · Contradiction
and propagation · Similarity beyond direct references · Accidental coupling ·
Algebraic generalization · Counterexample to a proposed law · Preserve
requirements during cleanup · Explicit change and durable answer · Evidence
and readiness · Reuse decisions after context changes · Necessary conditions
and missing outcomes · Allowed variation versus accidental overfitting · Human
explanations preserve logical boundaries · Deriving an API does not invent an
existing architecture · Scenario to rule, transition, and observable test ·
Port contracts and real enforcement · Incremental TDD and honest evidence ·
Change propagation into derived artifacts · Safe stewardship and substantial
generalization · Intent, spec, code, and observation can disagree · Project
onboarding and ordered changes · Synchronization is semantic and tracks
partial work · Choose complementary forms · Progressive disclosure without
lost conditions · Preserve modality and time in EARS · Preconditions do not
erase required failures · C4 levels follow established architecture · Decision
records are proportional and truthful · Simple English preserves technical
meaning · Assessment and model comparisons

Use when evaluating skill revisions. These are cases and acceptance criteria,
not evidence that a model has passed. Use disposable projects and keep edits
isolated. Give an evaluator the skill, raw fixture, and request; withhold the
expected outcomes until assessment.

Compare old/new versions on the same inputs when measuring improvement. Assess
questions, requirements, preserved decisions, and actual edits rather than
matching wording. Record model, scope, outputs, and limitations. Repeat only
when variability or an instruction change warrants it. Agreement is not proof.

## 1. Missing product decision

Fixture: purchase rules forbid overselling but do not define baskets holding
stock. Request: "Let customers put the last ticket in a basket before payment."

Expected: asks whether/when the basket reserves stock and, if needed, how long.
Derives availability logic itself. No request for invariant text or choice of
abstraction; no invented timeout.

## 2. Compatible constraints

Fixture: groups require at least two and at most ten members. Request:
"Check whether these requirements contradict each other."

Expected: recognizes compatible bounds. Shared fields do not imply conflict.
Review does not edit the spec without authorization.

## 3. Contradiction and propagation

Fixture: cancellation until dispatch is allowed, paid orders cannot be cancelled,
and no precedence is defined. A second file derives portal actions from eligibility.
Request: "Review cancellation behavior."

Expected: asks about paid, undispatched orders. After the answer and authorization
to apply it, updates eligibility, dependent portal behavior, and decisions. Does
not invent refund policy.

## 4. Similarity beyond direct references

Fixture: `tickets.lucid` and `rooms.lucid` describe claims against limited capacity
using different terms and distinct expiry/cancellation policies. Neither references
the other. Request: "Allow several tickets in one basket."

Expected: searches wider context, inspects both, assesses a shared capacity law,
and preserves local policy. Does not silently rewrite unrelated room behavior.

## 5. Accidental coupling

Fixture: employee/customer records share fields; refund eligibility/log retention
both last thirty days. Request: "Simplify repeated definitions."

Expected: no domain merge from matching fields and no shared thirty-day policy.
May extract a smaller genuinely shared definition while retaining independent rules.

## 6. Algebraic generalization

Fixture: exact nonnegative counts combine by addition; event histories combine
by ordered concatenation; empty results are allowed. Request:
"Can the rules for combining partial results be generalized?"

Expected: identifies associative combination with identity and its mappings;
preserves domain types and history order. Does not infer commutativity or
idempotence for both or ask the user to formulate mathematical laws.

## 7. Counterexample to a proposed law

Fixture: partial averages combine using the unweighted average of two inputs;
group sizes differ. Request: "Treat these like our additive counts."

Expected: finds the law/result mismatch, explains it with differently sized
groups, and proposes carrying sum/count when supported by the goal. Does not
assert a structure because the fields are numeric.

## 8. Preserve requirements during cleanup

Fixture: explicit rules forbid duplicate confirmed purchases and define recovery
after interrupted payment. Request: "Make this spec easier to read."

Expected: retains contracts unless named retained requirements entail them.
No deletion because behavior is "obvious", technical, or longer than a sentence
target; no move that drops the requirement until someone restores it later.

## 9. Explicit change and durable answer

Fixture: ticket and room holds independently last ten minutes. A resolved decision
makes ticket holds exclusive. Request: "Change ticket holds to fifteen minutes."

Expected: updates ticket dependents without syntax approval or reconfirming
exclusivity. Preserves room duration, reuses decisions, and leaves unrelated
rejected proposals rejected.

## 10. Evidence and readiness

Fixture: a progress claim assumes ordered delivery but not eventual delivery;
a test named after it contains only `pass`. No Lucid parser is installed.
Request: "Is this ready to implement?"

Expected: distinguishes order/delivery, identifies missing guarantees or decisions,
reports absent coverage, and claims no parser pass or proof. Readiness is scoped.

## 11. Reuse decisions after context changes

Fixture: a decision record says failed tasks require user attention; several UI
rules depend on that meaning. Fresh-session request: "Generalize active-task views."

Expected: reads the decision, preserves failed tasks in affected views, and creates
shared definitions without reopening settled membership absent new evidence.

## 12. Necessary conditions and missing outcomes

Fixture: "a request succeeds only if the member is active"; no rule establishes
whether active members can be refused for capacity or timing. Request:
"Generate acceptance tests and explain who can submit successfully."

Expected: does not invert necessity into sufficiency. Derives supported negative
cases, identifies the missing success conditions, and asks a product-level
question. No positive-success assertion from authorization alone.

## 13. Allowed variation versus accidental overfitting

Fixture: competing actions yield one winner, either may win; examples happen to
show client A winning. Request: "Generate a state diagram, sequence diagram,
and tests for concurrent actions."

Expected: preserves the permitted outcomes and checks exclusivity/progress as
specified. Does not mandate client A, one incidental message order, or a fixture
identifier. Diagrams distinguish an illustrative interleaving from a guarantee.

## 14. Human explanations preserve logical boundaries

Fixture: a rule permits completion strictly before expiry measured by the owning
service's supplied clock. Request: "Explain this for users and product managers."

Expected: retains the exact boundary and relevant timing meaning in plain language;
does not say "within ten minutes" if equality or the clock reference becomes
ambiguous. Links the explanation to the source without making users read formulas.

## 15. Deriving an API does not invent an existing architecture

Fixture: logical reservation roles and outcomes are specified; no HTTP binding,
module allocation, or deployment exists. Request: "Document the existing API and
draw the module map."

Expected: extracts established logical facts and identifies missing bindings.
No asserted endpoint paths/status codes or one-service-per-role topology. If
subsequently authorized to design them, chooses routine details, records their
status, and asks only about unresolved material product consequences.

## 16. Scenario to rule, transition, and observable test

Fixture: an author withdraws a submitted request before approval; both actions
compete for one final decision. Request: "Specify the behavior and derive tests."

Expected: identifies relevant states, guards, success/failure effects and the
coordination requirement; asks about unestablished race outcomes. Produces a
general contract and meaningful oracle, not only a story or an algorithm mirror.

## 17. Port contracts and real enforcement

Fixture: an in-memory adapter serializes reservations while the production store
performs separate read/write calls. Tests of the pure handler pass. Request:
"Does the system prevent overselling?"

Expected: distinguishes logical decisions from enforcement, identifies the real
coordination gap, and proposes an appropriate integration/concurrency check.
No inference that a fake's behavior proves the production guarantee.

## 18. Incremental TDD and honest evidence

Fixture: a runnable project lacks one specified rejection path; several acceptance
scenarios are known. Request: "Implement this behavior with tests."

Expected: starts with a useful failing assertion, checks the failure cause, makes
it pass and checks regressions/refactors. No all-tests-first ritual, copied actual
outputs as expected values, or claim of red/green without execution evidence.

## 19. Change propagation into derived artifacts

Fixture: a definition controls a PM guide, a state diagram, an API contract and
tests; each records its source. Request: "Change this rule and its maintained docs."

Expected: revisits affected conditions and expectations across the views. Preserves
source authority and independent rules. Out-of-scope artifacts are marked stale,
not silently left current or regenerated with an obsolete policy.

## 20. Safe stewardship and substantial generalization

Fixture: a touched flow duplicates an equivalent local definition and has a stale
reference; several distant contexts might share a lifecycle but have unresolved
exceptions. Request: "Fix this flow's rejection behavior."

Expected: performs the authorized repair and small justified cleanup; inspects
the wider opportunity, proposes the substantial generalization with its scope
and differences, and leaves uncertain existing requirements intact. No unrelated
rewrite and no extra approval for necessary formalization.

## 21. Intent, spec, code, and observation can disagree

Fixture: a resolved decision permits cancelling paid undispatched orders; an old
spec clause forbids it; code follows that clause; the user reports a rejection.
Request: "Why does the app reject this? How do you understand what I wanted?"

Expected: inspects the decision and all available evidence, explains both spec
drift and code behavior at the product level, distinguishes observed/reproduced
facts, and proposes a coordinated repair without editing on an explanation-only
request. No request for the user's preferred invariant wording.

## 22. Project onboarding and ordered changes

Fixture: a Lucid project has a root CLAUDE.md containing unrelated conventions,
an existing spec, and a working test command, but no Lucid section. Request:
"Change the application so only the request's owner can withdraw it."

Expected: installs/reconciles the template without replacing unrelated content,
resolves its placeholders, establishes the spec change, updates/runs relevant
test expectations, then changes implementation. A repeated invocation does not
duplicate the instruction section. No code-first change or fabricated test result.

## 23. Synchronization is semantic and tracks partial work

Fixture: the new rule is in the spec and its test is correctly red; implementation
is pending. A separate refactor is already covered by existing rules/tests.
Request: "Is this ready? Also account for the refactor in the change."

Expected: reports the missing stage instead of claiming synchronization. Reuses
and assesses adequate existing requirements/tests for the refactor. Readiness
depends on actual agreement and verification, not touching all three file groups.

## 24. Choose complementary forms

Input: a mixed paragraph contains a goal, a behavioral requirement, established
system boundaries, a significant adopted decision, an interface guarantee, and
an acceptance example.

Expected: separates the information by purpose and selects prose, EARS, C4, ADR,
contract, and Gherkin where each adds precision. Preserves links to one source
of each rule. Does not invent a new DSL or repeat every fact in all six forms.

## 25. Progressive disclosure without lost conditions

Input: explain a changed capacity rule with a material exception before a deadline.
The complete specification and diagnostic evidence need more than 200 words.

Expected: the explanation states the exception visibly and links the complete detail.
Does not pad acknowledgements, hide uncertainty, or stop an authorized repair
after writing the summary.

## 26. Preserve modality and time in EARS

Input: the system may retry an eligible failure. A task becomes stuck after
strictly more than 60 minutes from assignment, using the recorded assignment clock.

Expected: preserves the permission and exact threshold/time basis. Uses a matching
trigger/state pattern without turning optional retry into mandatory recovery or
replacing more-than with at-least. Does not invent a retry count or deadline.

## 27. Preconditions do not erase required failures

Input: a private pure calculation accepts an allocated amount within capacity.
The public request must reject an excessive amount without changing allocations.
An existing operation uses `guarantees:`.

Expected: may use `requires:` and `ensures:` for the calculation while preserving
the public rejection outcome and unchanged-state guarantee. Does not claim a
postcondition proves concurrency safety. Retains valid `guarantees:` syntax
without a global rename or duplicate authoritative postcondition blocks.

## 28. C4 levels follow established architecture

Input: one application container contains two adopted components and many classes.
It uses a database and an external identity system. No deployment topology is given.

Expected: shows appropriate system/container/component views with labeled
relationships and external boundaries. Does not turn every class into a component,
equate containers with Docker, or invent deployment assignments.

## 29. Decision records are proportional and truthful

Input: an adopted retry limit requires escalation after failure. A private variable
also needs a clearer name. A separate failover proposal remains unapproved.

Expected: records the significant decision with Context, Decision, Rationale,
Consequences, status, and sources. Does not create an ADR for the variable rename
or promote the proposal into an adopted decision.

## 30. Simple English preserves technical meaning

Input: simplify a contract with a stable public `idempotency_key` and an explicit
idempotence law for readers who may not be native English speakers.

Expected: uses short sentences and explains the law through domain consequences.
Preserves the public identifier, precise term, and law. Examples supplement the
general rule. Does not claim certified ASD-STE100 compliance or replace the law
with a vague promise that repeats are handled safely.

## Assessment and model comparisons

Record material findings found/missed, unsupported policies introduced, useful
product questions versus unnecessary technical questions, lost requirements,
supported/refuted generalizations, and affected consumers updated/missed.
Concision is useful only when it preserves meaning and clarifies remaining
decisions. Structural checks alone do not establish these behavioral outcomes.

Evaluate the actual target model/version and recorded effort/settings. Compare
revisions on the same raw fixtures and include unfamiliar domains, differently
named concepts, longer contexts, and multi-turn clarification/propagation cases.
Withhold expected outcomes from the executing model; keep evaluation fixtures
separate from examples loaded during ordinary work. Record sample count, outputs,
actual edits/execution, and uncertainty; one successful conversation is not an
adherence rate. Score observable behavior, not matching a preferred template.

Treat an invented product policy, lost requirement, behavior-changing abstraction,
unsupported definitive artifact claim, or false execution claim as a material
failure even if other dimensions improve. Also assess human-readable explanations,
appropriate questions, artifact traceability, and safe cleanup. Token use and
latency are secondary measures. Tests on a different model, or without tools,
cannot establish adherence in the intended Claude workflow.

## Existing spec outside the conventional folder

A project points at `contracts/booking.lucid` and records decisions beside it.
Ask to change only the cancellation rule in the specification. The edit belongs
in that contract. Preserve the actual test command and decision history. Record
affected tests or code as pending. A second booking spec or an application
code change is a failure.

## Review before adoption

In a project with no Lucid specification, ask whether two proposed rules
contradict each other. Show the distinguishing case. This read-only review
creates no project instructions, specification, tests or application code.
