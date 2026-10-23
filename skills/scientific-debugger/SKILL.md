---
name: scientific-debugger
description: "Investigate wrong scientific results, numerical failures, suspicious artifacts, model/implementation disagreements or missing-method blockers. Trace the affected calculation through its real consumers, distinguish data limitations from software defects, and carry authorized repairs through measured assessment."
---

# Scientific Debugger

Resolve the discrepancy, not merely its label. The optional `thinking-like-a-scientist`
skill adds shared reasoning principles when installed; no sibling skill is required.

## Establish the question

Identify the requested quantity, expected behavior, observed discrepancy and
precision needed to discriminate plausible causes. Inspect the real implementation,
inputs and downstream consumer before proposing an intervention. Existing code,
tests and documentation can all be wrong; none overrides contrary evidence.

Preserve original observations and failed outputs. Use the project's existing
records for command/configuration, inputs and results. A bounded numerical check
does not need a new manifest framework, full pipeline run or release audit.

## Choose the relevant checks

| Boundary | Inspect | Distinguish |
|---|---|---|
| Input identity | Actual dataset/sample, processing version, parameter layout and relevant lineage | Wrong/corrupt input versus incomplete historical attribution |
| Units and conventions | Scale, normalization, coordinate frame, time representation, weights and transformations | Representation error versus physical-model discrepancy |
| Applicability | Observed/simulated identity, valid domain, uncertainties and selection | Unsupported model use versus a valid negative result |
| Numerical method | Conditioning, stability, approximation, stopping, precision and support | Failed calculation versus inadequate information |
| Inference | Actual likelihood, nuisance parameters, dependence, exploration and model checks | Reliable broad uncertainty versus inaccurate computation |
| Consumer | Caller, serialized output, plotting/reporting and any decision boundary | Correct helper versus still-wrong delivered result |

Do not infer a failure from nonfiniteness alone: legitimate zero-density `-inf`
differs from an arithmetic error. Inspect NaN and both infinity signs separately
under the actual contract. Do not treat missing metadata as proof that every
independent calculation on verified inputs is impossible.

## Classify only as far as the evidence supports

- **Software contract:** wrong routing, shape/schema or output interpretation.
- **Environment:** unavailable dependency/device or incompatible implementation.
- **Data/identity:** corruption, wrong source, unknown relevant units or selection.
- **Applicability:** the chosen model is unsupported in the stated domain.
- **Numerical:** unstable solver, invalid arithmetic, inadequate approximation or sampling.
- **Interpretation:** output used beyond its demonstrated calibration or meaning.
- **Algorithmic:** a missing estimator, propagation method or implementation.
- **Observational:** an actual required measurement is absent or inaccessible.

A missing algorithm is not a missing observation. Investigate applicable literature,
existing libraries and authors' implementations before calling a difficult problem
infeasible. A paper's existence alone does not prove its applicability or a working
repair. Name actual attempts and the specific blocker if the next step cannot run.

## Repair and assess

1. Choose an informative independent comparison, limiting case or controlled
   perturbation. Failed fits/profiles may diagnose mechanisms without becoming
   adopted posteriors or integrated model evidence.
2. Once evidence supports an intervention, implement it at the owning calculation
   or decision and follow its affected callers. Keep unaffected safeguards intact.
   Do not fix a result by changing its label, deleting the failed case or narrowing
   scientific support without authorization.
3. Retain a focused regression with an independent expectation. Compare the
   before/after scientific effect, precision, memory/runtime where relevant, and
   residual limits. A mock of the calculation cannot verify that calculation.
4. When calibration/generalization is requested, use appropriate separate evaluation
   controls. Same-model simulations test self-consistency, not independent physical
   fidelity. Preserve failure/exclusion accounting and protected-data boundaries.

Simulation is a legitimate scientific operation when identified as such; it must
not silently replace missing measured inputs. Use the existing approved host and
budget, not a new remote run or expensive campaign by implication.

Report the finding, measured effect and actual delivery state first. A read-only
review stays read-only; an unresolved repair stays unfinished with a concrete next
route, not a growing administrative prerequisite list.
