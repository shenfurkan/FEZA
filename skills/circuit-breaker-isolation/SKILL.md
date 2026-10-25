---
name: circuit-breaker-isolation
description: "Designs isolated batch execution so one crashing or hanging candidate cannot erase unrelated work, with typed failures, bounded retries, breaker recovery, and complete accounting. Use when running many independent jobs against fallible inputs or shared services. Do not use to hide failed targets, to retry non-idempotent effects, or to claim process isolation from a library configuration alone."
---

# Circuit Breaker Isolation

## When to use

- Many independent candidates run against inputs that may crash, hang, or exhaust memory.
- A shared dependency can fail without invalidating unrelated work.
- You need a run manifest that distinguishes failure, deferral, quarantine, and success.

## When not to use

- A scientific nondetection or model-domain rejection is being relabeled as an
  infrastructure error.
- Shared state, a global input, or the result writer is corrupted; stop the affected
  run instead of continuing with invalid results.
- Retries would duplicate non-idempotent effects such as writes, charges, or observations.

## Inputs

- The candidate list, immutable input identities, ownership, and dependency graph.
- A failure taxonomy: transient, permanent, poisonous, unknown, and cancelled.
- Process or container isolation, wall-clock deadline, memory limit, and cleanup policy.
- A retry budget, jitter policy, and the breaker's failure domain.
- Trip threshold, counting window, minimum evidence, cooldown, and recovery rule.
- The [isolation contract](references/isolation-contract.md) covers state transitions
  and the partial-result manifest.

## Procedure

1. Classify failures before choosing behavior. Transient dependency failures may
   retry; permanent schema or configuration errors stop the item; poisonous inputs
   are quarantined; unknown failures stay unresolved; cancellation is not retryable.
2. Put each candidate in an owned process or container. A timeout in a thread does not
   stop native code, and a container declaration does not enforce a memory limit.
3. Enforce an independent wall-clock watchdog, memory boundary, bounded cleanup, and
   separate output path. Terminate only process groups you own.
4. Check available CPU, memory, disk, and accelerator capacity before admitting work.
   Bound worker and native-library pools. Shrink the working set, never the scientific
   sample, precision, or coverage requirement.
5. Retry only classified transient, idempotent operations. Bound attempts, total wall
   time, and backoff. Specify the jitter distribution; keep scheduling randomness away
   from scientific RNG streams.
6. Give each breaker a real failure domain. A poisoned candidate must not open a global
   breaker for healthy work; a shared outage may defer dependent work without deleting
   candidates from the manifest.
7. Define the states explicitly. CLOSED admits and records outcomes. OPEN rejects or
   defers matching calls for a finite cooldown. HALF-OPEN admits one probe at a time
   (project policy: one probe; change it only with evidence). A failed or timed-out
   probe reopens the breaker.
8. Validate the output contract and finish an atomic write before marking a candidate
   complete. Quarantine partial or invalid artifacts.
9. Reconcile the original list with completed, failed, quarantined, deferred, cancelled,
   and unresolved states. Keep attempt history, causes, denominators, and an explicit
   partial-run manifest.

### Worked example

Three hundred spectral fits run against a shared archive. One corrupt file crashes a
worker, and the archive starts timing out. Each fit runs in its own process with a
deadline and memory cap; the corrupt file is quarantined, and the archive breaker
defers the dependent fits while unrelated local fits continue. The manifest reports
297 complete, 1 quarantined, and 2 deferred. The report says coverage is 297 of 300,
not that "all sources fit". The counts illustrate the accounting, not a threshold.

## Failure modes

- **Pseudo-isolation:** a timed-out thread or unconstrained child exhausts the parent.
- **Retry storm:** permanent or poisonous failures retry, duplicate effects, or reset budgets.
- **Global trip:** one candidate disables unrelated healthy work through a shared key.
- **Probe herd:** concurrent half-open calls exceed the recovery admission rule.
- **Survivor bias:** failed or deferred targets disappear from the denominator.

## Verification

- Inspect the process boundary, enforced limits, watchdog independence, and cleanup.
  Configuration alone does not show runtime containment.
- Trace each failure class to a distinct status and a retained cause.
- Review CLOSED, OPEN, and HALF-OPEN transitions at the threshold, cooldown boundary,
  and concurrent probe admission.
- Check retry exhaustion and jitter cannot change scientific draw identity or overwrite
  completed outputs.
- Reconcile every candidate and attempt, including partial writes and writer failure.
- Demonstrate containment and recovery in the actual target environment before
  claiming them.

## Provenance

- Nygard, *Release It!* (2007), publisher-authorized preview, §4.3: cascading failures,
  resource-pool exhaustion, and the complementary roles of timeouts and breakers.
  Only the preview was available; the detailed breaker chapter was not read.
- resilience4j v2.3.0, `CircuitBreaker.java` and `CircuitBreakerConfig.java`: states,
  permissions, configurable thresholds, windows, permits, and waits. The source comments
  contain unresolved discrepancies about state counts and threshold equality; verify
  the exact version before relying on boundary behavior.
- Failure taxonomy, process containment, single-probe recovery, and scientific
  accounting are project policy. No product default or book excerpt establishes them all.

## Related locks

- [Quality ratchet](../quality-ratchet/SKILL.md) prevents failures from laundering gated metrics.
- [AST semantic hashing](../ast-semantic-hashing/SKILL.md) distinguishes complete and quarantined artifact identities.
- [Strangler fig migration](../strangler-fig-migration/SKILL.md) limits cutover failure to the affected slice.
- [Preregistered evaluation](../preregistered-evaluation/SKILL.md) freezes failure and exclusion accounting before assessment.
