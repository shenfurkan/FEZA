---
name: scientific-verification-and-validation
description: "Review whether scientific tests and comparisons support requirements and intended use. Assess oracle independence, numerical error, uncertainty, statistical acceptance, calibration, tested domain and honest reporting; do not impose another institution's approval process."
license: MIT
---

# Verification, Validation and Result Credibility

Ask three distinct questions: does the implementation perform the intended
operations, is the numerical solution sufficiently accurate, and does the method
describe the physical system well enough for the requested use? Evidence for one
does not automatically answer the others.

Use the project's actual requirements, review authority and analysis protocol.
These are general scientific-software practices, not institutional certification
or permission to create new release gates or mandatory report files.

## Select evidence that can answer the question

| Activity | Appropriate role | Not sufficient by itself |
|---|---|---|
| Test | Execute actual behavior with meaningful inputs and an independent expectation | One favorable example for a distribution-wide claim |
| Analysis | Derivation, error/coverage bounds or reasoning with explicit assumptions | Untested assumptions about what production code runs |
| Inspection | Examine source, documents, metadata or a released artifact | Runtime correctness or measured performance |
| Demonstration | Show an operation can complete | Numerical accuracy, calibration or physical validity |

Use combinations appropriate to the requirement. An exact analytic bound can be
stronger than a large simulation campaign; a simulation under the wrong model is
not independent validation of that model.

## Review the comparison

1. Identify the requested requirement/scientific claim, observable, input population,
   tested domain and consequence of a wrong decision. Do not make a full release
   plan the prerequisite for a bounded numerical check.
2. Identify each oracle: exact/analytic solution, independent algorithm, verified
   reference data, invariant, statistical construction or regression history.
   Same-code expected values catch changes but can repeat the original error.
3. Verify that tests execute the actual implementation and relevant consumer.
   Disclose mocks, independent references, substituted child processes and differences
   from the production configuration. Real-device claims need real-device evidence.
4. Assess numerical error: discretization, iteration/stopping, floating-point effects
   and finite sampling as applicable. Inspect conditioning and refinement/reference
   agreement, not only optimizer success or small residuals.
5. Check the uncertainty model and decision rule using
   [decision guidance](references/decision-guidance.md). Treat round-off/bounded
   regression separately from uncertain scientific acceptance. A standard deviation
   alone does not identify tails; a confidence level is not automatically false-accept risk.
6. For model validation/calibration, inspect independent referents, uncertainty,
   selection and applicable population. Separate tuning from evaluation. Retain null,
   background, failure and exclusion accounting relevant to the actual claim.
7. Assess use inside the demonstrated domain, or explicitly state the extrapolation
   and its impact. Reusing a method in a new regime needs appropriate new evidence.
8. Report executed versus planned/skipped/interrupted coverage and unresolved defects.
   A launched job, successful import, schema or digest is not a scientific test pass.

## Statistical checks

State estimator, statistic, trial design, dependence, seed policy, confidence/coverage
or risk target and required precision before evaluation. Fixed seeds serve regression;
they do not establish unbiasedness or population reliability. Account for selection,
multiple comparisons and sequential looks where consequential. Do not rerun until green.

Check finite-sample/boundary/asymptotic assumptions rather than prescribe a universal
multiple of standard error. Weighted events, dependent samples and shared systematic
uncertainty need their own treatment, not independent-binomial/Gaussian defaults.

## Delivery

For a focused question, give the finding, evidence, uncertainty, consequence and next
necessary action. For a requested plan/audit, map requirements to actual activities,
oracles, criteria, results and unverified scope in the project's existing format.
Do not invent measurements, trials or completed validation to fill a template.

An inconclusive required acceptance check is not a pass. An authorized risk acceptance
may disposition an unresolved gap but does not supply missing verification. Do not
silently widen tolerances or transfer another institution's thresholds to this project.
