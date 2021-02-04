from azdocli.lib.commons import create_azdo_connection
from azdocli.lib.exceptions import exception_handler


class PipelinesAPI:
    @exception_handler
    def __init__(self, org_name, org_pat):
        self.connection = create_azdo_connection(org_name, org_pat)
        self.core_client = self.connection.clients_v6_0.get_pipelines_client()

    @exception_handler
    def get_pipelineruns(self, project_id, pipeline_id):
        return (project_id, pipeline_id)