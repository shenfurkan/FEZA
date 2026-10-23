---
name: statistical-inference
description: "Assess scientific fitting, likelihoods, uncertainty, MCMC, nested sampling, model comparison and statistical calibration. Use for convergence, nuisance dependence, coverage, background/null controls and prior/model sensitivity; do not confuse estimator precision with model adequacy or discovery significance."
---

# Statistical Inference and Evidence

Use diagnostics appropriate to the estimator and scientific question. MCMC mixing,
optimization, evidence integration and independent Monte Carlo sums are different
problems; a single success flag cannot certify all of them.

## Define what is being inferred

Inspect the actual measured/simulated inputs, selection, units, parameterization,
likelihood and support. State nuisance parameters, calibration/background terms,
priors or constraints and their shared dependence. Separate a conditional estimate
with fixed nuisance values from an uncertainty that propagates them.

Do not assume Gaussian errors from a plotted symmetric bar or use a count model
blindly for weighted/subtracted quantities. Signed event weights or estimates are
not inherently invalid; their interpretation and uncertainty require the actual
construction. Empty/low-count regions do not automatically have zero uncertainty,
and adding arbitrary pseudocounts or clipping negative results changes the model.

Inspect coordinate changes and the induced measure/Jacobian, including whether the
software already accounts for it. A justified bounded prior is not retained-sample
clipping. Model boundaries and physical constraints can invalidate convenient
asymptotic approximations; verify applicability rather than assume it.

## Separate diagnostic calculations from adopted inference

Failed chains, fixed-parameter likelihood checks, slices and profiles can diagnose
geometry or numerical disagreement. They are not automatically marginalized
posteriors, integrated evidences or calibrated confidence intervals. A profile
likelihood is a different object from a marginalized likelihood; interpret each
with its own assumptions and uncertainty/coverage assessment.

A broad or multimodal distribution can be sampled correctly. An optimization path
between maxima does not establish posterior mass, mode weights or a failure cause.
Do not narrow support, delete modes or rerun seeds until a preferred picture appears.

## Sampler and optimizer checks

- **MCMC:** inspect initialization, adaptation/burn-in, stationarity, autocorrelation,
  effective sample size and Monte Carlo precision for the actual reported summaries.
  Tail/quantile accuracy may differ from bulk diagnostics. Preserve applicable
  declared criteria but do not treat any threshold as proof.
- **Independent chains:** use diagnostics under their actual assumptions. Interacting
  walkers in one ensemble are not independent chains. Verify mode exploration and
  weights with appropriate well-explored/trapped controls when at issue.
- **Optimization:** inspect gradients, constraints, boundaries, alternative starts
  and relevant curvature/identifiability. A local success or small objective change
  does not establish a global optimum or valid covariance uncertainty.
- **Nested sampling/integration:** report the integral/evidence estimate, uncertainty,
  stopping reason and cap/termination status. A requested stopping tolerance is not
  the measured integration error. Inspect weights, effective samples and mode coverage.
- **Retention:** memory-sized batches may preserve the same computation only when
  state, ordering, every required transition and RNG streams really continue.
  Disclose thinning or changed budgets; assess their information cost.

## Model comparison and significance

State whether the quantity is a likelihood ratio, posterior odds, Bayes factor,
p-value, confidence limit or posterior probability. Do not translate one into
another by terminology. Report log conventions, uncertainty and prior/model sensitivity
for evidence comparisons. A large factor among inadequate models does not make one true.

For searches or selection across alternatives, assess the relevant trials/selection
effect; local and global significance are not interchangeable. Confidence statements
need their actual sampling/coverage construction. Do not import a universal significance
cutoff or claim a discovery from an uncalibrated ranking score.

## Model and uncertainty checks

Choose discrepancies that could expose the relevant defect and compare data with
appropriate predictive or control distributions. Posterior predictive probabilities
are not generally ordinary uniform-null p-values. Residual smoothness/whiteness is
not proof of physical adequacy, and a flexible noise/background model can absorb
the signal of interest. Test recovery, bias and coverage where that risk matters.

Propagate shared calibration, nuisance and model uncertainty through the actual
joint/conditional computation. Independent input files do not guarantee independent
inferred parameters. More Monte Carlo samples do not remove systematic bias.

## Calibration and protected evaluation

Define the population/domain, trial budget, statistics, decision criteria and
exclusions before evaluation. Separate development/tuning from held-out assessment;
use null/background and independent controls as appropriate. Same-model simulations
are useful but can share the fitted model's errors. Assess bias, coverage, sensitivity
and false-alarm behavior with finite-trial uncertainty and retained failure accounting.

Honor the analysis's actual blinding/custody/unblinding protocol. Do not inspect
protected observations/answers to choose cuts, templates, priors or nuisance models.
Do not silently discard unfavorable trials or report exposed cases as untouched.

For a bounded question, deliver its comparison, precision and limits rather than
an unrelated full-inference checklist. For an authorized repair, carry the change
through the actual consumer and measured effect; the optional `scientific-debugger`
skill can help when installed. These instructions do not replace inspecting the primary
method and applicable software documentation before adopting a new estimator.
