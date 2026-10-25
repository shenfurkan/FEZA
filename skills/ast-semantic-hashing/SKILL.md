---
name: ast-semantic-hashing
description: "Designs and reviews computation-cache identities that survive formatting-only edits while invalidating on semantic, dependency, data, configuration, or environment changes. Use when a cache produces stale hits, when adding caching to an expensive analysis, or when deciding what an implementation identity must include. Do not use it to prove program equivalence, to validate cached results, or when observable inputs cannot be enumerated."
---

# AST Semantic Hashing

## When to use

- A cache misses after a whitespace-only reformat, or hits after a real code change.
- You are adding caching to an expensive parse, fit, or build step.
- You need to decide which code, data, and environment fields belong in a cache key.

## When not to use

- Docstrings, comments, line numbers, or reflection are observable and your normalizer
  cannot preserve their effects.
- Dynamic imports, external state, or generated code make the input set unknowable.
- You only need to navigate source; a lossy skeleton is not an executable identity.

## Inputs

- The actual parser, grammar, and normalizer versions you will use.
- A written list of observable outputs and side effects.
- The dependency lock, data inputs, configuration, and runtime environment.
- The digest and serialization contract, including field boundaries.
- The [normalization contract](references/normalization-contract.md) covers edge cases
  such as docstrings, type comments, and conditional compilation.

## Procedure

1. Write the observable contract first: what users, tests, logs, or downstream code
   can see. Include `__doc__`, tracebacks, and generated documentation if they matter.
2. List every input that can change those observables: source semantics, dependency
   versions, data files, configuration, environment, and random state.
3. Normalize only what the contract proves unobservable. Remove formatting and
   ordinary comments; keep docstrings unless nothing reads them; keep type comments,
   decorators, defaults, imports, and evaluation order.
4. If the parser drops a relevant token or fails, use a declared raw-source mode.
   Do not silently fall back to a partial AST.
5. Build a versioned key from explicit fields: normalized AST digest, parser and
   normalizer versions, dependency lock, data hashes, configuration, and environment.
   Serialize with typed boundaries; concatenating strings invites aliasing.
6. Store the raw source identity and a result manifest with the cached artifact.
   Missing, unreadable, or unknown inputs are a cache miss.
7. Validate with paired cases before trusting the cache in production.
8. For expensive outputs, keep a predeclared validation sample with independent
   expectations. Derive its size from risk, or label it a user-supplied starting value.

### Worked example

A spectral fitting function is cached by source identity. Reformatting the file and
reordering imports preserve behavior, so the key should not change. Changing a
default parameter, a decorator, or a docstring read by `__doc__` can change behavior, so
the key must change. Editing the calibration file or an environment variable that
selects a backend must also change the key even though the AST is identical. A parse
failure is a miss, not a reason to reuse the last result. The example is illustrative;
your observable contract decides each case.

## Failure modes

- **Semantic erasure:** discarded docstrings, type directives, or decorators affect results.
- **Incomplete closure:** changed data, native code, environment, or RNG state reuses a key.
- **Ambiguous encoding:** concatenated fields or unstable serialization alias identities.
- **False equivalence:** matching normalized syntax is advertised as a general proof.
- **Poisoned hit:** a valid key points to a partial, corrupted, or wrong output.

## Verification

- Reformat a file without changing behavior. The normalized key must stay equal.
- Change an operator, default, decorator, or observed docstring. The key must differ.
- Keep the AST identical while changing data, dependencies, configuration, or environment.
  The full key must differ.
- Corrupt or delete the cached output. The next lookup must miss or fail closed.
- Compare retained canonical payloads where a digest collision would matter. Finite
  fixtures cannot prove collision freedom or universal semantic equivalence.

## Provenance

- Unison, *The big idea*: definitions identified by syntax-tree hashes, with dependency
  hashes and positional binding references. This is a language-specific design, not a
  general Python or C++ normalizer.
- Bazel, *Remote Caching*: action inputs, output names, command line, environment,
  action cache, and content-addressed output store. It does not document source-AST hashing.
- Nix Reference Manual 2.34, *Store Derivation and Deriving Path*: derivations,
  process fields, and canonical serialized store objects.
- Do not assume another build system's cache is AST-based; verify its documented key.
  The full scientific key and observability rules are project policy, not a Bazel or
  Nix algorithm. A finite digest cannot guarantee no collision.

## Related locks

- [Quality ratchet](../quality-ratchet/SKILL.md) prevents silently weakening identity checks.
- [Strangler fig migration](../strangler-fig-migration/SKILL.md) separates old and new cache contracts.
- [Preregistered evaluation](../preregistered-evaluation/SKILL.md) binds evaluation to frozen code identity.
- [Circuit breaker isolation](../circuit-breaker-isolation/SKILL.md) quarantines corrupt cache consumers.
