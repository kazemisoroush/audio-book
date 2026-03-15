# Agent Fleet

This directory defines the agents that work in this repository.
Each file is a self-contained role definition used as the prompt
when spawning an agent via Claude Code's Task tool.

## Registry

| Agent | File | Trigger | Purpose |
|---|---|---|---|
| PR Check Fixer | [pr-check-fixer.md](pr-check-fixer.md) | Manual / on failing PR | Makes all CI checks pass on a given PR branch |

## How to invoke an agent

From Claude Code, reference the agent definition and provide context:

```
Read docs/agents/pr-check-fixer.md, then fix PR #<N> on branch <branch-name>.
```

## How to add an agent

1. Create `docs/agents/<name>.md` following the structure in existing definitions
2. Add it to the registry table above
3. Open a PR — harness files require human review (see CODEOWNERS)
