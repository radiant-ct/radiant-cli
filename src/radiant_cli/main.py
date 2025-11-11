import typer
from radiant_cli.commands import hello, config, init

app = typer.Typer()


app.command()(hello.hello)
app.command()(init.init)

app.add_typer(config.app, name="config")

def main():
    app()

if __name__ == "__main__":
    main()
