"""Core business logic — pure functions, no I/O.

Layer: domain (may import from: types, config)

CRITICAL CONSTRAINT: This layer has zero side effects.
No file reads, no API calls, no network, no randomness (unless seeded).
All functions take Pydantic models and return Pydantic models.

This makes the business logic:
    - Trivially testable (no mocks needed for I/O)
    - Readable without infrastructure knowledge
    - Reusable and composable

Modules:
    parser      — Text parsing: chapter splitting, dialogue attribution
    characters  — Character detection and voice assignment
    assembler   — Audio segment ordering and assembly plan

What this module does NOT do:
    - No file I/O (that lives in adapters/storage)
    - No ElevenLabs calls (that lives in adapters/elevenlabs)
    - No orchestration (that lives in services/)
"""
