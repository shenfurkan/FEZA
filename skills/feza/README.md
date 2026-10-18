# FEZA skill

Version 0.0.1 · MIT

Start with [SKILL.md](SKILL.md), then read the reference section for the task.

| Work | Reference |
|---|---|
| FITS, tables/masks, units, time, coordinates/WCS and linear propagation | [Astropy recipes](references/astropy-workflows.md) |
| Published method to analysis inputs | [Literature](references/literature.md) |
| Gaia query delivery and astrometric meaning | [Gaia](references/gaia.md) |
| STIS first-order selection, units, DQ and error context | [STIS](references/stis.md) |
| Source-data plot and methods/caption | [Publication](references/publication.md) |
| NASA basis, applicability and project-policy limits | [Standards](references/standards.md) |
| Lean code context across all research routes | [Stingy Context](references/stingy-context.md) |

FEZA contains Markdown instructions and Python recipes, not an importable analysis
library. Coding agents load FEZA from their client's skill location
and write native, self-contained Astropy and Astroquery code
directly inside the user's project. There is no FEZA module to import or wrapper
to invoke.
The optional [results report](assets/results-report.md) supports consequential
scientific results; a code-navigation request needs only paths, ranges and findings.
Formal assurance follows the project's actual requirements; installing FEZA does
not add a NASA classification or approval gate to unrelated research.

## Use

Keep this `feza/` directory together. With the FEZA Claude Code plugin, invoke
`/feza:feza`. Direct copies under `.claude/skills/feza/` or
`~/.claude/skills/feza/` use `/feza` instead. Use one installation method to avoid
duplicate entries.
OpenCode V2 reads `.opencode/skills/feza/`, `~/.config/opencode/skills/feza/` or a
configured `skills` source; mention `@feza` to load it. A runtime plugin is not
needed.
Codex uses `.agents/skills/feza/` or `~/.agents/skills/feza/` and `$feza` or
`/skills`. Other clients have their own discovery/invocation conventions;
`skills/feza/` is the repository's source layout, not a universal discovery path.
Reading the skill needs no Python, server, hook, credential or literature bundle.

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

Search paths/symbols and read known source ranges directly. For an unfamiliar large
module, a compact tree of paths, symbols and original ranges may help. The
[navigation guide](references/stingy-context.md#workflow) also offers an optional
standard-library AST recipe when a richer map is useful; use its exact
`symbol="Class.method"` focus if only one definition needs a map. Read original
implementations and relevant callers/tests before diagnosing or editing; inspect
enclosing context when needed. For non-Python inputs, use native inventories/search
and targeted excerpts. Maps never replace original code or scientific evidence.

## Rights and scientific limits

[MIT](LICENSE) covers the original instructions, summaries and template. Linked
and locally stored papers, software, documentation and observations retain their
terms.

FEZA does not provide a calibrated dust law, distance estimator, reduction pipeline
or universal quality threshold. Check generated code and scientific results
against the actual inputs, assumptions and intended use.
