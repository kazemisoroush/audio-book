# Contributing

## Working model

**Humans steer. Agents execute.**

Engineers write prompts and ExecPlans that describe intent. Agents implement,
test, and open pull requests. Humans and agents both review. No one pushes
directly to `main`.

## Branch and PR workflow

```
main  (protected — no direct pushes)
  └── feature/short-description   ← all work happens here
```

1. **Create a branch** from `main`:
   ```bash
   git checkout -b feature/my-thing
   ```

2. **Write an ExecPlan** if the work spans multiple modules or sessions
   (see [docs/PLANS.md](docs/PLANS.md)):
   ```bash
   # create docs/exec-plans/active/NNN-my-thing.md
   ```

3. **Implement using TDD** — write the failing test first, then the code.
   Run locally before pushing:
   ```bash
   pip install -e ".[dev]"
   ruff check src/ tests/
   mypy src/
   pytest tests/ -v
   python -m build
   ```

4. **Open a PR to `main`**. Fill in the PR template.

5. **CI runs automatically** (lint → test → build). All three must be green
   before merge.

6. **Agent review runs automatically** on every PR open and every push.
   Claude reads the diff against the project's core beliefs and posts review
   comments.

7. **Address feedback** — respond to comments (agent or human), push fixes
   to the same branch. The agent re-reviews on each push.

8. **Merge** once CI is green and the agent review is satisfied.
   Squash merge is preferred to keep `main` history clean.

## Naming conventions

| Type | Pattern | Example |
|---|---|---|
| Feature branch | `feature/<short-description>` | `feature/character-detection` |
| Fix branch | `fix/<short-description>` | `fix/retry-on-429` |
| Docs branch | `docs/<short-description>` | `docs/update-architecture` |
| ExecPlan file | `NNN-short-description.md` | `001-text-parser.md` |

## CI gates (all required to merge)

| Job | What it checks |
|---|---|
| `lint` | `ruff check` + `mypy` — no violations |
| `test` | `pytest` — all pass, coverage ≥ 80% |
| `build` | `python -m build` succeeds, `audiobook --help` works |

## Agent review

Every PR gets a Claude review automatically. The agent checks:
- TDD compliance (tests exist for new functions)
- Layer dependency violations
- Determinism issues (`datetime.now()`, unseeded random)
- Pydantic boundary enforcement
- Domain vocabulary in names
- Module docstrings on new modules

You can also ask Claude questions or request re-review by commenting:
```
@claude Can you check whether the retry logic handles a 422 correctly?
```

## Repository setup (first-time, maintainers only)

After pushing to GitHub, apply branch protection:

```bash
# 1. Authenticate
gh auth login

# 2. Create and push the repo
gh repo create audio-book --public --source=. --remote=origin --push

# 3. Protect main: require CI to pass, no direct pushes, no force pushes
gh api repos/{owner}/audio-book/branches/main/protection \
  --method PUT \
  --input - <<'EOF'
{
  "required_status_checks": {
    "strict": true,
    "contexts": ["Lint & type-check", "Test", "Build"]
  },
  "enforce_admins": true,
  "required_pull_request_reviews": {
    "required_approving_review_count": 0,
    "dismiss_stale_reviews": true
  },
  "restrictions": null,
  "allow_force_pushes": false,
  "allow_deletions": false
}
EOF

# 4. Add AWS credentials for agent review (Bedrock)
#    See "AWS credentials setup" below for the required IAM policy.
gh secret set AWS_ACCESS_KEY_ID     --body "<your-access-key-id>"
gh secret set AWS_SECRET_ACCESS_KEY --body "<your-secret-access-key>"
```

## AWS credentials setup (for agent review workflow)

The agent review workflow authenticates to AWS Bedrock using static IAM
credentials stored as GitHub Actions secrets.

Required secrets (set once per repo):
```bash
gh secret set AWS_ACCESS_KEY_ID     --body "<your-access-key-id>"
gh secret set AWS_SECRET_ACCESS_KEY --body "<your-secret-access-key>"
```

The IAM user needs this policy attached:
```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": ["bedrock:InvokeModel", "bedrock:InvokeModelWithResponseStream"],
    "Resource": "arn:aws:bedrock:us-east-1::foundation-model/anthropic.*"
  }]
}
```

## What agents must never do

- Push directly to `main`
- Skip CI by adding `[skip ci]` to commit messages
- Commit `.env` files or API keys
- Open a PR without running tests locally first
