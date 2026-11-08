# Examples of requirements collaboration

Contents: Derive logic; ask about the product choice · Generalize across
contexts · Preserve different stronger laws · Clarify a contradiction through
a scenario · Apply an explicit change · From a scenario to a contract, tests,
and views · Diagnose an application discrepancy without a spec questionnaire

These illustrate [SKILL.md](SKILL.md), not policies for unrelated domains.

## Derive logic; ask about the product choice

User: "Two customers must not buy the last ticket."

Inspect existing purchase and reservation rules. If reservation timing is not
settled, ask:

> Does adding a ticket to the basket reserve it for that customer? If so,
> how long should it remain reserved before other customers can buy it?

Do not ask the user to write or approve the wording of an availability invariant.
The prevention of overselling is established; reservation timing is not.
Record the open decision rather than inventing a timeout.

Suppose the answer is: "Adding it reserves it for ten minutes. Removing it from
the basket cancels the reservation. At expiry it becomes available again.
A purchase must complete before expiry; otherwise the customer must reserve again."

The model derives this fragment without syntax approval:

```lucid
definition: active ticket reservation — a ticket reservation that has not
  become a confirmed purchase, has not been cancelled, and whose expiry
  time is later than the current time
  meets:
    - an unconverted, uncancelled reservation one minute before expiry
  meets-not:
    - a reservation at its expiry time
    - a reservation already converted to a confirmed purchase

definition: available ticket — an unsold ticket with no active ticket reservation

invariant ticket_reservation_duration:
  a reservation expires ten minutes after it is created
  because: a basket holds a ticket temporarily while its customer decides

invariant ticket_purchase_requires_active_reservation:
  a purchase can be confirmed only while its customer's ticket reservation is active
  because: an expired reservation no longer protects the ticket for that customer

invariant ticket_has_one_current_allocation:
  a ticket has at most one active reservation; a sold ticket has no active reservation
  because: customers must not receive competing commitments for the same ticket
```

This is a partial fragment, not a complete ticketing spec. Creation, cancellation,
conversion, payment, and refunds require their own behavior definitions. If a
pending payment at expiry has no agreed outcome, ask about that scenario.

Check checkout, expiry, availability displays, and simultaneous claims against
the updated definitions. Report their consequences and remaining decisions.

## Generalize across contexts

While editing tickets, the model finds room reservations elsewhere. Both agreed
contracts prevent commitments beyond available capacity, but their expiry and
cancellation policies differ.

Share the capacity law if both contracts support the mapping. Retain separate
domain definitions. Do not invent one global expiry policy because current
values happen to match.

> Both reservation flows protect available capacity. I have expressed that
> shared rule once and retained their separate expiry and cancellation policies.

The model writes mappings and laws. It asks only about undecided behavior,
such as whether several groups may share a room reservation.

## Preserve different stronger laws

Exact event counts and ordered histories can share associative combination with
an empty result, per [generalization.md](generalization.md). Preserve history
order and do not assume duplicate-insensitive merging. Do not ask the user to
choose between a monoid and another type class.

If repeated delivery could mean the same event or a new one, ask whether it
should appear/count twice in the concrete situation.

## Clarify a contradiction through a scenario

One rule allows cancellation until dispatch; another forbids cancelling paid
orders. Inspect scope and precedence first. If neither resolves it, ask:

> A customer's order is paid but has not been dispatched. Should they still
> be able to cancel it? The current requirements give different answers.

After the answer, update eligibility, its definition, dependent guarantees, and
scenarios. Ask separately if refund behavior remains unknown. Do not silently
choose a refund policy to make the spec look complete.

## Apply an explicit change

User: "Increase basket reservations from ten to fifteen minutes."

Update the ticket duration and actual dependents, inspect wider context and
possible generalizations, and preserve independent room policies. Record the
change without asking for approval of the invariant or reconfirming the duration.

## From a scenario to a contract, tests, and views

Illustrative agreed scope: a submitted request may be withdrawn or approved.
The first action processed for that request succeeds; later actions are rejected
without changing its outcome. Simultaneous actions have no preferred winner.
Actor authorization is already checked before this scoped operation. Each request
has one logical decision owner; deployment and transport have not been chosen.

The model identifies request identity, terminal outcomes, and a per-request
consistency requirement. It does not infer a microservice or a database transaction
from the single-owner rule. A readable source contract can express:

```lucid
role RequestDecision:
  purpose: let a submitted request reach one final outcome
  assumes: actions for this request are processed serially against its latest state
  state:
    status: Submitted or Withdrawn or Approved = Submitted
  accepts:
    Withdraw():
      purpose: stop this request before approval
      fails when: status is not Submitted
      guarantees: succeeds exactly when status was Submitted before this action
      effect:
        on success: status becomes Withdrawn; the caller receives Withdrawn()
        on failure: state unchanged; the caller receives AlreadyDecided(status)
    Approve():
      purpose: accept this request before withdrawal
      fails when: status is not Submitted
      guarantees: succeeds exactly when status was Submitted before this action
      effect:
        on success: status becomes Approved; the caller receives Approved()
        on failure: state unchanged; the caller receives AlreadyDecided(status)
  invariant terminal_outcome_is_final:
    WHILE status is Withdrawn or Approved,
    THE request decision owner SHALL retain that status
    because: a request must not be both withdrawn and approved
```

This is a logical fragment for one request, not a complete authorization, routing,
durability, or deployment specification. Its serial-processing assumption needs
an adopted enforcement mechanism before claiming concurrent system correctness.
The prose contract also preserves the absence of a preferred simultaneous winner.

The model extracts this transition view from the handlers:

| Source | Action | Resulting state | Reply |
|---|---|---|---|
| Submitted | Withdraw | Withdrawn | Withdrawn |
| Submitted | Approve | Approved | Approved |
| Withdrawn or Approved | Either action | Unchanged | AlreadyDecided(current status) |

Use Gherkin for contrasting acceptance examples of the general rule:

```gherkin
Feature: One final request outcome
  # Source: RequestDecision handlers and terminal_outcome_is_final
  Scenario Outline: The first processed action decides the request
    Given a request has status Submitted
    When the owner processes <first> and then <second> for that request
    Then <first> succeeds and sets status to <final>
    And <second> receives AlreadyDecided(<final>) without changing state

    Examples:
      | first    | second   | final     |
      | Withdraw | Approve  | Withdrawn |
      | Approve  | Withdraw | Approved  |
```

A test expecting withdrawal to win every race would add a policy. A test merely
checking a terminal final status would miss success replies to both callers.
These examples illustrate the handlers; they do not replace their general rules
or establish that executable tests have run. The EARS invariant and Gherkin cases
use complementary forms from [writing.md](writing.md), without a new Lucid syntax.

For documentation and diagrams, derive views from these same rules:

- User: withdrawal works while the request is still awaiting a decision; a
  request already approved cannot be withdrawn through this operation.
- PM: simultaneous withdrawal/approval yields one final outcome, with no promised
  priority. Any proposed priority is a new product choice.
- Architect: one decision owner per request and a serial-processing requirement;
  the mechanism enforcing that requirement remains to be designed.
- Engineer: logical commands and outcome payloads are known; an HTTP route,
  status code, persistence strategy, and concrete module mapping are not yet
  adopted. Choose them only in authorized design work and record the bindings.
- State diagram: draw the two outgoing transitions from Submitted and annotate
  later requests as rejected without changing state.
- Sequence diagram: show either permitted order, or alternatives, and label the
  chosen trace as illustrative. Do not imply one order is mandatory.
- Module map: show the logical responsibility and its callers; a concrete service
  topology requires an adopted mapping rather than renaming each role a service.

## Diagnose an application discrepancy without a spec questionnaire

User: "Why can't I cancel this paid order? We agreed I could cancel before dispatch."

Inspect the accepted decision, eligibility definition, application path and
reported state. If evidence shows the spec permits cancellation but the handler
rejects every paid order, explain that mismatch in those terms. If the old spec
still forbids cancellation despite the accepted decision, identify that drift as
well. Ask about refunds only if that outcome is actually unresolved. A request
to explain does not itself authorize edits; a fix request includes the necessary
coordinated changes and a regression scenario.

During the fix, reuse an equivalent eligibility definition and repair affected
references yourself. If several other domains could share a broader cancellation
model, propose that generalization with its supported common laws and preserved
differences. Do not spread this order's cancellation policy across those domains.
