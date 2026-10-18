# Install FEZA in Claude Code, OpenCode and Codex

FEZA contains Markdown instructions and Python recipes, not a server or Python
package. Its canonical skill source is `skills/feza/`. Claude Code can install it
through its native plugin manager; direct skill installation is an alternative.

## 1. Claude Code plugin

Enter each command as a separate message **inside Claude Code**:

```text
/plugin marketplace add shenfurkan/FEZA
```

```text
/plugin install feza@feza
```

The second command opens the plugin details. Review the entry, choose an install
scope and confirm. Use `/feza:feza` to invoke the installed skill; `/skills` lists
it and `/plugin` shows whether the plugin is enabled. If requested, run
`/reload-plugins` after installation.

This route needs no npx or separate Node.js installation. The root
`.claude-plugin/marketplace.json` lists the `feza` plugin; `.claude-plugin/plugin.json`
sets its name/version, and Claude Code scans `skills/` for the canonical skill.
FEZA declares no hooks, MCP servers, executables or plugin dependencies.

For a local clone, use `/plugin marketplace add ./feza` from its parent directory
(or `/plugin marketplace add ./` from the FEZA clone root), then the same install
command above. Keep a locally registered clone in place.

The equivalent commands in a regular terminal are:

```bash
claude plugin marketplace add shenfurkan/FEZA
claude plugin install feza@feza
```

The terminal install defaults to user scope. Use `--scope project` or
`--scope local` on `claude plugin install` if needed. Registering/installing a
plugin changes the client's marketplace/plugin settings; the FEZA manifests do
not add permission grants or project rules. These commands are instructions for
the user, not commands executed while preparing this repository.

## 2. OpenCode V2

FEZA uses OpenCode's native Agent Skill support, not an OpenCode runtime plugin.
The skill ID is the directory name `feza`; the existing `SKILL.md` and supporting
references work without a separate JavaScript package, hook or server.

### One-command installation

Run this in your terminal for a personal installation:

```bash
npx skills@1.7.2 add shenfurkan/FEZA --skill feza --agent opencode --global --copy
```

Vercel Labs' third-party installer writes to `~/.config/opencode/skills/feza/`.
It requires Node.js 22.20.0+. For a project-local install, run from that research
project's root and omit `--global`; this installer uses `.agents/skills/feza/`,
which V2 discovers as a compatibility location.

### Native configuration without npx

Clone into a new directory:

```bash
git clone https://github.com/shenfurkan/FEZA.git "$HOME/FEZA"
```

Add `~/FEZA/skills` to the `skills` array in your existing global
`~/.config/opencode/opencode.jsonc`. Create that config only if you do not already
have one; otherwise merge the entry and keep unrelated settings:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "skills": ["~/FEZA/skills"]
}
```

Keep the clone in place. Use an absolute or `~/` path for a shared clone: V2
resolves relative skill-source paths from the active working directory, not from
the config file. The canonical source is `skills/feza/SKILL.md`, not the entire
repository as an always-loaded instruction file.

### Direct folder discovery

Instead of a configured source, copy the complete `skills/feza/` directory to:

| Scope | Native OpenCode location |
|---|---|
| Project | `<research-project>/.opencode/skills/feza/` |
| Personal | `~/.config/opencode/skills/feza/` |

V2 also reads `.agents/skills/` and `.claude/skills/` compatibility locations.
Project discovery searches from the working directory to the project root.
Avoid defining `feza` in multiple locations: later sources can override earlier
ones, and explicit `skills` entries have higher precedence than discovered ones.

### Invoke and troubleshoot

Mention the skill in an OpenCode prompt:

```text
@feza Inspect data/spectrum_x1d.fits and preserve its units and DQ masks.
```

OpenCode advertises the ID, name and description, then loads the Markdown body
through its `skill` tool. Supporting reference contents are read only as needed.
It does not use Claude Code's `/plugin` manager or Codex's `$feza` syntax.

If a running instance does not discover a changed configuration, run
`opencode reload` from your normal terminal. If the skill is still absent, check
the `feza/SKILL.md` path, description, duplicate IDs and the active agent's
`skill` permission for resource `feza`. A deny rule can hide the skill. FEZA does
not change permissions; review only the relevant rule instead of granting all
tools access.

These instructions target the [official V2 skill format](https://opencode.ai/v2/docs/skills/).
Do not add FEZA to `plugins` as though it were an executable OpenCode plugin.

## 3. Direct skill installation reference

Use one installation method, not both a plugin and a direct copy. Direct skill
locations and commands differ from the namespaced plugin command:

| Client | Project location | Personal location | Explicit invocation |
|---|---|---|---|
| Claude Code (direct skill) | `.claude/skills/feza/` | `~/.claude/skills/feza/` | `/feza`; list with `/skills` |
| OpenCode V2 (native skill) | `.opencode/skills/feza/` | `~/.config/opencode/skills/feza/` | Mention `@feza` |
| Codex CLI / IDE extension | `.agents/skills/feza/` | `~/.agents/skills/feza/` | `$feza`; select with `/skills` |
| Other Agent Skills clients | Follow that client's documented discovery configuration | Client-specific | Client-specific |

`skills/feza/` is the canonical **source layout**, not a universal automatic
discovery path. Direct skill copying requires no permission or rules-file changes.
Only the skill directory is needed. Developer bibliographies, the local literature
collection and repository instructions are not installation requirements.

### With npx

The following commands use Vercel Labs' third-party `skills` CLI **1.7.2**, whose
published Node requirement is **>=22.20.0**. FEZA has no npm package named `feza`.
Review the source and existing installed skills before enabling it. `--copy` avoids
symlink permission issues and keeps the installed reference files together.

#### Personal install: available in all projects on this machine

After the independent GitHub repository is published and accessible:

```bash
npx skills@1.7.2 add shenfurkan/FEZA --skill feza --agent claude-code --global --copy
```

The Claude Code destination is `~/.claude/skills/feza/`. On Windows this is under
your user profile. Do not put a manually installed skill under the managed `synced/`
directory; account synchronization owns those files.

The same npx command can be used in PowerShell.

#### Project install

Run this **from your research project's root**, without `--global`:

```bash
npx skills@1.7.2 add shenfurkan/FEZA --skill feza --agent claude-code --copy
```

Claude Code reads the result at `.claude/skills/feza/SKILL.md` in that project.
Inspect any files/lock records the third-party installer adds before committing them.
FEZA does not edit `CLAUDE.md`, settings, permissions, MCP configuration or hooks.

#### Install from an existing local clone

From this independent FEZA repository's root:

```bash
npx skills@1.7.2 add ./skills/feza --skill feza --agent claude-code --global --copy
```

This avoids a FEZA GitHub download, but npx may still download the installer from
npm. It is not an offline guarantee. Check an existing `feza` destination instead
of silently replacing it; the examples above deliberately retain confirmation prompts.

### Git clone without npm

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
The npx commands above target **Claude Code**; use `--agent codex` for Codex.

## 4. Confirm Claude Code discovery

For a plugin installation, use `/plugin` to check that `feza@feza` is enabled and
`/skills` to find `/feza:feza`. The checks below describe a direct skill copy.

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

Replace the path with an existing Python module in your project. Direct source
reads need no AST map. If a richer map is useful, the optional AST recipe uses
Python 3.12+ and only its standard library; no Astropy or network is needed.

Current Claude Code watches skill directories. If the top-level skills directory
did not exist when the session started, run `/reload-skills`, or restart Claude Code.
If it still does not appear, check the installed path, frontmatter, duplicate `feza`
names, settings sources and organization policy. FEZA does not override those controls.

Discovery is not proof that the analysis examples ran or produced valid science.
This setup was inspected against the documentation; no Claude account/client session
was installed or exercised by preparing this repository.

## 5. Claude.ai / Cowork account skills

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

## 6. Publication and updates

The intended independent remote is `https://github.com/shenfurkan/FEZA.git`.
Configuring a local Git remote does not create that repository or publish any files.
The GitHub commands require the repository to be accessible and to contain this
layout; private repositories additionally require the user's normal Git credentials.
Never paste a token into a command, URL or skill file.

For a plugin installation, use **Update now** in the Installed tab of `/plugin`,
or run this from your terminal:

```bash
claude plugin update feza@feza
```

Apply `/reload-plugins` if Claude Code requests it. Plugin updates and direct-skill
updates are separate; keep using the mechanism that installed your copy.

For OpenCode using a configured local clone, review changes and run
`git pull --ff-only` in that clone, then `opencode reload` from your normal
terminal. For an npx-installed OpenCode copy, re-run the explicitly targeted
OpenCode install command with the same scope and `--copy`; there is no FEZA
runtime plugin to update with `opencode plugin update`.

For an npx-installed copy, review the upstream changes and existing destination,
then re-run the same explicitly targeted installation command. Keep the prompts
and the original agent/copy choices:

```bash
npx skills@1.7.2 add shenfurkan/FEZA --skill feza --agent claude-code --global --copy
```

Do not use the installer's broad `update` command as a targeted FEZA update; its
destination/confirmation behavior can differ from the original install. Omit
`--global` above only for an originally project-local installation.

For a Git-linked install, review and pull changes in that independent clone using
`git pull --ff-only`. No updater is executed automatically by FEZA.

## 7. Removal

- **Claude Code plugin:** open `/plugin`, select FEZA on the Installed tab and
  choose **Uninstall**. In the terminal, use `claude plugin uninstall feza@feza`;
  target the same scope used at installation when passing `--scope`.
- **npx installation:** remove the skill for the selected client and scope, keeping
  confirmation prompts. For a personal OpenCode copy:

  ```bash
  npx skills@1.7.2 remove feza --agent opencode --global
  ```

  Use `--agent claude-code` or `--agent codex` for those clients; omit `--global`
  only for a project-local copy. Do not use a broad remove-all command.
- **Configured OpenCode source:** remove only the FEZA entry from the `skills`
  array, preserving the rest of the configuration, then run `opencode reload`.
- **Manual copy or symlink:** remove only the installed `feza` directory/link in
  the discovery location. Keep your research project, generated analysis and source
  clone unless you separately intend to delete them.

## Documentation basis

- [Claude Code skill locations, invocation and live changes](https://code.claude.com/docs/en/skills).
- [Claude Code marketplace creation](https://code.claude.com/docs/en/plugins/create-marketplace).
- [Claude Code marketplace reference](https://code.claude.com/docs/en/plugins/marketplace-reference).
- [Claude Code plugin manifest reference](https://code.claude.com/docs/en/plugins/manifest-reference).
- [Claude Code plugin installation and updates](https://code.claude.com/docs/en/plugins/install).
- [OpenCode V2 skill discovery, sources and invocation](https://opencode.ai/v2/docs/skills/).
- [OpenCode V2 configuration](https://opencode.ai/v2/docs/config/).
- [OpenCode V2 permissions](https://opencode.ai/v2/docs/permissions/).
- [OpenCode V2 CLI commands, including reload](https://opencode.ai/v2/docs/cli/commands/).
- [OpenCode V2 runtime plugins](https://opencode.ai/v2/docs/build/plugins/).
- [Codex local skill locations and invocation](https://developers.openai.com/codex/build-skills).
- [Vercel Labs skills 1.7.2 README](https://github.com/vercel-labs/skills/blob/v1.7.2/README.md).
- [skills 1.7.2 npm metadata](https://registry.npmjs.org/skills/1.7.2).
- [Agent Skills specification](https://agentskills.io/specification).
- [Claude custom-skill ZIP guidance](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills).

Original installation basis inspected 2026-10-13; Claude Code/Codex discovery
guidance rechecked 2026-10-15; OpenCode V2 guidance checked 2026-10-16. These establish
a documented installation route, not an
executed installer/client integration or scientific validation.
