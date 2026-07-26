import subprocess

from rich import print
from rich.prompt import Confirm
from rich.prompt import Prompt

from lx.ui.console import (
    console,
    header,
    separator,
)


def build() -> None:
    separator()
    header("[bold]Build a real curl command step by step.[/bold]")
    separator()

    console.print()
    url = Prompt.ask(
        "Which URL do you want to request?",
        default="https://jsonplaceholder.typicode.com/todos/1",
    )

    console.print()
    separator()

    command = f'curl "{url}"'

    print()
    print("[bold cyan]Generated curl command[/bold cyan]")
    print()
    print(f"👉 {command}")

    print()
    print("[bold]How To Read This Command[/bold]")
    print()

    print("curl")
    print("→ make an HTTP request")
    print()

    print(url)
    print("→ the address we want to contact")

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

        console.print(f"[bold]What came back?[/bold]")

        print()

        subprocess.run(command, shell=True)

        print()
        print()

        separator()
        print()

        console.print("[bold]What happened?[/bold]")
        print()

        print("curl contacted:")
        print()

        print(url)
        print()

        print("The server responded with data.")
        print()
