import json

from rich import print
from rich.prompt import Confirm
from rich.prompt import Prompt

from lx.ui.console import (
    console,
    header,
    separator,
)


EXAMPLE_JSON = {
    "userId": 1,
    "id": 1,
    "title": "delectus aut autem",
    "completed": False,
}


def build() -> None:
    separator()
    header("[bold]Build a real jq command step by step.[/bold]")
    separator()

    console.print()

    field = Prompt.ask(
        "Which JSON field do you want to extract?",
        default="title",
    )

    console.print()

    separator()

    command = f"jq .{field}"

    print()
    print("[bold]Generated jq command[/bold]")
    print()
    print(f"👉 [bold green]{command}[/bold green]")
    print()

    separator()

    print()
    print("[bold]How To Read This Command[/bold]")
    print()

    print("jq")
    print("→ the tool we are using")
    print()

    print(f".{field}")
    print(f"→ extract the {field} field from JSON data")

    print()

    separator()

    print()
    print("[bold]Example JSON[/bold]")
    print()

    print(
        json.dumps(
            EXAMPLE_JSON,
            indent=2,
        )
    )

    print()

    separator()

    print()

    if Confirm.ask("Run this command?"):
        print()

        separator()

        print()

        console.print(
            "[bold]Executing generated command ..[/bold]"
        )

        print()

        console.print(
            "[bold]What came back?[/bold]"
        )

        print()

        result = EXAMPLE_JSON.get(field)

        print(result)

        print()

        separator()

        print()

        console.print(
            "[bold]What happened?[/bold]"
        )

        print()

        print(
            "jq looked at the JSON data."
        )

        print()

        print(
            f"It extracted the '{field}' field."
        )

        print()

        print(
            "Only that value was returned."
        )

        print()