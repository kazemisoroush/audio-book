# Core Beliefs

These are the non-negotiable operating principles for this project. They are
agent-first: optimized for what allows agents to work reliably, not for what
humans would naturally prefer.

## 1. If it's not in the repo, it doesn't exist

Knowledge in Slack, email, or someone's head is not accessible to agents.
Every decision, rationale, and constraint must be encoded as a versioned
artifact in this repository. This includes architecture decisions (ADRs in
ARCHITECTURE.md), design decisions (docs/design-docs/), and product specs.

## 2. Validate at every boundary with Pydantic

Raw dicts and untyped data are agent-illegible. Every data shape crossing a
module boundary must be a Pydantic model. Agents can read models and infer
behavior; they cannot reliably infer behavior from implicit dict shapes.

## 3. The domain layer is pure

`audiobook/domain/` has zero side effects. No file I/O, no API calls, no
network. Pure functions in, pure functions out. This makes the most important
business logic trivially testable and readable without infrastructure.

## 4. Boring tech compounds

We prefer dependencies with stable APIs, extensive documentation, and wide
training-set representation. An agent can reason about `pydantic`, `typer`,
and `structlog` from first principles. It cannot reliably reason about
obscure or rapidly-changing libraries.

When in doubt: reach for the stdlib. When stdlib is insufficient: reach for
the most widely-used option. Never introduce a dependency for convenience
that a 20-line utility function would serve.

## 5. Mechanical enforcement over documentation

A rule that is only written in a doc will be forgotten. A rule enforced by a
linter, test, or CI gate is always applied. When a belief becomes important
enough, promote it from documentation to tooling.

## 6. Tests are the contract

Every public function in `types/` and `domain/` has a test. Tests are not an
afterthought — they are how agents verify their own output and how humans
verify agent output. A PR with failing tests is not ready for review.

## 7. Corrections are cheap, waiting is expensive

At high agent throughput, blocking on perfection compounds cost. Merge short-
lived PRs. Fix issues with follow-up PRs. Prefer a working 80% solution
shipped today over a perfect solution that blocks for a week. Technical debt
is paid down continuously via the garbage-collection cadence, not in bursts.

## 8. Test-driven development — tests define intent, not verify it

Write the test before the implementation. This is not a style preference —
it is how agents produce verifiable, non-hallucinated output.

The order is:
1. Write a failing test that precisely describes the expected behavior
2. Implement the minimum code to make it pass
3. Refactor if needed, keeping the test green

Why this matters for agents specifically: a test written after implementation
tends to describe what the code does, not what it should do. A test written
first is a specification. The agent cannot claim "done" until a real test
(not just the happy path) passes.

Practical rules:
- For domain functions: write the test, then the function body — no exceptions
- For adapters: write an integration test stub first; mock at the adapter
  boundary so domain tests remain fast and pure
- For services: write an end-to-end test describing user-visible behavior
  first; then wire the domain and adapters together to satisfy it
- A test that only tests the happy path is incomplete — write at least one
  error/edge-case test per function before considering it done

**Test file co-location (Go-style):** unit test files live next to the module
they test, named with a `_test.py` suffix:

```
src/audiobook/domain/parser.py        ← implementation
src/audiobook/domain/parser_test.py   ← unit tests for parser.py
```

This makes the test immediately discoverable when reading the code, ensures
tests move with the code they cover, and makes it obvious when a module has
no tests. The `tests/` directory at the project root is reserved exclusively
for integration tests that span multiple modules and cannot belong to a
single source file.

## 9. Push everything toward determinism

Given the same inputs, the system must always produce the same outputs.
Determinism is what makes agent-generated code testable, debuggable, and
trustworthy.

Concrete rules for this project:
- **No `datetime.now()` or `time.time()` in domain or service logic** — accept
  a timestamp as a parameter instead; tests pass a fixed value
- **No `random` without an explicit seed** — character voice assignment uses
  a seed derived from the book's content hash, so the same book always gets
  the same voices
- **No unordered iteration over sets or unordered dicts** — always sort before
  iterating when order affects output
- **No environment-dependent behavior in tests** — tests set all config
  explicitly; they do not read from actual env vars or the filesystem
- **Audio segment assembly is ordered by position in the source text**, not
  by generation time or filesystem order
- **Dependency versions are pinned** — same code, same environment, same
  behavior across runs

When a function cannot be deterministic (e.g., it calls an external API that
returns variable data), document that explicitly in its docstring and isolate
it behind an adapter boundary so the non-determinism is contained.

## 10. Module docstrings are the primary unit of knowledge

Every module (`__init__.py`, top of each `.py` file) begins with a docstring
explaining: what this module does, what it doesn't do, its key constraints,
and its place in the layer model. Agents read module docstrings before reading
function bodies.
