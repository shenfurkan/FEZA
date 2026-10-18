# [Result in one line: the number, figure or product, and its path]

This optional template supports consequential scientific results, not source
navigation or a simple read-only explanation. Use only the fields the result needs;
retain applicable uncertainty, warnings, input identity and checks. Mark required
but unavailable evidence "not run" or "unresolved"; omit genuinely inapplicable
sections with a brief basis when it matters. This is FEZA's reporting aid, not a
NASA-mandated Markdown format or an approval record.

**Intended use and consequences:** [use; what a wrong result or failed operation could affect]
**Classification, if applicable:** [project determination and rationale; or unresolved, with basis; omit when no formal project requirement applies]
**Safety/mission criticality:** [determination and evidence; or unresolved, never inferred from absent traceability]
**Decision owner:** [responsible human; decision status, not agent self-approval]
**Produced with:** an AI agent (FEZA) [plus who reviewed it, or "not reviewed"]

## Uncertainty (M&S 33–34)

[A quantitative estimate, a qualitative description, OR: "No quantitative estimate
or qualitative description of uncertainty is available."] Obtained by: [method:
propagated covariance, pipeline ERROR vector, bootstrap, ...; or "not applicable"].
Effects not included: [e.g. calibration systematics, wavelength-solution error; or "none known"].

## Reality check

Criterion (written before comparing): [quantity, units, threshold and decision purpose;
combined measurement/reference uncertainty, dependence, distribution assumptions and
false-accept risk; no generic sigma rule without its assumptions]
Independent value: [what, from where; actual source locator] → Outcome:
[criterion met / not met / indeterminate / not run, with residual and uncertainty]

## Warnings and limits (M&S 26, 27, 32)

- Warnings/errors seen, each with its explanation: [verbatim → explanation; or "none"]
- Acceptance criteria not met: [e.g. fit did not converge, failed its own χ² test; or "none"]
- Assumptions violated / limits exceeded: [what, by how much, impact; or "none"]
- Outside permissible use or the verified/validated domain: [limit type, extent,
  consequence; or "no"]
- Method not appropriate for this use, or setup/usage issues: [what; or "none"]
- Unrun applicable project checks (e.g. tests or lint): [what; or "none"]
- Open defects: [list; or "none"]

## Inputs and assumptions (M&S 11, 24, 46)

- Inputs and pedigree: [archive IDs, release, calibration version; measured vs derived]
- Units and frames: [flux/time/coordinate units, time scale, sky frame and epoch]
- Assumptions: [e.g. independent errors, point source, no blending; or "none stated"]

## Configuration (aligned with SWE-063, SWE-081, SWE-189; not compliance)

- Inputs: [paths and versions, exact query]
- Code: [actual project notebook/script path + snapshot/commit; native APIs used;
  new code and why reuse did not fit (SWE-033)]
- Environment: [Python, Astropy, NumPy versions]
- Checks and lint: [actual analysis checks/project validation and input snapshot;
  exact outcomes/skips, static results and unexecuted work; measured coverage and
  uncovered-code classification when required, or "not run".]
