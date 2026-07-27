from rich import print

from lx.ui.console import (
    page_header,
    section_header,
    separator,
)


def display_intro():
    separator()
    page_header("JQ", "EXPLORE AND EXTRACT JSON DATA.")


def learn_section():
    separator()

    section_header("Why Learn?")

    print("""  [cyan]jq[/cyan] helps you work with JSON data from the terminal.

  Instead of reading large JSON responses by eye, [cyan]jq[/cyan] can help you find exactly the information you care about.
""")    


def use_cases_section():
    separator()

    section_header("[bold]Common Use Cases[/bold]")

    print("""  • Show a single value from JSON

  • Explore API responses

  • Inspect configuration files

  • Filter large JSON documents
""")


def examples_section():
    separator()

    section_header("[bold]Examples[/bold]")

    print("""  [bold cyan]jq .title[/bold cyan]
    [italic]→ extract the title field[/italic]

  [bold cyan]jq .completed[/bold cyan]
    [italic]→ extract the completed field[/italic]

  [bold cyan]jq .[/bold cyan]
    [italic]→ display formatted JSON[/italic]
""")


def try_it_section():
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


def learn() -> None:
    display_intro()
    
    learn_section()

    use_cases_section()

    examples_section()

    try_it_section()