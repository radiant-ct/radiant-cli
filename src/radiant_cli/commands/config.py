import typer

app = typer.Typer(help="Say hello commands")

@app.command()
def remote(name: str):
    """Say hello to someone."""
    print(f"Remote was set to {name}")
