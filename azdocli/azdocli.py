import click
import configparser
from pprint import pprint

from azdocli.lib.commons import foo_commons, load_settings, controller_switch
from azdocli.lib.core import CoreAPI


def foo():
    return True


@click.group()
def cli():
    pass


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
@click.pass_context
def projects(ctx):
    """
    Commands for managing projects
    """
    ctx.ensure_object(dict)
    ctx.obj['controller'] = 'projects'
    pass


@click.group()
@click.pass_context
def svc(ctx):
    """
    Commands for managing service endpoints
    """
    ctx.ensure_object(dict)
    ctx.obj['controller'] = 'svc'


@click.command()
@click.pass_context
def getall(ctx):
    """
    Performs a list operation
    """
    print(ctx.obj['controller'])
    cfg = load_settings()
    if not cfg:
        click.echo("Init first")

    client = controller_switch(ctx.obj['controller'], cfg)

    if cfg:
        coreapi = CoreAPI(cfg['org']['name'], cfg['org']['pat'])
        click.echo(pprint(coreapi.list_projects()))
    else:
        click.echo("Init this")


cli.add_command(init)
cli.add_command(projects)
cli.add_command(svc)

projects.add_command(getall)
svc.add_command(getall)


