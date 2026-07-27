from lx.ui.console import (
    page_header,
    section_header,
    separator,
    console,
)


def display_intro():
    separator()
    page_header("FIND", "LOCATE FILES AND DIRECTORIES.")


def learn_section():
    separator()

    section_header("Why Learn find?")

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


def use_cases_section():
    separator()

    section_header("Common Use Cases")

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


def examples_section():
    separator()

    section_header("Examples")

    console.print('  [bold cyan]find . -name "*.py"[/bold cyan]')

    console.print("    [italic]→ Find all Python files.[/italic]")

    console.print()


def try_it_section():
    separator()

    section_header("Try It")

    console.print("  [bold cyan]touch demo.txt[/bold cyan]")

    console.print()

    console.print("  [bold cyan]find . -name \"demo.txt\"[/bold cyan]")

    console.print()

    console.print("[italic]   → Find one specific file[italic]")

    console.print()

    console.print("  [bold cyan]find . -name \"*.py\"[/bold cyan]")

    console.print()

    console.print("[italic]    → Find all Python files[/italic]")

    console.print()


def learn() -> None:
    display_intro()

    learn_section()

    use_cases_section()

    examples_section()

    try_it_section()