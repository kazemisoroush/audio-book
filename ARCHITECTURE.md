# Architecture

## Domain decomposition

The codebase is organized into a single Python package `audiobook` with
internal modules mapping to business domains:

```
src/audiobook/
├── __init__.py
├── types/          # Shared Pydantic models, enums, type aliases
├── config/         # Config loading from env, validation at startup
├── adapters/       # External service clients (ElevenLabs, filesystem)
│   ├── elevenlabs.py
│   └── storage.py
├── domain/         # Core business logic — no I/O, no external calls
│   ├── parser.py       # Text parsing, chapter splitting
│   ├── characters.py   # Character detection and voice assignment
│   └── assembler.py    # Audio segment assembly ordering
├── services/       # Orchestration — wires domain + adapters together
│   └── generator.py    # End-to-end audiobook generation workflow
└── cli/            # CLI entry point (Typer)
    └── main.py
```

## Layer model and dependency rules

Layers are ordered. Each layer may ONLY import from layers to its left:

```
types  →  config  →  adapters  →  domain  →  services  →  cli
```

**What this means in practice:**
- `domain/` must never import from `adapters/` or `services/`
- `adapters/` must never import from `domain/` or `services/`
- `services/` orchestrates: it imports from both `domain/` and `adapters/`
- `cli/` only imports from `services/` and `config/`

These rules are enforced by a ruff custom rule (see `pyproject.toml`).
Violations fail CI and must be fixed before merge.

## Cross-cutting concerns

The following are not domain-specific and live in dedicated modules:

| Concern | Module | Notes |
|---|---|---|
| Logging | `audiobook.logging` | structlog wrapper, JSON output |
| Errors | `audiobook.errors` | Base error types, error codes |
| Retry / rate limiting | `audiobook.retries` | Used by adapters only |

Cross-cutting modules may be imported by any layer.

## Key architectural decisions

### ADR-001: Pydantic at all boundaries
All data crossing module edges (especially into/out of adapters) is modeled
with Pydantic. This makes data shapes inspectable and enforceable.
Rationale: agents can read Pydantic models to understand data shapes without
running the code.

### ADR-002: Domain layer has zero I/O
`domain/` functions are pure: they take Pydantic models in and return Pydantic
models out. No file reads, no API calls, no side effects.
Rationale: pure functions are trivially testable and legible to agents.

### ADR-003: ElevenLabs client is thin
The ElevenLabs adapter does one thing: call the API and return raw bytes.
Audio assembly logic lives in `domain/assembler.py`, not in the adapter.
Rationale: keeps business logic testable without API credentials.

### ADR-004: Config validated at startup
All config (API keys, output dirs, voice mappings) is loaded and validated
via Pydantic Settings at process startup. If config is invalid, the process
exits immediately with a clear error message.
Rationale: agents can read `config/` to understand all environment variables
the system needs.
