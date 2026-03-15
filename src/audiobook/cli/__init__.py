"""Command-line interface entry point.

Layer: cli (may import from: types, config, services)

The CLI layer parses user arguments, initializes config, and delegates
all work to services/. It contains no business logic.

Entry point: audiobook.cli.main — defines the Typer app.

Commands:
    audiobook <book_file>                    Generate audiobook
    audiobook <book_file> --discover-characters   Detect characters and voices only

What this module does NOT do:
    - No business logic
    - No direct domain or adapter calls (goes through services/)
    - No I/O beyond printing progress and errors to stdout/stderr
"""
