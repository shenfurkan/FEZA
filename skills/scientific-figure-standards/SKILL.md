---
name: scientific-figure-standards
description: "Creates and reviews scientific figures so the evidence is readable and honest: final size and export, color-blind-safe encodings, axis units and normalization, uncertainty, residuals, and disclosed binning and selections. Use whenever a plot, chart, heatmap, image panel or multi-panel figure is made or fixed for a paper, poster, thesis, slide or report, including requests like 'make this figure publication-ready' or 'review my plotting script', in any discipline. Not for validating the analysis behind the figure."
---

# Scientific Figure Standards

Make the evidence and its limits legible. A polished plot cannot repair a wrong
calculation or confer statistical significance.

## Geometry and export

- Use the actual journal, collaboration or presentation template; do not transfer
  another publication's column widths, typography or figure limits as requirements.
- Inspect the exported figure at its intended physical size. Labels, ticks, legends,
  panels and captions must remain readable and unclipped. Automatic tight bounding
  boxes can change the final dimensions.
- Prefer vector output for line art/text where supported, with suitable raster
  resolution for image maps or dense layers. Confirm fonts and transparency in the
  actual delivery format; a filename extension does not prove vector content.
- Use the project's established plotting style and dependencies rather than adding
  another plotting framework for a few figures.

## Meaning and uncertainty

- Match axis units, zero point, coordinate convention and normalization to actual
  arrays. Distinguish counts, weighted yields, rates, densities and fractions;
  disclose bin widths, exposure/normalization and selections where consequential.
- Show uncertainty with its source and meaning: measurement errors, simulation
  statistics, systematic/model bands or interval coverage. Do not treat every band
  as independent Gaussian error or replace asymmetry without explanation.
- For weighted or signed quantities, use an applicable uncertainty treatment and
  axis scale. Do not silently clip negative bins to permit a logarithmic plot.
- Separate data, prediction and residual/ratio panels when they help assess the
  comparison. Define the residual, pull or ratio and handle zero denominators
  explicitly; plot smoothness alone does not demonstrate model adequacy.
- Disclose smoothing, binning, sample exclusions and whether plotting transforms
  differ from the data actually used in the likelihood.

## Accessible and honest encodings

Use color-accessible palettes and a second channel such as markers, line styles or
labels; never encode a scientific distinction by color alone. Check grayscale
legibility where relevant. Do not choose limits or omit points just to hide a
discrepancy. Insets and restricted ranges need clear context.

Keep protected/blinded regions hidden according to the analysis protocol. A plotting
request is not permission to inspect protected data or tune a selection on it.

## Check the actual exported artifact

Verify readable dimensions, matching units/normalization, visible uncertainty and
disclosed selections against the source arrays. Caption what the figure actually
shows, including significant limits. Do not label a source-only check as visual
inspection or a successful render as independent scientific validation.
