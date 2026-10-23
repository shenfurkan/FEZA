# Skeletonizer Self-Check Recipe

## Contents

- [Scope](#scope)
- [Recipe](#recipe)

## Scope

These checks accompany the [skeletonizer recipe](skeletonizer.md). They are code
inside Markdown, not installed tests or evidence of an executed run. On an approved
test host, save the skeletonizer as `scripts/skeletonize.py` and the checks as
`tests/test_skeletonize.py` under one owned project directory, or adapt `SCRIPT` to
the actual saved file. Use the project's Python 3.12+ interpreter and test policy.

The implementation-heavy fixture's lexical/character ratio is a deliberately
limited regression condition, not an LLM-token-saving or scientific-performance claim.

## Recipe

```python
"""Skill-local tests of the actual script; no project or third-party imports."""

import ast
import contextlib
import importlib.util
import io
import re
import tempfile
import tokenize
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "skeletonize.py"
SPEC = importlib.util.spec_from_file_location("stingy_skeletonize", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class SkeletonTests(unittest.TestCase):
    def test_imports_signatures_annotations_and_docstrings(self):
        source = '''"""Module contract."""
from __future__ import annotations
from typing import Generic, TypeVar
import pathlib as paths
LIMIT: int = expensive_setup()
type Names[T] = list[T]

@register("demo")
class Worker[T](Base, metaclass=Meta):
    """Class contract."""
    size: int = 32

    @classmethod
    async def run(cls, x: int = 3, /, *args: str, flag: bool = True, **kw: object) -> str:
        """First line.
        Second line, including indentation.
        """
        import json
        local: str = compute()
        values = [str(x) for x in args]
        return json.dumps(values)
'''
        result = MODULE.skeletonize(source)
        original = ast.parse(source)
        skeleton = ast.parse(result)
        for before, after in zip(
            [n for n in ast.walk(original) if isinstance(n, (ast.Module, ast.ClassDef, ast.AsyncFunctionDef))],
            [n for n in ast.walk(skeleton) if isinstance(n, (ast.Module, ast.ClassDef, ast.AsyncFunctionDef))],
            strict=True,
        ):
            self.assertEqual(ast.get_docstring(before, clean=False), ast.get_docstring(after, clean=False))
        before = original.body[-1].body[-1]
        after = skeleton.body[-1].body[-1]
        for field in ("args", "returns", "decorator_list", "type_params"):
            value_before, value_after = getattr(before, field), getattr(after, field)
            if isinstance(value_before, list):
                self.assertEqual([ast.dump(n) for n in value_before], [ast.dump(n) for n in value_after])
            else:
                self.assertEqual(ast.dump(value_before), ast.dump(value_after))
        self.assertIn("import json", result)
        self.assertIn("LIMIT: int = ...", result)
        self.assertIn("local: str = ...", result)
        self.assertIn("type Names[T] = list[T]", result)
        self.assertNotIn("expensive_setup", result)
        self.assertNotIn("json.dumps", result)
        compile(result, "<skeleton>", "exec", dont_inherit=True)

    def test_exact_ranges_include_multiline_decorators_and_pruned_bodies(self):
        source = (
            "# preamble\n"                              # 1
            "import os\n"                               # 2
            "\n"                                        # 3
            "@decorate(\n"                              # 4
            "    'é',\n"                                # 5
            ")\n"                                       # 6
            "def café(\n"                               # 7
            "    x: str,\n"                             # 8
            ") -> str:\n"                               # 9
            "    result = x.strip()\n"                   # 10
            "    return result\n"                       # 11
        )
        result = MODULE.skeletonize(source)
        self.assertEqual(re.findall(r"\[Lines (\d+)-(\d+)\]", result), [("2", "2"), ("4", "11"), ("10", "11")])
        self.assertIn("# [Lines 4-11]\n@decorate", result)

    def test_nested_and_conditional_architecture_keeps_scope(self):
        source = '''if TYPE_CHECKING:
    from package import Interface
try:
    import optional
except ImportError:
    import fallback as optional
else:
    configure()
finally:
    cleanup()

def outer(flag):
    work()
    if flag:
        def inner(x: int) -> int:
            return x + 1
    else:
        class Alternate:
            enabled: bool = True
    for value in items:
        do_work(value)
    return inner
'''
        result = MODULE.skeletonize(source)
        tree = ast.parse(result)
        self.assertIsInstance(tree.body[0], ast.If)
        self.assertIsInstance(tree.body[1], ast.Try)
        outer = tree.body[2]
        self.assertEqual(outer.name, "outer")
        conditional = outer.body[1]
        self.assertIsInstance(conditional, ast.If)
        self.assertEqual(conditional.body[0].name, "inner")
        self.assertEqual(conditional.orelse[0].name, "Alternate")
        self.assertNotIn("do_work", result)
        self.assertNotIn("for value", result)
        compile(result, "<skeleton>", "exec", dont_inherit=True)

    def test_syntax_edge_cases(self):
        sources = [
            "", "# comments only\n", "def f(): return 1\n", "class C: pass\n",
            "def f():\n\t\"\"\"é\"\"\"\n\treturn 1\n",
            "def f(x=lambda a: a + 1):\n    return x()\n",
            "def f():\n    # type: () -> int\n    return 1\n",
            "x: list[int] = [1, 2]  # type: ignore[assignment]\n",
            "async def f():\n    async with context():\n        import package\n",
            "def f():\n    try:\n        work()\n    except* ValueError:\n        import handler\n",
            "match kind:\n    case {'name': name} if name:\n        def found(): pass\n    case _:\n        missing()\n",
            "while enabled:\n    import plugin\nelse:\n    stopped()\n",
            "class C:\n    def f(self):\n        def g():\n            nonlocal x\n            return x\n        x = 1\n        return g\n",
        ]
        for source in sources:
            with self.subTest(source=source):
                result = MODULE.skeletonize(source)
                ast.parse(result)
                compile(result, "<skeleton>", "exec", dont_inherit=True)

    def test_compression_on_explicit_implementation_heavy_fixture(self):
        source = 'def transform(value: int) -> int:\n    """Transform a value."""\n'
        source += "".join(f"    value = value + {i}\n" for i in range(100))
        source += "    return value\n"
        result = MODULE.skeletonize(source)

        def lexical_tokens(text):
            ignored = {tokenize.ENCODING, tokenize.ENDMARKER, tokenize.INDENT, tokenize.DEDENT, tokenize.NL, tokenize.NEWLINE}
            return sum(t.type not in ignored for t in tokenize.generate_tokens(io.StringIO(text).readline))

        # Synthetic regression floor, including annotation comments; not an LLM-token claim.
        self.assertGreaterEqual(lexical_tokens(source) / lexical_tokens(result), 10)
        self.assertGreaterEqual(len(source) / len(result), 5)
        self.assertNotIn("value = value", result)

    def test_tiny_modules_may_expand_and_output_is_deterministic(self):
        source = "import os\n"
        result = MODULE.skeletonize(source)
        self.assertGreater(len(result), len(source))
        self.assertEqual(result, MODULE.skeletonize(source))

    def test_cli_respects_encoding_and_never_executes_or_modifies_input(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "encoded.py"
            raw = '# coding: latin-1\r\n"""café"""\r\nraise RuntimeError("not executed")\r\n'.encode("latin-1")
            path.write_bytes(raw)
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                self.assertEqual(MODULE.main([str(path)]), 0)
            self.assertEqual(path.read_bytes(), raw)
            self.assertEqual(ast.get_docstring(ast.parse(output.getvalue())), "café")
            self.assertNotIn("RuntimeError", output.getvalue())

    def test_cli_errors_are_nonzero_with_no_partial_skeleton(self):
        with tempfile.TemporaryDirectory() as directory:
            broken = Path(directory) / "broken.py"
            broken.write_text("def broken(:\n", encoding="utf-8")
            encoded = Path(directory) / "encoded.py"
            encoded.write_bytes(b"# coding: utf-8\n\xff")
            for path in (broken, encoded, Path(directory) / "missing.py", Path(directory)):
                with self.subTest(path=path):
                    output, error = io.StringIO(), io.StringIO()
                    with contextlib.redirect_stdout(output), contextlib.redirect_stderr(error):
                        with self.assertRaises(SystemExit) as caught:
                            MODULE.main([str(path)])
                    self.assertEqual(caught.exception.code, 2)
                    self.assertEqual(output.getvalue(), "")
                    self.assertIn("error:", error.getvalue())


if __name__ == "__main__":
    unittest.main()
```
