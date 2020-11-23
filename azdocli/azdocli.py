import configparser
from pprint import pprint

import click

from azdocli.lib.commons import load_settings
from azdocli.lib.controller_switch import execute_strategy


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


def run(ctx, operation):
    """
    Sets the context then executes the strategy

    :param ctx: context object passed around
    :param str operation: operation to be performed (get, getall, etc)
    :return:
    """
    if set_context(ctx, operation):
        result = execute_strategy(ctx)
        if result:
            pprint(result)
    else:
        click.echo("The settings.ini file is not found or is not initialized properly. Please use 'azdocli init' or "
                   "refer to the documentation.")


@click.group()
def cli():
    pass


@click.command()
@click.option('--orgname', prompt='The name of the Azure DevOps organization',
              help='The name of the Azure Devops organization')
@click.option('--pat', prompt='Your personal access token for that organization',
              help='Your personal access token for that organization')
@click.option('--filename', default='settings.ini',
              help='Location and filename.')
def init(orgname, pat, filename):
    """
    Initialize the settings.ini file
    """
    config = configparser.ConfigParser()
    config['org'] = {
        'name': orgname,
        'pat': pat
    }
    with open(filename, 'w') as f:
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


@click.group()
@click.pass_context
def teams(ctx):
    """
    Commands for managing teams
    """
    ctx.ensure_object(dict)
    ctx.obj['controller'] = 'teams'


@click.command()
@click.pass_context
def getall(ctx):
    """
    Performs a list operation
    """
    run(ctx, 'getall')


@click.command()
@click.pass_context
@click.option('--name', prompt='The name of the resource.', help='The name of the resource to get.')
def get(ctx, name):
    """
    Performs a get operation
    """
    ctx.obj['project_name'] = name
    run(ctx, 'get')


for command in [init, projects, svc, teams]:
    cli.add_command(command)


projects.add_command(getall)
projects.add_command(get)

svc.add_command(getall)
svc.add_command(get)

teams.add_command(getall)