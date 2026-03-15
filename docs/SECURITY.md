# Security

## API key handling

- `ELEVENLABS_API_KEY` is loaded from environment only. Never hardcoded.
- The config layer validates presence at startup and exits with a clear error
  if missing. No lazy loading — fail fast.
- Keys must never appear in logs. The structlog configuration redacts any
  field named `*key*`, `*token*`, `*secret*`, or `*password*`.

## Input validation

- Book file paths are resolved and validated before processing. Path traversal
  is prevented by resolving to absolute paths and confirming they are within
  the working directory.
- Voice mapping JSON is parsed with Pydantic. Unexpected fields are rejected.

## Dependencies

- Dependencies are pinned in `requirements.txt` with exact versions.
- No dependency should be added without a clear justification and a check
  for known CVEs at time of addition.

## What agents must not do

- Never log API keys, tokens, or secrets
- Never write user data outside the configured output and cache directories
- Never make network requests to endpoints not defined in `config/`
