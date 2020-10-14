import click

def foo():
    return True


@click.command()
def cli():
    """Example script"""
    click.echo("Hello World!")