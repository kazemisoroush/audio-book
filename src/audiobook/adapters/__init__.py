"""External service adapters.

Layer: adapters (may import from: types, config)

Adapters are thin wrappers around external systems. Each adapter:
    - Does one thing: call an external service and return typed data
    - Uses Pydantic models from types/ for all inputs and outputs
    - Implements retry logic via audiobook.retries
    - Never contains business logic

Adapters in this module:
    elevenlabs  — ElevenLabs TTS API client
    storage     — Filesystem: reading books, writing/reading audio cache

See docs/references/elevenlabs-reference.md for API patterns.
"""
