import unittest

from click.testing import CliRunner


class TestIntegrationProject(unittest.TestCase):
    def test_foobar(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()