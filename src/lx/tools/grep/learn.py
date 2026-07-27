from rich import print

from lx.ui.console import (
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

    print("✓ Search source code")
    print("✓ Find TODO comments")
    print("✓ Investigate log files")
    print("✓ Locate configuration values")
    print("✓ Find references in projects")

    print()


def use_cases_section() -> None:
    separator()

    section_header("[bold]Common Use Cases[/bold]")

    print("• Find TODO comments")
    print("• Search for error messages")
    print("• Search log files")
    print("• Locate code references")

    print()


def examples_section() -> None:
    separator()

    section_header("[bold]Examples[/bold]")

    example("grep \"TODO\" *.py", "Search all Python files for TODO comments.")

    example("grep -r \"error\" logs/", "Recursively search the logs directory.")

    example("grep -i \"warning\" app.log", "Search case-insensitively.")


def try_it_section() -> None:
    separator()

    section_header("[bold]Try It[/bold]")

    print(
        '[cyan]  echo "TODO: Fix bug" > demo.txt[/cyan]'
    )
    print()

    print(
        '[cyan]  grep "TODO" demo.txt[/cyan]'
    )
    print()

    print(
        "[italic]  → You should see the matching line printed to the terminal.[/italic]"
    )
    print()


def learn() -> None:

    display_intro()

    learn_section()

    use_cases_section()

    examples_section()

    try_it_section()