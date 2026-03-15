"""Orchestration services — wires domain and adapters together.

Layer: services (may import from: types, config, adapters, domain)

Services implement use cases by composing domain functions and adapter calls.
They are the only layer permitted to import from both domain/ and adapters/.

Services in this module:
    generator   — End-to-end audiobook generation workflow

What services do:
    - Call domain functions to compute what needs to happen
    - Call adapters to make it happen (read files, call APIs, write output)
    - Handle errors and translate them to user-facing messages
    - Report progress

What services do NOT do:
    - No business logic (that belongs in domain/)
    - No direct API calls (those go through adapters/)
    - No CLI argument parsing (that belongs in cli/)
"""
