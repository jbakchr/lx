from rich.console import Console
from rich.rule import Rule

console = Console()

def print_separator():
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
    console.print()


def print_examples() -> None:
    print_header("[bold]Examples[/bold]")

    console.print("[bold cyan]grep \"TODO\" *.py[/bold cyan]")
    console.print()
    console.print("[italic]→ Search all Python files for TODO comments.[/italic]")
    console.print()

    console.print("[bold cyan]grep -r \"error\" logs/[/bold cyan]")
    console.print()
    console.print("[italic]→ Recursively search the logs directory.[/italic]")
    console.print()

    console.print("[bold cyan]grep -i \"warning\" app.log[/bold cyan]")
    console.print()
    console.print("[italic]→ Search case-insensitively.[/italic]")
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

def learn() -> None:
    print()

    print_header("[bold]GREP[/bold] - [italic]SEARCH TEXT FOR PATTERNS.[/italic]", True)

    print_learn_section()

    print_use_cases()    

    print_separator()
    print_examples()

    print_separator()
    print_try_it()

