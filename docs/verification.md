# FEZA 0.0.1 — verification scope

Preparation date: 2026-10-15; client integration updated 2026-10-16. This is a
development record, not installed skill content, independent approval, NASA
certification or scientific validation.

## Intended use and authority

The deliverable is a Markdown assistant skill for astronomy analysis and read-only
Python navigation, not flight/control software or an executable analysis package.
No NASA software class is assigned to users merely because they install it. A
generated consequential analysis needs its own intended-use/classification and
criticality decision. Source maps do not establish physical truth or code behavior.

For the initial preparation pass below, the operator requested first-version
preparation, declined behavior tests and had not authorized installation, commits,
pushes or publication. The later removal and entrypoint revision are recorded
separately. Human release acceptance is pending; the authoring agent cannot supply
independent sign-off.

## Historical evidence inspected, not rerun

| Evidence | Exact recorded outcome | Scope and limits |
|---|---|---|
| Mechanical development run, 2026-10-15 15:32:59–15:33:01 UTC | 40 checks passed, 0 failed | Earlier cases 9/13/14; Python 3.13.15, Astropy 8.0.1, NumPy 2.5.4; synthetic only |
| Earlier with-skill agent round, cases 10–13 | 15/15 expectations met | Same model family and session-agent grading; rubric removed in round 2 |
| Earlier without-skill comparison | 14/15 expectations met | Both configurations inherited overlapping repository instructions; not a context-free baseline |
| Earlier `skills-ref validate skills/feza` | `Valid skill: skills/feza`, exit 0 | Frontmatter/naming only, before this preparation pass |

Retained historical records were read at:

- `/tmp/opencode/feza-eval-kaggle/run_local_20261015T153257Z.log`
- `/tmp/opencode/feza-eval-agent/agent_eval_report.md`
- `/tmp/opencode/feza-eval-agent/baseline_benchmark.md`

These local artifacts are not bundled with the skill or guaranteed available in a
clone. They are historical development evidence, not a repeatable release test
system. Round 1 of the agent exercise exposed its rubric and is excluded. Later
prompt/expectation edits, including the navigation-reporting expectation, invalidate
carrying the old denominator forward as a current score.

## Initial preparation pass

- Read-only reviews covered AST pruning/source ranges, navigation scope, package
  portability and installation commands. Confirmed defects were repaired in source.
- Skeleton repairs address non-newline separators in retained type comments and
  parenthesized-decorator start lines. Focused qualified-name lookup rejects
  unknown/ambiguous definitions; rendered maps check AST structure and label
  collisions. These protections are source changes, not behavior-test results.
- Development bibliography and local collection paths moved out of the skill into
  `docs/sources.md`; installed users do not inherit the developer download rule.
- The entrypoint routes navigation separately from scientific acceptance/reporting.
- The report step now explicitly limits physical acceptance comparisons to
  interpreted scientific results, not code-only work. The standards crosswalk
  names related practices/project responsibilities rather than claiming counted
  requirement coverage from installed instructions.
- Behavioral cases 10–13 now point to input-only `scenarios.md`; their expectations
  remain evaluator-side. Known-answer numerical controls remain development aids,
  not candidate instructions or held-out evidence. No new comparison was run.
- Claude Code marketplace/plugin manifests were added without executable hooks or
  duplicate skill sources. `claude plugin validate .` and
  `claude plugin validate .claude-plugin/plugin.json` both returned
  `Validation passed`, exit 0. These are local metadata checks, not installations.
- OpenCode V2 documentation was reviewed for native skill discovery, `skills`
  source arrays, `@feza`, permissions and reload. README/installation instructions
  now distinguish its Markdown skill support from its executable plugin API.
  No OpenCode or Claude Code user configuration was changed during preparation.
- Static verification covers portable frontmatter/version consistency, JSON and
  mirror consistency, Markdown paths/anchors and embedded-Python compilation.
- No embedded recipe, analysis, observation, network query, client install or
  scientific numerical pipeline is executed by these static checks.
- Current behavior tests, benchmarks, new with/without-skill trials and automated
  description optimization were **not run**, per operator direction.
- Static checks are now reproducible from a clone with `python3 tools/validate.py`,
  without the ignored literature collection. The GitHub workflow is manual-only;
  no remote job was started. The tool checks this repository's formatting and
  metadata conventions; it is not a complete Markdown/YAML/client validator.

### Static outcomes for that preparation pass

The repository's `tools/validate.py` ran with Python 3.14.4; it did not import or
execute any fenced recipe or fixture. It replaces the local `/tmp`-only checker
and includes indented fences that earlier syntax counts omitted. Results:

| Static check | Outcome |
|---|---|
| Markdown files inspected | 17 |
| Python fences parsed with Python 3.12 grammar and compiled for syntax | 28, no syntax errors |
| Development scripts compiled without importing | 1, no syntax errors |
| Bash fences checked with `bash -n` | 18, no syntax errors |
| JSON configuration examples parsed | 2, valid JSON; V2 field shapes reviewed against official documentation |
| Relative paths/anchors checked | 102, no missing targets/anchors or links outside their distribution boundaries |
| Canonical eval JSON parsed / byte-identical mirrors | 2 / 2; 14 declared cases |
| Claude Code marketplace and plugin manifests | Both passed `claude plugin validate`, CLI 2.1.300; name/version/source consistency also checked |
| Development literature files indexed separately (not needed in a clone) | 78/78 |
| Entrypoint metadata and version consistency | Matched `feza` / `0.0.1` |
| Earlier read-only reviews | No blockers reported within skeleton/earlier-documentation scope; not client-integration tests |

The official `skills-ref` validator was not rerun in this pass; frontmatter fields
and version were unchanged, and their consistency was checked statically without
installing tools. PowerShell examples were reviewed as text, not executed or
syntax-checked with PowerShell. No installed-client acceptance is implied.

Compilation is syntax evidence, not execution evidence; the historical 40/40 is
**not** acceptance of the revised skeleton. No coverage percentage, model-token
reduction or superiority over other skills is asserted.

## Entrypoint simplification — 2026-10-16

The operator authorized removing the global FEZA skill and simplifying its source,
with reinstallation deferred. No commit, push, release or reinstallation was made.
The global installer reported removal but retained its shared copy and lock entry;
the copy was compared byte-for-byte with the unchanged repository skill before
explicit removal. The entry was removed without changing other lock settings;
neither global skill path remained and OpenCode stopped advertising `feza`.

- Task routing now precedes process guidance. The entrypoint changed from 130 to
  104 lines and 1,134 to 867 whitespace-delimited words, not measured model tokens.
- Routine code/inspection/navigation work explicitly returns useful output rather
  than classification forms, physical-result checks or a full scientific report.
- The claim/evidence table moved unchanged to the standards reference. Scientific
  integrity, input preservation, permission and consequential-work boundaries
  remain; standards crosswalk labels no longer depend on workflow step numbers.
- Case 5 gained a code-only response expectation; both eval mirrors match. This
  is a regression specification, not an executed behavioral result.

Static verification used `/usr/bin/python3` 3.14.4, Python 3.12 grammar and Bash
5.3.9. `/usr/bin/python3 tools/validate.py` returned exit 0: 17 Markdown files,
109 relative links, 28 Python fences, 18 Bash fences, 2 JSON fences, 1 development
script, 4 JSON files, 2 mirror pairs, 14 declared cases and 2 plugin metadata
records; no errors. `git diff --check` returned exit 0. No recipes, scientific
computations, tests, benchmarks or comparison agents ran.

Evidence recorded at `2026-10-15T21:42:17Z` (2026-10-16 operator-local date), against
base commit `54b895622d22c7be5264c81df80fdf427ffd4ad1`. SHA-256 configuration items:

| Item | SHA-256 |
|---|---|
| `skills/feza/SKILL.md` | `ce31bd351bfb074859f0cfdfe916cfd1e8a984cafb5bb422b43b78d018951a24` |
| `skills/feza/references/standards.md` | `4755a8114a2d0e36355be435491d1ce5e7089e71d5997c34fbce6c2cbb79a17c` |
| `skills/feza/evals/evals.json` and its root mirror | `f76686de180f83b74ece3ed3fb1eb34416cd573157c38dff30b47d8e7d30c13b` |
| `tools/validate.py` | `b5eea4f3e9222c53f10a7bcbd48792a02d18f73a0c88b417b2d4ee3b2469e386` |
| `/usr/bin/python3` | `52e0a13e60a981d8c4b6478be2ba5176f69da07948a056bf49cf6f077e30cb41` |
| `/usr/bin/bash` | `3efccc187bafa75ff1e37d246270ab3e7aa559f242c7a52bf3ec2a1b5450bdbd` |

Reduced text and successful static checks do not establish better agent behavior.
The competing explanation is that agents still over-apply process, or miss detail
now behind a reference link. The next bounded assessment is an authorized
clean-context comparison of code-only case 5 and consequential-use case 10.

## Unresolved release risks

- Native-data cases 1–8 still need supplied inputs and independent expectations.
- The revised AST map and its source-range edge cases remain behaviorally untested.
- Claude Code/Codex install and discovery commands are documented, not exercised.
- NASA-HDBK-7009B's retained copy has approved-cover/draft-header inconsistency;
  NASA-HDBK-2203's PDF is only a landing-page stub. Neither is silently upgraded to
  final primary authority; the source index preserves both limitations.
- No held-out multi-model comparison or independent human scientific review exists.

For broader acceptance, the next bounded check is an authorized stdlib-only
skeleton regression pass, followed separately by one clean-workspace client smoke
check. Neither is required to deliver source under the operator's static-only scope.
