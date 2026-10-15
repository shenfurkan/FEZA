# HST/STIS extracted-spectrum inspection

## Contents

- [Scope and invariants](#python-reference-snippets--pitfalls)
- [Identify/acquire the product](#identify-and-acquire-the-right-product)
- [Inspect FITS selection](#inspect-the-actual-fits-selection)
- [Units and calibration](#units-and-calibration-switches)
- [DQ and uncertainties](#dq-and-uncertainties)
- [Working-table recipe](#recipe-one-declared-first-order-spectrum-to-a-working-table)
- [DQ selection and plotting](#native-dq-selection-and-source-data-plot)
- [Deliver](#deliver)

## Python Reference Snippets & Pitfalls

Native Astropy recipes for the user's notebook or script. Inputs, selectors and
quality policies come from the actual product and its documentation; the snippets
supply no surrogate observations or calibration.

Scope: first-order STIS `x1d`/`sx1` product inspection (`sx1` is the
combined-exposure variant where the mode produces it) and faithful visualization:
- **First-order filtering:** Enforce `SPORDER == 1` before applying first-order
  inspection recipes; do not silently concatenate or mix echelle/multi-order rows.
- **Valid-element slicing:** Slice spectral arrays (`WAVELENGTH`, `FLUX`, `ERROR`, `DQ`)
  to `[:nelem]` using the row's validated `NELEM` count (`0 < nelem <= len(a)`),
  never reading fixed-width binary-table padding as science data.
- **Bitmask discipline:** Filter serious data-quality flags via integer bitwise AND
  (`(dq & sdqflags) != 0`, with the policy read from `SDQFLAGS`) before scientific
  consumption, keeping missing `SDQFLAGS` fail-closed (never defaulting it to `0`).

This is not CALSTIS reduction, re-extraction, echelle splicing or a low-count fitter.

## Identify and acquire the right product

Use MAST observation/product metadata and established clients. Distinguish mission
`obs_id` from the MAST observation/group identifier used to request a product list.
Check instrument, detector, grating/aperture, science product type, access status,
filename and `dataURI`. A discovery row, preview or rectified product is not necessarily
the requested one-dimensional extracted spectrum.

Inspect each download outcome. Retain the unchanged native FITS. A failed download
remains a failed product, not an empty spectrum; successfully acquired products
may still be inspected.

## Inspect the actual FITS selection

With an established FITS reader, inspect primary/extension headers and SCI table
structure before interpreting arrays. Declare EXTNAME/EXTVER, row and spectral order;
do not concatenate multiple rows/orders silently. Retain:

- Instrument/detector/configuration and exposure/wavelength metadata.
- Processing version, calibration switches, reference names and relevant HISTORY.
- `SPORDER`, `NELEM`, `WAVELENGTH`, `FLUX`, `ERROR`, `DQ` and their raw `TUNIT` values.
- Structural/checksum findings, masks, null/scaling metadata and array capacities.

SCI rows contain array-valued spectra. Validate `NELEM` against the stored capacities
before indexing or allocation; distinguish valid elements from padding. Preserve
native precision, sample order, masks and DQ. Missing format checksums are
"not provided", not passed checksum verification.

## Units and calibration switches

The handbook names extracted wavelength units as angstroms. If an identity-checked
STIS WAVELENGTH column contains the exact legacy token `Angstroms`, an explicit
interpretation as standard Angstrom can resolve that metadata mismatch without
changing values. Retain raw token, interpreted unit and handbook basis. This is
not permission for a global alias, plural stripping, guessing arbitrary units or
applying the same exception to FLUX.

Read `FLUXCORR` before labeling a flux axis or its uncertainty. When flux calibration
did not run, handbook semantics zero the FLUX values while ERROR stays in counts/s:
those zeros are not observations of zero astrophysical flux. Completed switches and
familiar reference names describe processing history, not current-reference
validity or scientific fitness. Point-source calibration assumptions matter for
extended targets.

Separate usable native I/O, dimensional/unit interpretation, calibration history
and quantitative scientific readiness. An unresolved calibration issue need not
prevent an honest product/header/DQ report.

## DQ and uncertainties

Interpret DQ using the applicable instrument/mode documentation and recorded
`SDQFLAGS`; report affected samples. Do not silently delete them or turn every
nonzero flag into an identical scientific rejection. If the user requests a selection,
state the bit policy and retain its mask/selection record.

`ERROR` is a pipeline error vector, not automatically a complete Gaussian likelihood,
background model or calibration covariance. Low-count questions require count/rate
and exposure provenance, detector/mode applicability and treatment of background.
The official `poisson_err` utility uses the MAMA-specific `NET_ERROR` input to back
out the pre-dark-subtracted counts; it does not itself supply independent
coverage or a complete background/calibration model. Its presence is not a reason to
replace native errors or overwrite the input.

## Recipe: one declared first-order spectrum to a working table

First run the [FITS inventory](astropy-workflows.md#1-inventory-a-native-fits-before-choosing-data).
Input: native local STIS file, actual SCI EXTVER and row index. Output: an in-memory
table of valid elements, retaining masks/DQ and raw-unit/calibration context. This
recipe prepares a flux plot only when `FLUXCORR` is COMPLETE; other states still
permit the header/native-product audit above, not the same physical-flux label.
No example spectrum or calibration values are supplied or invented.

For an admitted bounded file, `extver` and `row_index` are explicitly selected from
the inventory. Preserve the native table masks before slicing valid elements:

```python
import operator

import astropy.units as u
import numpy as np
from astropy.io import fits
from astropy.table import Table

names = ("WAVELENGTH", "FLUX", "ERROR", "DQ")
with fits.open(path, mode="readonly", memmap=False) as hdul:
    primary = hdul[0].header
    if primary.get("INSTRUME") != "STIS":
        raise ValueError("Not an identified STIS product")
    sci = hdul["SCI", extver]
    if not isinstance(sci, fits.BinTableHDU):
        raise TypeError("The selected SCI HDU is not a binary table")
    native = Table.read(sci)
    index = operator.index(row_index)
    if not 0 <= index < len(native):
        raise IndexError("SCI row is out of range")
    if any(np.ma.is_masked(native[name][index]) for name in ("SPORDER", "NELEM")):
        raise ValueError("Order/valid-element count is missing")
    if operator.index(native["SPORDER"][index]) != 1:
        raise ValueError("Select the appropriate recipe for this spectral order")
    nelem = operator.index(native["NELEM"][index])
    arrays = {name: native[name][index] for name in names}
    if nelem <= 0 or any(a.ndim != 1 or len(a) < nelem for a in arrays.values()):
        raise ValueError("NELEM is inconsistent with stored capacities")
    raw_units = {name: sci.columns[name].unit for name in names}
    if any(not raw_units[name] for name in ("WAVELENGTH", "FLUX", "ERROR")):
        raise ValueError("A required spectral unit is absent")
    wave_unit = (u.AA if raw_units["WAVELENGTH"] == "Angstroms"
                 else u.Unit(raw_units["WAVELENGTH"], format="fits"))
    flux_unit = u.Unit(raw_units["FLUX"], format="fits")
    error_unit = u.Unit(raw_units["ERROR"], format="fits")
    flam_unit = u.erg / (u.s * u.cm**2 * u.AA)
    if not wave_unit.is_equivalent(u.m):
        raise u.UnitConversionError("WAVELENGTH is not a length")
    if not all(unit.is_equivalent(flam_unit) for unit in (flux_unit, error_unit)):
        raise u.UnitConversionError("FLUX/ERROR are not F_lambda units")
    if primary.get("FLUXCORR") != "COMPLETE":
        raise ValueError("Physical-flux plotting is unsupported by this calibration state")
    spectrum = Table({name: arrays[name][:nelem].copy() for name in names})
    for name, unit in (("WAVELENGTH", wave_unit), ("FLUX", flux_unit), ("ERROR", error_unit)):
        spectrum[name].unit = unit
    spectrum.meta.update({
        "source_path": str(path), "SCI_EXTVER": extver, "row_index": index,
        "SPORDER": 1, "NELEM": nelem, "raw_TUNIT": raw_units,
        "FLUXCORR": primary.get("FLUXCORR"), "CAL_VER": primary.get("CAL_VER"),
        "PHOTTAB": primary.get("PHOTTAB"), "TDSTAB": primary.get("TDSTAB"),
        "SDQFLAGS": sci.header.get("SDQFLAGS"),
    })
```

This rejects unresolved physical-flux use, not the observation: retain and report
its native/header information even if this recipe cannot produce that plot.
`NELEM` is the valid sample count, never the allocated vector length. Do not
include padding, concatenate orders, invent missing fields or change raw units.

Keep warnings visible: Astropy may report the legacy wavelength token before its
explicit interpretation. That is not a reason to repair the source header. The
table is a derivative selection, not a replacement native FITS. Retain the original
capacities/padding and other header/extraction fields in the audit. Unit/state
checks do not establish current reference validity or confidence coverage.

Use the [source-spectrum plot](publication.md#recipe-a-selected-spectrum-with-visible-quality-information)
with a documented DQ bit policy. For an integrated spectral measurement, declare
sample/bin weights, selected intervals and background/covariance treatment; the
[linear measurement recipe](astropy-workflows.md#7-measure-and-propagate-before-interpreting)
does not invent these inputs. Do not turn an ERROR band into line significance.

## Native DQ selection and source-data plot

Use the actual inspected `SDQFLAGS` or an explicitly justified alternative policy.
Absent metadata is **not zero**. Integer bit operations preserve the DQ meaning;
do not cast to float or silently narrow an unsigned bit field. `spectrum` below
is the working table above, and other input products need their own policy.

```python
bits_value = spectrum.meta["SDQFLAGS"]
if bits_value is None:
    raise ValueError("DQ evaluation is unresolved: no declared SDQFLAGS policy")
bits = operator.index(bits_value)
wave_col, flux_col, error_col, dq_col = (spectrum[name] for name in names)
if bits < 0 or dq_col.dtype.kind not in "iu":
    raise ValueError("A nonnegative integer policy and integer DQ are required")
missing = np.logical_or.reduce(
    [np.ma.getmaskarray(col) for col in (wave_col, flux_col, error_col, dq_col)])
wave = (np.asarray(np.ma.getdata(wave_col)) * wave_col.unit).to_value(u.AA)
flux = (np.asarray(np.ma.getdata(flux_col)) * flux_col.unit).to_value(flam_unit)
error = (np.asarray(np.ma.getdata(error_col)) * error_col.unit).to_value(flam_unit)
dq = np.asarray(np.ma.getdata(dq_col))
if dq.dtype.kind == "i":
    dq = dq.view(dq.dtype.str.replace("i", "u", 1))  # Same bits, width and byte order.
if bits > np.iinfo(dq.dtype).max:
    raise ValueError("DQ policy cannot be represented in the native bit field")
finite = np.isfinite(wave) & np.isfinite(flux) & np.isfinite(error)
displayable = ~missing & finite & (wave > 0) & (error >= 0)
marked = (dq & bits) != 0
accepted = displayable & ~marked
if not np.any(displayable):
    raise ValueError("No displayable spectral samples")
selection = {
    "serious_dq_bits": bits, "source_metadata": dict(spectrum.meta),
    "displayable": displayable, "dq_marked": marked, "accepted": accepted,
    "excluded_missing": missing, "excluded_nonfinite": ~finite,
    "excluded_nonpositive_wavelength": wave <= 0, "excluded_negative_error": error < 0,
    "error_meaning": "Native pipeline ERROR; coverage not established here",
}
```

Retain all selection arrays and counts by reason; reasons can overlap. Negative
fluxes and measured zero fluxes remain visible. For unit-aware masked columns,
inspect the mask first: strip the Column wrapper with `np.asarray` before attaching
its unit once, or use `QTable`/`MaskedQuantity`. Multiplying an already unit-bearing
Column by its own unit can square the unit; converting it to plain Quantity can
lose its mask. A zero DQ policy is allowed only when explicitly documented.

For a requested plot, use native Matplotlib; it is optional, not a skill dependency:

```python
from matplotlib import pyplot as plt

fig, ax = plt.subplots()
ax.errorbar(wave[accepted], flux[accepted], yerr=error[accepted],
            fmt=".", color="C0", label="Samples with pipeline ERROR bars")
ax.scatter(wave[displayable & marked], flux[displayable & marked],
           marker="x", color="C1", label="Selected DQ bits set")
ax.set_xlabel("Wavelength [Angstrom]")
ax.set_ylabel(f"Flux density [{flam_unit.to_string('latex_inline')}]")
ax.legend()
```

Keep the figure editable until review, save only to an owned new path, retain
`selection` alongside the source identity, and call `plt.close(fig)` after use.
This is a display, not a fitted likelihood or a new calibration. Before reuse,
verify the actual row/order, masks, capacity, nonfinite and quality edge cases with
independent expectations on the approved host; the recipe is not a test result.

## Deliver

Produce a short audit and, when requested, a metadata-preserving table or source-data
figure. Link the original FITS selection and any declared conversions/masks. A
display-only change belongs in the caption; it is not a new calibration. Preserve
unknown reference/error assumptions and withhold only the affected physical claim.
Do not infer line significance, radial velocity or a low-count confidence interval
from this inspection alone.
