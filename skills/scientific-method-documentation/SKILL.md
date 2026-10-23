---
name: scientific-method-documentation
description: "Document or review the actual scientific method behind an implementation: assumptions, likelihood, units, uncertainty propagation, selection, approximations and applicability. Use when changing scientific calculations or result interpretation; not only checking that documentation fields exist."
---

# Scientific Method Documentation

Describe the running scientific method, not just the paper's idealization or a
future design. Documentation does not repair a calculation. Optional installed
helpers are `thinking-like-a-scientist` for shared repair/delivery principles and
`code-documenter` for docstring style; this guide does not require either directory.

## Explain what matters to the result

- The physical question and inferred/measured quantity, actual input identity and
  whether inputs are measured, simulated, calibrated or model-derived.
- Units, normalization, coordinate/sign conventions and time representation at
  relevant boundaries. Do not impose a universal error-field naming scheme.
- The implemented model/likelihood, background/nuisance terms, prior or constraint
  treatment and selection function. Separate them from the cited ideal model.
- Approximations, numerical method, exposure/binning treatment where relevant,
  limiting cases, solver/sampling precision and assessed error.
- Uncertainty sources and dependence: shared calibration/model constraints, finite
  simulation statistics and nonlinear/asymmetric propagation as applicable.
- Actual validity domain, independent checks, calibration/evaluation population,
  exclusions and failure behavior. Do not invent a calibration because a fit completes.

## Keep interpretations distinct

| Evidence | Does not establish by itself |
|---|---|
| Search score or selected excess | Calibrated global significance or a physical discovery |
| Successful optimizer | Identifiability, valid uncertainty or model adequacy |
| Posterior summary | Adequate exploration or robustness to model/prior assumptions |
| Simulations generated with the fitted model | Independent physical fidelity |
| Agreement with a published estimate | Exact truth or validity outside the reference domain |
| Checkpoint, device telemetry, hashes or schema | Numerical convergence or experimental calibration |
| A diagnostic or workflow label | Scientific correctness or authorized publication status |

These are interpretation distinctions, not blanket refusals to use supported
measurements. State the answer the evidence supports and its precision.

## For a method change

Explain the original discrepancy, justified intervention, actual consumer, measured
before/after effect and focused regression. Preserve relevant covariance through
the computation, not merely an independence flag or a warning. Distinguish source
inspection, software regression, numerical convergence and empirical calibration.

For calibration/performance claims, identify development versus evaluation cases,
reference/control construction, trial budget, uncertainty/coverage, null behavior
and tested domain. Disclose outcome-informed changes; tuned cases are not untouched
assessment. Preserve failed cases and do not weaken criteria to make prose look complete.

Use existing code comments, documentation and analysis records. A bounded exploratory
calculation needs its actual inputs, assumptions and limits, not a new schema or
unrelated full-pipeline run. Verify cited relations against retained applicable sources
and errata; a citation's presence is not method verification.
