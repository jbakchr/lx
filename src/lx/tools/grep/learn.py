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

    section_header("[bold]Why Learn?[/bold]")

    print("  [cyan]grep[/cyan] is one of the most common tools developers use to search for text.")
    print()

    print("""  When working in unfamiliar codebases, [cyan]grep[/cyan] can help you quickly find TODO comments,
  error messages, configuration values, and references to specific functions or files.""")
    print()

    print("  Instead of manually browsing through files, [cyan]grep[/cyan] lets you search for exactly what you are looking for.")
    print()    

    print("  Learning [cyan]grep[/cyan] helps you investigate projects faster and navigate large codebases with confidence.")
    print()


def use_cases_section() -> None:
    separator()

    section_header("[bold]Common Use Cases[/bold]")

    print("  • Find TODO comments")
    print()

    print("  • Search for error messages")
    print()

    print("  • Search log files")
    print()

    print("  • Locate code references")
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