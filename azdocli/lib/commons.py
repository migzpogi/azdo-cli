import configparser

from azure.devops.connection import Connection

from msrest.authentication import BasicAuthentication


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


def load_settings(filename='settings.ini'):
    """
    Loads the settings.ini file which contains the organization name and personal access token

    :param str filename: location of the file
    :return: config object or None
    """

    config = configparser.ConfigParser()
    config.read(filename)

    if not config.sections():
        return None
    else:
        try:
            if config['org']['name'] is not None and config['org']['pat'] is not None:
                return config
        except KeyError:
            return None
