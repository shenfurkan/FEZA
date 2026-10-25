---
name: strangler-fig-migration
description: "Plans and reviews gradual replacement of a legacy pipeline behind a stable facade, with shadow comparison, bounded cutover, rollback, and evidence-based retirement. Use when old and new implementations can safely coexist for a migration period. Do not use for big-bang rewrites, irreversible side effects without safe replay, or as authorization to change the scientific model."
---

# Strangler Fig Migration

## When to use

- A legacy reader, calculation stage, or subsystem must be replaced without downtime.
- An internal dependency needs a new implementation while callers keep one interface.
- You need to decide when the old path is safe to remove.

## When not to use

- Calls cannot be intercepted and no internal integration point can be changed.
- The two implementations cannot coexist, or parallel execution would repeat
  irreversible writes or observations without a safe replay path.
- The real goal is a scientific model change; parity with the legacy result would
  hide that change rather than validate it.

## Inputs

- The legacy and new components, their callers, consumers, and owners.
- The seam where requests or stage inputs can be intercepted.
- The stable facade and the routing rule that selects the authoritative implementation.
- A predeclared comparison plan: scope, tolerance rationale, error budget, rollback
  trigger, and retirement evidence.
- The [migration contract](references/migration-contract.md) has the record format and
  the branch-by-abstraction variant.

## Procedure

1. Find the smallest seam that isolates one behavior. Prefer a stage boundary with
   explicit inputs and outputs over a shared mutable object.
2. Map every caller, including scheduled jobs, recovery paths, and backfills. If a
   caller bypasses the facade, the migration is not actually in progress.
3. Route through the facade with the legacy implementation authoritative. Record
   implementation, version, configuration, input identity, and routing decision.
4. Build one slice behind the same contract. Preserve units, masks, uncertainty,
   identifiers, time conventions, output schema, and failure semantics.
5. Freeze the comparison plan before looking at old/new differences. State the
   numerical tolerance and why it is appropriate; derive it or label it a user-supplied
   starting value.
6. Run the new slice as a read-only shadow: same inputs, separate output path,
   no external side effects. The shadow must not become authoritative by accident.
7. Investigate every disagreement. Agreement with the legacy result is regression
   evidence, not proof that either implementation is scientifically correct.
8. Cut over one accepted slice using a reversible routing decision. Keep the old path
   for the declared rollback window and reconcile state or schema compatibility.
9. Retire the legacy body only after zero calls in the justified observation window,
   caller and dependency inspection, required tests, state reconciliation, and an
   explicit ownership transfer. Missing telemetry does not prove zero calls.
10. Remove dead routing deliberately. Retain historical provenance and the archival
    decision; never delete unrecognized work.

### Worked example

A legacy FITS reader is replaced by a new reader for one instrument mode. The facade
routes reads to the legacy code while the new reader consumes the same files and writes
to a separate shadow directory. The team compares wavelengths, flux, masks, and failure
behavior against a predeclared tolerance, then cuts over that mode behind a feature
flag. If the new reader fails a validation case, routing reverts without changing the
legacy product. The old reader is retired after the declared no-call window and owner
sign-off. Matching the old reader does not, by itself, prove the reduction is correct.

## Failure modes

- **Hidden bypass:** a scheduled or indirect caller escapes the facade and stays legacy.
- **Dual authority:** old and new outputs overwrite each other or both become truth.
- **Unsafe shadow:** comparison repeats writes, spend, or protected observations.
- **Moving target:** tolerances or scope change after discrepancies appear.
- **Premature deletion:** a quiet telemetry interval is mistaken for retirement proof.

## Verification

- Trace each known caller through routing to one authoritative output and manifest.
- Inspect nominal, malformed, masked, nonfinite, and failure paths at the seam.
- Compare against an independent reference as well as the legacy result. Separate
  implementation agreement from a scientific-model claim.
- Check shadow writes are isolated and rollback restores state and schema meaning.
- Reconcile the retirement window, known callers, tests, ownership transfer, and any
  rare paths that remain unresolved.

## Provenance

- Fowler, *Original Strangler Fig Application*, 29 June 2004: the gradual-growth
  metaphor and Event Interception. The page is marked superseded by a later essay.
- Fowler, *Branch By Abstraction*, 7 January 2014: an abstraction lets old and new
  suppliers coexist during a staged switch. This is a descriptive author account.
- Microsoft, *Strangler Fig pattern*: facade routing, coexistence, cutover, and
  decommissioning, with cautions about shared state and rollback after deletion.
- These sources describe deployment mechanics, not scientific parity. Shadow safety,
  tolerance rationale, and retirement rules are project policy.

## Related locks

- [Quality ratchet](../quality-ratchet/SKILL.md) keeps replacement slices from weakening established gates.
- [AST semantic hashing](../ast-semantic-hashing/SKILL.md) separates old and new computation identities.
- [Preregistered evaluation](../preregistered-evaluation/SKILL.md) fixes cutover assessment before comparisons.
- [Circuit breaker isolation](../circuit-breaker-isolation/SKILL.md) contains a failing replacement slice.
