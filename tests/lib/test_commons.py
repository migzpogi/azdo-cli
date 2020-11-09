import unittest

from azdocli.lib import commons


class TestCommons(unittest.TestCase):

    def test_if_settings_file_does_not_exist_then_it_must_return_none(self):
        expected = None
        actual = commons.load_settings('./tests/lib/dummy/settings.ini')
        self.assertEqual(expected, actual)

    def test_if_settings_file_exists_then_it_must_return_correct_config_values(self):
        loaded = commons.load_settings('./tests/lib/test-settings.ini')

        expected_org_name = 'dummy_org_name'
        expected_pat = 'dummy_pat'
        actual_org_name = loaded['org']['name']
        actual_pat = loaded['org']['pat']

        self.assertEqual(expected_org_name, actual_org_name)
        self.assertEqual(expected_pat, actual_pat)

    def test_if_settings_file_exists_but_does_not_contain_correct_values_it_must_return_none(self):
        expected = None
        actual = commons.load_settings('./tests/lib/settings2.ini')
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()