# NASA standards behind FEZA's workflow

Applicability depends on the project's intended use and governing agreements. FEZA
**aligns with** these practices; it does not make any project compliant and it
cannot tailor a requirement. Compliance with NPR 7150.2D is verified by submission
of the completed Requirements Mapping Matrix(ces) and by internal and external
controls (P.5); relief from an applicable "X" requirement "can be granted only by
the designated TAs, Engineering, and SMA, or, for security issues, the NASA CIO"
(SWE-125 note).

## Contents

- [Who is bound](#who-is-bound)
- [Which class is a science analysis?](#which-class-is-a-science-analysis-npr-71502d-appendix-d)
- [What FEZA covers, and what it does not](#what-feza-covers-and-what-it-does-not)
- [Reporting results](#reporting-results-nasa-std-7009b)
  - [Claims and evidence](#claims-and-evidence)
- [Releasing code](#releasing-code-spd-41a-apd-policy-13)

## Who is bound

| Document | Binds | Reaches a grant-funded researcher? |
|---|---|---|
| NPR 7150.2D software engineering | NASA HQ and Centers | Only via award terms: applicability "alone is not sufficient to stipulate requirements for the contractor, grant recipient, or agreement" (P.2.a) |
| NASA-STD-8739.8B software assurance | NASA HQ and Centers, keyed to NPR 7150.2D class | Only via applicable agreement terms |
| NASA-STD-7009B models and simulations | Where a directive or agreement cites it (§1.2) | Same |
| SPD-41a SMD information policy | SMD-funded work (§II.F), subject to its scope/exclusions | Via applicable SMD funding terms |
| APD Policy-13 v1.8 | Astrophysics Division funding (expires 2027-01-13) | Via applicable APD funding terms |

NPR 2210.1E (software release) governs NASA's own releases. NASA civil servants may
release "Scientific Research Demonstration Software" with the paper (P.2.g).

## Which class is a science analysis? (NPR 7150.2D Appendix D)

| Class | Definition (verbatim fragments) | Scope reminder, not a classification decision |
|---|---|---|
| C | "Flight or ground software used to analyze or process mission data" | Out of scope: mission pipelines follow the mission's process |
| D | "Ground software that performs secondary science data analysis" | Check all definitions/exclusions; publication alone does not select D |
| E | "Software used to perform minor analyses of science or experimental data"; excludes "Software that can adversely affect the integrity of engineering/scientific artifacts" | Minor/exploratory use is insufficient without checking exclusions and criticality |

NPR 7150.2D §3.5.1–3.5.2 (printed pp.24–25) and Appendix D.1–D.2 (p.79)
require classification from intended use, system criticality, human dependence,
complexity and investment, retaining the determination. When multiple classes
apply, assign the highest applicable class, not automatically D. Read the full
Class C/D/E definitions and exclusions (pp.82–85); the table is not exhaustive.

**Using this guidance:** Establish intended use, failure consequences and relevant
acceptance evidence for consequential work. Formal classification and approval
follow the project's governing requirements, not installation of FEZA. Do not add
a NASA classification gate to independent research with no applicable agreement
or project requirement; this does not waive scientific integrity or data protection.

Where formal assurance applies, retain classification rationale, criticality,
acceptance evidence and the responsible human decision-maker. Class C/flight/
operational-control work is outside FEZA's stand-alone process. Unresolved mission
criticality or required approval pauses the affected operation pending project
review, not separable supported work. Binding project/local instructions still apply.

Missing hazard analysis/traceability does **not** establish noncriticality.
Within their applicable project scope, NASA-STD-8739.8B §4.2 (pp.15–16) and
NPR 7150.2D §3.7 (pp.26–27) require an
actual safety-criticality determination. Evaluate mission criticality too: SWE-134
addresses both. Assess IV&V applicability separately under NPR §3.6 (p.25).
Record applicable requirements, verification/nonconformance links and unresolved
decisions; FEZA cannot grant exclusions, tailoring, waivers, TA approval or IV&V status.
Proportionate quick-look reporting is a workflow choice, not a software class.

## What FEZA covers, and what it does not

NPR 7150.2D Appendix C and the LaRC Requirements Mapping Matrix templates for
Class D and Class E
(center versions) carry the same markings.

The table below identifies **related practices**, not requirements implemented or
verified by installing FEZA. It is not a Requirements Mapping Matrix: plans,
classification records, configuration
management procedures (SWE-079–085 beyond 081), coding standards (SWE-061), test plans
(SWE-065/071) and operations/retirement (SWE-075, 077, 194–196) stay with the project.

| Practice | Requirement | D | E | Related guidance / project responsibility |
|---|---|---|---|---|
| Assess acquiring/reusing vs developing | SWE-033 | X | X | Native-tool reuse guidance |
| Cybersecurity assessment incl. OSS risks | SWE-156 | X | X | Project assessment; reuse advice does not perform it |
| OSS/reused component V&V'd "to the same level required to accept a similar developed software component for its intended use" | SWE-027 | X | – | Generated-code checks supply prompts; project acceptance evidence is still required |
| Unit test the code; results repeatable | SWE-062, SWE-186 | X | – | Generated-code checks; actual tests/results remain project work |
| Static analysis for defects, security, complexity | SWE-135 | X | – | Project static-analysis runs; generated-code checks |
| Test against requirements; evaluate and record results | SWE-066, SWE-068 | X | – | Project requirements/evidence; generated-code checks |
| Measure and record code coverage | SWE-189 | X | – | Project coverage measurement and uncovered-code classification |
| Identify configuration items and their versions | SWE-081 | X | – | Input, code and environment provenance |
| Version description for each release | SWE-063 | X | – | Project release description; a VERSION value alone is insufficient |
| Track nonconformances (defects) to closure | SWE-201 | X | – | Check outcomes record defects; the project tracks closure |

Thresholds NASA does not set for this code: SWE-135's note says "no maximum
cyclomatic complexity score is required for non-safety critical software", and
SWE-189 sets no coverage percentage. Its note does require that code left
uncovered be classified as a missing requirement, a missing test, dead code or
deactivated code. SWEHB coverage guidance (guidance only, SWE-189) says statement
coverage "might suffice for non-critical systems where reliability is important but
not safety-related" for research and scientific analysis software.

The phrase "single use software in a Research & Technology project" seen in the
LaRC Class D template (SWE-075/077) is LaRC compliance guidance, not NPR text.

## Reporting results (NASA-STD-7009B)

7009B is "highly recommended" for M&S behind critical decisions; elsewhere its use
"is encouraged" (§1.2). Its note on Analysis says it spans "the gathering and
reduction of data". FEZA uses these reporting practices as an aid for fitted and
derived results, not a mandatory response format for unrelated projects:

- **M&S 33**: report "a quantitative estimate", "a qualitative description", or "a
  clear statement that no quantitative estimate or qualitative description of
  uncertainty is available"; **M&S 34**: describe the process used.
- **M&S 27**: record "warning messages, error messages, and explanations for the messages".
- **M&S 32**: warn on (a) unachieved acceptance criteria, (b) violated assumptions,
  (c) exceeded limits, (d) warning/error messages, (e) unfavorable appropriateness to
  the use, (f) setup or usage issues, (g) waivers, (h) outstanding defects; "In the
  absence of substantiating evidence … a warning is to be provided".
- **M&S 26**: use within "the permissible uses and within the domains of V&V", or
  placard the result with the limit exceeded, the extent and the consequence.
- **M&S 11, 24, 46**: record assumptions, input pedigree, units and coordinate frames.
- NASA-HDBK-7009B §4.5.3 (guidance): an AI application used for analysis "should
  also be evaluated for its possible impacts on credibility". The reviewed copy
  has conflicting approved-cover/draft-header markings; do not treat it as
  authoritative final requirements. FEZA's AI assistance still needs evaluation.

FEZA does not adopt 7009B's criticality matrix, 0–4 credibility scoring or
risk-acceptance records: they need program-set thresholds an agent cannot supply.

### Claims and evidence

These are FEZA's evidence distinctions, not a mandatory response format or an
additional NASA requirements table. Use the rows relevant to the requested claim.

| Claim | Evidence required | Not sufficient |
|---|---|---|
| Generated analysis meets its code contract | Actual project checks and static results, with exact scope and outcomes | An earlier run, another machine, "should pass" |
| A regression protects X | It distinguishes the original bug from the repair | Passing once |
| The physical result meets its criterion | Predeclared comparison including reference uncertainty and dependence | Tests passing, same-pipeline agreement, correct units |
| The uncertainty is σ | Named method, covariance and approximation/domain assessment; sampling when needed | An unexplained fit covariance |
| A consequential result is ready for its intended use | Relevant results-report fields and acceptance evidence | A plot that looks right; a subagent saying "success" |

Report unrun checks and unexplained warnings; withhold the affected claim rather
than withholding every otherwise usable output.

## Releasing code (SPD-41a, APD Policy-13)

SPD-41a "shall" is mandatory, "should" is recommended (§II.H):

- §VII.C: SMD-funded software "used in support of a scientific, peer-reviewed
  publication shall be released as open source software no later than the
  publication date"; it need not be maintained or supported.
- §VII.D: other software from the award is released at its end, "to extent practicable".
- §III.D, once public: a repository "widely recognized by the community" (v), "citable
  using a persistent identifier" (vii), reported for the NASA software catalog unless
  single-use (vi), and, for software projects, "a code of conduct and guidelines for how
  to make contributions" (iv). A permissive license is a "should" (iii).
- §III.G: activities "shall include a software management plan".
- Out of scope: "software developed only for preliminary analysis, plans for future
  research, or communication with colleagues" (§II.B.iii.b).
- APD Policy-13 §3.2.h: Astrophysics-funded software "shall be released under a
  permissive license". The OSS Guidance v2.2
  notes documentation and testing "are not required to be provided under SPD-41a",
  so FEZA's tests are engineering practice, not an open-science obligation.
