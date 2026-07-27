from rich import print

from lx.ui.console import (
    section_header,
    separator,
)


def learn() -> None:
    separator()
    section_header(
        "[bold]JQ[/bold] [italic]- EXPLORE AND EXTRACT JSON DATA.[/italic]"
    )
    separator()

    section_header("[bold]Why Learn?[/bold]")

    print("""  [cyan]jq[/cyan] helps you work with JSON data from the terminal.

  Instead of reading large JSON responses by eye, [cyan]jq[/cyan] can help you find exactly the information you care about.
""")

    separator()

    section_header("[bold]Common Use Cases[/bold]")

    print("""  • Show a single value from JSON

  • Explore API responses

  • Inspect configuration files

  • Filter large JSON documents
""")

    separator()

    section_header("[bold]Examples[/bold]")

    print("""  [bold cyan]jq .title[/bold cyan]
    → extract the title field

  [bold cyan]jq .completed[/bold cyan]
    → extract the completed field

  [bold cyan]jq .[/bold cyan]
    → display formatted JSON
""")

    separator()

    section_header("[bold]Try It[/bold]")

    print("""  First retrieve some JSON:

    → curl https://jsonplaceholder.typicode.com/todos/1

  Notice the response contains:

    → title
    → completed
    → userId

  Now imagine you only want:

    → title

  [italic][cyan]jq[/cyan] can help extract exactly that field.[/italic]
""")