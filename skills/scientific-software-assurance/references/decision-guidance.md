# Uncertainty-Aware Scientific Decisions

Apply this guidance to the requested comparison; it is not a universal calibration
procedure or a new mandatory gate. Use an established applicable project protocol
when one exists and identify any actual defect before changing it.

## Identify the kind of comparison

An ordinary deterministic regression may compare against an exact solution or
proven numerical bound with a justified tolerance. A value near that tolerance
can still pass. Such a test does not automatically need a probabilistic guardband.

A scientific acceptance criterion assessed with uncertain references, finite
simulation/trial scatter, uncertain inputs or model discrepancy needs a method
that accounts for those effects. Missing uncertainty is not zero uncertainty.

State the estimand, units, limits, sources, dependence, domain and decision rule.
Distinguish standard deviation, standard error, interval coverage, numerical bound
and systematic/model discrepancy; do not combine all as independent Gaussian noise.
For linearized propagation, include relevant covariance. For nonlinear/asymmetric
quantities, assess whether joint/distributional propagation is needed.

## Select an applicable construction

- Counts/rates need a model appropriate to the actual sampling design. A zero
  observed count does not prove a zero rate or zero uncertainty. Weighted/signed
  data are not automatically ordinary binomial or Poisson observations.
- Confidence intervals, posterior probabilities, likelihood-ratio tests and
  calibrated false-accept rates are different constructions. Name what is controlled
  and under which assumptions, not just a generic confidence percentage.
- Deterministic approximation bounds should be used as bounds unless a probabilistic
  interpretation is justified. More trials cannot remove common bias or model error.
- Prespecify applicable trial counts/stopping and account for dependence, multiplicity
  or repeated looks. Do not search over seeds/reruns for a favorable decision.

## A conditional normal example, not a universal acceptance recipe

For an explicitly justified normal comparison distribution centered at `delta`,
with finite standard uncertainty `u > 0` and limits `-L1`, `L2`, integrating its
density gives the in-limit probability/content:

`P_in = Phi((L1 + delta)/u) + Phi((L2 - delta)/u) - 1`.

Its evidential interpretation depends on why that distribution represents the
comparison. It is not automatically a calibrated false-accept rate or a posterior
probability about a fixed parameter. Do not use it for a binomial boundary estimate,
heavy/asymmetric tails or an unknown uncertainty just because a scalar `u` is available.

If the project explicitly adopts a rule requiring an in-limit estimate and
`P_in >= 1 - r_max`, an in-limit result below that target is indeterminate, not a
pass. `r_max` is a project-set target, not a transferable institutional constant.
Use the actual adopted rule for outside-limit outcomes and risk decisions.

For symmetric limits `±L`, the full expression is
`Phi((L - |delta|)/u) + Phi((L + |delta|)/u) - 1`.
The common one-tail approximation omits `1 - Phi((L + |delta|)/u)` and therefore
overstates containment. A one-tail guardband is not the exact two-sided boundary;
use the full expression for threshold decisions, even when the omitted tail seems
small. Unknown `u` must not become zero or an invented uncertainty floor.

Exact mathematical comparisons with genuinely zero uncertainty and comparisons
using proven error bounds use their own applicable rules, not division by zero.

## What to report

Give the result, limits, uncertainty model/bound, applicable rule, target and actual
outcome. State model/approximation limits and unexecuted checks. Address the real
cause of an indeterminate result: numerical defect, inadequate oracle, finite
sampling or inappropriate model. A recorded risk acceptance is not a verified pass;
widening a tolerance after seeing a failure is a requirement change, not a repair.
