from lx.ui.console import (
    header,
    separator,
    console,
)


def learn() -> None:
    separator()

    header(
        "[bold]FIND[/bold] - "
        "[italic]LOCATE FILES AND DIRECTORIES.[/italic]"
    )

    separator()

    header("[bold]Why Learn find?[/bold]")

    console.print(
        "✓ Find files by name"
    )

    console.print(
        "✓ Locate configuration files"
    )

    console.print(
        "✓ Search project directories"
    )

    console.print(
        "✓ Find specific file types"
    )

    console.print()

    console.print(
        "[bold]Common Use Cases[/bold]"
    )

    console.print()

    console.print(
        "• Find Python files"
    )

    console.print(
        "• Locate config files"
    )

    console.print(
        "• Search large projects"
    )

    console.print()

    separator()

    header("[bold]Examples[/bold]")

    console.print(
        '[bold cyan]find . -name "*.py"[/bold cyan]'
    )

    console.print()

    console.print(
        "[italic]→ Find all Python files.[/italic]"
    )

    console.print()
    separator()

    header("[bold]Try It[/bold]")

    console.print("[bold cyan]touch demo.txt[/bold cyan]")

    console.print()

    console.print("[bold cyan]find . -name \"demo.txt\"[/bold cyan]")

    console.print()

    console.print("→ Find one specific file")

    console.print()

    console.print("[bold cyan]find . -name \"*.py\"[/bold cyan]")

    console.print()

    console.print("→ Find all Python files")

    console.print()