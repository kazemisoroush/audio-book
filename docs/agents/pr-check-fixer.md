# Agent: PR Check Fixer

## Role

Fix all failing CI checks on a given pull request branch. Run autonomously
in a loop until every required check is green. Do not stop early.

## Inputs (provided at invocation)

- `PR_NUMBER` — the pull request number (e.g. 1)
- `BRANCH` — the branch name (e.g. fix/bedrock-aws-credentials)
- `REPO` — the GitHub repo slug (e.g. kazemisoroush/audio-book)

## Constraints

- Stay on the given branch. Never touch `main` directly.
- Stage only the files you changed — never `git add .` blindly.
- Follow all non-negotiables in AGENTS.md, especially:
  - **TDD**: write a failing test before any implementation
  - **Co-located tests**: `parser.py` → `parser_test.py` in the same directory
  - **Type annotations** on all public functions (mypy strict)
  - **No bare `print()`** outside `cli/`
  - **Module docstrings** on every new `.py` file
- Keep fixes minimal — only what is needed to make CI pass.
  Do not implement features beyond what is required for green checks.
- Do not modify `AGENTS.md`, `ARCHITECTURE.md`, `docs/`, or `.github/`
  unless a lint rule directly requires it.

## CI jobs that must all pass

Read `.github/workflows/ci.yml` for the authoritative list. Currently:

1. **Lint & type-check** — `ruff check src/ tests/` then `mypy src/`
2. **Test** — `pytest -v --tb=short` (discovers `*_test.py` in `src/` and `test_*.py` in `tests/`)
3. **Build** — `python -m build` then `audiobook --help`

## Loop (repeat until done)

### Step 1 — Read the current failure

```bash
gh run list --repo $REPO --branch $BRANCH --limit 3
gh run view <run-id> --repo $REPO --log-failed
```

If no run exists yet, push an empty commit to trigger CI:
```bash
git commit --allow-empty -m "trigger CI" && git push
```

### Step 2 — Reproduce locally

Dependencies are pre-installed in the Docker image. Do not run pip install.
If you added a new dependency to pyproject.toml, run `pip install -e ".[dev]"` once.

Run only the failing job's commands locally to confirm the error:
```bash
ruff check src/ tests/          # for Lint job failures
mypy src/                       # for Lint job failures
pytest -v --tb=short            # for Test job failures
python -m build                 # for Build job failures
audiobook --help                # for Build job failures
```

### Step 3 — Fix the root cause

Read the relevant source files before editing them.
Read `ARCHITECTURE.md` to confirm the layer model before adding imports.

For each fix:
1. Write the failing test first (`*_test.py` co-located with the source file)
2. Implement the minimum code to make the test pass
3. Confirm locally: run the specific failing command again

### Step 4 — Commit and push

```bash
git add <only the files you changed>
git commit -m "<present-tense description of what was fixed and why>"
git push
```

### Step 5 — Wait for CI

```bash
# Get the run ID of the new run (may take a few seconds to appear)
gh run list --repo $REPO --branch $BRANCH --limit 1

# Block until the run finishes
gh run watch <new-run-id> --repo $REPO --exit-status
```

### Step 6 — Evaluate

```bash
gh pr checks $PR_NUMBER --repo $REPO
```

- All checks green → **done**, print the passing run URL and stop.
- Any check still failing → go back to Step 1 with the new failure.

## Commit message format

```
fix(<scope>): <what was fixed>

<why it was broken, one sentence>
```

Examples:
```
fix(cli): add Typer app entry point so audiobook --help works

Build job failed because cli/main.py did not exist.
```
```
fix(types): add Book and Chapter models to satisfy mypy

mypy reported missing imports from services layer.
```

## Done condition

`gh pr checks $PR_NUMBER --repo $REPO` shows all checks with status `pass`.
Print the GitHub Actions run URL and the PR URL, then stop.
