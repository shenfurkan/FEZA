# FEZA development sources and local literature index

These primary papers, standards and official documents were used while writing
and reviewing FEZA. This development bibliography stays outside `skills/feza/`;
it is not part of the skill instructions or automatically loaded. Local paths are
relative to the repository root and identify the developer's git-ignored
collection, not files a user needs to download or install. Source names, versions
and locators support review; they are not scientific validation or an installation
manifest.

## Contents

- [Astropy API basis](#astropy-analysis-recipes)
- [Literature and formats](#literature-and-representation)
- [Gaia](#gaia)
- [STIS and FITS](#stis-and-fits)
- [NASA and context navigation](#nasa-standards-and-context-navigation)
- [Publication](#publication)
- [Agent Skills and client integration](#agent-skills-and-client-integration)
- [Skeleton design basis](#skeleton-design-basis)
- [Six Locks](#six-locks)
- [License boundary](#license-boundary)

## Astropy analysis recipes

The original examples in [Astropy workflows](../skills/feza/references/astropy-workflows.md) use the official
documentation displayed as **Astropy 8.0.1**. The versioned URLs and local copies
below record the inspected API basis; when adapting these recipes, use the
documentation for the scientist's installed environment.

| Operation in FEZA | Official source / inspected API basis | Local `literature/` path |
|---|---|---|
| FITS inventory/read-only access | [FITS reading and large-file notes](https://docs.astropy.org/en/v8.0.1/io/fits/index.html) | `literature/astropy_v8.0.1_fits.html` |
| Distinguish missing/failed checksums | [HDU verify_checksum / verify_datasum](https://docs.astropy.org/en/v8.0.1/io/fits/api/hdus.html): return 0 failure, 1 match, 2 absent | `literature/astropy_v8.0.1_hdus.html` |
| Explicit table-HDU selection and FITS nulls | [Unified FITS table I/O](https://docs.astropy.org/en/v8.0.1/io/unified_table_fits.html) | `literature/astropy_v8.0.1_unified_table_fits.html` |
| Preserve data under masks and numeric metadata | [ECSV data plus mask](https://docs.astropy.org/en/v8.0.1/io/ascii/ecsv.html#data-mask) | `literature/astropy_v8.0.1_ecsv.html` |
| F_lambda/F_nu conversion at sample wavelength | [Spectral flux-density equivalency](https://docs.astropy.org/en/v8.0.1/units/equivalencies.html#spectral-flux-and-luminosity-density-units) | `literature/astropy_v8.0.1_equivalencies.html` |
| Split time reference / scale versus arrival correction | [Time, val2, scales and light travel time](https://docs.astropy.org/en/v8.0.1/time/index.html) | `literature/astropy_v8.0.1_time.html` |
| All positional association candidates | [Catalogue matching and search_around_sky](https://docs.astropy.org/en/v8.0.1/coordinates/matchsep.html) | `literature/astropy_v8.0.1_matchsep.html` |
| Image pixel/world coordinates | [Shared WCS interface](https://docs.astropy.org/en/v8.0.1/wcs/wcsapi.html) and [pixel/array conventions](https://docs.astropy.org/en/v8.0.1/api/astropy.wcs.wcsapi.BaseLowLevelWCS.html) | `literature/astropy_v8.0.1_wcsapi.html`, `literature/astropy_v8.0.1_base_low_level_wcs.html` |
| WCS object construction (`fobj`, `has_celestial`) | [WCS class reference](https://docs.astropy.org/en/v8.0.1/api/astropy.wcs.WCS.html) | `literature/astropy_v8.0.1_wcs_class.html` |
| Unit-string parsing incl. `format="fits"` | [String representations of units and quantities](https://docs.astropy.org/en/v8.0.1/units/format.html) | `literature/astropy_v8.0.1_units_format.html` |
| Masked/`Quantity` semantics (`Masked`, masks in tables) | [Masked values and quantities](https://docs.astropy.org/en/v8.0.1/utils/masked/index.html) | `literature/astropy_v8.0.1_utils_masked.html` |
| VOTable document reading (`parse`, `resources`) | [VOTable handling](https://docs.astropy.org/en/v8.0.1/io/votable/index.html) | `literature/astropy_v8.0.1_votable.html` |

NumPy API basis: the `np.allclose` defaults (`rtol=1e-5`, `atol=1e-8`) used in the
time and measurement checks ([numpy.allclose](https://numpy.org/doc/stable/reference/generated/numpy.allclose.html),
`literature/numpy_allclose.html`, displayed NumPy 2.5).

Exact linear covariance propagation is a mathematical identity, not a fitted
empirical relation. Instrument calibration, background and model uncertainty remain
specific scientific inputs; these API citations cannot supply them.

## Literature and representation

- [NASA ADS Developer API](https://github.com/adsabs/adsabs-dev-api)
  (`literature/ads_dev_api_readme.md`): bibliographic identity, search and source
  discovery; a metadata match is not equation verification.
- [arXiv reuse](https://info.arxiv.org/help/license/reuse.html)
  (`literature/arxiv_license_reuse.html`): rights are tied to the actual
  source/version, not inferred from public metadata access.
- [DALI 1.1](https://www.ivoa.net/documents/DALI/20170517/REC-DALI-1.1.html),
  §§3.4.4/4.4 (`literature/ivoa_dali_1.1.pdf`, `literature/ivoa_dali_1.1.html`):
  service limits and result status, including trailing status entries.
- [VOTable 1.5](https://www.ivoa.net/documents/VOTable/20250116/REC-VOTable-1.5.html)
  (`literature/ivoa_votable_1.5.pdf`, `literature/ivoa_votable_1.5.tex`,
  `literature/ivoa_votable_1.5.html`): table metadata, arrays, coordinates/time
  representations and serialization.
- [Astropy time guide](https://docs.astropy.org/en/stable/time/index.html)
  (`literature/astropy_v8.0.1_time.html`): format, scale, precision, missing values
  and light-travel-time treatment.
- Gordon et al. (2023), *One Relation for All Wavelengths*, ApJ 950, 86:
  [DOI 10.3847/1538-4357/accb59](https://doi.org/10.3847/1538-4357/accb59),
  ADS `2023ApJ...950...86G` (`literature/gordon_2023_extinction_2304.01991v2.pdf`,
  TeX archive `literature/gordon_2023_extinction_2304.01991v2_source.tar.gz`).
- Gordon et al. (2025), erratum, ApJ 992, 217:
  [DOI 10.3847/1538-4357/ae0cca](https://doi.org/10.3847/1538-4357/ae0cca),
  ADS `2025ApJ...992..217G` (`literature/gordon_2025_extinction_erratum_apj_992_217.pdf`).
- [dust_extinction normalization details](https://dust-extinction.readthedocs.io/en/stable/dust_extinction/normalization_details.html)
  (`literature/dust_extinction_normalization_details.rst.txt`) and
  [G23 API](https://dust-extinction.readthedocs.io/en/stable/api/dust_extinction.parameter_averages.G23.html)
  (`literature/dust_extinction_g23_api.html`): software normalization/variant
  context, not independent observational calibration.

## Gaia

- [Gaia DR3 gaia_source data model](https://gea.esac.esa.int/archive/documentation/GDR3/Gaia_archive/chap_datamodel/sec_dm_main_source_catalogue/ssec_dm_gaia_source.html)
  (`literature/gaia_dr3_gaia_source_datamodel.html`): identifiers, units, epoch,
  proper-motion/error conventions and solution fields.
- [Gaia DR3 known issues](https://www.cosmos.esa.int/web/gaia/dr3-known-issues)
  (`literature/gaia_dr3_known_issues.html`): table- and field-specific caveats.
- [Astroquery Gaia](https://astroquery.readthedocs.io/en/stable/gaia/gaia.html)
  (`literature/astroquery_gaia.html`, `literature/astroquery_gaia_class.html`):
  TAP queries, helpers and ROW_LIMIT behavior.
- [PyVO query implementation](https://pyvo.readthedocs.io/en/stable/_modules/pyvo/dal/query.html)
  (`literature/pyvo_dal_query.html`): client status/error/overflow handling; inspect
  the installed version.
- [ESA EDR3 code/applicability page](https://www.cosmos.esa.int/web/gaia/edr3-code)
  (`literature/gaia_edr3_code.html`): tentative parallax recipe and the distinction
  from DR3's already-applied G correction.
- Lindegren et al. (2021), *The astrometric solution*, A&A 649, A2:
  [DOI 10.1051/0004-6361/202039709](https://doi.org/10.1051/0004-6361/202039709),
  ADS `2021A&A...649A...2L`; arXiv `2012.03380v1`
  (`literature/lindegren_2021_gaia_edr3_astrometry_2012.03380v1.pdf`).
  Relevant locators: [§2.3, five/six-parameter colour handling](https://arxiv.org/html/2012.03380v1#S2.SS3),
  [§5.3, fit statistics](https://arxiv.org/html/2012.03380v1#S5.SS3), and
  [§5.6, angular systematics](https://arxiv.org/html/2012.03380v1#S5.SS6).
- Lindegren et al. (2021), *Parallax bias versus magnitude, colour, and position*,
  A&A 649, A4: [DOI 10.1051/0004-6361/202039653](https://doi.org/10.1051/0004-6361/202039653),
  ADS `2021A&A...649A...4L`; arXiv `2012.01742v2`
  (`literature/lindegren_2021_gaia_edr3_parallax_bias_2012.01742v2.pdf`).
  Relevant locators: [§2.2, recipe variables](https://arxiv.org/html/2012.01742v2#S2.SS2)
  and [§8, limitations and use](https://arxiv.org/html/2012.01742v2#S8).
- El-Badry, Rix & Heintz (2021), *A million binaries from Gaia eDR3*, MNRAS 506, 2269:
  [DOI 10.1093/mnras/stab323](https://doi.org/10.1093/mnras/stab323),
  ADS `2021MNRAS.506.2269E`; arXiv `2101.05282v3`
  (`literature/el_badry_2021_gaia_edr3_binaries_2101.05282v3.pdf`).
  Relevant locators: [§5.4, conditional calibration](https://arxiv.org/html/2101.05282v3#S5.SS4)
  and [§5.5, shared angular systematics](https://arxiv.org/html/2101.05282v3#S5.SS5).
- Cantat-Gaudin et al. (2023), *An empirical model of the Gaia DR3 selection function*,
  A&A 669, A55: [DOI 10.1051/0004-6361/202244784](https://doi.org/10.1051/0004-6361/202244784),
  ADS `2023A&A...669A..55C`; arXiv `2208.09335v2`
  (`literature/cantat_gaudin_2023_gaia_dr3_selection_2208.09335v2.pdf`).
  Relevant locator: [§4.4, parent catalogue versus selected subsets](https://arxiv.org/html/2208.09335v2#S4.SS4).

## STIS and FITS

- [MAST observation/product queries](https://astroquery.readthedocs.io/en/stable/mast/mast_obsquery.html)
  (`literature/astroquery_mast_obsquery.html`): observation/group identifiers,
  product selection and individual downloads.
- [STIS Data Handbook: extracted spectra](https://hst-docs.stsci.edu/stisdhb/chapter-5-stis-data-analysis/5-5-working-with-extracted-spectra),
  especially §5.5.1/Table 5.2 (`literature/stsci_stis_data_handbook_v8.0.pdf`,
  `literature/stsci_stis_data_handbook_v7.0.pdf`): array-valued products, units and
  flux-calibration meaning.
- [Official poisson_err utility](https://stistools.readthedocs.io/en/latest/poisson_err.html)
  (`literature/stistools_poisson_err.html`): MAMA/count-input applicability; an
  official utility is not a complete likelihood or proof the user's observation
  satisfies its assumptions.
- [FITS Standard 4.0](https://fits.gsfc.nasa.gov/fits_standard.html)
  (`literature/fits_standard_4.0.pdf`, `literature/fits_standard_4.0.tex`): format
  authority, distinct from scientific calibration and authenticity.

## NASA standards and context navigation

- [NPR 7150.2D](https://nodis3.gsfc.nasa.gov/npg_img/N_PR_7150_002D_/N_PR_7150_002D_.pdf)
  (`literature/nasa_npr_7150_2d.pdf`), plus LaRC RMM templates for Class D
  (`literature/nasa_larc_rmm_class_d.pdf`) and Class E
  (`literature/nasa_larc_rmm_class_e.pdf`).
- [NASA-STD-8739.8B](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf)
  (`literature/nasa_std_8739_8b.pdf`).
- [NASA-STD-7009B](https://standards.nasa.gov/sites/default/files/standards/NASA/B/1/NASA-STD-7009B-Final-3-5-2024.pdf)
  (`literature/nasa_std_7009b.pdf`) and [NASA-HDBK-7009B](https://standards.nasa.gov/system/files/tmp/NASA-HDBK-7009B_Final%2002-03-2026.pdf)
  (`literature/nasa_hdbk_7009b.pdf`; the saved copy's page headers read "DRAFT"
  while its cover states approved 2026-02-03).
- [NASA-HDBK-2203 / SWEHB](https://swehb.nasa.gov)
  (`literature/nasa_swehb_selected_requirements.txt`; the saved
  `literature/nasa_hdbk_2203.pdf` is a site landing-page stub, not the handbook).
- [SPD-41a](https://science.nasa.gov/wp-content/uploads/2023/08/smd-information-policy-spd-41a.pdf)
  (`literature/nasa_spd_41a.pdf`), [SMD Open-Source Science Guidance v2.2](https://assets.science.nasa.gov/content/dam/science/cds/open-science/SMD%20Open-Source%20Science%20Guidance%20v2.2%2020250205.pdf)
  (`literature/nasa_smd_oss_guidance_v2.2.pdf`), [APD Policy-13 v1.8](https://science.nasa.gov/wp-content/uploads/2023/05/APD_Data_Policy_v1.8.pdf)
  (`literature/nasa_apd_policy_13_v1.8.pdf`), and NPR 2210.1E
  (`literature/nasa_npr_2210_1e.pdf`).
- Ostby (2026), *Stingy Context: 18:1 Hierarchical Code Compression for LLM Auto-Coding*,
  [arXiv:2601.19929v2](https://arxiv.org/abs/2601.19929v2) (revision date from the
  saved listing, `literature/ostby_arxiv_2601.19929_listing.html`); saved paper:
  `literature/ostby_2026_stingy_context_2601.19929v2.pdf`.
- [Python 3.12 `ast`](https://docs.python.org/3.12/library/ast.html)
  (`literature/python_3.12_ast.html`).
- [Python 3.12 `tokenize`](https://docs.python.org/3.12/library/tokenize.html)
  (`literature/python_3.12_tokenize.html`), especially `open`/`detect_encoding`.

## Publication

- [AAS manuscript AI/LLM guidance](https://journals.aas.org/author-llm-guidelines/)
  (`literature/aas_author_llm_guidelines.html`).
- [AAS Data Guide](https://journals.aas.org/data-guide/)
  (`literature/aas_data_guide.html`).
- [AAS software citation policy](https://journals.aas.org/policy-statement-on-software/)
  (`literature/aas_software_policy.html`).

## Agent Skills and client integration

- [Agent Skills specification](https://agentskills.io/specification)
  (`literature/agent_skills_specification_20261015.md`): portable frontmatter,
  directory layout, on-demand resources and relative links. `skills-ref` checks
  frontmatter/naming, not behavioral correctness or production certification.
- [Agent Skills creator best practices](https://agentskills.io/skill-creation/best-practices)
  (`literature/agent_skills_best_practices_20261016.md`): task-scoped instructions,
  progressive disclosure and procedures rather than unsupported quality claims.
- [Claude Code skills](https://code.claude.com/docs/en/skills)
  (`literature/claude_code_skills_20261015.md`): project/personal locations,
  symlink discovery, invocation, account uploads and live skill changes.
- Claude Code [marketplace creation](https://code.claude.com/docs/en/plugins/create-marketplace),
  [marketplace reference](https://code.claude.com/docs/en/plugins/marketplace-reference),
  [plugin manifest reference](https://code.claude.com/docs/en/plugins/manifest-reference)
  and [plugin installation](https://code.claude.com/docs/en/plugins/install)
  (`literature/claude_code_plugin_marketplaces_20261015.md`,
  `literature/claude_code_plugin_marketplace_reference_20261015.md`,
  `literature/claude_code_plugin_manifest_20261015.md`,
  `literature/claude_code_plugin_install_20261015.md`): native marketplace/plugin
  packaging, namespaces, scope and update commands. Both FEZA JSON manifests passed
  the installed CLI's local validation (Claude Code 2.1.300); no plugin was installed.
- OpenCode **V2** [Skills](https://opencode.ai/v2/docs/skills/),
  [Config](https://opencode.ai/v2/docs/config/),
  [Permissions](https://opencode.ai/v2/docs/permissions/),
  [CLI commands](https://opencode.ai/v2/docs/cli/commands/) and
  [Plugin overview](https://opencode.ai/v2/docs/build/plugins/)
  (`literature/opencode_v2_skills_20261016.md`,
  `literature/opencode_v2_config_20261016.md`,
  `literature/opencode_v2_permissions_20261016.md`,
  `literature/opencode_v2_cli_commands_20261016.md`,
  `literature/opencode_v2_plugin_guide_20261016.md`): native discovery,
  path-derived skill IDs, `@feza`, the `skills` array, permission scope and reload.
  The documented runtime plugin API is distinct from the Markdown skill format;
  FEZA needs no OpenCode executable plugin. Only V2 docs were used for these
  instructions; V1 config shapes were not inferred from the editor schema URL.
- [Vercel Labs skills 1.7.2](https://github.com/vercel-labs/skills/blob/v1.7.2/README.md),
  [npm metadata](https://registry.npmjs.org/skills/1.7.2) and
  [Codex skills](https://developers.openai.com/codex/build-skills) are the documented
  installation references (`literature/vercel_skills_v1.7.2_readme.md`,
  `literature/vercel_skills_v1.7.2_metadata.json`,
  `literature/codex_build_skills_20261015.md`). No installer/client session was
  executed for this revision; `INSTALLATION.md` keeps that limitation explicit.
- [GitHub: Manually running a workflow](https://docs.github.com/en/actions/using-workflows/manually-running-a-workflow)
  (`literature/github_manual_workflows_20261016.html`) and
  [actions/checkout v7.0.1 inputs](https://github.com/actions/checkout/blob/v7.0.1/action.yml)
  (`literature/github_checkout_v7.0.1_action.yml`): manual workflow dispatch and
  checkout without persisted credentials. The workflow is prepared, not launched.

## Skeleton design basis

The implementation in `skills/feza/references/stingy-context.md` is original
standard-library Python, not code copied from TREEFRAG. Its direct API basis is
the saved Python `ast` documentation above: source positions, syntax nodes,
`parse`, `unparse`, `copy_location` and `iter_fields`; `tokenize.open` respects the
input encoding declaration. Maps are never imported, executed or written over
their source.

FEZA adds exact qualified-symbol focus, tokenizer-based decorator start lines,
literal-newline handling, collision detection and an annotated-map/pruned-AST
comparison. These are deterministic source-level checks, not proof of behavior,
calibration or measured context savings. Focus intentionally omits enclosing
namespace/branch context, which must be read from the original source as needed.

Ostby's arXiv v2 listing dates the revision to 2026-02-04. The PDF itself is titled
"v5" and dated December 2025; it has no arXiv stamp. These different version
labels are retained, not silently reconciled. Section 5 describes hierarchical
metadata and excludes the decomposition process; section 6 covers serialization.
The paper supplies neither this AST algorithm nor independent evidence for it.

Table 7's 18:1–24:1 model-token ratios concern names-only trees of one application;
section 8's 94.5–97.3% scores concern model-consensus issue localization, not
executed patch correctness. Table 4 compares ASCII/CSV/JSON serialization.
Appendix D withholds full source/tree dumps and Appendix F asserts pending
patents. None is a FEZA compression guarantee, benchmark or patent-clearance
opinion. FEZA retains richer code contracts; actual context/quality gains remain
unmeasured. Python lexical tokens or byte counts are not model-token counts.

## Six Locks

The operator excluded Moving-Block Bootstrap during this task, leaving five new
engineering skills. The section's requested historical name is retained. See the
[scope and common doctrine](six-locks-boundary.md) and the
[download receipts, claim map, blockers and acceptance record](six-locks-provenance.md).
These source inputs remain Git-ignored; every installed skill contains its own
portable bibliography/contract and needs no developer collection or repository root.

The table indexes **every** acquired response, including denied/missing pages,
the excluded bootstrap paper and the subscription preview. Only the explicitly
selected passages in the evidence map support the five skills. Local access does
not change the source's copyright/licence. Downloaded Java/YAML was inspected as
source data and never executed, compiled, installed or distributed as software.

| ID | Local file | Full requested URL | Use/status |
|---|---|---|---|
| Q1 | `literature/six-locks/golangcilint_faq_20261025.html` | https://golangci-lint.run/docs/welcome/faq/ | First-party ratchet-related capability and CI exit handling |
| Q2 | `literature/six-locks/mypybaseline_usage_20261025.html` | https://mypy-baseline.orsinium.dev/usage.html | BLOCKED, retained 403 body |
| M0 | `literature/six-locks/kunsch_1989_stationary-bootstrap-access.html` | https://projecteuclid.org/journals/annals-of-statistics/volume-17/issue-3/The-Jackknife-and-the-Bootstrap-for-General-Stationary-Observations/10.1214/aos/1176347265.full | Challenge body, not article; bootstrap EXCLUDED |
| M1 | `literature/six-locks/politis_2004_automatic-block-length.pdf` | https://public.econ.duke.edu/~ap172/Politis_White_2004.pdf | Acquired before scope correction; EXCLUDED/unread |
| A1 | `literature/six-locks/bazel_remote-caching_20261025.html` | https://bazel.build/remote/caching | Action cache/CAS, not source-AST hashing |
| A2 | `literature/six-locks/nix_derivations_20261025.html` | https://nix.dev/manual/nix/2.24/store/derivation/ | BLOCKED, retained 404 page |
| A3 | `literature/six-locks/unison_big-idea_20261025.html` | https://www.unison-lang.org/docs/the-big-idea/ | Direct syntax-tree-addressed code example |
| Q2b | `literature/six-locks/mypybaseline_readme_20261025.md` | https://raw.githubusercontent.com/orsinium-labs/mypy-baseline/master/README.md | Upstream baseline synchronization/filtering |
| Q3 | `literature/six-locks/golangcilintaction_workflow_20261025.yml` | https://raw.githubusercontent.com/golangci/golangci-lint-action/master/.github/workflows/test.yml | Concrete new-only workflow with success-on-issues setting; not enforcing evidence |
| A2b | `literature/six-locks/nix_derivations-v2.34_20261025.html` | https://nix.dev/manual/nix/2.34/store/derivation/ | Canonical derivation/store-object representation, version 2.34 |
| S1 | `literature/six-locks/fowler_strangler-fig_20261025.html` | https://martinfowler.com/bliki/StranglerFigApplication.html | Later author revision dated 2024-08-22; discovery context only |
| S2 | `literature/six-locks/fowler_branch-abstraction_20261025.html` | https://martinfowler.com/bliki/BranchByAbstraction.html | Historical/descriptive author essay dated 2014-01-07 |
| E1 | `literature/six-locks/klein_2005_blind-analysis.pdf` | https://slac.stanford.edu/pubs/slacpubs/12000/slac-pub-12051.pdf | SLAC-PUB-12051 author manuscript, not inspected journal version |
| E3 | `literature/six-locks/fda_2022_multiple-endpoints.pdf` | https://www.fda.gov/media/162416/download | October 2022 final nonbinding guidance; clinical scope only |
| F1 | `literature/six-locks/nygard_2007_release-it-preview.pdf` | https://media.pragprog.com/titles/mnee/mnee-antipatterns.pdf | Publisher excerpt, 2007 copyright / 2009 printing; full book unexamined |
| E2a | `literature/six-locks/chambers_2022_registered-reports-access.html` | https://www.nature.com/articles/s41562-021-01193-7 | Subscription preview, abstract/metadata only; not method evidence |
| E2 | `literature/six-locks/plos_registered-reports_20261025.pdf` | https://plos-marketing.s3.amazonaws.com/Marketing/Biology+Preregistered+Articles+Guidelines+for+Authors.pdf | Official PLOS Biology policy updated 2020-01-28 |
| S3 | `literature/six-locks/microsoft_strangler-fig_20261025.html` | https://learn.microsoft.com/en-us/azure/architecture/patterns/strangler-fig | Official architecture guidance, updated 2026-06-02 |
| F2a | `literature/six-locks/resilience4j_circuitbreaker-v2.3.0_20261025.java` | https://raw.githubusercontent.com/resilience4j/resilience4j/v2.3.0/resilience4j-circuitbreaker/src/main/java/io/github/resilience4j/circuitbreaker/CircuitBreaker.java | First-party v2.3.0 API/state/permission documentation; static only |
| F2b | `literature/six-locks/resilience4j_config-v2.3.0_20261025.java` | https://raw.githubusercontent.com/resilience4j/resilience4j/v2.3.0/resilience4j-circuitbreaker/src/main/java/io/github/resilience4j/circuitbreaker/CircuitBreakerConfig.java | First-party v2.3.0 configuration/API documentation; static only |
| E3a | `literature/six-locks/fda_multiple-endpoints-status_20261025.html` | https://www.fda.gov/regulatory-information/search-fda-guidance-documents/multiple-endpoints-clinical-trials | Official status metadata for E3, Final; content current 2024-04-16 |
| S1o | `literature/six-locks/fowler_2004_original-strangler-fig.html` | https://martinfowler.com/bliki/OriginalStranglerFigApplication.html | Original 2004-06-29 author post, explicitly superseded; historical citation only |

## License boundary

MIT covers FEZA's original skill, summaries and template. It does not relicense the
linked papers, observations, software or mission documentation. Local copies under
`literature/` are retained for local primary-source verification under their own
respective terms.
