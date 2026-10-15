# FEZA skill

**0.0.1 · MIT · 100% Pure-Markdown Agent Skill**

Start with [SKILL.md](SKILL.md). It routes the scientist's requested observable to
the relevant reference rather than loading an astronomy encyclopedia.

| Work | Reference |
|---|---|
| FITS, tables/masks, units, time, coordinates/WCS and linear propagation | [Astropy recipes](references/astropy-workflows.md) |
| Published method to analysis inputs | [Literature](references/literature.md) |
| Gaia query delivery and astrometric meaning | [Gaia](references/gaia.md) |
| STIS first-order selection, units, DQ and error context | [STIS](references/stis.md) |
| Source-data plot and methods/caption | [Publication](references/publication.md) |
| NASA basis, applicability and project-policy limits | [Standards](references/standards.md) |
| Lean code context across all research routes | [Stingy Context](references/stingy-context.md) |

FEZA is a **100% pure-Markdown Agent Skill**, not a pip package, library API or
build-package hybrid. Coding agents load FEZA from their client's skill location
and write native, self-contained Astropy and Astroquery code
directly inside the user's project. There is no FEZA module to import or wrapper
to invoke.
The [results report](assets/results-report.md) supports consequential scientific
results; a code-navigation request needs only paths, source ranges and findings.

## Use

Keep this `feza/` directory together. Claude Code discovers it under
`.claude/skills/feza/` or `~/.claude/skills/feza/` and invokes it with `/feza`.
Codex uses `.agents/skills/feza/` or `~/.agents/skills/feza/` and `$feza` or
`/skills`. Other clients have their own discovery/invocation conventions;
`skills/feza/` is the repository's source layout, not a universal discovery path.
Reading the skill needs no Python, server, hook, credential or literature bundle.
Developer bibliographies and source-download rules are not installed with FEZA.

The Markdown reference snippets are self-contained, adaptable Python recipes.
Executing generated analysis code in the user's project requires the scientist's
approved environment: Astropy/NumPy, Astroquery for Gaia, Matplotlib for plots
and SciPy for catalogue search. No dependencies are installed automatically. Run
numerical work only on the approved host and within the agreed scope.

Verify the generated notebook/script against native metadata and independent
identities/reference values; keep actual masks, uncertainties and input identity.
Evaluation specifications under `evals/` describe expected native Astropy behavior;
they are not execution evidence. Do not infer a successful analysis from skill
discovery.

For an unfamiliar large Python module, use the standard-library `ast`
skeletonization recipe in [references/stingy-context.md](references/stingy-context.md)
and read the inclusive `[Lines X-Y]` ranges needed for the task. Skip the map when
the relevant range is already known. Use the exact `symbol="Class.method"` focus
when only one definition needs a map; inspect the enclosing source when its
context matters. For non-Python research inputs, use native
inventories/search and targeted excerpts.
This guidance applies at every assurance scope; it never replaces original code,
scientific evidence or the requirement to inspect callers/tests before editing.

## Rights and scientific limits

[MIT](LICENSE) covers the original instructions, summaries and template. Linked
and locally stored papers, software, documentation and observations retain their
terms.

FEZA does not provide a calibrated dust law, distance estimator, reduction pipeline,
universal quality threshold or scientific-validation engine. It delivers useful
artifacts with explicit assumptions, units and evidence boundaries.
