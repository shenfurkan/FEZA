# FEZA

**Framework for Extraterrestrial & Zenith-grade Astrophysics**

**0.0.1 · MIT · Pure-Markdown astronomy Agent Skill**

FEZA helps scientists analyze telescope data with Astropy and established astronomy
tools. It covers FITS/table handling, units, time, coordinates/WCS, Gaia, HST/STIS,
literature-to-method handoffs and scientific figures. Its `feza` Agent Skill is
**100% pure Markdown**: coding agents load it from their client's skills directory
and write native, self-contained Astropy code directly inside the
user's project. It is not a pip package, build-package hybrid or importable
analysis library.

## Install in Claude Code / Agent Skills environments

### With npx

After this repository is published at `shenfurkan/FEZA`:

```bash
DISABLE_TELEMETRY=1 npx skills@1.7.2 add shenfurkan/FEZA --skill feza --agent claude-code --global --copy
```

This uses the existing **Vercel Labs `skills` installer**, not an npm package named
`feza`. It needs Node.js 22.20.0 or newer and installs to the personal skills
location. Omit `--global` to install only in your research project. Review the
installer prompts; do not overwrite an existing `feza` skill without inspection.

### With Git clone

```bash
git clone https://github.com/shenfurkan/FEZA.git feza && cd feza
```

Then install from the clone with npx, or copy/link `skills/feza` **without npm**:
Claude Code uses `.claude/skills/feza` or `~/.claude/skills/feza`; Codex uses
`.agents/skills/feza` or `~/.agents/skills/feza`. Full safe
commands, project-local installation and Windows instructions are in
[INSTALLATION.md](INSTALLATION.md).

In Claude Code, use `/skills` to see FEZA and `/feza` to invoke it; in Codex,
use `/skills` or mention `$feza`. Coding agents
can also select it automatically from its description. Loading the skill supplies
Markdown instructions and recipes when relevant; it does not train the model,
grant new permissions or install scientific libraries.

**Publication boundary:** this local repository is prepared independently. A Git
remote URL or these instructions do not create/publish the GitHub repository. Remote
clone/npx commands require the repository and its files to be accessible to you.
From this already prepared local checkout, the local-path command in the installation
guide does not require FEZA to have been published.

## Claude.ai and Cowork

Upload a reviewed ZIP containing a single top-level `feza/` folder with `SKILL.md`
and its supporting Markdown files under **Customize > Skills**, when custom
skills/code execution are available for your account. A local skills directory
install does not by itself upload the skill to your account or enable it in Cowork.

## Start producing useful work

```text
/feza Map src/analysis.py without importing or running it. Find the loader,
then read its original implementation and callers before explaining it.

/feza Inspect data/spectrum_x1d.fits: select the SCI row/order, retain its
units, masks and DQ, and prepare a plot without changing the native product.

/feza Convert my wavelength-dependent flux and error quantities to Jy,
preserving negative flux and explicitly recording missing samples.
```

Use real paths/arrays in your project. A navigation request returns a compact map
and relevant original ranges, not a scientific-acceptance form. Python 3.12+ is
needed for the AST recipe; it uses only the standard library. Generated scientific
code needs the relevant Astropy/NumPy environment (plus Astroquery for queries,
Matplotlib for plots or SciPy for catalogue search). Nothing is installed or run
merely by loading FEZA.

## Repository layout

```text
FEZA/
├── README.md
├── INSTALLATION.md
├── LICENSE
├── VERSION
├── docs/               # development bibliography, design and verification
├── literature/         # local primary sources (git-ignored)
├── evals/
│   ├── evals.json
│   └── trigger_evals.json
└── skills/feza/
    ├── SKILL.md
    ├── README.md
    ├── LICENSE
    ├── evals/
    │   ├── evals.json
    │   ├── trigger_evals.json
    │   └── regression-controls.md
    ├── references/
    │   ├── astropy-workflows.md
    │   ├── gaia.md
    │   ├── literature.md
    │   ├── publication.md
    │   ├── standards.md
    │   ├── stingy-context.md
    │   └── stis.md
    └── assets/
        └── results-report.md
```

`skills/feza/SKILL.md` is the canonical source entrypoint; discovery and invocation
are client-specific, as the installation guide explains. The [skill guide](skills/feza/README.md)
describes the actual scientific scope. The repository-only
[development bibliography](docs/sources.md) indexes the primary sources and local
literature used to write the skill. It is not copied into the skill package.

## Source discipline (development)

Development rule for this repository: every formula, coefficient and unit
convention that enters `skills/feza/` is verified against the original primary
source (paper PDF/TeX, standard document) retained locally under `literature/`;
equations are never written from memory or from secondary summaries. `literature/`
is a local-only, git-ignored collection — it is not part of the published
repository or of the skill package. This discipline is a development rule for this
repository, not a rule imposed on installed users. The developer's bibliographic
links, local collection paths and paper-comparison notes stay in `docs/`.

The implementation basis is explicit in [development sources](docs/sources.md):
Astropy 8.0.1 documentation, Gaia DR3 data definitions, STIS handbooks, DALI/VOTable,
NASA engineering/credibility documents and the Agent Skills/client specifications.
The AST recipe is original stdlib code informed by hierarchy-first navigation; it
is not TREEFRAG code, a model fine-tune or a NASA-qualified implementation.

## Lean research context

Every research route starts with bounded discovery rather than loading whole
files. For unfamiliar large Python modules, agents use the standard-library-only
`ast` recipe in [Stingy Context](skills/feza/references/stingy-context.md) and
then read the original source ranges marked `[Lines X-Y]`. The recipe preserves
signatures, annotations, docstrings and imports while pruning implementation
statements.

The navigation recipe supports:

- **Module or focused view:** `skeletonize_file(path)` or
  `skeletonize_file(path, symbol="Analysis.measure")`; exact qualified names, no
  arbitrary first-match selection when definitions are ambiguous.
- **Original source ranges:** inclusive lines, including the first `@` of a
  multiline decorator; retained signatures, docstrings and nested structure.
- **Fail-closed rendering:** annotation-collision and AST-structure checks reject a
  distorted map; original implementations remain the authority.
- **No project execution:** stdlib-only parsing and syntax compilation, with text
  output rather than imports, hooks, a service, embeddings or source rewriting.

This is instruction-level routing, not a client hook that blocks raw-file reads.
Papers, notebooks and observational files still use native search/inventory tools.
The map retains source ranges and contracts; it does not establish behavior.
Read original implementation before making changes. The
[skeleton design notes](docs/sources.md#skeleton-design-basis) separate the
inspiration paper's findings from FEZA's own capabilities. No measured speedup or
model-token reduction is claimed for this release.

## Evaluation suite

`skills/feza/evals/` is canonical; root `evals/` contains compatibility mirrors of
the two JSON files. Keep each mirror byte-identical when editing. `evals.json`
contains behavioral **specifications**, not executed acceptance results. Its `files`
entries are real paths relative to the skill root; `input_requirements` describes
any additional evaluator-supplied material, not fictitious fixture paths.
The [synthetic development controls](skills/feza/evals/regression-controls.md)
retain numerical and policy regressions without posing as observations. Native
instrument cases remain unavailable until their declared inputs are supplied.
`trigger_evals.json` holds positive/near-miss prompts, including code navigation.
Keep input versions, independent expectations and the environment with evaluation
results. Evaluation rubrics are development material, not instructions for ordinary
users; with-skill candidates must not read them.

## Verification status — 0.0.1

- **Historical development evidence:** 40/40 mechanical checks on the earlier
  recipes (Python 3.13.15, Astropy 8.0.1, NumPy 2.5.4); four earlier agent cases
  scored 15/15 with the skill versus 14/15 without it. Both agent configurations
  inherited overlapping repository instructions; this is not a clean measure of
  the standalone skill's benefit.
- **Current revision:** static review, Markdown/link/JSON checks and embedded-Python
  syntax checks only. The revised skeleton is not covered by the historical score;
  behavior tests were explicitly declined for this preparation pass.
- **Still unverified:** native-data cases 1–8, clean-workspace client installation,
  held-out/other-model assessment and user review. No NASA certification or
  "official production quality" status is claimed.

See [verification scope](docs/verification.md) for the evidence and limitations.
Publishing to GitHub remains a separate, explicitly authorized action.

## Scientific scope and license

FEZA draws on applicable NPR 7150.2D engineering and NASA-STD-7009B reporting practices
summarized in [standards](skills/feza/references/standards.md); using it does not make
a project NPR-compliant. All scientific recipes live in pure Markdown under
`skills/feza/references/`, backed by primary literature and official standards
reviewed during development. Verify the actual generated analysis against
its inputs and independent expectations. API documentation is not a
scientific-validation result. Numerical work follows the scientist's approved
execution permissions and budget. Unsupported coefficients remain unsupported;
development bibliography/storage conventions are not runtime requirements.

[MIT](LICENSE) covers FEZA's original content. Linked and locally stored papers,
software, documentation and observations retain their own terms. "Zenith-grade" is
part of the name, not a certification.
