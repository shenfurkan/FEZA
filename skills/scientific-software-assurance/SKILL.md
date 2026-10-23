---
name: scientific-software-assurance
description: "Review scientific software changes for silent numerical/data failures, unsafe fallback, reproducibility defects and misleading verification. Inspect connected callers and outputs, apply contract-aware checks and give actionable evidence-based findings; not institutional certification or hardware safety approval."
license: MIT
---

# Scientific Software Assurance

A plausible wrong scientific result can be worse than an explicit failed
calculation. Review the paths that could produce it, not only a diff's appearance.
The [fail-closed rubric](references/fail-closed-rubric.md) owns the detailed checks.
Apply the project's actual standards and acceptance authority; no agency's classes,
review process or approval requirements automatically govern another institution.

## Scope the review

Use the change set named by the user and read the affected implementation, direct
callers, output consumers and tests. Preserve unfamiliar existing work. A review
request authorizes findings, not source edits, broad test campaigns or releases.
If scope is genuinely ambiguous, identify the narrow assumed scope or ask rather
than audit the whole repository by default.

Identify which outputs users rely on and the consequence of a wrong result.
Choose review depth from that consequence and the actual decision; do not invent
hardware safety classification for an offline analysis library.

## Inspect connected behavior

1. Trace relevant inputs through validation, transformations, numerical kernels,
   errors/fallback and serialization to the actual scientific consumer.
2. Apply the rubric to the changed/reached paths. Distinguish a demonstrated defect,
   plausible risk, justified behavior and an unperformed check.
3. At changed numerical boundaries, inspect finite values, NaN, positive infinity
   and negative infinity separately under the documented mathematical contract.
   A NaN-only guard does not reject unexpected positive infinity. Valid zero-density
   negative infinity and intentional exact endpoint comparisons are not defects.
4. Review uncertainty, approximation and dtype changes against the observable's
   required precision; finite output or optimizer termination alone is insufficient.
5. Check independent expectations and the real unit being tested. Mocks test their
   declared substituted boundary, not the calculation they replace. Keep failed
   cases visible and distinguish statistical acceptance from ordinary regression.
6. Check interface changes: numeric meaning, column order, defaults, precision,
   file formats and error behavior. A nominally cosmetic change can break consumers.
7. Assess resource/failure behavior, dependency contracts, raw-data protection and
   secret handling. Smaller working sets must not silently shrink the experiment.

## Verdict and findings

For a merge/release review, use **BLOCK**, **APPROVE WITH CONDITIONS** or **APPROVE**
at the inspected scope. A blocker is a demonstrated path to consequential wrong
results, data loss, secret exposure or an unmet required acceptance condition.
Do not declare approval from missing evidence or invent a project-specific waiver.

Give each material finding its location, observed behavior, scientific consequence,
smallest justified fix and closure evidence. State unexecuted checks and unresolved
assumptions. A focused question needs no fixed multi-section report or generated
audit file. This review is neither certification nor proof that uninspected code
contains no defects.
