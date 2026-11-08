# Explain and repair discrepancies in behavior

Use when the user says the application behaves incorrectly, asks what the model
understands a requirement to mean, or suspects that intent, spec, and code differ.
The application is the topic of the conversation; Lucid is the model's working
contract. Follow [SKILL.md](SKILL.md) for authority and user-level communication.

## Establish the distinguishing situation

Use the reported scenario and existing decisions to determine expected and actual
observable outcomes. Ask for the smallest missing fact that distinguishes the
readings: what action occurred, in which relevant situation, what happened, and
what was expected. Do not ask the user to locate a file or formulate an invariant.
Use accessible evidence before asking them to repeat information.

Keep a new desired behavior distinct from a report about previously agreed
behavior. If the user's new instruction explicitly changes the policy, apply its
authorized consequences; do not defend the old spec as the user's true intent.
If the report is ambiguous, explain the conflicting outcomes and ask about those.

## Compare four sources

| Source | What to inspect | What it establishes |
|---|---|---|
| Intent | Current request, original scenarios, accepted decisions | Desired outcomes and explicit changes; recollection without evidence remains uncertain |
| Specification | Applicable definitions, rules, scope, assumptions, dependencies, decisions | Outcomes the written contract permits, requires, or leaves undecided |
| Implementation | Relevant decision path, state ownership, adapters, configuration, tests | What the inspected code/configuration expresses; reading code is not observing its execution |
| Observation | Reproduction, logs/traces, stored state, environment, user report | What happened in the observed situation, subject to evidence and environment limits |

Trace the reported action through the relevant guards, transitions, interactions,
and outputs. Read the surrounding contract and dependent contexts, not only the
sentence matching the user's words. Use a minimal reproduction or behavioral
test when feasible and authorized; avoid modifying live state just to diagnose.
Distinguish the user's report from independently reproduced evidence.

## Locate the discrepancy

- **Intent versus spec:** find the missing, conflicting, or overstated rule.
  Explain the situation and difference; derive the repair from established intent
  or ask about a genuine product choice.
- **Spec versus implementation:** locate the code path or missing enforcement
  that violates the agreed contract. Do not redefine the contract to excuse it.
- **Implementation versus observation:** inspect configuration, deployment,
  persisted state, timing, external systems, and the assumptions used in analysis.
  Report hypotheses as hypotheses until evidence supports them.
- **Derived artifact versus source:** identify stale tests, diagrams, or docs.
  Reconcile their source and baseline rather than treating generated text as an
  independent policy decision.

There may be several discrepancies, including shared mistakes in the spec and
tests. Passing tests do not settle the user's intended behavior. If sources are
unavailable, state exactly which comparison remains unverified and continue the
independent diagnosis. Do not fabricate certainty by selecting one source.

## Explain at the user's level

Lead with a concrete account: "I understand that cancelling before dispatch
should stop the order, including paid orders. The spec contains that rule, but
the application rejects every paid order on this path." Say this only when the
evidence supports it. Explain a remaining decision through competing outcomes.

Give the answer first and keep material uncertainty visible. Link the complete
diagnostic evidence separately; the short report must not interrupt an authorized
repair or limit the diagnostic artifact's contents.

Provide concise source links or formal details on request or when they resolve
a contested point. Do not make the user review a SpecDelta, state table, or type
hierarchy to obtain an explanation. The model maintains those details itself.

## Repair within the authorized scope

An explanation/review request produces findings and a proposed correction.
A fix request authorizes the necessary coordinated edits. Preserve the reported
scenario as a regression case, establish its expected outcome from intent/spec,
then follow [spec-derived tests](spec-tests.md) and [lowering.md](lowering.md) as applicable.
Update the source contract when it is wrong or incomplete; update the code when
it diverges; repair both when required. Maintain decisions and affected derived
views per [workflow.md](workflow.md).

Apply small meaning-preserving cleanup to the touched area under the safe
stewardship rule. Propose larger generalizations separately with their benefit
and migration scope. Report the resulting application behavior, evidence that
the discrepancy is resolved, and specific remaining uncertainty. Do not claim
a production incident is fixed merely because a local model or unit test passes.
