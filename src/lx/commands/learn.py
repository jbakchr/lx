import typer

from lx.tools.grep.learn import learn as learn_grep
from lx.tools.find.learn import learn as learn_find
from lx.tools.curl.learn import learn as learn_curl
from lx.tools.jq.learn import learn as learn_jq


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

    if tool == "curl":
        learn_curl()
        return

    if tool == "jq":
        learn_jq()
        return

    raise typer.BadParameter(
        f"Unknown tool: {tool}"
    )