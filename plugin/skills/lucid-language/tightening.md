# Tightening — preserve requirements while improving their expression

Contents: Stewardship during ordinary changes · Scope and authority · Review
order · Preserve meaning · Findings the user can act on · Report and apply

Read [SKILL.md](SKILL.md) first. Tightening makes an agreed specification easier
to understand and maintain. It preserves its behavior, rationale, and coverage.
A missing product decision is surfaced through a user scenario rather than
quietly resolved during cleanup.

## Stewardship during ordinary changes

Use the safe stewardship rule in [SKILL.md](SKILL.md) even when the user has not
requested a dedicated cleanup pass. Inspect the semantic neighborhood touched
by an authorized change; fix small demonstrably equivalent issues alongside it.
Preserve the source basis, compare the aggregate result, and keep the change
reviewable. A plausible simplification without an equivalence basis stays a
proposal. Never repair uncertainty by weakening a requirement or strengthening
an optional choice into a mandate.

For a substantial opportunity, prepare a concise domain-level proposal: common
meaning/laws, affected contexts, local differences, benefit, and a migration
and validation plan. Keep the requested change progressing independently.
Do not treat a large line count as a reason to defer necessary consequences of
an already authorized requirement change. Read-only reviews remain read-only.

## Scope and authority

Start from the requested concept or file. Inspect its coupled definitions,
consumers, claims, and analogous constructs elsewhere in the spec. Analysis
may be wider than edits. Explain a material scope expansion; an unrelated
rewrite remains a proposal. Infer the target from context when unambiguous.

A request for a review or report produces a report. An explicit request to
apply findings or edit the spec authorizes the corresponding meaning-preserving
changes; do not request approval for each technical fragment again. Honor an
explicit report-only workflow and previous authorization in the conversation.

For saved reports, use the existing project location or
`tests/tightening_examples/<concept>.tightening.md`. Anchor the actual contents
of all reviewed files with hashes, plus the Git commit if available. See
[workflow.md](workflow.md) for stale proposals and decision records.

## Review order

Use these lenses in dependency order, at a depth proportionate to the task:

| Lens | What to establish | Reference |
|---|---|---|
| Structure | Constructs and references are understandable and well formed | [tightening-structural.md](tightening-structural.md) |
| Coherence and coverage | Requirements agree and relevant behavior is accounted for | [tightening-coherence.md](tightening-coherence.md) |
| Redundancy | A retained requirement actually entails the proposed removal | This file and [tightening-noise.md](tightening-noise.md) |
| Generalization | Recurring requirements have a sound shared basis; accidental policies stay local | [generalization.md](generalization.md) |
| Derivability | Requested tests, documentation, and diagrams have sufficient source facts and faithful mappings | [projections.md](projections.md), [spec-derived tests](spec-tests.md) for test work |
| Expression | Clarity improves without losing conditions, stakes, or traceability | [tightening-noise.md](tightening-noise.md) |

Subset reviews are allowed. Report their inspected scope and material skipped
checks. A discovered contradiction should be surfaced even during a wording
pass; do not suppress it because another pass owns that category. Do not
claim that an unperformed check passed.

## Preserve meaning

For each substantive rewrite, map the original requirements to the retained
or new constructs. Check conditions, quantifiers, boundary values, exceptions,
allowed choices, time, and ordering. Exercise useful distinguishing scenarios
or event traces. Review the combined effect of interacting rewrites.

A few matching scenarios support the review but do not prove equivalence.
Do not call model self-checking a proof. If the new text changes an observable
outcome, it is a requirement change and follows the authority and clarification
rules in SKILL.md. If a cleanup cannot be justified, retain the requirement
and surface the concrete uncertainty rather than deleting it.

Overfitting is addressed by deriving a supported general rule while retaining
meaningful examples and exceptions. Over-generalization is addressed by finding
where the proposed shared laws fail, not by banning mathematical vocabulary.

## Findings the user can act on

Lead with behavior and decisions. A finding should be understandable without
knowing Lucid syntax. Use stable finding IDs and clickable links supported by
the current interface; use absolute-path links in Codex, not `file://` URIs.

For a material finding include:

- **Situation and consequence:** what a user or operator can do or observe.
- **Finding:** the gap, contradiction, or opportunity and its evidence.
- **Proposed resolution:** the behavior retained/changed and affected areas.
- **Question:** only when an unresolved product choice needs an answer.
- **Supporting detail:** the proposed Lucid fragment, relevant scenarios,
  dependency changes, and verification limits when useful for review.

For a simple wording change, a before/after with a brief explanation is enough.
Lead with the finding that changes a decision and link to the full review.
Do not force every finding into a large template or fixed scenario count.
Group edits that implement one coherent decision; keep
independent product choices separately decidable. Technical names and formal
predicates are supporting detail, not the question addressed to the user.

Prioritize contradictions and missing decisions, then meaningful shared
concepts and redundancy, then wording. Rank by effect on understanding and
behavior rather than how many lines can be deleted. Zero findings is valid;
never manufacture issues to meet a quota.

## Report and apply

A saved report records the scope, baseline hashes, performed checks, substantive
findings, unresolved questions, and relevant limitations. Include outside-scope
concerns when they affect an assessed guarantee; do not create external tasks
or mutate other systems without authorization. Keep the summary focused on
the decisions and consequences that deserve the user's attention.

When findings are accepted or application was already authorized, check the
baseline, apply the coherent changes, update dependencies and the decision
record, and reassess affected scenarios. Use the user's amended outcome where
provided and derive its formalization yourself. Record material changes per
[workflow.md](workflow.md). A rejected proposal stays rejected unless new
information changes its basis.

Stop when the requested scope has been assessed and each material finding
is resolved or recorded with a concrete next decision. A clean wording pass
is not evidence that the requirements are globally complete.
