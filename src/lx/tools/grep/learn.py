from lx.content.grep import (
    examples_section,
    learn_section,
    try_it_section,
    use_cases_section,
)

from lx.ui.console import (
    section_header,
    separator,
)

def learn() -> None:
    separator()

    section_header("[bold]GREP[/bold] - [italic]SEARCH TEXT FOR PATTERNS.[/italic]")

    learn_section()
    use_cases_section()
    examples_section()
    try_it_section()