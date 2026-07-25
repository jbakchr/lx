import typer

from lx.commands.learn import learn
from lx.commands.build import build

app = typer.Typer(
    help="Learn command-line tools by using real commands."
)

app.command()(learn)
app.command()(build)


if __name__ == "__main__":
    app()
