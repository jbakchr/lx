import typer

from lx.tools import grep


def learn(tool: str) -> None:
    """
    Learn a command-line tool.
    """

    if tool == "grep":
        grep.learn()
        return

    raise typer.BadParameter(
        f"Unknown tool: {tool}"
    )