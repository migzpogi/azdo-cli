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


def run(ctx, operation, filename='settings.ini'):
    """
    Sets the context then executes the strategy

    :param ctx: context object passed around
    :param str operation: operation to be performed (get, getall, etc)
    :param str filename: location of the settings.ini file
    :return:
    """
    if set_context(ctx, operation, filename):
        result = execute_strategy(ctx)
        if result:
            pprint(result)
    else:
        click.echo("The settings.ini file is not found or is not initialized properly. Please use 'azdocli init' or "
                   "refer to the documentation.")


@click.group()
def cli():
    """
    azdocli is a command line interface for Azure DevOps. The user can perform GET operations for different
    resources directly in their terminal. The same can be achieved by using Postman or the web browser, but
    where is the fun in that.

    It uses a Personal Access Token (PAT) to connect to the API which the user must specify by running:

        azdocli init

    Once the settings.ini file is created, commands now can be ran such as:

        azdocli projects getall

    This will display all the projects that the user has access to in a given organization.

    For any issues or help needed: https://github.com/migzpogi
    """
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


@click.group()
@click.pass_context
def pipelineruns(ctx):
    """
    Commands for managing pipeline runs
    """
    ctx.ensure_object(dict)
    ctx.obj['controller'] = 'pipelineruns'


@click.command()
@click.pass_context
@click.option('--filename', default='settings.ini',
              help='Location and filename.')
def getall(ctx, filename):
    """
    Performs a list operation
    """
    run(ctx, 'getall', filename)


@click.command()
@click.pass_context
@click.option('--projectname', prompt='The name of the project.', help='The name of the project.')
@click.option('--pipelineid', default='', help="ID for pipeline commands.")
@click.option('--teamid', default='', help="ID for team commands.")
def get(ctx, projectname, pipelineid, teamid):
    """
    Performs a get operation
    """
    ctx.obj['project_name'] = projectname
    ctx.obj['pipeline_id'] = pipelineid
    ctx.obj['team_id'] = teamid
    run(ctx, 'get')


for command in [init, projects, svc, teams, pipelineruns]:
    cli.add_command(command)


projects.add_command(getall)
projects.add_command(get)

svc.add_command(getall)
svc.add_command(get)

teams.add_command(getall)
teams.add_command(get)

pipelineruns.add_command(get)