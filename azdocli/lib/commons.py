import configparser

from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication

from azdocli.lib.core import CoreAPI


def foo_commons():
    return "Hello commons"


def create_azdo_connection(org_name, org_pat):
    """
    Creates the connection to the Azure DevOps orgnanization that will be used by the clients

    :param str org_name: Name of the organization
    :param str org_pat:  Personal access token for the organization
    :return: azure.devops.connection.Connection
    """

    organization_url = f'https://dev.azure.com/{org_name}'
    credentials = BasicAuthentication('', org_pat)
    connection = Connection(base_url=organization_url, creds=credentials)

    return connection


def load_settings():
    """
    Loads the settings.ini file which contains the organization name and personal access token
    :return:
    """

    config = configparser.ConfigParser()
    config.read('settings.ini')

    if not config.sections():
        return None
    else:
        return config


def controller_switch(controller, cfg):
    """
    Determines what type of controller to execute
    :param controller:
    :param cfg:
    :return:
    """

    if controller == 'projects':
        return CoreAPI(cfg['org']['name'], cfg['org']['pat'])
    if controller == 'svc':
        return 2