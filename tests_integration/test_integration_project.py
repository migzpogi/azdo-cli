import unittest
import json

from click.testing import CliRunner
from azdocli.azdocli import cli


class TestIntegrationProject(unittest.TestCase):
    def test_if_getall_projects_then_count_must_be_two(self):
        runner = CliRunner()
        result = runner.invoke(cli, ['projects', 'getall'])

        actual = json.loads(result.output.replace("'", '"'))

        self.assertEqual(2, actual['count'])
        self.assertEqual(result.exit_code, 0)

    def test_if_get_project_then_id_must_be_correct(self):
        runner = CliRunner()
        result = runner.invoke(cli, ['projects',
                                     'get',
                                     '--name',
                                     'leonhard'])

        actual = json.loads(result.output.replace("'", '"'))

        self.assertEqual('leonhard', actual['name'])
        self.assertEqual(result.exit_code, 0)


if __name__ == '__main__':
    unittest.main()