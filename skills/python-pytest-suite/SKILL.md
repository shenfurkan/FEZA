---
name: python-pytest-suite
description: "Write, review or debug focused pytest coverage for scientific Python: real numerical kernels, independent oracles, justified tolerances, fixtures, mocks, recovery and CI. Separate regression, integration, statistical calibration and physical-device evidence."
---

# Scientific Python Test Standards

Test the actual behavior whose correctness is claimed. A green test can establish
an interface property without establishing numerical accuracy or physical validity.

## Choose the smallest informative test

For a known defect, retain a focused regression, demonstrate the expected failure
where feasible, repair the owning implementation and rerun affected callers.
An import/syntax failure is not evidence that the intended regression detected
the scientific defect. For an unknown cause, first use independent calculations
or controlled experiments; a full workflow fixture is not the entry ticket to
numerical diagnosis.

Run commands through the project's actual environment manager and supported
interpreter, not a machine-local activation or unrelated notebook kernel. Use
existing test configuration and markers; do not invent project flags or paths.

## Oracles and fixtures

- Use analytic solutions, independent implementations, verified reference tables,
  limiting cases and appropriate metamorphic relations as expected answers.
- A saved result from the same unverified implementation is regression history,
  not an independent correctness oracle. Do not regenerate it to conceal a defect.
- Import and execute the actual numerical unit under assessment. Independent code
  supplies an expected value; it must not replace the production function being tested.
- Synthetic controls, simulated events and pseudo-experiments are legitimate test
  inputs. Approved measured/reference samples can also be useful; preserve access
  rights, privacy, identity and uncertainty rather than banning all real-data tests.
- Simulation generators can legitimately be production software. The boundary to
  protect is presenting generated data as missing measured observations, not the
  location or mere existence of a generator.
- Test invalid/unsupported inputs and valid boundaries. For nonfinite values,
  inspect NaN, positive infinity and negative infinity separately under the actual
  contract; legitimate zero-density negative infinity is not automatically a failure.

## Tolerances and numerical semantics

Derive absolute/relative tolerances from scale, units, conditioning, approximation
error, reference precision and intended use. Do not select whichever tolerance
makes the test pass or round expected answers before comparing them.

Check shapes, dtype where consequential, units, finiteness/allowed infinities and
support separately from approximate agreement. Broadcasting and default absolute
tolerances can hide errors. Exact endpoint or discrete-value comparisons can be
correct; do not replace them with approximate tests that widen support.

For stochastic properties, define the estimand, domain, trial design, dependence,
statistic, uncertainty and decision rule before assessment. A fixed seed supports
regression; it does not establish unbiasedness, coverage, tail precision or absence
of failure. Use a distribution-appropriate interval/test, accounting for repeated
looks and multiple comparisons where relevant. Do not force weighted samples,
dependent trials or boundary estimates into an unjustified Gaussian approximation.

## Mocks and integration

Mock network, clocks and hardware probes where appropriate. A mocked engine can
test routing/error handling, not its likelihood or sampler. A mocked child launcher
cannot prove native-crash isolation or real continuation. State each substituted
boundary and test the actual boundary when making the corresponding claim.

Keep numerical, orchestration, data-format and end-to-end tests distinct. Follow a
repair through the relevant caller before claiming integrated behavior; do not
require every unrelated pipeline stage for each numerical check. Test output
content and semantics, not only file existence or a zero exit.

## Scientific calibration is different

Same-model injections can establish self-consistency but miss shared model errors.
When calibration/generalization is requested, separate tuning from evaluation and
include independent, null/background and failure controls as appropriate. Assess
bias, interval coverage, selection/sensitivity and false-alarm behavior with their
uncertainty and tested population. Preserve non-detections, failures and exclusions
in the appropriate denominator; exposed cases are not fresh blind evaluation.

## Execution, recovery and resources

- Use focused nodes during development. Run broad acceptance/full suites when the
  affected scope or operator request warrants it, not after every small edit.
- Choose concurrency from actual CPU/RAM/device capacity and the approved budget.
  Numerical pools and compiler caches can make individually small tests fail together.
  Preserve responsiveness on interactive machines; follow allocated resources on batch hosts.
- Respect host/window and stop requests. An interrupted, uncollected or unexecuted
  test is not a pass. Do not restart stopped work through a background service.
- Exercise real checkpoint/RNG/state continuation and device kernels when those
  properties are claimed. Virtual devices are not physical multi-device evidence.
- For transport/release acceptance, bind tests and required inputs to the executed
  snapshot and reconcile collected/executed nodes. Ordinary diagnosis needs no new
  bundle or collection dossier. Never pool different snapshots or execution modes.
- Static analysis, formatting and compilation are useful software checks, not
  scientific calibration. Run applicable focused checks and actual checkpoint policy.

Do not weaken tests to manufacture success. Correct a demonstrated wrong oracle
with independent evidence and preserved failure history. Report exact pass/fail/skip
and unexecuted scope; a normal pass does not imply optional slow validations ran.
