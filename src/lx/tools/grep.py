import subprocess

import typer

from lx.content.grep import (
    examples,
    learn_section,
    try_it_section,
    use_cases_section,
)
from lx.ui.console import (
    console,
    header,
    separator,
)


def print_generated_command(command: str) -> None:
    separator()

    header("[bold]Generated grep command[/bold]")

    console.print(
        f"[bold green]👉  {command}[/bold green]"
    )

    console.print()


def explain_command(search_text: str, target: str, recursive: bool) -> None:
    separator()

    header("[bold]Explanation[/bold]")

    console.print("grep        → search text")

    if recursive:
        console.print("-r          → search recursively")

    console.print(
        f'"{search_text}"    → text to search for'
    )

    console.print(
        f"{target}      → files to search"
    )

    console.print()


def run_command(command_parts: list[str]) -> None:
    separator()

    console.print("[bold]Executing command...[/bold]")
    console.print()

    subprocess.run(
        command_parts,
        check=False,
    )


def collect_build_inputs() -> tuple[str, str, bool]:
    search_text = typer.prompt(
        "What text are you looking for?"
    )

    console.print()

    target = typer.prompt(
        "Which file or directory should be searched?",
        default=".",
    )

    console.print()

    recursive = typer.confirm(
        "Search recursively?",
        default=False,
    )

    return search_text, target, recursive


def create_command_parts(search_text: str, target: str, recursive: bool) -> list[str]:
    command_parts = ["grep"]

    if recursive:
        command_parts.append("-r")

    command_parts.append(search_text)
    command_parts.append(target)

    return command_parts


def create_display_command(
    search_text: str,
    target: str,
    recursive: bool,
) -> str:
    display_command = ["grep"]

    if recursive:
        display_command.append("-r")

    display_command.append(f'"{search_text}"')
    display_command.append(target)

    return " ".join(display_command)


def learn() -> None:
    separator()
    header("[bold]GREP[/bold] - [italic]SEARCH TEXT FOR PATTERNS.[/italic]")

    separator()
    learn_section()
    use_cases_section()

    separator()
    examples()

    separator()
    try_it_section()


def build() -> None:
    header("[bold]Build a real grep command step by step.[/bold]")

    search_text, target, recursive = collect_build_inputs()

    command_parts = create_command_parts(
        search_text,
        target,
        recursive,
    )

    command_string = create_display_command(
        search_text,
        target,
        recursive,
    )

    print_generated_command(command_string)

    explain_command(
        search_text=search_text,
        target=target,
        recursive=recursive,
    )

    should_run = typer.confirm(
        "Run generated command?",
        default=True,
    )

    if should_run:
        run_command(command_parts)