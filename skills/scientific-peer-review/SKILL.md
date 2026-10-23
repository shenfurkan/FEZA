---
name: scientific-peer-review
description: "Use to review a scientific analysis, numerical method or manuscript for physical rigor, competing explanations, assumptions, uncertainty, selection effects and claim-evidence alignment. Inspect the scientific argument and its actual computational support, distinguish demonstrated defects from untested concerns, and propose discriminating checks. Not merely code-style review, a journal decision or permission to edit the analysis."
---

# Scientific Peer Review

Review the argument about nature, not the author's confidence, a prestigious
persona or a preferred conclusion. Challenge unsupported acceptance and unsupported
rejection equally. A polished report, matching files and passing tests are not
evidence that the physical interpretation is correct.

## Keep the review scoped

Identify the requested claim, observable, precision and intended use. Read the
relevant methods, actual inputs, implementation, output consumers and supporting
evidence. A focused question does not require a full repository audit or every
possible observation. State which material was inspected and which was not.

Treat review as read-only unless repair is also authorized. Do not change data,
priors, test expectations or manuscript conclusions simply to make a finding
disappear. Preserve protected evaluation answers and the receiving project's
actual compute, data-access and claim rules.

## Examine the scientific argument

Apply the dimensions relevant to the question, not a universal acceptance checklist.

| Dimension | Questions that can expose a consequential error |
|---|---|
| Physical explanation | What was observed, assumed and inferred? What is the strongest plausible alternative? Which observable could distinguish them? |
| Data and calibration | Are the measured quantities, response/calibration, selection, masks and exclusions appropriate? Could shared systematics or selection create the result? |
| Mathematical model | Are definitions, units, normalization, coordinate/sign conventions, parameter support and transformations consistent at the actual consumer? Do justified limiting cases hold? |
| Numerical implementation | Does the running calculation implement that model accurately enough? Check conditioning, stability, approximation and relevant convergence, not just finite output or a success flag. |
| Inference and uncertainty | Are covariance, nuisance dependence, model sensitivity, identifiability and finite-sampling error represented? Could several explanations fit the available information? |
| Independent assessment | What supplies the expected answer? Do controls exercise the real calculation with different failure modes? Is the tested domain appropriate to the claim? |
| Claim support | Does the conclusion exceed the observations, calibration or assessed domain? Are software verification, numerical accuracy and physical adequacy being confused? |

Do not transfer a field-specific threshold, positive-weight assumption, Gaussian
approximation or institutional approval rule to another discipline. Signed weights,
low counts, natural units, censoring and physical boundaries need their actual
mathematical contracts. A bounded prior is not the same operation as clipping
retained results; a parameter transformation needs its correct induced measure,
including whether the implementation already supplies any required Jacobian.

For sampling, distinguish genuine multimodality or weak information from inadequate
exploration. Inspect the diagnostics and Monte Carlo precision appropriate to the
algorithm and reported quantity. Forward-model agreement at fixed parameters does
not establish posterior mode weights, calibrated uncertainty or reliable tails.
For deterministic calculations, use relevant refinement or independent error
comparisons rather than imposing sampler diagnostics.

Separate observations do not guarantee independent inferred parameters. Trace
shared constraints before accepting independent error propagation. Check nonlinear
or asymmetric uncertainty where it affects the conclusion. Flexible nuisance or
noise models can absorb the signal; added flexibility is not automatically a repair.

## Make findings falsifiable and useful

For each consequential finding, identify:

- The specific claim, equation, source range or output being challenged.
- The inspected evidence and whether the defect is demonstrated, a plausible
  mechanism or an untested concern. Do not promote suspicion into a measured effect.
- Its physical or numerical consequence, quantified with units and uncertainty
  when measured. If not measured, say so rather than invent a magnitude.
- The smallest feasible independent calculation, control or observation that
  could resolve it, and what competing outcomes would mean.

A saved output from the same unvalidated implementation is not an independent
correctness oracle. Authentic source and a PDF of the same paper can establish
transcription fidelity, not independent physical corroboration. Simulations with
declared truth can test recovery under their assumptions; they are not observations
or proof that those assumptions describe the real data.

Do not block a conclusion on an irrelevant missing diagnostic or hypothetical
defect. Equally, do not waive a demonstrated failure because a suite passes or a
limitation is disclosed. Missing evidence restricts the affected inference; it is
not automatically evidence against the physical hypothesis.

## Deliver the review, not a bureaucracy

Lead with the supported conclusion and the few findings that could change it.
Distinguish required scientific corrections, useful sensitivity checks and optional
presentation improvements. A short review may be enough; produce a full referee
report or journal-style recommendation only when requested, without implying an
official editorial decision.

Ask questions only for genuine operator decisions or unavailable information.
Inspect what is already accessible instead of starting endless clarification rounds.
Stop when the scoped review is complete; do not invent a release or readiness queue.

When repair is also requested, carry justified findings through an intervention at
the actual consumer and measured before/after evidence. A repeated recommendation,
warning or deferred label is not the repair. The optional `scientific-repair-not-deferral`
and `thinking-like-a-scientist` skills can help when installed; neither is required
to use this standalone guide.
