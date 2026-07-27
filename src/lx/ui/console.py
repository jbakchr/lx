from rich.console import Console
from rich.rule import Rule

console = Console()


def separator() -> None:
    console.print(Rule())


def page_header(command_name: str, command_desc: str):
    console.print(f"[bold]{command_name.upper}[/bold] - [bold italic]{command_desc.upper()}[/bold italic]")


def section_header(
    text: str,
) -> None:
    console.print()
    console.print(text)
    console.print()
