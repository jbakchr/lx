from lx.ui.console import console
from lx.ui.console import header

def learn_section() -> None:
    header("[bold]Why Learn grep?[/bold]")

    console.print("✓ Search source code")
    console.print("✓ Find TODO comments")
    console.print("✓ Investigate log files")
    console.print("✓ Locate configuration values")
    console.print("✓ Find references in projects")


def use_cases_section() -> None:
    header("[bold]Common Use Cases[/bold]")

    console.print("• Find TODO comments")
    console.print("• Search for error messages")
    console.print("• Search log files")
    console.print("• Locate code references")

    console.print()


def examples() -> None:
    header("[bold]Examples[/bold]")

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

def try_it_section() -> None:
    header("[bold]Try It[/bold]")

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