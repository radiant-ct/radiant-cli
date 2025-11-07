import typer
from radiant_cli.commands import hello, config

app = typer.Typer()


app.command()(hello.hello)
# Register subcommands
app.add_typer(config.app, name="config")

def main():
    app()

if __name__ == "__main__":
    main()
