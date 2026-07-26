import typer

from lx.tools.grep.learn import learn as learn_grep
from lx.tools.find.learn import learn as learn_find


def learn(tool: str) -> None:
    """
    Learn a command-line tool.
    """

    if tool == "grep":
        learn_grep()
        return

    if tool == "find":
        learn_find()
        return

    raise typer.BadParameter(
        f"Unknown tool: {tool}"
    )