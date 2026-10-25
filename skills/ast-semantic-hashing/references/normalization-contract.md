# Conservative structural identity

## Primary basis and corrected attribution

1. Unison, [The big idea](https://www.unison-lang.org/docs/the-big-idea/), snapshot
   2026-10-25. The opening `increment` example explicitly identifies definitions
   by a syntax-tree hash, replaces named arguments with positional references, and
   references dependencies by their hashes. “No builds” limits its test-caching
   example to pure deterministic computations without I/O. This is a particular
   language design, not a sound normalizer for arbitrary Python, C++, or notebooks.
2. Bazel, [Remote Caching](https://bazel.build/remote/caching), HEAD documentation,
   snapshot 2026-10-25, “Overview”: actions have inputs, output names, command line,
   and environment; the action cache maps action hashes to result metadata, while
   CAS holds output files. “Known issues” discusses concurrent input changes,
   environment leakage, and tools outside the workspace. It supplies no source-AST
   hashing guarantee and expressly exposes incomplete-identity risks.
3. Nix, [Store Derivation and Deriving Path](https://nix.dev/manual/nix/2.34/store/derivation/),
   version 2.34, “Store Derivation”, “Process creation fields” and “Encoding”. Derivations
   specify a process, inputs and outputs, including platform/builder/arguments/
   environment. Their canonical serialized store objects are content-addressed.
   The document also discusses content-addressing derivations whose output paths
   are not known beforehand. Do not collapse all Nix modes into file hashes, or
   mistake a serialized derivation representation for a source program's AST.

The key composition below is project policy. It is not copied
from an unseen paper or presented as the implementation of any of these products.

## Identity record

| Component | Contract |
|---|---|
| Source | Raw bytes digest and snapshot identity, retained separately |
| Syntax | Canonical representation, language/grammar, parser/options |
| Normalization | Version, removed fields, observability rationale, unsupported modes |
| Digests | Algorithm, schema/domain tag, component hashes, field boundaries |
| Dependencies | Lock identity plus actual resolved code/native artifacts |
| Inputs | Data/calibration hashes, masks, selection/configuration and relevant units |
| Environment | Runtime/compiler/native libraries, device/precision/settings as relevant |
| Randomness | Generator, state/seed, continuation/draw and parallel-order contract |
| Result | Output hashes, completeness/validation status, independent validation evidence |

Do not write secrets into environment records. An unresolved secret-dependent
computation needs an approved protected identity mechanism or no cache reuse;
neither the value nor a guessed substitute belongs in this record.

## Removal decisions

| Candidate removal | Condition for normalization |
|---|---|
| Spaces and formatting | Not meaningful indentation/tokens/literal contents or observed source bytes |
| Ordinary comments | Not consumed by a preprocessor, generator, type tool, or application |
| Docstrings | No runtime `__doc__`, documentation output, reflection, or other declared consumer |
| Source locations | Not needed for observed tracebacks, inspection, debugging, or output |
| Identifier spelling | Preserve unless a language-specific, justified binding rule establishes safety |
| Import/decorator/default order | Preserve; do not infer that reordered evaluation is harmless |

Semantic observability is an input contract, not something proved by the mere
absence of a text search hit. If dynamic behavior prevents establishing it, retain
the original representation or disable normalized reuse. A documented raw-source
mode is a distinct identity contract, not an undocumented fallback after parse failure.

## Review cases

- A presentation-only pair should have identical canonical bytes and key under
  its declared contract. A change inside a string literal is not presentation-only.
- A changed operator, condition, decorator, import dependency or observed docstring
  should change the canonical payload and key in the relevant contract.
- Equal ASTs with changed data, dependency artifacts or environment require a miss.
- A stochastic result cannot be replayed from an AST and a seed alone when draw
  ordering, generator version or continuation state changed.
- Deliberately aliased field boundaries must be rejected by typed serialization.
- If equal digests conceal different retained payloads, stop reuse and preserve
  the discrepancy. No finite fixture collection guarantees collision freedom.

Validation-sample size, allowed numerical discrepancy and recheck frequency need
an explicit derivation or a user-supplied starting-value label. Hash algorithm names,
version identifiers and bibliographic dates are identifiers, not acceptance thresholds.
