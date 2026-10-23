---
name: unit-time-fidelity
description: "Check units, time representations, coordinate/sign conventions and normalization when values cross scientific software boundaries or a result differs by a suspicious factor/offset. Resolve the representation before changing the affected physical calculation."
---

# Units, Time and Convention Fidelity

A constant factor or offset is a hypothesis to investigate, not an automatic
diagnosis. Inspect the actual producer and consumer, not a remembered conversion.

## At the relevant boundary, establish

- **Quantity and units:** what is measured/computed; dimensional versus dimensionless
  quantities; energy, momentum, length, time, rate, density or normalized weight.
- **Unit convention:** the explicit system and scale. If natural units are used,
  specify which constants are set to one and how physical dimensions are restored.
  A numeric value cannot be converted just by renaming a column.
- **Time representation:** absolute timestamp, elapsed time or index; unit, scale,
  epoch, synchronization and correction state as relevant. An epoch offset is not
  a clock-scale conversion or an instrument timing correction.
- **Coordinates and signs:** frame, axes, metric/angle convention, ordering and any
  reference transformation actually used. Do not infer them from value magnitude.
- **Normalization:** counts versus rates/densities, fractions versus percentages,
  differential versus integrated quantities, event/sample weights and bin widths.

Use the project's existing unit types or explicit names and its verified constants
library. Exact conversions need a convention/derivation, not an invented empirical
citation; measured/calibrated factors need their uncertainty and validity domain.
Do not force a particular library or constants file into an unrelated project.

## Transform the full scientific quantity

1. Read native metadata, adapter behavior and the downstream mathematical contract.
   Check corrections already applied so they are not repeated.
2. Carry uncertainties and relevant covariance through the same transformation;
   nonlinear conversions may need a joint distribution rather than symmetric errors.
3. Retain coordinate/selection identifiers required to align arrays, weights,
   calibration and uncertainty. A row reorder can break alignment without changing units.
4. Check dimensional consistency, limiting cases and inverse/round-trip behavior
   where appropriate. Exact unit algebra alone does not prove numerical accuracy.
5. Reject or leave unresolved the affected quantitative use when relevant units or
   conventions cannot be established; do not guess a scale from a plausible result.

Document the resolved input/output convention at the owning interface. This is not
a demand for unrelated provenance audits or boilerplate on nondimensional helpers.

If installed, `statistical-inference` can help with dependence/inference questions
and `scientific-debugger` with a discrepancy that survives the representation check.
They are optional helpers, not filesystem or installation dependencies.
