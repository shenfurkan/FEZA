# Scientific Programming: Rationale and Limits

Use these notes when the reasoning behind the main skill needs explanation, not
as another mandatory checklist. The supporting documents and inspected passages
are identified in [the main guide's footnotes](../SKILL.md#sources-and-scope).

Scientific computation connects physical assumptions, a mathematical model,
numerical approximation, algorithm, implementation and actual consumer. Correctness
can fail at any connection. Research and software engineering are complementary
responsibilities; numerical-method selection and independent test design can be
research rather than clerical transcription.

| Question | Practical consequence |
|---|---|
| Is the implementation inspectable? | Make numerical inputs/outputs explicit and separate relevant calculation from I/O. Use established interfaces rather than a speculative framework. |
| Is the problem sensitive or the method unstable? | Distinguish conditioning, approximation, rounding, iteration and sampling error. More precision/iterations only address some causes. |
| Could the test disagree with wrong code? | Check the oracle's independence and sensitivity. Saved output or two wrappers around one kernel can repeat a common error. |
| What does numerical agreement establish? | Justify scale-dependent tolerances and compare shape, units and semantics separately. It is not proof of model adequacy. |
| What should be optimized? | Profile representative end-to-end work and compare accuracy as well as time/memory. Hardware preference is not evidence of a bottleneck. |
| Is replay exact? | Check actual RNG/state, call patterns, builds, reduction order and continuation. A seed alone is insufficient; distributional agreement is a different claim. |
| When is repair delivered? | Correct the owning implementation and affected consumers, retain focused independent expectations and measure the scientific effect. A guidance edit is not numerical repair. |

Stability cannot create absent observational information. Repeatability can repeat
a bug. Authentic source can faithfully encode an inadequate physical model. Shared
errors can make a differential comparison look reassuring. Calibrated performance
requires an appropriately distinct evaluation, not just more development examples.

These commitments guide judgment rather than prescribe a fixed sequence or a new
administrative packet. Apply actual authorization, compute budgets and protected-data
rules; do not manufacture certainty or stop at a refusal when a feasible repair is owed.
