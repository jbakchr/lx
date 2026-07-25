from rich.console import Console
from rich.rule import Rule

console = Console()


def separator() -> None:
    console.print(Rule())


def header(
    text: str,
    separator_before_after: bool = False,
) -> None:
    if separator_before_after:
        separator()

    console.print()
    console.print(text)
    console.print()

    if separator_before_after:
        separator()