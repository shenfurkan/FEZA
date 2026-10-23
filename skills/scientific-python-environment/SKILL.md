---
name: scientific-python-environment
description: "Use when scientific Python runs with the wrong interpreter, kernel, package import or incompatible dependency stack, or when changing dependencies, optional engines and package layout. Trace the actual runtime and scientific consumer, repair the narrow environment defect, and verify imports plus relevant numerical behavior. Do not impose one project's Python version, package manager or lock format, or confuse installation success with physical validity."
---

# Scientific Python Environment

Make the requested scientific calculation run in the intended, identifiable
environment. Diagnose the concrete runtime failure; do not replace scientific
work with an unsolicited packaging, pinning or environment-audit campaign.

## Identify the interpreter that actually executes the calculation

Read the existing environment definition, supported Python versions, dependency
groups and launch command. Inspect the actual consumer: terminal entry point,
notebook kernel, test subprocess, worker or approved remote session. An activated
shell environment does not establish which interpreter a notebook or child uses.

Use the project's declared command runner and interpreter. Diagnose relevant facts
from inside that same process when necessary:

- `sys.executable`, `sys.version` and the platform of the failing runtime.
- The imported module's `__file__` or `__spec__.origin`, and its distribution version
  from `importlib.metadata` where available. Import names and distribution names
  may differ; editable/namespace packages may not have an ordinary `__file__`.
- The relevant launch/kernel configuration and import path when a different source
  tree, same-named local file or accidental global installation could be selected.
- Native-library, driver/runtime or accelerator information only when it bears on
  the failure. A package name or successful GPU import does not prove device execution.

Inspect only the information needed to distinguish the causes. Do not dump all
environment variables, full configurations or authenticated package URLs into logs;
they may expose credentials. Do not import a heavy numerical stack merely to
collect an inventory on a host where execution is not authorized.

## Diagnose before reinstalling

Distinguish an absent dependency from an unsupported Python version, incompatible
binary/ABI, wrong import origin, circular import, unavailable optional backend,
missing system library and a real numerical/physical defect. Preserve the original
error and inspect the relevant dependency/entry-point contract.

Do not convert an import or numerical exception into plausible output, a silent
fallback or a successful status. A missing optional engine needs an explicit
capability error unless an established equivalent fallback is part of the actual
method contract. Record the selected path and assess any scientific differences.

First use the existing environment and install procedure correctly. A notebook
kernel may bootstrap execution, but its preinstalled scientific libraries are not
automatically the project's intended dependencies. Link/select the correct kernel
or launch the owned numerical process through the intended interpreter rather
than installing into an unrelated `pip` and hoping imports change.

## Make the smallest coherent environment change

- Change the authoritative dependency declaration in the project's actual layout.
  Put a genuinely optional engine in the appropriate optional group; do not move a
  required runtime dependency out of the base installation merely to hide failure.
- Honor the project's supported Python range and package manager. Do not import a
  fixed Python version, WSL requirement, `src/` layout or lock format from another
  repository. When a needed upgrade changes compatibility, update affected metadata,
  CI/runtime definitions, callers and installation guidance coherently.
- Regenerate existing resolved locks with their owning tool; do not hand-edit
  resolved version lines or create a second lock system without need. During active
  development, a justified dependency upgrade is an intervention to assess, not a
  forbidden change because yesterday's environment was pinned.
- Avoid reinstalling every extra, global packages, a browser, model stack or GPU
  toolchain for a narrow import problem. Respect installation, host and quota
  authorization; do not modify a running numerical job's environment in place.
- Preserve package resources, entry points, public import contracts and failure
  behavior when changing layout. Check actual readers and installed-package paths,
  not only imports that happen to work from the repository root.

For a requested remote notebook or transport, reuse the existing runner and carry
only code and inputs the actual calculation/tests read. Exclude environments,
caches, credentials, agent instructions and unrelated literature or observations.
Use the intended project environment on the approved host, not an accidental kernel
stack. A prepared archive is not evidence of a remote installation or executed fit.

## Verify the repair at the real consumer

Confirm the actual interpreter, import origin and required capabilities after the
change. Exercise the affected entry point or consumer and a focused regression on
an authorized host. Static metadata, dependency resolution and syntax checks prove
different things from importing a native extension or executing its numerical code.

For a numerical-library/backend upgrade, compare the relevant physical observable
and uncertainty against independent expectations at justified precision. Assess
applicable convergence, changed defaults, dtype and reduction/RNG behavior rather
than updating golden outputs until tests pass. Separate bitwise replay, numerical
agreement and statistical agreement; matching bytes do not establish correct physics.

Lead delivery with the restored scientific capability and measured effect when
executed, then the narrow environment change and checks performed. State a missing
dependency or authorization precisely when blocked; do not call an unexecuted
repair complete. Optional installed helpers such as `scientific-repair-not-deferral`
and `python-pytest-suite` complement this guide without becoming dependencies.
