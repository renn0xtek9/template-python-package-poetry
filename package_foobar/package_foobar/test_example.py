"""Example of unittest file"""

import unittest

from .example import return_two


class TestReturnTwo(unittest.TestCase):
    def test_return_two(self):
        self.assertEqual(2, return_two())
