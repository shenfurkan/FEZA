# Stingy Context: read directly, map when useful

Search and targeted source reads are the default. A compact tree can help locate
unknown code in an unfamiliar large module; the richer AST recipe below is optional.
Neither replaces the original implementation or the agent's existing navigation
tools. Return relevant source ranges and findings, not scientific approval forms.
This is navigation, not behavior evidence.

## Contents

- [Workflow](#workflow)
- [Focused use and output](#focused-use-and-output)
- [Optional stdlib AST recipe](#python-reference-snippet-stdlib-ast-skeletonizer)
- [Retained structure](#what-the-skeleton-retains)
- [Operational limits](#limits)

## Workflow

1. Find plausible files/symbols using the project's existing search/navigation
   tools. For short source or a known relevant range, read directly; no map is needed.
2. If locating code in an unfamiliar large module needs a map, start with a compact
   tree of paths, qualified symbols and verified original ranges. Add signatures
   when useful. Use an existing symbol view or the optional AST recipe below for
   richer structure; do not build a repository-wide dump or a new indexing system.
3. For AST maps, `# [Lines X-Y]` labels are **inclusive, one-based original source
   lines**, including decorators on definitions. For a read tool accepting one-based
   offsets, use `offset=X` and `limit=Y-X+1`. Prefer method ranges to whole classes.
4. Read original implementations, adjacent contract comments and relevant callers,
   tests and configuration before diagnosing or editing. Grep every caller of a
   changed function. A tree or skeleton does not establish behavior or correctness.
5. Refresh maps after source changes: line numbers are snapshot-local. Keep a short
   checkpoint of paths, symbols, inspected evidence and open questions instead of
   repeatedly pasting maps or whole files.

For papers, reference Markdown, notebooks, FITS and catalogs, use native
search/inventories and bounded excerpts, not the Python parser. Keep units,
provenance, equations, failure evidence, uncertainties and observations needed for
the scientific question; a navigation tree is not a substitute for that evidence.

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

If choosing the AST recipe below, adapt it in an owned scratch scope and call it
with an actual user-project path, not the skill's installation directory:

```python
print(skeletonize_file(path))
```

If only one class or method needs a map, request its exact qualified name:

```python
print(skeletonize_file(path, symbol="Analysis.measure"))
```

The focused form omits surrounding imports, sibling definitions and enclosing
class/module context; read those original ranges when needed. Missing or ambiguous
names yield an error with candidate ranges, not an arbitrary selection. Print/read
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


def _block(body: list[ast.stmt], declarations: bool, docstring: bool = False) -> list[ast.stmt]:
    kept, omitted = [], []
    for index, node in enumerate(body):
        is_doc = (
            docstring and index == 0 and isinstance(node, ast.Expr)
            and isinstance(node.value, ast.Constant) and isinstance(node.value.value, str)
        )
        retained = _statement(node, declarations) if not is_doc else node
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


def _statement(node: ast.stmt, declarations: bool) -> ast.stmt | None:
    if isinstance(node, _DEFINITIONS):
        node.body = _block(node.body, isinstance(node, ast.ClassDef), docstring=True)
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
            _compound(node, declarations)
            return node
    return None


def _compound(node: ast.AST, declarations: bool) -> None:
    for name, value in ast.iter_fields(node):
        if name in {"body", "orelse", "finalbody"}:
            setattr(node, name, _block(value, declarations))
        elif name in {"handlers", "cases"}:
            for child in value:
                _compound(child, declarations)


def skeletonize_file(path: str | Path, *, symbol: str | None = None) -> str:
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
            raise ValueError(f"Expected one definition for {symbol!r}; found ranges {spans}")
        tree.body = matches
    tree.body = _block(tree.body, declarations=True, docstring=True)
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
    return result
```

## What the skeleton retains

- Module, class and function docstring values, including multiline content.
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
- Long docstrings/defaults or tiny modules may expand after annotations. There is
  no guaranteed compression ratio, and contracts are never truncated to hit one.
- Standard-library `tokenize` counts Python lexical tokens, **not LLM/BPE tokens**.
  Net context savings require the same model tokenizer and account for guidance,
  recipe/map generation and subsequent source reads in both configurations. No
  repository-wide compression or agent-quality benchmark is claimed.
- Grammar support follows the interpreter; extreme input size/depth can exhaust
  memory or recursion. Admit one module and its rendered map to the available
  memory; use an external timeout where the host requires it. There is no cache,
  embedding index or persistent service.
