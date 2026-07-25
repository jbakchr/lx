import typer

from lx.tools.grep.build import build as build_grep


def build(tool: str) -> None:
    """
    Build a command interactively.
    """

    if tool == "grep":
        build_grep()
        return

    raise typer.BadParameter(
        f"Unknown tool: {tool}"
    )