---
name: reproducibility-auditor
description: "Audit reproducibility of a specified scientific result, stochastic computation or checkpoint. Distinguish byte identity, numerical agreement and distribution-level agreement; investigate an actual mismatch without turning routine scientific debugging into a full lineage audit."
---

# Reproducibility Auditor

Repeatability does not establish physical correctness. Specify the result and
replay claim under audit, then test that claim rather than demanding byte identity
for every scientific use.

## Define the replay level

| Claim | Appropriate comparison |
|---|---|
| File identity | Bytes/digests, including the declared metadata policy |
| Exact continuation | Adapted state, every required transition/draw, ordering and RNG state |
| Fixed numerical calculation | Observable differences against justified tolerances and error bounds |
| Independent stochastic runs | Applicable convergence, distribution/summary agreement and Monte Carlo uncertainty |

Different valid algorithms need not return identical samples. Identical seeds do
not guarantee identical streams across call patterns, versions, parallel schedules
or device builds. Nor does a changed archive timestamp prove changed science.

## Inspect only the relevant record

- Actual measured/simulated inputs, sample definition, selection, weights and units.
- Code/configuration and the environment that actually executed it: dependency,
  compiler/runtime, precision, hardware and relevant parallel/reduction settings.
- Generator/seed policy, algorithm initialization, continuation state and draw order.
- Calibration/model versions and processing steps that can change the result.

Use existing job records, configuration and environment definitions. Do not impose
a new file format, lock manager, Python version or manifest schema. Never fill an
unknown historical seed/version/hash with a plausible value.

## Execute the discriminating replay

1. Verify required inputs and snapshot identity for the chosen claim. A fresh hash
   cannot establish an unrecorded historical identity.
2. Run the actual implementation under the approved host/scope. A source review or
   mocked launcher cannot demonstrate replay or process isolation.
3. Compare results at the selected level and characterize differences. For a
   checkpoint, verify integrity, atomic recovery and RNG/state restoration; do not
   unpickle untrusted payloads or overwrite original evidence.
4. Distinguish platform/rounding effects from changed inputs, target distributions,
   missing transitions or corrupt state. Preserve unsuccessful attempts.

An attribution gap can prevent adoption of an old artifact without preventing an
independent new calculation on verified inputs. Actual corruption, wrong-source
data or unknown relevant units invalidate the affected result, not all science.

## Deliver

State the replay attempted, comparison precision, observed agreement/difference,
unexecuted scope and concrete blocker if any. Report proposed, launched and completed
replays distinctly. Do not generate a dossier file unless requested, or claim
scientific validity merely because the replay matches.
