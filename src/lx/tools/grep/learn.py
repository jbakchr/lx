from lx.ui.console import (
    console,
    page_header,
    section_header,
    separator,
    example
)


def display_intro():
    separator()
    page_header("GREP", "SEARCH TEXT FOR PATTERNS.")


def learn_section() -> None:
    separator()

    section_header("[bold]Why Learn grep?[/bold]")

    console.print("✓ Search source code")
    console.print("✓ Find TODO comments")
    console.print("✓ Investigate log files")
    console.print("✓ Locate configuration values")
    console.print("✓ Find references in projects")

    console.print()


def use_cases_section() -> None:
    separator()

    section_header("[bold]Common Use Cases[/bold]")

    console.print("• Find TODO comments")
    console.print("• Search for error messages")
    console.print("• Search log files")
    console.print("• Locate code references")

    console.print()


def examples_section() -> None:
    separator()

    section_header("[bold]Examples[/bold]")

    example("grep \"TODO\" *.py", "Search all Python files for TODO comments.")

    example("grep -r \"error\" logs/", "Recursively search the logs directory.")

    example("grep -i \"warning\" app.log", "Search case-insensitively.")


def try_it_section() -> None:
    separator()

    section_header("[bold]Try It[/bold]")

    console.print(
        '[cyan]  echo "TODO: Fix bug" > demo.txt[/cyan]'
    )
    console.print()

    console.print(
        '[cyan]  grep "TODO" demo.txt[/cyan]'
    )
    console.print()

    console.print(
        "[italic]  → You should see the matching line printed to the terminal.[/italic]"
    )
    console.print()


def learn() -> None:

    display_intro()

    learn_section()

    use_cases_section()

    examples_section()

    try_it_section()