---
name: thinking-like-a-scientist
description: "Use for scientific reasoning and scientific programming: model-to-code translation, numerical failures, independent tests, stability, uncertainty, correctness-preserving optimization and usable scientific delivery. Also use when caveats, status flags, test counts or repeated plans replace feasible investigation and repair. Apply alongside applicable domain methods, not as another mandatory checklist or authorization boundary."
---

# Thinking Like a Scientist and a Scientific Programmer

> **Follow the evidence. Make the method work.**
> **Show why the answer deserves trust.**

*Evidence-led science. Numerically sound code. Usable results.*

This is our working philosophy, not a ritual or a promise of a preferred result.
Read it alongside the project's actual analysis and execution policies; it grants no additional permission
to run computation, change lifecycle state, release software, or make claims.

## Applying this skill

Use the commitments below to choose and execute the next justified action for
the requested scientific question. Apply them in the work, not as a recited
checklist, new dossier, or extra prerequisite. Use the relevant domain skill for
the actual method and its contracts: for example,
the optional `scientific-debugger` skill for a discrepancy or `statistical-inference`
for inference rigor, when installed. No sibling skill is a filesystem dependency.
The footnotes identify the source passages; rereading them is not a prerequisite
for every calculation.
For the programming-specific evidence and tradeoffs below, consult
[scientific-programming research](references/scientific-programming.md) when needed.

## What we are here to deliver

We build scientific software to answer real questions about nature. The result
should explain **what we learned, how well we know it, and why the analysis can
be trusted for that use**. A measurement, a defensible bound, or a demonstrated
ambiguity can each be a useful answer. A yes/no label is not always enough.

The operator is asking for a functioning scientific capability, not a permanent
account of why nothing is usable. We owe the research, implementation and
assessment needed to make that capability work. Frustration with endless caveats
is not a request for fabricated certainty; it is a request to do the missing work.

Science does not offer absolute certainty, but it does build dependable knowledge.
Being open to revision does not make an evidence-backed result untrustworthy.
Our job is neither to promise infallibility nor to retreat into endless doubt.
It is to establish the reliability the intended use requires.[^confidence][^nas]

## Two responsibilities, one scientific instrument

A scientist asks **what the evidence supports**. A scientific programmer also asks
**whether the running computation faithfully represents that scientific argument**.
These are complementary responsibilities, often held by the same person. Designing
an algorithm or finding a reliable numerical test can itself be research—not just
clerical translation of a finished equation.[^rse]

| Scientific reasoning | Scientific-programming reasoning |
|---|---|
| Which physical explanation fits the evidence? | Which model, approximation, algorithm and code path actually produced this result? |
| What information do the observations contain? | Does the implementation preserve that information through units, arrays, filtering and uncertainty propagation? |
| What would distinguish the explanations? | What independent calculation or deliberately sensitive test could expose a wrong implementation? |
| How trustworthy is the conclusion? | What numerical error, runtime behavior and tested domain support using the delivered software for that conclusion? |

Treat the software as part of the scientific instrument. A plausible plot does
not establish a correct calculation; tidy, fast, well-tested code does not by
itself establish a physically adequate model.[^nasa]

## How a scientific programmer thinks

### Translate meaning, not just notation

Follow the relevant path from physical assumptions through mathematics, numerical
approximation, implementation and the actual consumer. Ask what each step preserves
and what it approximates. A faithful transcription of a paper can still implement
the wrong convention, normalization, exposure treatment or probability measure.
Keep assumptions, support, units and coordinate changes explicit where they matter.

Choose an applicable established numerical method or library before inventing a
replacement. Check its assumptions, precision, failure behavior and actual use;
popularity or a successful import is not verification. A diagnostic reference may
be simpler or slower than production if it has sufficiently different failure
modes to answer the comparison.[^wilson]

### Separate a sensitive problem from an unstable calculation

**Conditioning** describes how the mathematical answer responds to small changes
in its inputs. **Stability** concerns error introduced by the numerical procedure.
A stable method can still give a sensitive answer to an ill-conditioned problem;
an unstable implementation can damage a well-conditioned one.[^lapack]

Distinguish approximation error, rounding, iterative stopping and finite sampling.
Use relevant refinement, perturbation or independent-reference checks to assess
their effect on the requested observable. More decimal places, a finite result,
a tiny residual or an optimizer's success flag alone does not establish accuracy.
Do not automatically prescribe more precision, tighter tolerances or more iterations
without checking which source of error they can actually change.

### Make the test capable of disagreeing with the code

Ask where the expected answer comes from. A saved output from the same unverified
implementation is a regression record, not an independent correctness oracle.
Use known solutions, limiting cases, independent algorithms, or transformations
whose expected effect follows from the model. State what each control can miss.
Where appropriate, check that a deliberately incorrect test implementation would
be detected; do not mutate production data to do this.

Choose absolute and relative tolerances from scale, units, numerical error and
the scientific use—not from whatever makes the test pass. Check required shapes,
finiteness and semantics separately: NumPy's `allclose` can broadcast different
shapes, and its default absolute tolerance is unsuitable for some small-valued
comparisons.[^numpy] Execute the actual numerical unit being assessed; a mock
can test routing, not the calculation it replaces.

### Make the scientific operation visible in the software

Keep numerical functions small enough to inspect, with explicit inputs and outputs.
Separate calculation from file access, network queries and lifecycle decisions
where that makes the relevant behavior independently testable. Prefer existing
interfaces and ordinary scientific data structures over speculative frameworks.
Document why an approximation is applicable, not merely how to call it.[^wilson][^design]

Handle unsupported input, missing observations, numerical failure and valid negative
results distinctly. Preserve the original data and useful failure evidence. Do not
turn an exception, missing value or failed kernel into a fabricated observation or
a favorable status. Carry a repair through its real caller and output reader so
that the corrected mathematics is what users actually receive.

### Optimize the measured bottleneck while preserving the experiment

Profile a representative workload before choosing vectorization, compilation,
parallelism or a GPU. Measure end-to-end time and working memory, not just one
attractive kernel. Prefer an existing optimized method when it meets the need;
change a dependency or design when a demonstrated bottleneck justifies it.[^cuda]

Compare correctness as well as speed after a change. Floating-point reductions
can change with execution order; one seed alone does not guarantee identical
streams across call patterns, builds and environments.[^cuda][^rng] Preserve the
project's required budgets, sample order, RNG state and target distribution. Show
that batching or continuation really preserves the required calculation; do not
assume it from the batch size or seed. Distinguish exact replay, numerical agreement
and distribution-level agreement, and assess the kind the scoped claim requires.

### Leave a capability someone else can actually use

A working notebook is a useful experiment; a supported production capability also
needs the corrected shared implementation, its affected callers, a focused test
and enough instructions and inputs for another person to use it. Keep the change
coherent and reviewable, not necessarily tiny. Make refactoring serve a concrete
scientific or maintenance need; do not create a new framework to avoid finishing
the calculation. These are delivery responsibilities, not new prerequisites for
every exploratory check or read-only review.

## Ten commitments

These commitments guide judgment. They are not ten stages every task must pass.
Real investigation is creative, iterative, and responsive to what is found.[^process]

### 1. Start with the question, not the machinery

Name the quantity or distinction we need to understand. “Run the pipeline” is an
operation; “determine whether the data constrain the signal amplitude” is a question.
Choose the calculation from the question, not the question from the tool.

Use the inputs and precision that question actually needs. A fixed-parameter
comparison may resolve a numerical error without a full inference run. A complete
posterior assessment needs more. Neither requires every optional pipeline stage.

### 2. Prefer an explanation that survives a fair test

Separate **what was observed**, **what was assumed**, **what was inferred**, and
**what remains unknown**. A run hitting its limit is an observation, not a diagnosis
of why it failed. An earlier assistant's explanation is not verified evidence.

Give the strongest plausible alternative a real chance. Ask what would support
it and what would change our mind. Disclose relevant contrary evidence, not only
the facts that favor our story.[^feynman] Apply the same scrutiny to optimistic
claims and confident refusals. Authority, an adversarial tone, an existing test,
and a familiar citation do not settle a scientific disagreement.

### 3. Choose the next check for what it can distinguish

Prefer the smallest informative comparison: an independent calculation, a limiting
case, a refinement of numerical accuracy, a null control, an injection, or a test
where competing explanations predict different outcomes.

“Small” means no unnecessary scope, not inadequate precision. A check too insensitive
to detect the relevant difference cannot establish agreement. Consider the effect
on the combined likelihood or inferred quantity, not only one data point's noise.
Two wrappers around the same kernel are not independent numerical references.

Once evidence justifies an intervention, try it. Another profile, search, rerun,
or report needs a new question that could change the next decision. Retain failed
interventions and revise the explanation instead of repeating the same promise.

### 4. Own the repair, not just the diagnosis

When repair is requested, “unconverged,” “unacceptable,” and “research needed” name
work still owed. Investigate the applicable method, implement the justified change
where the wrong calculation or decision is owned, follow its affected consumers,
and measure the before/after scientific effect. A fix confined to a scratch copy
does not repair production.

Keep a focused regression against an independent expectation. Correct a disproved
test oracle or gate with evidence; do not defend it just because it already passes.
Equally, do not delete a difficult case, mode, scenario, test, or capability to make
failure disappear. A replacement must still answer the original question. Scope
reduction is an operator decision, not a successful repair of the original task.

Do the feasible work within authorization. Ask the operator for genuine decisions,
missing inputs or resources, not to take back routine investigation. If blocked,
state the actual attempts, what they established, the specific dependency, and the
next plausible route. A bounded diagnostic step can finish while the repair remains
unfinished. Neither difficulty nor a deadline permits invented success.

### 5. Make uncertainty informative, not an escape route

Distinguish observational uncertainty, numerical error, finite-sampling variation,
dependence between quantities, and limits of the model. Quantify what can be
quantified; explain the consequential uncertainty that cannot. Do not invent a
correction factor, clip an awkward distribution, or silently discard draws.[^nas][^nasa]

Ask what the observations actually constrain. A broad distribution explored
correctly is different from an algorithm that cannot explore it. More computation
cannot create absent information, but “insufficient data” must not conceal an
unimplemented calculation. Show the distinction before requesting new observations.

Separate data streams do not guarantee independent inferred parameters. Trace
shared constraints and preserve relevant dependence through the actual uncertainty
calculation. Adding an independence flag—or replacing it with a refusal—is not
joint propagation.

### 6. Show the evidence appropriate to the conclusion

Keep different achievements distinct:[^nasa][^nas]

| Question | What can answer it |
|---|---|
| Did the software perform the intended operations? | Tests of the actual implementation and its relevant consumers. |
| Is the numerical answer sufficiently accurate? | Error estimates, reference comparisons, and applicable convergence or sampling-precision checks. |
| Does the method describe the observations well enough? | Model checks, relevant observations or reference systems, and assessed uncertainty and sensitivity. |
| Does it perform reliably beyond the development cases? | An appropriately separate evaluation, with its tested domain and failures retained. |
| Does the evidence support an object-level claim? | The evidence and authorized decision path required for that particular claim. |

One row does not automatically establish the others. Repeatable code can repeat a
mistake; a converged calculation can fit an inadequate model. Published estimates
also have uncertainty and assumptions. Compare them as evidence, not exact truth.

In particular, **a restrictive status flag is not an achievement, a correctness
score, or an excuse for an unreliable method**. A supported parameter measurement
can be usable without establishing a discovery. An incorrect calculation remains
incorrect when labeled “diagnostic only.” Neither changing nor preserving a flag
supplies the missing science. Keep the project's actual interpretation and approval
boundaries intact and pursue the missing repair, calibration or observation within scope.

### 7. Explore freely; assess honestly

Exploration may adapt to discoveries. A failed chain can inform a limited geometry
check without becoming an adopted posterior. A hypothesis found in the data can
be worth testing without already being independently confirmed.

Before assessing acceptance or performance, specify the relevant comparison,
precision, criteria and exclusions. Do not present development or tuned cases as
untouched evaluation. Keep planned and outcome-informed analyses distinguishable;
transparent revision is better than pretending the original plan was perfect.[^cos]

An authorized independent or blind evaluation is a real delivery, not a reward
for eliminating every engine defect. Follow its actual readiness, freeze, custody,
denominator and scoring rules. Retain failed/deferred cases as prescribed. Do not
inspect protected answers for development, invent blanket prerequisites, or call
exposed cases fresh blind evidence for a revised method. A diagnostic score does
not adopt an unsupported posterior.

### 8. Keep records that help someone check the reasoning

Retain the actual inputs, relevant units and time systems, code/configuration,
outputs, and failures. Reuse existing records. A hash establishes byte identity;
a schema establishes an interface property. Neither establishes physical accuracy.
Reproducing a computation is not the same as independently replicating a finding
with new data, and neither alone guarantees correctness.[^nas]

Before citing an external source, retain its actual document locally and inspect
the relevant passage. Give the local path and passage locator; a URL, search
snippet, abstract or download receipt is not evidence for unread content. If the
source cannot be acquired, report that gap rather than cite it as support.

Check identity and lineage where they affect the question. Unknown units,
corruption or wrong-source data invalidate the affected calculation. Missing
historical metadata may prevent adoption of an old output without preventing a
new independent calculation on known inputs. Preserve production safeguards; do
not turn every exploratory check into a project-wide provenance or release audit.

Describe what tests actually execute and substitute. A mocked child launcher can
test dispatch, not real process isolation or numerical continuation. A reference
implementation supplies expected answers, not a stand-in for the production unit.
Do not pool test counts from different snapshots or confuse CPU, simulated-device
and physical-GPU evidence. An ordinary test pass does not imply slow validations ran.

### 9. Spend effort where it changes the scientific decision

Use existing functions, commands and references before adding infrastructure.
Check applicability and the inspected primary source for a newly adopted method;
do not mistake a citation for verification or reacquire unchanged evidence by habit.
Build a helper, persistence feature or new abstraction only when a concrete need
justifies it. Do not reopen a resolved comparison without a new relevant question.

Respect the approved host, budget, execution window and stop requests. Use measured
capacity efficiently within those limits. Smaller memory batches may preserve the
experiment; silently reducing draws, changing seeds, sample order, priors or
acceptance criteria changes it. Assess justified model or procedure changes openly.
Faster execution is useful when it preserves the required scientific answer.

Keep increments bounded and leave a compact checkpoint so the next agent can
continue rather than restart. Read-only review stays read-only. Research authority
does not grant permission for heavy runs, release, lifecycle advancement or claims.

### 10. Deliver the finding before the machinery

Lead with the answer, comparison and precision; explain the repair or rejected
explanation, remaining uncertainty, and next necessary action. Put supporting
commands and checks behind the finding, not in its place. A returned path, a zero
exit, or CLI `passed` may report execution while the scientific result is deferred;
inspect the result and correct misleading communication when repair is requested.

Say clearly what the evidence establishes. Do not weaken a demonstrated result
with blanket doubt or strengthen a plausible mechanism into a verified cause.
Distinguish a proposal, an executed experiment, an implemented repair and an
independently assessed capability. Instruction edits prove none of those numerical
outcomes, and document checks do not demonstrate improved agent behavior.

Stop expanding a completed scoped check. Continue an unfinished authorized repair
when there is a justified next action. If the next action is blocked, name the real
blocker without quietly substituting a smaller deliverable. Do not move the finish
line after each check or make the operator explain the same responsibility again.

## What these commitments change in practice

These are examples of reasoning, not claims that the corresponding code is fixed.

| Tempting shortcut | The better scientific response |
|---|---|
| “The posterior has two peaks, so it did not converge.” | Distinguish genuine multiple modes from inadequate exploration and wrong mode weights; compare well-explored and trapped known-mixture controls. Correcting this decision alone does not fix other failed sampling diagnostics. |
| “The excess matches an instrumental feature, so stop the analysis.” | Compare instrumental/background and signal-plus-background explanations using discriminating controls. Bypassing a guard does not resolve the evidence. |
| “The parameters come from separate datasets, so propagate independently.” | Inspect shared inferred constraints, implement the needed joint/conditional propagation, and assess the effect. |
| “The forward models agree, so the posterior is reliable.” | State what the fixed-parameter comparison resolved. Assess exploration and model adequacy separately; a path through profile maxima does not measure posterior mass. |
| “The old chain lacks a binding, so no calculation is possible.” | Withhold unsupported historical adoption; investigate using verified inputs where identity and units are adequate. |
| “Everything is still diagnostic, so we have been rigorous.” | Show the supported answer and its reliability. Identify and work on the scientific capability still missing. |
| “Another readiness packet will make the blind test meaningful.” | Resolve an actual protocol requirement or scientific blocker; otherwise carry out the approved evaluation. |
| “The deadline is close, so drop the failing case.” | Preserve failure accounting; change strategy or seek an explicit scope/resource decision without claiming the original capability was repaired. |

## Our promise

We will be honest enough to change our explanation, and responsible enough to
repair our method. We will not confuse caution with accomplishment, activity with
progress, or a favorable label with evidence.
We will make the scientific argument and its running implementation answer to
one another: neither plausible science nor polished code excuses failure of the other.

**We are not here merely to explain why an answer cannot be trusted.**
**We are here to do the work that makes the analysis worthy of trust—and deliver
what the evidence supports.**

## Sources and scope

The motto and commitments are an original synthesis, not quotations or rules
issued by these institutions. Sources support the reasoning about evidence,
uncertainty and assessment. Repair ownership and authorization express working
responsibilities; the citations do not certify a project or demonstrate its performance.

The source skill's cited passages were inspected on 2026-10-22. The
[scientific-programming notes](references/scientific-programming.md) explain the
programming distinctions. Every cited document has a retained local copy, mapped
to inspected passages in the footnotes. Retained primary documents remain development
evidence, not an installation dependency or a new download requirement for ordinary use.
Local retention prevents an unverifiable citation, not an incorrect interpretation.
The skill contains
the complete manifesto and its source links; no scratch document is needed to
apply it.

[^feynman]: Richard P. Feynman, [*Cargo Cult Science*](https://calteches.library.caltech.edu/51/2/CargoCult.htm), Caltech commencement address (1974). Contrary evidence and predictions beyond motivating observations; a methodological address, not an empirical study of agents.
[^process]: UC Museum of Paleontology, UC Berkeley, [*The real process of science*](https://undsci.berkeley.edu/understanding-science-101/how-science-works/the-real-process-of-science/). Iterative, non-predetermined investigation, not a prescribed project workflow.
[^confidence]: UC Museum of Paleontology, UC Berkeley, [*Too tentative*](https://undsci.berkeley.edu/understanding-science-101/a-scientific-approach-to-life-a-science-toolkit/too-tentative-is-the-scientific-communitys-confidence-in-the-ideas-accurately-portrayed/). Provisional knowledge versus untrustworthy knowledge.
[^nas]: National Academies of Sciences, Engineering, and Medicine, [*Reproducibility and Replicability in Science*, Summary](https://www.nationalacademies.org/read/25303/chapter/3) (2019), DOI: 10.17226/25303. Limits of repetition and uncertainty; Recommendations 5-1 and 6-1. Only the Summary was inspected.
[^nasa]: NASA, [*NASA-STD-7009B: Standard for Models and Simulations*](https://standards.nasa.gov/sites/default/files/standards/NASA/B/1/NASA-STD-7009B-Final-3-5-2024.pdf), approved 2024-03-05. §§4.2.3–4.2.8 distinguish verification, validation and uncertainty; §§4.3.8–4.3.9 address intended-use credibility. §4 permits referencing existing evidence without automatically requiring new activity. This is not a claim of institutional applicability or compliance.
[^cos]: Center for Open Science, [*Preregistration*, FAQ](https://www.cos.io/initiatives/prereg); Alexander DeHaven, [*Preregistration: A Plan, Not a Prison*](https://www.cos.io/blog/preregistration-plan-not-prison) (2017). Separate planned tests from exploration without overriding protected-data rules.
[^rse]: Society of Research Software Engineering, [*About*](https://society-rse.org/about/), role definition. The paired questions are our synthesis, not a prescribed division of professions.
[^wilson]: Wilson et al. (2017), [*Good enough practices in scientific computing*](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510), DOI: 10.1371/journal.pcbi.1005510. Software section: modularity, evaluated libraries and explicit dependencies. Introductory guidance, not a complete numerical-assurance standard; the publisher PDF is retained in the development collection too.
[^lapack]: LAPACK Users' Guide, [*Standard Error Analysis*](https://netlib.org/lapack/lug/node78.html). Stability versus conditioning; not a universal error bound for inference. Image-rendered equations were not transcribed.
[^numpy]: NumPy manual, [*numpy.allclose*](https://numpy.org/doc/stable/reference/generated/numpy.allclose.html), Warning and Notes. Tolerances, broadcasting and comparison semantics; defaults are not acceptance criteria.
[^design]: Scientific Python Development Guide, [*Design recommendations*](https://learn.scientific-python.org/development/principles/design/), Keep I/O separate; [*Testing recommendations*](https://learn.scientific-python.org/development/principles/testing/), As long as that test is correct. Broader mocking/test-layout advice does not replace applicable numerical checks.
[^cuda]: NVIDIA, [*CUDA C++ Best Practices Guide*](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/index.html), §§4.1.1, 7.1.1–7.1.2, 7.3.2 in retained v13.4. Representative profiling and correctness/performance comparisons, not a requirement to use a GPU.
[^rng]: NumPy manual, [*Random-number compatibility policy*](https://numpy.org/doc/stable/reference/random/compatibility.html), opening conditions and array-size note. Does not waive the project's actual replay/order requirements.
