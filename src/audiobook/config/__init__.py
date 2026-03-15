"""Configuration loading and validation.

Layer: config (may import from: types)

Loads all configuration from environment variables using pydantic-settings.
Configuration is validated at process startup — if required values are
missing or invalid, the process exits immediately with a clear error.

What this module does:
    - Defines Settings model (pydantic BaseSettings)
    - Loads from environment variables and optional .env file
    - Validates API keys, paths, and voice defaults at startup

What this module does NOT do:
    - No business logic
    - No external API calls
    - No file I/O beyond reading .env

Environment variables:
    ELEVENLABS_API_KEY  (required) ElevenLabs API key
    AUDIOBOOK_OUTPUT_DIR  (default: ./output) Where to write generated audio
    AUDIOBOOK_CACHE_DIR   (default: ~/.audiobook_cache) Where to cache segments
    AUDIOBOOK_LOG_LEVEL   (default: INFO) structlog log level
"""
