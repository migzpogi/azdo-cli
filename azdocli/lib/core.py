from azdocli.lib.commons import create_azdo_connection
from azure.devops.exceptions import AzureDevOpsServiceError, AzureDevOpsAuthenticationError
from azdocli.lib.exceptions import exception_handler


class CoreAPI:
    @exception_handler
    def __init__(self, org_name, org_pat):
        self.connection = create_azdo_connection(org_name, org_pat)
        self.core_client = self.connection.clients_v6_0.get_core_client()

    @exception_handler
    def list_projects(self):
        """

        :return:
        """
        list_of_projects = {
            'count': 0,
            'values': []
        }

        for p in self.core_client.get_projects():
            list_of_projects['count'] += 1
            list_of_projects['values'].append(
                {
                    'id': p.id,
                    'name': p.name
                }
            )

        return list_of_projects

    @exception_handler
    def get_project(self, project_name):
        """

        :param project_name:
        :return:
        """

        project = self.core_client.get_project(project_name)
        project_result = {
            "id": project.id,
            "name": project.name,
            "description": project.description if project.description else ""
        }

        return project_result

    @exception_handler
    def list_teams(self):
        """

        :return:
        """

        list_of_all_teams = []

        all_teams = self.core_client.get_all_teams()
        for team in all_teams:
            list_of_all_teams.append(
                {
                    "project_name": team.project_name,
                    "team_name": team.name
                }
            )

        return list_of_all_teams
