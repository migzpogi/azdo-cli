import click
import configparser
from pprint import pprint

from azdocli.lib.commons import foo_commons, load_settings
from azdocli.lib.core import CoreAPI


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


@click.command()
def stub():
    config = configparser.ConfigParser()
    config.read('settings.ini')
    click.echo(f'Config {config["org"]["pat"]}')


@click.command()
@click.option('--org_name', prompt='The name of the Azure DevOps organization',
              help='The name of the Azure Devops organization')
@click.option('--pat', prompt='Your personal access token for that organization',
              help='Your personal access token for that organization')
def init(org_name, pat):
    config = configparser.ConfigParser()
    config['org'] = {
        'name': org_name,
        'pat': pat
    }
    with open('settings.ini', 'w') as f:
        config.write(f)


@click.group()
def projects():
    """
    Commands for managing projects within Azure DevOps
    """
    pass


@click.command()
def listprojects():
    """
    Get all projects in the organization
    """
    cfg = load_settings()
    if cfg:
        coreapi = CoreAPI(cfg['org']['name'], cfg['org']['pat'])
        click.echo(pprint(coreapi.list_projects()))
    else:
        click.echo("Init this")


cli.add_command(hello)
cli.add_command(stub)
cli.add_command(init)
cli.add_command(projects)

projects.add_command(listprojects)


