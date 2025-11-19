import typer
from radiant_cli.commands import hello, config, init, dataset

app = typer.Typer()


app.command()(hello.hello)
app.command()(init.init)

app.add_typer(config.app, name="config")
app.add_typer(dataset.app, name="dataset")

def main():
    app()

if __name__ == "__main__":
    main()
