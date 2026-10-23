---
name: scientific-paper-writing
description: "Use to draft or revise a scientific manuscript from actual analysis results: connect numerical claims, figures and tables to evidence; explain methods, uncertainty and applicability; distinguish results from interpretation; and prepare scientific/coauthor review. Includes a bounded LaTeX build guide. Not authorization to run missing analyses, invent results, submit a paper or impose one discipline's journal rules."
---

# Scientific Paper Writing

Write the scientific argument the evidence supports, not a persuasive substitute
for missing analysis. Lead with the physical question, what was learned and how
well it is known. Clear writing cannot repair an incorrect calculation.

## Establish the paper's scope

Identify the requested manuscript, audience, central question and available results.
Use the project's existing paper directory, templates and bibliography; do not
impose a target-specific layout, journal class or new export framework. Keep
shared guidance free of project data and protect confidential or blinded material.

A writing request authorizes drafting, not new production fits, remote jobs,
uploads, publication or submission. Inspect existing results first. If a necessary
analysis is missing or unsupported, name that specific gap and the calculation
that could resolve it; do not fabricate the missing number or substitute a vague
limitation. When repair is also authorized, complete and assess the repair before
using its output as an established result.

## Ground the text in the actual analysis

- Trace each consequential numerical claim to the actual analysis output, table,
  figure source or inspected publication. Identify which run/model produced it
  and what the reported uncertainty means. Use existing notes, generated macros
  or small extraction helpers when useful; do not require a new manifest or hash
  inventory before drafting or reasoning.
- Check units, normalization, parameter definitions, precision and uncertainty
  consistently across prose, tables and captions. Distinguish posterior intervals,
  confidence intervals, standard errors, intrinsic scatter and upper bounds;
  do not silently convert one into another or imply unsupported significant digits.
- Describe the method that actually ran: input selection, calibration, physical
  model, likelihood or objective, nuisance treatment, priors/constraints, numerical
  approximations and relevant convergence or error checks. A cited ideal algorithm
  is not evidence that its implementation or assumptions fit these data.
- Preserve covariance, systematic effects, model sensitivity and failed cases
  relevant to the conclusions. Do not hide exclusions or tune acceptance thresholds
  in the manuscript to disguise an unsuccessful analysis.
- Retain and inspect sources before citing their equations, coefficients or
  claims. Verify identity, version, errata and the supporting passage; do not invent
  bibliographic entries, novelty, priority or evidence of agreement.

Distinguish observations, assumptions, calculated results and interpretation.
Explicitly labeled simulations are legitimate scientific evidence about the
simulated problem, not observed measurements. Optimizer termination, sampler
convergence, numerical agreement, empirical calibration and physical adequacy are
different achievements. A successful build or passing suite establishes none of
the others by itself.

## Build a readable scientific argument

Use the appropriate structure rather than a mandatory universal template:

- **Question and context:** what remains uncertain and why the requested observable
  or comparison can resolve it; cite the applicable literature, not prestige.
- **Data and methods:** enough detail to understand inputs, transformations,
  assumptions, numerical precision and assessed domain without a procedural diary.
- **Results:** actual measurements/comparisons, uncertainty and controls, including
  consequential failures. State the tested scope rather than claiming universality.
- **Interpretation:** strongest plausible alternatives, sensitivity to assumptions
  and which observations distinguish them. Agreement with a published estimate is
  evidence with uncertainty, not exact truth; failure to establish a claim does
  not establish the opposite claim.
- **Conclusion:** answer the original question at the supported strength, separating
  demonstrated findings from proposals for future work.

Create figures and tables from actual supported outputs. Captions should identify
the data, model or estimator, uncertainty representation, relevant selection and
what the comparison shows. Distinguish observed, simulated and model-derived curves.
Do not use aesthetic smoothing, clipping or missing failure panels to manufacture
agreement. Figure-file availability is not scientific validity.

Limitations should explain consequential scope and uncertainty, not bury the answer
in blanket doubt or present an unresolved repair as completed. Discovery, causality,
validation, exclusion and generalization claims require their particular evidence;
do not transfer another field's terminology, thresholds or institutional decisions.

## Review and deliver

Check that the abstract and conclusion match the body, the central claims have
supporting results, and symbols/values agree across text, captions and tables.
Keep placeholders unmistakable in a draft and resolve them before declaring a
manuscript complete. Preserve useful contrary evidence and distinguish optional
presentation edits from missing scientific support.

For LaTeX, follow the [build guide](references/latex-build.md) only when a build is
needed and authorized. Compilation is a delivery check, not scientific review.
Journal-specific formatting requirements must be checked against the journal's
actual current instructions; this guide supplies no universal class or word limit.

Describe data/code availability truthfully: what is accessible, where, under which
conditions and for which analysis version. Do not invent an archive DOI or imply
that a package reruns unavailable observations or network services. Optional final
packaging belongs after the scoped science is complete, if requested or required.

Deliver the revised manuscript and the few specific unresolved scientific or
editorial issues. Seek the requested scientific/coauthor review before submission;
an assistant cannot grant authorship approval or an official journal decision.
Optional installed helpers include `scientific-peer-review`, `citation-verifier`
and `scientific-figure-standards`; none is a filesystem dependency.
