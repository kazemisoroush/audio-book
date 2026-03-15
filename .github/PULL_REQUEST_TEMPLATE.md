## Summary

<!-- What does this PR do? 1–3 sentences from a user perspective. -->

## ExecPlan

<!-- Link to the ExecPlan in docs/exec-plans/ if one exists, or write "N/A" for small changes. -->

## How to validate

<!-- How can a reviewer (human or agent) verify this works?
     Be specific: commands to run, outputs to expect.
     Example:
       pip install -e ".[dev]"
       pytest tests/domain/test_parser.py -v
       # All tests pass; test_parse_empty_chapter is new and passes -->

## Checklist

- [ ] Tests written first (TDD) and all pass: `pytest tests/ -v`
- [ ] Lint and types pass: `ruff check src/ tests/ && mypy src/`
- [ ] New/changed public functions have type annotations
- [ ] New modules have a module-level docstring
- [ ] No `datetime.now()` or unseeded `random` in domain/services
- [ ] Docs updated if behaviour changed (ARCHITECTURE.md, product-specs, etc.)
- [ ] ExecPlan Progress section updated (if applicable)
