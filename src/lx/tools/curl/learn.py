from rich import print

from lx.ui.console import (
    section_header,
    separator,
)

def display_intro():
    separator()
    section_header("[bold]CURL[/bold] [italic]- RETRIEVE DATA FROM THE INTERNET.[/italic]")


def learn_section():
    separator()

    section_header("[bold]Why Learn?[/bold]")
    
    print("""  [cyan]curl[/cyan] is one of the most common command-line tools for working with websites, APIs, and online services.
    
  Learning [cyan]curl[/cyan] helps you retrieve data directly from your terminal.
    
  Many developer tools communicate with web services behind the scenes.
    
  [cyan]curl[/cyan] lets you see and test those requests yourself.
""")


def use_cases_section():
    separator()

    section_header("[bold]Common Use Cases[/bold]")

    print("""  • Check what data an API returns

  • Test a URL without opening a browser

  • Download files

  • Troubleshoot web services
""")


def examples_section():
    separator()

    section_header("[bold]Examples[/bold]")

    print("""  curl https://jsonplaceholder.typicode.com/todos/1
    [italic]→ retrieve JSON data[/italic]

  curl https://api.github.com
    [italic]→ explore an API[/italic]

  curl https://example.com
    [italic]→ retrieve a web page[/italic]
""")


def try_it_section():
    separator()

    section_header("[bold]Try It[/bold]")

    print("""  Run:

    → curl https://jsonplaceholder.typicode.com/todos/1

  What do you notice?

    → The response is JSON data.

  [italic]Later, [cyan]jq[/cyan] can help explore that data.[/italic]
""")    


def learn() -> None:
    display_intro()

    learn_section()

    use_cases_section()

    examples_section()

    try_it_section()