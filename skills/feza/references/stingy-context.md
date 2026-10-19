# Stingy Context: read directly, map when useful

Search and targeted source reads are the default. For a large codebase, a
names-and-ranges index is the map to grep; a per-module AST skeleton is optional.
Neither replaces the original implementation or the agent's existing navigation
tools. Return relevant source ranges and findings, not scientific approval forms.
This is navigation, not behavior evidence.

## Contents

- [Workflow](#workflow)
- [Index recipe: names and ranges](#index-recipe-names-and-ranges)
- [Focused use and output](#focused-use-and-output)
- [Keep the index across sessions](#keep-the-index-across-sessions)
- [Optional stdlib AST recipe](#python-reference-snippet-stdlib-ast-skeletonizer)
- [Retained structure](#what-the-skeleton-retains)
- [Operational limits](#limits)

## Workflow

1. Find plausible files/symbols using the project's existing search/navigation
   tools: grep, and LSP symbol/reference lookups where the client has them. For
   short source or a known relevant range, read directly; no map is needed. If the
   client already injects a code map (for example from a session-start hook), use
   it rather than building a second one.
2. If locating code needs a map, build the [index](#index-recipe-names-and-ranges)
   once and **grep it**; never load it whole. Use the per-module AST skeleton
   only when signatures or nesting of one large module matter. A whole-repository
   skeleton is not a map: in one measured package it kept 19–38% of the source.
3. For AST maps, `# [Lines X-Y]` labels are **inclusive, one-based original source
   lines**, including decorators on definitions. For a read tool accepting one-based
   offsets, use `offset=X` and `limit=Y-X+1`. Prefer method ranges to whole classes.
4. Read original implementations, adjacent contract comments and relevant callers,
   tests and configuration before diagnosing or editing. Find every caller of a
   changed function with grep or an LSP reference lookup; the index lists
   definitions, not callers. A tree or skeleton does not establish behavior or correctness.
5. Refresh maps after source changes: line numbers are snapshot-local. An index
   file entry whose `sha256=` prefix differs from the source is stale. Keep a short
   checkpoint of paths, symbols, inspected evidence and open questions instead of
   repeatedly pasting maps or whole files.

For papers, reference Markdown, notebooks, FITS and catalogs, use native
search/inventories and bounded excerpts, not the Python parser. Keep units,
provenance, equations, failure evidence, uncertainties and observations needed for
the scientific question; a navigation tree is not a substitute for that evidence.

## Index recipe: names and ranges

One line per definition: `name start-end`, nested by indentation under a
`path lines=N sha256=<12 hex>` header. Ranges are inclusive, one-based and start
at the first decorator. Write the text to an ignored/scratch path in the user's
project, never into source trees, then grep a symbol or a file header.

```python
import ast
import hashlib
from pathlib import Path

_INDEXED = (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)
_FLAT = (ast.Expr, ast.Assign, ast.AnnAssign, ast.Import, ast.ImportFrom, ast.Return)
_VENDORED = {"__pycache__", "site-packages", "node_modules", "venv"}


def _index_entries(body: list[ast.stmt], depth: int = 1):
    for node in body:
        if isinstance(node, _INDEXED):
            start = min([node.lineno] + [d.lineno for d in node.decorator_list])
            yield f"{'  ' * depth}{node.name} {start}-{node.end_lineno}"
            yield from _index_entries(node.body, depth + 1)
        elif not isinstance(node, _FLAT):
            # Definitions inside if/try/with/loop/match keep the enclosing depth.
            for field in ("body", "orelse", "finalbody", "handlers", "cases"):
                yield from _index_entries(getattr(node, field, None) or [], depth)


def index_tree(root: str | Path, pattern: str = "**/*.py") -> str:
    """Names and inclusive ranges for every definition; never imports the source."""
    root = Path(root)
    lines = []
    for path in sorted(root.glob(pattern)):
        relative = path.relative_to(root)
        if any(part.startswith(".") or part in _VENDORED for part in relative.parts[:-1]):
            continue  # Environments, caches and VCS data are not project source.
        data = path.read_bytes()
        name = relative.as_posix()
        lines.append(f"{name} lines={len(data.splitlines())} "
                     f"sha256={hashlib.sha256(data).hexdigest()[:12]}")
        try:
            tree = ast.parse(data, filename=name)
        except (SyntaxError, ValueError, RecursionError) as exc:
            lines.append(f"  PARSE-ERROR {type(exc).__name__}: {exc}")
            continue
        lines.extend(_index_entries(tree.body))
    return "\n".join(lines) + "\n"
```

Call it on the user's source root and write the result to an ignored scratch file.
Hidden directories (such as `.venv` or `.git`) and `__pycache__`, `site-packages`,
`node_modules` and `venv` directories are skipped; pass a narrower `pattern` or root
when other vendored trees remain. A module that fails to parse keeps its header and
a `PARSE-ERROR` line instead of entries; grep for it and read that module directly.

## Focused use and output

When a map is useful, return only the relevant tree/excerpt and original ranges,
then answer from the inspected implementations/callers. A useful handoff is:

```text
src/analysis.py — Analysis.measure [Lines 8-11]
Read: lines 8-11 plus the actual caller and nearby contract.
Finding: describe only what those original ranges establish.
Open: list any uninspected dependency or unresolved behavior.
```

The names/ranges above are illustrative, not an executed result. For long tasks,
retain this path/symbol/read/open checkpoint instead of repasting the module map.

## Keep the index across sessions

A skill loads only when a request matches it, so a navigation question that never
names astronomy may not load FEZA at all. The project's instruction file loads in
every session. When the user expects to navigate the same large Python codebase
across sessions, or asks to make the index persistent, offer a short pointer for
that file. Skip the offer when the client already injects an equivalent code map.

1. Save the adapted `index_tree` recipe as a small script in an ignored path of the
   user's project, so the pointer can name a regeneration command. Write the index
   itself to an ignored path too.
2. Show the snippet and the target file before writing anything: `AGENTS.md` for
   clients that read it (such as Codex and OpenCode), `CLAUDE.md` or a file it
   imports for Claude Code. Edit the instruction file only after explicit approval.
3. Put only the pointer in the instruction file. That file loads on every turn, and
   an index of a large package can run to hundreds of kilobytes.

Replace the bracketed paths with the actual ignored locations:

```markdown
## Code navigation
- Python names-and-ranges index: `[index path]`. Grep it for a symbol or file
  header; never read it whole. Regenerate it with `python [script path]`.
- Before using a range, compare the file header's `sha256=` prefix with the first
  12 hex characters of the file's current SHA-256; regenerate the index when they
  differ or after edits.
- Ranges only locate code. Read the original lines, and find callers with grep or
  LSP references, before explaining or editing.
```

The pointer changes where an agent looks first; it is not evidence that context
use or answer quality improved. Measuring that needs the same tasks with and
without the pointer, counting whole-task tokens and checking the ranges found.

If choosing the AST recipe below, adapt it in an owned scratch scope and call it
with an actual user-project path, not the skill's installation directory:

```python
print(skeletonize_file(path))
```

Docstrings are omitted by default; pass `docstrings=True` when contracts matter.
If only one class or method needs a map, request its exact qualified name:

```python
print(skeletonize_file(path, symbol="Analysis.measure"))
```

The focused form omits surrounding imports, sibling definitions and enclosing
class/module context; read those original ranges when needed. Missing or ambiguous
names yield an error with candidate ranges, not an arbitrary selection; a bare name
such as `measure` suggests qualified names ending in it. A map that is not shorter
than its source raises, because reading the source directly is cheaper. Print/read
the returned text; neither call imports the user module. Do not use `exec` or `eval`
on a map.

## Python Reference Snippet: stdlib AST skeletonizer

Load this optional recipe only when a richer map is useful. It needs Python 3.12+
and the standard library, not a scientific stack or network. The recipe reads
source and returns text; it never runs the source or writes a map over it.
Reading/parsing is subject to the host's normal file-access and resource limits.

```python
import ast
import io
import tokenize
from pathlib import Path

_DEFINITIONS = (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)
_IMPORTS = (ast.Import, ast.ImportFrom)
_BLOCKS = (
    ast.If, ast.For, ast.AsyncFor, ast.While, ast.With, ast.AsyncWith,
    ast.Try, ast.TryStar, ast.Match,
)


def _decorator_starts(source: str) -> dict[int, int]:
    starts, pending = {}, []
    statement_start = True
    for token in tokenize.generate_tokens(io.StringIO(source).readline):
        if token.type in {tokenize.NL, tokenize.COMMENT, tokenize.INDENT, tokenize.DEDENT}:
            continue
        if token.type == tokenize.NEWLINE:
            statement_start = True
            continue
        if statement_start:
            if token.type == tokenize.OP and token.string == "@":
                pending.append(token.start[0])
            elif pending:
                starts[token.start[0]] = pending[0]
                pending.clear()
            statement_start = False
    return starts


def _symbols(node: ast.AST, prefix: str = ""):
    for child in ast.iter_child_nodes(node):
        if isinstance(child, _DEFINITIONS):
            name = f"{prefix}.{child.name}" if prefix else child.name
            yield name, child
            yield from _symbols(child, name)
        else:
            yield from _symbols(child, prefix)


def _ellipsis(first: ast.stmt, last: ast.stmt) -> ast.Expr:
    node = ast.copy_location(ast.Expr(value=ast.Constant(value=Ellipsis)), first)
    node.end_lineno = last.end_lineno
    node.end_col_offset = last.end_col_offset
    return node


def _block(body: list[ast.stmt], declarations: bool, docstring: bool = False,
           keep_docs: bool = True) -> list[ast.stmt]:
    kept, omitted = [], []
    for index, node in enumerate(body):
        is_doc = (
            docstring and index == 0 and isinstance(node, ast.Expr)
            and isinstance(node.value, ast.Constant) and isinstance(node.value.value, str)
        )
        if is_doc and not keep_docs:
            omitted.append(node)
            continue
        retained = _statement(node, declarations, keep_docs) if not is_doc else node
        if retained is None:
            omitted.append(node)
            continue
        if omitted:
            kept.append(_ellipsis(omitted[0], omitted[-1]))
            omitted.clear()
        kept.append(retained)
    if omitted:
        kept.append(_ellipsis(omitted[0], omitted[-1]))
    return kept


def _statement(node: ast.stmt, declarations: bool, keep_docs: bool = True) -> ast.stmt | None:
    if isinstance(node, _DEFINITIONS):
        node.body = _block(node.body, isinstance(node, ast.ClassDef), True, keep_docs)
        return node
    if isinstance(node, _IMPORTS + (ast.TypeAlias,)):
        return node
    if isinstance(node, ast.AnnAssign) or (declarations and isinstance(node, ast.Assign)):
        if node.value is not None:
            node.value = ast.Constant(value=Ellipsis)
        return node
    if isinstance(node, _BLOCKS):
        relevant = _DEFINITIONS + _IMPORTS + (ast.AnnAssign, ast.TypeAlias)
        if declarations:
            relevant += (ast.Assign,)
        if any(isinstance(child, relevant) for child in ast.walk(node)):
            _compound(node, declarations, keep_docs)
            return node
    return None


def _compound(node: ast.AST, declarations: bool, keep_docs: bool = True) -> None:
    for name, value in ast.iter_fields(node):
        if name in {"body", "orelse", "finalbody"}:
            setattr(node, name, _block(value, declarations, keep_docs=keep_docs))
        elif name in {"handlers", "cases"}:
            for child in value:
                _compound(child, declarations, keep_docs)


def skeletonize_file(path: str | Path, *, symbol: str | None = None,
                     docstrings: bool = False) -> str:
    """Map a module or exact qualified definition; never execute the returned text."""
    with tokenize.open(path) as handle:
        source = handle.read()
    filename = str(path)
    tree = ast.parse(source, filename=filename, type_comments=True)
    original_decorators = _decorator_starts(source)
    definitions = list(_symbols(tree))
    names = {id(node): name for name, node in definitions}
    if symbol is not None:
        matches = [node for name, node in definitions if name == symbol]
        if len(matches) != 1:
            spans = [(original_decorators.get(node.lineno, node.lineno), node.end_lineno)
                     for node in matches]
            similar = [name for name, _ in definitions if name.endswith("." + symbol)]
            hint = f"; qualified names ending in it: {similar}" if similar else ""
            raise ValueError(f"Expected one definition for {symbol!r}; found ranges {spans}{hint}")
        tree.body = matches
    elif not docstrings and ast.get_docstring(tree, clean=False) is not None:
        tree.body = tree.body[1:]  # an `...` there would precede `from __future__` imports
    tree.body = _block(tree.body, declarations=True, docstring=True, keep_docs=docstrings)
    tree.type_ignores = []
    text = ast.unparse(tree)
    rendered = ast.parse(text, type_comments=True)
    rendered_decorators = _decorator_starts(text)
    originals = [node for node in ast.walk(tree) if isinstance(node, ast.stmt)]
    statements = [node for node in ast.walk(rendered) if isinstance(node, ast.stmt)]
    annotations = {}
    for original, statement in zip(originals, statements, strict=True):
        if type(original) is not type(statement):
            raise ValueError("AST rendering changed statement structure; read the source directly")
        start, output_start = original.lineno, statement.lineno
        if isinstance(original, _DEFINITIONS):
            start = original_decorators.get(start, start)
            output_start = rendered_decorators.get(output_start, output_start)
        label = f" {names[id(original)]}" if id(original) in names else ""
        if output_start in annotations:
            raise ValueError("Ambiguous rendered range; read the source directly")
        annotations[output_start] = f"# [Lines {start}-{original.end_lineno}]{label}"
    lines = [f"# Skeleton of {filename!r}; implementations omitted. DO NOT EXECUTE."]
    for number, line in enumerate(text.split("\n"), 1):
        if number in annotations:
            lines.append(" " * (len(line) - len(line.lstrip())) + annotations[number])
        lines.append(line)
    result = "\n".join(lines) + "\n"
    mapped = ast.parse(result, filename=filename, type_comments=True)
    if ast.dump(mapped, include_attributes=False) != ast.dump(tree, include_attributes=False):
        raise ValueError("Rendered map changed the pruned AST; read the source directly")
    compile(result, filename, "exec", dont_inherit=True)
    if len(result) >= len(source):
        raise ValueError("Map is not shorter than the source; read the source directly")
    return result
```

## What the skeleton retains

- Module, class and function docstring values, only with `docstrings=True`.
- Imports/aliases within the selected module/definition, including local and
  conditional imports. A focused view does not supply its enclosing namespace.
- Class bases, metaclass keywords, decorators and Python 3.12 type parameters.
- Sync/async signatures, positional-only/keyword-only arguments, variadics,
  defaults and parameter/return annotations.
- Annotated declarations and `type` aliases. Module/class assignment targets are
  retained but their values become `...`.
- Nested definitions with enclosing conditional/try/with/loop/match structure
  where it contains retained architecture. Other implementation statements are
  replaced by one `...` for each consecutive omitted group.

Range labels are Python comments, so output remains parseable and compilable.
`ast.unparse` normalizes whitespace/quote styles. A comment above `...` marks the
whole omitted source span. Decorator ranges start at the tokenizer's first `@`,
including parenthesized multiline decorators, not just the decorator expression.
For example (illustrative line numbers):

```python
# [Lines 4-90]
class Reader:
    # [Lines 8-90]
    def load(self, path: str) -> bytes:
        # [Lines 9-90]
        ...
```

The recipe honors encoding declarations with `tokenize.open`, parses without
importing or evaluating the source, prunes its AST, and unparses it. It pairs
retained statements with rendered counterparts, rejects annotation collisions,
and compares the annotated map's AST with the pruned tree ignoring locations.
It splits only on literal newlines, so form-feed or Unicode separators inside
comments do not turn into invented code lines. Compilation checks syntax only;
the result is never executed. On tokenization, syntax, structure or recursion
failure, retain the error and read targeted original ranges instead of guessing.

## Limits

- **Never execute the skeleton or overwrite source with it.** Imports, decorators,
  defaults and annotations may still have side effects if someone executes it.
- Ordinary comments, scientific citations, assignment values, `__all__` contents,
  side effects, local unannotated variables and dynamic definitions are not
  represented faithfully. Original source remains authoritative.
- This is not a redactor: docstrings, signatures and defaults may contain sensitive
  text. Inspect only authorized files and do not export research data with the map.
- Long defaults or tiny modules may expand after annotations; the recipe then
  raises instead of returning a longer map. There is no guaranteed ratio.
- Standard-library `tokenize` counts Python lexical tokens, **not LLM/BPE tokens**.
  Net context savings require the same model tokenizer and account for guidance,
  recipe/map generation and subsequent source reads in both configurations. One
  measurement, characters only (289-module scientific package, 6.2 M characters):
  skeletons kept ~38% with docstrings and ~19% without, the index ~2%. No
  agent-quality benchmark is claimed.
- Grammar support follows the interpreter; extreme input size/depth can exhaust
  memory or recursion. Admit one module and its rendered map to the available
  memory; use an external timeout where the host requires it. There is no cache,
  embedding index or persistent service.
