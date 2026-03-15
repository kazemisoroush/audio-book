# Design Philosophy

## Agent-first legibility

Every file in this repository is optimized first for agent legibility. This
means: clear module docstrings, Pydantic models for all data shapes, no hidden
state, and all constraints encoded mechanically (linters, tests).

If an agent reading a file can't determine what it does and what it expects
without running the code, the file needs better docs or cleaner structure.

## Explicit over implicit

- Configuration is explicit: all env vars are documented in `config/` and
  validated at startup. No surprising defaults.
- Data shapes are explicit: Pydantic models, never raw dicts at module edges.
- Dependencies are explicit: layer model enforced by linter, no surprise
  imports from higher layers.

## Small, focused modules

Each module does one thing. `domain/parser.py` parses text. It does not
detect characters. `domain/characters.py` detects characters. It does not
parse text. This keeps modules short enough that an agent can hold the full
context of a module in one read.

## CUPID properties

Code in this project follows Dan North's CUPID properties as a design lens.
Each property maps to concrete, enforceable practices here:

**Composable** — modules and functions play well with others.
A composable function has a focused purpose, takes well-typed inputs, and
returns well-typed outputs. It doesn't reach for global state or hidden
context. In this project: domain functions take Pydantic models and return
Pydantic models; they can be freely combined into new workflows without
coupling to infrastructure. Adapters are swappable — the ElevenLabs adapter
could be replaced with a local TTS adapter without touching domain logic.

**Unix philosophy** — each module does one thing well.
Already encoded in "Small, focused modules" below. Reiterated here because
CUPID names it explicitly: when a module starts doing two things, split it.
A good sign that a split is needed: the module docstring uses the word "and".

**Predictable** — code does what you expect, every time.
No hidden behavior, no environment-sensitive defaults, no spooky action at a
distance. Closely tied to core-beliefs #10 (Determinism). Predictability is
what makes a module legible to an agent reading it cold: the function name
and signature should fully predict the behavior. If it doesn't, the function
needs to be renamed, documented, or decomposed.

**Idiomatic** — feels natural in Python.
Use the language's idioms: generators for lazy sequences, context managers
for resource lifetimes, dataclasses/Pydantic for structured data, `pathlib`
for paths, `typing.Protocol` for structural interfaces. Avoid patterns that
make sense in other languages but feel unnatural in Python (e.g., Java-style
factory hierarchies, explicit null checks instead of `Optional`). Idiomatic
code is easier for agents to extend because it matches training-data patterns.

**Domain-based** — uses the vocabulary of audiobooks, not programming.
Names should reflect the problem domain. Prefer `chapter`, `speaker`,
`dialogue`, `narration`, `voice`, `segment`, `assignment` over `item`,
`entity`, `handler`, `manager`, `processor`, `util`. When an agent or a new
engineer reads the code, they should be able to map it to the product spec
in `docs/product-specs/audiobook-generation.md` without a translation layer.

## The module docstring contract

Every `.py` file begins with a module-level docstring that answers:
1. What does this module do?
2. What does it NOT do (boundaries)?
3. What are its key constraints?
4. Where does it sit in the layer model?

This is non-optional and enforced by a ruff lint rule.
