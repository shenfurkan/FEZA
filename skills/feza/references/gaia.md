# Gaia catalogue retrieval and interpretation

## Python Reference Snippets & Pitfalls

Use native Astropy/Astroquery in the user's analysis. `center`, `radius`,
`response_path`, `staged_response_path`, `table` and `row_index` denote inspected
inputs and chosen destinations; the snippets are adaptable recipes, not executed
acceptance evidence.

## Contents

- [Declare the query](#declare-the-query)
- [Retain a native response](#recipe-a-declared-cone-to-a-retained-native-response)
- [Verify delivery and exact IDs](#verify-delivery-without-inventing-completeness)
- [Retain astrometric covariance and its basis](#preserve-native-meaning-and-full-astrometric-covariance)
- [Limits of quantitative use](#quantitative-use-is-a-separate-question)

Key invariants enforced in the snippets below:
- **64-bit integer `source_id` preservation:** Always preserve `source_id` (and
  `solution_id`) as signed 64-bit integers (`int64`) or exact strings—never route
  them through `float64` (which loses precision above $2^{53} = 9{,}007{,}199{,}254{,}740{,}992$).
- **TAP / VOTable `QUERY_STATUS` validation:** Inspect all `QUERY_STATUS` `INFO`
  elements—including trailing `INFO` elements after `TABLE` per IVOA DALI 1.1—to
  distinguish `OK` from `OVERFLOW` (truncated result) or `ERROR` before consumption.
- **Astrometric covariance retention:** Retain all five astrometric parameters'
  correlations, units and conventions. The recipe constructs their 5x5 covariance;
  it does not construct the full 6x6 solution including pseudocolour.

## Declare the query

Specify release/table, selected columns, sky geometry, coordinate frame, relevant
epoch and all cuts. Prefer explicit ADQL and established Astroquery/PyVO clients.
Inspect the query actually sent: a helper's `ROW_LIMIT` setting may silently
restrict the returned rows even when the service call succeeds. Record `MAXREC`,
pagination, job identity and final status. Use only the rows/columns necessary for
the task.
Express cones as `1 = CONTAINS(POINT, CIRCLE)`, not `DISTANCE(...) < r`. Before
using a field, check the
[DR3 known issues](https://www.cosmos.esa.int/web/gaia/dr3-known-issues): they are
table/field-specific (e.g. IPD statistics, NSS, synthetic photometry).

For Gaia DR3 `gaiadr3.gaia_source`, select source identity and the metadata needed by
the intended use, rather than silently expanding into a whole-catalogue query:

- Identity/release: `source_id`, `solution_id`, optionally `designation`.
- Coordinates/motion: `ra`, `dec`, `ref_epoch`, `parallax`, `pmra`, `pmdec` as needed.
- Uncertainty: the corresponding errors and pairwise correlations when consumed.
- Solution/quality: `astrometric_params_solved`, `ruwe` and task-relevant diagnostics.
- Bias prescription, if separately requested: its solution-specific colour inputs,
  magnitude, sky-coordinate convention and documented calibration domain.

No universal RUWE, magnitude, parallax-S/N or nearest-neighbour cut is prescribed.
Apply any scientific selection explicitly and explain its effect on the sample.

## Recipe: a declared cone to a retained native response

Input: an actual scalar `SkyCoord`, a scientifically selected angular radius, and
a new local response path. This example requests positions/parallaxes for inspection,
not inputs of a correction or full-covariance model. Change the explicit columns
when the scientific use needs them. Frame conversion does not propagate epoch.
Validate geometry and destination ownership before importing a network-capable
client. In Astroquery 0.4.11, the Gaia client exposes server-status notifications
(the `GaiaClass(..., show_server_messages=True)` option); a local input check must
not require importing the client. Perform any import only after network access is
authorized, inside the project's bounded network execution scope. An asynchronous
server job is not a client-side wall-clock bound.

```python
from pathlib import Path

import astropy.units as u
import numpy as np

if not center.isscalar or not getattr(radius, "isscalar", False):
    raise ValueError("A scalar SkyCoord center and an angular radius Quantity are required")
ra = center.icrs.ra.to_value(u.deg)
dec = center.icrs.dec.to_value(u.deg)
angular_radius = radius.to_value(u.deg)
if (not np.all(np.isfinite([ra, dec, angular_radius]))
        or not 0 < angular_radius <= 180):
    raise ValueError("Finite coordinates and a radius in (0, 180] degrees are required")
if Path(response_path).exists():
    raise FileExistsError(response_path)
query = f"""SELECT source_id, solution_id, ref_epoch, ra, dec,
                   parallax, parallax_error, astrometric_params_solved
            FROM gaiadr3.gaia_source
            WHERE 1 = CONTAINS(
                POINT('ICRS', ra, dec),
                CIRCLE('ICRS', {ra:.17g}, {dec:.17g}, {angular_radius:.17g}))
            ORDER BY source_id"""
```

The precheck above is not a concurrent output reservation. Download into a new
owned staging directory, not a shared final filename. Under the approved external
wall-clock watchdog (including import, submission, polling and download), the
native call is:

```python
from astroquery.gaia import Gaia

job = Gaia.launch_job_async(query, output_file=str(staged_response_path),
                            output_format="votable", dump_to_file=True)
```

This call can wait for completion. If its approved budget cannot cover the query,
use the client's documented background/job API with bounded polling rather than
an unbounded loop. Retain job identity so cancellation can abort only the owned
server job. A client timeout does not prove the server job stopped. Validate native
status/schema/IDs before no-clobber publication; timeout/error artifacts stay
explicitly incomplete. Do not lower catalog completeness to meet a deadline.

Retain the returned query, actual job identity/phase, retrieval time and native
response digest. Estimate row volume and use the service's asynchronous limits;
removing `TOP` is not authorization for an arbitrarily expensive all-sky query.
This uses explicit ADQL rather than a helper inserting a `ROW_LIMIT` restriction.

The client recipe follows the Astroquery 0.4.11 API; check the installed version
when adapting it.

## Verify delivery without inventing completeness

Retain the response/query and inspect VOTable status entries, including those after
the table. Under DALI, a trailing `OVERFLOW` or `ERROR` can qualify an earlier `OK`.
Some clients still return a table with an overflow warning; no exception does not
prove full delivery. Distinguish a `TOP`-restricted query from service truncation.

Check native ID uniqueness, row counts and requested schema. For a bounded task,
a separately expressed count/ID selection can cross-check the query; equal counts
alone do not establish equal sets. Same-service agreement is not an independent
survey or proof Gaia contains every astrophysical source.

Keep successful partial data usable and report the missing coverage. A denied,
expired, failed or incomplete query cannot demonstrate that a source is absent.

For the bounded, single-result VOTable above, inspect the native statuses from the
resource's collected `INFO` elements (the snippet reads `resource.infos`) before
claiming full delivery. The DALI form places the trailing `QUERY_STATUS` after the
table, so confirm on the installed Astropy version that the parser retained it.
For multiple resources, select the relevant result explicitly.

```python
from astropy.io.votable import parse

document = parse(response_path)
results = [resource for resource in document.resources if resource.type == "results"]
if len(results) != 1:
    raise ValueError("Select one declared results resource explicitly")
resource = results[0]
statuses = [info.value for info in resource.infos if info.name == "QUERY_STATUS"]
if not statuses or any(status not in {"OK", "OVERFLOW"} for status in statuses):
    raise ValueError(f"Missing, malformed or unsuccessful status: {statuses}")
if len(resource.tables) != 1:
    raise ValueError("Select one declared result table explicitly")
delivery_incomplete = "OVERFLOW" in statuses
table = resource.tables[0].to_table(use_names_over_ids=True)
```

This bounded-file parser includes trailing INFO and avoids a second full table
parse. Inspect the raw pre-/post-table status placement when strict DALI structural
conformance is required; the status list alone does not certify document order.
An initial `OVERFLOW` without a trailing INFO is also valid (local DALI 1.1
§4.4.1); retain it as partial delivery. Parsing a large VOTable can allocate its
table even when the goal is status inspection: admit memory or use a verified
streaming path, never truncate rows.

Validate the identity column before any conversion or export:

```python
ids = table["source_id"]
if ids.dtype.kind != "i" or ids.dtype.itemsize != np.dtype("int64").itemsize:
    raise TypeError("Gaia source_id must remain a signed 64-bit integer")
if np.any(np.ma.getmaskarray(ids)):
    raise ValueError("A Gaia source identity is missing")
native_ids = np.asarray(ids).copy()
if np.unique(native_ids).size != len(native_ids):
    raise ValueError("Duplicate source IDs require an explicit multiplicity policy")
```

Keep `solution_id` exact too. FITS big-endian `>i8` and native-endian int64 have
the same integer width; compare kind/itemsize, not `dtype == np.int64`. Never route
identifiers through float, including a dataframe/CSV intermediate: values above
`2**53` need not survive float64. Keep row order and masks; a one-to-many join
needs a declared multiplicity policy rather than silent deduplication.

If any status is `OVERFLOW`, retain the partial response and label delivery
incomplete; do not infer completeness merely from a final `OK`. An error response
remains retained evidence even when the example declines to use it. For an already
status-inspected file, direct reading also works with
`Table.read(response_path, format="votable", use_names_over_ids=True)`. VOTable
FIELD IDs need not equal column names, so check the readback schema either way.
Check integer `source_id` dtype/uniqueness and compare any separate query's native
ID sets; use the
[Astropy export recipe](astropy-workflows.md#2-preserve-cataloguetable-semantics-when-exporting)
to preserve masks/units in a derivative. No distance is inferred by these steps.

## Preserve native meaning and full astrometric covariance

- Keep long IDs as exact integers/strings and qualify them by release. IDs are not
  guaranteed stable across releases; an association is not established identity.
- DR3 coordinates are ICRS. `ref_epoch` is a TCB Julian Year, not an unspecified year.
  Preserve native precision; perform propagation only for the requested use with
  the required motion/epoch/frame inputs and uncertainty treatment.
- `pmra` is the RA proper-motion component including `cos(dec)`; `ra_error` uses
  the corresponding tangent-plane convention. Do not multiply/divide by it twice.
- Error columns are marginal standard uncertainties; correlation columns are
  dimensionless. Construct and retain the full astrometric covariance matrix with
  compatible units/conventions and valid entries rather than discarding off-diagonal
  terms. Per-source formal correlations do not encode cross-source angular
  systematics or all auxiliary pseudocolour correlations.
- Preserve negative parallaxes and masks. Do not replace missing astrometry with
  zero, invert every parallax into a distance, or filter rows merely to simplify export.

For a declared row index `row_index` in a bounded native `table` (Table or QTable),
retain the five-astrometric-parameter submatrix for solution types 31 or 95. The
source must be identified as Gaia DR3 before applying these conventions. For type
95 this is **not** the full six-parameter solution: quantitative use of pseudocolour
needs its additional covariance terms, not invented zero correlations.

Supply a finite, nonnegative dimensionless `correlation_atol`, justified **before**
inspection from stored-correlation precision and the numerical error budget for the
dimensionless eigensolve. There is no universal tolerance supplied here. Keep the
original eigenvalues; never clip them or scale this criterion by mixed-unit errors.
If the criterion cannot support the intended precision, leave validity unresolved.

```python
import astropy.units as u
import numpy as np
from astropy.table import QTable
from astropy.time import Time

astrometry = QTable(table, copy=False)
row = astrometry[row_index]
parameters = ("ra_cosdec", "dec", "parallax", "pmra", "pmdec")
parameter_units = (u.mas, u.mas, u.mas, u.mas / u.yr, u.mas / u.yr)
err_cols = ("ra_error", "dec_error", "parallax_error", "pmra_error", "pmdec_error")
corr_pairs = (
    (0, 1, "ra_dec_corr"),
    (0, 2, "ra_parallax_corr"),
    (0, 3, "ra_pmra_corr"),
    (0, 4, "ra_pmdec_corr"),
    (1, 2, "dec_parallax_corr"),
    (1, 3, "dec_pmra_corr"),
    (1, 4, "dec_pmdec_corr"),
    (2, 3, "parallax_pmra_corr"),
    (2, 4, "parallax_pmdec_corr"),
    (3, 4, "pmra_pmdec_corr"),
)
required = err_cols + tuple(c for _, _, c in corr_pairs) + (
    "source_id", "solution_id", "ref_epoch", "astrometric_params_solved",
)
if any(astrometry[col].ndim != 1 or astrometry[col].dtype.kind not in "fiu"
       for col in required):
    raise TypeError("Real numeric scalar astrometric columns are required")
if any(np.any(getattr(row[col], "mask", False)) for col in required):
    raise ValueError("Required astrometric entry is masked")
for col in ("source_id", "solution_id"):
    if astrometry[col].dtype.kind != "i" or astrometry[col].dtype.itemsize != 8:
        raise TypeError(f"{col} must remain a signed 64-bit integer")
if (astrometry["astrometric_params_solved"].dtype.kind not in "iu"
        or row["astrometric_params_solved"] not in {31, 95}):
    raise ValueError("A five- or six-parameter astrometric solution is required")
if any(getattr(astrometry[col], "unit", None) is None
       for col in err_cols + ("ref_epoch",)):
    raise u.UnitConversionError("Missing astrometric error/epoch unit")
if (not np.isscalar(correlation_atol) or not np.isfinite(correlation_atol)
        or correlation_atol < 0):
    raise ValueError("A justified nonnegative scalar correlation tolerance is required")
with np.errstate(over="raise", divide="raise", invalid="raise", under="raise"):
    sigma = np.array([row[col].astype(np.float64).to_value(unit)
                      for col, unit in zip(err_cols, parameter_units, strict=True)],
                     dtype=np.float64)
    epoch_year = row["ref_epoch"].astype(np.float64).to_value(u.yr)
if not np.isfinite(epoch_year):
    raise ValueError("Reference epoch must be finite")
reference_epoch = Time(epoch_year, format="jyear", scale="tcb")
if not np.all(np.isfinite(sigma)) or np.any(sigma <= 0):
    raise ValueError("Astrometric standard uncertainties must be finite and positive")
corr = np.eye(5, dtype=np.float64)
for i, j, col in corr_pairs:
    rho = u.Quantity(row[col], dtype=np.float64).to_value(u.one)
    if not np.isfinite(rho) or not -1.0 <= rho <= 1.0:
        raise ValueError(f"Invalid correlation {col}={rho}")
    corr[i, j] = corr[j, i] = rho
eigvals = np.linalg.eigvalsh(corr)
if not np.all(np.isfinite(eigvals)) or eigvals[0] < -correlation_atol:
    raise ValueError("Astrometric correlation matrix fails the declared PSD criterion")
with np.errstate(over="raise", divide="raise", invalid="raise", under="raise"):
    cov_astrom = np.outer(sigma, sigma) * corr
if not np.all(np.isfinite(cov_astrom)):
    raise ValueError("Nonfinite reconstructed covariance")
astrometric_covariance = {
    "matrix": cov_astrom,
    "parameters": parameters,
    "parameter_units": parameter_units,
    "release": "Gaia DR3",
    "source_id": row["source_id"],
    "solution_id": row["solution_id"],
    "astrometric_params_solved": row["astrometric_params_solved"],
    "frame": "ICRS",
    "reference_epoch": reference_epoch,
    "ra_convention": "tangent-plane cos(dec) factor already included",
    "correlation_eigenvalues": eigvals,
    "correlation_atol": correlation_atol,
}
```

Matrix element `(i,j)` has unit `parameter_units[i] * parameter_units[j]`; do not
pass the bare numeric matrix downstream without this basis record. A negative
eigenvalue within the declared tolerance remains recorded numerical uncertainty,
not a repaired eigenvalue or evidence of model adequacy. Preserve legitimate
singular solutions.

These column meanings are specific to the Gaia DR3 `gaia_source` data model:
`ref_epoch`, `ra_error` through `pmdec_error`, the ten `*_corr` fields and
`astrometric_params_solved`. Covariance scaling is the definition of correlation;
its numerical validity criterion is an explicit analysis choice, not a Gaia cut.

Use metadata-preserving formats such as VOTable/FITS/ECSV when exporting. Check
IDs, dtypes, masks, units and sequence after readback; a plain CSV may lose semantics.

## Quantitative use is a separate question

EDR3/DR3 five- and six-parameter astrometric solutions have different colour handling;
the sixth astrometric parameter is pseudocolour, not radial velocity. The Lindegren
bias prescriptions require effective wavenumber or pseudocolour, not a guessed colour.
A nonselected input is not proof the archive lacks a measurement. The separate
six-parameter G-band photometric correction is already applied in DR3; check release
history before applying an EDR3 correction again.

An empirical isolated-source uncertainty prescription is conditional on its sample,
quality/isolation, prior bias correction and calibration assumptions. Shared local
systematics may cancel in binary comparisons. RUWE alone is neither a general error
scale nor a single-star guarantee. No correction/inflation recipe is supplied here.

Parent-catalogue inclusion and the selection of a parallax/quality/RVS subset differ.
Cantat-Gaudin et al.'s parent model concerns entries with published position and G;
it cannot automatically qualify an arbitrary subset or missing-G entries.

Deliver the retained table, exact query, status/completeness basis and a short
interpretation note.
