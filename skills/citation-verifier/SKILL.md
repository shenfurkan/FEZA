---
name: citation-verifier
description: "Verify an already-selected DOI, arXiv identifier, registry entry or technical source: identity, retained document, publication version, and whether the cited passage supports the implemented relation. Use for citation/code mismatches, not broad literature discovery or numerical validation."
---

# Citation and Equation Verification

Verify the actual source, not the plausibility of a citation string. A real paper
can still be the wrong reference for the equation or claim in front of you.

## Resolve identity

- Match title, authors, publication, year, identifier and version against an
  appropriate authoritative registry or publisher. Use the registry suited to the
  discipline; no particular astronomy service, credential or project CLI is required.
- Distinguish a preprint from its accepted/published counterpart and inspect errata
  or superseding work where they affect the relation. An access failure or an
  empty search result does not establish that a work does not exist.
- Retain the actual legally accessible document and an exact passage/equation/table
  locator before citing it as support. An abstract can support only what it states.
  Do not relocate existing retained documents without checking their consumers.

## Classify the value before demanding a citation

| Kind | Appropriate evidence |
|---|---|
| Measured input | Original measurement/product, uncertainty and processing definition |
| Standard constant | Versioned authoritative constants library or standards release |
| Mathematical identity or exact conversion | Derivation/convention, not an invented empirical paper |
| Numerical or policy setting | Algorithmic rationale or the project's actual policy |
| Empirical coefficient/model | Inspected primary source, units, applicability and uncertainty |
| Deliberate simulation/test input | Declared construction and purpose; never impersonated as measured data |

## Check the relation at its actual consumer

1. Read the cited passage and symbol definitions, then the implementing code and
   direct caller. A source filename or citation comment is not equation verification.
2. Prefer authentic author/journal source for mathematical text and official
   machine-readable tables for fixed data. Follow
  the optional `literature-tex-miner` skill, if installed, for source handling.
3. Check units, coordinate/sign conventions, normalization, probability measure,
   Jacobians, approximations, domain and uncertainty. Resolve macros and match the
   published rendering. Faithful extraction does not establish physical correctness.
4. Test algebraic equivalence before calling a stable reformulation a mismatch.
   Conversely, do not change the source transcription just to match faulty code.
5. Report a demonstrated discrepancy, supported equivalence or specific unresolved
   access/identity issue. Do not certify uninspected relations or silently replace
   an unavailable coefficient with a remembered value.

## Delivery

Give the checked relation/claim, source identity and local locator, implemented
convention, finding and unresolved gap. Use a table only when it helps the requested
review; do not generate a separate dossier or metadata file by default.
Citation verification is not numerical convergence, experimental calibration or
proof that a model applies to the data.
