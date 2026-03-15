# Reliability

## Requirements

| Scenario | Requirement |
|---|---|
| ElevenLabs 429 (rate limit) | Retry with exponential backoff, max 5 attempts |
| ElevenLabs 5xx | Retry with exponential backoff, max 3 attempts |
| Network timeout | Retry once after 5s, then fail with resume instructions |
| Corrupted cache file | Detect (hash check), delete, regenerate |
| Partial run (killed mid-generation) | Resume from last completed segment |
| Invalid input file | Fail fast with clear error message before any API calls |

## Resume semantics

Each generated audio segment is cached at `~/.audiobook_cache/<book_hash>/<segment_index>.mp3`.
On restart, existing segments are skipped. This means a killed run can be
resumed by re-running the same command.

Cache invalidation: if the book file or voice mapping changes (detected by
content hash), the cache for that book is invalidated and regenerated.

## Logging

All significant events are logged as structured JSON to stderr:
- Segment generation start/complete (with segment index and duration)
- API errors and retry attempts
- Cache hits
- Final assembly start/complete

This allows agents to diagnose failures from logs without re-running.
