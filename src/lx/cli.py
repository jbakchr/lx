import typer

from grep import learn

app = typer.Typer(
    help="Learn command-line tools by using real commands."
)

learn_app = typer.Typer(
    help="Learn a command."
)

app.add_typer(
    learn_app,
    name="learn",
)


@learn_app.command("grep")
def learn_grep() -> None:
    """Learn grep."""
    learn()


if __name__ == "__main__":
    app()