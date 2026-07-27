import subprocess
from dataclasses import dataclass

import typer

from lx.ui.console import (
    console,
    section_header,
    separator,
)


@dataclass
class FindCommand:
    target_directory: str
    file_pattern: str


def display_intro():
    separator()

    section_header("[bold]Build a real find command step by step.[/bold]")


def show_generated_command(command: str) -> None:
    separator()

    section_header("[bold]Generated find command[/bold]")

    console.print(
        f"[bold green]👉  {command}[/bold green]"
    )

    console.print()


def show_how_to_read_command(
    find_command: FindCommand,
) -> None:
    separator()

    section_header("[bold]How To Read This Command[/bold]")

    console.print("find")
    console.print(
        "→ the tool we are using"
    )

    console.print()

    console.print(
        find_command.target_directory
    )
    console.print(
        "→ start searching from this location"
    )

    console.print()

    console.print("-name")
    console.print(
        "→ search by file name"
    )

    console.print()

    console.print(
        f'"{find_command.file_pattern}"'
    )
    console.print(
        "→ file name pattern"
    )

    console.print()

    separator()

    console.print()


def run_command(command_parts: list[str]) -> None:

    console.print()
    separator()
    console.print()

    console.print(
        "[bold]Executing generated command:[/bold]"
    )
    console.print()

    subprocess.run(
        command_parts,
        check=False,
    )


def collect_build_inputs() -> FindCommand:
    separator()
    console.print()

    file_pattern = typer.prompt(
        "What file are you looking for?"
    )

    console.print()

    target_directory = typer.prompt(
        "Which directory should be searched?",
        default=".",
    )

    console.print()

    return FindCommand(
        target_directory=target_directory,
        file_pattern=file_pattern,
    )


def create_command_parts(
    find_command: FindCommand,
) -> list[str]:
    return [
        "find",
        find_command.target_directory,
        "-name",
        find_command.file_pattern]


def create_display_command(
    find_command: FindCommand,
) -> str:
    return (
        f'find {find_command.target_directory} '
        f'-name "{find_command.file_pattern}"'
    )


def build() -> None:
    display_intro()

    find_command = collect_build_inputs()

    command_parts = create_command_parts(find_command)

    command_string = create_display_command(find_command)

    show_generated_command(command_string)

    show_how_to_read_command(find_command)

    should_run = typer.confirm(
        "Run generated command?",
        default=True,
    )

    if should_run:
        run_command(command_parts)