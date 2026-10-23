---
name: stingy-context
description: "Navigate unfamiliar large Python modules using compact AST skeletons and original-source line ranges before reading implementation bodies. Use for locating definitions/callers and surgical edits, not as a substitute for reading numerical logic or validating code."
compatibility: "Markdown recipes use the Python 3.12+ standard library when adapted in the user's project. The optional tracked-source index also requires Git. They do not support C++ source."
---

# Stingy Context

Use a small architecture map to decide what source to read, not to infer what an
implementation does. No model call, external package, automatic hook or new database
is needed. If the symbol's location is already known, read its original range directly.

## One-file workflow

1. Locate plausible files with existing glob/grep/navigation tools.
2. For one unfamiliar large Python module, use an existing equivalent tool or adapt
   the [skeletonizer recipe](references/skeletonizer.md) into an owned project path.
   Run that actual saved path with the project's interpreter on the relevant module.
   This skill installs no Python executable or importable library.
3. Use the annotated inclusive, one-based **original source** ranges to choose the
   smallest relevant function/class/import bodies. Definition ranges include decorators.
4. Read the actual source and adjacent comments; AST spans omit ordinary leading/
   trailing comments. Inspect callers, tests, error paths, fixtures and configuration
   before explaining behavior or editing it. A skeleton is not that evidence.
5. Regenerate after edits. Ranges are a snapshot, not persistent symbol identities.

Do not concatenate a repository-wide set of skeletons into chat. Bound the search
to plausible files and stop expanding when more detail cannot change the decision.

## What is preserved and omitted

The script keeps module/class/function docstring values, imports, definition
signatures, annotations, decorators, bases, type parameters and nested definitions
with enclosing architecture-bearing control flow. It replaces implementation
groups and assignment values with annotated ellipses. Formatting is normalized
by `ast.unparse`; source is parsed, not imported or executed.

It is a lossy navigation map, not runnable code, a call graph or a correctness
proof. Never overwrite source with the result. Default expressions, imports and
decorators can still execute if someone ignores the warning and runs the skeleton.
Assignment values, exports, comments, imperative side effects and dynamic behavior
are not faithfully represented; inspect the original ranges.

The tool honors declared source encoding. Parse/encoding/recursion failures return
an error rather than a fabricated outline; read the source directly when parsing
fails. Grammar support follows the interpreter. Short files or long signatures/
docstrings can expand instead of compressing. No general compression or token-saving
ratio is promised; lexical Python tokens are not model tokenizer tokens.

## Optional tracked-source index

[The tracked-source index recipe](references/tracked-index.md) writes names,
original ranges and a short source SHA-256 for Git-tracked Python files without
importing them. Adapt it into the user's project only if needed and authorized,
then invoke the actual saved path with an explicit output location.
It defaults to the repository's `scratch/code-index.txt`; specify a path if that
location does not fit the project. New untracked files are absent. Parse failures
appear explicitly in the index. Grep the index instead of reading it whole;
compare the source's current digest prefix and regenerate before using stale ranges.

## Safety and checks

Only inspect authorized files: retained docstrings/defaults can contain sensitive
text, and this is not a redactor. This tool handles Python, not C++ macros or a
mixed-language dependency graph. Use the existing language tools for those files.

The [self-check recipe](references/self-checks.md) covers preservation, source ranges,
deterministic output, encoding, CLI failure and read-only behavior. It is Markdown,
not an installed or automatically executed test suite. On an approved host, save
and adapt it beside the actual generated implementation before running checks.
Syntax validation during integration is not a behavioral run or scientific validation.
