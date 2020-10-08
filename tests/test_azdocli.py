import unittest
from azdocli import azdocli


class TestAzdoCli(unittest.TestCase):

    def test_foo(self):
        self.assertTrue(azdocli.foo())


if __name__ == '__main__':
    unittest.main()