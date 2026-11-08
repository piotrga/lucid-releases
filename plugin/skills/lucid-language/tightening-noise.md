# Expression, redundancy, and preservation of meaning

Contents: What counts as removable noise · Review patterns · Definitions and
generalization · Technical detail and abstraction level · Preserve these ·
Review and output

Use with [tightening.md](tightening.md). Improve readability while preserving
requirements, domain distinctions, rationale, and meaningful examples.
The model writes the revised definitions and invariants itself.

Classify the information before rewriting it, using [writing.md](writing.md).
Apply the matching convention to artifacts and use progressive disclosure in
dialogue. A shorter sentence is an improvement only if it preserves meaning.

## What counts as removable noise

A phrase is removable when its deletion loses neither a behavioral constraint
nor information needed to understand, locate, or justify that constraint.
For a whole requirement, identify the retained requirements that entail it.
An expectation of what a reasonable implementation would do is insufficient.

Check the complete proposed result. A requirement moved to another layer must
exist there as part of the same authorized change; a note suggesting someone
restore it later is not preservation. If that move is out of scope, retain the
requirement and propose the coordinated change.

## Review patterns

Legacy pattern IDs remain recognizable; their meaning is subordinate to
preservation of requirements and the conversation contract in SKILL.md.

| ID | Candidate | Decision criterion |
|---|---|---|
| N0 | Difficult language | Explain unfamiliar terms; keep precise domain and mathematical vocabulary where useful |
| N1 | Throat-clearing | Remove a preface if it adds no orientation or meaning |
| N2 | Repeated intensifiers | Remove only words that bind no amount, certainty, or obligation |
| N3 | Description repeats a field name | Keep units, scope, defaults, and non-obvious meaning |
| N4 | Narration of document structure | Keep orientation that helps the reader navigate |
| N5 | Vague qualifiers | Determine whether uncertainty or implementation freedom is intentional before changing it |
| N6 | Rationale paraphrases the rule | Explain its established stakes; a weak rationale does not prove the rule is unnecessary |
| N7 | Inconsistent presentation | Make proportionate mechanical fixes; avoid taste-based reports |
| N8 | Implementation detail | Retain agreed technical contracts; omit incidental mechanisms only if no requirement is lost |
| N9 | Several independent obligations | Split where meanings or reasons differ; conjunction and sentence length alone are not grounds |
| N10 | Length obscures meaning | Clarify or organize without losing conditions, exceptions, or rationale |
| N11 | Repeated definition body | Reuse a named concept only when membership, scope, and time are equivalent |
| N12 | Hard-to-scan names | Choose descriptive domain names while preserving reference integrity |
| N13 | Apparently obvious behavior | Remove only if explicit retained requirements entail it; preserve essential contracts |

Prefer short sentences with one main idea while retaining their conditions.
Do not impose a reading-score threshold, a source-document word limit, or a
positive count of findings. Preserve each requirement and its rationale when shortening the text. Technical prose can contain
algebraic terms. Explain them through their consequences for the domain when
speaking to the user. Never mistranslate a technical term to make it simpler.

## Definitions and generalization

Extract recurring meanings into definitions and reuse them at all equivalent
sites. Search beyond the current file, following [generalization.md](generalization.md).
Check both membership and exclusions. Similar conditions in different scopes
may deserve separate definitions or share only part of their logic.

A shared definition may have multiple clauses when they describe one concept.
Do not automatically union scattered conditions: they may be alternatives,
exceptions, incompatible definitions, or rules for different times. Determine
which from the spec; ask about a distinguishing user scenario when unresolved.

After extracting a definition, review all affected consumers. Preserve their
additional constraints. Introducing "overdue loan" does not by itself require
a portal to display those loans, specify their order, or grant access to them.

## Technical detail and abstraction level

Talk to the user about goals, situations, and observable outcomes. Keep precise
technical details in the spec when they define a real contract, such as a wire
format, compatibility promise, deadline, or required consistency guarantee.
An API consumer is also an audience; its observable result may include a status
code or representation. Do not automatically reduce every contract to a screen.

If multiple mechanisms satisfy the same complete requirements, the choice can
remain in implementation. If a required technical detail belongs in another
spec module, move it coherently while retaining a reference. Internal ownership
alone does not make a constraint removable; external ownership alone does not
make an assumption true.

`because:` states why a requirement matters. It does not need to identify a
mutex, scheduler, or database to earn its place. A separate assumption or rule
records whatever enforcement contract the guarantee relies on.

## Preserve these

- User-approved outcomes, exceptions, and acceptance boundaries, including
  concurrency, retries, recovery, and behavior once thought "obvious".
- Rationale that explains a real stake or a choice between valid policies.
- Examples that distinguish interpretations or preserve a regression scenario.
- Definitions, units, source links, dependency references, and scoped assumptions.
- Intentionally unspecified choices and the bounds on consumer expectations.
- Mathematical laws needed for a valid shared abstraction and local stronger laws.

## Review and output

Inspect the relevant text, propose clearer wording, then compare its meaning
against retained requirements and relevant scenarios using
[tightening-coherence.md](tightening-coherence.md). Do not label sampled agreement
as proof of equivalence. Keep unverified conditions visible.

Use the compact format in tightening.md. Show important user consequences or
questions first. A routine formal rewrite needs no separate question. Respect
report-only requests and apply already-authorized edits without reopening
approval for every phrase. Zero findings is a valid result.
