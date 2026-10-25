---
name: quality-ratchet
description: "Establishes non-regressing baselines for deterministic engineering metrics, diagnostic counts, and reporting completeness. Use when adopting a check in a legacy codebase, protecting a measured improvement in CI, or reviewing a baseline change that could hide a regression. Do not use for flaky or incomparable measurements, or as evidence that a scientific result is correct."
---

# Quality Ratchet

## When to use

- You are adding a linter, type check, or coverage gate to code that already has debt.
- A metric must not regress while the team fixes the backlog incrementally.
- Someone proposes regenerating a baseline or widening an exemption.

## When not to use

- The metric is noisy, timing-dependent, or has no stable comparison rule.
- The tool, scope, or denominator changed and the old value no longer means the same thing.
- You need to know whether a scientific result is correct; use calibration or an
  independent referent instead.

## Inputs

- The property to protect and the metric that represents it, including direction and units.
- A reproducible measurement recipe: command, tool version, configuration, scope, and commit.
- The current baseline and the retained evidence it came from.
- A comparison rule and a named owner for exceptions.
- The [baseline contract](references/baseline-contract.md) has the full record format.

## Procedure

1. State the property in one sentence. "No new type errors" is a property;
   "coverage above 80%" is a proxy unless you can defend what it protects.
2. Measure the baseline from a complete run. Record the exact command, scope, tool
   version, commit, and date. A crashed or partial run is not a baseline.
3. Compare directionally. A lower-is-better metric may not rise; a higher-is-better
   metric may not fall. Do not offset one metric's regression with another's improvement.
4. For diagnostic counts, compare identities, not just totals. Fixing one warning
   must not create room for a different one.
5. Make every exemption visible and temporary: file or issue, owner, reason, expiry,
   and the condition for removal.
6. Update the baseline only in a separate reviewed change after an improvement is
   measured. Record the old value, new value, scope, and why the change is justified.
7. Wire the gate to the checker's exit status. New-only filtering is not enforcement
   if the command exits successfully on findings.
8. For scientific pipelines, ratchet reporting completeness (targets, masks,
   exclusions, uncertainty fields), not the size of error bars or a lower exclusion rate.

### Worked example

A Python service has 412 existing mypy errors. The team records that count at commit
`abc123`, with the exact mypy version and command, and adds a CI step that filters
against the baseline. A pull request introduces one new error: the filter reports it
and CI fails. A later pull request fixes twelve errors; the count is 400, and a
separate reviewed change updates the baseline. An upgrade that renames error codes is
handled as a migration, not as 412 new errors to grandfather. The numbers illustrate
the workflow; they are not a recommended threshold.

## Failure modes

- **Baseline laundering:** regenerating the baseline in the same change absorbs the regression.
- **Denominator gaming:** deleting files or narrowing the population improves a
  percentage without improving the code.
- **Flaky ratchet:** a lucky run freezes a noisy value, and rerunning until green
  becomes the workflow.
- **Permanent amnesty:** exemptions lose owners or expiry dates and become invisible policy.
- **False enforcement:** the job prints new findings but exits zero.

## Verification

- Walk through a worse, equal, and improved value. Only the improved case may propose
  a baseline update.
- Add one new finding while removing another. The gate must still fail on the new one.
- Run the gate with the checker missing or crashing. It must be unresolved, not pass.
- Inspect the CI command and its exit code, not just the log output.
- Check every exemption has an owner and an expiry date.

## Provenance

- golangci-lint FAQ, "How to use golangci-lint in CI" and the new-issue filtering
  sections: exit-code handling and changed-line blind spots.
- mypy-baseline README, "Usage": baseline creation, filtering, and explicit resynchronization.
- golangci-lint-action upstream `test.yml`: a concrete workflow that combines
  new-only filtering with a success-on-issues exit setting; do not copy that exit policy.
- Separate baseline updates, expiring exemptions, and scientific reporting rules are
  project policy. Full URLs and source limits are in the reference.

## Related locks

- [AST semantic hashing](../ast-semantic-hashing/SKILL.md) protects the identity of cached measurements.
- [Strangler fig migration](../strangler-fig-migration/SKILL.md) preserves gates across staged replacements.
- [Preregistered evaluation](../preregistered-evaluation/SKILL.md) freezes assessment rules before exposure.
- [Circuit breaker isolation](../circuit-breaker-isolation/SKILL.md) keeps failed measurements visible and isolated.
