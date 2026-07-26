import subprocess

from rich import print
from rich.prompt import Confirm
from rich.prompt import Prompt

from lx.ui.console import (
    console,
    header,
    separator,
)


def display_intro():
    separator()
    header("[bold]Build a real curl command step by step.[/bold]")
    separator()


def ask_for_url() -> str:
    console.print()

    url = Prompt.ask(
        "Which URL do you want to request?",
        default="https://jsonplaceholder.typicode.com/todos/1",
    )

    console.print()
    separator()

    return url


def build_command(url: str) -> str:
    return f'curl "{url}"'


def explain_command(command: str, url: str) -> None:

    print()
    print("[bold cyan]Generated curl command[/bold cyan]")
    print()
    print(f"👉 {command}")

    print()
    print("[bold]How To Read This Command[/bold]")
    print()

    print("  curl")
    console.print("    [italic]→ make an HTTP request[/italic]")
    print()

    print(f"  {url}")
    console.print("    [italic]→ the address we want to contact[/italic]")

    print()

    separator()

    print()


def run_command(command: str, url: str) -> None:
    print()
    separator()
    print()

    console.print(
        "[bold]Executing generated command ..[/bold]"
    )

    print()
    console.print("[bold]What came back?[/bold]")
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


def build() -> None:

    display_intro()

    url = ask_for_url()

    command = build_command(url)

    explain_command(command, url)

    if Confirm.ask("Run this command?"):
        run_command(command, url)
