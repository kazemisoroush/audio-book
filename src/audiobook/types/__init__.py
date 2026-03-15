"""Shared Pydantic models, enums, and type aliases.

Layer: types (leftmost — may not import from any other audiobook module)

This module defines the data contracts used across the entire codebase.
All data shapes that cross module boundaries must be defined here.

What this module does:
    - Defines Pydantic models for books, characters, voices, segments
    - Defines enums for speaker types, audio formats, etc.
    - Defines type aliases for common primitives

What this module does NOT do:
    - No I/O, no validation of external data, no business logic
    - No imports from other audiobook modules
"""
