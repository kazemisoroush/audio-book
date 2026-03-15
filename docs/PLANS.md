# Execution Plans (ExecPlans)

This document defines the format for ExecPlans — design documents that guide
an agent (or a novice human) through implementing a complex feature end-to-end.

ExecPlans live in `docs/exec-plans/active/` while in progress and move to
`docs/exec-plans/completed/` when done.

---

## When to use an ExecPlan

Use an ExecPlan for any work that:
- Spans more than two modules
- Requires research before implementation
- Involves an external API or infrastructure change
- Could take more than one agent session to complete

For small, well-scoped tasks (single function, clear implementation), a PR
description is sufficient — no ExecPlan needed.

Reference this file in `AGENTS.md` as: `docs/PLANS.md`

---

## Requirements (non-negotiable)

- **Self-contained**: Contains all knowledge needed for a novice to succeed.
- **Living document**: Updated as progress is made, decisions are finalized,
  and surprises are discovered. Each revision must remain self-contained.
- **Observable outcomes**: Acceptance is phrased as behavior a human can
  verify, not internal code attributes.
- **Novice-guiding**: Names files with full repo-relative paths, shows exact
  commands with expected output, defines all non-obvious terms.

---

## Format

Each ExecPlan is a single Markdown file. When writing to a `.md` file where
the content *is only* the ExecPlan, omit triple-backtick wrapping.

Write in plain prose. Prefer sentences over lists. Avoid checklists except
in the `Progress` section where they are mandatory.

Use two newlines after every heading.

---

## Required sections

Every ExecPlan must contain and maintain these sections:

### Progress
A checklist of granular steps with timestamps. Must always reflect actual
current state. Format:
```
- [x] (2025-10-01 13:00Z) Completed step description.
- [ ] Incomplete step description.
- [ ] Partially completed (done: X; remaining: Y).
```

### Surprises & Discoveries
Unexpected behaviors, bugs, or insights found during implementation.
Include concise evidence (test output preferred).

### Decision Log
Every decision made while working. Format:
```
- Decision: ...
  Rationale: ...
  Date/Author: ...
```

### Outcomes & Retrospective
Summary at major milestones or completion: what was achieved, what remains,
lessons learned.

---

## Skeleton

    # <Short, action-oriented description>

    This ExecPlan is a living document. Maintain Progress, Surprises &
    Discoveries, Decision Log, and Outcomes & Retrospective as work proceeds.
    This document follows the format defined in docs/PLANS.md.

    ## Purpose / Big Picture

    Explain what someone gains after this change and how they can see it
    working. State the user-visible behavior being enabled.

    ## Progress

    - [ ] Step one.
    - [ ] Step two.

    ## Surprises & Discoveries

    (none yet)

    ## Decision Log

    (none yet)

    ## Outcomes & Retrospective

    (not yet complete)

    ## Context and Orientation

    Describe the current relevant state as if the reader knows nothing. Name
    key files by full path. Define non-obvious terms.

    ## Plan of Work

    Prose description of the sequence of edits. For each edit: name the file,
    location, and what to change.

    ## Concrete Steps

    Exact commands to run with working directory and expected output transcript.

    ## Validation and Acceptance

    How to exercise the system and what to observe. Phrase as behavior with
    specific inputs and outputs.

    ## Idempotence and Recovery

    If steps can be repeated safely, say so. If risky, provide retry/rollback.

    ## Interfaces and Dependencies

    Name the libraries, modules, and services to use. Specify types and
    function signatures that must exist at the end.
