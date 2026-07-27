from lx.ui.console import (
    page_header,
    separator,
)

from lx.content.grep import (
    examples_section,
    learn_section,
    try_it_section,
    use_cases_section,
)

def learn() -> None:
    separator()
    page_header("GREP", "SEARCH TEXT FOR PATTERNS.")

    learn_section()
    use_cases_section()
    examples_section()
    try_it_section()