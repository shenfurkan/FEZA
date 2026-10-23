"""Check repository metadata, Markdown links and syntax without running recipes."""
import ast
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit

if sys.version_info < (3, 12):
    raise SystemExit("Use Python 3.12 or newer for the documented Python grammar.")

root = Path(__file__).resolve().parents[1]
skill = root / "skills/feza"
skill_dirs = sorted(path.parent for path in (root / "skills").glob("*/SKILL.md"))
errors = []
counts = Counter()


def distribution_boundary(path):
    return next((directory for directory in skill_dirs if path.is_relative_to(directory)), root)


def input_path(path):
    boundary = distribution_boundary(path)
    resolved = path.resolve()
    if not resolved.is_relative_to(boundary):
        label = str(path.relative_to(root)) if path.is_relative_to(root) else "external input"
        errors.append(f"{label}: input escapes its distribution")
        return None
    return resolved


def read_input(path, *, binary=False):
    resolved = input_path(path)
    if resolved is None:
        return None
    try:
        return resolved.read_bytes() if binary else resolved.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        errors.append(f"{path.relative_to(root)}: input unavailable: {exc}")
        return None


def read_json(path):
    text = read_input(path)
    if text is None:
        return None
    try:
        result = json.loads(text)
    except ValueError as exc:
        errors.append(f"{path.relative_to(root)}: {exc}")
        return None
    counts["json_files_parsed"] += 1
    return result


def markdown_parts(text, path):
    prose, blocks, body = [], [], []
    fence = None
    for number, line in enumerate(text.split("\n"), 1):
        if fence is None:
            match = re.match(r"^( {0,3})(`{3,}|~{3,})(.*)$", line)
            if match:
                indent, marker, info = match.groups()
                language = info.strip().split()[0] if info.strip() else ""
                fence = (len(indent), marker, language, number)
                body = []
                continue
            prose.append(line)
        else:
            indent, marker, language, start = fence
            if re.fullmatch(r" {0,3}" + re.escape(marker[0]) +
                            "{" + str(len(marker)) + r",}[ \t]*", line):
                blocks.append((language, start + 1, "\n".join(body) + "\n"))
                fence = None
            else:
                margin = min(indent, len(line) - len(line.lstrip(" ")))
                body.append(line[margin:])
    if fence is not None:
        errors.append(f"{path.relative_to(root)}: unclosed code fence")
    return "\n".join(prose), blocks


def anchors(text):
    result, seen = set(), Counter()
    for heading in re.findall(r"^#{1,6}\s+(.+?)\s*#*\s*$", text, re.M):
        heading = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", heading)
        base = re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
        number = seen[base]
        seen[base] += 1
        result.add(base if number == 0 else f"{base}-{number}")
    result.update(re.findall(r'<a\s+(?:id|name)="([^"]+)"', text))
    return result


files = [root / "README.md", root / "INSTALLATION.md"]
for directory in (root / "docs", root / "evals", *skill_dirs):
    if input_path(directory) is not None:
        files += sorted(directory.rglob("*.md"))
texts = {}
for path in files:
    text = read_input(path)
    if text is not None:
        texts[path] = text
parts = {path: markdown_parts(text, path) for path, text in texts.items()}
anchor_cache = {path: anchors(prose) for path, (prose, _) in parts.items()}
counts["markdown_files"] = len(texts)

for path, text in texts.items():
    relative = path.relative_to(root)
    prose, blocks = parts[path]
    if path.parent.name == "references" and len(text.split("\n")) > 100:
        if "## Contents" not in prose:
            errors.append(f"{relative}: missing Contents")
    for language, start, source in blocks:
        origin = f"{relative}:{start}"
        try:
            if language == "python":
                ast.parse(source, filename=origin, feature_version=(3, 12))
                compile(source, origin, "exec", dont_inherit=True)
                counts["python_fences_compiled"] += 1
            elif language == "json":
                json.loads(source)
                counts["json_fences_parsed"] += 1
            elif language == "bash":
                result = subprocess.run(["bash", "-n"], input=source, text=True,
                                        capture_output=True, timeout=5)
                counts["bash_fences_checked"] += 1
                if result.returncode:
                    errors.append(f"{origin}: {result.stderr.strip()}")
        except (OSError, ValueError, SyntaxError, subprocess.TimeoutExpired) as exc:
            errors.append(f"{origin}: check unavailable or failed: {exc}")
    for match in re.finditer(r"(?<!!)\[[^]]+\]\(([^)\s]+)\)", prose):
        link = match[1]
        if urlsplit(link).scheme or link.startswith("//"):
            continue
        destination, _, anchor = link.partition("#")
        target = (path.parent / unquote(destination)).resolve() if destination else path
        counts["relative_links_checked"] += 1
        boundary = distribution_boundary(path)
        if not target.is_relative_to(boundary):
            errors.append(f"{relative}: link escapes its distribution: {link}")
            continue
        if not target.exists():
            errors.append(f"{relative}: missing target {link}")
        elif anchor and target.suffix == ".md":
            if target not in anchor_cache or unquote(anchor) not in anchor_cache[target]:
                errors.append(f"{relative}: missing or unchecked anchor {link}")
    if path.is_relative_to(skill) and re.search(
            r"(?<![\w])literature/|sources\.md|STRICTLY FORBIDDEN|local-primary-source rule", text):
        errors.append(f"{relative}: developer bibliography/rule leaked into the skill")

for directory in skill_dirs:
    entrypoint = texts.get(directory / "SKILL.md", "")
    header = re.match(r"\A---\n(.*?)\n---\n", entrypoint, re.S)
    if not header:
        errors.append(f"{directory.relative_to(root)}: missing frontmatter")
        continue
    if not re.search(r"^name: " + re.escape(directory.name) + r"$", header[1], re.M):
        errors.append(f"{directory.relative_to(root)}: name/directory mismatch")
    description = re.search(r"^description: (.+)$", header[1], re.M)
    if not description or not 0 < len(description[1].strip("\"'")) < 1024:
        errors.append(f"{directory.relative_to(root)}: missing or oversized description")
    if len(entrypoint[header.end():].splitlines()) >= 500:
        errors.append(f"{directory.relative_to(root)}: skill body must be below 500 lines")
    if not (directory / "LICENSE").is_file():
        errors.append(f"{directory.relative_to(root)}: missing license")
    if (directory / "evals").exists():
        errors.append(f"{directory.relative_to(root)}: evaluator material inside installed skill")
    for path in directory.rglob("*"):
        if path.is_file() and path.suffix in {".py", ".sh", ".js", ".ts"}:
            errors.append(f"{path.relative_to(root)}: executable source must be a Markdown recipe")
    counts["skill_entrypoints_checked"] += 1

tools = root / "tools"
if input_path(tools) is not None:
    for path in sorted(tools.glob("*.py")):
        text = read_input(path)
        if text is not None:
            compile(text, str(path), "exec", dont_inherit=True)
            counts["development_scripts_compiled"] += 1

version = (read_input(root / "VERSION") or "").strip()
if not version:
    errors.append("VERSION: missing or empty")
entrypoint = texts.get(skill / "SKILL.md", "")
frontmatter = re.match(r"\A---\n(.*?)\n---\n", entrypoint, re.S)
if not frontmatter:
    errors.append("SKILL.md: missing frontmatter")
else:
    if not re.search(r"^name: feza$", frontmatter[1], re.M):
        errors.append("SKILL.md: name/directory mismatch")
    if f'  version: "{version}"' not in frontmatter[1]:
        errors.append("SKILL.md: version mismatch")
for path in (root / "README.md", skill / "README.md"):
    if version not in texts.get(path, ""):
        errors.append(f"{path.relative_to(root)}: version missing")
for path in (root / "LICENSE.txt", skill / "LICENSE"):
    resolved = input_path(path)
    if resolved is not None and not resolved.is_file():
        errors.append(f"{path.relative_to(root)}: missing license")

# Grading material stays outside the installed skill so candidates cannot read answers.
if (skill / "evals").exists():
    errors.append("skills/feza/evals: evaluator material must live in the repository evals/")
for filename in ("evals.json", "trigger_evals.json"):
    parsed = read_json(root / "evals" / filename)
    if parsed is None:
        continue
    if filename == "evals.json":
        cases = parsed["evals"]
        if [case["id"] for case in cases] != list(range(1, len(cases) + 1)):
            errors.append("evals: nonsequential case IDs")
        for case in cases:
            for item in case["files"]:
                target = input_path(root / item)
                if target is not None and not target.is_file():
                    errors.append(f'eval {case["id"]}: missing fixture {item}')
        counts["declared_cases"] = len(cases)
for case_dir in sorted(path.parent for path in (root / "evals").glob("*/prompt.md")):
    if not any((case_dir / "graders").glob("*.md")):
        errors.append(f"{case_dir.relative_to(root)}: plugin-eval case without graders")
    counts["plugin_eval_cases"] += 1

marketplace = read_json(root / ".claude-plugin/marketplace.json")
plugin = read_json(root / ".claude-plugin/plugin.json")
if marketplace is not None and plugin is not None:
    if marketplace.get("name") != "feza" or not marketplace.get("owner", {}).get("name"):
        errors.append("marketplace: name/owner missing or inconsistent")
    entries = marketplace.get("plugins", [])
    if len(entries) != 1 or entries[0].get("name") != "feza":
        errors.append("marketplace: expected one feza entry")
    elif (root / entries[0].get("source", "")).resolve() != root:
        errors.append("marketplace: expected root-local source")
    if plugin.get("name") != skill.name or plugin.get("version") != version:
        errors.append("plugin: name/version mismatch")
    if any(key in plugin for key in ("hooks", "mcpServers", "dependencies", "commands")):
        errors.append("plugin: unexpected executable components")
    counts["plugin_metadata_checked"] = 2

print(json.dumps({"scope": "static only; no recipes or tests executed",
                  "python": sys.version.split()[0], "grammar": "Python 3.12",
                  "counts": dict(counts), "errors": errors}, indent=2))
raise SystemExit(bool(errors))
