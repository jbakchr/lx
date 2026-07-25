import typer

from lx.tools.grep.learn import learn as learn_grep


def learn(tool: str) -> None:
    """
    Learn a command-line tool.
    """

    if tool == "grep":
        learn_grep()
        return

    raise typer.BadParameter(
        f"Unknown tool: {tool}"
    )