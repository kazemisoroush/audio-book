"""Audiobook generator package.

Converts plain-text books (Project Gutenberg format) into multi-voice
audiobooks using ElevenLabs TTS.

Layer model (dependency direction):
    types → config → adapters → domain → services → cli

Each layer may only import from layers to its left.
See ARCHITECTURE.md for the full module map and ADRs.
"""
