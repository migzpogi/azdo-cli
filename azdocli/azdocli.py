import click
import configparser

from azdocli.lib.commons import load_settings
from azdocli.lib.controller_switch import execute_strategy


def foo():
    return True


def set_context(ctx, operation):
    ctx.obj['operation'] = operation
    cfg = load_settings()
    if not cfg:
        print("Init first")
    else:
        ctx.obj['org_name'] = cfg['org']['name']
        ctx.obj['org_pat'] = cfg['org']['pat']


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
    set_context(ctx, 'getall')
    execute_strategy(ctx)


@click.command()
@click.pass_context
def get(ctx):
    """
    Performs a get operation
    """
    set_context(ctx, 'get')
    execute_strategy(ctx)


cli.add_command(init)
cli.add_command(projects)
cli.add_command(svc)

projects.add_command(getall)
projects.add_command(get)

svc.add_command(getall)
svc.add_command(get)

