__author__ = 'nick'

import unittest
from min import minimum_x


@minimum_x(6)
def _test(arg):
    print arg
    return arg


class TestMinDecorator(unittest.TestCase):

    def setUp(self):
        pass

    def test_decorator(self):
        arg = _test(6)
        self.assertEqual(arg, 6)
        arg = _test(7)
        self.assertEqual(arg, 7)

    def _test_raises_exception(self):
        return _test(5)

    def test_raises_exception(self):
        with self.assertRaises(ValueError):
            self._test_raises_exception()

if __name__ == "__main__":
    unittest.main()
