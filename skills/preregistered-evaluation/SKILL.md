---
name: preregistered-evaluation
description: "Freezes an evaluation protocol before protected outcomes are seen, with custody, amendments, unblinding, and deviation records. Use when tuning could leak into a held-out benchmark, when a comparison needs a defensible decision rule, or when auditing whether a claim was truly prespecified. Do not use to relabel already-seen results as preregistered, to choose the estimator, or to claim Registered Report status without a journal's stage-one acceptance."
---

# Preregistered Evaluation

## When to use

- A held-out benchmark or protected dataset will decide whether a method is accepted.
- You are choosing thresholds, exclusions, or metrics and want the choice recorded
  before performance is known.
- You need to audit whether a reported comparison was prespecified or assembled after
  the fact.

## When not to use

- The results have already been inspected; record the exposure and design a new
  protected evaluation instead of claiming prior registration.
- The work is exploratory and will be reported as exploratory; a frozen confirmatory
  protocol would misrepresent it.
- You need to choose or validate the statistical estimator; use the appropriate
  inference method and calibration checks.

## Inputs

- Hypotheses, competing explanations, estimand, and the evaluation population.
- Primary and secondary outcomes, decision thresholds, uncertainty treatment,
  multiplicity or sequential-look policy, exclusions, and failure handling.
- Analysis code identity, dependency and configuration versions, data split identity,
  seeds and RNG policy.
- A blinding and custody plan: what is hidden, who holds the key, and who may unblind.
- The [protocol and custody contract](references/protocol-and-custody.md) distinguishes
  preregistration, blinding, and a journal's Registered Reports process.

## Procedure

1. Write the protocol before inspecting protected outcomes. Include the decision rule,
   not just the metric: what result leads to acceptance, rejection, or "indeterminate".
2. Define development and held-out material under the real dependence structure.
   Disclose prior exposure; renaming or resplitting exposed cases does not erase it.
3. Freeze the exact protocol, analysis code, configuration, and data split with a
   version, UTC timestamp, and digest. A digest alone does not prove time or custody.
4. Record what is hidden and why. Check leakage through plots, logs, summaries, caches,
   and custodian messages, not only the answer column.
5. Name who holds the key and the process for release. Keep secret values out of the
   protocol, prompts, manifests, and logs.
6. Amend only before outcome exposure, with a new version, rationale, authority, and
   timestamp. Keep the previous version. After exposure, do not replace thresholds,
   endpoints, or exclusions to fit the result.
7. Unblind once through the named process. Record who released the key, when, and which
   code and data versions were used.
8. Report every prespecified outcome, exclusion, failure, and deviation. Separate
   exploratory or post-exposure analyses from the confirmatory claim.
9. If a genuine defect invalidates the protocol, disclose and repair it rather than
   publish a known-wrong result. A changed claim needs a new protected assessment.

### Worked example

A team compares two retrieval methods on a held-out catalog. Before requesting labels,
they freeze the primary metric, the acceptance threshold, exclusion rules, analysis
commit, and the exact data split. The custodian releases labels only after the frozen
analysis runs. The report includes the prespecified result, failed queries, and any
deviation. If the team later lowers the threshold after seeing the score, that is a new
exploratory analysis, not the original claim. A journal's Registered Report label is
used only if that journal actually accepted a Stage 1 protocol.

## Failure modes

- **Backdated protocol:** a digest or editable commit is offered as proof of prior intent.
- **Leaky blind:** diagnostics, cache hits, or custodian messages reveal the answer.
- **Held-out recycling:** exposed cases are renamed as fresh evaluation material.
- **Outcome switching:** thresholds, endpoints, or exclusions change after inspection.
- **Label inflation:** a local preregistration is advertised as a peer-reviewed
  Registered Report.

## Verification

- Reconcile each hypothesis and outcome with its frozen analysis and decision rule.
- Check the chronology and the limits of the timestamp or registration mechanism.
- Review custody and leakage with dummy material, not hidden answers.
- Confirm amendments preserve earlier versions and state exposure and authority.
- Reconcile unblinding events and the final report against all planned outcomes,
  including missing, excluded, failed, and indeterminate cases.

## Provenance

- Klein and Roodman, *Blind Analysis in Nuclear and Particle Physics*, SLAC-PUB-12051:
  hiding an applicable aspect of data or results, review before unblinding, and honest
  correction afterward. The journal version was not available for comparison.
- PLOS Biology, *Preregistered Research Article Guidelines for Authors*: staged review,
  in-principle acceptance, registration, and reporting of changes.
- FDA, *Multiple Endpoints in Clinical Trials*, final October 2022: prospective
  specification and multiplicity control in human-drug trials. The guidance is
  nonbinding and does not govern arbitrary software evaluations.
- Hash, custody, and amendment mechanics are project policy, not a universal CERN
  standard. Do not transplant clinical thresholds into another field.

## Related locks

- [Quality ratchet](../quality-ratchet/SKILL.md) prevents silent weakening of a frozen gate.
- [AST semantic hashing](../ast-semantic-hashing/SKILL.md) records a conservative analysis-code identity.
- [Strangler fig migration](../strangler-fig-migration/SKILL.md) uses outcome-independent cutover criteria.
- [Circuit breaker isolation](../circuit-breaker-isolation/SKILL.md) preserves failed evaluation cases and denominators.
