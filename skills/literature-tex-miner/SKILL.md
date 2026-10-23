---
name: literature-tex-miner
description: "Acquire authentic manuscript source or reconstruct a source-unavailable PDF through the remote MinerU API. Verify adopted equations, numbers, tables and normalizations against the original publication. Prefer author/journal source and official data releases, handle downloaded archives safely, and distinguish faithful transcription from scientific correctness. Includes existing-client CLI and retained-PDF conversion recipes."
---

# Authentic Scientific Source Extraction

An equation read from a lossy PDF text dump can lose signs, exponents, indices or
normalization. Authentic source improves extraction fidelity, not the physical
correctness of the equation or its applicability to the data.

## Establish the source

Verify the publication's identity, version, accepted/published counterpart and
relevant errata; the optional `citation-verifier` skill can help when installed.
Use an appropriate disciplinary registry or publisher; a particular registry is
not mandatory. Never guess an identifier from the title.

Prefer official machine-readable releases for tabulated values. For equations,
prefer authentic author/arXiv/journal LaTeX when available, checking the rendered
publication and symbol definitions. Resolve macros and included files; a source
archive can contain drafts or conditionally excluded material.

## Acquire and unpack safely

- Retain the downloaded original and its identity/version beside existing project
  literature records; do not require a new metadata format or repository layout.
- For arXiv source, use its source/e-print endpoint with the verified revision;
  unversioned retrieval may change. Inspect HTTP status, content type and magic
  bytes: HTML/error responses and PDFs are not authentic LaTeX.
- Treat archives as untrusted input. Before extraction, reject absolute/traversing
  paths, links and device entries; check expanded sizes against available resources.
  Use the interpreter's safe extraction facilities in addition to these checks.
  Extract into a new bounded directory, never over existing observations or code.
- Do not execute bundled scripts, fetch macro-directed URLs or enable TeX shell
  escape while mining a source. No automatic compilation is needed to read an equation.

Locate the real manuscript through document structure and included files, not an
assumed filename. A failed request does not establish that authentic source does
not exist; distinguish access failure, wrong revision and a genuine PDF-only release.

## When authentic source is unavailable

Check an official author/journal source release and a legal published-PDF route.
An approved local or remote conversion tool may produce reconstructed text/LaTeX;
label it as reconstructed, not author source, and check each adopted equation or
value against the rendered page. Never upload confidential documents without
authorization, assume free quota or install a large OCR stack without approval.

For the concrete **MinerU remote PDF-to-LaTeX workflow**, use
[the conversion guide](references/mineru.md): credential handling, current limits,
the existing SciPaperFinder CLI, direct conversion of a retained PDF, output
handling and page-level verification. FEZA bundles instructions, not the client
or credentials; loading this skill submits no job.

Text-layer/OCR extraction may help navigation, but is not an unchecked numerical
oracle. Where fidelity cannot be established, leave the affected transcription
unresolved rather than guess. Reuse an already verified official table or independent
derivation when it answers the actual question.

## Bind source meaning to the calculation

1. Locate the cited equation/table and all relevant variable definitions.
2. Check coordinate/sign convention, units, normalization, measure/Jacobian and
   approximation order against the actual implementation and consumer.
3. Preserve published precision and uncertainty; record transformations rather
   than silently round, rescale or discard terms.
4. Check version/errata and algebraic equivalence before calling a discrepancy.
   Do not rewrite the source transcription merely to agree with faulty code.
5. Use an independent check appropriate to the claimed accuracy. TeX and PDF from
   the same work corroborate transcription, not independent physical calibration.

Report the source/version, local locator, extraction channel, comparison and unresolved
gap. Retained literature is review evidence, not a runtime dependency to export with
every numerical test bundle.
