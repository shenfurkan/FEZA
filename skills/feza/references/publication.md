# Figures and publication from actual evidence

## Make the requested output

Use retained analysis/data products, not reconstructed or invented numbers. Match
each consequential sentence to an input/output and the relevant completed check.
Draft useful supported text even when one result remains unresolved; identify the
gap rather than filling it with a confident statement or refusing the whole task.

For a figure:

- Read the selected data/order/row and preserve provenance to its native source.
- State masks, binning, normalization, offsets, smoothing or display-only conversions.
- Label axes with the actual units, time scale/origin or coordinate convention.
- Distinguish uncertainties, residuals, limits and model predictions; show relevant
  uncertainty without implying an unassessed confidence/coverage interpretation.
- Use readable typography, an accessible palette and vector output when appropriate.
  Explain marked/omitted samples. Never plot fabricated observations to complete a panel.

A caption should identify the source/selection, plotted quantities, transformations,
uncertainty meaning and the limited conclusion supported by the panel.

## Recipe: a selected spectrum with visible quality information

Input: the [STIS working table](stis.md#recipe-one-declared-first-order-spectrum-to-a-working-table)
and an explicitly chosen serious-DQ bit mask from the applicable documentation.
Output: an editable Matplotlib figure and a display-selection record, not a fit.
Use pipeline ERROR bars without implying an independently established confidence
interval. No points are rebinned or smoothed by the native example.

Adapt the [native DQ and plotting recipe](stis.md#native-dq-selection-and-source-data-plot)
directly in the user's notebook/script. It uses Astropy quantities and Matplotlib,
not a FEZA runtime function. Verify the actual selection and generated code; these
instructions do not establish that a plot or a test ran.

Save the figure to a new path and retain the selection arrays alongside the native
source identity. Report masked/nonfinite/negative-error samples that were not
displayed; exclusion from this plot is not astrophysical rejection. Negative flux
values and measured zeros remain visible. Marked samples are shown without claiming
that their ERROR bars are scientifically usable. Other nonzero DQ bits are governed
by the declared policy, not automatically accepted as high-quality data.

For the caption, replace bracketed prompts with actual inspected information:

> Extracted STIS spectrum from [product, SCI EXTVER and row/order]. Points show
> native valid samples without smoothing or binning. Bars show the pipeline ERROR
> vector; its confidence coverage and calibration covariance were not established
> by this inspection. Crosses mark samples with [documented selected DQ bits].
> [Actual counts/reasons] were not displayed; their native values and selection masks
> are retained in [artifact]. [AI-assisted figure preparation: specific tool (and
> prompt), if any]. [Supported interpretation, if any].

Do not claim that this example produced a figure or counts until it actually ran.
Under AAS's policy, manuscript/figure use of AI also requires actual author
supervision, checking of data fidelity and appropriate disclosure; the template
does not replace that responsibility.

## Methods, results and citations

Methods describe what actually ran: inputs, product/release versions, selections,
software/settings, assumptions, uncertainties and completed checks. Distinguish a
proposed operation from an executed result. A diagnostic or successful pipeline is
not automatic validation of a physical object or explanation.

Resolve bibliography records through ADS/DOI/publisher metadata and verify the
inspected source supports the sentence. Cite actual-used datasets and software;
use an exact-version identifier/archive when available. Do not invent a DOI or cite
every installed dependency as though it contributed to the result.

Data/software availability statements describe actual paths, repositories, access
restrictions and rights. No public deposit, link, human review or author sign-off is
asserted unless it exists. Drafts can explicitly mark author-supplied information
still needed; that is not a completed submission statement.

## Venue-specific policy

Check the chosen journal/article type's current official policy when preparing a
submission. The AAS manuscript-AI guidance addresses manuscript preparation; it is
not automatically a general prohibition or authorization for scientific analysis.
Disclose actual AI assistance and actual author oversight under the applicable rule.
Do not copy an AAS requirement into another venue without checking it.

FEZA does not submit manuscripts, contact coauthors or upload private data by itself.
Its name and license are not institutional endorsement or scientific certification.
