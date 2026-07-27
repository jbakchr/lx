import subprocess
from dataclasses import dataclass

import typer

from lx.ui.console import (
    console,
    section_header,
    separator,
)


@dataclass
class GrepCommand:
    search_text: str
    target: str
    recursive: bool


def display_intro():
    separator()
    section_header("[bold]Build a real grep command step by step.[/bold]")
    separator()


def show_generated_command(command: str) -> None:
    separator()

    section_header("[bold]Generated grep command[/bold]")

    console.print(
        f"[bold green]👉  {command}[/bold green]"
    )

    console.print()


def show_how_to_read_command(grep_command: GrepCommand) -> None:
    separator()

    section_header("[bold]How To Read This Command[/bold]")

    console.print("  grep")
    console.print("    [italic]→ the tool we are using[/italic]")

    console.print()

    if grep_command.recursive:
        console.print("  -r")
        console.print("    [italic]→ search all files underneath this directory[/italic]")

        console.print()

    console.print(f'  "{grep_command.search_text}"')
    console.print("    → the text we want to find")

    console.print()

    console.print(f"  {grep_command.target}")
    console.print("    → start searching from this location")

    console.print()
    separator()
    console.print()


def run_command(command_parts: list[str]) -> None:
    console.print()

    separator()

    console.print()

    console.print(f"[bold]Executing generated command:[/bold]")
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
        default=True,
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

    display_intro()

    grep_command = collect_build_inputs()

    command_parts = create_command_parts(grep_command)

    command_string = create_display_command(grep_command)

    show_generated_command(command_string)

    show_how_to_read_command(grep_command)

    should_run = typer.confirm(
        "Run generated command?",
        default=True,
    )

    if should_run:
        run_command(command_parts)