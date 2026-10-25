# Six Locks: acquisition, evidence map and delivery record

## Scope and evidence vocabulary

The operator removed Moving-Block Bootstrap during acquisition. This record covers
**five active engineering locks**, not a replacement sixth. The historical file
names preserve the requested audit paths. See the [boundary analysis](six-locks-boundary.md).

`VERIFIED-PASSAGE` means the stated retained passage was actually read; it is not
software verification or scientific validation. `CORRECTED` records a contradicted
input claim. `ABSTRACT-ONLY` cannot support unseen methods. `BLOCKED` means the
required text/access was unavailable. `POLICY` denotes the operator's explicit
engineering requirements, not an externally verified law. `EXCLUDED` denotes the
subsequent scope correction. Unread material is never silently counted as evidence.

Downloads were explicitly authorized by the task. Public HEAD checks preceded GETs;
TLS verification remained enabled. A successful status was not treated as proof of
document identity: a challenge page, error body and subscription preview were retained
as such. No login, purchase, access-control workaround, or unauthorized upload occurred.
Each GET had a bounded socket timeout and an independent wall-clock alarm. Files
were written to exclusive incomplete paths and renamed only after full receipt.
Per-response size caps and network timeouts were agent-selected acquisition guards,
not operator-endorsed scientific thresholds or measured hardware limits. They did
not truncate any retained source. No retries ran without bounds; no partial file remains.

## Download receipts

All UTC values below are GET-start timestamps. Byte counts refer to the exact
retained response, not extracted/normalized text. All files are under the Git-ignored
`literature/six-locks/` collection; none is part of an installed skill. Full requested
URLs are recorded. Final URLs are identical except for E2a's publisher cookie-error
redirect, noted below. Access status does not confer redistribution rights.

| ID / local file | Full URL | UTC | HTTP / content type | Bytes | Access / licence / use |
|---|---|---|---|---:|---|
| Q1 `golangcilint_faq_20261025.html` | https://golangci-lint.run/docs/welcome/faq/ | 2026-10-25T16:17:08.052568Z | 200 / text/html; charset=utf-8 | 126138 | Public first-party docs; reuse licence not established; adopted |
| Q2 `mypybaseline_usage_20261025.html` | https://mypy-baseline.orsinium.dev/usage.html | 2026-10-25T16:17:09.006954Z | 403 / text/plain; charset=UTF-8 | 17 | BLOCKED; denial body, not documentation; no reuse grant |
| M0 `kunsch_1989_stationary-bootstrap-access.html` | https://projecteuclid.org/journals/annals-of-statistics/volume-17/issue-3/The-Jackknife-and-the-Bootstrap-for-General-Stationary-Observations/10.1214/aos/1176347265.full | 2026-10-25T16:17:09.898471Z | 200 / text/html | 1162 | BLOCKED challenge body; not article/abstract; subsequently excluded |
| M1 `politis_2004_automatic-block-length.pdf` | https://public.econ.duke.edu/~ap172/Politis_White_2004.pdf | 2026-10-25T16:17:12.181446Z | 200 / application/pdf | 193526 | Public academic-hosted PDF; licence uninspected; EXCLUDED/unread |
| A1 `bazel_remote-caching_20261025.html` | https://bazel.build/remote/caching | 2026-10-25T16:17:13.680248Z | 200 / text/html; charset=utf-8 | 274382 | Public first-party HEAD docs; reuse licence unestablished; adopted |
| A2 `nix_derivations_20261025.html` | https://nix.dev/manual/nix/2.24/store/derivation/ | 2026-10-25T16:17:15.137910Z | 404 / text/html; charset=utf-8 | 21655 | BLOCKED missing page; not documentation; no reuse grant |
| A3 `unison_big-idea_20261025.html` | https://www.unison-lang.org/docs/the-big-idea/ | 2026-10-25T16:17:16.255201Z | 200 / text/html; charset=UTF-8 | 89276 | Public first-party docs; reuse licence unestablished; adopted |
| Q2b `mypybaseline_readme_20261025.md` | https://raw.githubusercontent.com/orsinium-labs/mypy-baseline/master/README.md | 2026-10-25T16:19:18.097687Z | 200 / text/plain; charset=utf-8 | 1964 | Public upstream README; licence not established in this file; adopted |
| Q3 `golangcilintaction_workflow_20261025.yml` | https://raw.githubusercontent.com/golangci/golangci-lint-action/master/.github/workflows/test.yml | 2026-10-25T16:19:18.866810Z | 200 / text/plain; charset=utf-8 | 3925 | Public upstream CI configuration; licence unestablished in file; adopted/read only |
| A2b `nix_derivations-v2.34_20261025.html` | https://nix.dev/manual/nix/2.34/store/derivation/ | 2026-10-25T16:19:19.695220Z | 200 / text/html; charset=UTF-8 | 29388 | Public first-party manual 2.34; reuse licence unestablished; adopted |
| S1 `fowler_strangler-fig_20261025.html` | https://martinfowler.com/bliki/StranglerFigApplication.html | 2026-10-25T16:19:20.846861Z | 200 / text/html | 20366 | Public author essay, dated 2024-08-22; reuse licence unestablished; discovery/revision context only |
| S2 `fowler_branch-abstraction_20261025.html` | https://martinfowler.com/bliki/BranchByAbstraction.html | 2026-10-25T16:19:22.177046Z | 200 / text/html | 18254 | Public author essay, dated 2014-01-07; reuse licence unestablished; adopted as descriptive account |
| E1 `klein_2005_blind-analysis.pdf` | https://slac.stanford.edu/pubs/slacpubs/12000/slac-pub-12051.pdf | 2026-10-25T16:19:23.881753Z | 200 / application/pdf | 524224 | Public institutional author manuscript; reuse licence unestablished, not inferred from funding; adopted with version limit |
| E3 `fda_2022_multiple-endpoints.pdf` | https://www.fda.gov/media/162416/download | 2026-10-25T16:19:27.468064Z | 200 / application/pdf | 324708 | Public final federal guidance; no separate reuse licence claimed; adopted, nonbinding scope |
| F1 `nygard_2007_release-it-preview.pdf` | https://media.pragprog.com/titles/mnee/mnee-antipatterns.pdf | 2026-10-25T16:19:28.796910Z | 200 / application/pdf | 573624 | Public publisher-authorized excerpt; all rights reserved, 2007/2009 notices; preview only |
| E2a `chambers_2022_registered-reports-access.html` | https://www.nature.com/articles/s41562-021-01193-7 | 2026-10-25T16:21:22.860402Z | 200 / text/html; charset=utf-8 | 458054 | Subscription preview; abstract/metadata only; Springer Nature rights; not adopted for methods |
| E2 `plos_registered-reports_20261025.pdf` | https://plos-marketing.s3.amazonaws.com/Marketing/Biology+Preregistered+Articles+Guidelines+for+Authors.pdf | 2026-10-25T16:21:25.888720Z | 200 / application/pdf | 295325 | Public official publisher guidelines, updated 2020-01-28; reuse licence unestablished in file; adopted |
| S3 `microsoft_strangler-fig_20261025.html` | https://learn.microsoft.com/en-us/azure/architecture/patterns/strangler-fig | 2026-10-25T16:21:27.557374Z | 200 / text/html | 63587 | Public full first-party article despite generic sign-in UI banner; reuse licence unestablished; adopted |
| F2a `resilience4j_circuitbreaker-v2.3.0_20261025.java` | https://raw.githubusercontent.com/resilience4j/resilience4j/v2.3.0/resilience4j-circuitbreaker/src/main/java/io/github/resilience4j/circuitbreaker/CircuitBreaker.java | 2026-10-25T16:21:28.397046Z | 200 / text/plain; charset=utf-8 | 45887 | Public upstream v2.3.0 source/API, Apache-2.0 header; adopted/never executed |
| F2b `resilience4j_config-v2.3.0_20261025.java` | https://raw.githubusercontent.com/resilience4j/resilience4j/v2.3.0/resilience4j-circuitbreaker/src/main/java/io/github/resilience4j/circuitbreaker/CircuitBreakerConfig.java | 2026-10-25T16:21:29.165259Z | 200 / text/plain; charset=utf-8 | 44364 | Public upstream v2.3.0 source/API, Apache-2.0 header; adopted/never executed |
| E3a `fda_multiple-endpoints-status_20261025.html` | https://www.fda.gov/regulatory-information/search-fda-guidance-documents/multiple-endpoints-clinical-trials | 2026-10-25T16:21:30.649910Z | 200 / text/html; charset=UTF-8 | 36017 | Public official status metadata for E3, not an additional normative source |
| S1o `fowler_2004_original-strangler-fig.html` | https://martinfowler.com/bliki/OriginalStranglerFigApplication.html | 2026-10-25T16:23:20.362029Z | 200 / text/html | 18978 | Public author original, dated 2004-06-29 and marked superseded; licence unestablished; historical basis only |

E2a effective URL:
`https://www.nature.com/articles/s41562-021-01193-7?error=cookies_not_supported&code=0b726539-9e9e-40c5-af0b-7d81679bb98f`.
The retained page explicitly says it is a subscription preview; no paywall was bypassed.
E1's filename retains the year supplied in the task's bibliographic lead; that
filename is not evidence of the manuscript's date or equality to a published version.

Budget used: **22 files / 3,164,821 bytes**, including error bodies, the unused
bootstrap PDF, the author revision and the subscription preview. The task's stop
limits are 24 files / 200 MB, conservatively interpreted as 200,000,000 bytes.
No budget was enlarged. Acquisitions have stopped; remaining budget is not a reason
to collect unnecessary material. All acquired PDF bodies begin with the PDF magic.
The `.java`/`.yml` files are ignored source inputs, not executable deliverables.

## Selected primary sources

| Active skill | Adopted sources | Count |
|---|---|---:|
| quality-ratchet | Q1, Q2b, Q3 | 3 |
| ast-semantic-hashing | A1, A2b, A3 | 3 |
| strangler-fig-migration | S1o (historical only), S2 (descriptive only), S3 | 3 |
| preregistered-evaluation | E1 (author manuscript), E2, E3; E3a is E3 status metadata | 3 |
| circuit-breaker-isolation | F1 (preview only), F2a, F2b | 3 |

Nonselected acquisition candidates do not supply normative methods. In particular,
E2a is not a fourth adopted evaluation source, and S1 is not a fourth migration
source. Public access alone did not make their unread/unselected content authoritative.
Research discovery used search results only as leads, not as passage evidence.

## Claim-to-evidence map

Local files in this table are relative to `literature/six-locks/`. Locators refer
to printed pages, source symbols/lines or named HTML sections, not model recollection.

| Claim | Source identity | Locator | Local file | Status | Supports / does not support |
|---|---|---|---|---|---|
| New-only checks can support gradual quality adoption | Q1, golangci-lint FAQ | “How to use golangci-lint in CI”; “How to integrate ... large project”; “Why --new-from-xxx ...” | `golangcilint_faq_20261025.html` | VERIFIED-PASSAGE | Exit handling and diff filtering, including changed-line blind spots; no exhaustive defect detection or Google/Meta adoption |
| An explicit baseline tool separates synchronization and filtering | Q2b, mypy-baseline README | “Usage”, lines 28–42 | `mypybaseline_readme_20261025.md` | VERIFIED-PASSAGE | `sync`/`filter` roles; not separate review, expiry, or scientific validity |
| An upstream new-only CI example necessarily enforces regression failure | Q3, golangci-lint-action workflow | jobs `test`, lines 48–75; `test-go-install`, lines 77–105 | `golangcilintaction_workflow_20261025.yml` | CORRECTED | Both use `only-new-issues: true` **and** `--issues-exit-code=0`; this concrete example is not an enforcing gate |
| Google/Meta and universal large-CI practice are established | No inspected corporate implementation evidence | No supporting locator | None | UNVERIFIED | Corporate attribution omitted; first-party tool capability is a narrower supported claim |
| Bazel remote caching is source-AST semantic hashing | A1, Bazel Remote Caching, HEAD snapshot | “Overview”; “Known issues” / environment leakage and external tools | `bazel_remote-caching_20261025.html` | CORRECTED | Actions have inputs/outputs/command/environment, action-result cache and output CAS; not AST-semantic equivalence |
| Nix store identity is a source-program AST summary | A2b, Nix Reference Manual 2.34 | “Store Derivation”; “Process creation fields”; “Encoding” | `nix_derivations-v2.34_20261025.html` | CORRECTED | Canonical serialized derivations/store objects, process fields and content-addressing distinctions; not source-AST normalization |
| Syntax-tree-addressed code has a direct product example | A3, Unison The big idea | Opening `increment` example and dependency substitution; “No builds” | `unison_big-idea_20261025.html` | VERIFIED-PASSAGE | Definition trees, positional binding references, dependency hashes; pure-computation caching example; not a generic Python normalizer |
| Every semantically different program must have a distinct finite digest | Operator's original negative-check requirement, narrowed | New normalization contract, “Review obligations” | None (design deduction) | CORRECTED / POLICY | Finite fixture pairs must distinguish their payloads/digests; no collision-impossibility or arbitrary equivalence proof is claimed |
| AST key must also bind data, environment and dependencies | Operator request, identity-lock contract | Original task §6.3; new skill Procedure 6–9 | None (task policy) | POLICY | Explicit scientific cache identity, not an algorithm attributed to Bazel/Nix; no implementation run |
| Fowler's original metaphor dates to 2004 | S1o, Original Strangler Fig Application | Heading/date “29 June 2004”; “An alternative route”; “Event Interception” paragraph | `fowler_2004_original-strangler-fig.html` | VERIFIED-PASSAGE | Historical naming and gradual interception; original is marked superseded and is an author blog, not peer-reviewed authority |
| The requested Fowler URL still displays the original 2004 text | S1, Strangler Fig | Heading/date “22 August 2024”; final original-text link | `fowler_strangler-fig_20261025.html` | CORRECTED / context only | Current URL is a later essay; S1o was separately retrieved to inspect the original |
| Branch by abstraction permits coexisting internal implementations | S2, Fowler (2014) | Client/abstraction/supplier sequence and common-theme paragraph | `fowler_branch-abstraction_20261025.html` | VERIFIED-PASSAGE (descriptive) | Migration mechanics in an author account; not a scientific cutover criterion or normative standard |
| A facade can route legacy/new slices and support deliberate retirement | S3, Microsoft Strangler Fig pattern | “Solution”; “Problems and considerations”; “When to use”; “Example” | `microsoft_strangler-fig_20261025.html` | VERIFIED-PASSAGE | Routing, dependencies, inapplicable cases, data consistency and harder rollback after deletion; not numerical parity or scientific truth |
| Shadow isolation, scientific parity and zero-call retirement are universal external rules | Operator request, transition-lock contract | Original task §6.4; new migration contract | None (task policy) | POLICY | Adopted as explicit bounded project rules; not inferred from either blog |
| Blinding controls experimenter bias but is not correctness/calibration | E1, Klein & Roodman, SLAC-PUB-12051 | §2, report pp. 9–11; §3.4, pp. 23–26 | `klein_2005_blind-analysis.pdf` | VERIFIED-PASSAGE, manuscript only | Applicable narrow hiding, leakage/selection limits, review, honest corrections after unblinding; no universal bias elimination |
| The exact journal version/pages of Klein & Roodman were inspected | E1 author report; publisher endpoint unavailable | Report title page says “Submitted to Annual Reviews”; journal endpoint HEAD 403 | `klein_2005_blind-analysis.pdf` | BLOCKED for version-of-record inspection | The public author manuscript was read; journal-text parity and journal-page locators were not verified |
| Registered Report is simply another name for preregistration | E2, PLOS Biology guidelines, updated 2020-01-28 | pp. 1–4, 6–9; Stage 1/2 and deviations | `plos_registered-reports_20261025.pdf` | CORRECTED | Prior peer review and in-principle acceptance add a distinct publisher process; registration alone does not confer it |
| Clinical endpoint plans should be specified prospectively | E3, FDA Multiple Endpoints, final October 2022 | §II.B–C, printed pp. 4–6; §III.A, pp. 6–7 | `fda_2022_multiple-endpoints.pdf` | VERIFIED-PASSAGE | Prospective endpoints, analyses and multiplicity; no public-registry requirement or software-wide FDA authority |
| FDA status/version remains an identified final document | E3a, official status record for E3 | Title “October 2022”, “Final”, docket FDA-2016-D-4460; content current 2024-04-16 | `fda_multiple-endpoints-status_20261025.html` | VERIFIED-PASSAGE / metadata | Status on inspected official entry; not a guarantee that no related guidance exists elsewhere |
| FDA + CERN + Registered Reports form one general standard | E1/E2/E3 have different scopes; no CERN policy acquired | E1 §2; E2 pp. 1–3; E3 §I–II, pp. 1–2 | Files E1/E2/E3 above | CORRECTED / CERN claim UNVERIFIED | Separate practices and scoped guidance; no combined standard or compliance claim |
| A newer Registered Reports review was read in full | E2a, Chambers & Tzavella (2022), DOI 10.1038/s41562-021-01193-7 | “Abstract” and subscription-preview notice only | `chambers_2022_registered-reports-access.html` | ABSTRACT-ONLY; full text BLOCKED | Identity and abstract-level description only; no methods/effectiveness claims adopted |
| Nygard's 2007 book motivates circuit-breaker use | F1, Release It!, publisher excerpt | Copyright/ISBN/printing page; §4.3 printed pp. 67–69 (PDF pp. 4–6) | `nygard_2007_release-it-preview.pdf` | VERIFIED-PASSAGE, preview only | Cascading failures/timeouts/breaker motivation; copyright 2007, retained printing 2009; not full-book review or detailed Circuit Breaker chapter |
| Ordinary circuit-breaker states/admission are documented | F2a, resilience4j v2.3.0 API source | Class Javadoc lines 37–55; permission methods 433–473; `State` 810–837 | `resilience4j_circuitbreaker-v2.3.0_20261025.java` | VERIFIED-PASSAGE, static only | CLOSED/OPEN/HALF_OPEN and special states; admission semantics, not containment or executed library behavior |
| Thresholds/windows/half-open permits are configurable, not universal constants | F2b, resilience4j v2.3.0 config source | `failureRateThreshold` 391–410; waits/permits 452–569; windows 572–678 | `resilience4j_config-v2.3.0_20261025.java` | VERIFIED-PASSAGE, static only | Configuration/API constraints; documented multiple half-open permits contradict any claim of a universal single-probe default |
| The API introduction enumerates every state consistently | F2a opening versus `State` | Lines 40–41 versus 810–837 | `resilience4j_circuitbreaker-v2.3.0_20261025.java` | CORRECTED / discrepancy retained | Intro says five states; enum also includes METRICS_ONLY. Skill describes normal states, not an exhaustive three-state product |
| Boundary equality in the API comments is unambiguous | F2a versus F2b | F2a lines 53–54; F2b lines 391–410 | Files F2a/F2b above | UNRESOLVED documentation conflict | Reopen at/above conflicts with close below/or equal; config says open at/above. Internal runtime implementation was not inspected or executed |
| Half-open maximum-wait prose identifies its completion counter consistently | F2b wait versus permit documentation | Lines 530–568 | `resilience4j_config-v2.3.0_20261025.java` | UNRESOLVED documentation ambiguity | Wait comment mentions minimumNumberOfCalls; separate permit setting exists. No runtime resolution invented |
| A breaker alone guarantees candidate isolation and complete scientific coverage | Operator request, failure-lock contract | Original task §6.6; new isolation contract | None (task policy) | POLICY / overclaim rejected | Requires independent watchdog/process/resource boundaries and full accounting; no containment experiment ran |

## Inaccessible or unexamined material

HEAD-only failures below produced no downloaded body and do not consume file count.
They were not retried through authentication, alternate certificates, pirated copies,
ResearchGate or Sci-Hub. Public upstream alternatives are separate authorized sources,
not assumptions that inaccessible pages say the same thing.

| Source / full URL | Access or examination status | Disposition |
|---|---|---|
| https://mypy-baseline.orsinium.dev/usage.html | HEAD/GET 403; Q2 is denial text | README Q2b used instead; site methods unread |
| https://projecteuclid.org/journals/annals-of-statistics/volume-17/issue-3/The-Jackknife-and-the-Bootstrap-for-General-Stationary-Observations/10.1214/aos/1176347265.pdf | HEAD 200 but HTML, not PDF; M0 full-page GET is challenge | BLOCKED, then bootstrap removed from scope |
| https://www.math.ucsd.edu/~politis/PAPER/ppw.pdf | HEAD certificate-chain failure | No TLS bypass; no body retained; bootstrap later excluded |
| https://public.econ.duke.edu/~ap172/Politis_White_2004.pdf | M1 acquired before scope correction; not opened | EXCLUDED; no formula/method claim adopted |
| Politis–Romano variants and Patton–Politis–White correction | Original plan only; not acquired or examined | EXCLUDED after operator correction |
| https://nix.dev/manual/nix/2.24/store/derivation/ and https://nix.dev/manual/nix/2.24/store/derivation.html | Missing endpoints; first retained as A2, second HEAD 404 | Fixed-version 2.34 page A2b adopted; stable HEAD redirect identified 2.34 |
| https://orca.cardiff.ac.uk/id/eprint/45177/1/Chambers_Cortex_2013b_GreenOA.pdf | HEAD 403 | Chambers (2013) full text BLOCKED; PLOS official policy used instead |
| https://www.nature.com/articles/s41562-021-01193-7 | E2a exposes abstract/metadata and subscription notice only | Full text BLOCKED; no unseen passages reconstructed |
| https://www.annualreviews.org/content/journals/10.1146/annurev.nucl.55.090704.151521 | HEAD 403 | Published-review identity was a discovery lead; only SLAC manuscript passages adopted |
| https://slac.stanford.edu/pubs/slacpubs/12000/slac-pub-12051.html | HEAD 404 | No metadata page read; do not infer journal-version parity |
| https://resilience4j.readme.io/docs/circuitbreaker and https://resilience4j.readme.io/docs/circuitbreaker.md | HEAD 403 | Web docs BLOCKED; first-party v2.3.0 API source used instead |
| https://javadoc.io/static/io.github.resilience4j/resilience4j-circuitbreaker/2.3.0/io/github/resilience4j/circuitbreaker/CircuitBreaker.html | HEAD 404 | No Javadoc page read |
| https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/strangler-fig.html | HEAD TLS EOF | AWS page BLOCKED; Microsoft official pattern used instead |
| https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/retry-backoff.html | HEAD connection closed | AWS retry page unread; retry mechanics remain explicit task policy |
| https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/ | HEAD connection closed | Unread; no threshold or jitter law copied |
| https://raw.githubusercontent.com/orsinium-labs/mypy-baseline/master/.github/workflows/test.yml | HEAD 404 | Candidate discovery only; no CI behavior inferred |
| https://raw.githubusercontent.com/orsinium-labs/mypy-baseline/master/.github/workflows/main.yml | HEAD 200 only | Not acquired/read; Q3 selected instead |
| Nygard, full Release It! and detailed Circuit Breaker chapter | Not supplied/legally acquired in full | Full book unexamined; only F1 preview cited |
| resilience4j internal CircuitBreakerStateMachine implementation | Not acquired/inspected | Comment discrepancies stay unresolved; no runtime claim |

The S1 author revision was read to locate S1o and establish that the canonical URL
had changed; it is not adopted as another normative migration reference. No blog,
search snippet, textbook summary, Wikipedia entry or secondary copy supplies a
normative requirement. Paper abstracts do not establish method details or effectiveness.

## Static acceptance and delivery

### Delivered scope

Five new skill directories contain a `SKILL.md` and one self-contained Markdown
reference each. There is no `moving-block-bootstrap` directory. Together with this
ledger, `docs/six-locks-boundary.md`, and the updated `docs/sources.md`, the change
contains **12 new Markdown files and one modified Markdown file**. Only the source
index is a modified pre-existing tracked file. No executable package, CLI, service,
test implementation, installer, client configuration, commit or push was produced.

| Skill | SKILL.md lines | Description characters | Concrete non-use cases | Failure modes | Verification checks | Reference files |
|---|---:|---:|---:|---:|---:|---:|
| quality-ratchet | 92 | 375 | 3 | 5 | 5 | 1 |
| ast-semantic-hashing | 96 | 439 | 3 | 5 | 5 | 1 |
| strangler-fig-migration | 101 | 377 | 3 | 5 | 5 | 1 |
| preregistered-evaluation | 104 | 455 | 3 | 5 | 5 | 1 |
| circuit-breaker-isolation | 107 | 396 | 3 | 5 | 6 | 1 |

### Checks and scope

Static inspection used Python 3.14.4 and PyYAML 6.0.3 to check document structure,
metadata and links. It executed no downloaded source and ran no behavioral tests.
After the first draft, each skill body was revised to lead with the engineering
procedure, move record-keeping detail into its reference, add one worked example,
and remove wording specific to this authoring session. This is author self-review,
not independent evaluation or evidence that the skills improve a real workflow.

| Acceptance condition (task-supplied limits) | Result | Evidence / limitation |
|---|---|---|
| YAML parses; only name + description; directory/name agreement | PASS, 5/5 | PyYAML parse plus composed-key count; no duplicate/extra frontmatter keys |
| Description length at most 1024 characters | PASS, 5/5 | Counts above; all are strings |
| SKILL.md length 70–130 lines | PASS, 5/5 | Counts above, including frontmatter |
| English prose and third-person descriptions with use/non-use scope | PASS, author review | Language/scope review, not an automated language-classifier claim |
| Required section order | PASS, 5/5 | Exact eight-heading sequence from the task |
| At least two non-use cases, three failure modes and three verification checks | PASS, 5/5 | Bullet counts above plus content review |
| Numeric scientific/resource criteria have derivation requirements or user-supplied labels | PASS, author review | No copied numeric operating defaults; one-probe and zero-call rules are explicit project policy; dates/versions/locators are identifiers |
| No developer-collection dependency in installed skill text | PASS | No `literature/` string in any of the ten skill/reference files; no repository-root or home-directory requirement |
| Internal paths and heading anchors resolve | PASS | 51 links checked across all 13 new/modified Markdown documents |
| Related-lock cross-links are symmetric | PASS | 20 directed links among five active locks, four companions each; optional old-skill handoffs are not reverse-link requirements |
| Reference-depth/file budget and Markdown-only deliverables | PASS | One reference per skill; all new/changed nonignored paths have `.md` suffix |
| Existing skill files unchanged | PASS | All 23 original SKILL.md files compared byte-for-byte with starting HEAD; Git reports no tracked change anywhere under existing skills |
| Download receipts/index/budget | PASS | All 22 filenames, sizes and URLs are recorded; all filenames/URLs occur in docs/sources.md; total 3,164,821 bytes; no incomplete source file |
| Local literature and machine instructions remain ignored | PASS | Git check-ignore confirmed collection files and AGENTS.md; no force-add |
| Whitespace/static diff hygiene | PASS | git diff --check; new-file trailing whitespace/tabs/final-newline inspection also clean |

No applicable static structural check remains failed or pending. These are author
checks against the revised five-skill scope, not an independent review or acceptance.
The original six-skill request is superseded by the bootstrap exclusion, not silently
reported as satisfied.

Runtime tests, numerical calibration, benchmarks, skill-trigger evaluations,
with/without-skill agent trials, fault injection, real isolation/rollback demonstrations,
services and installation checks: **not run / not authorized**. No historical run or
syntax/metadata result is used as behavioral acceptance. Skill effectiveness and
generated-code correctness remain unmeasured. No standards-compliance claim is made.

### Input-claim disposition

- **Quality:** tool-supported gradual adoption verified; Google/Meta attribution
  unverified and omitted. The inspected concrete CI workflow disables issue-induced
  failure, so filtering was not confused with enforcement.
- **Bootstrap:** excluded by explicit operator correction, not replaced or implemented;
  its retained PDF remains unread. No bootstrap claim was promoted to verified.
- **Identity:** Bazel/Nix AST attribution corrected to action/derivation/store-object
  identities. Unison supplies a real syntax-tree example. Finite-digest fixture checks
  are not universal semantic-equivalence or collision-freedom proofs. Docstring/comment
  removal is conditional on observability rather than unconditional deletion.
- **Transition:** original Fowler date verified as 2004-06-29, while the current
  URL is a later revision. Author essays remain historical/descriptive; official
  facade guidance and explicit task policy supply the bounded migration contract.
- **Evaluation:** prespecification, preregistration, blinding and Registered Reports
  are separated. FDA guidance is final, scoped and nonbinding. A generic CERN standard
  is unverified; the SLAC manuscript is not falsely called the inspected journal version.
- **Failure:** Nygard preview/copyright/printing verified without claiming full-book
  review. resilience4j documents configurable permits, not a universal single probe;
  stale state/equality/wait comments remain visible and unresolved. Containment and
  scientific failure accounting are explicitly local design policy, not product proof.

### Remaining limitations and next bounded step

Unseen journal/book chapters, denied endpoints and the abstract-only review remain
unverified as listed above. None supplies a missing normative rule. The strongest
competing explanation for an apparently robust workflow is that it enforces a
well-recorded but scientifically wrong observable/selection/decision contract;
Passing engineering gates alone cannot discriminate that explanation.

Next: the operator reviews the five narrowed boundaries and explicit policy choices,
especially AST observability and the single-probe recovery rule. If a concrete
resilience4j adoption is later requested, a separately scoped source-level inspection
of its exact internal state-machine boundaries is the bounded check for the retained
comment conflicts. No launch, numerical evaluation or installation follows automatically.
