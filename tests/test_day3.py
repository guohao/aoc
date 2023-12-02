import unittest
from unittest import TestCase

from common import io_utils
from day3 import Day3


class TestDay2(TestCase):
    def test_part_one(self):
        data = """
        """
        lines = io_utils.raw_str_to_lines(data)
        self.assertEqual(Day3().part_one(lines), 8)

    def test_part_two(self):
        data = """
                """
        lines = io_utils.raw_str_to_lines(data)
        self.assertEqual(Day3().part_two(lines), 2286)


if __name__ == '__main__':
    unittest.main()
