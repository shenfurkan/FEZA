# Isolation, recovery admission and scientific accounting

## Primary basis and limits

1. Michael T. Nygard, *Release It! Design and Deploy Production-Ready Software*,
   copyright 2007, ISBN 978-0-9787392-1-8. The
   [publisher-authorized preview](https://media.pragprog.com/titles/mnee/mnee-antipatterns.pdf)
   identifies printing P3.0, February 2009, version 2009-3-27. The wrapper bears a
   2009 publisher copyright. Section 4.3, printed pp. 67–69 (PDF pp. 4–6), describes
   cascading failures, resource-pool exhaustion and the complementary roles of
   timeouts and circuit breakers. **The full book was not reviewed.** Its detailed
   Circuit Breaker chapter is absent from this preview and is not cited as read.
2. resilience4j v2.3.0, [CircuitBreaker.java](https://raw.githubusercontent.com/resilience4j/resilience4j/v2.3.0/resilience4j-circuitbreaker/src/main/java/io/github/resilience4j/circuitbreaker/CircuitBreaker.java),
   snapshot 2026-10-25, lines 37–55 describe ordinary transitions;
   `tryAcquirePermission`/`acquirePermission`, lines 433–473, describe permission
   handling; `State`, lines 810–837, describes ordinary and special states.
3. resilience4j v2.3.0, [CircuitBreakerConfig.java](https://raw.githubusercontent.com/resilience4j/resilience4j/v2.3.0/resilience4j-circuitbreaker/src/main/java/io/github/resilience4j/circuitbreaker/CircuitBreakerConfig.java),
   snapshot 2026-10-25. `failureRateThreshold`, lines 391–410; open-wait and
   half-open wait/permit methods, lines 452–569; sliding/minimum-call methods,
   lines 572–678; exception classification, `recordExceptions`/`ignoreExceptions`,
   lines 715–823.
   It documents configurable thresholds, evidence windows, permits and waits,
   not process isolation or a universal scientific failure threshold.

The official documentation site was unavailable during source collection; these
direct first-party API/source files are the retained documentation instead.
Both Java files carry Apache-2.0 headers. The retained evidence is static source,
not runtime behavior.

### Preserve documentation discrepancies

The interface opening says “five states” while its enum includes `METRICS_ONLY`
as well as the other five. Lines 53–54 overlap at equality: the first says reopen
at/above the threshold, the next says close below/or equal. The config threshold
documentation says opening occurs at/above. The half-open wait comment also
mentions `minimumNumberOfCalls`, while a separate setting configures half-open
permits. Do not resolve these inconsistencies by assertion. The retained public
source does not establish internal state-machine behavior. Verify the intended
version's boundaries before adopting that library; retain these gaps meanwhile.

## Project policy, not product defaults

| Boundary | Explicit contract |
|---|---|
| Failure domain | Candidate-specific poison versus shared dependency outage |
| Transient | Bounded retry only when idempotency and recovery plausibility hold |
| Permanent | Stop affected work; retain schema/configuration/domain cause |
| Poisonous | Quarantine input/artifacts; replace only the owned contaminated worker |
| Unknown/cancelled | Preserve uncertainty; cancellation cannot trigger retries |
| Isolation | Owned process/container plus independently enforced memory/wall-clock limits |
| Admission | Actual allocation/headroom, justified working set, bounded native pools |
| CLOSED | Admit under a declared evidence window and trip rule |
| OPEN | Defer/reject matching calls; record cause, finite cooldown and budget |
| HALF-OPEN | One atomic probe per cycle, explicitly user-supplied policy |
| Recovery | Valid successful probe closes; failed, timed-out or indeterminate probe reopens |
| Publication | Validate output contract, finish atomic write, then mark completion |
| Accounting | Every original target remains represented, even when no result exists |

A valid model-domain rejection may be a scientific result under its declared
model, not a software exception. A malformed observational input is not such a
result. Preserve the distinction rather than using one catch-all failure code.

All numeric trip/window/minimum-call criteria, cooldowns, retry counts, deadlines,
memory limits, concurrency and jitter parameters need retained measurement-based
justification or a user-supplied starting-value label. The single-probe rule is
this guide's policy; resilience4j permits configurable counts and its documented
default is not copied. A breaker does not stop a running
call, enforce memory, or make an unsafe operation idempotent.

## Partial-result manifest

Keep candidate/input identity, current status, attempts and UTC events, classified
cause, deadline/resource outcome, breaker identity/transitions, artifact paths and
validation/completion state. Include original/attempted/completed/failed/quarantined/
deferred/cancelled/unresolved denominators and overlap rules for attempt-level counts.
Candidate final states must be unambiguous; historical failed attempts remain visible
even after later success. A writer/supervisor failure leaves the run incomplete.

Never encode failed targets as zero measurements, empty catalogs, nondetections,
or successful exclusions. If failures depend on signal strength or target properties,
the scientific selection effect remains unresolved until assessed separately.
Scheduling jitter must not consume the scientific RNG stream or change draw ordering.

## Paper verification cases

| Case | Required observation before runtime acceptance |
|---|---|
| One candidate crashes | Owned child is contained; unrelated work survives; failure remains counted |
| Shared dependency is unavailable | Its breaker defers dependent work without deleting candidates |
| Two workers seek a half-open permit | Only the single admitted probe is allowed |
| Probe hangs or returns invalid output | Bounded cleanup and reopening; no false recovery |
| Retry budget expires | Terminal/deferred status is explicit, not an endless retry loop |
| Shared writer/state is corrupted | Affected run stops or remains incomplete; no success manifest |

Use these cases to design a containment test; they are not evidence that containment works.
