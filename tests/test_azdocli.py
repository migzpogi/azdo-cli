import unittest
import os.path

from click.testing import CliRunner

from azdocli.azdocli import set_context, cli


class DummyContext():

    def __init__(self):
        self.obj = {}


class TestAzdoCli(unittest.TestCase):

    def test_if_set_context_was_called_then_it_should_update_its_values(self):
        context = DummyContext()
        set_context(context, 'dummy_operation', filename='./tests/lib/test-settings.ini')

        expected_org_name = 'dummy_org_name'
        expected_org_pat = 'dummy_pat'
        expected_operation = 'dummy_operation'

        actual_org_name = context.obj['org_name']
        actual_org_pat = context.obj['org_pat']
        actual_operation = context.obj['operation']

        self.assertEqual(expected_org_name, actual_org_name)
        self.assertEqual(expected_org_pat, actual_org_pat)
        self.assertEqual(expected_operation, actual_operation)

    def test_if_set_context_was_called_and_no_settings_ini_file_was_found_then_it_should_return_none(self):
        context = DummyContext()
        expected = None
        actual = set_context(context, 'dummy_operation', filename='./tests/lib/dummy/test-settings.ini')

        self.assertEqual(expected, actual)

    def test_if_cli_was_called_then_it_should_exit_code_0(self):
        runner = CliRunner()
        result = runner.invoke(cli)
        self.assertEqual(result.exit_code, 0)

    def test_if_init_was_called_then_it_should_create_a_settings_ini_file(self):
        filename = './tests/lib/dummy/init_test_settings.ini'
        runner = CliRunner()
        result = runner.invoke(cli, ['init',
                                     '--orgname', 'org_name_init_test',
                                     '--pat', 'pat_init_test',
                                     '--filename', filename])

        self.assertEqual(result.exit_code, 0)
        self.assertTrue(os.path.isfile(filename))

    def test_if_projects_was_called_then_it_should_exit_code_0(self):
        runner = CliRunner()
        result = runner.invoke(cli, ['projects'])
        self.assertEqual(result.exit_code, 0)

    def test_if_svc_was_called_then_it_should_exit_code_0(self):
        runner = CliRunner()
        result = runner.invoke(cli, ['svc'])
        self.assertEqual(result.exit_code, 0)


if __name__ == '__main__':
    unittest.main()