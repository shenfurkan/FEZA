# Six Locks: boundaries and source plan

## Operator scope correction

During acquisition, the operator excluded Moving-Block Bootstrap as unrelated to
this engineering skill package. **Five locks remain in scope**; no replacement
sixth skill is authorized. The historical `six-locks` document names are retained
to keep the requested audit paths stable. References to six in the initial plan
below describe the original request, not the final deliverable count. New skills
will link to the other four active locks, not to an absent bootstrap skill.
The already acquired bootstrap PDF and failed publisher response remain in the
local collection and budget but are not normative evidence for these five skills.

## Inventory and authorization

The operator requested six new Markdown-only skills and bounded primary-source
downloads. The working tree was clean. All **23** existing `skills/*/SKILL.md` descriptions
were inspected (the task anticipated 22). None of those skills is to be changed.
The six requested names are unused, lowercase, hyphenated, and consistent with
existing directory/name pairs. Existing metadata has extra keys in some skills;
new skills use only `name` and `description`, without migrating older metadata.

Intended use is portable engineering guidance, not scientific analysis, operational
control, a software package, or certification. This is static exploratory authoring;
no deployed software is being classified or approved. Classification/criticality
remain deployment-specific decisions before consequential use. No safety/mission
deployment has been assessed or authorized. The operator owns
acceptance; the author cannot grant independent review or waive unresolved evidence.
Acceptance evidence is retained passages plus the task's static document checks.
No numerical computation, behavioral evaluation, installation, or service is authorized.

## Common doctrine

Close an escape route without claiming that the lock proves the science. Keep
observations, assumptions, design policy, source evidence and interpretation distinct.
The package's shared doctrine is recorded here once, not copied into every skill:

| Lock | Escape route closed | Residual question |
|---|---|---|
| Quality | Silent weakening or laundering of a comparable baseline | Does the gated property measure what matters? |
| Identity | Cache reuse across changes to declared computation meaning/inputs | Is the computation itself correct and the observability contract sound? |
| Transition | Unreviewed all-at-once replacement and loss of provenance authority | Do independent references support the new implementation/model? |
| Evaluation | Outcome-driven changes disguised as a prospective decision rule | Is the frozen estimator/decision rule adequate and calibrated? |
| Failure | One fault erases unrelated work or disappears from the denominator | How does incomplete coverage affect the scientific conclusion? |

All numeric acceptance/resource choices need a retained derivation or an explicit
user-supplied starting-value label. Historical/product examples are not universal
thresholds. Unknown evidence stays unresolved. Protected material, existing work,
scope, compute and publication permissions remain intact. No ISO, NASA or other
standards-compliance claim follows from these Markdown procedures.

## Boundaries

| Skill | Owns | Does not do | Related existing skill |
|---|---|---|---|
| `quality-ratchet` | Comparable, directional baselines, explicit improvements, expiring legacy exemptions | It does not certify scientific correctness, choose universal coverage targets, or replace assurance review. | [scientific-software-assurance](../skills/scientific-software-assurance/SKILL.md), [scientific-verification-and-validation](../skills/scientific-verification-and-validation/SKILL.md), [python-pytest-suite](../skills/python-pytest-suite/SKILL.md) |
| `ast-semantic-hashing` | Conservative, versioned syntax normalization and complete cache identities | It does not decide arbitrary program equivalence, validate a cached result, or use lossy navigation skeletons as executable identities. | [stingy-context](../skills/stingy-context/SKILL.md), [reproducibility-auditor](../skills/reproducibility-auditor/SKILL.md) |
| `strangler-fig-migration` | Seams, authoritative routing, shadow comparisons, bounded cutover and retirement | It does not authorize a scientific model change, a big-bang rewrite, duplicate side effects, or deletion of unrecognized work. | [scientific-software-assurance](../skills/scientific-software-assurance/SKILL.md), [scientific-method-comparison](../skills/scientific-method-comparison/SKILL.md) |
| `preregistered-evaluation` | Protocol freezing, custody, protected evaluation and visible amendments/deviations | It does not select the estimator, confer Registered Report status, guarantee unbiased inference, or substitute for calibration. | [statistical-inference](../skills/statistical-inference/SKILL.md), [scientific-verification-and-validation](../skills/scientific-verification-and-validation/SKILL.md) |
| `circuit-breaker-isolation` | Failure classification, recovery admission and isolated batch accounting | It does not provide isolation by itself, turn missing results into nondetections, or launch/terminate unrelated work. | [scientific-software-assurance](../skills/scientific-software-assurance/SKILL.md), [reproducibility-auditor](../skills/reproducibility-auditor/SKILL.md) |

All five stay narrow rather than duplicating the five specifically named existing
skills. Cross-links to existing skills are optional handoffs, not runtime
dependencies; each new skill must remain usable when installed alone. The five
new locks link mutually; existing skills need not be edited for reverse links.

## Source acquisition plan

Primary-source priority is published research, official guidance, official product
documentation, then author-origin accounts. Author web essays can establish naming
and history, not peer review or normative authority. Local engineering requirements
are explicitly task policy, not claims attributed to these essays.

| Lock | Planned primary sources (at most three per lock) | Discriminating question |
|---|---|---|
| Quality | golangci-lint FAQ; mypy-baseline upstream README (usage website unavailable); concrete upstream CI configuration | What is actually gated, and is Google/Meta attribution evidenced? |
| Identity | Bazel remote caching; Nix store derivations; Unison's big idea | Are the documented identities action/file/derivation based or syntax-tree based? |
| Transition | Fowler's original Strangler Fig and Branch by Abstraction essays; Microsoft strangler guidance (AWS unavailable) | Which claims are historical naming versus documented migration mechanics? |
| Evaluation | Klein & Roodman institutional manuscript; PLOS Biology Registered Reports policy (Chambers full text unavailable); FDA multiple-endpoints final guidance | How do blinding, preregistration, and a journal's Registered Reports process differ? |
| Failure | Nygard publisher-authorized preview; resilience4j CircuitBreaker and Config first-party API/source documents (website unavailable) | Which behavior belongs to a breaker versus isolation, timeout, or retry policy? |

Budget: at most 24 acquired files and 200 MB (conservatively interpreted as
200,000,000 bytes), including retained error bodies. No paywall circumvention,
certificate-verification bypass, third-party pirated copy, or unauthorized upload.
HEAD access checks precede each GET; an unhelpful HEAD is recorded rather than
mistaken for authenticated content. The network is available: official golangci-lint,
Unison, Fowler, and FDA endpoints answered successfully on 2026-10-25 UTC.
The Künsch publisher PDF HEAD returned `text/html`, not `application/pdf`;
the UCSD author site had a certificate-chain error. These are acquisition blockers
in the original plan, not reasons to invent passages. Bootstrap acquisition and
analysis stopped following the operator's scope correction.

The [provenance ledger](six-locks-provenance.md) owns actual receipts, locators,
corrections, access failures, and the final source selection. Skill drafting begins
only after accessible primary material has been retained and read for that lock.
Fifteen primary documents were adopted, three per active lock; inaccessible and
nonselected candidates are separately retained/recorded, not normative evidence.
