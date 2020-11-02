import unittest
from azdocli.lib import commons


class TestCommons(unittest.TestCase):

    def test_load_config(self):
        expected = None
        actual = commons.load_settings('./tests/lib/settings.ini')
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()