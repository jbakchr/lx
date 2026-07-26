import typer

from lx.tools.grep.build import build as build_grep
from lx.tools.find.build import build as build_find
from lx.tools.curl.build import build as build_curl


def build(tool: str) -> None:
    """
    Build a command interactively.
    """

    if tool == "grep":
        build_grep()
        return

    if tool == "find":
        build_find()
        return

    if tool == "curl":
        build_curl()
        return

    raise typer.BadParameter(
        f"Unknown tool: {tool}"
    )