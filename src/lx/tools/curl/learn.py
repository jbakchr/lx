from rich import print

from lx.ui.console import (
    page_header,
    section_header,
    separator,
    example
)


def display_intro():
    separator()
    page_header("CURL", "RETRIEVE DATA FROM THE INTERNET.")


def learn_section():
    separator()

    section_header("Why Learn?")
    
    print("""  [cyan]curl[/cyan] is one of the most common command-line tools for working with websites, APIs, and online services.
    
  Learning [cyan]curl[/cyan] helps you retrieve data directly from your terminal.
    
  Many developer tools communicate with web services behind the scenes.
    
  [cyan]curl[/cyan] lets you see and test those requests yourself.
""")


def use_cases_section():
    separator()

    section_header("Common Use Cases")

    print("""  • Check what data an API returns

  • Test a URL without opening a browser

  • Download files

  • Troubleshoot web services
""")


def examples_section():
    separator()

    section_header("Examples")

    example("curl https://jsonplaceholder.typicode.com/todos/1", "retrieve JSON data")

    example("curl https://api.github.com", "explore an API")

    example("curl https://example.com", "retrieve a web page")


def try_it_section():
    separator()

    section_header("Try It")

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