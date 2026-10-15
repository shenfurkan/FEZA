# Skills Suite Architecture & Scientific Assurance Summary

Updated 2026-10-15 — 100% Pure-Markdown Agent Skills Architecture

## 1. Architecture and Scope

FEZA is a **100% pure-Markdown Agent Skills repository** backed by locally downloaded
primary literature in `literature/`. Coding agents load FEZA from their client's
skill directory and write native, self-contained Astropy and
Astroquery code directly inside the user's project. There are no internal Python
library modules, build-package hybrids, or test-harness wrappers inside the skill.

## 2. Preserved Scientific & Numerical Invariants

The following intended scientific safeguards are documented as self-contained
**Python Reference Snippets & Pitfalls** under `skills/feza/references/`.
Their presence and syntax are not behavioral acceptance or scientific validation:

- **Two-part MJD split-time precision (`references/astropy-workflows.md`):**
  Preserves integer and fractional parts separately via
  `Time(mjdrefi, mjdreff, format="mjd", scale=timesys.lower())` without pre-summing
  into a single float, applies `TIMEZERO` and elapsed offsets via `TimeDelta`,
  checks `jd1`/`jd2` finiteness, and validates residuals in physical time units with
  `rtol=0`.
- **Per-sample $F_\lambda \to F_\nu$ conversion & uncertainty propagation (`references/astropy-workflows.md`):**
  Uses `u.spectral_density(wavelength)` per sample alongside the analytical check
  $\sigma_{F_\nu} = \sigma_{F_\lambda} \cdot (\lambda^2 / c)$, warning explicitly
  against scalar/mean-wavelength shortcuts, mask-dropping `Quantity` casts, and
  default `np.allclose` absolute-tolerance traps at astronomical flux scales.
- **Gaia 64-bit integer `source_id`, TAP status & covariance retention (`references/gaia.md`):**
  Validates local cone geometry and output staging before importing network-capable
  clients, inspects all VOTable `QUERY_STATUS` `INFO` entries (including trailing
  `OVERFLOW` or `ERROR` per IVOA DALI 1.1), preserves `source_id` as signed 64-bit
  integers (`int64`) via `use_names_over_ids=True` (never routing through `float64`),
  and retains the five-astrometric-parameter covariance with explicit units,
  exact source/solution identity, ICRS/TCB epoch metadata and a predeclared
  dimensionless correlation-validity criterion. This is not a full 6x6 solution.
- **HST/STIS first-order spectrum slicing & bitmask discipline (`references/stis.md`):**
  Verifies `INSTRUME == "STIS"`, enforces `SPORDER == 1`, slices spectral arrays to
  `[:nelem]` after checking `0 < nelem <= len(a)`, maps only the exact legacy
  `WAVELENGTH` token `"Angstroms"` to `u.AA` while preserving raw `TUNIT`, requires
  `FLUXCORR == "COMPLETE"` for physical-flux plotting, and filters serious quality
  flags via integer bitwise AND (`(dq & sdqflags) != 0`) while keeping missing
  `SDQFLAGS` fail-closed.
- **Stdlib AST context navigation (`references/stingy-context.md`):**
  Provides a self-contained Python 3.12+ `ast` and `tokenize` recipe for generating
  read-only, line-annotated `[Lines X-Y]` skeletons of unfamiliar large Python
  modules without external dependencies.

## 3. Source discipline belongs to development

The operator's local-original rule constrains writing and reviewing this skill;
it is not an installed-user download or storage requirement. The complete
development bibliography lives in [sources.md](sources.md), outside `skills/feza/`.
Operational recipes retain method definitions, units and limits without the
developer's local collection index or mandatory research-download workflow.

## 4. Current audit dispositions and acceptance gaps

Updated 2026-10-15. "Changed" means source/guidance changed, not runtime accepted.
Synthetic regressions were retained in `skills/feza/evals/regression-controls.md`
before repairing the scientific examples. No tests or numerical runs are authorized
on the current static-only workstation. No human risk acceptance is claimed.

| Finding | Disposition | Evidence still required |
|---|---|---|
| Publication-based class and missing-hazard exemption | Changed SKILL, standards and results template; intended-use/criticality/decision-owner record replaces the shortcuts | Human project determination; behavioral eval 10 |
| Gaia error units and mixed-scale covariance validity | Changed native Table/QTable recipe; retain unit/epoch basis, validate correlations before scaling, check finite outputs | Eval 9 against independent equivalent-unit, singular, invalid and malformed controls on an approved host |
| Initial TAP OVERFLOW rejected | Changed status gate to retain both valid overflow placements | Eval 14 native-parser cases; raw response and exact outcomes |
| Low-precision arithmetic | Changed spectral and linear-measurement examples to establish float64 before arithmetic | Eval 14 cancellation/spectral controls and the generated project's independent checks |
| Generic sigma acceptance example | Replaced with predeclared uncertainty/dependence/distribution/decision-risk fields | Use-specific criterion and independent reference evidence |
| Portable untrusted-content/secret boundary | Added explicit data-not-instructions and credential rules | Eval 12 with transport/secret-access monitoring; no demonstrated exploit or proven resistance |
| Developer literature rule imposed on users | Removed copied rule, collection index and local-path requirements from the package; corrected eval 11 and documentation | Unsupported coefficients still cannot be invented; no developer directory required |
| Non-path eval inputs and missing workflow controls | External inputs moved to explicit input_requirements; added synthetic development cases 9–14 and a navigation trigger | Native inputs for cases 1–8; held-out controls, fixed environments and exact comparison outcomes; no current pass |
| Client discovery ambiguity | Clarified Claude Code/Codex paths and invocation; no universal source-layout discovery claim | Actual installed-client discovery/invocation, not authorized or executed here |
| Source identity/provenance | Per operator direction, no checksum/hash/receipt bookkeeping: repository-only docs/sources.md keeps source identifiers and developer collection paths | Preserve unresolved source-status and extraction limits; no invented retrieval facts |
| Eval duplication and long-reference navigation | Skill-local JSON declared canonical; root mirrors retained; Gaia/STIS/AST contents lists added | Keep mirrors byte-identical and local links valid on edits |

The [verification record](verification.md) supersedes this earlier action list for
release status. Earlier 40/40 mechanical and 15/15 agent results are historical,
not acceptance of current edits. The operator declined behavior tests for the
current preparation pass; static checks do not close those behavioral gaps.
