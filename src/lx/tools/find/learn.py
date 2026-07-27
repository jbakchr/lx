from rich import print

from lx.ui.console import (
    page_header,
    section_header,
    separator,
    example
)


def display_intro():
    separator()
    page_header("FIND", "LOCATE FILES AND DIRECTORIES.")


def learn_section():
    separator()

    section_header("Why Learn find?")

    print(
        "✓ Find files by name"
    )

    print(
        "✓ Locate configuration files"
    )

    print(
        "✓ Search project directories"
    )

    print(
        "✓ Find specific file types"
    )

    print()


def use_cases_section():
    separator()

    section_header("Common Use Cases")

    print(
        "• Find Python files"
    )

    print(
        "• Locate config files"
    )

    print(
        "• Search large projects"
    )

    print()


def examples_section():
    separator()

    section_header("Examples")

    example("find . -name \"*.py\"", "Find all Python files.")

    print()


def try_it_section():
    separator()

    section_header("Try It")

    print("  [bold cyan]touch demo.txt[/bold cyan]")

    print()

    print("  [bold cyan]find . -name \"demo.txt\"[/bold cyan]")

    print()

    print("[italic]    → Find one specific file[italic]")

    print()

    print("  [bold cyan]find . -name \"*.py\"[/bold cyan]")

    print()

    print("[italic]    → Find all Python files[/italic]")

    print()


def learn() -> None:
    
    display_intro()

    learn_section()

    use_cases_section()

    examples_section()

    try_it_section()