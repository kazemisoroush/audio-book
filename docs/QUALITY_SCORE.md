# Quality Score

This document grades each domain and layer of the codebase on quality.
It is updated by agents as implementation progresses.

Grades: A (excellent) / B (good) / C (needs work) / D (poor) / — (not yet built)

## Domain grades

| Domain | Test coverage | Type safety | Docs | Overall |
|---|---|---|---|---|
| `types/` | — | — | — | — |
| `config/` | — | — | — | — |
| `adapters/elevenlabs` | — | — | — | — |
| `adapters/storage` | — | — | — | — |
| `domain/parser` | — | — | — | — |
| `domain/characters` | — | — | — | — |
| `domain/assembler` | — | — | — | — |
| `services/generator` | — | — | — | — |
| `cli/` | — | — | — | — |

## Grade definitions

**Test coverage**
- A: ≥95% line coverage, all edge cases covered
- B: ≥80%, happy path + main error cases covered
- C: ≥60%, happy path only
- D: <60% or untested error paths

**Type safety**
- A: mypy strict passes, no `Any`, no `# type: ignore`
- B: mypy passes with minor ignores, documented
- C: mypy passes in default mode
- D: mypy errors or not checked

**Docs**
- A: Module docstring + all public functions have docstrings
- B: Module docstring + most public functions documented
- C: Module docstring only
- D: No module docstring

## Enforcement

The CI gate requires:
- `domain/` and `types/`: test coverage ≥ 95% (pytest-cov)
- All modules: mypy strict
- All modules: ruff passes

Grades below C in `domain/` or `types/` block merge.
