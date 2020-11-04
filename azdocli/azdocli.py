import click
import configparser

from azdocli.lib.commons import load_settings
from azdocli.lib.controller_switch import execute_strategy

from pprint import pprint


def set_context(ctx, operation, filename='settings.ini'):
    """
    Always done before performing an operation (get, getall, etc) to ensure that the organization name and pat is
      initialized in the context.

    :param ctx: context object passed around
    :param str operation: operation to be performed (get, getall, etc)
    :param str filename: location of the settings.ini file
    :return: ctx or None
    """
    ctx.obj['operation'] = operation
    cfg = load_settings(filename)
    if not cfg:
        return None
    else:
        ctx.obj['org_name'] = cfg['org']['name']
        ctx.obj['org_pat'] = cfg['org']['pat']
        return ctx


@click.group()
def cli():
    pass


@click.command()
@click.option('--org_name', prompt='The name of the Azure DevOps organization',
              help='The name of the Azure Devops organization')
@click.option('--pat', prompt='Your personal access token for that organization',
              help='Your personal access token for that organization')
def init(org_name, pat):
    """
    Initialize the settings.ini file
    """
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
    if set_context(ctx, 'getall'):
        result = execute_strategy(ctx)
        pprint(result)
    else:
        click.echo("The settings.ini file is not found or is not initialized properly. Please use 'azdocli init' or "
                   "refer to the documentation.")


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

