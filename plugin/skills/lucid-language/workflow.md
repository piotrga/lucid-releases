# Ordered changes, persistence, and project onboarding

Contents: Maintain the agreed contract · Durable decisions · Change impact
(SpecDelta) · Spec → tests → implementation · Save and verify · Review
baselines · Initialize the project instruction contract

Follow [SKILL.md](SKILL.md) for authority and conversation. Use this reference
when saving requirements, applying reviewed changes, or onboarding a project.

## Maintain the agreed contract

Use the project's existing layout. Usual Lucid locations are:

- `spec/<context>.lucid`: current agreed requirements and derived rules.
- `spec/changes.log`: append-only record of material accepted changes.
- `spec/decisions.md`: material questions, proposals, and resolved decisions
  when there is no existing equivalent.

Create only needed files. Exploratory discussion does not authorize adopting
Lucid across a repository. Once maintenance is authorized, keep the spec in
sync without asking separately for each derived definition or invariant.
Infer a new context's home from the project when clear; ask about actual domain
ambiguity, not routine filenames. Preserve unrelated local edits. This skill's
commit conventions do not independently authorize commits or publication.

Keep agreed behavior and adopted technical bindings at identifiable source sites.
Their logical consequences reference those sources; drafts and external
assumptions retain their status. Follow [projections.md](projections.md) for
derived artifacts. Use an existing layout/decision mechanism for this distinction
instead of requiring one file or directory per audience.

## Durable decisions

Record each material open decision with a stable ID, user-level scenario and
question, affected requirements, options if useful, status, and what depends
on the answer. Record the inspection that found the gap. Proposed answers
must not appear as agreed behavior in normative requirements.

Statuses distinguish `open`, `proposed`, `resolved`, `rejected`, and `superseded`.
Resolution includes the answer, its actual source (the user's words, an
earlier decision, or a choice the model made within delegated authority), and
affected constructs.
Preserve links to earlier decisions when superseding them. Rejected proposals
stay rejected unless new evidence makes them relevant again.

For significant architectural or engineering decisions, use an ADR with Context,
Decision, Rationale, and Consequences. Retain status and source links. Use the
project's existing ADR location and link it from affected spec constructs; do not
copy competing decisions into both records. Routine local choices need no ADR.
Follow [writing.md](writing.md) for selection and concise expression.

Use actual statements or available source references. Do not invent message
IDs, approvals, dates, or evidence. Derived requirements cite their agreed
basis rather than pretending the user dictated their wording.

A temporary draft assumption stays labeled as a proposal outside the normative
spec. Do not silently use it as a premise for implementation or generalization.
Continue independent work while awaiting answers.

## Change impact (SpecDelta)

Keep a structured impact summary when useful. It is model bookkeeping and
optional review detail, not a form for the user:

```text
SpecDelta
  intent: <source requirement or accurate paraphrase with reference>
  adds: <new definitions and requirements>
  removes: <constructs and retained basis or superseding decision>
  modifies: <constructs and meaning before/after>
  conflicts_with: <incompatible outcomes in a concrete scenario>
  implies_changes: <affected consumers, claims, code, checks>
  derived_artifacts: <affected tests, documentation, diagrams, interface bindings>
  generalization: <shared basis, applications, preserved differences>
  open_questions: <unresolved product decisions>
```

Omit empty fields in summaries and lead with behavior. Authorized edits do
not require a second approval of their SpecDelta. Advice/review-only tasks
remain proposals until application is authorized. Honor explicit review gates.

Follow declared references and inspect semantic dependencies between definitions,
invariants, flow guarantees, messages, relations, and system-level claims.
Compatible overlap is not a contradiction. For weakened or removed rules,
revisit known dependents and search for unlinked uses. Follow
[tightening-coherence.md](tightening-coherence.md).

## Spec → tests → implementation

Apply this order to every authorized system change, including fixes requested in
application language and technical work that affects a contract. Maintain a small
change record in the project's existing plan/decision mechanism: intent and source,
affected spec constructs, test cases/evidence, implementation locations, derived
artifacts, current stage, and unresolved work. Reuse existing records; no mandatory
new database or duplicate checklist. Keep the user-facing discussion about behavior.

1. **Establish the contract.** Inspect current rules and decisions, then write the
   intended change and its consequences to the spec. For already-specified behavior,
   identify the applicable rule and assess it. Record ambiguities as open decisions;
   settle only what follows from accepted intent or authorized design choices.
2. **Establish its verification.** Derive or update test expectations from those
   rules, including relevant regression cases. Identify existing adequate tests
   instead of duplicating them. Run the targeted tests when feasible and record
   the real result; a missing behavior should fail for the intended reason.
   Follow [spec-derived tests](spec-tests.md) for contract-derived verification.
   A tool/environment failure is not behavioral red.
3. **Implement the established change.** Modify only behavior whose contract and
   test expectations are settled. Routine coding and design choices remain the
   model's responsibility within those constraints. If coding reveals a new
   product choice, return to the source contract and tests before its implementation.
4. **Reconcile the result.** Check the combined diff against the intent, source
   rules, assertions, observed behavior, and affected maintained views. Record
   actual test results and remaining gaps. Completion requires agreement in the
   requested scope; passing unrelated tests or merely editing all three places
   does not demonstrate synchronization.

A behavior-preserving change still maps to the requirements and checks that must
remain true. An internal restructuring can reuse them if they are sufficient;
adopted module/API mappings are updated before their implementation changes.
Documentation or spec-only work uses appropriate semantic/structural verification
and identifies downstream impact without manufacturing a production code change.

Record stages such as contract updated, tests pending/red, implementation pending,
verification pending, or synchronized. These describe progress, not alternative
authorities. Do not conceal temporary drift, claim a generated test ran, or mark
the whole system synchronized when only a subset was assessed. If required checks
cannot run, leave verification pending and report the concrete limitation.

Before marking an implementation change complete or finalizing/publishing it,
require traceable intent, a settled contract, meaningful checks with actual
results, conforming implementation, and current in-scope derived artifacts.
Explicitly requested WIP checkpoints remain WIP and disclose the outstanding
stage; they never establish readiness. Git operations still need task authorization.

## Save and verify

Apply authorized changes across affected definitions and consumers coherently.
Check their combined effect and preserve meaningful examples. Resolve a decision
when dependent requirements are updated, or clearly record pending work.

Append to the existing project change log (default `spec/changes.log`) for each material accepted change, with date,
context, changed behavior, reason, and source. Append at the end; newest-first
ordering belongs in a view. Preserve prior entries. For an existing reverse-
chronological log, record the append convention once without reordering history.

If maintaining per-file history blocks, add records without rewriting earlier
entries and link to the main change/review. Avoid repeating a full narrative.
Recheck external assumptions after incidents or environmental changes; periodic
calibration applies only when the user or project has adopted a schedule.

Spec, code, and checks for implemented behavior changes should be reviewed and,
when committing is requested, committed together. Spec-only design work may
record implementation as pending. Clarified requirements need no gratuitous
code edit when existing code already satisfies them; record the evidence.
Read [lowering.md](lowering.md) for implementation work.

Maintain a lightweight mapping from source constructs/baselines to the generated
artifacts that depend on them, using existing test metadata and documentation
references where possible. An accepted change includes reassessing affected
expectations and diagrams, not just regenerating wording. Update maintained
outputs within scope; record stale sections and pending regeneration otherwise.
Do not generate every audience document on every change.

Record routine technical decisions made within authorized design work with their
reason and constraints; do not attribute them to user approval that did not occur.
An observed implementation fact remains evidence, not a product decision, until
its relationship to the agreed contract is resolved. Preserve explicit design
review gates without adding approval requests for ordinary representation choices.

## Review baselines

Saved reviews record hashes of actual input files, including uncommitted content.
The Git commit is optional context; `HEAD` alone does not anchor a dirty working
tree. Before applying a proposal, compare against the reviewed content and
reassess changed context instead of blindly applying stale fragments. Ask only
about newly unresolved behavior.

## Initialize the project instruction contract

Run on explicit onboarding or before the first authorized change in a project
using Lucid when its instruction contract is absent or outdated. A read-only
explanation/review does not bootstrap files, and exploratory discussion does not
adopt Lucid across an unrelated repository.

1. Locate the project root and inspect existing `CLAUDE.md`, scoped instruction
   files, spec/test locations, decisions, and established tooling. Respect genuine
   project constraints; resolve conflicting instructions instead of leaving two
   contradictory workflows active.
2. Merge the section from [assets/CLAUDE.lucid.md](assets/CLAUDE.lucid.md) into
   the root `CLAUDE.md`, creating that file if needed. Preserve unrelated content
   and existing user edits. Replace the template's spec/test placeholders
   with verified project locations or the actual established test command.
   Keep the skill reference as the template gives it: the skill's name, never
   a file path on one machine.
   Where a test command does not exist, say so explicitly; do not invent one.
3. If the environment also uses `AGENTS.md` or another entrypoint, add a concise
   reference to the shared contract where needed rather than copying independently
   maintained variants. This supplements the requested `CLAUDE.md` contract.
4. Check the effective section states the ordered change rule, behavior-level
   dialogue, writing conventions, safe stewardship, and honest conditions for
   work in progress and completion.
   Verify local links/paths, reconcile duplicate Lucid sections, and confirm no
   unresolved placeholders. Re-running onboarding must not append another copy.
5. Report the installed instruction location briefly and continue the authorized
   task. Do not make the user approve individual clauses already requested here.

Do not copy the full skill into project instructions. Maintain this short contract
and the skill reference by name so future sessions on any machine load the same
operating rules.
Lack of Git does not block local setup. Onboarding authorizes neither a commit
nor publication. A prompt instruction improves adherence but is not a mechanical
merge gate; do not claim CI enforcement unless a real project check exists.
