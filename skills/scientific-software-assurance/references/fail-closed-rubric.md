# Contract-Aware Scientific Software Rubric

## Contents

- [Failure, arithmetic and representation](#failure-arithmetic-and-representation)
- [Resources, interfaces and integrity](#resources-interfaces-and-integrity)

Use these rules on the reviewed paths, not as a universal project-reorganization
checklist. Severity depends on the actual consequence and adopted project requirements.
Scientific validity, numerical accuracy and software execution are separate judgments.

## Failure, arithmetic and representation

1. **No silent fallback.** Missing required measured input or failed calculation must
   not become a plausible constant, simulated observation, stale cache or a different
   method unless that substitution is an explicit applicable contract and disclosed.
2. **Explicit failure semantics.** Distinguish missing input, unsupported model,
   numerical failure, valid no-detection and a scientific rejection. Ensure callers
   cannot mistake failure sentinels for observations or successful estimates.
3. **Validate nonfinite values by contract.** Check finite values, NaN, positive
   infinity and negative infinity separately at the relevant numeric boundary.
   NaN comparisons do not validate range: ordered comparisons/equality are false,
   while inequality is true. NaN-aware reductions require justified exclusions and
   accounting; reject an empty usable set where the calculation needs observations.
   A failed in-support calculation must not be silently recoded as zero density.
   For a scalar log-density contract admitting only finite values and legitimate
   zero-density negative infinity, an explicit consumer is:

   ```python
   import math

   def consume_log_result(value: float) -> float:
       """Accept finite log density or producer-established zero-density -inf."""
       if not (math.isfinite(value) or value == -math.inf):
           raise ValueError("unexpected NaN or +inf log density")
       return value
   ```

   This cannot establish whether a producer hid a failure as negative infinity.
   Nor is it a universal rule for models with documented singular densities.
4. **Floating-point semantics are explicit.** Use justified absolute/relative
   tolerances for approximate agreement, checking shapes and allowed values
   separately. Exact endpoints, discrete values represented as floats and intentional
   exact algorithmic comparisons can be correct. Numeric equality is not byte identity.
   Assess precision loss, cancellation, overflow/underflow and integer ranges; no
   dtype, including float64 or int64, is automatically sufficient for every calculation.
5. **Declare reproducibility boundaries.** Preserve required initialization, RNG state,
   ordering and continuation. State whether identity, numerical agreement or independent
   distribution agreement is intended. A seed alone is not proof of replay.
6. **Units and constants are explicit.** Use verified constants and retained empirical
   sources with applicability. Exact identities/conversions need their convention;
   numerical settings need rationale, not invented papers. Honor natural-unit and
   coordinate/sign conventions where used.
7. **Validate trust boundaries.** Check required schema/shape/type, units, domain,
   selection and alignment before use. Unknown conventions cannot be inferred from
   plausible output. Runtime checks use actual exceptions/results, not removable asserts.
8. **Protect inputs.** Preserve raw observations; document intentional in-place array
   operations and prevent derived outputs from overwriting their required inputs.
9. **No corrective clipping that hides a defect.** Do not alter a posterior, uncertainty
   or observation merely to make a result plausible. Distinguish valid model support,
   specified selection, display bounds and justified numerical safeguards from this abuse.

## Resources, interfaces and integrity

10. **Resources do not silently change the experiment.** Chunk/batch to reduce working
    memory while preserving the required draws, transitions, resolution and ordering.
    A timeout/OOM does not authorize fewer trials or an undocumented model change.
11. **Warnings stay meaningful.** Do not suppress arithmetic/runtime warnings globally.
    Narrow suppression needs a reason grounded in the specific contract and must not
    conceal a consequential numerical failure.
12. **Completion reaches the caller accurately.** Use appropriate failure status and
    atomic output or clearly marked incomplete artifacts. A partial run must not leave
    something another stage mistakes for a complete result.
13. **Concurrency has ownership.** Synchronize shared state; avoid overlapping writers,
    duplicate attempts and contested devices. Combine results under the declared order.
14. **Dependencies and execution context are identified.** Follow actual supported
    environment/build definitions; do not silently import a different kernel's libraries
    or fetch dependencies at import. A measured need may justify an explicit upgrade.
15. **Tests are not weakened for success.** Preserve independent expectations and failure
    history. A demonstrated wrong oracle can be corrected with independent evidence;
    favorable output or a regenerated golden file is not that evidence.
16. **Assertions are not external-input protection.** Python optimization can remove
    assertions. Production trust boundaries need explicit checks; assertions remain
    useful in tests and appropriate internal invariants.
17. **Secrets and protected data stay protected.** No credentials in source, logs or
    outputs. No unapproved upload of internal documents, blinded data or held-out answers.
18. **Outputs are interfaces.** Assess changes to meaning, layout, units, precision,
    defaults and error behavior through actual consumers and appropriate compatibility
    or migration evidence; do not force a version bump for an unchanged interface.
19. **Reused methods need applicability evidence.** Inspect version, known failures
    and differences in domain/workload. Popularity, heritage or an import success does
    not establish numerical/physical validity in a new domain.
20. **Check output reasonableness.** Apply relevant dimensional, range, conservation
    or normalization checks. Do not treat every signed estimate/weight as unphysical or
    silently correct a failing value before reporting it.
21. **Unknown cases are explicit.** Handle supported modes and reject/report unknown
    ones instead of mapping all unfamiliar inputs to a convenient known branch.
22. **Coverage gaps have consequences.** Identify untested reached paths, missing
    expectations, dead/deactivated code and remaining risk. Do not present coverage
    percentage alone as proof or demand irrelevant tests for an unrelated question.
23. **Calibration/reference validity is checked.** Select actual model/calibration
    versions by their applicable domain, conditions and validity. Do not silently
    extrapolate, reuse incompatible corrections or apply a correction twice.
24. **Scientific acceptance uses uncertainty appropriately.** Distinguish deterministic
    regression against an exact/bounded oracle from a requirement assessed with
    reference uncertainty, sampling scatter or model discrepancy. Use an applicable
    prespecified rule, not a universal Gaussian guardband or arbitrary error multiplier.
    Unresolved applicability/uncertainty is not a verified pass. Follow
    [the decision guidance](decision-guidance.md).

These are adapted review practices, not an agency or laboratory's certification
scheme. State the actual adopted requirement when making a compliance finding.
