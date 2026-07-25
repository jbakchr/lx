import subprocess
from dataclasses import dataclass

import typer

from lx.ui.console import (
    console,
    header,
    separator,
)


@dataclass
class GrepCommand:
    search_text: str
    target: str
    recursive: bool



def show_generated_command(command: str) -> None:
    separator()

    header("[bold]Generated grep command[/bold]")

    console.print(
        f"[bold green]👉  {command}[/bold green]"
    )

    console.print()


def show_command_explanation(grep_command: GrepCommand) -> None:
    separator()

    header("[bold]Explanation[/bold]")

    console.print("grep        → search text")

    if grep_command.recursive:
        console.print("-r          → search recursively")

    console.print(
        f'"{grep_command.search_text}"    → text to search for'
    )

    console.print(
        f"{grep_command.target}      → files to search"
    )

    console.print()


def run_command(command_parts: list[str]) -> None:
    separator()

    console.print()

    console.print(f"[bold]Executing generated command:[/bold] [italic green]{" ".join(command_parts)}[/italic green]")
    console.print()

    console.print("[bold]Output from running grep command:[/bold]")
    console.print()
    subprocess.run(
        command_parts,
        check=False,
    )


def collect_build_inputs() -> GrepCommand:
    console.print()
    
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

    console.print()

    return GrepCommand(
        search_text=search_text,
        target=target,
        recursive=recursive,
    )


def create_command_parts(grep_command: GrepCommand) -> list[str]:
    command_parts = ["grep"]

    if grep_command.recursive:
        command_parts.append("-r")

    command_parts.append(grep_command.search_text)
    command_parts.append(grep_command.target)

    return command_parts


def create_display_command(grep_command: GrepCommand) -> str:
    display_command = ["grep"]

    if grep_command.recursive:
        display_command.append("-r")

    display_command.append(f'"{grep_command.search_text}"')
    display_command.append(grep_command.target)

    return " ".join(display_command)




def build() -> None:
    separator()
    header("[bold]Build a real grep command step by step.[/bold]")
    separator()

    grep_command = collect_build_inputs()

    command_parts = create_command_parts(grep_command)

    command_string = create_display_command(grep_command)

    show_generated_command(command_string)

    show_command_explanation(grep_command)

    should_run = typer.confirm(
        "Run generated command?",
        default=True,
    )

    console.print()

    if should_run:
        run_command(command_parts)