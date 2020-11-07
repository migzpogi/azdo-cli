from azdocli.lib.commons import create_azdo_connection
from azure.devops.exceptions import AzureDevOpsServiceError


class CoreAPI:
    def __init__(self, org_name, org_pat):
        self.connection = create_azdo_connection(org_name, org_pat)
        self.core_client = self.connection.clients_v6_0.get_core_client()

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

    def get_project(self, project_name):
        """

        :param project_name:
        :return:
        """

        try:
            project = self.core_client.get_project(project_name)
            project_result = {
                "id": project.id,
                "name": project.name,
                "description": project.description
            }
        except AzureDevOpsServiceError:
            print("Project does not exist.")
            project_result = None

        return project_result