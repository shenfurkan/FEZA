# Read-Only Python Skeletonizer Recipe

## Contents

- [Use](#use)
- [Recipe](#recipe)
- [Limits](#limits)

## Use

This is a Markdown recipe, not an installed Python module or an automatic tool.
When useful and authorized, adapt/save the code in an owned location in the user's
project, for example `scripts/skeletonize.py`, and run it with the project's Python
3.12+ interpreter on one actual source file. Reading this document runs nothing.
Use an existing equivalent navigation tool instead of creating a second one.

## Recipe

```python
#!/usr/bin/env python3
"""Produce a read-only Python architecture map using only the standard library."""

import argparse
import ast
import tokenize
from pathlib import Path


_DEFINITIONS = (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)
_IMPORTS = (ast.Import, ast.ImportFrom)
_BLOCKS = (
    ast.If, ast.For, ast.AsyncFor, ast.While, ast.With, ast.AsyncWith,
    ast.Try, ast.TryStar, ast.Match,
)


def _ellipsis(first: ast.stmt, last: ast.stmt) -> ast.Expr:
    node = ast.copy_location(ast.Expr(value=ast.Constant(value=Ellipsis)), first)
    node.end_lineno = last.end_lineno
    node.end_col_offset = last.end_col_offset
    return node


def _block(body: list[ast.stmt], declarations: bool, docstring: bool = False) -> list[ast.stmt]:
    kept = []
    omitted = []
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


def skeletonize(source: str, filename: str = "<unknown>") -> str:
    """Return parseable, non-executable-by-contract skeleton text with source ranges.

    Ranges are inclusive and refer to the input, including definition decorators.
    Consecutive discarded statements become one ellipsis with their combined range.
    """
    tree = ast.parse(source, filename=filename, type_comments=True)
    tree.body = _block(tree.body, declarations=True, docstring=True)
    tree.type_ignores = []
    text = ast.unparse(tree)
    rendered = ast.parse(text)
    originals = [node for node in ast.walk(tree) if isinstance(node, ast.stmt)]
    statements = [node for node in ast.walk(rendered) if isinstance(node, ast.stmt)]
    annotations = {}
    for original, statement in zip(originals, statements, strict=True):
        if type(original) is not type(statement):
            raise ValueError("AST rendering changed statement structure; read the source directly")
        start = min([original.lineno] + [d.lineno for d in getattr(original, "decorator_list", [])])
        output_start = min(
            [statement.lineno] + [d.lineno for d in getattr(statement, "decorator_list", [])]
        )
        annotations[output_start] = f"# [Lines {start}-{original.end_lineno}]"
    lines = [f"# Skeleton of {filename!r}; implementations omitted. DO NOT EXECUTE."]
    for number, line in enumerate(text.splitlines(), 1):
        if number in annotations:
            lines.append(" " * (len(line) - len(line.lstrip())) + annotations[number])
        lines.append(line)
    result = "\n".join(lines) + "\n"
    compile(result, filename, "exec", dont_inherit=True)
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="one Python source file (never imported or modified)")
    args = parser.parse_args(argv)
    try:
        with tokenize.open(args.path) as handle:
            source = handle.read()
        result = skeletonize(source, str(args.path))
    except (OSError, UnicodeError, SyntaxError, ValueError, RecursionError) as error:
        parser.error(str(error))
    print(result, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

## Limits

The returned text is a lossy navigation aid. Do not execute it or overwrite source
with it. Signatures, decorators and imports may still have executable effects if
the warning is ignored. Read original code and callers to establish behavior.
This recipe is preserved from the imported navigation tool; integration syntax
checks do not demonstrate new behavioral acceptance.
