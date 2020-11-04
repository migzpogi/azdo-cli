import unittest
from azdocli.azdocli import set_context


class DummyContext():

    def __init__(self):
        self.obj = {}


class TestAzdoCli(unittest.TestCase):

    def test_if_set_context_was_called_then_it_should_update_its_values(self):
        context = DummyContext()
        set_context(context, 'dummy_operation', filename='./tests/lib/settings.ini')

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
        actual = set_context(context, 'dummy_operation', filename='./tests/lib/dummy/settings.ini')

        self.assertEqual(expected, actual)





if __name__ == '__main__':
    unittest.main()