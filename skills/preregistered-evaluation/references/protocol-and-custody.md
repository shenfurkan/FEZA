# Protocol, custody and distinct meanings

## Primary basis

1. Joshua R. Klein and Aaron Roodman, *Blind Analysis in Nuclear and Particle
   Physics*, [SLAC-PUB-12051 manuscript](https://slac.stanford.edu/pubs/slacpubs/12000/slac-pub-12051.pdf).
   The retained author/institution report says “Submitted to Annual Reviews”; its
   pagination is not the journal pagination. Section 2, report pp. 9–11, explains
   hiding an applicable aspect of data/results, limits to experimenter-bias control,
   review before unblinding, and transparent post-unblinding corrections. Section
   3.4, pp. 23–26, gives data-prescaling assumptions and pitfalls. It supports
   neither automatic calibration nor an institution-wide CERN policy.
2. PLOS Biology, [Preregistered Research Article Guidelines for Authors](https://plos-marketing.s3.amazonaws.com/Marketing/Biology+Preregistered+Articles+Guidelines+for+Authors.pdf),
   updated 28 January 2020, snapshot 2026-10-25. Pages 1–3 describe prior peer
   review, in-principle acceptance, registration and editorial handling of changes.
   Page 4 specifies hypotheses, sampling, analyses, exclusions and contingencies;
   page 6 distinguishes pilot/existing-data exposure. Pages 7–9 distinguish
   incremental registrations and exploratory analyses from the approved protocol.
   This is a specific publisher policy, not a generic definition of all registries.
3. FDA, [Multiple Endpoints in Clinical Trials](https://www.fda.gov/media/162416/download),
   final guidance, October 2022. Sections I–II, printed pp. 1–2, limit the scope
   and identify recommendations as nonbinding. Section II.B, pp. 4–5, calls for
   prospective endpoint/analysis specification; §II.C, pp. 5–6, addresses
   multiplicity and changes after unmasking. Section III.A, pp. 6–7, separates
   primary, secondary and exploratory endpoint families. The
   [official status entry](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/multiple-endpoints-clinical-trials)
   still identifies the October 2022 document as Final when inspected on
   2026-10-25; its content-current date is 2024-04-16. This is not a claim that
   FDA governs an arbitrary software evaluation or mandates public preregistration.

The preregistration mechanics below are project policy.
Do not transplant clinical significance cutoffs or a journal's power/Bayes-factor
requirements into another field. Every numeric threshold needs its own rationale
or a user-supplied starting-value label.

## Vocabulary

| Term | Distinct commitment |
|---|---|
| Prespecification | Analysis choices stated before the relevant outcome exposure |
| Preregistration | A prospective protocol deposited with an identifiable timed record |
| Local freeze | An internal fixed version with explicitly limited timestamp/custody evidence |
| Blinding | Specified information is hidden while outcome-sensitive choices are made |
| Registered Report | Publisher-specific protocol peer review and in-principle acceptance process |

A preregistered analysis can be unblinded; a blinded analysis need not have a public
registration. A Registered Report is not obtained by naming a file that way.

## Minimal protocol record

| Field group | Required content |
|---|---|
| Question | Hypotheses, competing explanations, estimand, intended use and domain |
| Outcomes | Primary/secondary definitions, population, units, contrasts and denominators |
| Decisions | Thresholds and rationale, uncertainty, multiplicity and sequential looks |
| Selection | Inclusion/exclusion, missingness, failures, stopping/resource rules |
| Analysis | Exact code hash, configuration/dependencies and data/split identities |
| Randomness | Generator/seed/stream policy, required continuation and ordering |
| Controls | Development exposure, held-out separation, null/alternative controls |
| Blind | Hidden information, custodian/access boundary, leak review and release criteria |
| Freeze | Version, digest algorithm, UTC, approved immutable record and actual receipt |
| Deviations | Old/new version, rationale, authority, timestamp, exposure and claim impact |

Store key **custody metadata**, not the secret key. Do not publish/upload a protocol,
data or hashes that disclose protected material without the data owner's approval.
An approved record can remain private; public posting is not implied by this skill.

## Failure and amendment handling

- Prior to exposure, a legitimate amendment is a new prospective version, not an
  overwrite. A purportedly outcome-neutral change still needs an exposure statement.
- After exposure, retain the original result/rule and disclose invalidity or deviations.
  Do not lower thresholds, suppress failed candidates, or call repair development
  a fresh confirmatory evaluation on the same already exposed material.
- Never publish a known-wrong analysis merely because its protocol was frozen.
  An invalid confirmatory result may remain unresolved while a scientific defect is
  repaired and a genuinely protected next assessment is designed.
- Clinical guidance and the blinding review do not mandate identical amendment rules.
  The no-retroactive-threshold rule is a stricter local policy.

## Review cases

| Case | Expected disposition |
|---|---|
| Hash exists but no trustworthy chronology | Locally frozen/uncertain timing, not verified preregistration |
| Diagnostic plot reveals protected result | Record exposure; stop treating the affected assessment as blind |
| Threshold changed after scores are seen | Exploratory/deviation, not the original confirmatory claim |
| Protocol error is discovered after unblinding | Disclose, repair and bound the next protected assessment |
| File is called Registered Report without stage-one acceptance | Correct the label; no journal-status claim |

Use these as review criteria; they are not evidence that an evaluation was valid.
