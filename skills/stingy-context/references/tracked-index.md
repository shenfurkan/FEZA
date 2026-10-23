# Git-Tracked Python Index Recipe

This optional recipe indexes Git-tracked Python source without importing it.
Untracked and ignored files are absent; parse failures are explicit. If an existing
index already answers the question, use it rather than adding another tool.

Adapt/save in an owned project location only when needed and authorized. The default
output is `scratch/code-index.txt` under the Git root; pass a different ignored output
path when appropriate. Compare each current source hash prefix before trusting ranges.

```python
#!/usr/bin/env python3
"""Write a grep-able names-and-ranges index of tracked Python source.

Usage: python <skill-directory>/scripts/index_tree.py [OUTPUT]
Default OUTPUT is scratch/code-index.txt under the Git root. Never imports indexed source.
"""

import ast
import hashlib
import subprocess
import sys
from pathlib import Path

_INDEXED = (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)
_FLAT = (ast.Expr, ast.Assign, ast.AnnAssign, ast.Import, ast.ImportFrom, ast.Return)


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


def index_tree(root: Path) -> str:
    """Names and inclusive one-based ranges for every definition in git-tracked *.py files."""
    # Tracked files only; untracked work and ignored data are deliberately absent.
    names = subprocess.run(
        ["git", "ls-files", "-z", "*.py"], cwd=root, check=True, capture_output=True, text=True
    ).stdout.split("\0")
    lines = []
    for name in sorted(n for n in names if n):
        data = (root / name).read_bytes()
        lines.append(f"{name} lines={len(data.splitlines())} sha256={hashlib.sha256(data).hexdigest()[:12]}")
        try:
            tree = ast.parse(data, filename=name)
        except (SyntaxError, ValueError, RecursionError) as exc:
            lines.append(f"  PARSE-ERROR {type(exc).__name__}: {exc}")
            continue
        lines.extend(_index_entries(tree.body))
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    root = Path(subprocess.run(
        ["git", "rev-parse", "--show-toplevel"], check=True, capture_output=True, text=True
    ).stdout.strip())
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else root / "scratch" / "code-index.txt"
    text = index_tree(root)
    out.parent.mkdir(parents=True, exist_ok=True)
    tmp = out.with_suffix(".tmp")
    tmp.write_text(text, encoding="utf-8")
    tmp.replace(out)
    print(f"{out}: {text.count(chr(10))} lines, {len(text)} chars")
```

The usage docstring preserves the original standalone tool's command shape; after
saving the recipe, invoke the actual owned project path, not a nonexistent installed
skill executable. Reading this reference runs no subprocess or source scan.
