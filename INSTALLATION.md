# Install FEZA in Claude and Agent Skills Environments

FEZA is a **100% pure-Markdown Agent Skill**, not a server, model fine-tune or
Python package. Its canonical location in this repository is `skills/feza/`.
Install its complete directory in the chosen client's discovery location below.
Agents then write native, self-contained Astropy code in the user's project.

| Client | Project location | Personal location | Explicit invocation |
|---|---|---|---|
| Claude Code | `.claude/skills/feza/` | `~/.claude/skills/feza/` | `/feza`; list with `/skills` |
| Codex CLI / IDE extension | `.agents/skills/feza/` | `~/.agents/skills/feza/` | `$feza`; select with `/skills` |
| Other Agent Skills clients | Follow that client's documented discovery configuration | Client-specific | Client-specific |

`skills/feza/` is the canonical **source layout**, not a universal automatic
discovery path. No client settings or permissions are changed by these instructions.
Only the skill directory is needed. Developer bibliographies, the local literature
collection and repository instructions are not installation requirements.

## 1. Claude Code with npx

The following commands use Vercel Labs' third-party `skills` CLI **1.7.2**, whose
published Node requirement is **>=22.20.0**. FEZA has no npm package named `feza`.
Review the source and existing installed skills before enabling it. `--copy` avoids
symlink permission issues and keeps the installed reference files together.

### Personal install: available in all projects on this machine

After the independent GitHub repository is published and accessible:

```bash
DISABLE_TELEMETRY=1 npx skills@1.7.2 add shenfurkan/FEZA --skill feza --agent claude-code --global --copy
```

The Claude Code destination is `~/.claude/skills/feza/`. On Windows this is under
your user profile. Do not put a manually installed skill under the managed `synced/`
directory; account synchronization owns those files.

For PowerShell, set the telemetry flag separately:

```powershell
$env:DISABLE_TELEMETRY = "1"
npx skills@1.7.2 add shenfurkan/FEZA --skill feza --agent claude-code --global --copy
```

### Project install

Run this **from your research project's root**, without `--global`:

```bash
DISABLE_TELEMETRY=1 npx skills@1.7.2 add shenfurkan/FEZA --skill feza --agent claude-code --copy
```

Claude Code reads the result at `.claude/skills/feza/SKILL.md` in that project.
Inspect any files/lock records the third-party installer adds before committing them.
FEZA does not edit `CLAUDE.md`, settings, permissions, MCP configuration or hooks.

### Install from an existing local clone

From this independent FEZA repository's root:

```bash
DISABLE_TELEMETRY=1 npx skills@1.7.2 add ./skills/feza --skill feza --agent claude-code --global --copy
```

This avoids a FEZA GitHub download, but npx may still download the installer from
npm. It is not an offline guarantee. Check an existing `feza` destination instead
of silently replacing it; the examples above deliberately retain confirmation prompts.

## 2. Git clone without npm

Clone the independent published repository into a new directory:

```bash
git clone https://github.com/shenfurkan/FEZA.git feza && cd feza
```

In Bash on Linux, macOS or WSL, create a personal link without replacing an existing
file, directory or even a dangling symlink:

```bash
target="$HOME/.claude/skills/feza"
if [ ! -f "$PWD/skills/feza/SKILL.md" ]; then
    echo "Run this from the inspected FEZA clone root." >&2
elif [ -e "$target" ] || [ -L "$target" ]; then
    echo "FEZA destination exists; inspect it before changing anything." >&2
else
    mkdir -p "$HOME/.claude/skills" && ln -s "$PWD/skills/feza" "$target"
fi
```

Claude Code documents symlinked skill folders. Keep the clone in place while using
the link. Pulling reviewed changes updates the linked skill; independent npx `--copy`
installs do not follow that clone automatically.

On Windows, or when symlinks are unavailable, copy only the complete `skills/feza`
directory to your personal skills directory. PowerShell example from the clone root:

```powershell
$ErrorActionPreference = "Stop"
if (-not (Test-Path -LiteralPath "skills/feza/SKILL.md" -PathType Leaf)) {
    throw "Run this from the inspected FEZA clone root."
}
$target = Join-Path $HOME ".claude/skills/feza"
if ($null -ne (Get-Item -LiteralPath $target -Force -ErrorAction SilentlyContinue)) {
    throw "FEZA destination exists; inspect it before changing anything."
}
New-Item -ItemType Directory -Force (Join-Path $HOME ".claude/skills") | Out-Null
Copy-Item -LiteralPath "skills/feza" -Destination $target -Recurse
```

For a project-local manual installation, copy/link the same directory to
`.claude/skills/feza/` for Claude Code, or `.agents/skills/feza/` for Codex, inside
the research project. Do not copy the whole FEZA repository. For Codex, select FEZA
with `/skills` or mention `$feza`; restart that client if changes are not discovered.
The commands in section 1 target **Claude Code**, not every client.

## 3. Confirm Claude Code can discover it

The resulting directory must contain `feza/SKILL.md`, `references/`, `assets/` and
`LICENSE` together. The frontmatter's `name` is `feza`, matching its directory.
The root `README.md`, `docs/`, `literature/` and local `AGENTS.md` are not part of
the install. `evals/` contains development specifications and can be omitted from
a manually prepared distribution; ordinary use does not load it.

1. In Claude Code, run `/skills` and check for FEZA.
2. Invoke `/feza Inspect this FITS product and preserve its units and quality masks`.
3. Or ask an applicable astronomy question normally; Claude may select the skill
   from its description and load only the relevant references.

For a data-free first request, try:

```text
/feza Map src/analysis.py without importing it. Show original ranges and read
the function relevant to my question; do not run the analysis.
```

Replace the path with an existing Python module in your project. The AST recipe
uses Python 3.12+ and only its standard library; no Astropy or network is needed.

Current Claude Code watches skill directories. If the top-level skills directory
did not exist when the session started, run `/reload-skills`, or restart Claude Code.
If it still does not appear, check the installed path, frontmatter, duplicate `feza`
names, settings sources and organization policy. FEZA does not override those controls.

Discovery is not proof that the analysis examples ran or produced valid science.
This setup was inspected against the documentation; no Claude account/client session
was installed or exercised by preparing this repository.

## 4. Claude.ai / Cowork account skills

Create or obtain a reviewed ZIP archive of `skills/feza/`, then upload it in
**Customize > Skills** when the feature and code execution are available for your
account/organization. Upload the ZIP containing **one top-level `feza/` folder**,
not a GitHub source ZIP with the entire repository.

The portable frontmatter has only `name`, `description`, `license` and `metadata.version`; the description
is also kept below the help article's 200-character limit. Account upload/activation
is separate from a filesystem install. Cowork/cloud sessions do not simply read
your machine's personal `~/.claude/skills/`. Local skill edits are not uploads to
claude.ai; synchronized copies should be managed through the account interface.

FEZA does not create an account, enable code execution, change organization policy
or guarantee that a particular account exposes custom-skill upload. No upload or
account acceptance test is claimed here.

## 5. Publication and updates

The intended independent remote is `https://github.com/shenfurkan/FEZA.git`.
Configuring a local Git remote does not create that repository or publish any files.
The GitHub commands require the repository to be accessible and to contain this
layout; private repositories additionally require the user's normal Git credentials.
Never paste a token into a command, URL or skill file.

For an npx-installed copy, review the upstream changes and existing destination,
then re-run the same explicitly targeted installation command. Keep the prompts
and the original agent/copy choices:

```bash
DISABLE_TELEMETRY=1 npx skills@1.7.2 add shenfurkan/FEZA --skill feza --agent claude-code --global --copy
```

Do not use the installer's broad `update` command as a targeted FEZA update; its
destination/confirmation behavior can differ from the original install. Omit
`--global` above only for an originally project-local installation.

For a Git-linked install, review and pull changes in that independent clone using
`git pull --ff-only`. No updater is executed automatically by FEZA.

## Documentation basis

- [Claude Code skill locations, invocation and live changes](https://code.claude.com/docs/en/skills).
- [Codex local skill locations and invocation](https://developers.openai.com/codex/build-skills).
- [Vercel Labs skills 1.7.2 README](https://github.com/vercel-labs/skills/blob/v1.7.2/README.md).
- [skills 1.7.2 npm metadata](https://registry.npmjs.org/skills/1.7.2).
- [Agent Skills specification](https://agentskills.io/specification).
- [Claude custom-skill ZIP guidance](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills).

Original installation basis inspected 2026-10-13; Claude Code/Codex discovery
guidance rechecked 2026-10-15. These establish a documented installation route, not an
executed installer/client integration or scientific validation.
