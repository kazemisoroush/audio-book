# Design Docs Index

Design documents capture significant decisions and the reasoning behind them.
They are not tutorials — they are the answer to "why does it work this way?"

| Document | Status | Summary |
|---|---|---|
| [core-beliefs.md](core-beliefs.md) | Active | Operating principles for this project |

## How to add a design doc

1. Create a file in `docs/design-docs/` named `NNN-short-title.md`
2. Add it to the table above with status (Draft / Active / Superseded)
3. Reference it from the relevant module docstring or ARCHITECTURE.md ADR

## Status values

- **Draft** — under discussion, not yet authoritative
- **Active** — current, enforced, relied upon
- **Superseded** — replaced by a newer doc (keep for history, link to replacement)
