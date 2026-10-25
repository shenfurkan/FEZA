# Migration contract and historical attribution

## Primary basis

1. Martin Fowler, [Original Strangler Fig Application](https://martinfowler.com/bliki/OriginalStranglerFigApplication.html),
   dated 29 June 2004. The opening identifies it as superseded. The paragraph
   beginning “An alternative route” describes gradual replacement around the old
   system; the following paragraph names Event Interception. Use this to verify
   historical naming, not as a peer-reviewed rule or cost/risk guarantee.
2. Martin Fowler, [Branch By Abstraction](https://martinfowler.com/bliki/BranchByAbstraction.html),
   7 January 2014. The client/supplier sequence introduces an abstraction, moves
   callers, adds a new supplier, switches sections, then removes the unused supplier.
   The common-theme paragraph describes coexistence through an abstraction. This
   author essay is descriptive history; it does not supply scientific tolerances.
3. Microsoft Azure Architecture Center, [Strangler Fig pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/strangler-fig),
   updated 2026-06-02, snapshot 2026-10-25. “Solution” describes a facade routing
   to legacy/new services and retirement after dependencies are removed. “Problems
   and considerations” warns about shared resources, cross-system dependencies,
   facade bottlenecks and transitional cost. “When to use this pattern” gives
   inapplicable cases. “Example” requires data consistency before cutover and
   explains why deleting legacy data structures makes rollback harder.

The first two sources are primary accounts of patterns, not normative authorities.
The third is official architecture guidance, not a portability or safety guarantee.
The following scientific adaptation is project policy.

## Slice record

| Item | Record before comparison |
|---|---|
| Boundary | Seam, facade, all known callers, scope excluded and why |
| Meaning | Input/output schema, units, masks, calibration, time/frame conventions |
| Authority | Which path supplies adopted results at each stage |
| Identity | Code, environment, configuration, inputs, required RNG/state identities |
| Shadow | Safe replay/isolation method and forbidden external side effects |
| Assessment | Independent oracle, parity criterion, uncertainty/error rationale |
| Coverage | Required domains, adverse cases, denominator, caller/telemetry limits |
| Cutover | Acceptance owner, error budget, observation window, rollback trigger |
| Reversal | Routing, schema/state restoration, reconciliation and retained evidence |
| Retirement | Zero-call evidence, dependency inventory, tests, transfer and archive owner |

Each numeric tolerance, window, traffic fraction, scope target and error budget
needs a derivation or an explicit user-supplied starting-value label. Do not import
deployment percentages or generic floating-point tolerances from a web example.

## Authority and parity

- Old and new implementations may coexist; their outputs need distinct paths and
  implementation provenance. Choose one authoritative result per routed request.
- The legacy implementation is a comparator, not an independent oracle. Its errors
  may be exactly what motivated the migration.
- Changed science and changed implementation are different decisions. A new
  likelihood, calibration or approximation cannot be accepted merely by relabeling
  its discrepancy as a migration tolerance.
- Identical random seeds alone do not ensure paired stochastic calculations;
  record the estimator, generator/continuation and ordering contract when relevant.
- A read-only shadow may still consume quota or expose protected results. Planning
  shadow execution is not approval to run or upload it.

## Retirement is a separate decision

Zero observed calls is meaningful only with a declared window, complete routing
instrumentation and known population of paths. Pair it with static dependency/
caller inspection, test evidence from the project's execution environment, state reconciliation and owner
handoff. Scheduled or seasonal paths absent from the window remain unresolved.
Do not erase raw products, historical provenance, or a still-required rollback path.
Facade removal is optional if it remains a necessary adapter for supported clients.

## Review cases

| Case | Expected response |
|---|---|
| Direct legacy call discovered outside facade | Expand known scope; no retirement claim |
| Old/new parity passes but independent reference fails | Investigate common defect; no scientific acceptance |
| Shadow publishes adopted output | Block dual authority; preserve both products separately |
| Cutover requires irreversible state conversion | Establish recovery/reconciliation before switching |
| No calls logged because telemetry failed | Unresolved accounting, not zero-call evidence |

Use these cases during review; they do not certify a migration that has not been exercised.
