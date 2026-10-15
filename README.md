# FEZA

**Framework for Extraterrestrial & Zenith-grade Astrophysics**

Version 0.0.1 · [MIT license](LICENSE.txt)

FEZA is an astronomy Agent Skill for **OpenCode, Claude Code and Codex**. It brings
together **native Astropy/Astroquery workflows**, **NASA-informed software
engineering and assurance practices**, and **AST-based Python navigation designed
to reduce unnecessary LLM context usage**. Its Markdown instructions and Python
recipes guide the assistant's work directly in the user's research project.

FEZA is not a Python package or a data-reduction pipeline. There is no `import feza`
or FEZA command-line program. Installing the skill makes its instructions available
to the assistant; it does not install scientific libraries or run an analysis.

## Contents

- [Why FEZA exists](#why-feza-exists)
- [NASA-informed engineering and assurance](#nasa-informed-engineering-and-assurance)
- [Context reduction without discarding evidence](#context-reduction-without-discarding-evidence)
- [Scope](#scope)
- [Requirements](#requirements)
- [Installation](#installation)
  - [Claude Code plugin](#claude-code-plugin)
  - [OpenCode V2](#opencode-v2)
- [Usage](#usage)
- [Python source navigation](#python-source-navigation)
- [Sources used during development](#sources-used-during-development)
- [Repository structure](#repository-structure)
- [Verification and limitations](#verification-and-limitations)
- [Contributing](#contributing)
- [License](#license)

## Why FEZA exists

FEZA's purpose is to help researchers use coding assistants for astronomy without
losing the scientific meaning of their data or filling the context window with
irrelevant implementation details. The goal is not just code that runs or a plot
that looks plausible, but an inspectable path from inputs and documented methods
to outputs whose assumptions, uncertainty and verification status are clear.

The skill turns that goal into working instructions:

- **Reuse established astronomy tools.** Write native Astropy/Astroquery code in
  the research project rather than introducing an opaque FEZA API or reimplementing
  an applicable instrument pipeline.
- **Preserve scientific meaning.** Carry units, masks, exact source identifiers,
  time scales, coordinate frames and calibration information through the analysis;
  retain covariance where the method requires it.
- **Keep claims tied to evidence.** Check methods against applicable primary
  sources and product documentation. Missing observations, unsupported coefficients
  and failed checks remain explicit problems, not invented defaults or silent fixes.
- **Make work reviewable.** Keep raw inputs unchanged, write derivatives to new
  paths and report the actual code, selections, versions, checks and unresolved
  limits needed to understand the output.

The process stays proportional: source navigation returns a code map and relevant
findings; code-only requests return code with its check status; consequential
scientific interpretation needs its own acceptance evidence and responsible human.
These are instructions for the assistant, not a runtime enforcement system or a
guarantee that generated code is scientifically valid.

## NASA-informed engineering and assurance

NASA documents are a design basis for FEZA's workflow, not just bibliography
entries. They contribute three complementary perspectives:

| Basis | How it informs FEZA's instructions |
|---|---|
| **NPR 7150.2D — NASA Software Engineering Requirements** (§§3.1, 3.5, 3.12, 5.1) | Consider reuse before new development; establish intended use and classification rationale; connect requirements to verification and defects; identify relevant code, data and tool versions |
| **NASA-STD-8739.8B — Software Assurance and Software Safety Standard** (§4) | Distinguish software checks from assurance and safety-criticality decisions; identify applicable project responsibilities rather than treating an agent's review as independent approval |
| **NASA-STD-7009B — Standard for Models and Simulations** (§§4.2–4.3) | Make input provenance, units, assumptions, permissible-use limits, warnings and uncertainty visible when assessing and reporting derived results |

In practice, FEZA asks the assistant to **reuse → verify → inspect → record →
report**, within the user's authorized scope. A passing software test is not
evidence of adequate instrument calibration, model adequacy or a physical discovery.
Consequential work needs an intended-use and criticality decision; read-only source
navigation does not inherit a scientific approval form.

**NASA-informed does not mean NASA-affiliated, endorsed, certified or fully
compliant.** Actual requirements depend on the project and governing agreements.
FEZA cannot grant classification approval, waivers or independent verification
status, and is not a stand-alone process for flight or operational-control work.
The [standards guide](skills/feza/references/standards.md) explains applicability;
the [development bibliography](docs/sources.md#nasa-standards-and-context-navigation)
identifies the primary documents.

## Context reduction without discarding evidence

FEZA aims to spend the model's context on the current question rather than on
repeated full-file reads. It uses two complementary approaches:

1. **On-demand guidance:** load the skill entrypoint and only the reference
   sections relevant to the request, not every astronomy recipe at once.
2. **Structure-first source navigation:** search for files and symbols, generate
   an abstract syntax tree (AST) skeleton for an unfamiliar large Python module,
   then read the original implementation ranges and connected callers/tests.
   The map retains signatures, docstrings, imports and selected enclosing structure;
   implementation statements are omitted where they are not needed for navigation.

The sequence is **search → map → read → check**, not "replace the source with a
summary." Exact qualified-symbol focus narrows a map to a class or method, original
line labels point back to the code, and short path/symbol checkpoints avoid
reloading the same module. Known source ranges can be read directly without a map.

This reduces what is requested for inspection, not the scientific evidence kept
on disk. Units, provenance, uncertainties, relevant equations and failure evidence
must not be discarded to fit a context budget. The approach takes design inspiration
from *Stingy Context*, but FEZA's stdlib AST recipe is separately written: it does
not implement TREEFRAG or claim the paper's compression ratios. Actual model-token
savings and agent-quality gains remain unmeasured. See
[Python source navigation](#python-source-navigation) for the recipe and limits.

## Scope

| Area | Work described by the skill |
|---|---|
| FITS and tables | Inspect HDUs, select tables explicitly, interpret units and masks, retain integer identifiers, export tables with readback checks |
| Spectra and units | Convert wavelength-dependent flux densities and uncertainties without substituting a single reference wavelength |
| Time | Interpret split time references, offsets and time scales; distinguish a scale conversion from a barycentric correction |
| Coordinates and WCS | Retain frame/epoch information, keep association alternatives and interpret image pixel conventions |
| Gaia DR3 | Prepare ADQL, inspect query delivery status, preserve exact identifiers and reconstruct the documented astrometric covariance basis |
| HST/STIS | Inspect first-order extracted spectra, valid-element counts, calibration switches and data-quality flags |
| Measurements | Carry units, weights and covariance through declared linear measurements |
| Literature and figures | Map a published method to analysis inputs, record its assumptions and prepare figures/captions from actual data |
| Python source | Produce an AST map with original line ranges, then read the relevant implementations and callers |

The instrument-specific recipes cover Gaia DR3 and first-order STIS `x1d`/`sx1`
inspection. They do not implement a general reduction pipeline, distance estimator,
dust-law calibration or universal quality cut. Another instrument needs its own
product documentation and calibration assumptions.

## Requirements

To load FEZA, use a client that supports Agent Skills. Reading its Markdown files
does not require Python. Requirements for executing generated code depend on the
task:

| Task | Environment needed |
|---|---|
| AST source navigation | Python 3.12+; standard library only |
| FITS, tables, units, time and coordinates | Astropy and NumPy |
| Archive queries | Astroquery or another applicable archive client; authorized network access |
| Figures | Matplotlib |
| Catalogue searches using Astropy's matching routines | SciPy in addition to Astropy |

The recipes were written against Astropy 8.0.1 documentation. That identifies their
API basis, not a requirement to replace every user's existing environment. Check
the installed library versions when adapting code. FEZA does not install or update
dependencies automatically.

## Installation

### Claude Code plugin

Enter these as **two separate messages inside Claude Code**, not in your shell:

```text
/plugin marketplace add shenfurkan/FEZA
```

```text
/plugin install feza@feza
```

In the plugin panel, confirm the installation and choose whether it applies to
your user account or this project. Then invoke the skill with `/feza:feza`.
If Claude Code asks for a reload, use `/reload-plugins`.

This route uses Claude Code's built-in plugin manager. It does not require npx,
Node.js or manually copying the skill. The plugin loads the existing
`skills/feza/` directory; there is no second copy of the skill source to maintain.

### OpenCode V2

Install the skill for your user account:

```bash
npx skills@1.7.2 add shenfurkan/FEZA --skill feza --agent opencode --global --copy
```

This uses the third-party `skills` installer. Its global OpenCode destination is
`~/.config/opencode/skills/feza/`; without `--global`, it uses the compatible
project-local `.agents/skills/feza/` directory. The installer needs Node.js 22.20.0+;
FEZA itself does not need a JavaScript plugin.

To use OpenCode's native configuration instead, without npx, clone FEZA:

```bash
git clone https://github.com/shenfurkan/FEZA.git "$HOME/FEZA"
```

Add this skill source to your existing global
`~/.config/opencode/opencode.jsonc`, preserving its other settings:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "skills": ["~/FEZA/skills"]
}
```

Keep the clone in place. OpenCode V2 discovers `feza/SKILL.md` in that source and
loads its body on demand. In an OpenCode prompt, use:

```text
@feza Map src/analysis.py, then read the original loader and its callers.
```

OpenCode also supports direct copies under `.opencode/skills/feza/` or
`~/.config/opencode/skills/feza/`. The Claude Code `/plugin` commands above do not
apply to OpenCode. See [OpenCode installation details](INSTALLATION.md#2-opencode-v2)
for discovery, permissions and reload notes.

### Alternative direct installation with npx

Install for your user account, so the skill is available across projects:

```bash
npx skills@1.7.2 add shenfurkan/FEZA --skill feza --agent claude-code --global --copy
```

For one research project, run this from that project's root instead:

```bash
npx skills@1.7.2 add shenfurkan/FEZA --skill feza --agent claude-code --copy
```

These commands use Vercel Labs' `skills` installer, version 1.7.2, which requires
Node.js 22.20.0 or newer. `--global` selects a personal installation; without it the
installation is project-local. `--copy` keeps an independent copy of the complete
skill directory. Review any existing FEZA installation before replacing it.

For Codex, use `--agent codex` in place of `--agent claude-code`.

### Git clone and manual installation

Clone the repository:

```bash
git clone https://github.com/shenfurkan/FEZA.git feza && cd feza
```

Copy the complete `skills/feza/` directory to one of these locations, retaining
`feza` as the directory name:

| Client | Personal installation | Project-local installation |
|---|---|---|
| Claude Code | `~/.claude/skills/feza/` | `<research-project>/.claude/skills/feza/` |
| OpenCode V2 | `~/.config/opencode/skills/feza/` | `<research-project>/.opencode/skills/feza/` |
| Codex | `~/.agents/skills/feza/` | `<research-project>/.agents/skills/feza/` |

Copy `SKILL.md`, `references/`, `assets/` and `LICENSE` together, not just the
entrypoint. Do not copy the entire repository into the client's skill directory.
The manual route does not require Node.js or npm. Symlinks are another option if
you want the installed skill to follow a reviewed local clone.

Alternatively, from the clone root, install the local skill with npx:

```bash
npx skills@1.7.2 add ./skills/feza --skill feza --agent claude-code --global --copy
```

[INSTALLATION.md](INSTALLATION.md) contains Bash symlink commands, Windows
PowerShell copying instructions, discovery troubleshooting, updates and removal.

### Claude.ai and Cowork

Where custom-skill uploads are available, upload a ZIP containing one top-level
`feza/` directory with `SKILL.md` and its supporting files through **Customize >
Skills**. A local Claude Code installation is separate from an account upload.
Account and organization settings determine whether the upload is available.

## Usage

In Claude Code, list skills with `/skills`. Plugin installations use the namespaced
command `/feza:feza`; direct npx/manual installations use `/feza`. In Codex, use
`/skills` or mention `$feza`. In OpenCode V2, mention `@feza`; the agent loads it
with the `skill` tool using the ID `feza`. A client may also select FEZA when a
request matches its description. Choose one installation method to avoid duplicate
entries.

Examples for Claude Code; replace the paths and quantities with actual project
inputs:

```text
/feza:feza Inspect data/spectrum_x1d.fits. Identify the SCI extension, spectral
order, valid samples, units, calibration state and quality flags. Do not
modify the original file.
```

```text
/feza:feza Convert the wavelength, flux and error quantities in my notebook
from F_lambda to Jy. Keep negative flux values and record missing samples.
```

```text
/feza:feza Map src/analysis.py without importing or running it. Locate the
loader, then read its original implementation and relevant callers.
```

The output depends on the request: code, an input audit, a table, a measurement,
a figure or a source map. Code supplied without execution is identified as such.
Source navigation does not require a scientific classification form or the full
results-report template.

For a direct npx/manual installation, replace `/feza:feza` with `/feza` in those
examples.

## Python source navigation

The [AST recipe](skills/feza/references/stingy-context.md) is intended for an
unfamiliar Python module whose full implementation is not needed at once:

1. Search for relevant files and symbols.
2. Produce a map of one module, retaining definitions, signatures, docstrings,
   imports and selected enclosing structure while omitting implementation bodies.
3. Use its inclusive `[Lines X-Y]` labels to read the original implementation,
   nearby contracts and relevant callers/tests.
4. Regenerate the map after source changes; old ranges describe the old source.

After adapting the recipe from the Markdown reference, an assistant can request
the whole module or one exact qualified definition:

```python
skeletonize_file(path)
skeletonize_file(path, symbol="Analysis.measure")
```

`skeletonize_file` is defined in the recipe, not provided by an installed FEZA
module. The focused form omits enclosing namespace and branch context; those
original ranges still need inspection when relevant. Missing or ambiguous symbol
names produce an error rather than selecting an arbitrary definition.

The recipe uses Python's `ast`, `tokenize`, `io` and `pathlib`. It reads source
without importing it, includes decorator start lines in definition spans and
checks that rendering/annotations preserve the pruned AST. The returned map is
text for navigation: do not execute it or write it over the original source.

This workflow is an instruction to the assistant, not a client hook or access
restriction. It does not apply the Python parser to notebooks, papers, FITS files
or catalogues. There is no measured context-reduction ratio or agent-performance
benchmark for the current recipe.

## Sources used during development

The following documents were used to write or review the instructions. They are
development references, not extra files users must install. The full bibliography,
source versions and local-copy index are in [docs/sources.md](docs/sources.md).

### Astronomy libraries, data products and formats

| Source | Use in FEZA |
|---|---|
| [Astropy 8.0.1 documentation](https://docs.astropy.org/en/v8.0.1/) — FITS I/O, tables/ECSV, masked quantities, unit equivalencies, time, coordinate matching and WCS | Native analysis recipes and API conventions |
| [NumPy documentation: `numpy.allclose`](https://numpy.org/doc/stable/reference/generated/numpy.allclose.html), reviewed as NumPy 2.5 | Numerical comparison defaults and tolerance cautions |
| [Astroquery Gaia documentation](https://astroquery.readthedocs.io/en/stable/gaia/gaia.html), displayed as 0.4.11, and [MAST observation queries](https://astroquery.readthedocs.io/en/stable/mast/mast_obsquery.html) | Query preparation, product selection and download handling |
| [PyVO DAL query implementation](https://pyvo.readthedocs.io/en/stable/_modules/pyvo/dal/query.html) | Client-side status, error and overflow handling |
| [Gaia DR3 `gaia_source` data model](https://gea.esac.esa.int/archive/documentation/GDR3/Gaia_archive/chap_datamodel/sec_dm_main_source_catalogue/ssec_dm_gaia_source.html) and [Gaia DR3 Known Issues](https://www.cosmos.esa.int/web/gaia/dr3-known-issues) | Column meanings, units, epochs, correlations and release-specific limitations |
| [ESA Gaia EDR3 code and applicability notes](https://www.cosmos.esa.int/web/gaia/edr3-code) | Distinguishing EDR3 corrections from changes already applied in DR3 |
| *STIS Data Handbook*, versions 8.0 and 7.0, especially [Working with Extracted Spectra](https://hst-docs.stsci.edu/stisdhb/chapter-5-stis-data-analysis/5-5-working-with-extracted-spectra) | Extracted-spectrum structure, units, calibration and DQ interpretation |
| [STIS `stistools.poisson_err` documentation](https://stistools.readthedocs.io/en/latest/poisson_err.html) | MAMA/count-input applicability and limits of the error utility |
| [FITS Standard 4.0](https://fits.gsfc.nasa.gov/fits_standard.html) | File-format and metadata conventions |
| [IVOA DALI 1.1](https://www.ivoa.net/documents/DALI/20170517/REC-DALI-1.1.html) and [VOTable 1.5](https://www.ivoa.net/documents/VOTable/20250116/REC-VOTable-1.5.html) | Query delivery status, overflow and table representation |
| [`dust_extinction` G23 documentation](https://dust-extinction.readthedocs.io/en/stable/api/dust_extinction.parameter_averages.G23.html) and [normalization notes](https://dust-extinction.readthedocs.io/en/stable/dust_extinction/normalization_details.html) | The literature handoff example's model-version and normalization distinctions |

### Research papers

| Paper | Subject used in the guidance |
|---|---|
| Lindegren et al. (2021), *The astrometric solution*, A&A 649, A2 — [10.1051/0004-6361/202039709](https://doi.org/10.1051/0004-6361/202039709) | Five/six-parameter astrometry, colour handling and systematics |
| Lindegren et al. (2021), *Parallax bias versus magnitude, colour, and position*, A&A 649, A4 — [10.1051/0004-6361/202039653](https://doi.org/10.1051/0004-6361/202039653) | Inputs and applicability of parallax-bias prescriptions |
| El-Badry, Rix & Heintz (2021), *A million binaries from Gaia eDR3*, MNRAS 506, 2269 — [10.1093/mnras/stab323](https://doi.org/10.1093/mnras/stab323) | Conditional uncertainty calibration and shared systematics |
| Cantat-Gaudin et al. (2023), *An empirical model of the Gaia DR3 selection function*, A&A 669, A55 — [10.1051/0004-6361/202244784](https://doi.org/10.1051/0004-6361/202244784) | Parent-catalogue selection versus selected subsets |
| Gordon et al. (2023), *One Relation for All Wavelengths*, ApJ 950, 86 — [10.3847/1538-4357/accb59](https://doi.org/10.3847/1538-4357/accb59); 2025 erratum, ApJ 992, 217 — [10.3847/1538-4357/ae0cca](https://doi.org/10.3847/1538-4357/ae0cca) | Source-version, correction and implementation-variant checks; no calibrated extinction implementation is bundled |
| David Linus Ostby, *Stingy Context: 18:1 Hierarchical Code Compression for LLM Auto-Coding*, [arXiv:2601.19929v2](https://arxiv.org/abs/2601.19929v2) | Hierarchy-first navigation as a design reference; FEZA's AST recipe is separately written and does not reproduce TREEFRAG or inherit its reported ratios |

### Engineering, assurance and publication guidance

| Document | Use in FEZA |
|---|---|
| [NPR 7150.2D — NASA Software Engineering Requirements](https://nodis3.gsfc.nasa.gov/npg_img/N_PR_7150_002D_/N_PR_7150_002D_.pdf), including Appendix C/D and LaRC Class D/E Requirements Mapping Matrix templates | Intended use, software classification, verification, configuration and defect records |
| [NASA-STD-8739.8B — Software Assurance and Software Safety Standard](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf) | Assurance scope and safety-criticality distinctions |
| [NASA-STD-7009B — Standard for Models and Simulations](https://standards.nasa.gov/sites/default/files/standards/NASA/B/1/NASA-STD-7009B-Final-3-5-2024.pdf) | Assumptions, uncertainty, warnings and permissible-use reporting |
| NASA-HDBK-7009B and [NASA Software Engineering Handbook (SWEHB)](https://swehb.nasa.gov) | Explanatory credibility and coverage guidance, distinct from mandatory requirements |
| [SPD-41a — Scientific Information Policy for the Science Mission Directorate](https://science.nasa.gov/wp-content/uploads/2023/08/smd-information-policy-spd-41a.pdf), *SMD Open-Source Science Guidance* v2.2, and [APD Policy-13 v1.8](https://science.nasa.gov/wp-content/uploads/2023/05/APD_Data_Policy_v1.8.pdf) | Applicable SMD/APD software-release and licensing terms |
| NPR 2210.1E — *Release of NASA Software* | Distinguishing NASA's own software-release process from other research software |
| [AAS author AI/LLM guidelines](https://journals.aas.org/author-llm-guidelines/), [AAS Data Guide](https://journals.aas.org/data-guide/) and [AAS software citation policy](https://journals.aas.org/policy-statement-on-software/) | Manuscript/figure disclosure, data presentation and software citations |
| [NASA ADS Developer API](https://github.com/adsabs/adsabs-dev-api) and [arXiv reuse guidance](https://info.arxiv.org/help/license/reuse.html) | Literature discovery, bibliographic identity and source reuse terms |

The retained NASA-HDBK-7009B copy has conflicting approved-cover/draft-header
markings. The NASA-HDBK-2203 PDF is a landing-page stub; the coverage discussion
uses the retained SWEHB text, not that stub. These limitations are recorded in
the development bibliography.

NASA requirements apply according to the relevant project and agreement; citing
them does not certify FEZA or make a user's analysis NASA-compliant.

### Skill format and Python navigation

- [Agent Skills specification](https://agentskills.io/specification): directory
  structure, frontmatter and on-demand resource loading.
- [Claude Code: Extend Claude with skills](https://code.claude.com/docs/en/skills)
  and [OpenAI: Build skills](https://developers.openai.com/codex/build-skills):
  client discovery locations and invocation.
- [OpenCode V2: Skills](https://opencode.ai/v2/docs/skills/),
  [Config](https://opencode.ai/v2/docs/config/) and
  [Permissions](https://opencode.ai/v2/docs/permissions/): native skill discovery,
  the `skills` source array, `@feza` invocation and skill-scoped permissions.
  The [OpenCode V2 plugin guide](https://opencode.ai/v2/docs/build/plugins/) describes
  runtime plugins, which FEZA does not require.
- [Claude Code: Create a marketplace](https://code.claude.com/docs/en/plugins/create-marketplace),
  [Plugin manifest reference](https://code.claude.com/docs/en/plugins/manifest-reference)
  and [Install and manage plugins](https://code.claude.com/docs/en/plugins/install):
  the marketplace/manifest files and native plugin installation flow.
- [Vercel Labs `skills` 1.7.2 README](https://github.com/vercel-labs/skills/blob/v1.7.2/README.md)
  and [npm package metadata](https://registry.npmjs.org/skills/1.7.2): installer
  options and Node.js requirement.
- [Python 3.12 `ast`](https://docs.python.org/3.12/library/ast.html) and
  [`tokenize`](https://docs.python.org/3.12/library/tokenize.html): parsing, source
  positions, rendering and encoding-aware source reading.

During development, source-dependent formulas and conventions are checked against
retained primary documents rather than reconstructed from memory. The local
`literature/` collection is git-ignored and is not part of the skill distribution.
This is a rule for authoring FEZA, not a download/storage requirement for its users.

## Repository structure

```text
.github/workflows/validate.yml # manually triggered static checks
tools/validate.py              # local, dependency-free development checks

.claude-plugin/
├── marketplace.json         # catalog used by /plugin marketplace add
└── plugin.json              # plugin name/version; loads skills/ by default

skills/feza/
├── SKILL.md                 # entrypoint and task routing
├── README.md                # installed-directory usage
├── LICENSE
├── references/              # operational instructions and Python recipes
│   ├── astropy-workflows.md
│   ├── gaia.md
│   ├── literature.md
│   ├── publication.md
│   ├── standards.md
│   ├── stingy-context.md
│   └── stis.md
├── assets/results-report.md # scientific-result reporting template
└── evals/                   # development cases, prompts and controls

docs/
├── sources.md               # development bibliography and local-copy index
├── verification.md          # recorded checks and unresolved coverage
└── skills-suite-improvement-plan.md

evals/                      # compatibility mirrors of the two eval JSON files
INSTALLATION.md              # platform-specific installation details
VERSION
LICENSE.txt
```

The client initially sees skill metadata, loads `SKILL.md` when FEZA is selected
and reads the relevant recipe files as needed. The repository's development
bibliography is outside the installed skill. `evals/` is development material,
not part of the normal task workflow.

## Verification and limitations

The current source has undergone static review, metadata/JSON consistency checks,
relative-link checks and syntax checking of the embedded Python and Bash examples.
The revised skeleton has not been behaviorally tested; client installation and
native-data cases 1–8 have not been exercised for this revision. Earlier development
results do not establish acceptance of later edits.

[docs/verification.md](docs/verification.md) records the check scope, historical
results and remaining gaps. The evaluation definitions are in
[skills/feza/evals/evals.json](skills/feza/evals/evals.json), with synthetic controls
in [regression-controls.md](skills/feza/evals/regression-controls.md). Synthetic
controls are not observations or independent scientific validation.

Run the repository's static checks from a clone with Python 3.12+ and Bash:

```bash
python3 tools/validate.py
```

This checks inline relative Markdown links/anchors, JSON and mirror consistency,
basic name/version metadata and code-example syntax, including indented fences.
It does not import or execute recipes, query services, install packages or require
the developer's ignored literature collection. It is not a replacement for the
official client/frontmatter validators or scientific tests. PowerShell examples
and external URL availability are outside this check.

The **Static validation** GitHub Actions workflow runs the same command when a
maintainer selects **Run workflow**. It is manual-only, read-only and bounded to
three minutes; no remote workflow run is claimed here.

Generated scientific code still needs checks against the actual inputs, method
domain and intended use. Preserve units, masks, source identifiers and native
products; distinguish a passing software check from adequate calibration or a
supported physical inference.

## Contributing

Edit the canonical skill under `skills/feza/`. Keep development bibliographies and
source-download procedures in repository documentation, not in the installed
instructions. For a correction, describe the affected input/output and retain a
case that distinguishes the defect from the intended behavior. State checks that
were not run. Keep root evaluation JSON mirrors identical to the skill-local files.
For behavioral comparisons, supply only the relevant input from
[scenarios.md](skills/feza/evals/scenarios.md). Keep `evals.json` and the known-answer
regression controls out of candidate workspaces; they are evaluator-side material.
Keep `VERSION`, `metadata.version` in `SKILL.md` and the plugin manifest version
aligned. Change the version for a new published plugin revision so clients can
refresh the versioned copy; first-release preparation remains at `0.0.1`.

For a bug report, include the client/library versions, a minimal redacted input,
the expected and actual behavior, and the relevant warnings or error. Do not
attach credentials or private observations to a public report.

## License

FEZA's original instructions and recipes are distributed under the
[MIT license](LICENSE.txt). Referenced papers, documentation, datasets and third-party
software retain their own licenses and reuse terms.
