import unittest
from unittest import TestCase

from common import io_utils
from day3 import Day3


class TestDay3(TestCase):
    def test_part_one(self):
        data = """
        467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.
        """
        lines = io_utils.raw_str_to_lines(data)
        self.assertEqual(Day3().part_one(lines), 4361)

    def test_part_two(self):
        data = """
        467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
                """
        lines = io_utils.raw_str_to_lines(data)
        self.assertEqual(Day3().part_two(lines), 467835)


if __name__ == '__main__':
    unittest.main()
