---
name: code-documenter
description: "Write or revise scientific module, class and function documentation from the actual implementation: source/derivation, units, assumptions, uncertainty and failure behavior. Put result-interpretation restrictions only at boundaries that actually own them."
---

# Scientific Code Documentation

Explain the contract a downstream reader must understand, not a repeated warning
that every function is somehow responsible for publication or discovery decisions.

## Read before writing

Inspect the implementation, callers, data structures and tests. Identify actual
formulas, coefficients, units, approximations and error paths. Separate behavior
implemented today from a desired correction; documentation does not perform repair.

## Document the applicable contract

1. **Purpose and derivation/source.** For empirical/non-standard scientific relations,
   give a verified primary source/version and equation/table locator. Exact identities
   and unit conversions need their convention, not an invented paper. Numerical or
   policy settings need their rationale rather than fabricated literature support.
2. **Inputs and outputs.** State physical units, coordinate/sign conventions, shapes,
   normalization and uncertainty semantics where they can be ambiguous. Distinguish
   measured data, simulated quantities and model-derived estimates.
3. **Applicability.** State the implemented assumptions, domain, approximation and
   known precision/model limitations. Do not invent a valid range to fill a heading.
4. **Failure and mutation behavior.** Describe actual validation, exceptions,
   missing-value treatment, allowed mathematical infinities and in-place changes.
   Do not claim finite-input rejection when the function performs no such check.
5. **Interpretation at its owner.** If this routine owns a reported diagnostic or
   decision, explain what that output supports. A unit conversion/integrator with
   no such responsibility needs no claim-eligibility paragraph or invented flag.

Put shared definitions at the module/class boundary and refer to them from functions
instead of duplicating boilerplate. Use the project's existing documentation style,
whether docstrings, API comments or another established convention.

## Check the finished text

- Every documented validation/return field exists in the actual implementation.
- Units, normalization, uncertainty and applicability agree with the caller.
- Sources are locally retained and inspected where cited; unresolved provenance
  is explicit, never repaired with a guessed identifier.
- No test, input validation or scientific boundary was weakened for documentation.

Return the changed documentation and meaningful unresolved gaps. A separate
documentation report file is not required for ordinary edits. For method correctness,
consult the optional `scientific-method-documentation` skill, if installed; for source
identity, `citation-verifier` is another optional helper. Neither is an installation dependency.
