import subprocess

import typer
from rich.console import Console
from rich.rule import Rule

console = Console()


def print_separator() -> None:
    console.print(Rule())


def print_header(text: str, sep: bool = False) -> None:
    if sep:
        print_separator()

    console.print()
    console.print(text)
    console.print()

    if sep:
        print_separator()


def print_learn_section() -> None:
    print_header("[bold]Why Learn grep?[/bold]")

    console.print("✓ Search source code")
    console.print("✓ Find TODO comments")
    console.print("✓ Investigate log files")
    console.print("✓ Locate configuration values")
    console.print("✓ Find references in projects")


def print_use_cases() -> None:
    print_header("[bold]Common Use Cases[/bold]")

    console.print("• Find TODO comments")
    console.print("• Search for error messages")
    console.print("• Search log files")
    console.print("• Locate code references")


def print_examples() -> None:
    print_header("[bold]Examples[/bold]")

    console.print('[bold cyan]grep "TODO" *.py[/bold cyan]')
    console.print()
    console.print(
        "[italic]→ Search all Python files for TODO comments.[/italic]"
    )
    console.print()

    console.print('[bold cyan]grep -r "error" logs/[/bold cyan]')
    console.print()
    console.print(
        "[italic]→ Recursively search the logs directory.[/italic]"
    )
    console.print()

    console.print('[bold cyan]grep -i "warning" app.log[/bold cyan]')
    console.print()
    console.print(
        "[italic]→ Search case-insensitively.[/italic]"
    )
    console.print()


def print_try_it() -> None:
    print_header("[bold]Try It[/bold]")

    console.print(
        '[bold cyan]echo "TODO: Fix bug" > demo.txt[/bold cyan]'
    )
    console.print()

    console.print(
        '[bold cyan]grep "TODO" demo.txt[/bold cyan]'
    )
    console.print()

    console.print(
        "You should see the matching line printed to the terminal."
    )
    console.print()


def print_generated_command(command: str) -> None:
    print_separator()

    print_header("[bold]Generated grep command[/bold]")

    console.print(
        f"[bold green]👉  {command}[/bold green]"
    )

    console.print()


def explain_command(
    search_text: str,
    files_pattern: str,
    recursive: bool,
) -> None:
    print_separator()

    print_header("[bold]Explanation[/bold]")

    console.print("grep        → search text")

    if recursive:
        console.print("-r          → search recursively")

    console.print(
        f'"{search_text}"    → text to search for'
    )

    console.print(
        f"{files_pattern}      → files to search"
    )

    console.print()


def run_command(command_parts: list[str]) -> None:
    print_separator()

    console.print("[bold]Executing command...[/bold]")
    console.print()

    subprocess.run(
        command_parts,
        check=False,
    )


def learn() -> None:
    print_header(
        "[bold]GREP[/bold] - [italic]SEARCH TEXT FOR PATTERNS.[/italic]",
        True,
    )

    print_learn_section()

    print_use_cases()

    print_separator()
    print_examples()

    print_separator()
    print_try_it()


def build() -> None:
    print_header(
        "[bold]Build a real grep command step by step.[/bold]",
        True,
    )

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

    #
    # Command used for execution
    #
    command_parts = ["grep"]

    if recursive:
        command_parts.append("-r")

    command_parts.append(search_text)
    command_parts.append(target)

    #
    # Command shown to user
    #
    display_command = ["grep"]

    if recursive:
        display_command.append("-r")

    display_command.append(f'"{search_text}"')
    display_command.append(target)

    command_string = " ".join(display_command)

    print_generated_command(command_string)

    explain_command(
        search_text=search_text,
        files_pattern=target,
        recursive=recursive,
    )

    should_run = typer.confirm(
        "Run generated command?",
        default=True,
    )

    if should_run:
        run_command(command_parts)