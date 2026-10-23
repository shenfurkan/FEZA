---
name: scientific-repair-not-deferral
description: "Use when a scientific calculation, numerical fit or physical model fails, especially when an agent substitutes disclaimers, deferred status, widened tolerances, self-referential tests, mocked physics or repeated plans for a repair. Require a justified intervention at the actual consumer, independent scientific checks, verified units and applicability, relevant convergence evidence and measured before-and-after results. An honest blocker is unfinished work, not a completed repair."
license: MIT
---

# Scientific Repair Is Not a Disclaimer

> **Investigate the failure. Make the justified intervention. Measure the effect.**

Treating disclaimers, widened tolerances and deferrals as completed work is a
failure of scientific coding. Explaining why something failed is not repairing it.
For an authorized repair request, the only acceptable **completed repair** is a
justified intervention, working code at the actual consumer, and measured
before-and-after evidence against an independent expectation.

This is a working discipline, not a promise that every requested conclusion is
physically possible. Missing observations, non-identifiability, a disproved model
and an unstable implementation are different problems. Establish which applies;
do not invent data or force a preferred result. If a genuine blocker prevents
completion, report the work as unfinished, not as a successful deferral.

## Three prohibited substitutes for repair

### 1. Evasion as a solution

Do not replace a feasible numerical or physical repair with caveats, docstring
warnings, a `deferred` status, a diagnostic-only flag or a graceful error message.
These may communicate a limitation or prevent misuse; they do not resolve it.
Do not call a new rejection guard a fix for a failure inside the supported domain.

Carry the intervention through the shared scientific implementation, its real
callers and output readers. A corrected scratch copy does not repair production.
Do not remove the failing case, drop a supported mode, discard awkward samples,
clip uncertainties or narrow applicability merely to make failure disappear.
Scope reduction requires the operator's decision, not an agent's success label.

### 2. Tautological testing and tolerance dilution

Never weaken assertions, inflate tolerances or substitute mocked physical
computations to obtain a green suite. Do not hide failures with skips, `xfail`,
changed denominators, filtered residuals or regenerated golden outputs.

An expected answer must have an independently justified basis: an applicable
analytic solution, conservation law, limiting case, trustworthy independent
algorithm, or calibrated reference with its uncertainty. A saved output from the
same unvalidated code is a regression record, not a correctness oracle. Two
wrappers around one numerical kernel are not independent implementations.
Simulations with declared known truth are legitimate controls, not observations;
they test the simulated assumptions and cannot alone establish real-data adequacy.

Set tolerances from physical scale, units, conditioning, numerical error, reference
uncertainty and the intended use before judging the repaired result. An incorrect
oracle or acceptance rule may need correction, but preserve the discrepancy and
justify the change independently; never choose a tolerance because it passes.

Execute the actual scientific unit and affected consumer. Mocks may test routing,
network failures or scheduling separately; they cannot establish the numerical
accuracy of the computation they replace. Test agreement does not by itself
establish model adequacy, empirical calibration or observational support.

### 3. Plan-inflation over execution

Do not substitute diagnostic lists, administrative breakdowns, research summaries
or repeated promises for the next feasible experiment. Name the competing causes
and the observation that would distinguish them, then execute the smallest
authorized calculation sensitive enough to make that distinction.

Once evidence supports an intervention, implement it. Another search, profile,
rerun or report needs a question that could change the next decision. Reuse an
existing command, notebook, test or numerical function; do not build a framework
to avoid finishing the calculation. Keep records compact and reuse existing ones.

## Execute a bounded scientific repair

1. **Reproduce the consequential failure.** Inspect the actual input-to-output
   path and callers. Pin down relevant units, time/frame conventions, shapes,
   masks, parameter support and uncertainty. Retain the failing case and its
   physical or numerical effect; do not start an unrelated provenance audit.
2. **Run a discriminating check.** Separate implementation error, instability,
   conditioning, finite-sampling error, inadequate exploration, model mismatch
   and absent information. Use an independent expectation capable of disagreeing
   with the current implementation. Investigate the strongest plausible alternative.
3. **Intervene where the defect is owned.** Implement the supported change at the
   actual scientific consumer, not only in a wrapper or warning. Verify any newly
   adopted formula, empirical coefficient or approximation against its applicable
   primary source. A prior, likelihood, mask or model change alters the inference;
   justify and disclose it rather than presenting it as a neutral numerical fix.
4. **Measure before and after on a comparable task.** Retain inputs, relevant
   settings, budgets and failure accounting. Quantify the changed observable,
   error, bias, uncertainty or convergence behavior, in its physical units, against
   the independent reference. If the old method produces no valid value, report
   that failure honestly; do not fabricate a numerical baseline. For stochastic
   comparisons assess Monte Carlo variation, not one favorable random seed.
5. **Establish usable boundaries and regression coverage.** Check applicable
   limiting cases, domain edges, covariance propagation and failure behavior.
   Execute a focused independent regression through the repaired computation.
   Assess separately on untuned cases when generalization is claimed; do not call
   exposed development cases fresh blind evidence. Preserve unresolved failures.

Correctness may require replacing a disproved test oracle rather than changing
already-correct physics. Establish that with independent evidence; do not manufacture
code churn or defend existing code merely because it already has tests.

## Deliver physically bounded, numerically assessed code

Verify units and conversions at the boundaries that matter to the result. Bound
the method by justified physical and mathematical support, not by arbitrary
clipping or invented floors. Signed weights, natural units, low counts, masked
values and valid zero-density log probabilities need their actual contracts,
not universal positivity, normality or finiteness assumptions.

Use convergence checks appropriate to the method and requested precision.
Deterministic calculations may need refinement and independent error estimates;
fits may need identifiability and objective/derivative checks; posterior sampling
needs relevant mixing, mode coverage and Monte Carlo precision evidence. A finite
answer, optimizer success flag, longer chain or smaller residual is not sufficient
by itself. Fixed-parameter forward-model agreement does not establish reliable
posterior exploration. Do not require unrelated diagnostics as new entry gates.

Lead delivery with the scientific change and measured before/after effect,
uncertainty, tested domain and remaining failures. Then identify the implementation
and checks actually executed. A test count, warning, status flag, hash or completed
plan cannot substitute for that evidence. Do not generate a new dossier by default.

## Honest stopping is not completion

Honor read-only scope, protected data, approved hosts, budgets and stop requests.
This skill authorizes no new computation, uploads, agents, releases or claims.
Do not execute an unauthorized run to satisfy its evidence requirement.

When the next necessary experiment cannot proceed, state the attempts and findings,
the specific blocking input, dependency or authorization, and the next plausible
route. Continue other justified work within scope. Label the repair unfinished;
do not present a proposal, static check or newly written instruction as an executed
repair or evidence of improved scientific behavior.

The optional `thinking-like-a-scientist` and `science-before-bookkeeping` skills
complement this guide when installed. Neither is an installation dependency.
