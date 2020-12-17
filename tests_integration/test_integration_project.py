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

    def test_foo(self):
        filename = './tests_integration/settings-wrong-creds.ini'
        runner = CliRunner()
        result = runner.invoke(cli, ['projects',
                                     'get',
                                     '--name',
                                     'leonhard',
                                     '--filename',
                                     filename])
        self.assertEqual(result.exit_code, 0)
        # with self.assertRaises(AzureDevOpsServiceError):
        #     result = runner.invoke(cli, ['projects',
        #                                  'get',
        #                                  '--name',
        #                                  'leonhard',
        #                                  '--filename',
        #                                  filename])
        # with self.assertRaises(AzureDevOpsServiceError):
        #     runner.invoke(cli, ['projects', 'getall'])



if __name__ == '__main__':
    unittest.main()