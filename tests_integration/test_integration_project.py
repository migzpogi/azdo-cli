import unittest
import json

from click.testing import CliRunner
from azdocli.azdocli import cli

from azure.devops.exceptions import AzureDevOpsServiceError, AzureDevOpsAuthenticationError


class TestIntegrationProject(unittest.TestCase):
    def test_if_getall_projects_then_count_must_be_two(self):
        """001"""
        runner = CliRunner()
        result = runner.invoke(cli, ['projects', 'getall'])

        actual = json.loads(result.output.replace("'", '"'))

        self.assertEqual(2, actual['count'])
        self.assertEqual(result.exit_code, 0)

    def test_if_get_project_then_id_must_be_correct(self):
        """002"""
        runner = CliRunner()
        result = runner.invoke(cli, ['projects',
                                     'get',
                                     '--name',
                                     'leonhard'])

        actual = json.loads(result.output.replace("'", '"'))

        self.assertEqual('leonhard', actual['name'])
        self.assertEqual(result.exit_code, 0)

    def test_if_getall_projects_with_wrong_pat_then_exit_2(self):
        """003"""
        filename = './tests_integration/settings-wrong-creds.ini'
        runner = CliRunner()
        result = runner.invoke(cli, ['projects', 'getall', '--filename', filename])
        self.assertEqual(result.exit_code, 2)

    def test_if_getall_projects_with_invalid_pat_then_exit_1(self):
        """003"""
        filename = './tests_integration/settings-invalid-creds.ini'
        runner = CliRunner()
        result = runner.invoke(cli, ['projects', 'getall', '--filename', filename])
        self.assertEqual(result.exit_code, 1)




if __name__ == '__main__':
    unittest.main()