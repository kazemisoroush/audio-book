# ElevenLabs API Reference (agent-readable summary)

This is an in-repo summary of the ElevenLabs API patterns used by this
project. It is maintained here so agents don't need to fetch external docs.

## Authentication

All requests require the header:
```
xi-api-key: <ELEVENLABS_API_KEY>
```

The API key is loaded from the `ELEVENLABS_API_KEY` environment variable
by `audiobook.config`.

## Text-to-speech endpoint

```
POST https://api.elevenlabs.io/v1/text-to-speech/{voice_id}
```

Request body (JSON):
```json
{
  "text": "Text to synthesize",
  "model_id": "eleven_monolingual_v1",
  "voice_settings": {
    "stability": 0.5,
    "similarity_boost": 0.75
  }
}
```

Response: raw audio bytes (MP3 by default).

Add `?output_format=mp3_44100_128` for explicit format selection.

## Voice listing

```
GET https://api.elevenlabs.io/v1/voices
```

Response shape (relevant fields):
```json
{
  "voices": [
    {
      "voice_id": "21m00Tcm4TlvDq8ikWAM",
      "name": "Rachel",
      "labels": { "accent": "american", "gender": "female" }
    }
  ]
}
```

## Rate limits and error codes

| Code | Meaning | Action |
|---|---|---|
| 200 | Success | — |
| 400 | Bad request | Log and fail — do not retry |
| 401 | Invalid API key | Exit immediately with clear message |
| 422 | Text too long (>5000 chars) | Split text and retry |
| 429 | Rate limited | Retry with exponential backoff |
| 5xx | Server error | Retry with exponential backoff |

## Retry policy (as implemented in `audiobook.retries`)

- Base delay: 1 second
- Backoff factor: 2x
- Max retries: 5 for 429, 3 for 5xx
- Max delay cap: 60 seconds

## Voice IDs used in this project

The voice assignment is managed in the user's `<book>.voices.json` file.
Default voices for character discovery are defined in `audiobook.config`.

Common starting voices (from ElevenLabs free tier):
- `21m00Tcm4TlvDq8ikWAM` — Rachel (female, American)
- `AZnzlk1XvdvUeBnXmlld` — Domi (female, American)
- `EXAVITQu4vr4xnSDxMaL` — Bella (female, American)
- `ErXwobaYiN019PkySvjV` — Antoni (male, American)
- `MF3mGyEYCl7XYWbV9V6O` — Elli (female, American)
- `TxGEqnHWrfWFTfGW9XjX` — Josh (male, American)
- `VR6AewLTigWG4xSOukaG` — Arnold (male, American)
- `pNInz6obpgDQGcFmaJgB` — Adam (male, American)
- `yoZ06aMxZJJ28mfd3POQ` — Sam (male, American)
