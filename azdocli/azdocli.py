import click


def foo():
    return True


@click.group()
def cli():
    pass


@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    for x in range(count):
        click.echo(f'Hello {name}!')


cli.add_command(hello)


