import unittest
from unittest.mock import patch

from helpers import get_input


class TestHelpers(unittest.TestCase):
    def test_get_input(self):
        user_input = ['', 3]

        with patch('builtins.input', side_effect=user_input):
            self.assertEqual(42, get_input('foo', 42))
            self.assertEqual(3, get_input('foo', 42))
