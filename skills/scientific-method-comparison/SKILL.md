---
name: scientific-method-comparison
description: "Use when choosing between scientific models, numerical algorithms, libraries or execution strategies. Compare the current baseline and plausible alternatives using measured accuracy, uncertainty, stability, applicability and end-to-end cost. Separate changes to the physical model from implementation optimizations, preserve failures and assess ranking uncertainty. Not a default risk-register exercise, benchmark campaign or authorization for new compute."
---

# Scientific Method Comparison

Choose the method that answers the physical question reliably within the actual
constraints. Do not choose a familiar library, fashionable algorithm or fast kernel
first and retrofit the scientific justification. More scorecards do not replace a
discriminating calculation.

## Frame a decision that measurements can change

State the requested observable or distinction, required precision, applicable
domain and actual resource constraints. Include the current implementation as a
baseline and only plausible alternatives. Use existing numerical entry points or
notebooks before creating benchmark infrastructure.

Separate two kinds of alternatives:

- **Same scientific model, different implementation:** preserve the mathematical
  target, units, support, required budgets and applicable RNG/continuation contracts.
  Assess accuracy as well as speed; identical bytes are not the general criterion.
- **Different scientific model or inference procedure:** identify changed assumptions,
  likelihood, priors, nuisance treatment or information used. Compare adequacy,
  identifiability and uncertainty as well as computational performance; do not
  describe a science-changing simplification as a neutral optimization.

Do not invent new institutional gates. Existing scientific, security, data-access
and execution requirements remain binding. A method that fails the required physical
accuracy or supported domain cannot be rescued by a favorable runtime score.

## Choose evidence before choosing a winner

Use criteria that matter to this decision, with their units and independent basis.
Relevant criteria may include:

- Error in the requested physical quantity against an analytic solution, justified
  limiting case, independent numerical method or uncertain calibrated reference.
- Bias, uncertainty coverage, sensitivity to nuisance assumptions or model mismatch,
  including representative failures and boundary cases.
- Stability, conditioning, discretization or sampling precision at the required
  accuracy, not only agreement at one favorable input.
- End-to-end runtime and peak working memory on the actual approved host/device,
  including setup, compilation, transfer and I/O when relevant to intended use.
- Concrete integration and maintenance constraints that could prevent reliable use.

Do not turn guessed impressions into quantitative scores or probabilities. Published
performance is a lead, not a measurement of this workload. A reference has assumptions
and uncertainty; a saved baseline output is not automatically the correct answer.

## Run the smallest fair comparison

Select cases that can distinguish the alternatives at the required precision.
Preserve the same scientific question, input meaning and comparison conditions.
Disclose necessary differences instead of pretending incompatible workloads match.

1. Use an isolated, bounded pilot when that can settle the decision. Inspect outputs
   from the real scientific functions and relevant consumers; mocks cannot compare
   the physical calculations they replace.
2. Retain invalid outputs, nonconvergence, timeouts and unsupported cases in the
   comparison. Report their causes separately; do not rank methods on survivors
   alone or lower one method's scientific budget to manufacture a speedup.
3. Assess variability where it matters. Separate cold-start and retained/steady-state
   use when both are relevant. For stochastic methods assess error and cost variation
   across justified repetitions, not one favorable seed or a universal trial count.
4. Keep numerical agreement, estimator convergence and real-data model adequacy
   distinct. A forward-model microbenchmark does not establish calibrated inference.
5. Tune on declared development cases. If claiming broader reliability, assess on
   appropriately separate cases; do not expose protected answers or relabel tuned
   cases as untouched validation.

Honor approved hosts, budgets and stop requests. A comparison request grants no
automatic remote launches, uploads, installations, agents or expensive evaluations.
If measurements cannot be made, give a conditional recommendation and the specific
missing experiment, not invented timing, accuracy or a completed benchmark claim.

## Decide from the evidence, not a decorative total

Report the measured quantities and uncertainty directly. Prefer the simplest
alternative that meets the scientific need across its assessed domain. Preserve
tradeoffs: a method may be better in one regime and unsupported in another.
Past effort is not evidence for retaining the baseline; novelty is not evidence
for replacing it.

Use a weighted decision matrix only if the requested decision actually needs one.
Define score meanings and priorities before looking for a preferred winner, retain
the underlying physical measurements, and examine whether plausible uncertainty
or priority changes reverse the recommendation. Do not use arbitrary perturbation
percentages as a universal robustness test. Uncertain rankings call for the next
discriminating measurement, not a falsely precise total score.

Lead with the recommended method, measured scientific advantage, tested domain
and important failure or cost tradeoff. Keep a compact comparison in the existing
record or response; no default risk register, FMECA, new manifest or mandatory report
template is needed. If repair or integration is also authorized, implement the
selected intervention at the actual consumer and measure before/after there.
Otherwise leave the implementation unchanged.

The optional `scientific-peer-review`, `scientific-repair-not-deferral` and
`thinking-like-a-scientist` skills complement this standalone guide when installed.
