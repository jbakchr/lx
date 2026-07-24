import typer

import grep

app = typer.Typer(
    help="Learn command-line tools by using real commands."
)

learn_app = typer.Typer()
build_app = typer.Typer()

app.add_typer(learn_app, name="learn")
app.add_typer(build_app, name="build")


@learn_app.command("grep")
def learn_grep() -> None:
    grep.learn()


@build_app.command("grep")
def build_grep() -> None:
    grep.build()


if __name__ == "__main__":
    app()