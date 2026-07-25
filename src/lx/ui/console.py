from rich.console import Console
from rich.rule import Rule

console = Console()


def separator() -> None:
    console.print(Rule())


def header(
    text: str,
) -> None:
    console.print()
    console.print(text)
    console.print()
