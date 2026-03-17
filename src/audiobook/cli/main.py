"""CLI entry point for the audiobook generator.

Layer: cli (may import from: types, config, services)

Defines the Typer application and top-level commands. All business logic
is delegated to services/; this module only handles argument parsing and
output formatting.
"""

import typer

app = typer.Typer(
    name="audiobook",
    help="Convert plain-text books into multi-voice audiobooks.",
    add_completion=False,
)


@app.command()
def main(
    book_file: str = typer.Argument(..., help="Path to the plain-text book file."),
    discover_characters: bool = typer.Option(
        False,
        "--discover-characters",
        help="Detect characters and voices only — do not generate audio.",
    ),
) -> None:
    """Generate an audiobook from a plain-text book file."""
    raise NotImplementedError("Audiobook generation not yet implemented.")
