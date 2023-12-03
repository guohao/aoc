import unittest
from unittest import TestCase

from common import io_utils
from day4 import Day4


class TestDay4(TestCase):
    def test_part_one(self):
        data = """
        """
        lines = io_utils.raw_str_to_lines(data)
        self.assertEqual(Day4().part_one(lines), 4361)

    def test_part_two(self):
        data = """
                """
        lines = io_utils.raw_str_to_lines(data)
        self.assertEqual(Day4().part_two(lines), 467835)


if __name__ == '__main__':
    unittest.main()
