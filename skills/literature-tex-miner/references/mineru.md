# MinerU Remote PDF-to-LaTeX Conversion

## Contents

- [Purpose and permission](#purpose-and-permission)
- [Prepare the conversion](#prepare-the-conversion)
- [Distinguish API surfaces](#distinguish-api-surfaces)
- [Existing SciPaperFinder client](#existing-scipaperfinder-client)
- [Verify the reconstructed science](#verify-the-reconstructed-science)
- [Failures and delivery](#failures-and-delivery)

## Purpose and permission

Use MinerU when an adopted equation or table needs faithful extraction from a
PDF and authentic author/journal source or an official data release does not answer
the need. MinerU reconstructs content through document recognition; it does not
recover the author's original TeX or establish that the published physics is right.

Prefer the remote API for this workflow. Do not install MinerU models, a local OCR
stack or unrelated package extras merely because the skill was loaded. Remote
conversion uploads the PDF and can consume quota or money: confirm upload rights,
confidentiality and the operator's scope before submitting. Loading this reference
does not authorize a job, installation or account change.

## Prepare the conversion

- Retain the legally acquired PDF and identify its publication, version and the
  relevant pages/equations/tables. Use the receiving discipline's registry; NASA
  ADS is not a universal prerequisite for a retained-PDF conversion.
- Check the actual page count, file size, current service/account limits and
  remaining quota. Do not assume historical free allowances or fixed page caps.
  Resolve an over-limit document with an approved route; do not silently omit pages
  or split the retained original. Approved derivatives need explicit page mappings.
- Keep `MINERU_API_TOKEN`, or the client's fallback `MINERU_API_KEY`, in the runtime
  environment or an approved secret manager. Never print credentials, paste them
  into instructions or write them to generated scripts. For the inspected
  SciPaperFinder client, an explicitly selected `.env` may supply missing values
  with `override=False`; exported values take precedence. The default `.env`
  location belongs to that client, not necessarily the user's current directory.
- Confirm the configured API deployment and its output capabilities. Do not assume
  every endpoint/version can return `.tex`; the inspected V1 client requires both
  `latex` and `zip`. Set `MINERU_API_URL` only for a trusted, verified deployment;
  never send a bearer token to a guessed URL or an unrelated artifact host.

## Distinguish API surfaces

The official documentation inspected on 2026-10-23 describes different interfaces:

- The [hosted precision API](https://mineru.net/apiManage/docs) uses
  `/api/v4/extract/task` and `/api/v4/file-urls/batch`. Its documented request field
  `extra_formats` can request `latex` in addition to default Markdown/JSON exports.
  Its task states and result ZIP fields are not the V1 job schema.
- The same hosted documentation also describes lightweight `/api/v1/agent/parse/*`
  routes that return Markdown, not the precision API's LaTeX export contract.
- The [V1 HTTP service](https://opendatalab.github.io/MinerU/usage/http_api/) uses
  upload/file/job resources such as `/v1/uploads` and `/v1/parse/jobs`. The
  [output contract](https://opendatalab.github.io/MinerU/reference/output_files/)
  lists Markdown/JSON/ZIP outputs for the self-hosted V1 entry point; a renderer's
  ability to emit LaTeX does not establish that the deployed API offers it.

The inspected SciPaperFinder adapter below is a **V1 client requiring advertised
`latex` and `zip` outputs**. Those requirements are not guaranteed by the current
general self-hosted V1 documentation, and the adapter is not an implementation
of the hosted V4 contract. Do not treat changing its base URL as an API migration,
claim universal compatibility or silently substitute Markdown for requested TeX.
Select a client that actually matches the approved deployment and verify its
capabilities before uploading. These are documentation findings, not a live probe.

## Existing SciPaperFinder client

These examples describe the inspected SciPaperFinder `latex` command and
`scipaperfinder.mineru_api.convert_pdf_to_latex` interface, not a bundled FEZA
executable or a live-service test. Use this route only when that client is already
available in the approved project environment. Confirm its installed help/version
and contract; do not assume a public package release matches a local checkout.
An existing approved MinerU connector is also acceptable; inspect its actual schema
rather than transplanting commands between incompatible API versions.

### Verified publication identifier, authentic source first

After setting `PAPER_ID` to a verified DOI or versioned arXiv identifier and
`PAPER_DIR` to an owned output directory, run through the project's interpreter
or command runner:

```bash
scipaperfinder latex "${PAPER_ID:?Set a verified paper identifier}" \
  --mineru-fallback --output "${PAPER_DIR:?Set an owned output directory}"
```

The inspected command tries original arXiv source before resolving and uploading
a PDF. `spf` is an alias in that client. Do not add `--prefer-refereed-pdf` by
default: it intentionally converts an ADS-confirmed refereed publisher PDF before
trying available original source, and has its own ADS-dependent prerequisites.

### An already retained PDF, from any discipline

When the PDF identity and upload permission are established, the existing client
can convert that exact file without a new literature search. Adapt the example
paths; this code performs a real upload when executed:

```python
from pathlib import Path
from scipaperfinder.mineru_api import convert_pdf_to_latex

result = convert_pdf_to_latex(
    Path("literature/paper/published.pdf"),
    output_dir=Path("literature/paper/conversion"),
)
print(result["tex_path"])
```

The inspected adapter checks advertised output formats, uploads the PDF, submits
a parse job, polls with limits and saves the returned TeX, result ZIP and image
assets in a separate `.mineru` directory. Use the actual returned paths; do not
guess successful filenames or declare success from a queued job. Retain native
job/output records when useful; do not add an unrelated checksum campaign.

## Verify the reconstructed science

Label the result `mineru-converted` or `reconstructed_latex`, never authentic source.
Keep the original PDF and conversion output separate. Check every equation, number
or table row actually adopted against the rendered original page, including signs,
Greek symbols, exponents, subscripts, units, normalization and uncertainty notation.
Tables need their headings, footnotes, scaling factors and row/column associations.
Do not silently replace missing cells, infer lost signs or repair OCR to agree with
unvalidated production code.

Treat downloaded archives as untrusted: inspect paths, links and expanded sizes,
extract safely into a new owned directory, and never execute bundled scripts or
TeX shell commands. The main skill's archive rules apply to conversion bundles too.

Record the source/page locator, conversion channel and consequential discrepancies
in existing notes or at the actual use site. Check definitions, applicability and
errata before binding a value to code. PDF-versus-TeX agreement establishes faithful
transcription, not an independent physical oracle or empirical calibration.

## Failures and delivery

Distinguish missing credentials, upload restrictions, exhausted quota, service
failure, unsupported output formats and unverified transcription. Retry only within
the approved bounds; do not install models, change providers or spend more quota
silently. A failed extraction does not prove the scientific method impossible.
Use an already verified table, legitimate source release or independent derivation
when it resolves the affected question. Leave unverified values unused rather than
guessing, and state the actual remaining dependency and next plausible route.

Deliver the checked equation/table values and their physical meaning first, with
the PDF locator and actual output paths behind them. A returned ZIP or `.tex` file
alone is not a completed scientific extraction. These recipes were source-inspected;
their presence does not claim a new installation, API call or successful conversion.
