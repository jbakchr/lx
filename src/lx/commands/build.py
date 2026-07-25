import typer

from lx.tools import grep


def build(tool: str) -> None:
    """
    Build a command interactively.
    """

    if tool == "grep":
        grep.build()
        return

    raise typer.BadParameter(
        f"Unknown tool: {tool}"
    )