# Astropy recipes for telescope-data analysis

## Python Reference Snippets & Pitfalls

Self-contained recipes to adapt in the user's notebook or script with installed
Astropy/NumPy. Names such as `path`, `table`, `wavelength` and `offsets` denote
inspected user inputs. Record actual library versions; execute on an approved host
and admit file/array sizes before materializing them. Preconditions are explicit; a
recipe is not an independently validated analysis.

## Contents

- [FITS inventory and checksums](#1-inventory-a-native-fits-before-choosing-data)
- [Tables, masks and ECSV](#2-preserve-cataloguetable-semantics-when-exporting)
- [Physical units and spectral densities](#3-convert-the-physical-quantity-not-just-its-axis-label)
- [Time references and scales](#4-reconstruct-time-only-after-interpreting-the-product-convention)
- [Sky association candidates](#5-generate-association-candidates-without-certifying-identity)
- [Image WCS](#6-use-an-image-wcs-with-the-right-axis-conventions)
- [Measurements and covariance](#7-measure-and-propagate-before-interpreting)

## 1. Inventory a native FITS before choosing data

Input: an unchanged local FITS. Output: its HDU inventory and explicit checksum
findings. Select the image/table, EXTNAME/EXTVER and row/order from this inventory
and the instrument documentation. Do not assume `hdul[1]` contains calibrated science.

```python
from astropy.io import fits

findings = []
with fits.open(path, mode="readonly", memmap=False) as hdul:
    hdul.info()
    hdul.verify("exception")
    for index, hdu in enumerate(hdul):
        for keyword, verify in (("CHECKSUM", hdu.verify_checksum),
                                ("DATASUM", hdu.verify_datasum)):
            if keyword not in hdu.header:
                findings.append((index, keyword, "not provided"))
            elif verify() != 1:
                raise ValueError(f"HDU {index}: {keyword} mismatch")
            else:
                findings.append((index, keyword, "matched"))
```

This small-file recipe may read all data for checksums. For large observations,
choose access/chunks from measured memory and retain which HDUs were checked.
Memory mapping does not eliminate allocation by scaling, decompression or copies.
Never use `verify("fix")` to silently repair the retained observation.

Inspect `BUNIT`/`TUNIT`, scaling/null keywords, calibration state and the documented
ERR/variance/inverse-variance/DQ meaning. A column called ERROR or an extension
called ERR does not, by its name alone, specify a standard deviation or likelihood.
Do not suppress FITS/unit warnings and then label the product verified.

## 2. Preserve catalogue/table semantics when exporting

Choose the actual table HDU; do not rely on automatic first-table selection.
`Table.read(hdu)` preserves table metadata/units and recognizes supported FITS nulls.
Inspect the product's null conventions: not every format/type can encode a mask.

```python
from astropy.io import fits
from astropy.table import Table

with fits.open(path, mode="readonly", memmap=False) as hdul:
    selected = hdul[hdu_selector]  # Explicit index or (EXTNAME, EXTVER).
    if not isinstance(selected, (fits.BinTableHDU, fits.TableHDU)):
        raise TypeError("The selected HDU is not a FITS table")
    table = Table.read(selected)
```

For a bounded table with primitive numeric scalar columns, use ECSV's explicit data/mask
serialization and read back the result. This check preserves row order, numeric
kind/width, native values including those under masks, masks and units. Byte order
is not required to survive a text export. Mixin columns such as Time/SkyCoord,
strings, metadata and nested arrays need their own relevant round-trip checks.

For this numeric-scalar recipe, `output_path` is a new destination with an existing
parent directory. Stage and verify before publishing; the hard link below provides
same-filesystem atomic no-clobber publication. If hard links are unsupported, stop
and use an explicitly reviewed completion protocol, not an overwriting rename.

```python
import os
import tempfile
from pathlib import Path

import numpy as np
from astropy.table import Table

if any(col.dtype.kind not in "biufc" or col.ndim != 1
       for col in table.columns.values()):
    raise TypeError("This recipe checks primitive numeric scalar columns only")
output = Path(output_path)
stage_dir = Path(tempfile.mkdtemp(prefix=".ecsv-", dir=output.parent))
staged = stage_dir / "unverified.ecsv"
table.write(staged, format="ascii.ecsv", overwrite=False, serialize_method="data_mask")
restored = Table.read(staged, format="ascii.ecsv")
if restored.colnames != table.colnames or len(restored) != len(table):
    raise ValueError(f"Schema/row count changed; retain evidence in {stage_dir}")
for name in table.colnames:
    before, after = table[name], restored[name]
    if (before.dtype.kind, before.dtype.itemsize, before.shape, before.unit) != (
        after.dtype.kind, after.dtype.itemsize, after.shape, after.unit
    ):
        raise ValueError(f"Column representation changed: {name}")
    np.testing.assert_array_equal(np.ma.getmaskarray(before), np.ma.getmaskarray(after))
    np.testing.assert_array_equal(np.ma.getdata(before), np.ma.getdata(after))
os.link(staged, output)  # Fails if the destination already exists.
staged.unlink()
stage_dir.rmdir()
```

`serialize_method="data_mask"` belongs to the legacy `ascii.ecsv` writer used here;
the newer `format="ecsv"` writer accepts, besides the delimiter, only
`names`/`include_names`/`exclude_names` and ignores or rejects other write
arguments in the documented Astropy 8.0.1 interface.

On failure, the staging directory remains evidence, not a completed derivative.
These explicit readback assertions are comparisons, not removable Python `assert`
guards. Also compare metadata consumed downstream; this numeric-only check does
not establish arbitrary metadata/mixin fidelity. `QTable(table)` retains masks on
unit-bearing columns. For masked quantities, prefer `QTable`/`MaskedQuantity` and
verify `column.quantity`/`u.Quantity(...)`
paths on the installed version. Never use a conversion to bypass missingness.

This is an export consistency check, not independent astrophysical validation.
If it fails, retain the input and failed derivative; do not relax it to drop masked
rows or cast long identifiers to floats. An integer `source_id` is an identifier,
not a physical quantity. A match/join can multiply rows; inspect key multiplicity
and unmatched/ambiguous records before treating the output as a sample.

## 3. Convert the physical quantity, not just its axis label

Keep units on quantities while calculating. `Quantity.to()` performs an ordinary
unit conversion; an equivalency supplies additional physical/conventional meaning.
For spectral densities, use the wavelength of each sample, **never a scalar, mean,
or pivot-wavelength shortcut**.

For fixed sample wavelengths, the exact per-sample conversion and linear error
propagation are:

$$F_\nu = F_\lambda \cdot \frac{\lambda^2}{c}, \qquad \sigma_{F_\nu} = \sigma_{F_\lambda} \cdot \frac{\lambda^2}{c}$$

The $(\lambda^2 / c)$ factor is evaluated **per sample** using Astropy's
`u.spectral_density(wavelength)` equivalency and `astropy.constants.c`, never a
central/mean wavelength or a retyped scalar $c$.

```python
import astropy.units as u
import numpy as np
from astropy.constants import c

flam_unit = u.erg / (u.s * u.cm**2 * u.AA)
if not wavelength.unit.is_equivalent(u.m):
    raise u.UnitConversionError("A wavelength quantity is required")
if not all(q.unit.is_equivalent(flam_unit) for q in (flambda, sigma_flambda)):
    raise u.UnitConversionError("Flux and standard error must have F_lambda units")
if wavelength.shape != flambda.shape or flambda.shape != sigma_flambda.shape:
    raise ValueError("Sample shapes differ")
inputs = (wavelength, flambda, sigma_flambda)
if any(np.any(getattr(q, "mask", False)) for q in inputs):
    raise ValueError("Select unmasked samples explicitly and retain the original mask")
if any(q.dtype.kind not in "fiu" for q in inputs):
    raise TypeError("Real numeric wavelength/flux/error quantities are required")
with np.errstate(over="raise", divide="raise", invalid="raise", under="raise"):
    wave64, flux64, error64 = (q.astype(np.float64) for q in inputs)
    if (any(not np.all(np.isfinite(q.value)) for q in (wave64, flux64, error64))
            or np.any(wave64.value <= 0) or np.any(error64.value < 0)):
        raise ValueError("Invalid wavelength/flux/error; do not replace or clip it")
    equivalency = u.spectral_density(wave64)
    fnu = flux64.to(u.Jy, equivalencies=equivalency)
    sigma_fnu = error64.to(u.Jy, equivalencies=equivalency)
    expected_fnu = (flux64 * wave64**2 / c).to(u.Jy)
    expected_sigma_fnu = (error64 * wave64**2 / c).to(u.Jy)
if not all(np.all(np.isfinite(q.value)) for q in (fnu, sigma_fnu)):
    raise ValueError("Nonfinite converted flux/error")
np.testing.assert_allclose(fnu.to_value(u.Jy), expected_fnu.to_value(u.Jy), rtol=1e-12, atol=0.0)
np.testing.assert_allclose(
    sigma_fnu.to_value(u.Jy), expected_sigma_fnu.to_value(u.Jy), rtol=1e-12, atol=0.0
)
```

**Pitfalls and edge-case guards:**
- **Working precision:** Promote unmasked real quantities to float64 before
  arithmetic, keeping original arrays unchanged. Promotion cannot recover precision
  already lost in storage.
- **Scalar/mean-wavelength shortcut:** Evaluating `u.spectral_density(np.mean(wavelength))`
  corrupts both the continuum slope and the per-sample uncertainty vector $\sigma_{F_\nu}$
  across a spectrum. Always pass the full `wavelength` vector.
- **Mask-dropping conversions:** Verify `column.quantity`, `u.Quantity(column)` and
  `np.ma.MaskedArray(...) * unit` on the installed version before relying on them; a
  dropped mask silently exposes underlying values. Use `QTable(table)[name]` or
  extract `np.ma.getmaskarray(col)` explicitly before converting unmasked samples.
- **Tolerance trap at tiny flux scales:** Default `np.allclose(..., atol=1e-8)` passes
  even if an astronomical flux around $10^{-15}\,\mathrm{erg\,s^{-1}\,cm^{-2}\,\AA^{-1}}$
  is wiped to zero. Always verify with `atol=0.0` and a tight relative tolerance
  (`rtol=1e-12`) against the explicit `(flambda * wavelength**2 / c).to(u.Jy)` oracle.
- **Underflow and nonfinite values:** An underflow failure requests an explicit
  range/error analysis; do not silently replace it with zero. Negative measured flux
  and zero error remain distinguishable from missing data; zero error does not
  automatically define a usable likelihood.

The uncertainty conversion above assumes standard deviations, fixed known sample
wavelengths, and the same linear conversion of both vectors. Apply it to an
explicitly selected finite, positive-wavelength subset with its mask retained.
Uncertain wavelength calibration needs additional propagation; covariance changes
as `C_new = J C_old J.T`, not merely by relabeling diagonal errors.

Counts, count rates, integrated flux, flux density and surface brightness differ.
Dividing by an exposure does not flux-calibrate a detector; a pixel area does not
follow from the axis names. Doppler conversions additionally require a declared
rest value, velocity convention, wavelength medium and reference frame. Converting
parallax units is not a justified distance posterior.

## 4. Reconstruct time only after interpreting the product convention

Identify format, scale, origin, time unit, reference position and applied corrections.
Instrument keywords may include `TIMESYS`, `TIMEUNIT`, `MJDREFI`/`MJDREFF`, `TIMEZERO`
and `TREFPOS`; their presence/placement and meanings are product-specific.
**Preserve two-part MJD split-time precision** by passing integer and fractional parts
separately via `Time(mjdrefi, mjdreff, format="mjd", scale=scale)` without
pre-summing into a single float.

For a product documented as uniform-scale offsets from an MJD reference, this
recipe accepts the actual inspected reference, offsets, zero term and units. Resolve
keyword locations and column/header unit precedence from the product first: `header`
contains the inspected time metadata and `offsets` contains numeric TIME values in
that unit. Missing `TIMEZERO` is not silently replaced with zero; a format-defined
default requires a documented interpretation before adaptation.

```python
import astropy.units as u
import numpy as np
from astropy.time import Time, TimeDelta

timesys = header["TIMESYS"]
scale = timesys.lower()
if scale not in {"tai", "tt", "tcb", "tcg", "tdb"}:
    raise ValueError("Use the appropriate reader for this non-uniform/unsupported scale")
time_unit = u.Unit(header["TIMEUNIT"], format="fits")
if not time_unit.is_equivalent(u.s):
    raise u.UnitConversionError("TIMEUNIT must be a time unit")
mjdrefi, mjdreff, timezero = header["MJDREFI"], header["MJDREFF"], header["TIMEZERO"]
time_inputs = (mjdrefi, mjdreff, offsets, timezero)
if (any(np.any(getattr(q, "mask", False)) for q in time_inputs)
        or any(not np.all(np.isfinite(q)) for q in time_inputs)):
    raise ValueError("Select finite unmasked time inputs and retain their masks")
reference = Time(mjdrefi, mjdreff, format="mjd", scale=scale)
elapsed = TimeDelta(offsets * time_unit, scale=scale)
zero = TimeDelta(timezero * time_unit, scale=scale)
times = reference + elapsed + zero
if not np.all(np.isfinite(times.jd1)) or not np.all(np.isfinite(times.jd2)):
    raise ValueError("Nonfinite reconstructed time")
```

**Pitfalls and edge-case guards:**
- **Never pre-sum `mjdrefi + mjdreff` into a single float**, or add small offsets to a
  large single-float JD/MJD: an IEEE 754 `float64` at MJD $\approx 50{,}000$ loses
  sub-microsecond precision in the mantissa, whereas Astropy's two-part `(jd1, jd2)`
  representation via `Time(mjdrefi, mjdreff, format="mjd", scale=scale)`
  retains full split-time precision.
- **BTJD offset convention:** For a product explicitly documented as
  `BTJD_TDB = BJD_TDB - 2457000 d`, use `Time(2457000, btjd, format="jd", scale="tdb")`
  with validated numeric BTJD values; the offset is a convention, not a new
  barycentric correction. Do not apply an MJD offset recipe to a JD-reference product
  without interpreting its native convention.
- **Verification tolerance trap:** Check against independently specified epochs and
  nonzero offsets/zero terms. Compare `(times - expected_times).to_value(u.s)` with
  `rtol=0` and a justified absolute time tolerance (e.g., `atol=1e-9` s). Default
  `np.allclose` (`rtol=1e-5`) on MJD around $50{,}000$ admits errors approaching
  **half a day ($0.5\,\mathrm{d} \approx 43{,}200\,\mathrm{s}$)**. A time-scale
  round trip (`(times.tai.tt - times).to_value(u.ns)`) checks internal scale
  self-consistency only; it does not test that `MJDREFF` or `TIMEZERO` was applied.

This example takes unmasked numeric offsets/zero terms. Keep the original sample
selection/masks and reference-position metadata with the returned Time.
Nonfinite inputs, ambiguous origins, UTC/leap-second offset conventions and other
representations require their appropriate reader; do not force them into this recipe.
For absolute timestamps use `Time(values, format=actual_format, scale=actual_scale)`.

`.tdb` converts a scale; it does not alone produce BJD. Light-travel-time correction
requires a target direction and valid observer position/ephemeris, and must not be
repeated on an already corrected product. Ground-site convenience functions cannot
stand in for a spacecraft trajectory. Record actual IERS/ephemeris resources and
any degraded-accuracy warnings when an operation uses them.

## 5. Generate association candidates without certifying identity

Use units from the tables and the documented frame/epoch. Before an association,
account for relevant epoch differences and proper motion; transforming a frame does
not itself propagate source motion. Do not invent missing radial velocity/distance
for a precise propagation or fit. Keep the original rows and invalid-coordinate mask.

For two already harmonized, finite, unmasked one-dimensional coordinate arrays:

```python
from astropy.coordinates import search_around_sky
from astropy.table import QTable

index_a, index_b, separation, _ = search_around_sky(coords_a, coords_b, search_radius)
pairs = QTable({"row_a": index_a, "row_b": index_b, "separation": separation})
```

Validate dimensions, masks, finite positions and a finite positive angular radius
before searching. The arrays' frame/epoch harmonization is a scientific precondition,
not something this call verifies. Test one-to-many, no-match and RA-wrap cases;
do not replace all candidates with the nearest neighbor or assume output ordering.

The caller supplies a scientifically motivated angular radius; FEZA supplies no
universal cutoff. Retain all candidate pairs, including multiple neighbors, and
restore indices to the native table selection. No pairs within a radius is not
proof the object is absent. Even the nearest pair needs uncertainty, density and
other discriminating evidence before an identity claim.

## 6. Use an image WCS with the right axis conventions

Input: a selected two-dimensional celestial image with its actual header and any
distortion-table HDUs. High-level pixel coordinates are zero-based pixel centers;
`(x, y)` differs from NumPy's `[row, column]`. Cubes require explicit axis/slice
handling, not a blind application of this two-dimensional example.

```python
from astropy.io import fits
from astropy.wcs import WCS

with fits.open(path, mode="readonly", memmap=False) as hdul:
    selected = hdul[hdu_selector]
    if (not isinstance(selected, (fits.PrimaryHDU, fits.ImageHDU, fits.CompImageHDU))
            or selected.header.get("NAXIS") != 2):
        raise ValueError("Select a two-dimensional image")
    wcs = WCS(selected.header, fobj=hdul)
    if wcs.pixel_n_dim != 2 or wcs.world_n_dim != 2 or not wcs.has_celestial:
        raise ValueError("A two-dimensional celestial WCS is required")
    sky = wcs.pixel_to_world(x, y)
```

Validate finite input/output positions and the documented pixel footprint; do not
blindly extrapolate beyond the image. Retain distortion HDUs when constructing WCS.
An independent known reference pixel is a useful oracle; inverse WCS round trips
only check self-consistency. Set both relative and absolute pixel tolerances.

Keep WCS warnings visible. A catalogue comparison needs compatible epochs/frames
and its own uncertainty; the catalogue may itself be the image's upstream calibrator,
so agreement need not be independent evidence.

## 7. Measure and propagate before interpreting

State the selected samples/aperture, background treatment and definition of the
measurement. A mask changes coverage: keep omitted area/wavelength/time intervals
visible. Do not use zero-filling or interpolation as a missing measurement.

For a declared linear measurement `y = w.T x`, propagate the relevant covariance
as `Var(y) = w.T C w`. Summing `w_i**2 * sigma_i**2` is its independent-error special
case, not a safe default after resampling, smoothing or shared background estimation.
For nonlinear transformations, identify the approximation or appropriate posterior
propagation. A pipeline standard deviation does not include every calibration term.

Input: actual unmasked sample quantities, declared weights with their own units,
and a finite valid covariance matrix in squared sample units. Output: the linear
measurement and its propagated standard uncertainty. Weights may be dimensionless
for a combination or have a wavelength unit for an integration. Their derivation,
bin boundaries, selected intervals and background treatment remain part of the method.

For a bounded dense covariance already established to be symmetric and positive
semidefinite under a declared numerical criterion, use native quantities directly:

```python
import numpy as np

if any(np.any(getattr(q, "mask", False)) for q in (values, weights, covariance)):
    raise ValueError("Select unmasked samples and retain their original masks")
if values.ndim != 1 or len(values) == 0 or weights.shape != values.shape:
    raise ValueError("One weight per sample in a nonempty vector is required")
if covariance.shape != (len(values), len(values)):
    raise ValueError("Covariance dimensions differ from the samples")
if any(q.dtype.kind not in "fiu" for q in (values, weights, covariance)):
    raise TypeError("Real numeric measurement quantities are required")
with np.errstate(over="raise", divide="raise", invalid="raise", under="raise"):
    values64 = values.astype(np.float64)
    weights64 = weights.astype(np.float64)
    cov = covariance.astype(np.float64).to(values.unit**2)
    if not all(np.all(np.isfinite(q.value)) for q in (values64, weights64, cov)):
        raise ValueError("Nonfinite measurement inputs")
    measurement = np.sum(weights64 * values64, dtype=np.float64)
    variance = weights64 @ cov @ weights64
if (not np.isfinite(measurement.value) or not np.isfinite(variance.value)
        or variance.value < 0):
    raise ValueError("Invalid measurement/variance; do not clip it")
sigma = np.sqrt(variance)
```

Establish matrix validity **before** this contraction: inspect symmetry and
eigenvalues or an appropriate factorization, respecting units, conditioning and
legitimate singular covariance. `w.T C w >= 0` for one vector does not prove
positive semidefiniteness. An indefinite matrix can produce a positive answer.
Do not symmetrize or clip eigenvalues to hide failure. Dense storage is quadratic
in sample count; use measured admission and an appropriate structured model when
the real covariance cannot fit, never silently discard off-diagonal terms.

The returned uncertainty is not a confidence interval and is incomplete if required
covariance terms were omitted. Establish float64 before products/reductions, not
after a low-precision sum.

Before fitting, specify units, noise/likelihood assumptions and parameter meanings.
Inspect residual structure and diagnostic limitations; neither a successful optimizer
nor a visually plausible figure establishes model adequacy. Produce supported
measurements and limits rather than an invented significance or confidence interval.

The covariance expressions are exact linear propagation identities, not empirical
calibration prescriptions. Instrument-specific uncertainty terms need their sources.
