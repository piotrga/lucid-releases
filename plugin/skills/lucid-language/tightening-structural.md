# Structural review

Use with [tightening.md](tightening.md). The slot table in
[language.md](language.md) is authoritative; do not maintain a competing one.
Structural review checks the shape of the specification. Semantic review
checks whether its promises actually fit together.

## Checks

| ID | Defect | Resolution |
|---|---|---|
| S1 | Required slot missing | Derive the content from agreed intent, or ask about the missing user outcome |
| S2 | Construct in a misleading or unsupported location | Move the whole construct while preserving meaning and references |
| S3 | Reference does not resolve to a declaration | Find the intended declaration or surface the unsupported dependency |
| S4 | Required slot is empty or a placeholder | Fill from established requirements; keep unresolved behavior explicit |
| S5 | Duplicate slot with conflicting or scattered content | Consolidate compatible content; investigate conflicting outcomes |
| S6 | Required construct name missing or ambiguous | Choose a stable descriptive name and update references yourself |

Inspect whole constructs and their scopes. Read the actual definition sites;
a text search hit on the reference itself does not establish that a target
exists. Do not fix a missing `rests_on` target merely by deleting the dependency:
the system-level claim may have lost its basis. Check its meaning and affected
consumers before choosing a repair.

Some checks are mechanical when a suitable parser exists. Conditional slots,
ambiguous names, and meaningful rationale still require interpretation. Use
available tools and report their actual results. Manual inspection is not a
successful parse, and the Sublime highlighter does not validate semantics.

## Preserve intent

A missing rationale can often be drafted from the user's goal. It should not
invent a benefit or change the requirement to justify itself. If the intended
outcome is genuinely unknown, ask about a scenario; do not ask the user to
compose the missing slot.

When a structural repair might alter behavior, follow
[tightening-coherence.md](tightening-coherence.md). Preserve definition membership,
branch scope, temporal conditions, and declared assumptions. Verify the combined
result of related repairs and update cross-file references.

## Legitimate forms

- `purpose:` on a self-explanatory pure intent is optional.
- `assumes:`, `fails when:`, and `guarantees:` are required when the construct
  relies on the corresponding conditions or outcomes, not on every construct.
  `ensures:` can express the postconditions instead of `guarantees:`. `requires:`
  identifies caller obligations; it must not hide a required rejection outcome.
- Handlers under `accepts:` declare their messages inline. Reply payloads may
  be constructed in `effect:` without a separate message declaration.
- Invariants can belong to an entity or role as well as appear at top level.
- Existing `tightening_history:` and `calibration_history:` blocks are metadata.
- Legacy forms documented in language.md are compatibility cases, not grounds
  for a compulsory migration during unrelated work.

## Output

Use the findings format in tightening.md. Explain any behavioral consequence
first; names, slot repairs, and reference locations are supporting detail.
Group repairs to one construct when they form one coherent change. Surface
material semantic gaps discovered during this review, even if their resolution
needs the coherence analysis. Do not fabricate a finding when the structure
is already sound.
