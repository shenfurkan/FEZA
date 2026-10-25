# Baseline contract and evidence limits

## Primary basis

1. golangci-lint, [FAQ](https://golangci-lint.run/docs/welcome/faq/), snapshot
   2026-10-25. “How to use golangci-lint in CI” says to inspect exit status and
   fail on an unsuccessful status. “How to integrate golangci-lint into a large
   project with thousands of issues” documents new-issue filtering against a base.
   “Why --new-from-xxx don't seem to be working in some cases?” explains that
   diagnostics outside changed lines may be missed. This is a documented capability,
   not proof that every new defect is detected or that a named corporation uses it.
2. mypy-baseline, [upstream README](https://raw.githubusercontent.com/orsinium-labs/mypy-baseline/master/README.md),
   snapshot 2026-10-25, lines 28–42, “Usage”. It describes creating/synchronizing a
   baseline and subsequently filtering it. It recommends regeneration after fixes;
   it does not prescribe independent review, expiring waivers, or scientific gates.
3. golangci-lint-action, [upstream workflow](https://raw.githubusercontent.com/golangci/golangci-lint-action/master/.github/workflows/test.yml),
   snapshot 2026-10-25, lines 48–75 and 77–105. This concrete workflow uses
   `only-new-issues: true`, but also `--issues-exit-code=0`. It exercises the action;
   it is **not** evidence for an enforced no-new-issues gate. Do not copy that exit
   policy into a ratchet.

All three are first-party software documents, not peer-reviewed evidence of a
universal quality law. Google/Meta attribution remains unverified and is omitted.
The provisions below are project policy.

## Manifest fields

| Field | Required meaning |
|---|---|
| Metric | Definition, direction, units, diagnostic identity/matching rule |
| Scope | Included files/population, denominator, selections and exclusions |
| Measurement | Exact command, configuration, tool/plugin versions |
| Snapshot | Commit plus dirty/untracked-input identity when relevant |
| Time | Measurement UTC and the identity of retained raw evidence |
| Baseline | Measured value or issue set; approval and evidence location |
| Gate | Comparison rule; source or user-supplied label for numeric limits |
| Exemptions | Issue, file, owner, reason, expiry and closure condition |
| Update | Previous baseline, proposed change, reason and reviewer |

Reuse the project's existing record format. Do not install a tool, introduce a
second ledger, or run a measurement just to populate this template without permission.

## Gate semantics

- A lower-is-better metric may not increase; a higher-is-better metric may not
  decrease. Exact set/identity comparisons are appropriate for discrete findings.
- A precision allowance needs a measured error/rounding justification fixed before
  comparison; it is not an unexplained tolerance added after a regression appears.
- Unknown, skipped, interrupted, nonfinite and zero are different outcomes.
- A changed denominator breaks comparability until an explicit migration resolves it.
- For debt findings, a non-increasing count is insufficient: an unrelated fix can
  conceal a new issue. Preserve identities and examine unmatched findings.
- Tool changes can change issue identities; investigate rather than mass-grandfather.

## Scientific adaptation

An accounting-completeness gate asks whether required targets, masks, uncertainty
descriptions and failures are reported. It does not demand that uncertainty values
shrink. A larger, more honest uncertainty is not a regression in scientific quality.
An exclusion rate can legitimately increase after a calibration defect is found;
forcing it downward can suppress quality flags or hide censoring. Preserve the
selection mechanism and impact, and assess those scientifically outside this lock.

## Paper review cases

| Proposed case | Expected disposition |
|---|---|
| Worse metric under the same contract | Reject the regression; retain evidence |
| Improvement followed by ordinary gate execution | Keep old baseline until separately reviewed update |
| Equal totals but one new diagnostic | Reject the new diagnostic or explicitly disposition it |
| Missing checker output | Unresolved measurement, never successful zero findings |
| Higher coverage after deleting clean files | Investigate denominator; no improvement claim |
| Tool upgrade with changed diagnostic labels | Explicit compatibility/rebaseline review |

Use these cases as review prompts; any recorded value needs its own evidence.
